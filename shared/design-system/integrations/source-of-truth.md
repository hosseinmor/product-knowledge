---
id: design-system.reference.source-of-truth
collection: design-system
type: reference
title: Sources of Truth
summary: Defines which source owns design meaning, visual construction, runtime implementation, product behavior, and temporary change history.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.overview
  - design-system.structure
  - design-system.reference.figma
  - design-system.reference.code
---

# Sources of Truth

No single tool is the source of truth for every Design System fact.

Use ownership by question:

| Question | Primary source |
|---|---|
| Why does this component/pattern exist? | Design System Knowledge |
| When should it be used or avoided? | Design System Knowledge |
| What does a semantic token/state mean? | Design System Knowledge |
| What are the current editable visual properties/layouts? | Figma |
| What is the runtime API/default/implemented behavior? | Code / Storybook when available |
| Which examples and interaction tests actually run? | Storybook / test suite when available |
| What business rule or product workflow applies? | Product Knowledge |
| What changed during migration? | Migration/change artifact |

## Conflict rule

When sources disagree, do not silently merge them.

```text
Meaning / usage conflict
→ Design System Knowledge owner reviews

Visual construction conflict
→ Figma implementation is inspected and reconciled

Runtime/API conflict
→ Code implementation is inspected and reconciled

Product-behavior conflict
→ Product Knowledge owner resolves
```

A mismatch is a maintenance gap, not permission for AI to invent a compromise.

## Duplication rule

Do not manually duplicate facts that another live source can provide reliably.

Examples that normally belong outside prose documentation:
- generated component props and defaults;
- every Figma property/value combination;
- raw token-value catalogs;
- exhaustive rendered state permutations;
- test implementation details;
- historical token/component migration mappings after migration is complete.

Design System Knowledge should retain durable semantic decisions, decision rules, important constraints, and known gaps.

## AI use

AI should retrieve the smallest relevant knowledge set, then query the owning live source for exact facts. If a required source is unavailable or the contract is incomplete, surface the gap rather than guessing.
