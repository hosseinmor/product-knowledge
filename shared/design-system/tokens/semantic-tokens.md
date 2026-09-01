---
id: design-system.token.semantic-tokens
collection: design-system
type: token
title: Semantic Tokens
summary: '> Status: draft'
knowledge_state: unverified
document_maturity: draft
related: []
---

# Semantic Tokens

> Status: draft

Semantic tokens are the default color interface consumed by components. Their role meaning remains stable across Brand modes and Light/Dark themes.

## Resolution

```text
Primitive Value
→ Brand: Jobvision or Cando
→ Semantic: Light or Dark
→ Component
```

Brand provides product-identity inputs where required. Semantic may also alias generic Primitive hue scales directly when a role does not vary by product. Components do not consume Brand directly.

## Surface

Structural surfaces:

```text
surface/default
surface/muted
surface/inset
surface/raised
surface/inverse
```

Interactive neutral surfaces:

```text
surface/neutral-muted
surface/neutral-muted-hover
surface/neutral-muted-active

surface/neutral-emphasis
surface/neutral-emphasis-hover
surface/neutral-emphasis-active
```

Transparent interaction states:

```text
surface/transparent-hover
surface/transparent-active
surface/transparent-inverse-hover
surface/transparent-inverse-active
```

Persistent neutral selected containers:

```text
surface/selected
surface/selected-hover
```

Brand:

```text
surface/brand
surface/brand-hover
surface/brand-active
```

Accent:

```text
surface/accent-muted
surface/accent-muted-hover
surface/accent-muted-active

surface/accent-emphasis
surface/accent-emphasis-hover
surface/accent-emphasis-active
```

Magic:

```text
surface/magic-muted
surface/magic-emphasis
surface/magic-emphasis-hover
surface/magic-emphasis-active
```

Danger:

```text
surface/danger-muted
surface/danger-emphasis
surface/danger-emphasis-hover
surface/danger-emphasis-active
```

Support:

```text
surface/info-muted
surface/success-muted
surface/warning-muted
surface/error-muted
```

Disabled:

```text
surface/disabled
```

`canvas`, `surface/floating`, the v3 `surface/control*` and `surface/emphasis*` names, `surface/brand-muted`, and the expanded v3 Selected surface matrix are removed in v4.

### Surface meanings

- `surface/default` is the ordinary base content surface and default root page/workspace surface.
- `surface/muted` is passive lower-emphasis structure and has no interaction states.
- `surface/inset` is behind `surface/default` in the local hierarchy and may represent recessed regions, workspace chrome, or structural backdrops.
- `surface/raised` is elevated relative to its parent and includes menus, popovers, dropdowns, floating panels, and appropriate dialogs. Elevation/shadow remains separate.
- `surface/neutral-muted` is a visible neutral interactive treatment; it is not interchangeable with structural `surface/muted`.
- `surface/neutral-emphasis` is the strong neutral interactive treatment used by operational Primary actions.
- `surface/selected` is specifically a neutral persistent selected-container background, not a general Selected color family.
- `surface/brand` is reserved for product identity and approved key product/conversion moments.
- Accent communicates chromatic interaction/affordance and may be used by component selection states when a colored cue is appropriate.

The `bg-*` and `fill-*` families remain deprecated.

## Foreground

Use `fg/*` for text and icons.

General hierarchy and input roles:

```text
fg/primary
fg/secondary
fg/tertiary
fg/placeholder
fg/disabled
```

Contextual foregrounds:

```text
fg/on-inverse
fg/on-brand
fg/on-color
```

Colored semantics:

```text
fg/accent
fg/magic
fg/danger

fg/info
fg/success
fg/warning
fg/error
```

Colored Support content on inverse surfaces:

```text
fg/info-inverse
fg/success-inverse
fg/warning-inverse
fg/error-inverse
```

`fg/brand`, `fg/selected`, and `fg/on-color-disabled` are not part of v4. Disabled filled controls suppress tone and use `surface/disabled + fg/disabled`.

## Line

```text
line/muted
line/default
line/emphasis
line/disabled
line/inverse

line/accent
line/magic
line/danger

line/info
line/success
line/warning
line/error
```

Use `line/accent` for chromatic indicators such as the selected indicator of a line Tab when the component calls for an Accent cue. `line/brand` and `line/selected` are removed.

Keep `line` rather than `border` as the source-token family to avoid collision with implementation utility naming.

## Selection

Selection is a component state rather than a parallel global color family.

A selected/current/checked/on/applied component may express its state with existing Semantic roles according to anatomy:

```text
selected line Tab → fg/primary + line/accent
checked checkbox  → surface/accent-emphasis + fg/on-color
saved bookmark    → fg/accent
selected row      → surface/selected + fg/primary
```

Only persistent neutral selected-container backgrounds receive dedicated global tokens: `surface/selected` and `surface/selected-hover`.

## Brand and Accent

Brand and Accent are separate semantics even when JobVision maps both to the same Blue Primitive family.

```text
Brand  → identity + approved key conversion moments
Accent → chromatic interaction / affordance
```

Cando demonstrates the distinction clearly: Brand resolves to Yellow while Accent resolves to Blue.

## Support

Information, success, warning, and error meanings are invariant across products and themes. Danger remains separate and is reserved for destructive actions.

Only muted Support surfaces are approved globally. The inverse Support foregrounds are retained specifically for colored Support content on `surface/inverse`, such as inverse Toast patterns.

## Focus

```text
focus/default
focus/inverse
```

Focus remains independent from Brand and Accent and must remain visible across supported products, themes, and surfaces.

## Link

```text
link/default
link/hover

link/subtle
link/subtle-hover

link/inverse
link/inverse-hover
```

- Default is the recognizable chromatic link.
- Subtle is the intentional neutral lower-prominence link for contexts where clickability is already clear.
- Inverse adapts Link for `surface/inverse`; one inverse treatment is approved in v4.
- Link remains an independent semantic family even when it resolves to the same Blue Primitive family as Accent.

`link/visited`, `link/emphasis`, and `link/emphasis-hover` are removed in v4. Visited may return only when a real product pattern requires it.

## Utility roles

```text
highlight/default
highlight/inverse
overlay/default
skeleton/base
skeleton/shimmer
```

`overlay/default` is a backdrop/scrim role, not a Surface.

## Component-owned exception

Categorical Tag colors are component-owned rather than Semantic. Use the approved `tag/surface/*`, `tag/fg/*`, and `tag/line/*` families documented in `component-tokens.md`. They communicate grouping, not information, success, warning, or error.

## Source of truth

The complete v4 token catalog, Button mappings, deprecations, and open implementation decisions are defined in `jobvision-color-tokens-v4-surface-model.md`. Mode-by-mode alias targets and unresolved values are recorded in `color-token-aliases.md`.
