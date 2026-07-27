# Lightweight Retrieval Manifest

`manifest.generated.json` is a generated index for AI retrieval. It is not a Product Knowledge document and does not add a new team workflow.

The active knowledge model remains simple:

```text
Product Group Overview
Product Overview
Product Area
Shared Product Concept
Shared Product Service
Design System
```

The manifest helps AI find the smallest relevant set of files without scanning the whole repository or guessing from filenames.

## What the manifest contains

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
  "id": "kando.ats.recruitment-request",
  "kind": "product-area",
  "group": "kando",
  "product": "ats",
  "title": "Recruitment Request",
  "summary": "Explains how Kando ATS creates, submits, approves, rejects, resubmits, and fulfills an internal hiring request.",
  "status": "draft",
  "owner": "ATS product team",
  "last_reviewed": null,
  "related": ["kando.ats.overview"],
  "topics": ["approval-workflow", "hiring-capacity", "recruitment-request"],
  "path": "products/kando/ats/areas/recruitment-request.md"
}
```

## Supported knowledge kinds

Product knowledge:

```text
product-group-overview
product-overview
product-area
product-area-flow
shared-product-concept
shared-product-service-overview
shared-product-service
```

Shared guidance:

```text
content-guideline
product-standard
```

Design System documents are normalized as:

```text
design-system-{existing type}
```

Examples:

```text
design-system-component
design-system-pattern
design-system-token
design-system-foundation
design-system-accessibility
```

The Design System keeps its existing full structure and metadata. The generator only normalizes that metadata into the lightweight manifest.

## Required lightweight frontmatter

Product Group Overview, Product Overview, Product Area, Shared Product Concept, and Shared Product Service documents use:

```yaml
---
id:
kind:
group: # for Product Groups and product documents
product: # only for product documents
title:
summary:
status: draft | reviewed
owner:
last_reviewed:
related: []
topics: []
---
```

`summary`, `topics`, and `related` are retrieval aids. They should describe the subject, not repeat the document body.

## Retrieval sequence

AI should:

```text
1. Read README.md and manifest.generated.json.
2. Filter by group, product, kind, title, summary, and topics.
3. Read the relevant Product Group and Product Overview.
4. Read only the required Product Areas and Shared Product Concepts.
5. Add relevant Shared Product Services.
6. For design work, add the relevant Design System and content documents.
7. Follow related IDs only when they materially affect the task.
```

AI should not read the entire repository by default.

## Commands

Install the lightweight tooling dependency:

```bash
python -m pip install -r requirements-dev.txt
```

Generate the manifest:

```bash
python scripts/generate_manifest.py generate
```

Validate metadata, IDs, relationships, and manifest freshness:

```bash
python scripts/generate_manifest.py check
```

Show counts by kind, group, and product:

```bash
python scripts/generate_manifest.py report
```

## Validation scope

The lightweight check validates only retrieval integrity:

- Every indexed Markdown file has parseable frontmatter.
- `id`, `title`, and `summary` exist.
- IDs are unique.
- Product Group documents identify their group.
- Product documents identify their group and product.
- `related` IDs resolve.
- Dates use `YYYY-MM-DD` when present.
- The committed manifest matches current documents.

It does not validate product semantics, release state, canonical ownership, or delivery workflows.
