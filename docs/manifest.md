# Lightweight Retrieval Manifest

`manifest.generated.json` is a generated index for AI retrieval. It is not a Product Knowledge document and does not add a team workflow.

The active knowledge model remains:

```text
Product Group Overview
Product Overview
Product Area
Shared Product Concept
Shared Product Service
Design System
```

The manifest helps AI find the smallest relevant set of files without scanning the whole repository or guessing from filenames.

## Manifest fields

Each entry contains:

```text
id
kind
group when relevant
product when relevant
title
summary
status
owner
last_reviewed
related IDs
topics
path
```

Example:

```json
{
  "id": "cando.ats.recruitment-request",
  "kind": "product-area",
  "group": "cando",
  "product": "ats",
  "title": "Recruitment Request",
  "summary": "Explains how Cando ATS creates, submits, approves, rejects, resubmits, and fulfills an internal hiring request.",
  "status": "draft",
  "owner": "ATS product team",
  "last_reviewed": null,
  "related": ["cando.ats.overview", "cando.ats.approval-workflow"],
  "topics": ["approval-workflow", "hiring-capacity", "recruitment-request"],
  "path": "products/cando/ats/areas/recruitment-request.md"
}
```

## Supported knowledge kinds

```text
product-group-overview
product-overview
product-area
product-area-flow
shared-product-concept
shared-product-service-overview
shared-product-service
content-guideline
product-standard
```

Design System documents are normalized as:

```text
design-system-{existing type}
```

The Design System keeps its existing structure and metadata. The generator only normalizes that metadata into the retrieval manifest.

### Design System ownership defaults

The manifest may resolve a narrowly defined collection owner when Design System governance explicitly defines one.

Current rule:

```text
shared/design-system/accessibility/**
→ Design System team
```

An explicit document-level `owner` overrides the collection default. This keeps operational accessibility documents from appearing ownerless without requiring the same owner string to be repeated in every file.

Do not add new inferred-owner rules merely for convenience; they require a corresponding canonical governance decision.

## Required lightweight frontmatter

Product Group Overview, Product Overview, Product Area, Shared Product Concept, and Shared Product Service documents use:

```yaml
---
id:
kind:
group:
product:
title:
summary:
status: draft | reviewed
owner:
last_reviewed:
related: []
topics: []
---
```

`group` and `product` are used only when relevant. `summary`, `topics`, and `related` are retrieval aids and should not duplicate the full document.

## Retrieval sequence

```text
1. Read README.md and manifest.generated.json.
2. Filter by group, product, kind, title, summary, and topics.
3. Read the relevant Product Group and Product Overview.
4. Read only the required Product Areas and Shared Product Concepts.
5. Add relevant Shared Product Services.
6. For design work, add relevant Design System and content documents.
7. Follow related IDs only when they materially affect the task.
```

AI should not read the entire repository by default.

## Commands

```bash
python -m pip install -r requirements-dev.txt
python scripts/generate_manifest.py generate
python scripts/generate_manifest.py check
python scripts/generate_manifest.py report
```

## Validation scope

The lightweight check validates retrieval integrity:

- Indexed Markdown files have parseable frontmatter.
- `id`, `title`, and `summary` exist.
- IDs are unique.
- Product Group documents identify their group.
- Product documents identify their group and product.
- `related` IDs resolve.
- Dates use `YYYY-MM-DD` when present.
- The committed manifest matches current documents.

It does not validate product semantics, release state, or delivery workflows.
