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
surface-inset
surface-muted
surface-inverse
surface-control-*
surface-emphasis-*
surface-transparent-*
surface-brand-*
surface-selected-*
surface-disabled
surface-danger-*
surface-{info|success|warning|error}
```

`surface-muted` is passive and has no interaction states. `surface-control` is the visible neutral interactive background. The `bg-*` and `fill-*` families are deprecated.

## Foreground

Use `fg-*` for text and icons. On-surface pairings such as `fg-on-brand`, `fg-on-emphasis`, and `fg-on-selected` remain distinct because their contrast mappings can diverge.

## Line

Use `line-*` for borders, dividers, and indicators. Do not use `border-*` as the source-token family because it conflicts with Tailwind utilities.

## Support

Information, success, warning, and error meanings are invariant across all modes. Danger remains separate and is reserved for destructive actions.

## Focus

Use `focus-default` and `focus-inverse`. Focus must remain visible across every supported Brand × Experience × Semantic combination.

## Component-owned exception

Categorical Tag colors are component-owned rather than Semantic. Use the approved `tag-surface-*`, `tag-fg-*`, and `tag-line-*` families documented in `component-tokens.md`. They communicate grouping, not information, success, warning, or error.

## Source of truth

The complete token catalog, Button mappings, deprecations, Figma collection structure, and open implementation decisions are defined in `jobvision-color-tokens-v3-surface-model.md`. The mode-by-mode alias targets are defined separately in `color-token-aliases.md`.
