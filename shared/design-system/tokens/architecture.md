# Token Architecture

> Status: draft

## Purpose

The token architecture separates raw values, brand identity, experience context, light/dark semantics, and component consumption.

The canonical resolution path is:

```text
Primitive
→ Brand
→ Experience
→ Semantic
→ Component usage
```

Components consume Semantic tokens only. A component-specific token layer is exceptional and follows the criteria in `component-tokens.md`.

## Collections and modes

| Collection | Modes | Responsibility |
|---|---|---|
| Primitive | Value | Raw values with no UI meaning |
| Brand | Jobvision, Cando | Accent ramp, on-accent content, and any genuinely brand-specific focus value |
| Experience | Productive, Expressive | Environment-level choices such as canvas |
| Semantic | Light, Dark | Stable UI roles consumed by components |

### Primitive

Primitive tokens store direct values such as color scales, typography, spacing, radius, elevation, and motion. Product UI must not consume them directly.

### Brand

Brand aliases primitives into a small set of brand roles such as `accent/*` and `content/on-accent`. Semantic tokens may reference Brand roles, but product names do not enter semantic token names.

### Experience

Experience resolves contextual design choices before the Semantic Light/Dark mapping.

| Mode | Intent | Default contexts |
|---|---|---|
| Productive | Focused, operational, repetitive, and management-oriented work | Employer panels, ATS, onboarding, dashboards, forms, tables, and workflow-heavy tools |
| Expressive | Discovery, browsing, editorial, marketing, and visually prominent experiences | Jobseeker, job pages, company pages, landing pages, campaigns, and selected prominent moments |

In v3, Experience initially controls `canvas/light` and `canvas/dark`. Expansion to typography, density, layout rhythm, or component treatments remains an open decision.

### Semantic

Semantic has Light and Dark modes and exposes stable roles such as `canvas`, `surface-*`, `fg-*`, `line-*`, and `focus-*`. It aliases the active Brand and Experience values where required.

Light/Dark is separate from Productive/Expressive. Changing either mode must not change action meaning, validation, interaction behavior, or accessibility requirements.

### Component usage

Components use Semantic tokens only. A Primary Button remains Primary and a danger state remains danger across brands, experiences, and themes.

## Experience mode rules

- Select Experience at the product, journey, or bounded surface level, not independently per component.
- Use Productive for frequent, dense, data-heavy, or time-sensitive work.
- Use Expressive for discovery, editorial, marketing, and intentionally brand-forward contexts.
- Do not mix modes inside a component.
- Both modes must meet the same contrast, focus, reduced-motion, and target-size requirements.
- Brand and Light/Dark remain separate mode dimensions.

## Naming

Mode names do not appear in Semantic token names. Do not create `productive-surface-*`, `expressive-surface-*`, `jobvision-surface-*`, or `cando-surface-*` families.

The current color vocabulary is defined in `jobvision-color-tokens-v3-surface-model.md`. The deprecated `bg-*` and `fill-*` background families must not be used for new work.

## References

- `jobvision-color-tokens-v3-surface-model.md`
- `primitive-tokens.md`
- `semantic-tokens.md`
- `component-tokens.md`
- `product-overrides.md`
- `usage-rules.md`
