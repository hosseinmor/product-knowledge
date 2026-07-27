# Simplified Product Knowledge Model

## Product Group

A Product Group is the stable umbrella that contains related products under one brand or suite.

Current Product Groups:

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

A Product Group overview owns only:

- Group purpose and boundary
- Products inside the group
- Major relationships between products
- Shared journeys at group level
- Important shared concepts and services
- Group-level documentation gaps

It does not own detailed product flows, permissions, states, or UI behavior.

Path:

```text
products/{group}/overview.md
```

## Product Overview

One overview per product. It explains:

- Product purpose
- Primary users
- Problems the product solves
- Product boundaries
- Main Product Areas
- Major journeys
- Important integrations
- Known documentation gaps

Path:

```text
products/{group}/{product}/overview.md
```

## Product Area

A Product Area is a meaningful and relatively independent part of a product that supports one coherent outcome or closely related set of outcomes.

A Product Area usually contains several related flows and owns the product-specific explanation of:

- Users and roles
- Outcomes
- Entry points
- Main concepts
- Main flows
- Rules
- Permissions
- States and transitions
- Validations
- Edge cases
- Relationships with other areas
- Variations
- Unknowns and evidence

A Product Area is not just a page, component, modal, Jira Epic, team, service, or one requested change.

Path:

```text
products/{group}/{product}/areas/{area}.md
```

### Splitting a large area

Keep flows in one Product Area document by default. Split only when the document becomes hard to understand or maintain:

```text
products/{group}/{product}/areas/{area}/
├── overview.md
└── flows/
    ├── create.md
    ├── submit.md
    └── approve.md
```

Flow files are an optional extension, not a required document type.

## Shared Product Concept

A Shared Product Concept contains a business definition, data model, lifecycle, or rule that has the same meaning in more than one product.

Path:

```text
shared/product-concepts/{concept}.md
```

Shared Product Concepts do not own product-specific user experience.

Example:

```text
shared/product-concepts/job-post.md
→ shared definition, common fields, shared lifecycle, shared rules

products/jobvision/employer/areas/job-post-management.md
→ create, edit, publish, pause, close, and manage

products/jobvision/candidate/areas/job-post-experience.md
→ view, understand, save, share, evaluate, and apply
```

Create a fully shared Product Area only when outcomes, behavior, rules, ownership, and flows are genuinely the same across products. This should be uncommon.

## Shared Product Service

A Shared Product Service is a durable product capability consumed by more than one product. It may be delivered by a platform, data, or AI team, but the organizational team is not the knowledge hierarchy.

Path:

```text
shared/product-services/{service-group}/overview.md
shared/product-services/{service-group}/services/{service}.md
```

For AI:

```text
shared/product-services/ai/overview.md
shared/product-services/ai/services/{service}.md
```

Use this split:

```text
Cross-product AI service behavior
→ Shared Product Service

How one product uses and presents the service
→ That product's Product Area

Reusable AI interaction UI
→ Design System Component or Pattern
```

For example, a shared fit model may document common inputs, outputs, quality, confidence, limitations, and fallback expectations. Candidate, Employer, ATS, or another product still documents its own user-facing flow, thresholds, permissions, copy, and presentation.

The AI product team can appear as `owner` of a service. It should not be added as a product alongside Candidate, Employer, ATS, Pulse, Onboarding, or Learning unless it later owns a distinct user-facing product with its own users and product boundary.

## Design System

The Design System remains a complete and independent knowledge structure under:

```text
shared/design-system/
```

It owns reusable UI foundations, tokens, components, patterns, accessibility rules, product variations, references, templates, and governance.

## Lightweight retrieval metadata

Product Group Overview, Product Overview, Product Area, Shared Product Concept, and Shared Product Service documents use a small YAML frontmatter block:

```yaml
---
id:
kind:
group: # for Product Groups and product documents
product: # for product documents
title:
summary:
status: draft | reviewed
owner:
last_reviewed:
related: []
topics: []
---
```

This metadata exists only to support ownership and AI retrieval. It does not introduce Capability, Domain, Decision, release, or handoff concepts.

The Design System keeps its existing full metadata. The manifest generator normalizes it without changing Design System document structure.

## AI retrieval manifest

`manifest.generated.json` is the generated discovery index for the repository.

It helps AI:

- Find documents by group, product, kind, title, summary, and topics
- Resolve `related` IDs to file paths
- Avoid reading the whole repository
- Add only relevant shared product services, Design System, and content guidance

Recommended retrieval sequence:

```text
1. Read README.md and manifest.generated.json.
2. Select the relevant Product Group and Product Overview.
3. Select only the necessary Product Areas and Shared Product Concepts.
4. Add relevant Shared Product Services.
5. For design tasks, add relevant Design System and content documents.
6. Follow related IDs only when they materially affect the task.
```

See `docs/manifest.md` for generation and validation rules.

## Status and ownership

Every Product Group Overview, Product Overview, Product Area, Shared Product Concept, and Shared Product Service should include:

```text
Status: Draft | Reviewed
Owner: person or team
Last reviewed: date
```

`Reviewed` means the owner has reviewed the document as usable current team context. It does not mean every branch and edge case has been tested.

Unknowns, assumptions, variations, and untested behavior must be written explicitly.

## Update rule

AI may identify a gap and propose an exact update. A named owner decides whether the proposal is correct and updates the repository manually through a normal branch and pull request.

After any indexed document changes, regenerate `manifest.generated.json` and include it in the same pull request.
