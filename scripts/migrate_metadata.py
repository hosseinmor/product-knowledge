#!/usr/bin/env python3
"""Migrate indexable Markdown documents to the common metadata envelope."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

from knowledge import (
    DOCUMENT_MATURITIES,
    KNOWLEDGE_STATES,
    ScannedDocument,
    meaningful_body_text,
    scan_documents,
)

H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
SLUG_RE = re.compile(r"[^a-z0-9]+")

PRODUCT_FOLDER_TYPES = {
    "capabilities": "capability",
    "flows": "flow",
    "domains": "domain",
    "decisions": "decision",
}

DESIGN_SYSTEM_FOLDER_TYPES = {
    "accessibility": "accessibility",
    "components": "component",
    "experience-rules": "experience-rule",
    "foundations": "foundation",
    "governance": "governance",
    "integrations": "reference",
    "patterns": "pattern",
    "product-variations": "product-variation",
    "tokens": "token",
}

GENERIC_SUMMARIES = {
    "product": "Overview of the product, its users, boundaries, capabilities, and major journeys.",
    "capability": "Describes a durable product ability and its current boundaries.",
    "flow": "Describes one concrete product behavior from trigger to outcome.",
    "domain": "Defines stable concepts, rules, permissions, relationships, and lifecycle constraints.",
    "decision": "Records durable rationale for an approved decision.",
    "overview": "Overview of the shared Design System and its structure.",
    "foundation": "Defines a reusable Design System foundation.",
    "token": "Defines Design System token architecture or usage guidance.",
    "component": "Defines a reusable Design System component and its usage rules.",
    "pattern": "Defines a reusable interaction or composition pattern.",
    "experience-rule": "Defines a reusable experience rule across products.",
    "accessibility": "Defines accessibility guidance for the shared Design System.",
    "product-variation": "Defines controlled product-specific Design System variation.",
    "reference": "Defines a Design System integration or source-of-truth reference.",
    "governance": "Defines Design System governance and maintenance rules.",
    "ui-template": "Defines a reusable Design System UI template.",
    "content-guideline": "Defines shared content guidance across products.",
    "product-standard": "Defines a shared product standard.",
    "documentation-guideline": "Defines shared documentation rules.",
}

COMMON_KEYS = {
    "id",
    "collection",
    "type",
    "product",
    "title",
    "summary",
    "knowledge_state",
    "document_maturity",
    "related",
    "owner",
    "last_verified",
}
LEGACY_KEYS = {"status", "maturity", "scope"}


def slugify(value: str) -> str:
    slug = SLUG_RE.sub("-", value.lower()).strip("-")
    return slug or "document"


def infer_collection_and_type(path: str) -> tuple[str, str, str | None]:
    parts = Path(path).parts
    if parts[0] == "products":
        product = parts[1]
        if parts[-1] == "product-overview.md":
            return "product", "product", product
        folder = parts[2]
        if folder not in PRODUCT_FOLDER_TYPES:
            raise ValueError(f"Unsupported product folder for {path}: {folder}")
        return "product", PRODUCT_FOLDER_TYPES[folder], product

    if parts[:2] == ("shared", "design-system"):
        if parts[-1] in {"overview.md", "STRUCTURE.md"}:
            return "design-system", "overview", None
        folder = parts[2]
        if folder not in DESIGN_SYSTEM_FOLDER_TYPES:
            raise ValueError(f"Unsupported Design System folder for {path}: {folder}")
        return "design-system", DESIGN_SYSTEM_FOLDER_TYPES[folder], None

    if parts[:2] == ("shared", "content"):
        return "content", "content-guideline", None

    if parts[:2] == ("shared", "product-standards"):
        if parts[-1] == "documentation-guidelines.md":
            return "product-standard", "documentation-guideline", None
        return "product-standard", "product-standard", None

    if parts[:2] == ("shared", "domains"):
        return "shared-domain", "domain", None

    raise ValueError(f"Cannot infer collection and type for {path}")


def first_h1(body: str) -> str | None:
    match = H1_RE.search(body)
    return match.group(1).strip() if match else None


def title_from_path(path: str) -> str:
    stem = Path(path).stem
    if stem == "STRUCTURE":
        return "Design System Structure"
    return stem.replace("-", " ").replace("_", " ").title()


def first_summary_paragraph(body: str) -> str | None:
    in_fence = False
    paragraph: list[str] = []
    for raw in body.splitlines():
        line = raw.strip()
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not line:
            if paragraph:
                break
            continue
        if line.startswith("#") or line.startswith("|") or line.startswith("-") or line.startswith("*"):
            if paragraph:
                break
            continue
        paragraph.append(line)
    if not paragraph:
        return None
    value = " ".join(paragraph)
    return value[:237] + "..." if len(value) > 240 else value


def generated_id(path: str, collection: str, doc_type: str, product: str | None) -> str:
    stem = slugify(Path(path).stem)
    if collection == "product":
        if doc_type == "product":
            return product or stem
        return f"{product}.{doc_type}.{stem}"
    if collection == "design-system":
        if doc_type == "overview" and Path(path).name == "overview.md":
            return "design-system.overview"
        if doc_type == "overview":
            return "design-system.structure"
        return f"design-system.{doc_type}.{stem}"
    if collection == "content":
        return f"content.{stem}"
    if collection == "product-standard":
        return f"standard.{stem}"
    if collection == "shared-domain":
        return f"shared-domain.{stem}"
    raise ValueError(collection)


def map_knowledge_state(existing: dict[str, Any], body: str) -> str:
    substantive = len(meaningful_body_text(body)) >= 80
    current = existing.get("knowledge_state")
    if current in KNOWLEDGE_STATES:
        if current == "canonical" and not substantive:
            return "unverified"
        return current

    legacy = str(existing.get("status", "")).strip().lower()
    if legacy in {"deprecated", "archived"}:
        return "deprecated"
    if legacy in {"active", "approved", "stable"} and substantive:
        return "canonical"
    return "unverified"


def map_document_maturity(existing: dict[str, Any], body: str, knowledge_state: str) -> str:
    substantive = len(meaningful_body_text(body)) >= 80
    if not substantive:
        return "scaffold"

    current = existing.get("document_maturity")
    if current in DOCUMENT_MATURITIES and current != "scaffold":
        return current

    legacy_status = str(existing.get("status", "")).strip().lower()
    if knowledge_state == "canonical" or legacy_status in {"active", "approved", "stable"}:
        return "reviewed"
    return "draft"


def normalized_related(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(item).strip() for item in value if str(item).strip()]


def build_metadata(doc: ScannedDocument) -> dict[str, Any]:
    existing = dict(doc.metadata or {})
    collection, doc_type, product = infer_collection_and_type(doc.relative_path)
    title = str(existing.get("title") or first_h1(doc.body) or title_from_path(doc.relative_path)).strip()
    summary = str(
        existing.get("summary")
        or first_summary_paragraph(doc.body)
        or GENERIC_SUMMARIES[doc_type]
    ).strip()
    knowledge_state = map_knowledge_state(existing, doc.body)
    document_maturity = map_document_maturity(existing, doc.body, knowledge_state)

    metadata: dict[str, Any] = {
        "id": str(existing.get("id") or generated_id(doc.relative_path, collection, doc_type, product)),
        "collection": collection,
        "type": doc_type,
    }
    if product:
        metadata["product"] = product
    metadata.update(
        {
            "title": title,
            "summary": summary,
            "knowledge_state": knowledge_state,
            "document_maturity": document_maturity,
            "related": normalized_related(existing.get("related")),
        }
    )

    if existing.get("owner") not in (None, ""):
        metadata["owner"] = existing["owner"]
    if existing.get("last_verified") not in (None, ""):
        metadata["last_verified"] = existing["last_verified"]

    if collection == "design-system":
        if existing.get("status") not in (None, ""):
            metadata["design_status"] = existing["status"]
        if existing.get("maturity") not in (None, ""):
            metadata["design_maturity"] = existing["maturity"]

    for key, value in existing.items():
        if key in COMMON_KEYS or key in LEGACY_KEYS:
            continue
        if key in metadata:
            continue
        metadata[key] = value

    return metadata


def render_document(metadata: dict[str, Any], body: str) -> str:
    dumped = yaml.safe_dump(
        metadata,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    ).rstrip()
    return f"---\n{dumped}\n---\n\n{body.lstrip()}"


def main() -> int:
    changed = 0
    generated_ids: dict[str, str] = {}
    documents = scan_documents()
    rendered: list[tuple[ScannedDocument, dict[str, Any], str]] = []

    for doc in documents:
        metadata = build_metadata(doc)
        doc_id = metadata["id"]
        if doc_id in generated_ids:
            raise SystemExit(
                f"Duplicate generated ID {doc_id!r}: {generated_ids[doc_id]} and {doc.relative_path}"
            )
        generated_ids[doc_id] = doc.relative_path
        rendered.append((doc, metadata, render_document(metadata, doc.body)))

    for doc, _, output in rendered:
        current = doc.path.read_text(encoding="utf-8")
        if current == output:
            continue
        doc.path.write_text(output, encoding="utf-8")
        changed += 1
        print(f"Migrated {doc.relative_path}")

    print(f"Migrated {changed} document(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
