---
id: design-system.token.jobvision-color-tokens-v4-surface-model
collection: design-system
type: token
title: JobVision Color Tokens v4 — Surface Model
summary: '> Status: working draft'
knowledge_state: unverified
document_maturity: draft
related: []
---

# JobVision Color Tokens v4 — Surface Model

> Status: working draft  
> Theme scope: Light + Dark  
> Product scope: JobVision + Cando  
> Implementation mapping: open decision

This document is the canonical v4 color-token catalog. It records the approved semantic structure. Exact opaque Primitive scale values and final Light/Dark alias steps remain intentionally open until the palette pass.

## Architecture

```text
01 Primitives
      ↓
02 Brand
      ↓
03 Semantic
      ↓
04 Component
```

Collections and modes:

```text
01 Primitives
- Value

02 Brand
- Jobvision
- Cando

03 Semantic
- Light
- Dark

04 Component
- Light
- Dark
```

`Experience` is removed in v4. The former Productive/Expressive distinction was only resolving the root canvas and did not justify a dedicated alias layer.

Components consume Semantic tokens by default. Component tokens remain exceptional and are created only when a stable component-owned contract cannot be expressed by the shared Semantic vocabulary.

Figma variable names use slash grouping. Code may flatten `/` to `-` when implementation mapping is approved.

---

## Primitive color model

Primitive color scales are context-free and are named by hue rather than product ownership.

```text
color/neutral/*
color/blue/*
color/yellow/*
color/red/*
color/purple/*
color/green/*
color/emerald/*
color/orange/*
color/black-alpha/*
color/white-alpha/*
```

Remove product-owned Primitive families such as:

```text
color/brand/jobvision/*
color/brand/cando/*
```

Current brand color anchors:

```text
JobVision blue  → #0053FF
Cando yellow    → #FFC400
```

The exact 50–950 scale values and the final `green` versus `emerald` inventory remain open.

A Primitive palette may feed multiple independent semantic meanings. Sharing a Primitive value does not merge semantic roles.

```text
blue/*
├─ JobVision Brand
├─ Accent
├─ Link
├─ Info
└─ categorical blue

yellow/*
├─ Cando Brand
├─ Warning
└─ categorical yellow when needed
```

Do not create a second blue or yellow palette only to preserve semantic separation. Create a new Primitive family only when tonal or contrast requirements prove that one scale cannot serve the required roles.

---

## Brand collection

Brand resolves product identity only.

Modes:

```text
Jobvision
Cando
```

Variables:

```text
brand/50
brand/100
brand/200
brand/300
brand/400
brand/500
brand/600
brand/700
brand/800
brand/900
brand/950

content/on-brand
```

Mappings:

```text
Jobvision brand/* → color/blue/*
Cando brand/*     → color/yellow/*
```

`content/on-brand` is independently resolved because JobVision blue and Cando yellow may require different foreground polarity for contrast.

The v3 Brand names `accent/*` and `content/on-accent` are deprecated in favor of `brand/*` and `content/on-brand`. Accent is now a separate Semantic concept.

Do not put general interaction, selection, feedback, focus, or page-surface roles in Brand.

---

## Structural surfaces

`canvas` is removed. The root page or workspace uses the same Surface vocabulary as the rest of the interface.

```text
surface/default
surface/muted
surface/inset
surface/raised
surface/inverse
```

Definitions:

- `surface/default`: ordinary base content surface and default page/root surface.
- `surface/muted`: passive lower-emphasis supporting or grouping surface. It has no interaction states.
- `surface/inset`: surface behind `surface/default` in the local hierarchy; appropriate for recessed regions, workspace chrome, or structural backdrops.
- `surface/raised`: surface elevated above its immediate parent, including menus, popovers, dropdowns, floating panels, and dialogs when they behave as elevated panels.
- `surface/inverse`: high-contrast inverted neutral surface.

`surface/raised` is a color role, not an elevation value. Pair it with the approved elevation or shadow token when depth must be visible.

There is no separate `surface/floating`; floating panels use `surface/raised`.

---

## Neutral interactive surfaces

The v3 `control` and generic `emphasis` names are replaced by an explicit neutral tone × prominence grammar.

```text
surface/neutral-muted
surface/neutral-muted-hover
surface/neutral-muted-active

surface/neutral-emphasis
surface/neutral-emphasis-hover
surface/neutral-emphasis-active
```

Use `neutral-muted` for visible neutral interactive treatments with medium emphasis, such as the Secondary Button.

Use `neutral-emphasis` for high-emphasis neutral operational actions, such as the Primary Button.

Do not confuse structural `surface/muted` with interactive `surface/neutral-muted`.

State suffix remains `active` in v4. A future `active → pressed` rename is not approved.

---

## Transparent interaction states

```text
surface/transparent-hover
surface/transparent-active
surface/transparent-inverse-hover
surface/transparent-inverse-active
```

Use the normal family for transparent-at-rest interactions on ordinary surfaces and the inverse family on `surface/inverse`.

---

## Selected container surfaces

Selection remains a component state, not a general color family.

Global Selected color semantics are intentionally minimal:

```text
surface/selected
surface/selected-hover
```

These are neutral persistent-selection backgrounds for containers such as selected rows, menu/list items, tree nodes, and navigation items.

Do not add `fg/selected`, `line/selected`, selected emphasis, selected inverse, selected disabled, or selected active families without a repeated use case.

Chromatic selection cues use Accent semantics when appropriate. Examples:

```text
Selected line tab
→ fg/primary + line/accent

Checked checkbox
→ surface/accent-emphasis + fg/on-color

Saved bookmark
→ fg/accent

Selected row
→ surface/selected + fg/primary
```

The component state may be named `selected`, `current`, `checked`, `on`, or `applied`; it does not need a same-named global color token.

---

## Brand semantic

Brand is intentionally small and rare.

```text
surface/brand
surface/brand-hover
surface/brand-active

fg/on-brand
```

Brand means product identity or a defined key product/conversion moment. It is not generic emphasis and it is not the default interaction color.

Removed from v3:

```text
surface/brand-muted
fg/brand
line/brand
```

A brand-colored foreground used only for expressive marketing composition should be handled by a reviewed component/pattern treatment if a repeated need emerges rather than by a general `fg/brand` semantic.

---

## Accent semantic

Accent is the general chromatic interaction/affordance color. It is independent from Brand, Danger, Magic, and Support. Selected/current/checked component states may use Accent as a visual cue when chromatic emphasis is appropriate.

```text
surface/accent-muted
surface/accent-muted-hover
surface/accent-muted-active

surface/accent-emphasis
surface/accent-emphasis-hover
surface/accent-emphasis-active

fg/accent
line/accent
```

In the current two-product system, Accent resolves from `color/blue/*` in both JobVision and Cando. It does not need to route through Brand because its value does not currently vary by product.

Do not add `fg/on-accent`; strong Accent surfaces use `fg/on-color`.

Do not add Accent-specific disabled, focus, or inverse families without a real use case.

---

## Magic

Magic remains reserved for AI-assisted, generated, or explicitly magical experiences.

```text
surface/magic-muted
surface/magic-emphasis
surface/magic-emphasis-hover
surface/magic-emphasis-active

fg/magic
line/magic
```

Magic must not replace Brand, Accent, Selected, or Support meaning.

---

## Danger

Danger remains separate from Error.

```text
surface/danger-muted
surface/danger-emphasis
surface/danger-emphasis-hover
surface/danger-emphasis-active

fg/danger
line/danger
```

Danger communicates destructive intent/action. Error communicates validation or system state.

---

## Support

Support meanings remain invariant across products and themes.

```text
surface/info-muted
surface/success-muted
surface/warning-muted
surface/error-muted

fg/info
fg/success
fg/warning
fg/error

line/info
line/success
line/warning
line/error
```

Only muted Support surfaces are approved globally. Do not pre-build strong Support surface matrices without a repeated use case.

Colored Support foregrounds on inverse surfaces are retained for patterns such as inverse Toasts:

```text
fg/info-inverse
fg/success-inverse
fg/warning-inverse
fg/error-inverse
```

These are specifically colored Support content on `surface/inverse`, not a general Support-inverse family.

---

## Foreground

General and contextual foreground inventory:

```text
fg/primary
fg/secondary
fg/tertiary
fg/placeholder
fg/disabled

fg/on-inverse
fg/on-brand
fg/on-color

fg/accent
fg/magic
fg/danger

fg/info
fg/success
fg/warning
fg/error

fg/info-inverse
fg/success-inverse
fg/warning-inverse
fg/error-inverse
```

Removed in v4:

```text
fg/brand
fg/selected
fg/on-color-disabled
```

Disabled filled controls suppress tone and use `surface/disabled + fg/disabled`; therefore a separate colored disabled foreground is not needed.

---

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

Removed in v4:

```text
line/brand
line/selected
```

Selected indicators may use `line/accent`. Keep the source-token family named `line`, not `border`, to avoid collision with implementation utility naming.

---

## Disabled

```text
surface/disabled
fg/disabled
line/disabled
```

Disabled suppresses tone by default. Do not create:

```text
brand-disabled
accent-disabled
neutral-disabled
danger-disabled
```

Filled Brand, Primary, Secondary, and Danger Buttons all resolve to the same general disabled treatment.

---

## Focus

```text
focus/default
focus/inverse
```

Focus remains independent from Brand and Accent. Cando yellow must not be the sole focus indicator.

A dual-layer focus treatment for media remains an open pattern-level decision.

---

## Link

Link remains a dedicated navigation semantic family even when it shares the Blue Primitive palette with Accent.

```text
link/default
link/hover

link/subtle
link/subtle-hover

link/inverse
link/inverse-hover
```

Rules:

- `default` is the recognizable chromatic link and uses the shared blue interaction palette.
- `subtle` is a neutral lower-prominence link for contexts where clickability is already clear, such as dense product UI, navigation, card metadata, or “View all” patterns.
- `subtle` should not replace the normal inline link in body copy unless another persistent affordance such as underline preserves recognition.
- `inverse` adapts Link for `surface/inverse`; one inverse treatment is sufficient in v4.
- Link does not alias `fg/accent` directly. It may resolve to the same Primitive blue while remaining an independent semantic contract.

Removed in v4:

```text
link/visited
link/emphasis
link/emphasis-hover
```

Visited state can be introduced later only if a real product pattern such as visited search results requires it.

---

## Utility roles

```text
highlight/default
highlight/inverse
overlay/default
skeleton/base
skeleton/shimmer
```

`overlay/default` is the modal/sheet/dialog backdrop. It is not a Surface role.

---

## Button mapping

Button preset naming is updated so `Accent` no longer ambiguously refers to Brand.

| Preset | Rest | Hover | Active | Foreground |
|---|---|---|---|---|
| Brand | `surface/brand` | `surface/brand-hover` | `surface/brand-active` | `fg/on-brand` |
| Primary | `surface/neutral-emphasis` | `surface/neutral-emphasis-hover` | `surface/neutral-emphasis-active` | `fg/on-color` |
| Secondary | `surface/neutral-muted` | `surface/neutral-muted-hover` | `surface/neutral-muted-active` | `fg/primary` |
| Danger Filled | `surface/danger-emphasis` | `surface/danger-emphasis-hover` | `surface/danger-emphasis-active` | `fg/on-color` |

Tertiary and Ghost remain transparent at rest and use `surface/transparent-hover/active`. Danger Outline and Danger Ghost use `fg/danger` and `line/danger` as appropriate.

Disabled filled Buttons use:

```text
surface/disabled + fg/disabled
```

Internal Button tone becomes:

```text
brand | neutral | danger
```

`brand × strong` is the currently approved Brand combination. Do not generate Brand Subtle, Brand Outline, or Brand Ghost merely to complete a matrix.

Brand Button is reserved for defined product conversions or product-defining entry points. Everyday operational actions remain Neutral Primary even when they are the most important action in the current context.

---

## Component tokens

Component tokens remain exceptional. The approved categorical Tag family continues to live in the Component collection and must not be reused by unrelated components as a generic categorical palette.

Applied Filter Chip should first use shared Semantic roles. If a stable component-specific applied treatment cannot be expressed by those roles, introduce a reviewed `filter-chip/*` Component contract rather than consuming Tag tokens directly.

---

## v3 → v4 migration summary

```text
Remove Experience collection
Remove canvas

surface/control*           → surface/neutral-muted*
surface/emphasis*          → surface/neutral-emphasis*

surface/brand-emphasis*    → surface/brand*
remove surface/brand-muted
remove fg/brand
remove line/brand

add surface/accent-muted*
add surface/accent-emphasis*
add fg/accent
add line/accent

replace full selected family with:
surface/selected
surface/selected-hover

remove fg/selected
remove line/selected
remove fg/on-color-disabled

link/emphasis* → link/subtle*
remove link/visited

Button Accent preset/tone → Brand preset/tone

Brand collection accent/* → brand/*
Brand content/on-accent    → content/on-brand

product-specific Primitive brand palettes → generic hue palettes
```

---

## Open decisions

The following are intentionally not blockers for the v4 semantic architecture:

1. Final opaque Primitive scale values, including Blue and Yellow ramps
2. Final `green` versus `emerald` Primitive inventory
3. Exact Light/Dark alias steps and contrast validation
4. CSS variable strategy
5. Tailwind implementation mapping
6. Dual-layer focus treatment for media

Do not infer or ship unresolved opaque values from this document. The alias graph in `color-token-aliases.md` records value-resolution status separately from this semantic catalog.
