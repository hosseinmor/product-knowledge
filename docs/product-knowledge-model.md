# Simplified Product Knowledge Model

## Product Group

A Product Group is the stable umbrella that contains related products under one brand or suite.

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

A Product Group overview owns the group purpose, products, major relationships, shared journeys, important shared concepts and services, and group-level documentation gaps.

Path:

```text
products/{group}/overview.md
```

## Product Overview

One overview per product. It explains purpose, users, boundaries, main Product Areas, major journeys, integrations, and documentation gaps.

Path:

```text
products/{group}/{product}/overview.md
```

## Product Area

A Product Area is a meaningful and relatively independent part of a product that supports one coherent outcome or a closely related set of outcomes.

It owns product-specific users, outcomes, entry points, concepts, flows, rules, permissions, states, validations, edge cases, variations, unknowns, and evidence.

A Product Area is not just a page, component, modal, Jira Epic, team, service, or one requested change.

Path:

```text
products/{group}/{product}/areas/{area}.md
```

Keep flows inside the Product Area by default. Split a large area only when one document becomes difficult to understand or maintain:

```text
products/{group}/{product}/areas/{area}/
├── overview.md
└── flows/
    ├── create.md
    ├── submit.md
    └── approve.md
```

Flow files are optional, not required.

## Shared Product Concept

A Shared Product Concept contains a business definition, data model, lifecycle, or rule that has the same meaning in more than one product.

Path:

```text
shared/product-concepts/{concept}.md
```

Shared Product Concepts do not own product-specific user experience.

Implemented example:

```text
shared/product-concepts/job-post.md
→ shared definition and cross-product questions

products/jobvision/employer/areas/job-post-management.md
→ Employer-side creation and management

products/jobvision/candidate/areas/job-post-experience.md
→ Candidate-side understanding and actions
```

Create a fully shared Product Area only when outcomes, behavior, rules, ownership, and flows are genuinely the same across products. This should be uncommon.

## Shared Product Service

A Shared Product Service is a durable service consumed by more than one product. The owning team is metadata, not the repository hierarchy.

```text
shared/product-services/{service-group}/overview.md
shared/product-services/{service-group}/services/{service}.md
```

For AI services:

```text
shared/product-services/ai/overview.md
shared/product-services/ai/services/{service}.md
```

Use this split:

```text
Cross-product service behavior
→ Shared Product Service

Product-specific use, flow, threshold, permission, fallback, and presentation
→ The consuming Product Area

Reusable interaction UI
→ Design System
```

The AI product team may be the `owner` of a service. It is not a product unless it later owns a distinct user-facing product with its own users and boundary.

## Design System

The Design System remains a complete and independent knowledge structure under:

```text
shared/design-system/
```

Its internal structure is unchanged by this model.

## Lightweight retrieval metadata

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

The Design System keeps its existing metadata. The manifest generator normalizes it into the common retrieval index.

## AI retrieval manifest

`manifest.generated.json` helps AI find documents by group, product, kind, title, summary, topics, and related IDs.

Recommended sequence:

```text
1. Read README.md and manifest.generated.json.
2. Select the relevant Product Group and Product Overview.
3. Select only the necessary Product Areas and Shared Product Concepts.
4. Add relevant Shared Product Services.
5. For design tasks, add relevant Design System and content documents.
6. Follow related IDs only when they materially affect the task.
```

## Status and ownership

```text
Draft
→ Incomplete or awaiting owner review

Reviewed
→ Reviewed by the named owner and usable as current team context
```

A reviewed document may still contain explicit unknowns or untested behavior.

## Update rule

AI may identify a gap and propose an exact update. A named owner reviews and applies it through a normal branch and pull request.

After indexed documents change, regenerate `manifest.generated.json` and include it in the same pull request.
