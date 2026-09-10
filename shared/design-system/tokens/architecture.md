---
id: design-system.token.architecture
collection: design-system
type: token
title: Token Architecture
summary: Current v4 Color token layering, collection responsibilities, and Product × Appearance model.
knowledge_state: canonical
document_maturity: reviewed
related: []
last_reviewed: '2026-09-10'
---

# Token Architecture

## Purpose

This document defines the **Color token architecture**. It separates raw Color values, Product identity, shared UI semantics, and exceptional component-owned Color contracts.

## Resolution model

```text
Default
Primitive → Semantic → Product UI

Optional Product identity
Primitive → Brand → Semantic → Product UI

Exceptional component-owned contract
Primitive / Semantic / Brand → Component → Product UI
```

Brand is not a mandatory hop. A Semantic token uses Brand only when Product identity intentionally controls its value; otherwise it may alias a Primitive directly.

Component Color tokens are exceptional. They are justified only when a stable component-owned contract cannot be represented by the shared Semantic vocabulary.

This graph is specific to Color. Typography, Spacing, Radius, Elevation, and Motion may define different token graphs.

## Collections and modes

The current Figma Color model is:

| Collection | Modes | Responsibility | Library exposure |
|---|---|---|---|
| `01 Primitives` | `Value` | Context-free Color values and hue scales | Hidden |
| `02 Brand` | `JobVision`, `Cando` | Product-identity aliases | Hidden |
| `03 Semantic` | `light`, `dark` | Shared UI Color API | Published |
| `04 Component` | `Light`, `Dark` | Approved component-owned Color contracts | Published |

Product and Appearance are independent Theme dimensions. Do not encode them into combined Semantic modes.

## Primitive

Primitive Color tokens are named by hue rather than Product or semantic ownership. A hue may feed several meanings without merging those meanings.

Product UI must not consume Primitive Color directly. The only approved direct Primitive consumption above this layer is inside a reviewed Component-token exception such as categorical Tag colors.

Most Semantic values alias Primitive or Brand variables. Transparent interaction colors and overlay are an intentional exception: their resolved RGBA values live directly in the Semantic Color variables, so a published alpha-palette layer is not part of the current Color contract.

## Brand

Brand is the optional Product-identity branch. Current Product modes are `JobVision` and `Cando`.

The core strong roles are:

```text
brand/brand-default
brand/brand-hover
brand/brand-active
brand/on-brand
```

Tag also requires a small Brand-owned categorical mapping because the Product identity hue differs:

```text
brand/brand-muted
brand/brand-muted-hover
brand/brand-fg
brand/brand-line
```

Brand does not own general interaction, selection, feedback, focus, or page-surface semantics.

Brand is currently Appearance-agnostic: the same Product mappings feed Light and Dark. If real UI validation proves this insufficient, add the minimum Appearance-aware aliasing without changing public Semantic names.

## Semantic

Semantic is the default Color interface consumed by product UI and most components. It resolves Appearance through `light | dark` while preserving stable role meaning.

Main families include:

```text
surface/*
fg/*
line/*
link/*
utility/*
```

Brand, Accent, Info, and Link may all resolve from Blue primitives in JobVision while remaining distinct semantic roles.

Figma keeps picker-friendly names such as `surface/surface-default`, `fg/fg-primary`, `line/line-default`, and `link/link-default`. Canonical documentation may use `surface/default`, `fg/primary`, `line/default`, and `link/default`; the difference is an explicit mapping, not a requirement to rename Figma variables.

## Component

Use Component Color tokens only when Semantic Color cannot express the stable component-owned meaning.

The current approved exception is categorical Tag Color:

```text
tag/{color}/surface
tag/{color}/surface-hover
tag/{color}/fg
tag/{color}/line
```

Current canonical colors:

```text
neutral
brand
blue
teal
green
yellow
orange
red
magenta
purple
```

Neutral and categorical Tag colors may alias Primitives directly. Brand Tag roles consume the Brand branch. Tag colors communicate grouping/categorization and must not become a general-purpose categorical palette for unrelated components.

## Removed Experience layer

The v3 `Experience` Color collection is removed. Productive/Expressive is no longer a Color Theme dimension, and `canvas` is removed as a separate root Color role.

The root page/workspace uses the shared structural Surface vocabulary:

```text
surface/default
surface/muted
surface/inset
surface/raised
surface/inverse
```

## Product variation rule

Introduce Product-aware aliasing only when a value actually varies by Product.

Brand differs by Product and therefore uses `02 Brand`. Accent currently resolves to the same Blue Primitive family for JobVision and Cando, so it remains a direct Semantic mapping.

If a future Product needs a different Accent hue, introduce the minimum new indirection while preserving the public Semantic API.

## Naming

Product and Appearance names do not enter Semantic token names. Do not create families such as `jobvision-surface-*`, `cando-surface-*`, `light-*`, or `dark-*`.

Figma uses slash grouping. Runtime/CSS naming remains a separate implementation contract and must not be inferred from Figma naming.

## References

- `semantic-tokens.md`
- `component-tokens.md`
- `product-overrides.md`
- `color-token-aliases.md`
- `primitive-tokens.md`
- `usage-rules.md`
