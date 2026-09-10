# Design Tokens

> Status: draft

This section defines the v4 Color token architecture, naming, semantics, Product/Appearance theme dimensions, Brand mappings, and approved component-owned Color exceptions. Non-color foundations such as Typography, Spacing, Radius, Elevation, and Motion document their own token structures and are not required to follow the Color graph.

## Documents

- `architecture.md` — Color collection and resolution model for Primitive, Brand, Semantic, and Component usage
- `primitive-tokens.md` — Raw design values and current Primitive color inventory
- `jobvision-color-tokens-v4-surface-model.md` — Current color-token catalog and canonical v4 Surface-model specification
- `jobvision-color-tokens-v3-surface-model.md` — Historical v3 working draft retained for migration reference
- `color-token-aliases.md` — Appearance-specific Color alias targets and unresolved value mappings
- `semantic-tokens.md` — Stable shared UI Color roles and Appearance resolution constraints
- `component-tokens.md` — Criteria and catalog for approved component-specific token exceptions; the current Color exception is Tag
- `product-overrides.md` — Product-identity rules and Product × Appearance application constraints
- `usage-rules.md` — Semantic Color consumption, fallbacks, and migration rules

## Color Resolution Model

```text
Core path
Primitive
→ Semantic
→ Component

Optional product-identity branch
Primitive
→ Brand
→ Semantic
```

Brand is not a mandatory hop. Semantic roles use the Brand branch only when their value intentionally depends on Product identity; otherwise they may alias Primitive values directly.

Components consume Semantic Color tokens by default. Approved component-owned Color exceptions are exposed through Component tokens; the current retained exception is the Tag family.

## Theme terminology

The two logical Theme dimensions are:

```text
Product    → JobVision | Cando
Appearance → Light | Dark
```

Product identity may feed Semantic roles through the optional Brand branch. Appearance controls Light/Dark Semantic resolution. The exact Figma collection/mode implementation for Product × Appearance remains a separate open decision.

For example, Cando Brand resolves to Yellow while Cando Accent can resolve directly to the shared Blue Primitive family because Accent does not currently vary by Product.

The former Productive/Expressive Experience Color collection and root `canvas` role are removed in v4.

Existing Figma names that still include `Productive` are legacy naming references unless a component explicitly documents another active dimension.

Exact opaque Primitive scales and final alias steps remain open until the palette pass. Semantic structure should not be expanded only to anticipate hypothetical future values.
