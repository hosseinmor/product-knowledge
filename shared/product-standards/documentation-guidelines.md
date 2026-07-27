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
Status: Draft | Reviewed
Owner: person or team
Last reviewed: date
```

- `Draft` means incomplete or awaiting owner review.
- `Reviewed` means the named owner considers the document usable as current team context.

A Reviewed document may still contain explicit unknowns or untested behavior.

## Writing principles

- Describe current product behavior and known rules.
- Keep assumptions, unknowns, variations, and untested behavior visible.
- Do not copy the same behavior into several documents.
- Put shared definitions in Shared Product Concepts and product-specific behavior in Product Areas.
- Add source links such as Jira, Figma, research, analytics, or walkthrough evidence.
- Use clear headings and direct language so humans and AI can retrieve the relevant context.

## Updating knowledge

AI may propose exact document changes. The named owner reviews and applies them through a normal branch and pull request.

No manifest, special metadata schema, release handoff, or automated synchronization is required in the active model.
