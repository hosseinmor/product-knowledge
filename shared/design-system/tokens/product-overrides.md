---
id: design-system.token.product-overrides
collection: design-system
type: token
title: Token Product and Brand Variations
summary: '> Status: draft'
knowledge_state: unverified
document_maturity: draft
related: []
---

# Token Product and Brand Variations

> Status: draft

## Brand modes

The Brand collection has two modes:

```text
Jobvision
Cando
```

Brand values alias generic Primitive hue scales into shared product-identity roles:

```text
brand/*
content/on-brand
```

Current mapping direction:

```text
Jobvision brand/* → color/blue/*
Cando brand/*     → color/yellow/*
```

Cando may resolve `content/on-brand` to a dark neutral on yellow Brand surfaces. JobVision may resolve it to a light neutral on blue Brand surfaces. Final contrast must be validated after the Primitive palettes are built.

## Semantic Accent

Accent is not a Brand alias in v4.

```text
JobVision Accent → color/blue/*
Cando Accent     → color/blue/*
```

Because Accent currently has the same interaction hue in both products, Semantic Accent may alias Blue primitives directly. Do not create a product-aware Accent layer until a real product requires a different Accent hue.

If a future product needs a different Accent value, introduce the minimum product-aware alias needed at that time while keeping the public Semantic names stable.

## Product application

Products select Brand and Semantic modes independently:

| Context | Brand | Semantic |
|---|---|---|
| JobVision public experience | Jobvision | Light or Dark when supported |
| JobVision employer panel | Jobvision | Light or Dark when supported |
| Cando ATS | Cando | Light or Dark |

Productive/Expressive is no longer a token mode in v4. Those concepts may still guide composition, density, and visual expression outside the color alias graph.

## Brand usage

Brand color is intentionally rare in operational UI.

Use Brand semantics for:

- Product identity
- Approved key conversions
- Product-defining entry points or feature moments

Do not use Brand merely because an element needs more emphasis. General interactive chromatic emphasis belongs to Accent; operational hierarchy is primarily Neutral.

Low frequency of yellow Brand usage inside Cando ATS is expected and is not evidence that the Brand system is underused.

## Cross-product identity

When JobVision appears explicitly inside Cando, do not rely on blue hue alone to communicate identity. Use the JobVision logo, name, or a reviewed branded composition. Cando may already use the same Blue Primitive family for interaction Accent.

## Constraints

- Components consume Semantic tokens by default.
- Product names do not enter Semantic token names.
- Brand modes do not contain general surfaces, selection, feedback, focus, or Accent roles.
- Light/Dark does not become a Brand mode.
- A product may not redefine semantic meaning locally.
- Missing product-specific variation must not be solved by direct Primitive binding in component implementation.
