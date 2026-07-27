# AI Retrieval Rules

This document defines the default method AI workflows should use to discover and read Product Knowledge.

The goal is to retrieve the smallest sufficient and trustworthy context for the task instead of reading the entire repository or relying on filenames alone.

## Retrieval principles

- Read Product Knowledge before proposing changes to existing behavior.
- Use document metadata and the generated manifest for discovery.
- Prefer documents with `knowledge_state: canonical`.
- Treat `knowledge_state: observed` as evidence that requires explicit uncertainty.
- Do not treat `deprecated` documents as current behavior.
- Keep proposed or unreleased behavior and raw walkthrough evidence from `product-work` separate from Product Knowledge.
- Follow stable document IDs and explicit relationships rather than guessing from folder proximity.
- Read Evidence, Coverage, Unknowns, and untested-case sections before treating a document as complete.
- Absence from a document is not evidence that behavior does not exist when coverage is incomplete.
- Expand context only when the current document indicates a dependency, relationship, conflict, coverage gap, or missing rule.
- Never silently choose between conflicting Product Knowledge documents.

## Default discovery sequence

```text
1. Read the root README and knowledge model when the workflow is unfamiliar
2. Read manifest.generated.json when available
3. Filter by product, document type, summary, actors, and related IDs
4. Read the relevant product-overview.md
5. Read the smallest sufficient set of Capabilities and Flows
6. Read Domain rules and accepted Decisions only when relevant
7. Inspect Evidence, Coverage, Unknowns, and last_verified
8. Report conflicts, observed knowledge, stale verification, coverage gaps, and missing documents
```

## Context by task type

### Product research and discovery

Read:

```text
Product overview
→ relevant Capabilities
→ relevant Flows for concrete behavior
→ relevant Domains when business constraints matter
→ accepted Decisions when prior rationale matters
```

Use this context to understand current boundaries, major user journeys, known behavior, durable constraints, evidence limits, and decisions that should not be reopened without evidence.

Research and walkthrough source material remains in `product-work` and should not automatically become Product Knowledge.

### Product and interaction design

Read:

```text
Product overview
→ Capability
→ relevant Flow
→ referenced Domain rules
→ relevant design-system and content standards
→ accepted Decisions
```

Use the Product overview for product and major-journey context, the Capability for current product ability, the Flow for concrete behavior, and the Domain for rules that must remain true.

Before relying on a Flow or Capability, verify which actors, access states, entry points, states, and branches its Coverage section confirms. Surface material gaps instead of designing as though they were settled.

### Requirements and delivery preparation

Read:

```text
Product overview
→ Capability
→ relevant Flows
→ referenced Domain rules and lifecycle
→ accepted Decisions
→ shared standards
```

Do not convert Product Knowledge documents directly into backlog items without identifying the proposed change. Product Knowledge describes the current product; a Product Backlog item describes work intended to change it.

### Product Knowledge update

Read:

```text
Reviewed source evidence
→ affected Capability or Flow
→ owning Domain rules when applicable
→ Product overview when boundaries, major Capabilities, or major user journeys changed
→ affected Decisions
→ related shared knowledge
```

Update only documents whose owned facts changed. Do not copy the same rule into every related document.

For recovery from product interaction, use only a human-reviewed output produced according to `ai/skills/product-walkthrough/SKILL.md`.

## Trust and conflict handling

Use this trust order for current product truth:

```text
Reviewed canonical owner document with supporting evidence
→ other reviewed canonical documents
→ draft canonical documents with explicit coverage
→ reviewed observed documents
→ draft observed documents
→ reviewed temporary source material
→ unreviewed temporary source material
```

This order does not authorize AI to resolve semantic conflicts automatically.

When sources conflict:

1. Identify the canonical owner by document type and fact scope.
2. Present the conflicting statements, source IDs, and evidence.
3. Compare actors, environments, states, and coverage because the statements may describe different contexts.
4. Check accepted Decisions for relevant rationale.
5. Request human review when the intended truth is still unclear.
6. Do not rewrite history or hide uncertainty.

## Canonical ownership checks

Before using or changing a fact, identify its owner:

```text
Product purpose, boundary, major Capabilities, and major user journeys
→ Product overview

Stable business rule, permission, entity relationship, or lifecycle
→ Domain

Durable product ability, entry point, availability, or Capability-specific state
→ Capability

Behavioral step, branch, validation, error, recovery, cancellation, persistence, or end state
→ Flow

Approved rationale and historical trade-off
→ Decision

Cross-product rule with genuinely shared meaning
→ Shared knowledge
```

Related documents may explain how they use an owned fact, but should reference its stable ID instead of independently redefining it.

## Metadata expectations

AI should use frontmatter fields as discovery signals, not as substitutes for document content.

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
domain
capability
flow
decision
shared
```

Journey, Feature, User Goal, Scenario, Rule, State, Lifecycle, and Subdomain are not standalone retrieval types.

The generated manifest must be rebuilt when metadata, document paths, or relationships change. The manifest is an index, not a source of product rules or proof of coverage.

## Evidence and coverage handling

Evidence indicates why a fact is documented. Coverage indicates where the evidence applies and where it does not.

When reading a document:

- Identify actors, roles, authentication states, environments, entry points, states, and branches that were verified.
- Preserve explicit Unknown, blocked, and untested cases.
- Do not generalize from one actor or context to all users.
- Do not interpret `not-tested` as unsupported or absent behavior.
- Do not promote an inference to current truth.
- Request a Product Walkthrough when a material current behavior cannot be established from the available evidence.

## Staleness handling

`last_verified` is a review signal, not proof that content is outdated.

When a document appears stale:

- Compare it with newer accepted Decisions and released change evidence.
- Check whether related documents were updated more recently.
- Inspect whether its evidence and coverage still match the task context.
- Surface the staleness risk.
- Do not discard the document solely because of its date.

## Stop conditions

Stop expanding context when:

- The actor, user outcome, trigger, current behavior, governing rules, relevant rationale, evidence, and coverage are sufficiently clear for the task.
- Additional related documents do not materially affect the task.
- The next dependency requires unavailable source material, a new walkthrough, or a human decision.

Do not read the entire repository merely to increase confidence.

## Output expectations

When Product Knowledge is used, AI outputs should distinguish:

```text
Canonical current behavior
Observed but unconfirmed behavior
Inference
Proposed change
Coverage gap
Unknown or untested case
Suspected bug
Human-approved decision
```

Any conclusion not directly supported by Product Knowledge or approved initiative material must be labeled as an inference or recommendation.
