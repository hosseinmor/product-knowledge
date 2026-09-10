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
Primitive → Semantic → Product UI / Component
```

Brand-dependent Semantic roles may use:

```text
Primitive → Brand → Semantic → Product UI / Component
```

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

### Resolution rules

- `neutral` maps directly to Neutral Primitives because it is a Tag color variant, not the shared Semantic neutral-interaction family.
- `brand` consumes the Product-aware Brand aliases because its hue changes between JobVision and Cando.
- Other categorical hues map directly to their Primitive ramps.
- Do not map categorical Green to Success, Yellow to Warning, Red to Error, or Purple to Magic merely because the hues match.
- Other components must not consume Tag tokens as a general categorical palette.

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
- Is the mapping valid across supported Product × Appearance contexts?
