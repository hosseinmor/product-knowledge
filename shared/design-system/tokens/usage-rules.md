# Token Usage Rules

> Status: draft

## Allowed usage

- Components consume Semantic tokens only.
- Select Brand, Experience, and Semantic modes independently.
- Use Productive for operational product interfaces and Expressive for discovery, editorial, marketing, or other intentionally prominent experiences.
- Use `canvas` only for the root page or workspace background.
- Use `surface-*` for every UI background above canvas.
- Document non-default mode combinations in the design specification.
- Test every supported Brand × Experience × Semantic combination for accessibility.

## Surface selection

- Normal container, card, panel, sheet, modal, or popover → `surface-default`
- Nested recessed region → `surface-inset`
- Passive supporting or grouping region → `surface-muted`
- Visible neutral interactive control → `surface-control`
- High-emphasis neutral action → `surface-emphasis`
- Transparent-at-rest interaction → `surface-transparent-hover/active`
- Brand conversion action → `surface-brand-emphasis`
- Destructive action → `surface-danger-emphasis`
- Validation or system feedback → matching support surface, foreground, and line roles

Do not use `surface-muted` as an interactive control background.

## Prohibited usage

- Do not consume Primitive, Brand, or Experience variables from components.
- Do not encode mode or product names into Semantic token names.
- Do not use deprecated `bg-*`, `fill-*`, `fg-on-fill`, `fg-on-primary`, `focus`, or `focus-ring` names for new work.
- Do not let a mode change action meaning, validation, state meaning, or interaction behavior.
- Do not invent hover or active states for passive or disabled surfaces.
- Do not introduce undocumented mixed-mode regions.

## Fallbacks

- Semantic Light/Dark mappings must resolve the active Brand and Experience inputs.
- If an intended Expressive mapping is not defined, use the approved Productive value and record the gap.
- If a proposed value fails accessibility, use an accessible approved mapping.
- Never fall back from Semantic directly to an arbitrary primitive at component level.

## Migration rules

1. Replace root `bg-canvas` usage with `canvas`.
2. Replace other `bg-*` and `fill-*` roles using the mapping in `jobvision-color-tokens-v3-surface-model.md`.
3. Keep Brand, Experience, and Light/Dark as separate collection modes.
4. Update Figma and code references together when final implementation mappings are approved.
5. Validate visual regression, contrast, focus, reduced motion, and supported themes.
6. Record open values and mappings as open decisions; do not present provisional v3 values as final.

See `architecture.md` and `jobvision-color-tokens-v3-surface-model.md`.
