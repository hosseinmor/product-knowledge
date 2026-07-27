# Product Knowledge

This repository contains reusable context about the current products and the complete shared Design System.

Its purpose is practical:

- give PMs reliable product context for AI-assisted research;
- help PMs create complete PRDs in Jira;
- help designers combine an approved Jira PRD, Product Knowledge, and the Design System to create a useful first design draft;
- improve gradually as new gaps are discovered.

The previous, more elaborate knowledge-system model is preserved on the branch:

```text
archive/knowledge-system-v1
```

It is not part of the active model on `main`.

## Active model

The Product Knowledge side uses only three document types:

```text
Product Overview
→ What the product is, who it serves, its boundaries, main areas, and major journeys

Product Area
→ How one meaningful part of one product works

Shared Product Concept
→ A business concept, definition, lifecycle, or rule that is genuinely shared across products
```

The Design System keeps its existing full structure under `shared/design-system/`.

## Repository structure

```text
products/
├── ats/
│   ├── overview.md
│   └── areas/
├── employer/
│   ├── overview.md
│   └── areas/
├── hrcando/
│   ├── overview.md
│   └── areas/
└── jobseeker/
    ├── overview.md
    └── areas/

shared/
├── product-concepts/
├── product-rules/
├── content/
└── design-system/

templates/
├── product-overview.md
├── product-area.md
├── shared-product-concept.md
└── jira-prd.md

ai/
├── pm-research.md
├── pm-to-prd.md
├── design-start.md
├── product-walkthrough.md
└── knowledge-update.md
```

## Product Area

A Product Area is a meaningful and relatively independent part of a product that supports a recognizable outcome and contains related behavior, flows, rules, permissions, states, and edge cases.

A Product Area is not merely a page, component, modal, navigation item, Jira Epic, team, or microservice.

Examples:

```text
ATS
→ Recruitment Request, Approval Workflow, Candidate Management

Employer
→ Job Post Management

Jobseeker
→ Job Search, Job Post Experience, Application Management
```

Keep the main flows inside one Product Area document by default. Split complex flows into separate files only when the Area document becomes difficult to understand or maintain.

## Shared concepts and cross-product behavior

When two products use the same business concept but expose different behavior, separate shared meaning from product-specific behavior.

Example:

```text
shared/product-concepts/job-post.md
→ shared definition, data, lifecycle, and rules

products/employer/areas/job-post-management.md
→ create, edit, publish, pause, and close behavior

products/jobseeker/areas/job-post-experience.md
→ view, evaluate, save, share, and apply behavior
```

Create a shared Product Area only when outcome, behavior, rules, and ownership are essentially the same across products. Shared UI behavior belongs in the Design System, not Product Knowledge.

## PRD workflow

PRDs stay in Jira. A separate Brief file is not required.

The initial Jira input or AI conversation should at least identify:

```text
Problem
Why now or supporting evidence
Affected users
Desired outcome
Known constraints
```

Then:

```text
Initial Jira input
→ AI reads relevant Product Knowledge
→ AI reports current context and blocking questions
→ PM answers product decisions
→ AI drafts or completes the PRD in Jira
```

## Design workflow

```text
Approved Jira PRD
+ relevant Product Knowledge
+ shared Design System
→ AI prepares design context
→ AI creates a first flow, IA, screen, state, component, or copy draft
→ Designer reviews and develops the solution
```

AI output is a starting point, not the final design decision.

## Product Walkthrough

Product Walkthrough is an optional framework for filling knowledge gaps. It is useful when an Area is missing, outdated, disputed, or poorly understood.

```text
Choose a bounded Product Area and role
→ inspect current behavior and meaningful states
→ record evidence, unknowns, and untested cases
→ owner reviews the findings
→ owner manually updates the Product Area document
```

A walkthrough does not automatically establish intended product rules.

## Updating Product Knowledge

AI may suggest an update when research, PRD work, design work, or a walkthrough reveals missing or outdated knowledge.

```text
AI proposes the exact document and sections to change
→ the Area owner reviews the suggestion
→ the owner edits the document on a branch
→ another relevant team member reviews it
→ the change is merged
```

Use only two simple document states when they are useful:

```text
Draft
Reviewed
```

Do not write undecided proposals as current product behavior.
