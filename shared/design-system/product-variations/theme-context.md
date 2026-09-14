---
id: design-system.product-variation.theme-context
collection: design-system
type: product-variation
title: Theme Package Architecture
summary: Defines Theme as an installable visual-token implementation selected by an application, with stable shared Design System contracts and runtime Appearance resolution.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.token.product-overrides
  - design-system.token.architecture
  - design-system.reference.code
last_reviewed: '2026-09-14'
---

# Theme Package Architecture

Theme is an **installable implementation of Design System visual token values**. It is not Product identity itself and it does not own token meaning.

The architecture separates three concerns:

```text
Product / application
→ selects an installed Theme package

Theme package
→ provides token values for supported Foundations

Appearance
→ selects the runtime appearance variant inside that Theme
```

## Product is not Theme

Product and Theme are related but not identical.

```text
JobVision application → JobVision Theme package
Cando application     → Cando Theme package
```

This is the current mapping, not a permanent one-to-one architectural rule. A future Product may reuse an existing Theme, and a deployment may intentionally select another compatible Theme.

Product remains application/business identity. Theme is visual-system implementation.

## Shared contract versus Theme implementation

The shared Design System owns stable token names, meanings, component contracts, accessibility rules, and consumption policy.

Each Theme package owns the concrete values needed to implement those contracts.

```text
Shared DS contract
  surface/default
  surface/brand
  fg/primary
  line/default
  ...
        │
        ├── JobVision Theme → values
        └── Cando Theme     → values
```

Product code consumes the stable Design System contract. It must not depend on which Primitive value a Theme uses to implement that contract.

## Theme package scope

Theme packages are Foundation-agnostic by architecture but intentionally narrow by implementation.

### v1

Theme packages provide **Color only**:

```text
Theme package
├── theme-local Color Primitives
└── Semantic Color values
    ├── Light
    └── Dark
```

Both Light and Dark belong to the same Theme package. Do not create separate packages such as `jobvision-light` and `jobvision-dark`.

### Future-ready

A Theme may later provide values for other Foundations when a validated cross-theme difference exists:

```text
Theme
├── color        v1
├── spacing      future if needed
├── radius       future if needed
├── typography   future if needed
├── elevation    future if needed
└── motion       future if needed
```

Do not move a Foundation into Theme merely because the architecture permits it. Shared Foundations remain shared until a real Theme-level variation requires otherwise.

## Appearance

Appearance remains a runtime choice inside the installed Theme.

Resolved Appearance is only:

```text
light | dark
```

If the application supports:

```text
light | dark | system
```

`system` is a preference/source, not a third resolved Appearance.

Appearance may change at runtime without installing or switching Theme packages.

## Primitive ownership

Primitive values are **Theme-local implementation details** in the target runtime architecture.

The Design System may define required semantic behavior and palette quality constraints, but Product code must not depend on a global cross-Theme Primitive identity.

For example, two Themes may both contain a Blue ramp but they are not required to share identical Primitive values merely because their Semantic contracts use the same token names.

## Brand

Brand is semantic meaning, not a required runtime token layer.

In the target architecture, a Theme may resolve Brand semantics directly from its local Primitives:

```text
JobVision Theme
  surface/brand → local blue

Cando Theme
  surface/brand → local yellow
```

A separate global `Brand` alias layer is therefore not required by the runtime contract.

The current Figma `02 Brand` collection remains a transitional design implementation until the Figma Theme model is migrated. Do not infer the target runtime graph from that temporary collection structure.

## Components

Default component behavior:

```text
Component
→ Semantic tokens
→ values supplied by installed Theme
```

Private Component tokens may alias Semantic tokens when they add useful component-owned meaning, but they do not become Theme responsibilities merely because they exist.

Categorical Tag is the approved sparse Component Theme Extension. Tag owns the `tag/{color}/*` contract; each Theme implements its values. The extension remains component-only and is not Product-facing API.

In v1 these values may ship inside the same physical Theme package. Separate component-extension packages or entry points are optional future optimizations rather than required architecture.

## Runtime ownership

```text
Application / deployment
→ selects and installs Theme package
→ owns Product identity

Application shell / Theme service
→ owns Appearance preference and runtime Light/Dark resolution

Theme package
→ provides Foundation values for the selected visual system

Design System components
→ consume shared Semantic / approved private component contracts
→ do not branch on Product identity for normal styling
```

## Figma target model

Figma represents the final contract with:

```text
01 Primitives            → Value
02 Product               → JobVision | Cando
03 Semantic              → JobVision Light | JobVision Dark | Cando Light | Cando Dark
04 Component Extensions  → same four contexts
```

Rules:

- `01 Primitives` remains a hidden authoring palette while runtime Theme packages own their Primitive implementation.
- `02 Product` is not a Color Theme layer; it retains Product-aware authoring concerns such as the current font-family variable.
- old `02 Brand` Color aliases become hidden legacy after Semantic/Tag mappings stop depending on them.
- `03 Semantic` keeps the stable shared token names while modes hold Theme × Appearance values.
- `04 Component Extensions` is hidden from normal library consumption and currently owns the Tag extension values.

Combined Figma mode labels are an authoring representation only. Product/Theme/Appearance still do not enter public Semantic token names.

## Deferred implementation contracts

This document does not define:

- exact package names or import syntax;
- whether Theme artifacts are CSS, JSON, TypeScript, or generated combinations;
- exact CSS selector/attribute mechanism;
- exact Theme build/publish pipeline;
- SSR preference persistence and no-flash mechanism.

Those belong to the frontend token-package, Tailwind, component-token, and Theme-initialization contracts.
