# Token Usage Rules

> Status: draft

## Allowed Usage

- Consume semantic roles through the active Experience mode.
- Use Productive as the default for product application interfaces.
- Select Expressive for a defined surface or journey only when brand expression or emotional emphasis is part of the intended experience.
- Apply product overrides after the Experience mode has been selected.
- Document the selected mode in the design specification when it differs from the product default.
- Test every mode and product-override combination used in production for accessibility.

## Mode Selection

Choose Productive when the experience is primarily:

- Frequent or repeatable
- Task-focused
- Dense or data-heavy
- Operational
- Time-sensitive

Consider Expressive when the experience is intentionally:

- Brand-forward
- Editorial or campaign-led
- Introductory or celebratory
- Designed as a prominent moment rather than a repeated work surface

When uncertain, use Productive.

## Prohibited Usage

- Do not select a mode independently for individual components.
- Do not use Expressive as a visual importance switch.
- Do not encode mode names into duplicated semantic token families.
- Do not let a mode change action meaning, state meaning, validation, or interaction behavior.
- Do not treat Productive or Expressive as a light/dark theme, product variant, responsive breakpoint, component variant, or density setting.
- Do not bypass semantic tokens by mapping component values directly to primitives.
- Do not introduce an undocumented mixed-mode region.

## Fallbacks

- If a component has no approved Expressive mapping, use its Productive mapping.
- If an Expressive value fails accessibility requirements, use the accessible Productive value or another approved semantic mapping.
- If a product override is missing, use the shared mapping for the active mode.
- A fallback must preserve semantic meaning and be recorded as a known gap when it affects the intended experience.

## Migration Rules

1. Keep existing semantic role names stable.
2. Treat existing product interfaces as Productive unless a documented decision selects Expressive.
3. Add Experience mode mappings without duplicating component variants.
4. Apply product overrides as a separate resolution step.
5. Validate visual regression, contrast, focus, reduced motion, and responsive behavior.
6. Record unsupported Expressive mappings instead of creating local one-off tokens.

See `architecture.md` for the complete layer model.
