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

This document defines the current **Color token architecture** for installable Theme packages.

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

Figma intentionally keeps one hidden `01 Primitives` authoring palette. This does not make Primitive a shared runtime API: each runtime Theme package owns its Primitive implementation. If Theme palettes later diverge materially, the Figma authoring strategy can evolve without changing the public Semantic contract.

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

The former Figma `02 Brand` collection has been retired as a live Color layer. It is now `02 Product`; only Product-aware authoring concerns such as `typography/font-family` remain active there, while former Brand Color variables are hidden legacy only.

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

Categorical Tag is the approved **sparse Component Theme Extension**.

```text
Tag contract
→ owns tag/{color}/* names + meaning

Theme package
→ implements values for that contract

Tag implementation
→ consumes tag/*

Product code
→ does not consume tag/*
```

This keeps Theme aware only of a declared extension contract, not Tag anatomy or implementation details.

In v1, Tag extension values may ship inside the same physical Theme package as core Color values. A separate Tag package/entry point is optional implementation optimization, not an architectural requirement.

Do not promote Tag-specific needs into the global Semantic API solely to make Theme packaging easier. Do not introduce shared `categorical/*` tokens until categorization becomes a demonstrated cross-component contract.

## Current Figma model

Current editable Figma structure:

| Collection | Current modes | Migration status |
|---|---|---|
| `01 Primitives` | `Value` | hidden authoring palette; runtime Primitives remain Theme-local |
| `02 Product` | `JobVision / Cando` | hidden Product-aware authoring; currently `typography/font-family`; former Brand Color vars are hidden legacy |
| `03 Semantic` | `JobVision Light / JobVision Dark / Cando Light / Cando Dark` | published shared Semantic contract with Theme × Appearance value contexts |
| `04 Component Extensions` | same four contexts | hidden component-only Theme values; currently Tag |

Figma combines Theme and Appearance in mode names as an authoring convenience. This does not create combined public token identities or require the runtime package API to mirror Figma modes.

Do not interpret Figma collection boundaries as public runtime package boundaries.

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
