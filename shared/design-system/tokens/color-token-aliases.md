---
id: design-system.token.color-token-aliases
collection: design-system
type: token
title: Color Token Alias Mappings
summary: '> Status: working draft > Scope: v4 alias graph and unresolved values'
knowledge_state: unverified
document_maturity: draft
related: []
---

# Color Token Alias Mappings

> Status: working draft  
> Scope: v4 alias graph and unresolved values  
> Source catalog: `jobvision-color-tokens-v4-surface-model.md`

## Purpose

This document records how color variables above Primitive resolve. The token catalog defines meaning and usage; this file defines value resolution and explicitly marks unresolved mappings.

Exact opaque palette values and several scale-step choices remain open. Do not infer production values from v3 mappings when a v4 row is marked `TBD`.

## Resolution rules

- Only `01 Primitives` stores direct color values.
- `02 Brand` aliases generic Primitive hue scales.
- `03 Semantic` aliases Primitive or Brand variables.
- `04 Component` aliases Semantic by default; approved categorical Tag tokens may alias Primitive variables directly.
- Components must not bind directly to undocumented Primitive values.
- Figma uses slash-grouped variable names. Code may flatten `/` to `-` after implementation mapping is approved.

The v3 `Experience` collection is removed.

## Required alpha primitives

| Primitive variable | Direct value |
|---|---|
| `color/black-alpha/4` | `rgba(0, 0, 0, 0.04)` |
| `color/black-alpha/8` | `rgba(0, 0, 0, 0.08)` |
| `color/black-alpha/40` | `rgba(0, 0, 0, 0.40)` |
| `color/white-alpha/8` | `rgba(255, 255, 255, 0.08)` |
| `color/white-alpha/12` | `rgba(255, 255, 255, 0.12)` |

## 02 Brand

Modes: `Jobvision`, `Cando`.

The numbered Brand ramp mirrors the corresponding generic hue ramp by step:

| Variable | Jobvision | Cando |
|---|---|---|
| `brand/50` | `color/blue/50` | `color/yellow/50` |
| `brand/100` | `color/blue/100` | `color/yellow/100` |
| `brand/200` | `color/blue/200` | `color/yellow/200` |
| `brand/300` | `color/blue/300` | `color/yellow/300` |
| `brand/400` | `color/blue/400` | `color/yellow/400` |
| `brand/500` | `color/blue/500` | `color/yellow/500` |
| `brand/600` | `color/blue/600` | `color/yellow/600` |
| `brand/700` | `color/blue/700` | `color/yellow/700` |
| `brand/800` | `color/blue/800` | `color/yellow/800` |
| `brand/900` | `color/blue/900` | `color/yellow/900` |
| `brand/950` | `color/blue/950` | `color/yellow/950` |
| `content/on-brand` | `color/neutral/0`* | `color/neutral/950`* |

`*` Foreground polarity is the approved direction but must be revalidated after the final Blue and Yellow scales are built.

The v3 Brand variables `accent/*` and `content/on-accent` are deprecated.

## 03 Semantic

Modes: `Light`, `Dark`.

### Structural surfaces

The roles are approved; exact opaque step mappings remain pending the palette pass.

| Variable | Light | Dark |
|---|---|---|
| `surface/default` | TBD neutral | TBD neutral |
| `surface/muted` | TBD neutral | TBD neutral |
| `surface/inset` | TBD neutral | TBD neutral |
| `surface/raised` | TBD neutral | TBD neutral |
| `surface/inverse` | TBD neutral | TBD neutral |

`surface/raised` may equal `surface/default` in Light and diverge in Dark. Elevation remains a separate token.

### Neutral interactive surfaces

| Variable | Light | Dark |
|---|---|---|
| `surface/neutral-muted` | TBD neutral | TBD neutral |
| `surface/neutral-muted-hover` | TBD neutral | TBD neutral |
| `surface/neutral-muted-active` | TBD neutral | TBD neutral |
| `surface/neutral-emphasis` | TBD neutral | TBD neutral |
| `surface/neutral-emphasis-hover` | TBD neutral | TBD neutral |
| `surface/neutral-emphasis-active` | TBD neutral | TBD neutral |

### Transparent interaction surfaces

These mappings remain structurally approved from v3:

| Variable | Light | Dark |
|---|---|---|
| `surface/transparent-hover` | `color/black-alpha/4` | `color/white-alpha/8` |
| `surface/transparent-active` | `color/black-alpha/8` | `color/white-alpha/12` |
| `surface/transparent-inverse-hover` | `color/white-alpha/8` | `color/black-alpha/4` |
| `surface/transparent-inverse-active` | `color/white-alpha/12` | `color/black-alpha/8` |

### Selected container surfaces

| Variable | Light | Dark |
|---|---|---|
| `surface/selected` | TBD neutral | TBD neutral |
| `surface/selected-hover` | TBD neutral | TBD neutral |

Selected surfaces are neutral persistent-state backgrounds. Chromatic selection cues use Accent roles rather than a separate selected color family.

### Brand surfaces

| Variable | Light | Dark |
|---|---|---|
| `surface/brand` | `Brand/brand/{TBD}` | `Brand/brand/{TBD}` |
| `surface/brand-hover` | `Brand/brand/{TBD}` | `Brand/brand/{TBD}` |
| `surface/brand-active` | `Brand/brand/{TBD}` | `Brand/brand/{TBD}` |

`fg/on-brand` resolves to `Brand/content/on-brand` in both Semantic modes.

### Accent surfaces

Accent uses the generic Blue Primitive family in both products; exact steps remain TBD.

| Variable | Light | Dark |
|---|---|---|
| `surface/accent-muted` | `color/blue/{TBD}` | `color/blue/{TBD}` |
| `surface/accent-muted-hover` | `color/blue/{TBD}` | `color/blue/{TBD}` |
| `surface/accent-muted-active` | `color/blue/{TBD}` | `color/blue/{TBD}` |
| `surface/accent-emphasis` | `color/blue/{TBD}` | `color/blue/{TBD}` |
| `surface/accent-emphasis-hover` | `color/blue/{TBD}` | `color/blue/{TBD}` |
| `surface/accent-emphasis-active` | `color/blue/{TBD}` | `color/blue/{TBD}` |

`fg/accent` and `line/accent` also resolve to `color/blue/*` with final steps TBD.

### Magic and Danger

| Family | Source direction |
|---|---|
| `surface/magic-*`, `fg/magic`, `line/magic` | `color/purple/*`, exact steps TBD |
| `surface/danger-*`, `fg/danger`, `line/danger` | `color/red/*`, exact steps TBD |

Danger remains semantically separate from Error even when both resolve to Red primitives.

### Support

| Family | Source direction |
|---|---|
| Info | `color/blue/*`, exact steps TBD |
| Success | Green/Emerald decision pending; exact steps TBD |
| Warning | `color/yellow/*`, exact steps TBD |
| Error | `color/red/*`, exact steps TBD |

Approved roles:

```text
surface/{info|success|warning|error}-muted
fg/{info|success|warning|error}
line/{info|success|warning|error}
fg/{info|success|warning|error}-inverse
```

The inverse foreground roles are colored Support content on `surface/inverse`, such as inverse Toast status icons or text. They do not imply Support inverse surfaces.

### Foreground

Neutral and contextual mappings remain pending final contrast validation:

```text
fg/primary
fg/secondary
fg/tertiary
fg/placeholder
fg/disabled
fg/on-inverse
fg/on-color
```

Product-dependent foreground:

```text
fg/on-brand → Brand/content/on-brand
```

Chromatic foregrounds:

```text
fg/accent → color/blue/{TBD}
fg/magic → color/purple/{TBD}
fg/danger → color/red/{TBD}
```

`fg/brand`, `fg/selected`, and `fg/on-color-disabled` are removed in v4.

### Line

Neutral line steps remain TBD:

```text
line/muted
line/default
line/emphasis
line/disabled
line/inverse
```

Chromatic lines:

```text
line/accent → color/blue/{TBD}
line/magic → color/purple/{TBD}
line/danger → color/red/{TBD}
line/{info|success|warning|error} → matching support hue, exact step TBD
```

`line/brand` and `line/selected` are removed.

### Disabled

```text
surface/disabled → TBD neutral
fg/disabled      → TBD neutral
line/disabled    → TBD neutral
```

Disabled suppresses tone; no tone-specific disabled aliases are approved.

### Focus

```text
focus/default → TBD contrast-safe neutral
focus/inverse → TBD contrast-safe neutral
```

Focus remains brand- and accent-independent.

### Link

The six Link variables are structurally approved. Exact Alias values remain TBD pending the Blue/Neutral palette pass and contrast validation.

| Variable | Source direction |
|---|---|
| `link/default` | `color/blue/*` |
| `link/hover` | `color/blue/*` |
| `link/subtle` | neutral foreground scale |
| `link/subtle-hover` | neutral or Blue depending final interaction test |
| `link/inverse` | contrast-safe inverse Link treatment |
| `link/inverse-hover` | contrast-safe inverse hover treatment |

Link remains independent from `fg/accent` even when both resolve to the same Blue Primitive value.

`link/visited`, `link/emphasis`, and `link/emphasis-hover` are removed.

### Utility

| Variable | Light | Dark |
|---|---|---|
| `highlight/default` | TBD | TBD |
| `highlight/inverse` | TBD | TBD |
| `overlay/default` | `color/black-alpha/40` | `color/black-alpha/40` |
| `skeleton/base` | `color/black-alpha/8` | `color/white-alpha/8` |
| `skeleton/shimmer` | `color/black-alpha/4` | `color/white-alpha/12` |

## 04 Component

Modes: `Light`, `Dark`.

The approved categorical Tag family remains structurally unchanged:

```text
tag/surface/{neutral|blue|purple|green|orange}
tag/surface/{variant}-hover
tag/fg/{variant}
tag/line/{variant}
```

Existing Tag step mappings should be revalidated against the final Primitive palette pass. Tag colors communicate grouping/categorization and must not be reused as a general categorical palette by unrelated components.

## Open value decisions

1. Final opaque Primitive 50–950 scales
2. Exact Light/Dark neutral surface, foreground, and line steps
3. Exact Brand strong/hover/active steps
4. Exact Accent, Link, Magic, Danger, and Support steps
5. Success source family (`green` versus `emerald`)
6. Final contrast validation for `content/on-brand`, `fg/on-color`, inverse roles, and Link roles
