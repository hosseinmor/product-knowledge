# Product Knowledge

This repository provides the product context that humans and AI need for product research, PRD writing, and design.

The active knowledge model is intentionally small:

```text
Product Group Overview
→ What a stable product group contains and how its products relate

Product Overview
→ What one product is, who it serves, its boundaries, and its main areas

Product Area
→ How one meaningful part of a product works

Shared Product Concept
→ A business concept or rule that is genuinely shared across products

Shared Product Service
→ A durable cross-product service used by several products

Design System
→ Reusable UI foundations, tokens, components, patterns, accessibility, and governance
```

The previous, more elaborate knowledge model is preserved in:

```text
archive/product-knowledge-v1-2026-07-27
```

## Product structure

```text
products/
├── jobvision/
│   ├── overview.md
│   ├── candidate/
│   │   ├── overview.md
│   │   └── areas/
│   └── employer/
│       ├── overview.md
│       └── areas/
│
└── kando/
    ├── overview.md
    ├── ats/
    │   ├── overview.md
    │   └── areas/
    ├── pulse/
    │   ├── overview.md
    │   └── areas/
    ├── onboarding/
    │   ├── overview.md
    │   └── areas/
    └── learning/
        ├── overview.md
        └── areas/
```

`Jobvision` and `Kando` are Product Groups. Candidate, Employer, ATS, Pulse, Onboarding, and Learning are Products. Detailed behavior belongs in Product Areas inside those products.

## Shared structure

```text
shared/product-concepts/
→ Business definitions and rules shared across products

shared/product-services/
→ Cross-product services such as AI-powered fit or matching services

shared/design-system/
→ The complete Design System knowledge base

shared/content/
→ Shared content and language guidance

shared/product-standards/
→ Cross-product product and documentation standards
```

## AI product team placement

The AI product team is an organizational owner, not a Product in the hierarchy.

Document its cross-product services under:

```text
shared/product-services/ai/
```

Use this rule:

```text
AI service used by several products
→ shared/product-services/ai/services/

AI behavior specific to one product
→ the relevant Product Area

Reusable AI interaction UI
→ shared/design-system/
```

The AI product team can be the `owner` of a shared service. It should appear as a Product only if it later owns a distinct user-facing product with its own users and product boundary.

## Repository structure

```text
products/
→ Product Group overviews, Product overviews, and product-specific areas

shared/product-concepts/
→ Business concepts shared across products

shared/product-services/
→ Durable services shared across products

shared/design-system/
→ The complete Design System knowledge base

shared/content/
→ Shared content and language guidance

templates/
→ Simple templates for Product Groups, Products, Product Areas, Shared Concepts, Shared Services, and Jira PRD

ai/
→ Lightweight guidance for PM research, PRD writing, design start, optional walkthroughs, and knowledge updates
```

## Lightweight AI retrieval manifest

`manifest.generated.json` is a generated technical index that helps AI find the smallest relevant set of documents. It does not add a workflow for PMs and Designers.

AI should use the manifest to filter documents by:

```text
group
product
kind
title
summary
topics
related IDs
```

Then it should read only the relevant Product Group Overview, Product Overview, Product Areas, Shared Product Concepts, Shared Product Services, Design System documents, and content guidance.

Commands:

```bash
python -m pip install -r requirements-dev.txt
python scripts/generate_manifest.py generate
python scripts/generate_manifest.py check
```

Any change to indexed documents must include the regenerated manifest. CI checks metadata, unique IDs, related IDs, and manifest freshness.

See [`docs/manifest.md`](docs/manifest.md).

## Main use cases

### PM research

```text
Research question
→ manifest selects relevant Product Knowledge
→ internal product context
→ external research
→ findings and opportunities
```

### PM to PRD

The PRD lives in Jira. No separate Brief document is required.

```text
Initial Jira input
→ manifest selects relevant Product Knowledge
→ blocking questions
→ PM decisions
→ complete PRD in Jira
```

The initial Jira input should at least state:

- Problem
- Why it matters or available evidence
- Affected users
- Desired outcome
- Known constraints

### Design start

```text
Approved Jira PRD
+ Product Knowledge selected through the manifest
+ relevant Shared Product Services
+ relevant Design System guidance
→ AI prepares design context and an initial draft
→ Designer reviews and develops the solution
```

### Knowledge update

```text
AI identifies missing or outdated knowledge
→ AI proposes exact document changes
→ the named owner reviews the proposal
→ the owner updates the document through a normal branch and PR
→ the manifest is regenerated
```

No release handoff or automated synchronization is required in the current model.

## Product Walkthrough

Product Walkthrough is an optional framework for filling knowledge gaps. It is useful when an area is undocumented, disputed, outdated, or difficult to understand from existing sources.

A walkthrough produces evidence and unknowns. It does not automatically overwrite Product Knowledge. The relevant owner reviews the findings and updates the Product Area manually.

## Product Area rule

A Product Area is a meaningful and relatively independent part of a product that combines related user outcomes, flows, rules, permissions, states, validations, and edge cases.

A Product Area is not merely a page, modal, component, Jira Epic, team, service, or one product change.

Keep flows inside the Product Area document by default. Split a large area into an overview and separate flow files only when the single document becomes difficult to understand or maintain.

## Shared concepts and services

When the same business concept appears in more than one product:

```text
Shared definition, data, lifecycle, or rule
→ shared/product-concepts/

Product-specific behavior, outcomes, permissions, and flows
→ products/{group}/{product}/areas/

Cross-product service behavior
→ shared/product-services/

Reusable UI behavior
→ shared/design-system/
```

For example, `Job Post` may be a shared concept, while Employer Job Post Management and Candidate Job Post Experience remain separate Product Areas.

## Document status

Use only two documentation statuses:

```text
Draft
→ Incomplete or awaiting owner review

Reviewed
→ Reviewed by the named owner and usable as current team context
```

Unknown or untested behavior must remain visible inside the document. Do not present assumptions as confirmed product behavior.
