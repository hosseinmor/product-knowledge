---
id: design-system.structure
collection: design-system
type: overview
title: Design System Knowledge Structure
summary: Defines the compact post-AI knowledge architecture and source boundaries for the shared Design System.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.design-language
  - design-system.overview
  - design-system.reference.source-of-truth
---

# Design System Knowledge Structure

The physical folders stay stable, but the system is intentionally understood as **five knowledge layers**.

```text
1. DESIGN.md
   Global design intent and default choices

2. Foundations + Tokens
   Shared models and semantic vocabulary

3. Components + Patterns
   Reusable decision contracts

4. Specialized Rules
   Experience Rules + Accessibility + Product Variations

5. Integrations + Governance
   Live-source boundaries, maturity, ownership, maintenance
```

Current folders:

```text
design-system/
├── DESIGN.md
├── README.md
├── overview.md
├── foundations/
├── tokens/
├── components/
├── patterns/
├── experience-rules/
├── accessibility/
├── product-variations/
├── integrations/
├── governance/
└── templates/
```

## What belongs where

### `DESIGN.md`

Only durable design language that should shape many design decisions. Keep it compact. Do not turn it into a full token catalog or component manual.

### Foundations and Tokens

Own shared system models and semantic vocabulary. Exact machine-readable values should come from the designated token/live source when available; Markdown explains meaning and usage rules.

### Components

Own the reusable component decision contract:
- purpose;
- when to use / avoid;
- meaningful choices and variants;
- non-obvious behavior and states;
- composition/content constraints;
- component-specific accessibility;
- known gaps;
- live references.

Do not copy generated API tables, every Figma property, every token value, or migration history into component guidance by default.

### Patterns

Own behavior that emerges from composing multiple components or from a reusable flow. Product-specific business policy stays in Product Knowledge.

### Experience Rules

Own a rule only when it genuinely applies across several components/patterns. If a rule is component-specific, keep it in that component. If it is an accessibility requirement, the Accessibility corpus owns the normative rule.

### Accessibility

Own the shared accessibility baseline and specialized standards guidance. Mature component/pattern contracts may encapsulate relevant mechanics; incomplete contracts fail open to specialized guidance.

### Product Variations

Own intentional Design System differences between JobVision and Cando. Do not put ordinary product business logic here.

### Integrations

Describe source-of-truth boundaries and how Figma, code, Storybook when available, and the knowledge repository relate. Do not mirror their complete content.

### Governance

Own maturity, ownership, contribution, maintenance, and validation rules.

## Retrieval model

```text
DESIGN.md
→ relevant Component / Pattern
→ only relevant specialized rules
→ query live implementation/design source for exact facts
```

AI should not read the entire Design System by default.

## Source boundary

- **Design System Knowledge** → meaning, usage, semantic decisions, relationships, known gaps.
- **Figma** → editable visual assets and construction.
- **Code / Storybook** → runtime API, implementation behavior, executable examples and tests.
- **Product Knowledge** → product-specific behavior and business rules.
- **Product Work / migration artifacts** → temporary proposals and change history.

See `integrations/source-of-truth.md` when sources disagree.
