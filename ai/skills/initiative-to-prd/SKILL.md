# Initiative to PRD

## Purpose

Turn a short product initiative brief into a reviewable Product Requirements Document with minimal manual writing.

The AI performs:

- Product Knowledge discovery
- Context gathering
- Problem and scope structuring
- Actor and scenario extraction
- Dependency analysis
- Assumption detection
- Blocking-question prioritization
- Option comparison
- PRD drafting
- Consistency checks

Humans remain responsible for product decisions and final approval.

## Required inputs

- Product identifier
- Initiative identifier
- Short initiative brief
- Access to the relevant Product Knowledge

## Optional inputs

- Jira ticket or epic
- User research
- Data analysis
- Design references
- Technical notes
- Previous PRDs
- Walkthrough output

## Expected workspace

```text
product-work/
└── initiatives/
    └── {initiative-id}/
        ├── initiative.md
        └── prd.md
```

## Workflow

### 1. Read the brief

Extract:

- Problem
- Desired outcome
- Initial scope
- Product
- Owner
- Change type

Do not assume the proposed solution or capability name is correct.

### 2. Gather relevant knowledge

Follow `ai/retrieval-rules.md`.

Use the generated manifest to discover the smallest sufficient set of documents, then read only relevant documents from:

- Shared Product Knowledge
- Product overview
- Related journeys
- Related capabilities
- Related flows
- Related domains
- Accepted decisions
- Design system patterns
- Content and product standards

Prefer `knowledge_state: canonical` documents. Treat `observed` knowledge as unconfirmed and surface it explicitly.

Identify the canonical owner of every important rule instead of copying similar statements from several documents.

### 3. Build `initiative.md`

Use this structure:

```md
# Initiative

## Original Brief
## Current Product Context
## Problem and Desired Outcome
## Proposed Scope
### In Scope
### Out of Scope
## Actors and Main Scenarios
## Existing Rules and Constraints
## Dependencies
## Assumptions
## Blocking Questions
## Non-Blocking Questions
## Human Decisions
## Related Product Knowledge
```

Use stable Product Knowledge IDs in `Related Product Knowledge` when available.

### 4. Ask only blocking questions

A blocking question materially changes one or more of:

- Core scope
- Main user flow
- Business rule
- Permission model
- Lifecycle
- Data model
- Technical feasibility

Do not interrupt humans with cosmetic, copy, layout, or low-impact questions.

For each blocking question provide:

```md
## Decision

### Question
### Options
### AI Recommendation
### Reason
### Impact
### Required Reviewer
```

Route decisions to:

- Product behavior or scope → PM
- Interaction or journey → Designer
- Technical feasibility or constraint → Tech
- Cross-functional rule → PM + Tech

The AI may recommend an option, but must not record it as approved without a human decision.

A working decision inside an initiative is not automatically a canonical Decision document. After approval and release, preserve it as a canonical Decision only when its rationale is durable according to `knowledge-model.md`.

### 5. Apply human decisions

After each answer:

- Record the decision
- Update scope and assumptions
- Resolve contradictions
- Remove answered blocking questions
- Keep deferred questions visible
- Recheck consistency with Product Knowledge

### 6. Generate `prd.md`

Use this structure unless the team provides another template:

```md
# Product Requirements Document

## Summary
## Problem
## Desired Outcome
## Scope
### In Scope
### Out of Scope
## Actors
## User Scenarios
## Functional Requirements
## Business Rules
## Permissions
## States and Lifecycle
## Main Flows
## Alternative and Error Flows
## Dependencies
## Constraints
## Analytics and Success Indicators
## Open Questions
## Deferred Items
## Related Product Knowledge
```

### 7. Validate the PRD

Verify that:

- Every requirement is supported by the brief, Product Knowledge, or an approved human decision
- Assumptions are not written as confirmed rules
- Current behavior and intended behavior are not mixed
- Scope is internally consistent
- Business rules do not silently conflict with existing Domain documentation
- Permissions and lifecycle transitions are explicit
- Existing Capabilities are not confused with proposed backlog work
- Accepted Decisions that constrain the change are respected or explicitly reconsidered
- Open questions remain visible
- Out-of-scope items are explicit

### 8. Stop for approval

Present:

- The PRD
- Remaining open questions
- Important assumptions
- Conflicts with existing Product Knowledge
- Major risks or dependencies

Do not mark the PRD as approved on behalf of a human.

## Human responsibilities

Humans are responsible for:

- Providing the initial brief
- Answering blocking decisions
- Approving final scope
- Approving the final PRD

## Rules

- Do not invent product decisions
- Do not hide uncertainty
- Do not ask non-blocking questions too early
- Do not create multiple working documents when one `initiative.md` is enough
- Do not update canonical Product Knowledge before release
- Do not treat a PRD as canonical current-product behavior
- Do not treat Jira Epic, Feature, Story, or Task hierarchy as the Product Knowledge structure
