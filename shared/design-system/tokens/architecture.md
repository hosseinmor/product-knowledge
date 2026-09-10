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

The v4 architecture described here is the **Color token architecture**. It separates raw color values, Product identity, Appearance-dependent shared UI semantics, and exceptional component-owned color contracts.

The canonical Color resolution model is:

```text
Core path
Primitive
→ Semantic
→ Component

Optional product-identity branch
Primitive
→ Brand
→ Semantic
```

Brand is not a mandatory hop between Primitive and Semantic. A Semantic token aliases Brand only when its value intentionally depends on Product identity; otherwise it may alias a Primitive directly.

Components consume Semantic Color tokens by default. An approved Component Color token is exceptional and follows the criteria in `component-tokens.md`.

This graph must not be assumed to be the resolution graph for Typography, Spacing, Radius, Elevation, or Motion. Those foundations may use different Primitive/Semantic structures and must document their own resolution model when their shared contracts are finalized. Brand is an optional identity branch even within Color and must not be introduced into another foundation by convention.

## Collections and logical dimensions

The logical Theme dimensions are Product and Appearance. The table below describes how the current Color collections participate in those dimensions; it does **not** define the final Figma collection/mode implementation.

| Collection | Logical variation | Responsibility |
|---|---|---|
| `01 Primitives` | Value | Context-free raw color values |
| `02 Brand` | Product: JobVision, Cando | Optional product-identity aliases for the Brand color ramp and on-brand content |
| `03 Semantic` | Appearance: Light, Dark | Stable shared UI Color roles consumed by components |
| `04 Component` | Appearance: Light, Dark | Approved component-owned Color roles, currently categorical Tag colors |

### Primitive

Primitive Color tokens store direct color values such as hue scales and alpha values. Product UI must not consume Primitive color values directly unless an approved Component Color token explicitly aliases a Primitive source.

Primitive color palettes are named by hue rather than product ownership. Product Brand colors may share a Primitive palette with other semantics without sharing meaning.

Typography, Spacing, Radius, Elevation, and Motion may also have primitive values, but their token graphs are outside the scope of this Color architecture document.

### Brand

Brand is the optional product-identity alias branch. It aliases generic Primitive hue scales into the active Product identity when a Semantic role intentionally depends on that identity.

```text
brand/*
content/on-brand
```

Current direction:

```text
JobVision brand/* → color/blue/*
Cando brand/*     → color/yellow/*
```

Brand does not contain general interaction, selection, feedback, focus, or page-surface roles. Semantic roles whose values do not vary by Product identity should alias Primitive values directly rather than routing through Brand.

### Semantic

Semantic resolves the Appearance dimension and owns the stable shared Color vocabulary across:

```text
surface/*
fg/*
line/*
focus/*
link/*
overlay/*
skeleton/*
```

A Semantic token may alias a Primitive directly or consume the Brand branch when Product identity is part of the role's value. Semantic meaning remains stable across products and Appearance values even when underlying values overlap. For example, Brand, Accent, Info, and Link may all draw from `color/blue/*` in JobVision without becoming the same semantic role.

### Component

Components use Semantic Color tokens by default. Approved Component Color tokens are allowed only when a stable component-owned role cannot be represented by the shared Semantic vocabulary.

The approved categorical Tag family is:

```text
tag/surface/*
tag/fg/*
tag/line/*
```

Tag tokens communicate categorization rather than feedback status and must not be reused by unrelated components as a general-purpose categorical palette.

## Removed Experience layer

v3 Color used:

```text
Primitive
→ Brand
→ Experience
→ Semantic
→ Component
```

The `Experience` collection is removed in v4. It only controlled the former root `canvas` value and did not justify a dedicated Color alias layer.

Productive versus Expressive may remain useful as design guidance, but it is no longer a Color Theme dimension. Existing Figma component names that still contain `Productive` are legacy naming references unless a separate active design dimension is explicitly documented by that component.

## Root surface model

`canvas` is removed. The root page or workspace uses the same Surface vocabulary as nested UI:

```text
surface/default
surface/muted
surface/inset
surface/raised
surface/inverse
```

This allows multiple structural surfaces to coexist in one product without switching a product-level canvas mode.

## Product variation rule

Introduce a product-aware alias only when a Semantic value actually differs by Product.

Today Brand differs by Product, so the optional Brand branch carries Product identity. Accent currently resolves to the shared Blue Primitive palette in both products, so it remains a direct Semantic mapping rather than gaining speculative product variation.

If a future product needs a different Accent hue, add the minimum product-aware alias required at that time while preserving the Semantic API.

## Naming

Product names and Appearance names do not enter Semantic token names. Do not create `jobvision-surface-*`, `cando-surface-*`, `light-*`, or `dark-*` Semantic families.

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
