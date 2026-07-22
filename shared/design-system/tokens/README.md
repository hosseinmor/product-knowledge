# Design Tokens

> Status: draft

This section defines the token architecture, naming, semantics, Experience modes, and product overrides.

## Documents

- `architecture.md` — Layer model, including the Productive and Expressive Experience modes
- `primitive-tokens.md` — Raw design values
- `semantic-tokens.md` — Stable interface roles and mode resolution constraints
- `component-tokens.md` — Criteria for justified component-specific tokens
- `product-overrides.md` — Product and brand mapping rules
- `usage-rules.md` — Mode selection, fallbacks, and migration rules

## Resolution Order

```text
Primitive
→ Semantic
→ Experience mode (Productive or Expressive)
→ Optional product override
→ Component usage
```
