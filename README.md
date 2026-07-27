# Product Knowledge

This repository contains the permanent, canonical knowledge of the product ecosystem.

It is organized into four main layers:

```text
shared/
→ Knowledge that is consistent across multiple products

products/
→ Product-specific overviews, capabilities, flows, domains, and decisions

templates/
→ Required document shapes for Product Knowledge and reviewed walkthrough output

ai/
→ Stable AI workflows that discover, consume, validate, and update Product Knowledge
```

Temporary product work, initiative drafts, PRD drafts, recordings, screenshots, raw walkthrough notes, and walkthrough outputs belong in the separate `product-work` repository.

## Main principles

- Canonical documentation describes approved current product behavior.
- Proposed or unreleased behavior is not canonical.
- The default documentation set is Product overview, Capability, and Flow.
- Domain and Decision documents are created only when their additional responsibility is needed.
- Major user journeys live inside the Product overview; Journey is not a separate canonical document type, template, or folder.
- Feature is not a canonical Product Knowledge type; use Capability for durable product abilities.
- User outcomes, usage contexts, rules, states, and lifecycles are content inside their owning documents, not separate document types.
- Shared knowledge belongs in `shared/` only when its meaning and ownership are genuinely cross-product.
- Every durable product fact has one canonical owner; related documents reference rather than redefine it.
- Evidence, coverage limitations, unknowns, and blocked areas must remain visible.
- Document truth state is separate from document maturity.
- Stable metadata and generated discovery indexes help AI retrieve the smallest sufficient set of documents.
- AI prepares evidence, drafts, and documentation changes; humans approve semantic decisions and final diffs.

## Knowledge model

The repository uses a minimal model centered on Product overview, Capability, Flow, Domain, and Decision.

See [`knowledge-model.md`](knowledge-model.md) for canonical definitions, ownership rules, metadata, retrieval, and the relationship with Scrum and delivery work.

See [`ai/retrieval-rules.md`](ai/retrieval-rules.md) for the default document-discovery and context-expansion behavior expected from AI workflows.

## Templates

Use the repository templates when creating or materially restructuring documents:

```text
templates/product-overview-template.md
templates/capability-template.md
templates/flow-template.md
templates/domain-template.md
templates/decision-template.md
templates/walkthrough-output-template.md
```

Templates define required structure and metadata. Skills define how evidence is collected, validated, and converted into Product Knowledge.

## Main workflows

### Product walkthrough

```text
A bounded product area is selected
→ AI records scope, actor, role, authentication state, and environment
→ AI inventories surfaces and entry points
→ AI follows actions through outcomes and meaningful branches
→ AI records evidence and a coverage matrix
→ Humans review gaps, unknowns, and suspected bugs
→ Reviewed walkthrough output becomes eligible input for Product Knowledge update
```

See:

```text
ai/skills/product-walkthrough/SKILL.md
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
Approved change is released or a walkthrough output is reviewed
→ AI validates source readiness and coverage
→ AI identifies canonical owners
→ AI prepares template-compliant patches
→ Humans review the semantic diff
→ Approved changes are merged
```

See:

```text
ai/skills/product-knowledge-update/SKILL.md
```
