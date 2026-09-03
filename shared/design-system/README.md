# Design System Knowledge

This directory contains the canonical **meaning and usage knowledge** of the shared JobVision / Cando Design System.

The goal is not to reproduce Figma, Storybook, code, or every standards document in Markdown. Keep durable decisions here and route exact live specifications to their owning source.

## Start here

```text
DESIGN.md
→ design intent and default choices

STRUCTURE.md
→ what belongs where

components/ or patterns/
→ reusable decision contracts

foundations/, tokens/, experience-rules/, accessibility/
→ load only when the task needs specialized rules

integrations/source-of-truth.md
→ resolve Figma / code / knowledge ownership
```

## Documentation rule

Prefer **small, high-confidence documents with clear ownership** over exhaustive pages.

A document should primarily contain information that cannot be reliably derived from a live source:

- why and when to use something;
- semantic meaning and decision rules;
- important behavior/composition constraints;
- component-specific accessibility requirements;
- known gaps and unsupported behavior.

Do not manually duplicate generated props, token values, every Figma property, every visual permutation, or migration history when a live source can own them.

## Sections

- `foundations/` — durable visual/system models
- `tokens/` — token architecture, semantics, and approved mappings
- `components/` — reusable component decision contracts
- `patterns/` — reusable composition and flow contracts
- `experience-rules/` — cross-component interaction rules only
- `accessibility/` — accessibility baseline and specialized rules
- `product-variations/` — approved product-specific Design System differences
- `integrations/` — source-of-truth boundaries and live-system references
- `governance/` — ownership, maturity, contribution, maintenance
- `templates/` — minimum authoring structures
