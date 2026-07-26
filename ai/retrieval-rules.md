# AI Retrieval Rules

This document defines the default method AI workflows should use to discover and read Product Knowledge.

The goal is to retrieve the smallest sufficient and trustworthy context for the task instead of reading the entire repository or relying on filenames alone.

## Retrieval principles

- Read canonical Product Knowledge before proposing changes to existing behavior.
- Use document metadata and the generated manifest for discovery.
- Prefer documents with `knowledge_state: canonical`.
- Treat `knowledge_state: observed` as evidence that requires explicit uncertainty.
- Do not treat `deprecated` documents as current behavior.
- Keep proposed or unreleased behavior from `product-work` separate from current Product Knowledge.
- Follow stable document IDs and explicit relationships rather than guessing from folder proximity.
- Expand context only when the current document indicates a dependency, relationship, conflict, or missing rule.
- Never silently choose between conflicting canonical documents.

## Default discovery sequence

```text
1. Read the root README and knowledge model when the workflow is unfamiliar
2. Read manifest.generated.json
3. Filter by product, document type, summary, actors, and related IDs
4. Read the relevant product-overview.md
5. Read the smallest sufficient set of Capabilities and Flows
6. Read Domain rules and accepted Decisions only when relevant
7. Read a separate Journey only when the Product overview or relationships identify one
8. Report conflicts, observed knowledge, stale verification, and missing documents
```

## Context by task type

### Product research and discovery

Read:

```text
Product overview
→ relevant Capabilities
→ relevant Domains when business constraints matter
→ accepted Decisions when prior rationale matters
→ optional complex Journey when explicitly related
```

Use this context to understand current boundaries, known behavior, durable constraints, and decisions that should not be reopened without evidence.

Research source material supplied for the current initiative remains in `product-work` and should not automatically become canonical Product Knowledge.

### Product and interaction design

Read:

```text
Product overview
→ Capability
→ relevant Flow
→ referenced Domain rules
→ relevant design-system and content standards
→ accepted Decisions
→ optional complex Journey when end-to-end context is not sufficient in the Product overview
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
```

Do not convert canonical documents directly into backlog items without identifying the proposed change. Product Knowledge describes the current product; a Product Backlog item describes work intended to change it.

### Product Knowledge update

Read:

```text
Released change evidence
→ affected Capability or Flow
→ owning Domain rules when applicable
→ Product overview when boundaries or major journeys changed
→ affected Decisions
→ related shared knowledge
→ optional Journey only when it owns a complex end-to-end fact
```

Update only documents whose owned facts changed. Do not copy the same rule into every related document.

## Trust and conflict handling

Use this trust order for current product truth:

```text
Reviewed canonical owner document
→ other reviewed canonical documents
→ draft canonical documents
→ reviewed observed documents
→ draft observed documents
→ temporary source material
```

This order does not authorize AI to resolve semantic conflicts automatically.

When sources conflict:

1. Identify the canonical owner by document type and fact scope.
2. Present the conflicting statements and source IDs.
3. Check accepted Decisions for relevant rationale.
4. Request human review when the intended truth is still unclear.
5. Do not rewrite history or hide uncertainty.

## Canonical ownership checks

Before using or changing a fact, identify its owner:

```text
Product purpose, boundary, major capabilities, and major user journeys
→ Product overview

Stable business rule, permission, entity relationship, or lifecycle
→ Domain

Durable product ability, entry point, availability, or capability-specific state
→ Capability

Behavioral step, branch, validation, error, or recovery path
→ Flow

Approved rationale and historical trade-off
→ Decision

Complex end-to-end journey with independent documentation
→ optional Journey

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

Supported primary types are:

```text
product
domain
capability
flow
decision
shared
```

`journey` is supported only for optional complex Journey documents.

User goals, usage contexts, rules, states, and lifecycles are represented inside their owning documents and are not standalone retrieval types.

The generated manifest must be rebuilt when metadata, document paths, or relationships change.

The manifest is an index. It is not a source of product rules.

## Staleness handling

`last_verified` is a review signal, not proof that content is outdated.

When a document appears stale:

- Compare it with newer accepted Decisions and released change evidence.
- Check whether related documents were updated more recently.
- Surface the staleness risk.
- Do not discard the document solely because of its date.

## Stop conditions

Stop expanding context when:

- The actor, goal, trigger, current behavior, governing rules, and relevant rationale are clear.
- Additional related documents do not materially affect the task.
- The next dependency requires unavailable source material or a human decision.

Do not read the entire repository merely to increase confidence.

## Output expectations

When Product Knowledge is used, AI outputs should distinguish:

```text
Canonical current behavior
Observed but unconfirmed behavior
Proposed change
Assumption
Open question
Human-approved decision
```

Any conclusion not directly supported by Product Knowledge or approved initiative material must be labeled as an inference or recommendation.