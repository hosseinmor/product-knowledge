---
id: design-system.foundation.color
collection: design-system
type: foundation
title: Color
summary: Operational entry point for JV Color semantics, token architecture, Product × Appearance behavior, accessibility, and source routing.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.token.architecture
  - design-system.token.semantic-tokens
  - design-system.token.component-tokens
  - design-system.token.product-overrides
  - design-system.accessibility.color-and-contrast
  - design-system.reference.source-of-truth
last_reviewed: '2026-09-10'
---

# Color

Color communicates structure, hierarchy, interaction, Product identity, system feedback, and a small number of reviewed product meanings. Choose it by semantic role rather than by hue.

This document is the compact entry point. It defines durable rules and routes exact questions to the owning source instead of duplicating the full token catalog or Figma value table.

## Color model

The normal product-UI path is:

```text
Default
Primitive → Semantic → Product UI

Optional Product identity
Primitive → Brand → Semantic → Product UI

Exceptional component-owned contract
Primitive / Semantic / Brand → Component → Product UI
```

- **Primitive** stores context-free Color values and hue scales.
- **Brand** resolves Product identity only where a role intentionally varies by Product.
- **Semantic** is the normal shared UI Color API.
- **Component** Color tokens are exceptional and exist only when a stable component-owned meaning cannot be expressed by Semantic roles.

Product UI should consume Semantic tokens or an approved Component token. Do not bind product UI directly to Primitive or Brand variables.

Categorical Tag colors are the current approved Component-level Color exception. They may resolve directly to Primitive hues because their meaning belongs to Tag categorization rather than to a shared system semantic. Do not reuse Tag tokens as a general categorical palette for unrelated components.

## Product × Appearance

Color resolves two independent Theme dimensions:

```text
Product    → JobVision | Cando
Appearance → Light | Dark
```

Do not encode Product and Appearance into combined Semantic modes. Resolve them as independent dimensions.

The current Figma Color model is:

```text
01 Primitives → Value
02 Brand      → JobVision | Cando
03 Semantic   → light | dark
04 Component  → Light | Dark
```

`01 Primitives` and `02 Brand` are hidden from library publishing. `03 Semantic` is the normal public shared Color API; `04 Component` exposes only approved component-owned contracts.

Brand currently keeps the same Product mapping across Light and Dark. If real dark-theme UI validation proves that Brand needs Appearance-aware values, introduce the minimum additional aliasing without changing the public Semantic names.

Dark Appearance is a **dimmed-dark** theme with independently resolved Semantic aliases; it is not a numerical inversion of Light.

## Semantic boundaries

| Need | Use |
|---|---|
| Page, container, depth, or neutral interaction | `surface/*` |
| Text or icon | `fg/*` |
| Divider, outline, or boundary | `line/*` |
| Product identity or approved key conversion moment | Brand semantics |
| General chromatic interaction or affordance | Accent |
| AI-assisted or AI-generated capability | Magic |
| Destructive intent or irreversible action | Danger |
| Information, success, warning, or error feedback | Support |
| Navigation link | `link/*` |
| Keyboard focus indication | Focus roles |

Brand is not a synonym for primary, selected, focused, or important. Accent is not system feedback. Danger and Error may share Red primitives while remaining different meanings: Danger is destructive intent; Error is validation or system failure.

Selection is primarily a component state expressed through component anatomy. Do not create a parallel global Selected Color matrix. Use existing Surface, Foreground, Line, and Accent roles; only the reviewed persistent neutral selected-container surfaces are shared semantics.

Transparent interaction states and overlay are represented by resolved Semantic Color values themselves. A published alpha-palette API is not part of the current Color contract.

## Primitive palette rules

Primitive families are named by hue, not by Product or semantic ownership. The same hue ramp may feed several independent meanings.

For example, Blue may feed JobVision Brand, Accent, Link, Info, and a categorical Tag without those roles becoming interchangeable.

Do not add a hue family only to make the palette visually complete. Add or split one when a real Semantic or Component use case requires a distinct tonal range, or when contrast and appearance validation show that the current palette cannot serve the required roles.

Primitive step numbers represent tonal order; they are not semantic labels. Equivalent roles across different hues do not need the same numeric step.

## Accessibility

WCAG 2.2 AA is the web baseline. Validate **actual Semantic pairings and component states**, not isolated Primitive swatches.

- Normal text should meet the applicable text contrast requirement in its real background/state pairing.
- Essential non-text boundaries and focus indicators should meet their applicable contrast requirement.
- Disabled appearance is not a reason to make required explanatory content unreadable.
- Color must not be the only signal for state, validation, status, or meaning when another perceivable cue is required.
- Focus is independent from Brand and Accent so it remains visible across supported Product × Appearance contexts.

For exact acceptance rules and edge cases, use [`../accessibility/color-and-contrast.md`](../accessibility/color-and-contrast.md).

## Where exact truth lives

- Token graph and layer responsibilities → [`../tokens/architecture.md`](../tokens/architecture.md)
- Semantic role meanings and boundaries → [`../tokens/semantic-tokens.md`](../tokens/semantic-tokens.md)
- Exact current aliases and visual values → current Figma variables; use [`../tokens/color-token-aliases.md`](../tokens/color-token-aliases.md) for the documented mapping contract
- Product identity and Product × Appearance constraints → [`../tokens/product-overrides.md`](../tokens/product-overrides.md)
- Component-owned Color exceptions such as Tag → [`../tokens/component-tokens.md`](../tokens/component-tokens.md)
- Accessibility and contrast requirements → [`../accessibility/color-and-contrast.md`](../accessibility/color-and-contrast.md)
- Source conflicts and ownership → [`../integrations/source-of-truth.md`](../integrations/source-of-truth.md)

Figma owns current editable visual values and aliases. Design System Knowledge owns semantic meaning and usage. Code/Storybook owns the runtime API and implemented behavior when available. A mismatch between them is a maintenance gap; do not invent a compromise.

## AI retrieval rule

For a Color question, start here and load only the next source needed:

```text
Color foundation
→ semantic meaning question?      semantic-tokens.md
→ architecture/layering question? architecture.md
→ exact current value/alias?       Figma, then color-token-aliases.md
→ Product variation?               product-overrides.md
→ Tag/component exception?         component-tokens.md
→ contrast/accessibility?          accessibility/color-and-contrast.md
```

Do not preload or reproduce the full token catalog when a semantic rule is sufficient. Do not infer unresolved runtime Theme, CSS variable, Tailwind, or SSR behavior from the Figma model.
