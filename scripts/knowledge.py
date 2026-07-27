#!/usr/bin/env python3
"""Generate and validate Product Knowledge metadata and manifest."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "PyYAML is required. Install requirements-dev.txt before running this script."
    ) from exc

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "manifest.generated.json"

INDEX_ROOTS = (
    ROOT / "products",
    ROOT / "shared" / "design-system",
    ROOT / "shared" / "content",
    ROOT / "shared" / "product-standards",
    ROOT / "shared" / "domains",
)

EXCLUDED_NAMES = {"README.md"}
EXCLUDED_PARTS: set[str] = set()

ALLOWED_TYPES: dict[str, set[str]] = {
    "product": {"product", "capability", "flow", "domain", "decision"},
    "design-system": {
        "overview",
        "foundation",
        "token",
        "component",
        "pattern",
        "experience-rule",
        "accessibility",
        "product-variation",
        "reference",
        "governance",
        "ui-template",
    },
    "content": {"content-guideline"},
    "product-standard": {"product-standard", "documentation-guideline"},
    "shared-domain": {"domain"},
}

KNOWLEDGE_STATES = {"canonical", "observed", "unverified", "deprecated"}
DOCUMENT_MATURITIES = {"scaffold", "draft", "reviewed", "stable"}
COMMON_REQUIRED = {
    "id",
    "collection",
    "type",
    "title",
    "summary",
    "knowledge_state",
    "document_maturity",
    "related",
}
OPTIONAL_MANIFEST_FIELDS = (
    "owner",
    "actors",
    "domains",
    "capabilities",
    "last_verified",
    "source_refs",
    "design_refs",
    "figma_file",
    "figma_node",
    "code_refs",
    "supersedes",
    "superseded_by",
)

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)


@dataclass(frozen=True)
class Finding:
    severity: str
    path: str
    code: str
    message: str

    def render(self) -> str:
        return f"{self.severity.upper():7} {self.path}: [{self.code}] {self.message}"


@dataclass
class ScannedDocument:
    path: Path
    relative_path: str
    metadata: dict[str, Any] | None
    body: str
    parse_error: str | None = None


def iter_indexable_markdown() -> Iterable[Path]:
    paths: set[Path] = set()
    for root in INDEX_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*.md"):
            relative_parts = path.relative_to(ROOT).parts
            if path.name in EXCLUDED_NAMES:
                continue
            if any(part in EXCLUDED_PARTS for part in relative_parts):
                continue
            paths.add(path)
    yield from sorted(paths, key=lambda item: item.as_posix())


def parse_document(path: Path) -> ScannedDocument:
    raw = path.read_text(encoding="utf-8")
    relative = path.relative_to(ROOT).as_posix()
    match = FRONTMATTER_RE.match(raw)
    if not match:
        return ScannedDocument(path, relative, None, raw)

    frontmatter = match.group(1)
    body = raw[match.end() :]
    try:
        loaded = yaml.safe_load(frontmatter)
    except yaml.YAMLError as exc:
        return ScannedDocument(path, relative, None, body, str(exc))

    if loaded is None:
        loaded = {}
    if not isinstance(loaded, dict):
        return ScannedDocument(
            path,
            relative,
            None,
            body,
            "Frontmatter must be a YAML mapping.",
        )
    return ScannedDocument(path, relative, loaded, body)


def scan_documents() -> list[ScannedDocument]:
    return [parse_document(path) for path in iter_indexable_markdown()]


def is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def is_valid_date(value: Any) -> bool:
    if value in (None, ""):
        return True
    if isinstance(value, date):
        return True
    if not isinstance(value, str):
        return False
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


def meaningful_body_text(body: str) -> str:
    lines: list[str] = []
    in_fence = False
    for raw_line in body.splitlines():
        line = raw_line.strip()
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not line or line.startswith("#"):
            continue
        if line in {"---", "-", "*"}:
            continue
        lines.append(line)
    return " ".join(lines)


def classify_unindexed(doc: ScannedDocument) -> tuple[str, str]:
    if doc.parse_error:
        return "invalid-frontmatter", doc.parse_error
    if doc.metadata is None:
        return "missing-frontmatter", "Document has no YAML frontmatter."
    legacy = {"status", "maturity"}.intersection(doc.metadata)
    missing = sorted(COMMON_REQUIRED.difference(doc.metadata))
    if legacy and missing:
        return (
            "legacy-metadata",
            "Uses legacy fields and is missing required metadata: " + ", ".join(missing),
        )
    if missing:
        return "incomplete-metadata", "Missing required metadata: " + ", ".join(missing)
    return "invalid-metadata", "Metadata does not satisfy the repository schema."


def validate_document(doc: ScannedDocument, *, strict: bool) -> list[Finding]:
    findings: list[Finding] = []
    path = doc.relative_path
    if doc.parse_error:
        return [Finding("error", path, "invalid-frontmatter", doc.parse_error)]
    if doc.metadata is None:
        severity = "error" if strict else "warning"
        return [Finding(severity, path, "missing-frontmatter", "Add the common metadata envelope.")]

    metadata = doc.metadata
    if "status" in metadata or "maturity" in metadata:
        severity = "error" if strict else "warning"
        findings.append(
            Finding(
                severity,
                path,
                "legacy-metadata",
                "Replace legacy status/maturity fields with knowledge_state and document_maturity.",
            )
        )

    missing = sorted(COMMON_REQUIRED.difference(metadata))
    if missing:
        severity = "error" if strict else "warning"
        findings.append(
            Finding(
                severity,
                path,
                "missing-required-fields",
                ", ".join(missing),
            )
        )
        return findings

    for field in ("id", "collection", "type", "title", "summary", "knowledge_state", "document_maturity"):
        if not is_nonempty_string(metadata.get(field)):
            findings.append(Finding("error", path, "invalid-field", f"{field} must be a non-empty string."))

    collection = metadata.get("collection")
    doc_type = metadata.get("type")
    if collection not in ALLOWED_TYPES:
        findings.append(
            Finding("error", path, "invalid-collection", f"Unsupported collection: {collection!r}.")
        )
    elif doc_type not in ALLOWED_TYPES[collection]:
        findings.append(
            Finding(
                "error",
                path,
                "invalid-type",
                f"Type {doc_type!r} is not allowed in collection {collection!r}.",
            )
        )

    if metadata.get("knowledge_state") not in KNOWLEDGE_STATES:
        findings.append(
            Finding(
                "error",
                path,
                "invalid-knowledge-state",
                f"Expected one of {sorted(KNOWLEDGE_STATES)}.",
            )
        )
    if metadata.get("document_maturity") not in DOCUMENT_MATURITIES:
        findings.append(
            Finding(
                "error",
                path,
                "invalid-document-maturity",
                f"Expected one of {sorted(DOCUMENT_MATURITIES)}.",
            )
        )

    related = metadata.get("related")
    if not isinstance(related, list) or any(not is_nonempty_string(item) for item in related):
        findings.append(Finding("error", path, "invalid-related", "related must be a list of document IDs."))

    if collection == "product" and not is_nonempty_string(metadata.get("product")):
        findings.append(Finding("error", path, "missing-product", "Product documents require product."))

    if not is_valid_date(metadata.get("last_verified")):
        findings.append(
            Finding("error", path, "invalid-last-verified", "Use an ISO date in YYYY-MM-DD format.")
        )

    body_text = meaningful_body_text(doc.body)
    if metadata.get("knowledge_state") == "canonical" and metadata.get("document_maturity") == "scaffold":
        findings.append(
            Finding("error", path, "canonical-scaffold", "A scaffold cannot be canonical.")
        )
    if metadata.get("knowledge_state") == "canonical" and len(body_text) < 80:
        severity = "error" if strict else "warning"
        findings.append(
            Finding(
                severity,
                path,
                "empty-canonical-document",
                "Canonical documents must contain substantive owned facts.",
            )
        )

    if metadata.get("document_maturity") in {"reviewed", "stable"} and not metadata.get("last_verified"):
        findings.append(
            Finding(
                "warning",
                path,
                "missing-last-verified",
                "Reviewed or stable documents should record last_verified.",
            )
        )

    return findings


def validate_repository(documents: list[ScannedDocument], *, strict: bool) -> list[Finding]:
    findings: list[Finding] = []
    indexed: list[ScannedDocument] = []
    ids: dict[str, str] = {}

    for doc in documents:
        doc_findings = validate_document(doc, strict=strict)
        findings.extend(doc_findings)
        if doc.metadata and COMMON_REQUIRED.issubset(doc.metadata):
            indexed.append(doc)
            doc_id = doc.metadata.get("id")
            if is_nonempty_string(doc_id):
                if doc_id in ids:
                    findings.append(
                        Finding(
                            "error",
                            doc.relative_path,
                            "duplicate-id",
                            f"ID {doc_id!r} is already used by {ids[doc_id]}.",
                        )
                    )
                else:
                    ids[doc_id] = doc.relative_path

    for doc in indexed:
        metadata = doc.metadata or {}
        for related_id in metadata.get("related", []):
            if related_id == metadata.get("id"):
                findings.append(
                    Finding("error", doc.relative_path, "self-related", "A document cannot relate to itself.")
                )
            elif related_id not in ids:
                severity = "error" if strict else "warning"
                findings.append(
                    Finding(
                        severity,
                        doc.relative_path,
                        "unresolved-related-id",
                        f"Related ID {related_id!r} does not resolve in the manifest.",
                    )
                )

    for unwanted in ROOT.rglob(".DS_Store"):
        findings.append(
            Finding("error", unwanted.relative_to(ROOT).as_posix(), "forbidden-file", "Remove .DS_Store files.")
        )

    return sorted(findings, key=lambda item: (item.severity != "error", item.path, item.code))


def metadata_is_indexable(doc: ScannedDocument) -> bool:
    if doc.metadata is None or doc.parse_error:
        return False
    metadata = doc.metadata
    if not COMMON_REQUIRED.issubset(metadata):
        return False
    collection = metadata.get("collection")
    doc_type = metadata.get("type")
    return (
        collection in ALLOWED_TYPES
        and doc_type in ALLOWED_TYPES[collection]
        and metadata.get("knowledge_state") in KNOWLEDGE_STATES
        and metadata.get("document_maturity") in DOCUMENT_MATURITIES
    )


def manifest_entry(doc: ScannedDocument) -> dict[str, Any]:
    metadata = doc.metadata or {}
    entry: dict[str, Any] = {
        "id": metadata["id"],
        "path": doc.relative_path,
        "collection": metadata["collection"],
        "type": metadata["type"],
        "title": metadata["title"],
        "summary": metadata["summary"],
        "knowledge_state": metadata["knowledge_state"],
        "document_maturity": metadata["document_maturity"],
        "related": metadata.get("related", []),
    }
    if metadata.get("product") not in (None, ""):
        entry["product"] = metadata["product"]
    for field in OPTIONAL_MANIFEST_FIELDS:
        value = metadata.get(field)
        if value not in (None, "", []):
            entry[field] = value.isoformat() if isinstance(value, date) else value
    return entry


def build_manifest(documents: list[ScannedDocument]) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    unindexed: list[dict[str, str]] = []
    for doc in documents:
        if metadata_is_indexable(doc):
            entries.append(manifest_entry(doc))
        else:
            reason, detail = classify_unindexed(doc)
            unindexed.append({"path": doc.relative_path, "reason": reason, "detail": detail})

    entries.sort(key=lambda item: item["id"])
    unindexed.sort(key=lambda item: item["path"])
    return {
        "schema_version": 1,
        "documents": entries,
        "unindexed": unindexed,
        "summary": {
            "indexed_documents": len(entries),
            "unindexed_documents": len(unindexed),
        },
    }


def write_manifest(path: Path, manifest: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def print_findings(findings: list[Finding]) -> None:
    if not findings:
        print("Knowledge validation passed with no findings.")
        return
    for finding in findings:
        print(finding.render())
    errors = sum(item.severity == "error" for item in findings)
    warnings = len(findings) - errors
    print(f"\n{errors} error(s), {warnings} warning(s)")


def command_generate(args: argparse.Namespace) -> int:
    documents = scan_documents()
    manifest = build_manifest(documents)
    output = (ROOT / args.output).resolve() if not Path(args.output).is_absolute() else Path(args.output)
    write_manifest(output, manifest)
    print(
        f"Wrote {output.relative_to(ROOT) if output.is_relative_to(ROOT) else output} "
        f"with {manifest['summary']['indexed_documents']} indexed and "
        f"{manifest['summary']['unindexed_documents']} unindexed documents."
    )
    return 0


def command_validate(args: argparse.Namespace) -> int:
    findings = validate_repository(scan_documents(), strict=args.strict)
    print_findings(findings)
    return 1 if any(item.severity == "error" for item in findings) else 0


def command_check(args: argparse.Namespace) -> int:
    documents = scan_documents()
    findings = validate_repository(documents, strict=args.strict)
    print_findings(findings)
    if any(item.severity == "error" for item in findings):
        return 1

    expected = json.dumps(build_manifest(documents), ensure_ascii=False, indent=2) + "\n"
    if not DEFAULT_MANIFEST.exists():
        print("ERROR   manifest.generated.json: [missing-manifest] Run generate and commit the result.")
        return 1
    actual = DEFAULT_MANIFEST.read_text(encoding="utf-8")
    if actual != expected:
        print("ERROR   manifest.generated.json: [stale-manifest] Run generate and commit the result.")
        return 1
    print("Manifest is current.")
    return 0


def command_report(_: argparse.Namespace) -> int:
    documents = scan_documents()
    manifest = build_manifest(documents)
    findings = validate_repository(documents, strict=False)
    errors = sum(item.severity == "error" for item in findings)
    warnings = len(findings) - errors
    print(json.dumps({**manifest["summary"], "errors": errors, "warnings": warnings}, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate = subparsers.add_parser("generate", help="Generate manifest.generated.json")
    generate.add_argument("--output", default="manifest.generated.json")
    generate.set_defaults(handler=command_generate)

    validate = subparsers.add_parser("validate", help="Validate metadata and relationships")
    validate.add_argument("--strict", action="store_true")
    validate.set_defaults(handler=command_validate)

    check = subparsers.add_parser("check", help="Validate and verify the committed manifest")
    check.add_argument("--strict", action="store_true")
    check.set_defaults(handler=command_check)

    report = subparsers.add_parser("report", help="Print repository quality counts")
    report.set_defaults(handler=command_report)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.handler(args)


if __name__ == "__main__":
    sys.exit(main())
