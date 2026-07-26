# Product Knowledge

This repository contains the permanent, canonical knowledge of the product ecosystem.

It is organized into three main layers:

```text
shared/
→ Knowledge that is consistent across multiple products

products/
→ Product-specific overviews, capabilities, flows, domains, decisions, and optional complex journeys

ai/
→ Stable AI workflows that discover, consume, and update Product Knowledge
```

Temporary product work, initiative drafts, PRD drafts, recordings, screenshots, and walkthrough notes belong in the separate `product-work` repository.

## Main principles

- Canonical documentation describes approved current product behavior.
- Proposed or unreleased behavior is not canonical.
- The default documentation set is Product overview, Capability, and Flow.
- Domain and Decision documents are created only when their additional responsibility is needed.
- Major user journeys normally live in the Product overview; separate Journey documents are optional for complex cases.
- User goals, usage contexts, rules, states, and lifecycles are content inside their owning documents, not separate document types.
- Shared knowledge should be placed in `shared/` only when its meaning and ownership are genuinely cross-product.
- Product-specific rules remain inside the relevant product.
- Every durable product fact has one canonical owner; related documents reference rather than redefine it.
- Document truth state is separate from document maturity.
- Stable metadata and generated discovery indexes help AI retrieve the smallest sufficient set of documents.
- AI prepares documentation changes; humans approve semantic decisions and final diffs.

## Knowledge model

The repository uses a minimal model centered on Product overview, Capability, Flow, Domain, and Decision.

See [`knowledge-model.md`](knowledge-model.md) for canonical definitions, ownership rules, optional Journey guidance, metadata, retrieval, and the relationship with Scrum and delivery work.

See [`ai/retrieval-rules.md`](ai/retrieval-rules.md) for the default document-discovery and context-expansion behavior expected from AI workflows.

## Main workflows

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
Approved change is released
→ AI identifies affected canonical documents
→ AI prepares patches
→ Humans review the diff
→ Approved changes are merged
```

See:

```text
ai/skills/product-knowledge-update/SKILL.md
```

### Knowledge recovery through walkthrough

```text
Current behavior is unclear
→ Temporary walkthrough in product-work
→ Reviewed output.md
→ Product Knowledge update workflow
```