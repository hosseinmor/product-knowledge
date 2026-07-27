---
id: standard.documentation-guidelines
title: Documentation Guidelines
summary: Defines the active Product Overview, Product Area, Shared Product Concept, status, ownership, and manifest maintenance rules.
status: reviewed
owner: Product Knowledge owner
last_reviewed: 2026-07-27
related: []
topics:
  - product-knowledge
  - documentation
  - product-area
  - manifest
---

# Documentation Guidelines

## Active document types

The active Product Knowledge model uses:

```text
Product Overview
Product Area
Shared Product Concept
```

The Design System keeps its own complete document structure under `shared/design-system/`.

PRDs live in Jira. A separate Brief document is not required.

## Product Overview

Use one overview per product to document:

- Purpose
- Primary users
- Product boundaries
- Main Product Areas
- Major journeys
- Integrations
- Documentation gaps

Path:

```text
products/{product}/overview.md
```

## Product Area

A Product Area is a meaningful and relatively independent part of a product that combines related outcomes, flows, rules, permissions, states, validations, and edge cases.

A Product Area is not just a page, modal, component, Jira item, team, or one requested change.

Keep flows inside the Product Area document by default. Split them into separate files only when the area becomes too large to understand or maintain.

Path:

```text
products/{product}/areas/{area}.md
```

## Shared Product Concept

Use a Shared Product Concept only when a business definition, data model, lifecycle, or rule has the same meaning across more than one product.

Product-specific behavior stays in the relevant Product Area. Reusable UI behavior stays in the Design System.

Path:

```text
shared/product-concepts/{concept}.md
```

## Status and ownership

Use only:

```text
status: draft | reviewed
owner: person or team
last_reviewed: YYYY-MM-DD
```

- `draft` means incomplete or awaiting owner review.
- `reviewed` means the named owner considers the document usable as current team context.

A reviewed document may still contain explicit unknowns or untested behavior.

## Lightweight retrieval metadata

Product Overview, Product Area, and Shared Product Concept documents use:

```yaml
id:
kind:
product: # only for product documents
title:
summary:
status:
owner:
last_reviewed:
related: []
topics: []
```

The metadata helps AI find the smallest relevant context. It does not add new Product Knowledge document types or team workflows.

## Writing principles

- Describe current product behavior and known rules.
- Keep assumptions, unknowns, variations, and untested behavior visible.
- Do not copy the same behavior into several documents.
- Put shared definitions in Shared Product Concepts and product-specific behavior in Product Areas.
- Add source links such as Jira, Figma, research, analytics, or walkthrough evidence.
- Use a specific summary and useful topics so AI can retrieve the document correctly.
- Use clear headings and direct language.

## Updating knowledge

AI may propose exact document changes. The named owner reviews and applies them through a normal branch and pull request.

After an indexed document changes:

```bash
python scripts/generate_manifest.py generate
python scripts/generate_manifest.py check
```

The generated manifest is a technical retrieval index. No release handoff or automated synchronization is required in the active model.
