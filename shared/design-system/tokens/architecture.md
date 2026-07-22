# Token Architecture

> Status: draft

## Purpose

The token architecture separates raw design values from shared meaning, contextual experience, and component implementation.

The default resolution path is:

```text
Primitive tokens
→ Semantic tokens
→ Experience mode
→ Component usage
```

A component-specific token layer may be added after Experience only when the criteria in `component-tokens.md` are met.

## Layers

### Primitive

Primitive tokens store raw values such as color scales, type scales, spacing, radius, elevation, and motion values.

They do not describe product or interface intent and must not be consumed directly by product UI.

### Semantic

Semantic tokens describe stable roles such as surface, foreground, line, support, and focus.

A semantic role must retain its meaning across products and Experience modes. For example, an error role remains an error role in both Productive and Expressive modes even when its resolved visual value changes.

### Experience

Experience is the contextual resolution layer between Semantic tokens and component usage.

It controls how the same semantic system is expressed for a specific kind of experience without changing component meaning or interaction behavior. The layer has two modes:

| Mode | Intent | Default contexts |
|---|---|---|
| Productive | Support frequent, task-focused work with clarity, efficiency, and controlled visual emphasis | Product application flows, dashboards, forms, tables, management interfaces, and repeated operational tasks |
| Expressive | Create a more distinctive, engaging, and brand-forward experience while preserving usability | Brand and marketing surfaces, campaign or editorial moments, selected onboarding or success moments, and other deliberately prominent touchpoints |

Productive is the default mode for product interfaces. Expressive must be selected intentionally for a defined surface or journey.

The distinction is consistent with the Jobvision brand sources: the experience must remain professional, reliable, current, approachable, and free of unnecessary complexity. Expressive mode may increase emotional and brand presence, but must not become decorative at the expense of clarity.

### Component usage

Components consume tokens through the active Experience mode.

Components must not branch their semantics based on the mode. A Primary Button remains Primary, and a danger state remains danger. The active mode may alter approved visual qualities such as typography, spacing, radius, elevation, motion, or emphasis only through documented token mappings.

## Experience Mode Rules

- Choose the mode at the surface or journey level, not independently for each component.
- Use Productive when users are completing frequent, dense, data-heavy, or time-sensitive tasks.
- Use Expressive only when stronger brand expression or emotional emphasis is part of the intended experience.
- Do not use Expressive merely to make a screen look more important.
- Do not mix modes within one component.
- A bounded Expressive region may exist inside a Productive experience only when the boundary and purpose are explicit and the composition is accessibility-tested.
- Mode changes must not alter information hierarchy, action meaning, validation, state meaning, keyboard behavior, or assistive-technology semantics.
- Both modes must meet the same accessibility requirements, including contrast, focus visibility, reduced motion, and target size.
- Product-specific brand mappings are overrides within a mode; they do not create additional Experience modes.

## What Experience Modes Are Not

Productive and Expressive are not:

- Light and dark themes
- Product or brand variants
- Responsive breakpoints
- Component variants
- Interaction states
- Density settings
- Permission or business-rule changes

These concerns may coexist with an Experience mode but must be modeled separately.

## Naming Model

Mode is a resolution dimension, not part of the semantic role name.

The stable role name should remain the same while its approved value or alias is resolved through the active `Productive` or `Expressive` mode. Do not create pairs such as `productive-surface-*` and `expressive-surface-*` in product code only to duplicate the same semantic role.

The exact Figma collection structure and code API must preserve this separation:

```text
stable semantic role
+ active Experience mode
+ optional product override
= resolved component value
```

## References

- `primitive-tokens.md`
- `semantic-tokens.md`
- `component-tokens.md`
- `product-overrides.md`
- `usage-rules.md`
- `../product-variations/brand-variants.md`

Supporting brand references reviewed for this decision:

- Jobvision Guidelines v3
- Jobvision Brand Platform V1
- Jobvision Verbal Identity 2.1

The Productive and Expressive mode names and their addition to the token architecture are an approved design-system direction supplied for this update. The brand references support the behavioral constraints but do not define this token taxonomy.

## Ownership

The Design System team owns:

- Mode definitions
- Token mappings for each mode
- Criteria for selecting a mode
- Cross-product accessibility requirements

Product teams may select a documented mode for an eligible surface. New modes, mixed-mode exceptions, or changes to shared mappings require Design System review.
