# Design Tokens

> Status: draft

This section defines the v4 token architecture, naming, semantics, themes, brand mappings, and approved component-owned exceptions.

## Documents

- `architecture.md` — Collection and resolution model for Primitive, Brand, Semantic, and Component usage
- `primitive-tokens.md` — Raw design values and current Primitive color inventory
- `jobvision-color-tokens-v4-surface-model.md` — Current color-token catalog and canonical v4 Surface-model specification
- `jobvision-color-tokens-v3-surface-model.md` — Historical v3 working draft retained for migration reference
- `color-token-aliases.md` — Mode-by-mode alias targets and unresolved value mappings
- `semantic-tokens.md` — Stable shared UI roles and Light/Dark resolution constraints
- `component-tokens.md` — Criteria and catalog for approved component-specific tokens, currently Tag
- `product-overrides.md` — Brand-mode rules and product application constraints
- `usage-rules.md` — Semantic consumption, fallbacks, and migration rules

## Resolution Order

```text
Primitive
→ Brand
→ Semantic
→ Component
```

Components consume Semantic tokens by default. Approved component-owned exceptions are exposed through Component tokens; the current color exception is the Tag family.

Brand variation is resolved through the Brand collection. Light/Dark is resolved in Semantic. The former Productive/Expressive Experience collection and root `canvas` role are removed in v4.

Exact opaque Primitive scales and final alias steps remain open until the palette pass. Semantic structure should not be expanded only to anticipate hypothetical future values.
