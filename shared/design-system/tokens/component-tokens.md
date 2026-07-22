# Component Tokens

## Purpose

This document defines when a component-specific token layer is justified.

The Button guideline does not define Button-specific color tokens. It defines:

1. Designer-facing presets
2. Internal component properties: `tone × appearance`
3. Direct mappings from those presets to shared semantic tokens

These are different concepts.

```text
tone / appearance
= component properties

surface-* / fg-* / line-* / focus-*
= semantic tokens
```

## Default Architecture

The default path is:

```text
Primitive tokens
→ Brand
→ Experience
→ Semantic tokens
→ Component usage
```

Do not insert a component-token alias only to rename an existing semantic token.

For Button:

```text
Accent
→ surface-brand-emphasis

Primary
→ surface-emphasis

Secondary
→ surface-control

Tertiary and Ghost hover
→ surface-transparent-hover

Danger Filled
→ surface-danger-emphasis
```

The complete Button mapping is documented in `../components/button.md`.

## Button Property Model Is Not a Token Model

The internal Button properties are:

```text
tone:
accent | neutral | danger

appearance:
strong | subtle | outline | ghost
```

They organize Figma and code variants. They must not be copied directly into Core token names.

For example:

```text
tone=accent
≠ accent token family

appearance=subtle
≠ subtle token family
```

The resulting preset maps to the appropriate semantic token.

## When to Create a Component Token

Create a component-specific token only when:

- Existing semantic tokens cannot express the value clearly
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
- A theming abstraction that cannot be represented through shared semantic roles

## Inappropriate Uses

Do not create component tokens for:

- Direct aliases of semantic colors
- One-off values
- Temporary experiments
- Product-specific business behavior
- Every Figma property
- Every component state
- Names that encode a specific primitive value
- Button presets that already map cleanly to shared semantic tokens

## Naming

When justified:

```text
{component}-{element}-{property}-{variant-or-state}
```

Examples:

```text
button-container-min-height-small
button-icon-size-medium
modal-header-padding-inline
```

Do not encode primitive color names, pixel values, or product names into a shared component token.

## Required Metadata

Every component token must document:

- Purpose
- Primitive or semantic source
- Component and element
- Variant or state
- Supported themes
- Supported products
- Figma variable
- Code token
- Owner
- Deprecation path

## Review Checklist

- Can an existing semantic token express this value?
- Does the token add stable component meaning?
- Is it reused?
- Does it reduce real branching or duplication?
- Is its name independent from a specific visual value?
- Is it mapped in both Figma and code?
- Is ownership clear?
