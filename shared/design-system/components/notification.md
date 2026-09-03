---
id: design-system.component.notification
collection: design-system
type: component
title: Notification
summary: '> Status: structure only; v4 Color mapping stress-tested'
knowledge_state: canonical
document_maturity: scaffold
related:
  - design-system.governance.documentation-maintenance
---

# Notification

> Status: component specification remains structure-only. The v4 Color mappings below are **reviewed Color architecture evidence** and are authoritative for that stated scope. Final anatomy, timing, placement, dismissal, and accessibility behavior remain open.

## Purpose

Not yet fully defined in the shared component guideline.

## Severity Model

Standard system-feedback severities are:

```text
Info
Success
Warning
Error
```

Danger is not a fifth Notification severity. Danger represents destructive intent/action; Error represents validation failure or a system/problem state.

## Inline Notification Color Mapping

```text
Container    → surface/{severity}-muted
Status icon  → fg/{severity}
Title        → fg/primary
Description  → fg/secondary
Border       → line/{severity} only when the anatomy uses a semantic border
```

Only muted Support surfaces are part of the current shared Color contract. This reviewed mapping does not justify a strong `surface/{severity}-emphasis*` matrix.

## Inverse Toast Color Mapping

Toast is a transient Notification presentation. The reviewed inverse Toast composition is:

```text
Container    → surface/inverse
Title/body   → fg/on-inverse
Status icon  → fg/{severity}-inverse
Action Link  → link/inverse
```

Current inverse Support foregrounds:

```text
fg/info-inverse
fg/success-inverse
fg/warning-inverse
fg/error-inverse
```

These tokens are intentionally narrow and do not imply Support inverse surfaces or inverse line families.

## Destructive Warning

A pre-action destructive callout uses Danger rather than Error:

```text
surface/danger-muted
fg/danger
fg/primary
line/danger only when anatomy requires it
```

Example distinction:

```text
“This action permanently deletes the job.” → Danger
“Deleting the job failed.”                 → Error
```

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

- Final Notification anatomy and component variants
- Toast duration, stacking, dismissal, and announcement behavior
- Exact close/action control composition
- Final contrast validation after palette aliases are resolved

## Related Documents

- `../governance/documentation-maintenance.md`
- `../patterns/notifications.md`
- `../tokens/semantic-tokens.md`
- `../tokens/usage-rules.md`
- `../tokens/jobvision-color-tokens-v4-surface-model.md`
