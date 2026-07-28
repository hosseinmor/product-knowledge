---
id: standard.documentation-guidelines
title: Documentation Guidelines
summary: Defines Product Group, Product, Product Area, Shared Product Concept, Shared Product Service, status, ownership, and manifest maintenance rules.
status: reviewed
owner: Product Knowledge owner
last_reviewed: 2026-07-28
related:
  - jobvision.overview
  - cando.overview
  - shared.job-post
  - shared.ai-services.overview
topics:
  - product-knowledge
  - documentation
  - product-group
  - product-area
  - shared-concept
  - shared-service
  - manifest
---

# Documentation Guidelines

## Active document types

```text
Product Group Overview
Product Overview
Product Area
Shared Product Concept
Shared Product Service
```

The Design System keeps its complete structure under `shared/design-system/`.

PRDs live in Jira. A separate Brief document is not required.

## Product Group Overview

Use one overview per stable product group to document purpose, boundary, included products, major relationships, shared journeys, important shared concepts and services, and group-level gaps.

```text
products/{group}/overview.md
```

Current groups:

```text
Jobvision
→ Candidate
→ Employer

Cando
→ ATS
→ Pulse
→ Onboarding
→ Learning
```

## Product Overview

Use one overview per product to document purpose, users, boundaries, main Product Areas, major journeys, integrations, and gaps.

```text
products/{group}/{product}/overview.md
```

## Product Area

A Product Area is a meaningful and relatively independent part of a product that combines related outcomes, flows, rules, permissions, states, validations, and edge cases.

A Product Area is not just a page, modal, component, Jira item, team, service, or one requested change.

Keep flows inside the Product Area by default. Split them only when the area becomes too large to understand or maintain.

```text
products/{group}/{product}/areas/{area}.md
```

## Shared Product Concept

Use a Shared Product Concept only when a business definition, data model, lifecycle, or rule has the same meaning across more than one product.

Product-specific behavior stays in the relevant Product Area. Reusable UI behavior stays in the Design System.

```text
shared/product-concepts/{concept}.md
```

Implemented example:

```text
shared/product-concepts/job-post.md
products/jobvision/employer/areas/job-post-management.md
products/jobvision/candidate/areas/job-post-experience.md
```

## Shared Product Service

Use a Shared Product Service when a durable service is consumed by more than one product.

The team that owns the service is metadata, not the repository hierarchy. The AI product team may own shared AI services but is not a Product alongside Candidate, Employer, ATS, Pulse, Onboarding, or Learning.

```text
shared/product-services/{service-group}/overview.md
shared/product-services/{service-group}/services/{service}.md
```

Placement rules:

```text
Cross-product service behavior
→ Shared Product Service

Product-specific use, flow, permission, threshold, fallback, and presentation
→ the relevant Product Area

Reusable interaction UI
→ Design System
```

## Status and ownership

```text
status: draft | reviewed
owner: person or team
last_reviewed: YYYY-MM-DD
```

- `draft` means incomplete or awaiting owner review.
- `reviewed` means the named owner considers the document usable as current team context.
- A reviewed document may still contain explicit unknowns or untested behavior.

## Lightweight retrieval metadata

Product Group Overview, Product Overview, Product Area, Shared Product Concept, and Shared Product Service documents use:

```yaml
id:
kind:
group:
product:
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

- Describe current behavior and known rules.
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
