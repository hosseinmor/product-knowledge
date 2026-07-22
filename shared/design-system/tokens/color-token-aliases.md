# Color Token Alias Mappings

> Status: working draft  
> Scope: current Figma alias graph for color collections  
> Source catalog: `jobvision-color-tokens-v3-surface-model.md`

## Purpose

This document is the value source of truth for color variables above the Primitive layer. It defines the alias target for every Brand, Experience, Semantic, and approved Component color variable.

The token catalog defines meaning and usage. This file defines resolution values. Keep those responsibilities separate so a value can change without rewriting the role definition.

## Resolution rules

- Only `01 Primitives` stores direct color values.
- `02 Brand` aliases Primitive variables.
- `03 Experience` aliases Primitive variables.
- `04 Semantic` aliases Primitive, Brand, or Experience variables.
- `05 Component` aliases Semantic by default; the approved Tag family aliases Primitive variables because no shared categorical Semantic role exists.
- Every cell below is an alias unless it is explicitly listed as a Primitive direct value.
- Figma uses the slash-grouped variable names shown in the tables. Code flattens `/` to `-`.
- A component must not skip this graph and bind directly to an undocumented Primitive value.

## Required alpha primitives

These direct-value primitives support transparent interaction states:

| Primitive variable | Direct value |
|---|---|
| `color/black-alpha/4` | `rgba(0, 0, 0, 0.04)` |
| `color/black-alpha/8` | `rgba(0, 0, 0, 0.08)` |
| `color/white-alpha/8` | `rgba(255, 255, 255, 0.08)` |
| `color/white-alpha/12` | `rgba(255, 255, 255, 0.12)` |

## 02 Brand

Modes: `Jobvision`, `Cando`.

| Variable | Jobvision | Cando |
|---|---|---|
| `accent/50` | `color/brand/jobvision/50` | `color/brand/cando/50` |
| `accent/100` | `color/brand/jobvision/100` | `color/brand/cando/100` |
| `accent/200` | `color/brand/jobvision/200` | `color/brand/cando/200` |
| `accent/300` | `color/brand/jobvision/300` | `color/brand/cando/300` |
| `accent/400` | `color/brand/jobvision/400` | `color/brand/cando/400` |
| `accent/500` | `color/brand/jobvision/500` | `color/brand/cando/500` |
| `accent/600` | `color/brand/jobvision/600` | `color/brand/cando/600` |
| `accent/700` | `color/brand/jobvision/700` | `color/brand/cando/700` |
| `accent/800` | `color/brand/jobvision/800` | `color/brand/cando/800` |
| `accent/900` | `color/brand/jobvision/900` | `color/brand/cando/900` |
| `accent/950` | `color/brand/jobvision/950` | `color/brand/cando/950` |
| `content/on-accent` | `color/neutral/0` | `color/neutral/950` |

No Brand-level `focus` variable is currently defined. Focus remains Semantic and brand-independent until a real brand-specific treatment is approved.

## 03 Experience

Modes: `Productive`, `Expressive`.

| Variable | Productive | Expressive |
|---|---|---|
| `canvas/light` | `color/neutral/50` | `color/neutral/0` |
| `canvas/dark` | `color/neutral/950` | `color/neutral/900` |

Experience controls only the root canvas in the current version.

## 04 Semantic

Modes: `Light`, `Dark`.

### Canvas and base surfaces

| Variable | Light | Dark |
|---|---|---|
| `canvas` | `Experience/canvas/light` | `Experience/canvas/dark` |
| `surface/default` | `color/neutral/0` | `color/neutral/900` |
| `surface/inset` | `color/neutral/100` | `color/neutral/950` |
| `surface/muted` | `color/neutral/50` | `color/neutral/800` |
| `surface/inverse` | `color/neutral/950` | `color/neutral/0` |

### Neutral interaction surfaces

| Variable | Light | Dark |
|---|---|---|
| `surface/control` | `color/neutral/200` | `color/neutral/800` |
| `surface/control-hover` | `color/neutral/300` | `color/neutral/700` |
| `surface/control-active` | `color/neutral/400` | `color/neutral/600` |
| `surface/emphasis` | `color/neutral/950` | `color/neutral/0` |
| `surface/emphasis-hover` | `color/neutral/800` | `color/neutral/100` |
| `surface/emphasis-active` | `color/neutral/700` | `color/neutral/200` |
| `surface/transparent-hover` | `color/black-alpha/4` | `color/white-alpha/8` |
| `surface/transparent-active` | `color/black-alpha/8` | `color/white-alpha/12` |

### Brand surfaces

| Variable | Light | Dark |
|---|---|---|
| `surface/brand-muted` | `Brand/accent/50` | `Brand/accent/950` |
| `surface/brand-emphasis` | `Brand/accent/600` | `Brand/accent/600` |
| `surface/brand-emphasis-hover` | `Brand/accent/700` | `Brand/accent/700` |
| `surface/brand-emphasis-active` | `Brand/accent/800` | `Brand/accent/800` |

The emphasis ramp stays stable across themes because `Brand/content/on-accent` has a different contrast pairing for Jobvision and Cando. Validate both brand ramps before implementation; do not lighten the Dark value independently if it breaks the paired foreground contrast.

### Selected and disabled surfaces

| Variable | Light | Dark |
|---|---|---|
| `surface/selected-muted` | `color/neutral/100` | `color/neutral/800` |
| `surface/selected-muted-hover` | `color/neutral/200` | `color/neutral/700` |
| `surface/selected-muted-active` | `color/neutral/300` | `color/neutral/600` |
| `surface/selected-emphasis` | `color/neutral/950` | `color/neutral/0` |
| `surface/selected-emphasis-hover` | `color/neutral/800` | `color/neutral/100` |
| `surface/selected-emphasis-active` | `color/neutral/700` | `color/neutral/200` |
| `surface/disabled` | `color/neutral/100` | `color/neutral/800` |

### Danger and support surfaces

| Variable | Light | Dark |
|---|---|---|
| `surface/danger-muted` | `color/red/50` | `color/red/950` |
| `surface/danger-emphasis` | `color/red/600` | `color/red/300` |
| `surface/danger-emphasis-hover` | `color/red/700` | `color/red/200` |
| `surface/danger-emphasis-active` | `color/red/800` | `color/red/100` |
| `surface/info` | `color/blue/50` | `color/blue/950` |
| `surface/success` | `color/emerald/50` | `color/emerald/950` |
| `surface/warning` | `color/yellow/50` | `color/yellow/950` |
| `surface/error` | `color/red/50` | `color/red/950` |

Dark danger emphasis uses a light red ramp so the shared Dark `fg/on-emphasis` pairing remains contrast-safe. Danger meaning remains separate from Error even where Primitive aliases overlap.

### Foreground

| Variable | Light | Dark |
|---|---|---|
| `fg/primary` | `color/neutral/950` | `color/neutral/0` |
| `fg/secondary` | `color/neutral/700` | `color/neutral/200` |
| `fg/subtle` | `color/neutral/500` | `color/neutral/400` |
| `fg/disabled` | `color/neutral/400` | `color/neutral/600` |
| `fg/inverse` | `color/neutral/0` | `color/neutral/950` |
| `fg/brand` | `Brand/accent/700` | `Brand/accent/300` |
| `fg/on-brand` | `Brand/content/on-accent` | `Brand/content/on-accent` |
| `fg/on-emphasis` | `color/neutral/0` | `color/neutral/950` |
| `fg/on-selected` | `color/neutral/0` | `color/neutral/950` |
| `fg/danger` | `color/red/700` | `color/red/300` |
| `fg/info` | `color/blue/700` | `color/blue/300` |
| `fg/success` | `color/emerald/700` | `color/emerald/300` |
| `fg/warning` | `color/yellow/800` | `color/yellow/300` |
| `fg/error` | `color/red/700` | `color/red/300` |

### Line

| Variable | Light | Dark |
|---|---|---|
| `line/subtle` | `color/neutral/200` | `color/neutral/800` |
| `line/default` | `color/neutral/300` | `color/neutral/700` |
| `line/strong` | `color/neutral/400` | `color/neutral/600` |
| `line/disabled` | `color/neutral/200` | `color/neutral/800` |
| `line/brand` | `Brand/accent/300` | `Brand/accent/600` |
| `line/selected` | `color/neutral/950` | `color/neutral/0` |
| `line/danger` | `color/red/300` | `color/red/700` |
| `line/info` | `color/blue/300` | `color/blue/700` |
| `line/success` | `color/emerald/300` | `color/emerald/700` |
| `line/warning` | `color/yellow/300` | `color/yellow/700` |
| `line/error` | `color/red/300` | `color/red/700` |

### Focus

| Variable | Light | Dark |
|---|---|---|
| `focus/default` | `color/neutral/950` | `color/neutral/0` |
| `focus/inverse` | `color/neutral/0` | `color/neutral/950` |

## 05 Component

Modes: `Light`, `Dark`.

The current approved family is Tag. It aliases Primitive values directly by exception because the colors communicate categorization, not a shared Semantic status.

| Variant | Token role | Light | Dark |
|---|---|---|---|
| Neutral | `tag/surface/neutral` | `color/neutral/100` | `color/neutral/800` |
| Neutral | `tag/surface/neutral-hover` | `color/neutral/200` | `color/neutral/700` |
| Neutral | `tag/fg/neutral` | `color/neutral/700` | `color/neutral/200` |
| Neutral | `tag/line/neutral` | `color/neutral/200` | `color/neutral/700` |
| Blue | `tag/surface/blue` | `color/blue/50` | `color/blue/950` |
| Blue | `tag/surface/blue-hover` | `color/blue/100` | `color/blue/900` |
| Blue | `tag/fg/blue` | `color/blue/700` | `color/blue/300` |
| Blue | `tag/line/blue` | `color/blue/200` | `color/blue/800` |
| Purple | `tag/surface/purple` | `color/purple/50` | `color/purple/950` |
| Purple | `tag/surface/purple-hover` | `color/purple/100` | `color/purple/900` |
| Purple | `tag/fg/purple` | `color/purple/700` | `color/purple/300` |
| Purple | `tag/line/purple` | `color/purple/200` | `color/purple/800` |
| Green | `tag/surface/green` | `color/emerald/50` | `color/emerald/950` |
| Green | `tag/surface/green-hover` | `color/emerald/100` | `color/emerald/900` |
| Green | `tag/fg/green` | `color/emerald/700` | `color/emerald/300` |
| Green | `tag/line/green` | `color/emerald/200` | `color/emerald/800` |
| Orange | `tag/surface/orange` | `color/orange/50` | `color/orange/950` |
| Orange | `tag/surface/orange-hover` | `color/orange/100` | `color/orange/900` |
| Orange | `tag/fg/orange` | `color/orange/700` | `color/orange/300` |
| Orange | `tag/line/orange` | `color/orange/200` | `color/orange/800` |

## Implementation checks

Before these mappings are promoted from working draft to stable:

1. Confirm every referenced Primitive variable exists in Figma and code.
2. Validate text and icon contrast for both Brand modes in Light and Dark.
3. Validate state distinction for rest, hover, and active surfaces.
4. Validate directly nested `canvas`, `surface/default`, `surface/inset`, and `surface/muted` combinations in Productive and Expressive contexts.
5. Validate Tag foreground and line contrast in both themes.
6. Export the alias graph and reject unresolved or circular references in CI.

