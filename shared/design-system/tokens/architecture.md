---
id: design-system.token.architecture
collection: design-system
type: token
title: Token Architecture
summary: '> Status: draft'
knowledge_state: unverified
document_maturity: draft
related: []
---

# Token Architecture

> Status: draft

## Purpose

The v4 architecture described here is the **Color token architecture**. It separates raw color values, product brand identity, shared Light/Dark color semantics, and exceptional component-owned color contracts.

The four collections have this **layer order**:

```text
01 Primitive
02 Brand
03 Semantic
04 Component
```

Layer order is not a requirement that every token resolves through every layer. The actual allowed Color alias edges are:

```text
Brand     → Primitive
Semantic  → Brand | Primitive
Component → Semantic | Primitive (approved exception only)
```

Ordinary UI components consume Semantic Color tokens directly. They may consume an approved Component token when that component-owned contract is justified. They do not consume Brand or undocumented Primitive Color values directly.

The Component collection is therefore optional in a resolution path, and Brand is only present when the semantic meaning is product identity. For example, shared Accent may resolve `Semantic → Primitive` without passing through Brand, while an approved categorical Tag token may resolve `Component → Primitive` by exception.

An approved Component color token is exceptional and follows the criteria in `component-tokens.md`.

This graph must not be assumed to be the resolution graph for Typography, Spacing, Radius, Elevation, or Motion. Those foundations may use different Primitive/Semantic structures and must document their own resolution model when their shared contracts are finalized. In particular, non-color foundations do not route through Brand merely because Color can.

## Collections and modes

| Collection | Modes | Responsibility |
|---|---|---|
| `01 Primitives` | Value | Context-free raw color values |
| `02 Brand` | Jobvision, Cando | Product brand color ramp and on-brand content |
| `03 Semantic` | Light, Dark | Stable shared UI color roles consumed by components |
| `04 Component` | Light, Dark | Approved component-owned color roles, currently categorical Tag colors |

### Primitive

Primitive Color tokens store direct color values such as hue scales and alpha values. Product UI must not consume Primitive color values directly unless an approved Component color token explicitly aliases a Primitive source.

Primitive color palettes are named by hue rather than product ownership. Product brand colors may share a Primitive palette with other semantics without sharing meaning.

Typography, spacing, radius, elevation, and motion may also have primitive values, but their token graphs are outside the scope of this Color architecture document.

### Brand

Brand aliases generic Primitive hue scales into the active product identity.

```text
brand/*
content/on-brand
```

Current direction:

```text
Jobvision brand/* → color/blue/*
Cando brand/*     → color/yellow/*
```

Brand does not contain general interaction, selection, feedback, focus, or page-surface roles.

### Semantic

Semantic has Light and Dark modes. It owns the stable shared Color vocabulary across:

```text
surface/*
fg/*
line/*
focus/*
link/*
overlay/*
skeleton/*
```

Semantic meaning remains stable across products even when values overlap. For example, Brand, Accent, Info, and Link may all draw from `color/blue/*` in JobVision without becoming the same semantic role.

Semantic may alias Brand when the role is product-dependent, or Primitive directly when the role is shared across products.

### Component

Components use Semantic color tokens by default. Approved Component color tokens are allowed only when a stable component-owned role cannot be represented by the shared Semantic vocabulary.

The approved categorical Tag family is:

```text
tag/surface/*
tag/fg/*
tag/line/*
```

Tag tokens communicate categorization rather than feedback status and must not be reused by unrelated components as a general-purpose categorical palette.

Approved Component Color tokens should alias Semantic by default. A direct Primitive alias is an explicit exception, currently allowed for categorical Tag roles when no shared Semantic meaning exists.

## Removed Experience layer

v3 Color used an additional Experience collection between Brand and Semantic. That collection is removed in v4 because it only controlled the former root `canvas` value and did not justify a dedicated Color alias layer.

Productive versus Expressive may remain useful as design guidance, but it is no longer a Color token mode dimension. Existing Figma component names that still contain `Productive` are legacy naming references unless a separate active design dimension is explicitly documented by that component.

## Root surface model

`canvas` is removed. The root page or workspace uses the same structural Surface vocabulary as nested UI:

```text
surface/default
surface/muted
surface/inset
surface/raised
surface/inverse
```

This allows multiple structural surfaces to coexist in one product without switching a product-level canvas mode.

## Product variation rule

Introduce a product-aware alias only when a semantic value actually differs by product.

Today Brand differs by product, so Brand has modes. Accent currently resolves to the shared Blue Primitive palette in both products, so it remains a direct Semantic mapping rather than gaining speculative product variation.

If a future product needs a different Accent hue, add the minimum product-aware alias required at that time while preserving the Semantic API.

## Naming

Product names and theme names do not enter Semantic token names. Do not create `jobvision-surface-*`, `cando-surface-*`, `light-*`, or `dark-*` semantic families.

Figma Color variables use slash grouping. Code may flatten `/` to `-` **only after** implementation mapping is approved. Until then, flattened names shown in component documentation are illustrative/proposed mappings rather than a production code-token contract.

The current Color vocabulary is defined in `jobvision-color-tokens-v4-surface-model.md`. The v3 catalog is historical migration reference only.

## References

- `jobvision-color-tokens-v4-surface-model.md`
- `color-token-aliases.md`
- `primitive-tokens.md`
- `semantic-tokens.md`
- `component-tokens.md`
- `product-overrides.md`
- `usage-rules.md`
