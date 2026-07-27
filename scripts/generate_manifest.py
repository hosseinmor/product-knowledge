#!/usr/bin/env python3
"""Generate and validate the lightweight AI retrieval manifest."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "PyYAML is required. Run: python -m pip install -r requirements-dev.txt"
    ) from exc

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "manifest.generated.json"
INDEX_ROOTS = (
    ROOT / "products",
    ROOT / "shared" / "product-concepts",
    ROOT / "shared" / "design-system",
    ROOT / "shared" / "content",
    ROOT / "shared" / "product-standards",
)
EXCLUDED_FILENAMES = {"README.md"}
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
SLUG_RE = re.compile(r"[^a-z0-9]+")
VALID_STATUS = {"draft", "reviewed"}


@dataclass(frozen=True)
class Finding:
    path: str
    message: str

    def render(self) -> str:
        return f"ERROR {self.path}: {self.message}"


@dataclass
class Document:
    path: Path
    relative_path: str
    metadata: dict[str, Any] | None
    body: str
    parse_error: str | None = None


def iter_markdown() -> Iterable[Path]:
    found: set[Path] = set()
    for root in INDEX_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*.md"):
            if path.name in EXCLUDED_FILENAMES:
                continue
            found.add(path)
    yield from sorted(found, key=lambda item: item.as_posix())


def parse_document(path: Path) -> Document:
    raw = path.read_text(encoding="utf-8")
    relative = path.relative_to(ROOT).as_posix()
    match = FRONTMATTER_RE.match(raw)
    if not match:
        return Document(path, relative, None, raw)

    try:
        loaded = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return Document(path, relative, None, raw[match.end() :], str(exc))

    if loaded is None:
        loaded = {}
    if not isinstance(loaded, dict):
        return Document(
            path,
            relative,
            None,
            raw[match.end() :],
            "Frontmatter must be a YAML mapping.",
        )
    return Document(path, relative, loaded, raw[match.end() :])


def scan_documents() -> list[Document]:
    return [parse_document(path) for path in iter_markdown()]


def slugify(value: str) -> str:
    return SLUG_RE.sub("-", value.lower()).strip("-")


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def as_string_list(value: Any) -> list[str]:
    if value in (None, ""):
        return []
    if not isinstance(value, list):
        raise ValueError("must be a list")
    result: list[str] = []
    for item in value:
        if not nonempty_string(item):
            raise ValueError("must contain only non-empty strings")
        result.append(item.strip())
    return result


def infer_product(path: str, metadata: dict[str, Any]) -> str | None:
    if nonempty_string(metadata.get("product")):
        return str(metadata["product"]).strip()
    parts = Path(path).parts
    if len(parts) >= 2 and parts[0] == "products":
        return parts[1]
    return None


def infer_kind(path: str, metadata: dict[str, Any]) -> str:
    if nonempty_string(metadata.get("kind")):
        return str(metadata["kind"]).strip()

    parts = Path(path).parts
    if parts[0] == "products":
        if parts[-1] == "overview.md" and len(parts) == 3:
            return "product-overview"
        if "areas" in parts:
            return "product-area-flow" if "flows" in parts else "product-area"

    if parts[:2] == ("shared", "product-concepts"):
        return "shared-product-concept"

    if parts[:2] == ("shared", "design-system"):
        doc_type = metadata.get("type")
        if nonempty_string(doc_type):
            return f"design-system-{str(doc_type).strip()}"
        folder = parts[2] if len(parts) > 3 else "overview"
        return f"design-system-{slugify(folder)}"

    if parts[:2] == ("shared", "content"):
        return "content-guideline"

    if parts[:2] == ("shared", "product-standards"):
        return "product-standard"

    raise ValueError("path is outside the supported manifest structure")


def infer_status(metadata: dict[str, Any]) -> str:
    explicit = metadata.get("status")
    if nonempty_string(explicit) and str(explicit).lower() in VALID_STATUS:
        return str(explicit).lower()

    design_status = str(metadata.get("design_status", "")).lower()
    if design_status in {"reviewed", "stable", "approved", "active"}:
        return "reviewed"
    if design_status:
        return "draft"

    maturity = str(metadata.get("document_maturity", "")).lower()
    knowledge_state = str(metadata.get("knowledge_state", "")).lower()
    if maturity in {"reviewed", "stable"} and knowledge_state == "canonical":
        return "reviewed"
    return "draft"


def normalize_date(value: Any) -> str | None:
    if value in (None, ""):
        return None
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, str):
        try:
            return date.fromisoformat(value).isoformat()
        except ValueError as exc:
            raise ValueError("must use YYYY-MM-DD") from exc
    raise ValueError("must use YYYY-MM-DD")


def derive_topics(path: str, metadata: dict[str, Any], kind: str) -> list[str]:
    topics: set[str] = set()
    for field in ("topics", "tags"):
        value = metadata.get(field)
        if value not in (None, ""):
            topics.update(as_string_list(value))

    parts = Path(path).parts
    for part in parts[:-1]:
        if part not in {"products", "shared", "areas", "design-system"}:
            topics.add(part)
    stem = Path(path).stem
    if stem not in {"overview", "STRUCTURE"}:
        topics.add(stem)
    topics.add(kind)
    return sorted(topics)


def normalize_document(doc: Document) -> tuple[dict[str, Any] | None, list[Finding]]:
    findings: list[Finding] = []
    if doc.parse_error:
        return None, [Finding(doc.relative_path, f"Invalid YAML frontmatter: {doc.parse_error}")]
    if doc.metadata is None:
        return None, [Finding(doc.relative_path, "Missing YAML frontmatter.")]

    metadata = doc.metadata
    for field in ("id", "title", "summary"):
        if not nonempty_string(metadata.get(field)):
            findings.append(Finding(doc.relative_path, f"Missing non-empty `{field}`."))

    if findings:
        return None, findings

    try:
        kind = infer_kind(doc.relative_path, metadata)
    except ValueError as exc:
        findings.append(Finding(doc.relative_path, str(exc)))
        return None, findings

    product = infer_product(doc.relative_path, metadata)
    if kind in {"product-overview", "product-area", "product-area-flow"} and not product:
        findings.append(Finding(doc.relative_path, "Product documents require `product`."))

    try:
        related = as_string_list(metadata.get("related", []))
        topics = derive_topics(doc.relative_path, metadata, kind)
        last_reviewed = normalize_date(
            metadata.get("last_reviewed", metadata.get("last_verified"))
        )
    except ValueError as exc:
        findings.append(Finding(doc.relative_path, str(exc)))
        return None, findings

    status = infer_status(metadata)
    if status not in VALID_STATUS:
        findings.append(Finding(doc.relative_path, "Status must be `draft` or `reviewed`."))

    entry: dict[str, Any] = {
        "id": str(metadata["id"]).strip(),
        "kind": kind,
        "title": str(metadata["title"]).strip(),
        "summary": " ".join(str(metadata["summary"]).split()),
        "status": status,
        "owner": str(metadata["owner"]).strip() if nonempty_string(metadata.get("owner")) else None,
        "last_reviewed": last_reviewed,
        "related": related,
        "topics": topics,
        "path": doc.relative_path,
    }
    if product:
        entry["product"] = product

    return entry, findings


def build_manifest(documents: list[Document]) -> tuple[dict[str, Any], list[Finding]]:
    entries: list[dict[str, Any]] = []
    findings: list[Finding] = []
    ids: dict[str, str] = {}

    for doc in documents:
        entry, document_findings = normalize_document(doc)
        findings.extend(document_findings)
        if entry is None:
            continue
        doc_id = entry["id"]
        if doc_id in ids:
            findings.append(
                Finding(doc.relative_path, f"Duplicate ID `{doc_id}` also used by {ids[doc_id]}.")
            )
        else:
            ids[doc_id] = doc.relative_path
        entries.append(entry)

    for entry in entries:
        for related_id in entry["related"]:
            if related_id == entry["id"]:
                findings.append(Finding(entry["path"], "A document cannot relate to itself."))
            elif related_id not in ids:
                findings.append(
                    Finding(entry["path"], f"Related ID `{related_id}` does not exist.")
                )

    entries.sort(key=lambda item: item["id"])
    by_kind = Counter(entry["kind"] for entry in entries)
    by_product = Counter(entry["product"] for entry in entries if "product" in entry)

    manifest = {
        "schema_version": 1,
        "documents": entries,
        "summary": {
            "documents": len(entries),
            "by_kind": dict(sorted(by_kind.items())),
            "by_product": dict(sorted(by_product.items())),
        },
    }
    return manifest, findings


def serialized_manifest(manifest: dict[str, Any]) -> str:
    return json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"


def print_findings(findings: list[Finding]) -> None:
    for finding in sorted(findings, key=lambda item: (item.path, item.message)):
        print(finding.render())
    if findings:
        print(f"\n{len(findings)} error(s)")


def command_generate(_: argparse.Namespace) -> int:
    manifest, findings = build_manifest(scan_documents())
    if findings:
        print_findings(findings)
        return 1
    MANIFEST_PATH.write_text(serialized_manifest(manifest), encoding="utf-8")
    print(f"Generated {MANIFEST_PATH.relative_to(ROOT)} with {manifest['summary']['documents']} documents.")
    return 0


def command_check(_: argparse.Namespace) -> int:
    manifest, findings = build_manifest(scan_documents())
    if findings:
        print_findings(findings)
        return 1
    expected = serialized_manifest(manifest)
    if not MANIFEST_PATH.exists():
        print("ERROR manifest.generated.json: file is missing. Run `python scripts/generate_manifest.py generate`.")
        return 1
    actual = MANIFEST_PATH.read_text(encoding="utf-8")
    if actual != expected:
        print("ERROR manifest.generated.json: file is stale. Run `python scripts/generate_manifest.py generate`.")
        return 1
    print(f"Manifest is current with {manifest['summary']['documents']} documents.")
    return 0


def command_report(_: argparse.Namespace) -> int:
    manifest, findings = build_manifest(scan_documents())
    print(json.dumps(manifest["summary"], ensure_ascii=False, indent=2))
    if findings:
        print_findings(findings)
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("generate").set_defaults(handler=command_generate)
    subparsers.add_parser("check").set_defaults(handler=command_check)
    subparsers.add_parser("report").set_defaults(handler=command_report)
    args = parser.parse_args()
    return args.handler(args)


if __name__ == "__main__":
    sys.exit(main())
