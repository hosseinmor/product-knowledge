---
id: design-system.component.text-input
collection: design-system
type: component
title: Text Input
summary: '> Status: structure only; v4 Color mapping stress-tested'
knowledge_state: unverified
document_maturity: scaffold
related: []
---

# Text Input

> Status: component specification remains structure-only. The v4 Color mapping below is approved as architecture stress-test evidence; it does not finalize anatomy, dimensions, or all behavior.

## Purpose

Not yet defined in the shared component guideline.

## v4 Color Mapping Evidence

The current Semantic Color vocabulary resolves a standard Text Input without Text-Input-specific Color tokens:

```text
Label       → fg/secondary
Value       → fg/primary
Placeholder → fg/placeholder
Helper      → fg/secondary
Aux meta / character counter → fg/tertiary

Rest surface → surface/default
Rest line    → line/default
Hover line   → line/emphasis
Focus line   → line/emphasis
Focus ring   → focus/default
Error line   → line/error
Error content→ fg/error

Disabled surface → surface/disabled
Disabled line    → line/disabled
Disabled content → fg/disabled
```

### State notes

- Focus composes `line/emphasis + focus/default`; `line/emphasis` does not replace the focus indicator.
- Error Focus keeps Error meaning while Focus remains independently visible.
- `surface/error-muted` is not the default invalid-field background; it is a Support feedback surface.
- Read-only is not Disabled and does not currently justify `read-only/*` Color tokens. Its final visual/behavioral contract remains a component/form-field decision.
- A separate visual Active/Pressed state is not required for the baseline Text Input mapping.

This stress test currently validates:

```text
fg/primary
fg/secondary
fg/tertiary
fg/placeholder
fg/disabled
surface/default
surface/disabled
line/default
line/emphasis
line/error
line/disabled
focus/default
```

No `input/*`, `fg/helper`, `read-only/*`, or input-specific focus Color family is approved from this test.

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

- Full anatomy and behavior specification
- Exact Disabled label/helper treatment
- Final Read-only treatment
- Final geometry and Focus ring specification
- Validation behavior beyond the Color mapping evidence above

## Related Documents

- `../tokens/semantic-tokens.md`
- `../tokens/usage-rules.md`
- `../tokens/jobvision-color-tokens-v4-surface-model.md`
