# Semantic Tokens

> Status: draft

Semantic tokens are the default color interface consumed by components. Their role meaning remains stable across Brand, Experience, and Light/Dark modes.

## Resolution

```text
Primitive Value
→ Brand: Jobvision or Cando
→ Experience: Productive or Expressive
→ Semantic: Light or Dark
→ Component
```

Brand and Experience provide inputs to Semantic mappings. Components never consume those collections directly. An approved Component token may alias a Primitive or Semantic source when no shared semantic role exists.

## Backgrounds

The root background is:

```text
canvas
```

All UI backgrounds above canvas use the unified Surface family:

```text
surface-default
surface-raised
surface-inset
surface-muted
surface-inverse
surface-control-*
surface-emphasis-*
surface-transparent-*
surface-transparent-inverse-*
surface-brand-*
surface-magic-*
surface-selected-*
surface-selected-inverse-*
surface-disabled
surface-danger-*
surface-{info|success|warning|error}-muted
```

- `surface-default` is the ordinary background for containers that remain in the document or layout flow.
- `surface-raised` is the background for a surface visually elevated above its immediate parent, including menus, popovers, dropdowns, floating panels, and non-full-screen dialogs. Pair it with the approved elevation token when depth must be visible.
- `surface-inset` is a recessed nested region.
- `surface-muted` is passive and has no interaction states.
- `surface-control` is the visible neutral interactive background.

`surface-raised` is a color role, not an elevation value. It may alias the same primitive as `surface-default` in Light mode while resolving differently in Dark mode. Components must still apply the appropriate shadow or elevation token when the pattern requires visual depth.

The `bg-*` and `fill-*` families are deprecated.

## Foreground

Use `fg-*` for text and icons.

- General hierarchy: `fg-primary`, `fg-secondary`, `fg-tertiary`
- Input role: `fg-placeholder`
- Contextual content: `fg-on-inverse`, `fg-on-brand`, `fg-on-color`, `fg-on-color-disabled`
- Semantic color: Brand, Magic, Danger, and Support roles
- Colored Support on inverse surfaces: `fg-{info|success|warning|error}-inverse`

`fg-subtle`, `fg-inverse`, `fg-on-emphasis`, and `fg-on-selected` are deprecated.

## Line

Use `line-*` for borders, dividers, and indicators. The neutral hierarchy is `line-muted`, `line-default`, and `line-emphasis`; `line-inverse` is for inverse surfaces. Do not use `border-*` as the source-token family because it conflicts with Tailwind utilities.

## Support

Information, success, warning, and error meanings are invariant across all modes. Danger remains separate and is reserved for destructive actions.

## Focus

Use `focus-default` and `focus-inverse`. Focus must remain visible across every supported Brand × Experience × Semantic combination.

## Link and utility roles

Link provides Default, Hover, Visited, Emphasis, Emphasis Hover, Inverse, and Inverse Hover roles.

Highlight, Overlay, and Skeleton remain Semantic utilities:

```text
highlight-default
highlight-inverse
overlay-default
skeleton-base
skeleton-shimmer
```

## Component-owned exception

Categorical Tag colors are component-owned rather than Semantic. Use the approved `tag-surface-*`, `tag-fg-*`, and `tag-line-*` families documented in `component-tokens.md`. They communicate grouping, not information, success, warning, or error.

## Source of truth

The complete token catalog, Button mappings, deprecations, Figma collection structure, and open implementation decisions are defined in `jobvision-color-tokens-v3-surface-model.md`. The mode-by-mode alias targets are defined separately in `color-token-aliases.md`.
