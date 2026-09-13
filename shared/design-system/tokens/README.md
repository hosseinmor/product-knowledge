# Design Tokens

This section contains the detailed v4 Color contracts. Start with `../foundations/color.md` for the operational model and use the smallest detailed document needed for the question.

Non-Color foundations such as Typography, Spacing, Radius, Elevation, and Motion define their own token structures and are not required to follow the Color graph.

## Current Color documents

- `architecture.md` — finalized Color layering, Figma collections, and Product × Appearance responsibilities
- `primitive-tokens.md` — Primitive Color inventory and raw palette values
- `semantic-tokens.md` — stable shared UI Color roles and usage boundaries
- `color-token-aliases.md` — validated current Brand, Semantic, and Tag mappings synchronized with Figma
- `component-tokens.md` — criteria for Component Color exceptions and the finalized categorical Tag contract
- `product-overrides.md` — Product identity, Brand mappings, and Product × Appearance constraints
- `usage-rules.md` — Semantic Color consumption and migration rules
- `frontend-token-contract.md` — draft Design-side runtime package, public/internal API, alias-preservation, naming, and enforcement contract; Frontend review is still required

Historical/working catalogs:

- `jobvision-color-tokens-v4-surface-model.md` — earlier detailed v4 working catalog retained for decision history; do not use it as the source for exact current alias values when it conflicts with the reviewed contracts above
- `jobvision-color-tokens-v3-surface-model.md` — historical v3 migration reference

## Color resolution model

```text
Default
Primitive → Semantic → Product UI

Optional Product identity
Primitive → Brand → Semantic → Product UI

Exceptional component-owned contract
Primitive / Semantic / Brand → Component → Product UI
```

Brand is not mandatory. Semantic roles use Brand only when Product identity intentionally controls the value.

Product UI consumes Semantic Color by default. Component Color tokens are reviewed exceptions; the current approved exception is categorical Tag Color.

## Runtime consumption boundary

Current Design-side direction for frontend consumption is:

```text
Primitive → internal runtime dependency
Brand → internal runtime dependency
Semantic → public Product API
Component → public only for approved component-owned contracts
```

Runtime presence does not make a token public. See `frontend-token-contract.md` for the draft package/enforcement contract and the remaining Frontend review questions.

## Theme dimensions

```text
Product    → JobVision | Cando
Appearance → Light | Dark
```

Product and Appearance are independent. Current Figma resolution:

```text
01 Primitives → Value
02 Brand      → JobVision | Cando
03 Semantic   → light | dark
04 Component  → Light | Dark
```

The Figma collection/mode model and Color alias values are finalized for the current scope. Runtime Theme initialization, CSS representation, Tailwind mapping, and SSR behavior remain separate implementation contracts.
