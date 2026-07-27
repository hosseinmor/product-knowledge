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

Brand values alias primitives into shared roles such as `accent/*` and `content/on-accent`. Product-specific semantic token families are not allowed.

Cando may resolve `content/on-accent` to a dark neutral on yellow accent surfaces. Focus belongs in Brand only when the focus treatment genuinely differs by brand; yellow alone must not be the sole focus indicator.

## Product application

Products select a supported combination of independent modes:

| Context | Brand | Experience | Semantic |
|---|---|---|---|
| Jobvision public experience | Jobvision | Expressive | Light |
| Jobvision employer panel | Jobvision | Productive | Light |
| Cando ATS | Cando | Productive | Light or Dark |

A product may not redefine semantic meaning. Any new combination or local exception requires Design System review and accessibility validation.

## Constraints

- Components consume Semantic tokens only.
- Brand modes do not contain `canvas`, `surface-*`, selected, or feedback roles.
- Experience modes do not become product themes.
- Light/Dark does not become an Experience mode.
- Missing combinations fall back only through an approved Semantic mapping; do not map components directly to primitives.
