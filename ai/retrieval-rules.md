# AI Retrieval Rules

This document defines the default method AI workflows should use to discover and read Product Knowledge.

The goal is to retrieve the smallest sufficient and trustworthy context for the task instead of reading the entire repository or relying on filenames alone.

## Retrieval principles

- Read Product Knowledge before proposing changes to existing behavior.
- Use document metadata and the generated manifest for discovery.
- Prefer documents with `knowledge_state: canonical`.
- Treat `knowledge_state: observed` as evidence that requires explicit uncertainty.
- Do not treat `deprecated` documents as current behavior.
- Keep proposed or unreleased behavior from `product-work` separate from current Product Knowledge.
- Follow stable document IDs and explicit relationships rather than guessing from folder proximity.
- Expand context only when a dependency, relationship, conflict, coverage gap, or missing rule requires it.
- Read Evidence, Coverage, Unknowns, and Open Questions before presenting a document as complete.
- Never silently choose between conflicting Product Knowledge documents.
- Never infer full product coverage from one actor, role, account, authentication state, or happy path.

## Default discovery sequence

```text
1. Read the root README and knowledge model when the workflow is unfamiliar
2. Read manifest.generated.json when available
3. Filter by product, document type, summary, actors, and related IDs
4. Read the relevant product-overview.md
5. Read the smallest sufficient set of Capabilities and Flows
6. Read Domain rules and accepted Decisions only when relevant
7. Inspect evidence, coverage, unknowns, and last verification
8. Report conflicts, observed knowledge, stale verification, and missing documents
```

## Context by task type

### Product research and discovery

Read:

```text
Product overview
→ relevant Capabilities
→ relevant Flows when concrete behavior matters
→ relevant Domains when business constraints matter
→ accepted Decisions when prior rationale matters
→ Evidence and Coverage sections
```

Use this context to understand current boundaries, major user journeys, known behavior, durable constraints, and documented gaps.

Raw research and walkthrough material remains in `product-work` and should not automatically become Product Knowledge.

### Product and interaction design

Read:

```text
Product overview
→ Capability
→ relevant Flow
→ referenced Domain rules
→ relevant design-system and content standards
→ accepted Decisions
→ Coverage and Unknowns
```

Use the Product overview for product and major-journey context, the Capability for current product ability, the Flow for concrete behavior, and the Domain for rules that must remain true.

### Requirements and delivery preparation

Read:

```text
Product overview
→ Capability
→ relevant Flows
→ referenced Domain rules and lifecycle
→ accepted Decisions
→ shared standards
→ documented gaps and untested cases
```

Do not convert Product Knowledge documents directly into backlog items without identifying the proposed change. Product Knowledge describes the current product; a Product Backlog item describes work intended to change it.

### Product walkthrough

Read existing Product Knowledge only to identify known boundaries, entry points, expected behavior, and coverage targets.

Do not use existing documents as proof that current production behavior was observed. The walkthrough must produce its own evidence and coverage matrix using `ai/skills/product-walkthrough/SKILL.md`.

### Product Knowledge update

Read:

```text
Released change evidence or reviewed walkthrough output
→ source readiness and coverage
→ affected Capability or Flow
→ owning Domain rules when applicable
→ Product overview when boundaries, major Capabilities, or major user journeys changed
→ affected Decisions
→ related shared knowledge
```

Update only documents whose owned facts changed. Do not copy the same rule into every related document.

## Trust and conflict handling

Use this trust order for current product truth:

```text
Reviewed canonical owner document with current evidence
→ other reviewed canonical documents
→ draft canonical documents
→ reviewed observed documents
→ draft observed documents
→ reviewed walkthrough evidence
→ raw temporary source material
```

This order does not authorize AI to resolve semantic conflicts automatically.

When sources conflict:

1. Identify the canonical owner by document type and fact scope.
2. Present the conflicting statements and source IDs.
3. Check accepted Decisions for relevant rationale.
4. Compare evidence, actor, role, environment, and verification date.
5. Request human review when intended truth remains unclear.
6. Do not rewrite history or hide uncertainty.

## Canonical ownership checks

```text
Product purpose, boundary, major Capabilities, and major user journeys
→ Product overview

Stable business rule, permission, entity relationship, or lifecycle
→ Domain

Durable product ability, entry point, availability, or Capability-specific state
→ Capability

Behavioral step, branch, validation, error, recovery, persistence, or end state
→ Flow

Approved rationale and historical trade-off
→ Decision

Cross-product rule with genuinely shared meaning
→ Shared knowledge
```

Related documents may explain how they use an owned fact, but should reference its stable ID instead of independently redefining it.

## Metadata expectations

At minimum, retrieval depends on:

```text
id
type
product
title
summary
knowledge_state
document_maturity
related
last_verified
```

Supported document types are:

```text
product
capability
flow
domain
decision
shared
```

Journey, Feature, User Goal, Scenario, Rule, State, Lifecycle, and Subdomain are not standalone retrieval types.

The generated manifest must be rebuilt when metadata, document paths, or relationships change. The manifest is an index, not a source of product rules.

## Coverage handling

Coverage is scoped evidence, not a binary property of the whole product.

When evaluating a document, check:

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

Use these coverage statuses consistently:

```text
observed
blocked
not-tested
not-applicable
unknown
```

Do not describe a Capability or Flow as fully verified when material `blocked`, `not-tested`, or `unknown` cases remain.

## Staleness handling

`last_verified` is a review signal, not proof that content is outdated.

When a document appears stale:

- Compare it with newer accepted Decisions and released change evidence.
- Check whether related documents were updated more recently.
- Check whether its evidence still represents the relevant environment and roles.
- Surface the staleness risk.
- Do not discard the document solely because of its date.

## Stop conditions

Stop expanding context when:

- Actor, user outcome, trigger, current behavior, governing rules, relevant rationale, and material coverage gaps are clear.
- Additional related documents do not materially affect the task.
- The next dependency requires unavailable evidence or a human decision.

Do not read the entire repository merely to increase confidence.

## Output expectations

When Product Knowledge is used, AI outputs should distinguish:

```text
Canonical current behavior
Observed but unconfirmed behavior
Inference
Proposed change
Assumption
Coverage gap
Open question
Human-approved decision
```

Any conclusion not directly supported by Product Knowledge or approved initiative material must be labeled as an inference or recommendation.
