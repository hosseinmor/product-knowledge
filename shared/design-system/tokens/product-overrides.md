---
id: design-system.token.product-overrides
collection: design-system
type: token
title: Token Product and Brand Variations
summary: Defines Product identity in Color and its relationship to the independent Appearance dimension.
knowledge_state: canonical
document_maturity: reviewed
related: []
last_reviewed: '2026-09-10'
---

# Token Product and Brand Variations

## Scope

This document describes Product variation in the v4 **Color token system**. Product and Appearance are independent Theme dimensions.

```text
Product    → JobVision | Cando
Appearance → Light | Dark
```

The current Figma model resolves them in separate collections:

```text
02 Brand    → JobVision | Cando
03 Semantic → light | dark
04 Component → Light | Dark
```

Do not encode Product and Appearance into combined Semantic modes. Runtime Theme initialization and CSS representation remain separate implementation contracts.

## Product identity in Brand

`02 Brand` is the optional Product-identity alias branch. Its core strong roles are:

```text
brand/brand-default
brand/brand-hover
brand/brand-active
brand/on-brand
```

Current Product mapping:

```text
JobVision
brand-default → blue/700
brand-hover   → blue/800
brand-active  → blue/900
on-brand      → white

Cando
brand-default → yellow/500
brand-hover   → yellow/600
brand-active  → yellow/700
on-brand      → neutral/900
```

Tag requires four additional Brand aliases because its categorical Brand hue also varies by Product:

```text
brand/brand-muted
brand/brand-muted-hover
brand/brand-fg
brand/brand-line
```

These are Brand implementation inputs for the Tag contract, not general shared UI semantics.

Brand is currently Appearance-agnostic: the same Product mappings feed Light and Dark. The potential need for Appearance-aware Brand aliases remains a known follow-up only if real dark-theme UI validation demonstrates a problem.

## Semantic Accent

Accent is not Brand.

```text
JobVision Accent → blue/*
Cando Accent     → blue/*
```

Because Accent currently uses the same interaction hue in both Products, its Semantic roles alias Blue Primitives directly. Do not create Product-aware Accent indirection until a real Product requires different values.

If that happens, preserve the public Semantic names and introduce only the minimum additional aliasing needed.

## Product × Appearance application

A Product selects identity and Appearance independently. Examples:

| Context | Product | Appearance |
|---|---|---|
| JobVision public experience | JobVision | Light or Dark when supported |
| JobVision employer experience | JobVision | Light or Dark when supported |
| Cando ATS | Cando | Light or Dark |

This describes the resolved design context. It does not prescribe the runtime Theme API or initialization mechanism.

Productive/Expressive is not a Color Theme dimension in v4.

## Brand usage

Brand Color is intentionally rare in operational UI.

Use Brand semantics for Product identity, approved key conversions, and Product-defining entry points or feature moments. Do not use Brand merely because an element needs more emphasis.

General chromatic interaction belongs to Accent. Operational action hierarchy is primarily Neutral.

Low frequency of yellow Brand usage inside Cando ATS is expected and is not evidence that Brand is underused.

## Cross-product identity

When JobVision appears explicitly inside Cando, do not rely on Blue alone to communicate identity because Cando also uses Blue for Accent. Use the JobVision logo, name, or another reviewed branded composition.

## Constraints

- Product UI consumes Semantic Color or an approved Component Color contract, not Brand directly.
- Product and Appearance remain independent dimensions.
- Product names do not enter Semantic token names.
- Brand does not own general surfaces, selection, feedback, focus, or Accent roles.
- A Product may not redefine semantic meaning locally.
- Missing Product variation must not be solved by direct Primitive binding in ordinary component implementation.
