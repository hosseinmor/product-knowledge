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

The v4 architecture separates raw values, product brand identity, shared Light/Dark semantics, and exceptional component-owned contracts.

The canonical resolution path is:

```text
Primitive
→ Brand
→ Semantic
→ Component
```

Components consume Semantic tokens by default. An approved Component token is exceptional and follows the criteria in `component-tokens.md`.

## Collections and modes

| Collection | Modes | Responsibility |
|---|---|---|
| `01 Primitives` | Value | Context-free raw values |
| `02 Brand` | Jobvision, Cando | Product brand ramp and on-brand content |
| `03 Semantic` | Light, Dark | Stable shared UI roles consumed by components |
| `04 Component` | Light, Dark | Approved component-owned roles, currently categorical Tag colors |

### Primitive

Primitive tokens store direct values such as color scales, typography, spacing, radius, elevation, and motion. Product UI must not consume Primitive color values directly unless an approved Component token explicitly aliases a Primitive source.

Primitive color palettes are named by hue rather than product ownership. Product brand colors may share a Primitive palette with other semantics without sharing meaning.

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

Semantic has Light and Dark modes. It owns the stable shared UI vocabulary across:

```text
surface/*
fg/*
line/*
focus/*
link/*
highlight/*
overlay/*
skeleton/*
```

Semantic meaning remains stable across products even when values overlap. For example, Brand, Accent, Info, and Link may all draw from `color/blue/*` in JobVision without becoming the same semantic role.

### Component

Components use Semantic tokens by default. Approved Component tokens are allowed only when a stable component-owned role cannot be represented by the shared Semantic vocabulary.

The approved categorical Tag family is:

```text
tag/surface/*
tag/fg/*
tag/line/*
```

Tag tokens communicate categorization rather than feedback status and must not be reused by unrelated components as a general-purpose categorical palette.

## Removed Experience layer

v3 used:

```text
Primitive
→ Brand
→ Experience
→ Semantic
→ Component
```

The `Experience` collection is removed in v4. It only controlled the former root `canvas` value and did not justify a dedicated alias layer.

Productive versus Expressive remains useful as design guidance, but it is no longer a token mode dimension.

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

Figma variables use slash grouping. Code may flatten `/` to `-` when implementation mapping is approved.

The current color vocabulary is defined in `jobvision-color-tokens-v4-surface-model.md`. The v3 catalog is historical migration reference only.

## References

- `jobvision-color-tokens-v4-surface-model.md`
- `color-token-aliases.md`
- `primitive-tokens.md`
- `semantic-tokens.md`
- `component-tokens.md`
- `product-overrides.md`
- `usage-rules.md`
