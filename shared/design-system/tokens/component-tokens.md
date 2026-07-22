# Component Tokens

## Purpose

This document defines when a component-specific token layer is justified and catalogs approved component-token families.

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
→ Component tokens
```

Components use Semantic tokens by default. Do not insert a component-token alias only to rename an existing semantic token.

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

## Approved Color Family: Tag

Tag is the first approved component-specific color family. It exists because reusable categorical Tag colors need a stable component contract but do not carry a shared Semantic meaning.

Approved variants:

```text
neutral
blue
purple
green
orange
```

Tokens per variant:

```text
tag-surface-{variant}
tag-surface-{variant}-hover
tag-fg-{variant}
tag-line-{variant}
```

Complete list:

```text
tag-surface-neutral
tag-surface-neutral-hover
tag-fg-neutral
tag-line-neutral

tag-surface-blue
tag-surface-blue-hover
tag-fg-blue
tag-line-blue

tag-surface-purple
tag-surface-purple-hover
tag-fg-purple
tag-line-purple

tag-surface-green
tag-surface-green-hover
tag-fg-green
tag-line-green

tag-surface-orange
tag-surface-orange-hover
tag-fg-orange
tag-line-orange
```

Figma variables are grouped under `05 Component` as `tag/surface/*`, `tag/fg/*`, and `tag/line/*`. Code uses the flattened names above.

Rules:

- These tokens communicate grouping or categorization, not feedback status.
- Static Tags use `tag-surface-{variant}`, `tag-fg-{variant}`, and optionally `tag-line-{variant}`.
- Only interactive Tags use `tag-surface-{variant}-hover`.
- Information, success, warning, and error Tags use Semantic support tokens instead.
- Other components must not consume the Tag family as a general-purpose categorical palette.
- Light mappings are defined in `jobvision-color-tokens-v3-surface-model.md`; Dark mappings are still open.

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
{component}-{element-or-property}-{variant-or-state}
```

Examples:

```text
button-container-min-height-small
button-icon-size-medium
modal-header-padding-inline
tag-surface-blue-hover
tag-fg-blue
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
