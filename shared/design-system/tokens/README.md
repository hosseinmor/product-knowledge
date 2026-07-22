# Design Tokens

> Status: draft

This section defines the token architecture, naming, semantics, Experience modes, themes, and brand mappings.

## Documents

- `architecture.md` — Collection and resolution model for Primitive, Brand, Experience, Semantic, and component usage
- `primitive-tokens.md` — Raw design values
- `jobvision-color-tokens-v3-surface-model.md` — Current color-token catalog and canonical Surface-model specification
- `semantic-tokens.md` — Stable interface roles and Light/Dark resolution constraints
- `component-tokens.md` — Criteria for justified component-specific tokens
- `product-overrides.md` — Brand-mode rules and product application combinations
- `usage-rules.md` — Experience selection, semantic consumption, fallbacks, and migration rules

## Resolution Order

```text
Primitive
→ Brand
→ Experience
→ Semantic
→ Component usage
```

Components consume Semantic tokens only. Productive/Expressive and Light/Dark are separate mode dimensions; brand variation is resolved through the Brand collection.
