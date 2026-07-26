# Product Knowledge

This repository contains the permanent, canonical knowledge of the product ecosystem.

It is organized into three main layers:

```text
shared/
→ Knowledge that is consistent across multiple products

products/
→ Product-specific journeys, flows, features, domains, and decisions

ai/
→ Stable AI workflows that consume and update Product Knowledge
```

Temporary product work, initiative drafts, PRD drafts, recordings, screenshots, and walkthrough notes belong in the separate `product-work` repository.

## Main principles

- Canonical documentation describes approved product behavior.
- Proposed or unreleased behavior is not canonical.
- Shared knowledge should be placed in `shared/` only when its meaning and ownership are genuinely cross-product.
- Product-specific rules remain inside the relevant product.
- AI prepares documentation changes; humans approve semantic decisions and final diffs.

## Knowledge model

The repository separates business truth, user experience, capability, behavior, and decision history into related document types.

See [`knowledge-model.md`](knowledge-model.md) for the canonical definitions of Product, Domain, Subdomain, Journey, Task, Scenario, Feature, Flow, lifecycle, Rule, Decision, Shared knowledge, and design-system concepts.

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
