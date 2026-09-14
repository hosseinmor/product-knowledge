---
id: design-system.token.product-overrides
collection: design-system
type: token
title: Product and Theme Selection
summary: Defines the relationship between Product identity, installable Theme packages, and Appearance without making Product a token dimension.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.product-variation.theme-context
  - design-system.token.architecture
last_reviewed: '2026-09-14'
---

# Product and Theme Selection

## Scope

Product identity and Theme are separate concepts.

```text
Product / application
→ selects a compatible Theme package

Theme package
→ supplies visual token values

Appearance
→ selects Light or Dark values within that Theme
```

Current intended selection:

```text
JobVision → JobVision Theme
Cando     → Cando Theme
```

This current mapping does not make Product a permanent Theme dimension. A future Product may reuse a Theme or a deployment may select another compatible Theme.

## Color identity

Brand semantics remain part of the shared Semantic API:

```text
surface/brand
surface/brand-hover
surface/brand-active
fg/on-brand
```

Their values are Theme-owned.

Conceptually:

```text
JobVision Theme
  surface/brand        → JobVision-local Blue value
  surface/brand-hover  → JobVision-local Blue hover value
  surface/brand-active → JobVision-local Blue active value
  fg/on-brand          → JobVision-local on-Brand value

Cando Theme
  surface/brand        → Cando-local Yellow value
  surface/brand-hover  → Cando-local Yellow hover value
  surface/brand-active → Cando-local Yellow active value
  fg/on-brand          → Cando-local on-Brand value
```

A separate runtime `Brand` alias layer is not required.

## Accent remains independent from Brand

Brand means Product identity or approved Product-defining moments. Accent means general chromatic interaction/affordance.

A Theme may currently map both roles to similar hues or different hues without merging their meaning.

For example, Cando may resolve Brand from Yellow while Accent remains Blue.

## Appearance

Each Theme package contains both Light and Dark Semantic value sets.

```text
Installed Theme
├── Light
└── Dark
```

Appearance may change at runtime without changing the installed Theme package.

## Product code constraint

Product code consumes shared Design System contracts. It must not:

- branch on Product merely to choose a DS color;
- consume Theme-local Primitives;
- assume a specific Theme Primitive name/value;
- encode Product names into shared Semantic token names.

Product-specific business behavior may still depend on Product identity; this document governs visual token resolution only.

## Current Figma representation

Product-aware Color values now live directly in the Theme × Appearance modes of `03 Semantic`.

```text
03 Semantic
├── JobVision Light
├── JobVision Dark
├── Cando Light
└── Cando Dark
```

Brand Semantic roles alias the appropriate Primitive values directly in each Theme context; there is no active Brand Color alias layer.

`02 Product → JobVision | Cando` remains a hidden Figma authoring collection for Product-aware non-Color concerns such as `typography/font-family`. Former Brand Color variables remain hidden legacy only and have no Semantic/Tag dependencies.
