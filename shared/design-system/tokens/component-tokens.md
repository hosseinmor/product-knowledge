---
id: design-system.token.component-tokens
collection: design-system
type: token
title: Component Tokens
summary: Defines when component-specific Color tokens are justified and documents the approved Tag exception.
knowledge_state: canonical
document_maturity: reviewed
related: []
last_reviewed: '2026-09-10'
---

# Component Tokens

## Purpose

Component Color tokens are exceptions. Create them only when a stable component-owned contract cannot be expressed clearly through shared Semantic Color roles.

Other foundations may define component-owned geometry or motion tokens under their own contracts; they are not required to follow the Color graph.

## Default rule

Most components consume Semantic Color directly:

```text
Theme-local Primitive → Semantic → Product UI / Component
```

A private Component token may alias a Semantic role when that indirection adds useful component-owned meaning, but Theme packages should not need to know about ordinary component anatomy.

Do not insert a Component-token layer merely to rename an existing Semantic token.

For example, Button presets map directly to Semantic roles. Button does not need its own Color-token family.

## When a Component Color token is justified

Create one only when:

- existing Semantic roles cannot express the value clearly;
- the meaning is stable and owned by that component;
- the role recurs across variants, states, or implementations;
- the extra layer reduces real implementation or theming complexity;
- the contract can be mapped consistently in Figma and code;
- the Design System owner approves it.

Do not create Component Color tokens for one-off values, experiments, every Figma property/state, or aliases that only rename Semantic Color.

## Approved Color exception: Tag

Tag owns a categorical Color contract because its hues communicate grouping/categorization rather than shared system semantics such as Success, Warning, or Error.

Canonical Figma contract:

```text
tag/{color}/surface
tag/{color}/surface-hover
tag/{color}/fg
tag/{color}/line
```

Current canonical colors:

```text
neutral
brand
blue
teal
green
yellow
orange
red
magenta
purple
```

This set is intentionally not a complete hue palette. Add a categorical hue only when a real Tag use case requires it. Cyan and Warm Gray are retained only as hidden legacy variables; they are not part of the canonical Tag API.

### Current resolution and migration status

The current Figma implementation resolves Tag categorical values from the existing shared Primitive/Brand structure. That implementation remains valid until the Theme migration is completed.

The **target Theme boundary for categorical Tag is intentionally open**. We still need to decide how a Theme supplies Product/Theme-varying categorical values without making the Theme package depend on Tag anatomy and without inflating the global Semantic API.

Locked rules remain:

- categorical hues communicate grouping/categorization, not Support semantics;
- do not map categorical Green to Success, Yellow to Warning, Red to Error, or Purple to Magic merely because the hues match;
- other components must not consume Tag tokens as a general categorical palette;
- ordinary components such as Button should continue resolving from Semantic roles rather than require Theme-specific component slots.

The current four Tag roles are retained for every canonical color. `surface-hover` is consumed only when the rendered Tag is interactive; its existence does not make every Tag interactive. `line` is part of the Tag visual contract but may be decorative where the surface itself establishes the boundary.

Current Neutral Dark mapping is intentionally subtle:

```text
tag/neutral/surface       → neutral/900
tag/neutral/surface-hover → neutral/800
```

Exact current Light/Dark alias values live in Figma and are documented in `color-token-aliases.md`.

## Applied Filter rule

Do not use Tag tokens merely because an applied Filter Chip visually resembles a Tag.

Use this order:

1. Express the state with existing Semantic roles, such as `surface/accent-muted*` when appropriate.
2. If a stable component-owned treatment still cannot be expressed, introduce a reviewed component-specific contract.
3. Reuse Tag tokens only when the UI is actually rendering the Tag component.

## Naming

Canonical Tag naming follows:

```text
{component}/{variant}/{role-or-state}
```

Examples:

```text
tag/blue/surface
tag/blue/surface-hover
tag/blue/fg
tag/blue/line
```

Runtime/CSS flattening is a separate implementation decision.

## Review checklist

- Can an existing Semantic token express this value?
- Does the token add stable component meaning?
- Is it reused enough to justify another layer?
- Does it reduce real branching or duplication?
- Is the name independent from an accidental visual value, except where hue itself is the approved categorical contract?
- Is the mapping valid across supported Theme × Appearance contexts?
