---
id: design-system.token.color-token-aliases
collection: design-system
type: token
title: Color Token Alias Mappings
summary: Validated v4 Color mappings synchronized with the current Figma Variables model.
knowledge_state: canonical
document_maturity: reviewed
related: []
last_reviewed: '2026-09-10'
---

# Color Token Alias Mappings

## Purpose

This document records the current validated Color mappings above Primitive. Figma owns the current editable aliases and values; this file is the documented mapping contract and review snapshot.

If this document and Figma diverge, treat the mismatch as a maintenance gap and inspect Figma rather than guessing.

Canonical documentation uses names such as `surface/default`; Figma keeps picker-friendly names such as `surface/surface-default`. Alias targets below reproduce the current Figma Primitive spelling `pallete/*` intentionally.

## Resolution rules

```text
Default
Primitive → Semantic → Product UI

Optional Product identity
Primitive → Brand → Semantic → Product UI

Exceptional component-owned contract
Primitive / Semantic / Brand → Component → Product UI
```

Product and Appearance remain independent. Current Figma collections:

```text
01 Primitives → Value
02 Brand      → JobVision | Cando
03 Semantic   → light | dark
04 Component  → Light | Dark
```

Most values above Primitive are aliases. Transparent Semantic interaction colors and overlay intentionally store resolved RGBA directly.

## 02 Brand

| Role | JobVision | Cando |
|---|---|---|
| `brand-default` | `pallete/blue/700` | `pallete/yellow/500` |
| `brand-hover` | `pallete/blue/800` | `pallete/yellow/600` |
| `brand-active` | `pallete/blue/900` | `pallete/yellow/700` |
| `on-brand` | `pallete/bw/white` | `pallete/neutral/900` |
| `brand-muted` | `pallete/blue/100` | `pallete/yellow/100` |
| `brand-muted-hover` | `pallete/blue/200` | `pallete/yellow/200` |
| `brand-fg` | `pallete/blue/800` | `pallete/yellow/800` |
| `brand-line` | `pallete/blue/500` | `pallete/yellow/700` |

The first four roles feed shared Brand semantics. The muted/fg/line roles exist to resolve the Product-aware Brand Tag variant and are not general Semantic Color roles.

Brand is currently Appearance-agnostic. Light and Dark Semantic Brand roles consume the same Product-specific Brand aliases.

## 03 Semantic

### Structural Surface

| Canonical role | Light | Dark |
|---|---|---|
| `surface/default` | `pallete/bw/white` | `pallete/neutral/900` |
| `surface/muted` | `pallete/neutral/50` | `pallete/neutral/800` |
| `surface/inset` | `pallete/neutral/100` | `pallete/neutral/950` |
| `surface/raised` | `pallete/bw/white` | `pallete/neutral/800` |
| `surface/inverse` | `pallete/neutral/950` | `pallete/bw/white` |

Dark uses a dimmed-dark hierarchy rather than numerical inversion.

### Neutral interactive Surface

| Role | Light | Dark |
|---|---|---|
| `surface/neutral-muted` | `neutral/200` | `neutral/800` |
| `surface/neutral-muted-hover` | `neutral/300` | `neutral/700` |
| `surface/neutral-muted-active` | `neutral/400` | `neutral/600` |
| `surface/neutral-emphasis` | `neutral/900` | `neutral/200` |
| `surface/neutral-emphasis-hover` | `neutral/800` | `neutral/300` |
| `surface/neutral-emphasis-active` | `neutral/700` | `neutral/400` |

All unqualified hue paths in tables refer to `pallete/{hue}/{step}`.

### Transparent Surface

| Role | Light | Dark |
|---|---|---|
| `surface/transparent-hover` | `rgba(0,0,0,.04)` | `rgba(255,255,255,.08)` |
| `surface/transparent-active` | `rgba(0,0,0,.08)` | `rgba(255,255,255,.12)` |
| `surface/transparent-inverse-hover` | `rgba(255,255,255,.08)` | `rgba(0,0,0,.04)` |
| `surface/transparent-inverse-active` | `rgba(255,255,255,.12)` | `rgba(0,0,0,.08)` |

These are direct Semantic COLOR values, not aliases to a published alpha Primitive family.

### Selected Surface

| Role | Light | Dark |
|---|---|---|
| `surface/selected` | `neutral/200` | `neutral/800` |
| `surface/selected-hover` | `neutral/300` | `neutral/700` |

### Brand

| Role | Light | Dark |
|---|---|---|
| `surface/brand` | `brand/brand-default` | `brand/brand-default` |
| `surface/brand-hover` | `brand/brand-hover` | `brand/brand-hover` |
| `surface/brand-active` | `brand/brand-active` | `brand/brand-active` |
| `fg/on-brand` | `brand/on-brand` | `brand/on-brand` |

### Accent

| Role | Light | Dark |
|---|---|---|
| `surface/accent-muted` | `blue/50` | `blue/950` |
| `surface/accent-muted-hover` | `blue/100` | `blue/900` |
| `surface/accent-muted-active` | `blue/200` | `blue/800` |
| `surface/accent-emphasis` | `blue/600` | `blue/500` |
| `surface/accent-emphasis-hover` | `blue/700` | `blue/400` |
| `surface/accent-emphasis-active` | `blue/800` | `blue/300` |
| `fg/accent` | `blue/700` | `blue/400` |
| `line/accent` | `blue/600` | `blue/500` |
| `fg/on-color` | `bw/white` | `neutral/950` |

### Magic

| Role | Light | Dark |
|---|---|---|
| `surface/magic-muted` | `purple/100` | `purple/950` |
| `surface/magic-emphasis` | `purple/600` | `purple/500` |
| `surface/magic-emphasis-hover` | `purple/700` | `purple/400` |
| `surface/magic-emphasis-active` | `purple/800` | `purple/300` |
| `fg/magic` | `purple/700` | `purple/400` |
| `line/magic` | `purple/600` | `purple/500` |

### Danger

| Role | Light | Dark |
|---|---|---|
| `surface/danger-muted` | `red/100` | `red/950` |
| `surface/danger-emphasis` | `red/600` | `red/500` |
| `surface/danger-emphasis-hover` | `red/700` | `red/400` |
| `surface/danger-emphasis-active` | `red/800` | `red/300` |
| `fg/danger` | `red/700` | `red/400` |
| `line/danger` | `red/600` | `red/500` |

### Support

| Severity | Muted Surface Light | Muted Surface Dark | FG Light | FG Dark | Inverse FG Light | Inverse FG Dark | Line Light | Line Dark |
|---|---|---|---|---|---|---|---|---|
| Info | `blue/100` | `blue/950` | `blue/700` | `blue/400` | `blue/500` | `blue/700` | `blue/500` | `blue/600` |
| Success | `green/100` | `green/950` | `green/700` | `green/500` | `green/600` | `green/700` | `green/600` | `green/600` |
| Warning | `yellow/100` | `yellow/950` | `yellow/800` | `yellow/600` | `yellow/700` | `yellow/800` | `yellow/700` | `yellow/700` |
| Error | `red/100` | `red/950` | `red/700` | `red/400` | `red/500` | `red/700` | `red/500` | `red/600` |

### Neutral Foreground

| Role | Light | Dark |
|---|---|---|
| `fg/primary` | `neutral/950` | `neutral/200` |
| `fg/secondary` | `neutral/700` | `neutral/400` |
| `fg/tertiary` | `neutral/600` | `neutral/500` |
| `fg/placeholder` | `neutral/600` | `neutral/500` |
| `fg/disabled` | `neutral/500` | `neutral/500` |
| `fg/on-inverse` | `bw/white` | `neutral/950` |

The old Figma variable `fg/fg-on-disabled` remains hidden for migration safety and is not canonical.

### Neutral Line

| Role | Light | Dark |
|---|---|---|
| `line/muted` | `neutral/200` | `neutral/800` |
| `line/default` | `neutral/300` | `neutral/700` |
| `line/emphasis` | `neutral/400` | `neutral/600` |
| `line/disabled` | `neutral/200` | `neutral/800` |
| `line/inverse` | `neutral/600` | `neutral/500` |

### Disabled Surface

| Role | Light | Dark |
|---|---|---|
| `surface/disabled` | `neutral/100` | `neutral/800` |

### Link

| Role | Light | Dark |
|---|---|---|
| `link/default` | `blue/700` | `blue/400` |
| `link/hover` | `blue/800` | `blue/300` |
| `link/subtle` | `neutral/700` | `neutral/400` |
| `link/subtle-hover` | `neutral/900` | `neutral/200` |
| `link/inverse` | `blue/400` | `blue/700` |
| `link/inverse-hover` | `blue/300` | `blue/800` |

### Utility

Canonical semantic meaning and current Figma variable names are:

| Meaning | Figma variable | Light | Dark |
|---|---|---|---|
| Focus default | `utility/focus-default` | `neutral/900` | `neutral/100` |
| Focus inverse | `utility/focus-inverse` | `bw/white` | `neutral/950` |
| Overlay | `utility/overlay` | `rgba(0,0,0,.50)` | `rgba(0,0,0,.50)` |
| Skeleton background | `utility/skeleton-background` | `neutral/100` | `neutral/800` |
| Skeleton base | `utility/skeleton-base` | `neutral/300` | `neutral/700` |
| Skeleton element | `utility/skeleton-element` | `neutral/300` | `neutral/700` |
| Skeleton shimmer | `utility/skeleton-shimmer` | `neutral/100` | `neutral/600` |

## 04 Component — Tag

Canonical contract:

```text
tag/{color}/surface
tag/{color}/surface-hover
tag/{color}/fg
tag/{color}/line
```

Current canonical colors:

```text
neutral | brand | blue | teal | green | yellow | orange | red | magenta | purple
```

Cyan and Warm Gray are hidden legacy variants only.

### Tag mappings

| Color | Surface Light | Surface Dark | Hover Light | Hover Dark | FG Light | FG Dark | Line Light | Line Dark |
|---|---|---|---|---|---|---|---|---|
| Neutral | `neutral/200` | `neutral/900` | `neutral/300` | `neutral/800` | `neutral/700` | `neutral/200` | `neutral/400` | `neutral/600` |
| Brand | `brand/brand-muted` | `brand/brand-muted` | `brand/brand-muted-hover` | `brand/brand-muted-hover` | `brand/brand-fg` | `brand/brand-fg` | `brand/brand-line` | `brand/brand-line` |
| Blue | `blue/100` | `blue/950` | `blue/200` | `blue/900` | `blue/800` | `blue/300` | `blue/500` | `blue/600` |
| Teal | `teal/100` | `teal/950` | `teal/200` | `teal/900` | `teal/700` | `teal/400` | `teal/500` | `teal/600` |
| Green | `green/100` | `green/950` | `green/200` | `green/900` | `green/800` | `green/400` | `green/600` | `green/600` |
| Yellow | `yellow/100` | `yellow/950` | `yellow/200` | `yellow/900` | `yellow/800` | `yellow/400` | `yellow/700` | `yellow/600` |
| Orange | `orange/100` | `orange/950` | `orange/200` | `orange/900` | `orange/700` | `orange/400` | `orange/500` | `orange/600` |
| Red | `red/100` | `red/950` | `red/200` | `red/900` | `red/800` | `red/300` | `red/500` | `red/600` |
| Magenta | `magenta/100` | `magenta/950` | `magenta/200` | `magenta/900` | `magenta/700` | `magenta/400` | `magenta/500` | `magenta/600` |
| Purple | `purple/100` | `purple/950` | `purple/200` | `purple/900` | `purple/700` | `purple/300` | `purple/500` | `purple/500` |

Categorical Tag mappings are chosen hue-by-hue for appearance and contrast; equivalent roles do not need matching numeric steps.

## Deferred decisions

The current Color alias graph is validated. Remaining decisions are implementation or future-use concerns rather than unresolved Color values:

- whether Brand eventually needs Appearance-aware aliases after real dark-theme UI validation;
- runtime Theme composition and initialization;
- CSS variable/package naming and scoping;
- Tailwind mapping;
- destructive removal of hidden legacy variables after migration consumers are known;
- future categorical hues only when real Tag use cases require them.
