# Design System Knowledge

This directory contains the canonical **decision knowledge** of the shared JobVision/Cando Design System.

The goal is not to mirror Figma, Storybook, code, or token data in Markdown. Keep durable meaning and decisions here; query live sources for exact implementation facts.

## Start here

For design work:

```text
DESIGN.md
→ relevant Component / Pattern
→ only relevant specialized rules
→ live Figma / Code / Storybook source for exact facts
```

Do not read the whole Design System by default.

## Knowledge layers

1. **`DESIGN.md`** — compact design language and default intent.
2. **Foundations + Tokens** — shared models and semantic vocabulary.
3. **Components + Patterns** — reusable decision contracts.
4. **Specialized Rules** — Experience Rules, Accessibility, and Product Variations.
5. **Integrations + Governance** — source boundaries, ownership, maturity, and maintenance.

See `STRUCTURE.md` for the detailed ownership model and `integrations/source-of-truth.md` when sources disagree.

## Documentation principle

Prefer **minimum useful documentation with broad coverage** over exhaustive prose for a small subset of components.

A document should usually explain only what another reliable live source cannot answer by itself:
- why something exists;
- when to use or avoid it;
- semantic meaning;
- meaningful choices;
- non-obvious behavior;
- composition constraints;
- component/pattern-specific accessibility;
- known gaps.

Do not manually copy generated API tables, every Figma property, exhaustive state permutations, raw token catalogs, test implementation, or completed migration history into normal runtime guidance.

Documentation depth should follow complexity: simple/native components stay compact; composite/custom widgets need fuller behavior/accessibility contracts.
