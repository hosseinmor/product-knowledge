# Product Knowledge

This repository provides the product context that humans and AI need for product research, Product Knowledge authoring, PRD writing, and design.

## AI starting point

AI tools should start with:

```text
AGENTS.md
→ Tool-agnostic repository instructions

ai/router.md
→ Intent routing to the appropriate Skill or workflow
```

After one-time tool setup, users should be able to provide a problem, product knowledge, or files and state the desired outcome without pasting repository paths or a long routing prompt. See [`docs/ai-tool-setup.md`](docs/ai-tool-setup.md).

The active knowledge model is intentionally small:

```text
Product Group Overview
→ What a stable product group contains and how its products relate

Product Overview
→ What one product is, who it serves, its boundaries, and its main areas

Product Area
→ Where meaningful product behavior happens around an outcome, capability, or business process

Product Concept
→ What a business entity, actor, or concept means and what is intrinsically true about it

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
└── cando/
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

`Jobvision` and `Cando` are Product Groups. Candidate, Employer, ATS, Pulse, Onboarding, and Learning are Products. Detailed contextual behavior belongs in Product Areas inside those products.

## Shared structure

```text
shared/product-concepts/
→ Canonical business definitions, attributes, relationships, intrinsic rules, and lifecycle used across multiple Product Areas

shared/product-services/
→ Cross-product services such as AI-powered fit or matching services

shared/design-system/
→ The complete Design System knowledge base

shared/content/
→ Shared content and language guidance

shared/product-standards/
→ Cross-product product and documentation standards
```

A Product Concept does not need to be used by different products before it becomes useful as a canonical Concept. Reuse across multiple Product Areas, independent business meaning, intrinsic rules, relationships, or lifecycle can justify promotion. The current repository stores promoted canonical Concepts under `shared/product-concepts/`.

## Core Area / Concept ownership rule

Use this distinction throughout the repository:

```text
Meaning and intrinsic truth of a thing
→ Product Concept

Behavior of things in a context
→ Product Area
```

Examples:

```text
Application connects a Candidate to a Job Post
→ Application Product Concept

After successful Apply, an Application is created
→ Candidate Apply Product Area
```

Attribute existence and meaning belong in Product Concepts; context-dependent requiredness or validation belongs in Product Areas. Canonical States and lifecycle belong in Product Concepts; transitions created or controlled by one Area belong in that Area.

Do not duplicate canonical Concept definitions or intrinsic rules inside Product Areas.

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
AGENTS.md
→ Tool-agnostic AI entry point

products/
→ Product Group overviews, Product overviews, and product-specific areas

shared/product-concepts/
→ Canonical Product Concepts

shared/product-services/
→ Durable services shared across products

shared/design-system/
→ The complete Design System knowledge base

shared/content/
→ Shared content and language guidance

templates/
→ Simple templates for Product Groups, Products, Product Areas, Product Concepts, Shared Services, and Jira PRD

ai/
→ Intent routing, workflow guidance, and active lightweight Skills for recurring AI-assisted product work
```

## Lightweight AI retrieval manifest

`manifest.generated.json` is a generated technical index that helps AI find the smallest relevant set of documents. It does not add a workflow for product teams.

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

Then it should read only the relevant Product Group Overview, Product Overview, Product Areas, Product Concepts, Shared Product Services, Design System documents, and content guidance.

Commands:

```bash
python -m pip install -r requirements-dev.txt
python scripts/generate_manifest.py generate
python scripts/generate_manifest.py check
```

Any change to indexed documents must include the regenerated manifest. CI checks metadata, unique IDs, related IDs, and manifest freshness.

See [`docs/manifest.md`](docs/manifest.md).

## Main use cases

### Product Knowledge authoring

Workflow: [`ai/product-knowledge-authoring.md`](ai/product-knowledge-authoring.md)  
Skill: [`ai/skills/product-knowledge-authoring/SKILL.md`](ai/skills/product-knowledge-authoring/SKILL.md)  
Templates: [`templates/product-area.md`](templates/product-area.md), [`templates/shared-product-concept.md`](templates/shared-product-concept.md)

The owner does not need to fill the complete canonical template manually.

```text
Short or free-form owner knowledge
+ current Product Knowledge selected through the manifest
+ optional supporting sources
→ Product Knowledge Authoring Skill classifies Area vs Concept ownership
→ AI creates a structured review draft and derives boundaries
→ owner corrects missing or wrong product knowledge
→ AI normalizes the final draft
→ approved changes use the normal knowledge-update workflow
```

This flow is intentionally owner-knowledge-first while walkthrough coverage is incomplete. AI should not treat sparse evidence as sufficient to reconstruct undocumented product behavior.

### Research

Workflow: [`ai/research.md`](ai/research.md)

```text
Research question
→ manifest selects relevant Product Knowledge
→ internal product context
→ external research
→ findings and opportunities
```

### PRD writing

Workflow: [`ai/prd-writing.md`](ai/prd-writing.md)  
Skill: [`ai/skills/prd-writing/SKILL.md`](ai/skills/prd-writing/SKILL.md)  
Template: [`templates/jira-prd.md`](templates/jira-prd.md)

The PRD lives in Jira. No separate Brief document is required.

```text
Initial Jira input
→ PRD Skill loads the workflow and template
→ manifest selects relevant Product Knowledge
→ blocking questions
→ product decisions
→ complete PRD in Jira
```

The initial Jira input should at least state:

- Problem
- Why it matters or available evidence
- Affected users
- Desired outcome
- Known constraints

When the AI environment is connected through `AGENTS.md`, the product owner only needs to provide this input and ask for a PRD. The template and routing prompt do not need to be pasted into every conversation.

### Design start

Workflow: [`ai/design-start.md`](ai/design-start.md)

```text
Approved Jira PRD
+ Product Knowledge selected through the manifest
+ relevant Shared Product Services
+ relevant Design System guidance
→ AI prepares design context and an initial draft
→ Designer reviews and develops the solution
```

### Knowledge update

Workflow: [`ai/knowledge-update.md`](ai/knowledge-update.md)

```text
Reviewed owner knowledge, approved decision, or eligible evidence
→ claims are reconciled against the current product model
→ AI proposes exact document changes
→ the named owner reviews the proposal
→ approved changes are applied through a normal branch and PR
→ the manifest is regenerated when indexed documents change
```

Reviewed evidence packages from the separate `hosseinmor/product-walkthrough` project may be used as sources for this workflow. Draft or unreviewed walkthrough evidence may inform investigation but must not establish canonical Product Knowledge. Walkthrough capture artifacts do not live in this repository.

No release handoff or automated synchronization is required in the current model.

## Product Area rule

A Product Area is a meaningful and relatively independent part of a product around an outcome, capability, or business process whose behavior is described through flows, rules, actors, permissions, validations, relevant state transitions, errors/recovery, and variations.

A Product Area is not merely a page, modal, component, Jira Epic, team, service, walkthrough scope, navigation destination, or one product change.

Product Area creation is a product-modeling decision. One walkthrough or owner explanation may update several Product Areas, and several sources may contribute to one Product Area.

Each Product Area should make its boundary clear through `Includes` and `Does Not Include`, and should reference adjacent Product Areas or Concepts without claiming their behavior.

Keep flows inside the Product Area document by default. Split a large area into an overview and separate flow files only when the single document becomes difficult to understand or maintain.

## Product Concept rule

A Product Concept is a business entity, actor, or concept with independent meaning that may be used in several Product Areas and may have its own attributes, relationships, intrinsic rules, states, or lifecycle.

Do not create a Product Concept for every noun. Promote a Concept when an independent canonical definition materially reduces ambiguity or duplication, especially when:

- it is used across multiple Product Areas;
- it has important business/product attributes;
- it has semantic relationships to other Concepts;
- it has intrinsic rules or lifecycle;
- changes to its definition would affect multiple Areas.

Product Areas own what happens to a Concept in a context. Product Concepts own what the Concept means and what is intrinsically true about it.

## Evidence and product truth

Keep evidence, owner knowledge, product decisions, and canonical Product Knowledge distinct.

```text
Explicit knowledge confirmed by the responsible owner
→ eligible for canonical Product Knowledge after review

Reviewed production walkthrough evidence
→ eligible supporting evidence; do not generalize beyond what the evidence and owner review support

Draft or unreviewed walkthrough evidence
→ cannot establish canonical Product Knowledge

Unknown, inferred, contradictory, or untested behavior
→ keep visible; do not present it as confirmed product truth
```

See [`ai/knowledge-update.md`](ai/knowledge-update.md) for the reconciliation taxonomy and evidence gate.

## Product Concepts and services

Use this placement model:

```text
Canonical definition, attributes, relationships, intrinsic rules, or lifecycle reused across Product Areas
→ shared/product-concepts/

Contextual behavior, outcomes, permissions, validations, and flows
→ products/{group}/{product}/areas/

Cross-product service behavior
→ shared/product-services/

Reusable UI behavior
→ shared/design-system/
```

`Job Post`, `Application`, `Resume`, and `Company` are currently documented canonical Product Concepts. Product-specific management and experience remain in separate Product Areas.

## Document status

Use only two documentation statuses:

```text
Draft
→ Incomplete or awaiting owner review

Reviewed
→ Reviewed by the named owner and usable as current team context
```

Unknown or untested behavior must remain visible inside the document. Do not present assumptions as confirmed product behavior.
