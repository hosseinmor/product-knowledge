---
id: design-system.token.component-tokens
collection: design-system
type: token
title: Component Tokens
summary: This document defines when a component-specific token layer is justified and catalogs approved component-token families.
knowledge_state: canonical
document_maturity: draft
related:
  - design-system.governance.documentation-maintenance
---

# Component Tokens

## Purpose

This document defines when a component-specific token layer is justified and catalogs approved component-token families.

The Color architecture uses Component Color tokens only as exceptions. Other foundations may define component-owned geometry or motion tokens under their own future contracts; they are not required to route through the Color graph.

The Button guideline does not define Button-specific color tokens. It defines:

1. Designer-facing presets
2. Internal component properties: `tone × appearance`
3. Direct mappings from those presets to shared Semantic tokens

These are different concepts.

```text
tone / appearance
= component properties

surface/* / fg/* / line/* / focus/*
= semantic color tokens
```

## Default Color Architecture

Color collection order:

```text
01 Primitive
02 Brand
03 Semantic
04 Component
```

This order is not a mandatory alias chain. Relevant allowed edges are:

```text
Brand     → Primitive
Semantic  → Brand | Primitive
Component → Semantic | Primitive (approved exception only)
```

Ordinary components use Semantic Color tokens directly. Do not insert a Component-token alias only to rename an existing Semantic token.

For Button:

```text
Brand
→ surface/brand

Primary
→ surface/neutral-emphasis

Secondary
→ surface/neutral-muted

Tertiary and Ghost hover
→ surface/transparent-hover

Danger Filled
→ surface/danger-emphasis
```

The complete Button mapping is documented in `../components/button.md`, which is the canonical owner of Button preset/state recipes.

## Button Property Model Is Not a Token Model

The internal Button properties are:

```text
tone:
brand | neutral | danger

appearance:
strong | subtle | outline | ghost
```

They organize Figma and code variants. They must not be copied directly into Core token names.

Not every theoretical combination is supported. In v4, `brand × strong` is approved; Brand Subtle, Brand Outline, and Brand Ghost must not be created merely to complete the matrix.

Magic is also **not** a Button tone or preset in the current Button model. AI-related Buttons continue to use the normal Button hierarchy. A future Magic Button treatment requires an explicit Button-component review rather than being inferred from `surface/magic-emphasis*`.

## When to Create a Component Token

Create a component-specific token only when:

- Existing Semantic tokens cannot express the value clearly
- The value has stable meaning inside the component
- The value is reused across multiple variants, states, sizes, or implementations
- The additional layer reduces meaningful implementation or theming complexity
- The token can be mapped consistently in Figma and code
- The Design System owner approves it

## Appropriate Uses

Possible uses include:

- Stable component geometry
- Repeated internal spacing relationships
- Component-specific motion values
- A theming abstraction that cannot be represented through shared Semantic roles
- A stable component-owned color contract with no shared Semantic meaning

Non-color component tokens must follow the contract of their own foundation; the Color Brand layer must not be inserted into those token graphs by default.

## Approved Color Family: Tag

Tag remains the approved component-specific Color family. It exists because reusable categorical Tag colors need a stable component contract but do not carry a shared Semantic meaning.

Approved-for-review variants:

```text
neutral
blue
purple
green
orange
```

Current retained tokens per variant:

```text
tag/surface/{variant}
tag/surface/{variant}-hover
tag/fg/{variant}
tag/line/{variant}
```

Rules:

- These tokens communicate grouping or categorization, not feedback status.
- Static Tags use `tag/surface/{variant}`, `tag/fg/{variant}`, and optionally `tag/line/{variant}`.
- Only interactive Tags use `tag/surface/{variant}-hover`.
- Information, success, warning, and error Tags use Semantic Support tokens instead.
- Other components must not consume the Tag family as a general-purpose categorical palette.
- Existing Tag step mappings must be revalidated after the final Primitive palette pass.

The Tag family is retained in v4, but the **full five-variant × Hover × Line matrix is not yet declared permanently required**. The Tag component review must validate which variants are real, which are interactive, and where a line is part of the anatomy.

Until that review is complete, Tag is approved as an architectural exception but its implementation metadata is incomplete. Do not treat the scaffold Tag guideline as proof that every retained token is production-ready.

## Applied Filter Rule

Do not use Tag tokens merely because an applied Filter Chip visually resembles a colored Tag.

Apply this order:

1. Express the applied state with existing Semantic roles, including `surface/accent-muted*` when an interactive tonal Accent treatment is appropriate.
2. If the component has a stable treatment that cannot be represented semantically, create a reviewed `filter-chip/*` Component contract.
3. Reuse Tag tokens only when the UI is actually rendering the Tag component itself.

## Inappropriate Uses

Do not create Component tokens for:

- Direct aliases of Semantic colors
- One-off values
- Temporary experiments
- Product-specific business behavior
- Every Figma property
- Every component state
- Names that encode a specific Primitive value
- Button presets that already map cleanly to shared Semantic tokens
- A generic categorical palette for unrelated components

## Naming

When justified:

```text
{component}/{element-or-property}/{variant-or-state}
```

Examples:

```text
button/container-min-height/small
button/icon-size/medium
modal/header-padding/inline
tag/surface/blue-hover
tag/fg/blue
```

Implementation may flatten `/` to `-` only after the code mapping is approved. Before then, flattened names in documentation are proposed examples rather than a production contract.

Do not encode Primitive color names, pixel values, or product names into a shared Component token unless the component contract itself is explicitly categorical by hue, as with the approved Tag variants.

## Required Metadata

Every production-ready Component token must document:

- Purpose
- Primitive or Semantic source
- Component and element
- Variant or state
- Supported themes
- Supported products
- Figma variable
- Code token
- Owner
- Deprecation path

A family may be architecturally approved before this metadata is complete, but it must remain explicitly marked as pending implementation/component review until the metadata exists.

## Review Checklist

- Can an existing Semantic token express this value?
- Does the token add stable component meaning?
- Is it reused?
- Does it reduce real branching or duplication?
- Is its name independent from an accidental visual value?
- Is it mapped in both Figma and code?
- Is ownership clear?
