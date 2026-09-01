# Design Tokens

> Status: draft

This section defines the v4 Color token architecture, naming, semantics, themes, brand mappings, and approved component-owned Color exceptions. Non-color foundations such as Typography, Spacing, Radius, Elevation, and Motion document their own token structures and are not required to follow the Color Brand/Semantic graph.

## Documents

- `architecture.md` — Color collection and resolution model for Primitive, Brand, Semantic, and Component usage
- `primitive-tokens.md` — Raw design values and current Primitive color inventory
- `jobvision-color-tokens-v4-surface-model.md` — Current color-token catalog and canonical v4 Surface-model specification
- `jobvision-color-tokens-v3-surface-model.md` — Historical v3 working draft retained for migration reference
- `color-token-aliases.md` — Mode-by-mode Color alias targets and unresolved value mappings
- `semantic-tokens.md` — Stable shared UI Color roles and Light/Dark resolution constraints
- `component-tokens.md` — Criteria and catalog for approved component-specific token exceptions; the current Color exception is Tag
- `product-overrides.md` — Brand-mode rules and product application constraints
- `usage-rules.md` — Semantic Color consumption, fallbacks, and migration rules

## Color Resolution Order

```text
Primitive
→ Brand
→ Semantic
→ Component
```

Components consume Semantic Color tokens by default. Approved component-owned Color exceptions are exposed through Component tokens; the current retained exception is the Tag family.

Brand variation is resolved through the Brand collection. Light/Dark is resolved in Semantic. The former Productive/Expressive Experience Color collection and root `canvas` role are removed in v4.

Existing Figma names that still include `Productive` are legacy naming references unless a component explicitly documents another active dimension.

Exact opaque Primitive scales and final alias steps remain open until the palette pass. Semantic structure should not be expanded only to anticipate hypothetical future values.
