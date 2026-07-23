# Token Usage Rules

> Status: draft

## Allowed usage

- Components consume Semantic tokens by default; use an approved Component token only for its documented owner component.
- Select Brand, Experience, and Semantic modes independently.
- Use Productive for operational product interfaces and Expressive for discovery, editorial, marketing, or other intentionally prominent experiences.
- Use `canvas` only for the root page or workspace background.
- Use Semantic `surface-*` for every general UI background above canvas. The approved Tag component uses its own `tag-surface-*` family.
- Document non-default mode combinations in the design specification.
- Test every supported Brand × Experience × Semantic combination for accessibility.

## Surface selection

- Normal container, card, panel, sheet, modal, or popover → `surface-default`
- Nested recessed region → `surface-inset`
- Passive supporting or grouping region → `surface-muted`
- Visible neutral interactive control → `surface-control`
- High-emphasis neutral action → `surface-emphasis`
- Transparent-at-rest interaction → `surface-transparent-hover/active`
- Transparent interaction on inverse surface → `surface-transparent-inverse-hover/active`
- Brand conversion action → `surface-brand-emphasis`
- AI-assisted or generated treatment → matching `surface-magic-*`, `fg-magic`, and `line-magic` roles
- Selected state → matching `surface-selected-*` role; use the inverse family on `surface-inverse`
- Destructive action → `surface-danger-emphasis`
- Validation or system feedback → matching `surface-*-muted`, foreground, and line roles

Do not use `surface-muted` as an interactive control background.

## Prohibited usage

- Do not consume Primitive, Brand, or Experience variables directly from component implementations. Approved Component tokens may alias documented Primitive or Semantic sources.
- Do not encode mode or product names into Semantic token names.
- Do not use deprecated `bg-*`, `fill-*`, `fg-subtle`, `fg-inverse`, `fg-on-fill`, `fg-on-primary`, `fg-on-emphasis`, `fg-on-selected`, `line-subtle`, `line-strong`, `focus`, or `focus-ring` names for new work.
- Do not let a mode change action meaning, validation, state meaning, or interaction behavior.
- Do not invent hover or active states for passive or disabled surfaces.
- Do not introduce undocumented mixed-mode regions.

## Fallbacks

- Semantic Light/Dark mappings must resolve the active Brand and Experience inputs.
- If an intended Expressive mapping is not defined, use the approved Productive value and record the gap.
- If a proposed value fails accessibility, use an accessible approved mapping.
- Never fall back from Semantic or an approved Component token to an arbitrary primitive in component implementation.

## Migration rules

1. Replace root `bg-canvas` usage with `canvas`.
2. Replace other `bg-*` and `fill-*` roles using the mapping in `jobvision-color-tokens-v3-surface-model.md`.
3. Keep Brand, Experience, and Light/Dark as separate collection modes.
4. Apply the v3 renames together in Figma and code: `fg-subtle → fg-tertiary`, `fg-inverse → fg-on-inverse`, `fg-on-emphasis/fg-on-selected → fg-on-color`, `line-subtle → line-muted`, and `line-strong → line-emphasis`.
5. Update Figma and code references together when final implementation mappings are approved.
6. Validate visual regression, contrast, focus, reduced motion, and supported themes.
7. Record open values and mappings as open decisions; do not present provisional v3 values as final.
8. Migrate the former categorical family to the approved `tag-surface-*`, `tag-fg-*`, and `tag-line-*` Component tokens; do not create new `categorical-*` names.

See `architecture.md`, `jobvision-color-tokens-v3-surface-model.md`, and `color-token-aliases.md`.
