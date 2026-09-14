# Design Tokens

This section contains the detailed Color contracts. Start with `../foundations/color.md` for the operational model and use the smallest detailed document needed for the question.

The target architecture separates a **shared Design System token contract** from **installable Theme packages that provide values**.

Non-Color Foundations such as Typography, Spacing, Radius, Elevation, Motion, and Responsive Layout keep their own contracts. Theme packages are Foundation-agnostic in architecture, but v1 Theme packages provide Color only.

## Current Color documents

- `architecture.md` — target shared-contract ↔ Theme-implementation model and Figma migration status
- `primitive-tokens.md` — current Primitive inventory and palette work; target runtime ownership is Theme-local
- `semantic-tokens.md` — stable shared UI Color roles and usage boundaries
- `color-token-aliases.md` — current validated Figma alias/value snapshot during migration
- `component-tokens.md` — component-token criteria; categorical Tag target Theme resolution remains open
- `product-overrides.md` — Product ↔ Theme selection and Brand semantic resolution
- `usage-rules.md` — Semantic Color consumption and migration rules

Historical/working catalogs remain migration/reference material only when they conflict with the reviewed contracts above.

## Target Color model

```text
Shared DS contract
  Semantic names + meanings
          │
          ▼
Installed Theme package
  Theme-local Primitives
  Light/Dark Semantic values
          │
          ▼
Product UI / Components
```

Product UI consumes Semantic Color by default. Theme-local Primitives are implementation detail.

Brand remains Semantic meaning, not a required runtime alias layer.

## Current Figma transition

```text
01 Primitives → Value
02 Brand      → JobVision | Cando
03 Semantic   → light | dark
04 Component  → Light | Dark
```

This is still the current editable Figma model. It will be migrated once the remaining categorical Tag/component Theme boundary is finalized.
