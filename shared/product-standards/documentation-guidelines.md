---
id: standard.documentation-guidelines
title: Documentation Guidelines
summary: Defines Product Group, Product, Product Area, Shared Product Concept, Shared Product Service, status, ownership, and manifest maintenance rules.
status: reviewed
owner: Product Knowledge owner
last_reviewed: 2026-07-27
related:
  - jobvision.overview
  - kando.overview
  - shared.ai-services.overview
topics:
  - product-knowledge
  - documentation
  - product-group
  - product-area
  - shared-service
  - manifest
---

# Documentation Guidelines

## Active document types

The active Product Knowledge model uses:

```text
Product Group Overview
Product Overview
Product Area
Shared Product Concept
Shared Product Service
```

The Design System keeps its own complete document structure under `shared/design-system/`.

PRDs live in Jira. A separate Brief document is not required.

## Product Group Overview

Use one overview per stable product group to document:

- Group purpose and boundary
- Products inside the group
- Major relationships and shared journeys
- Important shared concepts and services
- Group-level documentation gaps

Path:

```text
products/{group}/overview.md
```

Current groups:

```text
Jobvision
→ Candidate
→ Employer

Kando
→ ATS
→ Pulse
→ Onboarding
→ Learning
```

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
products/{group}/{product}/overview.md
```

## Product Area

A Product Area is a meaningful and relatively independent part of a product that combines related outcomes, flows, rules, permissions, states, validations, and edge cases.

A Product Area is not just a page, modal, component, Jira item, team, service, or one requested change.

Keep flows inside the Product Area document by default. Split them into separate files only when the area becomes too large to understand or maintain.

Path:

```text
products/{group}/{product}/areas/{area}.md
```

## Shared Product Concept

Use a Shared Product Concept only when a business definition, data model, lifecycle, or rule has the same meaning across more than one product.

Product-specific behavior stays in the relevant Product Area. Reusable UI behavior stays in the Design System.

Path:

```text
shared/product-concepts/{concept}.md
```

## Shared Product Service

Use a Shared Product Service when a durable service is consumed by more than one product.

The team that owns the service is metadata, not the repository hierarchy. For example, the AI product team owns shared AI services but is not a Product alongside Candidate, Employer, ATS, Pulse, Onboarding, or Learning.

Path:

```text
shared/product-services/{service-group}/overview.md
shared/product-services/{service-group}/services/{service}.md
```

Rules:

```text
Cross-product AI service behavior
→ shared/product-services/ai/

Product-specific use, flow, permission, threshold, and presentation
→ the relevant Product Area

Reusable AI interaction UI
→ Design System
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

Product Group Overview, Product Overview, Product Area, Shared Product Concept, and Shared Product Service documents use:

```yaml
id:
kind:
group: # for Product Groups and product documents
product: # for product documents
title:
summary:
status:
owner:
last_reviewed:
related: []
topics: []
```

The metadata helps AI find the smallest relevant context. It does not add Capability, Domain, Decision, release, or handoff workflows.

## Writing principles

- Describe current product behavior and known rules.
- Keep assumptions, unknowns, variations, and untested behavior visible.
- Do not copy the same behavior into several documents.
- Put shared definitions in Shared Product Concepts.
- Put cross-product service behavior in Shared Product Services.
- Put product-specific behavior in Product Areas.
- Add source links such as Jira, Figma, research, analytics, model documentation, or walkthrough evidence.
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
