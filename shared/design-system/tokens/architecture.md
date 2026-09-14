---
id: design-system.token.architecture
collection: design-system
type: token
title: Token Architecture
summary: Defines the shared Color contract versus Theme-owned Color implementation, including Theme-local Primitives, stable Semantic roles, and component-token boundaries.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.product-variation.theme-context
last_reviewed: '2026-09-14'
---

# Token Architecture

## Purpose

This document defines the target **Color token architecture** after adopting installable Theme packages.

The central separation is:

```text
Design System
→ owns token contract

Theme
→ owns token values
```

## Target resolution model

```text
Theme-local Primitive
→ shared Semantic role
→ Product UI / Component
```

Semantic role names and meaning are shared across all compatible Themes. Primitive values are implementation details of each Theme.

There is no required global Brand layer between Primitive and Semantic.

## Shared Design System contract

The Design System owns:

- Semantic token names;
- Semantic meaning and usage boundaries;
- which contracts are Product-facing;
- component-owned token contracts;
- accessibility expectations;
- compatibility requirements a Theme must satisfy.

Examples of stable Color API:

```text
surface/*
fg/*
line/*
link/*
utility/*
```

Adding a new Theme must not require Product code to rename these roles.

## Theme implementation

Each Theme package owns:

- its Color Primitive inventory and values;
- Light Semantic mappings;
- Dark Semantic mappings;
- any approved Theme-internal implementation slots required by the final architecture.

Current products are expected to select:

```text
JobVision → JobVision Theme
Cando     → Cando Theme
```

but Product identity is not encoded into Semantic token names.

## Primitive

Primitive Color is Theme-local in the target runtime architecture.

Rules:

- Product code does not consume Primitive values directly;
- components do not depend on a Theme Primitive name when a shared Semantic role exists;
- different Themes may use different Primitive values or ramps while implementing the same Semantic API;
- Primitive naming remains hue/value-oriented inside a Theme rather than semantic.

The current shared Figma Primitive collection is a transitional authoring structure and may be reorganized during the Figma Theme migration.

## Brand

Brand remains a semantic concept but is no longer a required token layer.

```text
surface/brand
surface/brand-hover
surface/brand-active
fg/on-brand
```

are shared Semantic roles whose values are supplied by each Theme.

Example:

```text
JobVision Theme → Brand semantics resolve from JobVision-local Blue values
Cando Theme     → Brand semantics resolve from Cando-local Yellow values
```

The current Figma `02 Brand` collection is transitional and should not be reproduced as a mandatory runtime package layer.

## Appearance

One Theme package contains both Appearance mappings:

```text
Theme
└── Color Semantic
    ├── Light
    └── Dark
```

Appearance names do not enter Semantic token names.

## Component tokens

Most components consume Semantic Color directly.

Private Component tokens are acceptable when they clarify a stable component-owned contract, but they should normally resolve from Semantic roles rather than require Theme-specific knowledge.

Button is the default example:

```text
button/primary/surface
→ surface/accent-emphasis
```

where the private Button alias may exist in component implementation but Theme only needs to implement `surface/accent-emphasis`.

### Categorical Tag

Categorical Tag remains the one unresolved exception because some of its values are intentionally categorical rather than shared UI semantics and the Brand categorical variant varies by Theme.

Current `tag/{color}/*` contract and current Figma mappings remain valid during migration. The target Theme boundary for this contract will be decided separately before Figma collections are restructured.

Do not promote Tag-specific needs into the global Semantic API solely to make Theme packaging easier.

## Current Figma transition model

Current editable Figma structure:

| Collection | Current modes | Migration status |
|---|---|---|
| `01 Primitives` | `Value` | transitional; target values become Theme-local |
| `02 Brand` | `JobVision / Cando` | transitional; not required as target runtime layer |
| `03 Semantic` | `light / dark` | contract survives; values move into Theme implementations |
| `04 Component` | `Light / Dark` | retained until Tag/component Theme boundary is finalized |

Do not interpret transitional Figma collection boundaries as public runtime package boundaries.

## Non-Color Foundations

The Theme-package architecture is Foundation-agnostic.

In v1, only Color is Theme-provided. Typography, Spacing, Radius, Elevation, Motion, and Responsive Layout remain governed by their current shared contracts unless a validated Theme-level variation requires migration.

## Naming

Theme, Product, and Appearance identity do not enter shared Semantic token names.

Do not create public families such as:

```text
jobvision-surface-*
cando-surface-*
light-surface-*
dark-surface-*
```

Runtime/CSS serialization remains a separate frontend contract.

## References

- `semantic-tokens.md`
- `component-tokens.md`
- `product-overrides.md`
- `color-token-aliases.md`
- `primitive-tokens.md`
- `usage-rules.md`
