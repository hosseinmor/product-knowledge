# Design Tokens

This section contains the detailed Color contracts. Start with `../foundations/color.md` for the operational model and use the smallest detailed document needed for the question.

The current architecture separates a **shared Design System token contract** from **installable Theme packages that provide values**.

Non-Color Foundations such as Typography, Spacing, Radius, Elevation, Motion, and Responsive Layout keep their own contracts. Theme packages are Foundation-agnostic in architecture, but v1 Theme packages provide Color only.

## Current Color documents

- `architecture.md` — shared-contract ↔ Theme-implementation model and current Figma representation
- `primitive-tokens.md` — current Primitive inventory and palette work; runtime ownership is Theme-local
- `semantic-tokens.md` — stable shared UI Color roles and usage boundaries
- `color-token-aliases.md` — current validated Figma Theme × Appearance mappings
- `component-tokens.md` — component-token criteria and the finalized categorical Tag Theme Extension
- `product-overrides.md` — Product ↔ Theme selection and Brand semantic resolution
- `usage-rules.md` — Semantic Color consumption and migration rules

Historical/working catalogs remain reference material only when they conflict with the reviewed contracts above.

## Color model

```text
Shared DS contract
  Semantic names + meanings
          │
          ▼
Installed Theme package
  Theme-local Primitives
  Light/Dark Semantic values
  approved sparse Component Extensions
          │
          ▼
Product UI / DS Components
```

Product UI consumes Semantic Color by default. Theme-local Primitives are implementation detail.

Brand remains Semantic meaning, not a required runtime alias layer.

Categorical Tag is currently the only approved sparse Component Theme Extension. Its `tag/*` contract is component-only and not Product-facing API.

## Current Figma model

```text
01 Primitives            → Value
02 Product               → JobVision | Cando
03 Semantic              → JobVision Light | JobVision Dark | Cando Light | Cando Dark
04 Component Extensions  → JobVision Light | JobVision Dark | Cando Light | Cando Dark
```

- `01 Primitives` is hidden.
- `02 Product` is hidden and currently carries `typography/font-family`; former Brand Color aliases are hidden legacy.
- `03 Semantic` is the published shared Color contract.
- `04 Component Extensions` is hidden and currently contains Tag extension values.
