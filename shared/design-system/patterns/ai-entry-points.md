---
id: design-system.pattern.ai-entry-points
collection: design-system
type: pattern
title: AI Entry Points
summary: AI-assisted and AI-generated experiences may use the shared Magic color semantics.
knowledge_state: canonical
document_maturity: draft
related: []
---

# AI Entry Points

## Problem

AI capability appears across more than one component anatomy. The interface needs a repeatable visual language that can identify AI-assisted or AI-generated experiences without turning every AI element into Brand, Accent, Selected, or Support feedback.

## When to Use

Use Magic when the UI is explicitly communicating an AI-assisted, AI-generated, or intentionally magical product capability.

Typical uses include:

- AI entry cards or sections
- AI chips/labels
- AI-specific icons or inline indicators
- AI-owned interactive pills, controls, or entry surfaces that are not the standard shared Button component
- AI-specific outlines when the component anatomy needs a line

Do not use Magic merely as a decorative purple treatment.

## Color Semantics

```text
surface/magic-muted
→ subtle AI card, section, chip, or container

surface/magic-emphasis
surface/magic-emphasis-hover
surface/magic-emphasis-active
→ strong AI-owned interactive surface when that anatomy is not the standard shared Button component

fg/magic
→ AI icon, label, sparkle, or inline emphasis

line/magic
→ AI-specific outline/indicator when required by anatomy
```

The component's interaction model still determines which states exist. A passive AI container does not gain Hover or Active merely because Magic Emphasis has those state tokens available.

## Button Boundary

Magic does **not** define a Button preset or Button tone in v4.

When the action is implemented with the shared Button component, choose its visual treatment from the canonical Button hierarchy:

```text
Brand
Primary
Secondary
Tertiary
Ghost
Danger
```

according to the action's actual role. Use Magic on the surrounding AI container, icon, label, indicator, or another AI-owned anatomy to communicate the AI capability.

Do not create a purple/Magic Button simply by binding a Button to `surface/magic-emphasis*`. If repeated product evidence later requires a Magic-styled standard Button, the Button component contract must be explicitly reviewed and extended first.

## Semantic Boundary

Magic means AI capability. It does not replace:

- Brand for product identity or approved conversion moments
- Accent for general chromatic interaction/affordance
- Selected for a component state
- Support for Info/Success/Warning/Error feedback

If an AI feature is also selected, disabled, focused, or in error, compose the relevant component/state semantics rather than using Magic to encode every state.

## Component Composition

Use shared Semantic Color tokens directly where the component anatomy can express the pattern. Do not create an `ai-card/*` Color-token family solely to rename Magic roles.

Do not create an `ai-button/*` family or bypass the Button preset model solely because an action belongs to an AI feature.

Component-specific tokens require a stable AI component contract that cannot be represented by the existing Semantic vocabulary.

## Accessibility

- Magic color must not be the only cue that an experience is AI-assisted when that distinction is important to understanding or trust.
- Preserve readable text contrast on Magic surfaces.
- Focus remains independent and uses the shared Focus roles.
- Disabled suppresses tone according to the component's normal Disabled contract.

## Product Examples

Current reviewed use-case categories include AI cards/sections, AI chips/labels, AI-owned entry surfaces, and AI icons/indicators across JobVision and Cando experiences.

Exact product-level component mappings remain owned by the corresponding component/product documentation.

## Anti-Patterns

- Using Magic for any visually special CTA that is not AI-related
- Using Magic instead of Brand for product identity
- Using Magic instead of Accent for ordinary interaction
- Using Magic instead of Error/Warning/Info feedback
- Treating `surface/magic-emphasis*` as an undeclared Magic Button preset
- Building a full component-specific Magic matrix when shared Semantic roles already resolve the anatomy

## Related Documents

- `../components/button.md`
- `../tokens/semantic-tokens.md`
- `../tokens/usage-rules.md`
- `../tokens/jobvision-color-tokens-v4-surface-model.md`
