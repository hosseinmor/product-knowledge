# AI Retrieval Rules

This document defines how AI workflows discover and read repository knowledge.

The goal is to retrieve the smallest sufficient and trustworthy context without reading the entire repository, guessing from filenames, or treating migration gaps as absence of knowledge.

## Retrieval principles

- Read repository guidance and `manifest.generated.json` before selecting knowledge documents.
- Use manifest `collection`, `product`, `type`, `summary`, and related IDs for discovery.
- Do not glob folders or infer document meaning from filenames when the manifest can resolve it.
- Inspect the manifest `unindexed` list before claiming repository coverage.
- Treat unindexed documents as an explicit coverage gap, not as nonexistent knowledge.
- Prefer `knowledge_state: canonical` for current intended truth.
- Treat `observed` as current evidence whose intended meaning remains unconfirmed.
- Treat `unverified` as content or metadata requiring semantic review.
- Do not use `deprecated` as current truth.
- Keep proposed and unreleased behavior from `product-work` separate from current repository knowledge.
- Follow stable IDs and explicit relationships rather than folder proximity.
- Read Evidence, Coverage, Unknowns, and Open Questions before presenting a document as complete.
- Never silently resolve conflicts.
- Never infer full coverage from one actor, role, account, authentication state, environment, or happy path.

## Required discovery sequence

```text
1. Read the root README when the workflow is unfamiliar
2. Read manifest.generated.json
3. Inspect summary and unindexed entries
4. Select the relevant collection
5. Filter by product, type, summary, and related IDs
6. Read the relevant overview or canonical owner
7. Read the smallest sufficient related set
8. Inspect evidence, coverage, unknowns, and last verification
9. Report conflicts, unverified knowledge, staleness, and unindexed coverage gaps
```

When the manifest is missing or stale, stop and report a repository-quality failure. Do not silently replace it with filename-based discovery.

## Collections

### Product

Supported types:

```text
product
capability
flow
domain
decision
```

Typical retrieval order:

```text
Product overview
→ relevant Capabilities
→ relevant Flows
→ governing Domains when stable rules matter
→ accepted Decisions when rationale matters
```

### Design System

Supported types:

```text
overview
foundation
token
component
pattern
experience-rule
accessibility
product-variation
reference
governance
ui-template
```

Typical retrieval order:

```text
Design System overview or governance
→ relevant foundation or token model
→ relevant Component or Pattern
→ accessibility and experience rules
→ product variation
→ Figma or code references
```

A Design System Component or Pattern is not a Product Capability. Do not use product-document ownership rules to classify reusable UI knowledge.

### Content

Supported type:

```text
content-guideline
```

Read content guidance when the task changes product copy, messaging, naming, notifications, email, SMS, or other cross-product communication behavior.

### Product Standard

Supported types:

```text
product-standard
documentation-guideline
```

Read product standards when they constrain product behavior or documentation practice across products.

### Shared Domain

Supported type:

```text
domain
```

Read a shared Domain only when its meaning, rules, and ownership are genuinely consistent across products.

## Context by task type

### Product research and discovery

Read:

```text
Product overview
→ relevant Capabilities
→ relevant Flows when concrete behavior matters
→ relevant Domains
→ accepted Decisions
→ Evidence, Coverage, and Unknowns
```

Raw research and walkthrough material remains in `product-work` and should not automatically become canonical knowledge.

### Product and interaction design

Read:

```text
Product overview
→ Capability
→ relevant Flow
→ governing Domain rules
→ Design System Component and Pattern knowledge
→ accessibility, content, and product standards
→ accepted Decisions
→ Coverage and Unknowns
```

### Requirements and delivery preparation

Read:

```text
Product overview
→ affected Capabilities
→ relevant Flows
→ governing Domain rules and lifecycle
→ accepted Decisions
→ Design System and shared standards
→ documented gaps and untested cases
```

Do not convert current knowledge directly into backlog work without identifying the proposed change.

### Product walkthrough

Read existing knowledge only to identify known boundaries, entry points, expected behavior, and coverage targets.

Do not use existing documents as proof that production behavior was observed. The walkthrough must produce its own evidence and coverage matrix using `ai/skills/product-walkthrough/SKILL.md`.

### Product Knowledge update

Read:

```text
Released change evidence or reviewed walkthrough output
→ source readiness and coverage
→ affected canonical owner
→ related documents whose references or applications changed
→ accepted Decisions
→ relevant shared collections
```

Update the owner of each changed fact. Do not copy the same rule into every related document.

## Trust and conflict handling

Use this trust order for current product truth:

```text
Reviewed canonical owner with current evidence
→ other reviewed canonical documents
→ draft canonical documents
→ reviewed observed documents
→ draft observed documents
→ reviewed unverified documents
→ reviewed walkthrough evidence
→ raw temporary source material
```

This order does not authorize automatic conflict resolution.

When sources conflict:

1. Identify the canonical owner by collection, type, and fact scope.
2. Present the conflicting statements and IDs.
3. Compare evidence, actor, role, environment, and verification date.
4. Check accepted Decisions for rationale.
5. Request human review when intended truth remains unclear.
6. Do not rewrite history or hide uncertainty.

## Canonical Product Knowledge ownership

```text
Product purpose, boundary, main Capabilities, and major user journeys
→ Product overview

Stable business rule, permission, entity relationship, or lifecycle
→ Domain

Durable product ability, entry point, availability, or Capability-specific state
→ Capability

Behavioral step, branch, validation, error, recovery, persistence, or end state
→ Flow

Approved rationale and historical trade-off
→ Decision
```

Design System, Content, Product Standard, and Shared Domain collections use their own type-specific ownership rules.

## Metadata expectations

Every indexed document has:

```text
id
collection
type
title
summary
knowledge_state
document_maturity
related
```

Product documents also have `product`.

Relationships use stable IDs. Resolve them through the manifest rather than reconstructing paths.

Legacy `status` or `maturity` metadata is not equivalent to the common metadata envelope and must be treated as unindexed until migrated.

## Manifest coverage handling

The manifest contains:

```text
documents
→ fully indexable documents

unindexed
→ paths whose metadata is missing, legacy, incomplete, or invalid
```

Before answering:

- Check whether relevant directories or known areas appear in `unindexed`.
- State when retrieval may be incomplete because of unindexed documents.
- Do not claim that the repository has no rule or document solely because it is absent from `documents`.
- Do not read all unindexed files by default; open only paths materially relevant to the task.

## Product behavior coverage

Coverage is scoped evidence, not a binary property of a whole product.

Check:

- Actor and role
- Account and permission level
- Authentication state
- Environment
- Entry points
- Main path
- Meaningful branches
- Empty, validation, error, and recovery states
- Persistence and return behavior
- Blocked and untested cases

Use these statuses consistently:

```text
observed
blocked
not-tested
not-applicable
unknown
```

Do not describe a Capability or Flow as fully verified while material blocked, not-tested, or unknown cases remain.

## Staleness handling

`last_verified` is a review signal, not proof that content is wrong.

When a document appears stale:

- Compare it with newer accepted Decisions and release evidence.
- Check whether related documents were updated more recently.
- Check whether evidence still represents relevant environments and roles.
- Surface the risk.
- Do not discard the document solely because of its date.

## Stop conditions

Stop expanding context when:

- The owner, current behavior, governing rules, relevant rationale, and material coverage gaps are clear.
- Additional related documents do not materially affect the task.
- The next dependency requires unavailable evidence or a human decision.

Do not read the entire repository merely to increase confidence.

## Output expectations

Distinguish:

```text
Canonical current behavior
Observed but unconfirmed behavior
Unverified knowledge
Inference
Proposed change
Assumption
Coverage gap
Repository indexing gap
Open question
Human-approved decision
```

Any conclusion not directly supported by repository knowledge or approved initiative material must be labeled as an inference or recommendation.
