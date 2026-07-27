# Product Knowledge

This repository provides the product context that humans and AI need for product research, PRD writing, and design.

The active knowledge model is intentionally small:

```text
Product Overview
→ What the product is, who it serves, its boundaries, and its main areas

Product Area
→ How one meaningful part of a product works

Shared Product Concept
→ A business concept or rule that is genuinely shared across products

Design System
→ Reusable UI foundations, tokens, components, patterns, accessibility, and governance
```

The previous, more elaborate knowledge model is preserved in:

```text
archive/product-knowledge-v1-2026-07-27
```

## Repository structure

```text
products/
→ Product overviews and product-specific areas

shared/product-concepts/
→ Business concepts shared across products

shared/design-system/
→ The complete Design System knowledge base

shared/content/
→ Shared content and language guidance

templates/
→ Simple templates for Product Overview, Product Area, Shared Product Concept, and Jira PRD

ai/
→ Lightweight guidance for PM research, PRD writing, design start, optional walkthroughs, and knowledge updates
```

## Lightweight AI retrieval manifest

`manifest.generated.json` is a generated technical index that helps AI find the smallest relevant set of documents. It does not change the simple Product Knowledge model or add a workflow for PMs and Designers.

AI should use the manifest to filter documents by:

```text
product
kind
title
summary
topics
related IDs
```

Then it should read only the relevant Product Overview, Product Areas, Shared Product Concepts, Design System documents, and content guidance.

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
+ relevant Design System guidance
→ AI prepares design context and an initial draft
→ Designer reviews and develops the solution
```

### Knowledge update

```text
AI identifies missing or outdated knowledge
→ AI proposes exact document changes
→ the Product Area owner reviews the proposal
→ the owner updates the document through a normal branch and PR
→ the manifest is regenerated
```

No release handoff or automated synchronization is required in the current model.

## Product Walkthrough

Product Walkthrough is an optional framework for filling knowledge gaps. It is useful when an area is undocumented, disputed, outdated, or difficult to understand from existing sources.

A walkthrough produces evidence and unknowns. It does not automatically overwrite Product Knowledge. The relevant owner reviews the findings and updates the Product Area manually.

## Product Area rule

A Product Area is a meaningful and relatively independent part of a product that combines related user outcomes, flows, rules, permissions, states, validations, and edge cases.

A Product Area is not merely a page, modal, component, Jira Epic, team, or one product change.

Keep flows inside the Product Area document by default. Split a large area into an overview and separate flow files only when the single document becomes difficult to understand or maintain.

## Shared concepts

When the same business concept appears in more than one product:

```text
Shared definition, data, lifecycle, or rule
→ shared/product-concepts/

Product-specific behavior, outcomes, permissions, and flows
→ products/{product}/areas/

Reusable UI behavior
→ shared/design-system/
```

For example, `Job Post` may be a shared concept, while Employer Job Post Management and Jobseeker Job Post Experience remain separate Product Areas.

## Document status

Use only two documentation statuses:

```text
Draft
→ Incomplete or awaiting owner review

Reviewed
→ Reviewed by the named owner and usable as current team context
```

Unknown or untested behavior must remain visible inside the document. Do not present assumptions as confirmed product behavior.
