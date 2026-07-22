# Design Tokens

> Status: draft

This section defines the token architecture, naming, semantics, Experience modes, themes, and brand mappings.

## Documents

- `architecture.md` — Collection and resolution model for Primitive, Brand, Experience, Semantic, and component usage
- `primitive-tokens.md` — Raw design values
- `jobvision-color-tokens-v3-surface-model.md` — Current color-token catalog and canonical Surface-model specification
- `color-token-aliases.md` — Mode-by-mode alias targets for Brand, Experience, Semantic, and approved Component color variables
- `semantic-tokens.md` — Stable interface roles and Light/Dark resolution constraints
- `component-tokens.md` — Criteria and catalog for approved component-specific tokens, currently Tag
- `product-overrides.md` — Brand-mode rules and product application combinations
- `usage-rules.md` — Experience selection, semantic consumption, fallbacks, and migration rules

## Resolution Order

```text
Primitive
→ Brand
→ Experience
→ Semantic
→ Component
```

Components consume Semantic tokens by default. Approved component-owned exceptions are exposed through Component tokens; the current exception is the Tag color family. Productive/Expressive and Light/Dark are separate mode dimensions, and brand variation is resolved through the Brand collection.
