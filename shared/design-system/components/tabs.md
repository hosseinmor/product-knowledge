---
id: design-system.component.tabs
collection: design-system
type: component
title: Tabs
summary: '> Status: structure only; v4 Color mapping stress-tested'
knowledge_state: unverified
document_maturity: scaffold
related: []
---

# Tabs

> Status: component specification remains structure-only. The v4 Color mapping below is approved as architecture stress-test evidence; it does not finalize anatomy, sizes, keyboard behavior, or the full variant set.

## Purpose

Not yet defined in the shared component guideline.

## v4 Color Mapping Evidence

### Line Tab

A line-style Tab uses Accent as the selected indicator rather than a global Selected line/foreground family:

```text
Unselected label → fg/secondary
Unselected Hover → fg/primary + optional surface/transparent-hover
Selected label   → fg/primary
Selected indicator → line/accent
Focus            → focus/default
Disabled         → fg/disabled
```

The selected/current Tab has **no Hover state when it is not meaningfully interactive**. Hover on unselected Tabs does not imply Selected + Hover.

Do not add:

```text
fg/selected
line/selected
surface/selected-active
```

for this anatomy.

### Pill / Segmented-style current choice

When the grouping/anatomy already makes an exclusive current choice unambiguous, a strong neutral treatment may reuse the existing Neutral Emphasis semantics:

```text
Unselected → transparent + fg/primary
Selected   → surface/neutral-emphasis + fg/on-color
```

Do not create `surface/selected-emphasis` merely to rename this component treatment.

Any Hover/Active treatment on a current pill choice must follow the actual component interaction contract. Do not infer those states solely because the Neutral Emphasis family contains Hover/Active tokens.

### Persistent selected containers are different

`surface/selected` and `surface/selected-hover` are intended for persistent selected rows/items/containers, not as the default Tab background model.

`surface/selected-hover` applies only when the selected container remains interactive.

## Selection Principle

Selection is the component state; Accent, Neutral Emphasis, or Selected Surface is the visual treatment selected according to anatomy.

```text
Line Tab       → Accent indicator
Strong pill    → Neutral Emphasis
Selected row   → Selected surface
```

This stress test does not justify a full global Selected Color matrix.

## When to Use
## When Not to Use
## Anatomy
## Variants
## Sizes
## States
## Behavior
## Content Guidelines
## Accessibility
## Product Variations
## Figma Reference
## Code Reference

## Known Gaps

- Formal Tab anatomy and supported variants
- Rest/Hover/Focus/Disabled geometry
- Keyboard model and overflow behavior
- Exact pill/segmented component ownership
- Final typography and spacing mappings

## Related Documents

- `../experience-rules/selection.md`
- `../tokens/semantic-tokens.md`
- `../tokens/usage-rules.md`
- `../tokens/jobvision-color-tokens-v4-surface-model.md`
