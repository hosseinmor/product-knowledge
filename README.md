# Product Knowledge

This repository contains the permanent, canonical knowledge of the product ecosystem.

It is organized into four main layers:

```text
shared/
→ Knowledge that is consistent across multiple products

products/
→ Product-specific overviews, capabilities, flows, domains, and decisions

templates/
→ Required document shapes for Product Knowledge and temporary walkthrough output

ai/
→ Stable AI workflows that discover, consume, and update Product Knowledge
```

Temporary product work, initiative drafts, PRD drafts, recordings, screenshots, walkthrough outputs, and raw evidence belong in the separate `product-work` repository.

## Main principles

- Canonical documentation describes approved current product behavior.
- Proposed or unreleased behavior is not canonical.
- The default documentation set is Product overview, Capability, and Flow.
- Domain and Decision documents are created only when their additional responsibility is needed.
- Major user journeys live inside the Product overview; Journey is not a separate canonical document type, template, or folder.
- Feature is not a Product Knowledge document type; use Capability for durable product abilities.
- User outcomes, usage contexts, rules, states, and lifecycles are content inside their owning documents, not separate document types.
- Shared knowledge belongs in `shared/` only when its meaning and ownership are genuinely cross-product.
- Every durable product fact has one canonical owner; related documents reference rather than redefine it.
- Document truth state is separate from document maturity.
- Evidence, coverage limits, and unknowns remain visible.
- Stable metadata and generated discovery indexes help AI retrieve the smallest sufficient set of documents.
- AI prepares evidence and documentation changes; humans approve semantic decisions and final diffs.

## Knowledge model and templates

The repository uses a minimal model centered on Product overview, Capability, Flow, Domain, and Decision.

See [`knowledge-model.md`](knowledge-model.md) for definitions, ownership rules, metadata, retrieval, and the relationship with Scrum and delivery work.

See [`templates/README.md`](templates/README.md) for official document templates. New documents and material restructures must use these templates.

See [`ai/retrieval-rules.md`](ai/retrieval-rules.md) for the document-discovery and context-expansion behavior expected from AI workflows.

## Main workflows

### Product walkthrough

```text
Product area and actor are scoped
→ AI inventories surfaces and executes safe interactions
→ AI tracks branch and state coverage
→ AI connects observations to evidence
→ AI exposes unknown, blocked, and untested cases
→ Human reviews the walkthrough output
```

The completed walkthrough output remains in `product-work`. Candidate Capabilities, Flows, rules, and Decisions are not canonical until the Product Knowledge Update workflow routes reviewed facts to their owner documents.

See:

```text
ai/skills/product-walkthrough/SKILL.md
templates/walkthrough-output-template.md
```

### Initiative to PRD

```text
PM creates a short initiative brief
→ AI gathers relevant Product Knowledge
→ AI prepares initiative.md
→ AI asks only blocking questions
→ Humans make required decisions
→ AI generates prd.md
→ Humans approve the PRD
```

See:

```text
ai/skills/initiative-to-prd/SKILL.md
```

### Product Knowledge update

```text
Approved change is released or a walkthrough is reviewed
→ AI classifies facts and identifies canonical owners
→ AI uses the official templates
→ AI preserves evidence, coverage, and unknowns
→ AI prepares patches
→ Humans review the diff
→ Approved changes are merged
```

See:

```text
ai/skills/product-knowledge-update/SKILL.md
```
