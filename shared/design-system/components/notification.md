---
id: design-system.component.notification
collection: design-system
type: component
title: Notification
summary: '> Status: structure only; v4 Color mapping stress-tested'
knowledge_state: unverified
document_maturity: scaffold
last_reviewed: 2026-09-19
related: []
---

# Notification

> Status: component specification remains structure-only. The v4 Color mappings below are approved as architecture stress-test evidence. Final anatomy, timing, placement, dismissal, and accessibility behavior remain open.

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

## Inline Notification Working Contract

### Content model

Inline Notification uses a stable vertical content model rather than a responsive layout variant:

```text
Status icon
Content
  Message      required
  Description  optional
  Action       optional; always below the text content
Dismiss        optional; absolute, independent from Content
```

A short one-line notification is the same component with Description omitted. Do not create a separate one-line or "Inline Long" variant.

The Action belongs to Content and remains below the text at all widths. This avoids consuming horizontal reading space on narrow containers and avoids adding a responsive Action-position variant.

Action does not define notification-specific text styling or interaction states. It reuses the canonical interaction primitives:

- navigation / destination change → Link;
- operation / state change in the current context → Button.

The Figma component exposes a swappable `Action control` instance with Link as the default composition. Use a Button only when the action has Button semantics. Keep at most one action.

### Typography and foreground

```text
Message      → Heading/SM          14/20, 700, fg/primary
Description  → Body/Compact/SM     14/20, 400, fg/primary
Action       → shared Link or Button component; Notification does not own its typography recipe
```

Description is part of the primary feedback message, not helper metadata, so it uses `fg/primary`. Keep Description concise; one or two wrapped lines are compatible with Body/Compact. Paragraph-like or reading-oriented content should use regular Body or a different pattern.

### Color mapping

```text
Container    → surface/{severity}-muted
Status icon  → fg/{severity}
Message      → fg/primary
Description  → fg/primary
Border       → none in the current canonical anatomy
Shadow       → none
```

Only muted Support surfaces are approved globally. A Notification does not justify a strong `surface/{severity}-emphasis*` matrix.

### Width

Inline Notification has no intrinsic component-level max width. It fills the available width of the related content container and must not exceed that container. Page-level readability is controlled by the page/grid container, not by Notification.

The 560px width used in the current Figma component set is an example authoring width, not a maximum.

## Dismiss Control

Notification does not create a local close control. Dismiss reuses the canonical Icon Button:

- Style: `Ghost`;
- Size: `Medium` — 40×40px;
- Icon: `close` at the shared 18px Icon Button visual size.

For the canonical RTL layout, Dismiss is absolutely positioned flush to the physical top-left of the Notification surface:

```text
top = 0
left = 0
size = 40 × 40
```

Equivalent logical runtime intent:

```css
dismiss {
  inset-block-start: 0;
  inset-inline-end: 0;
}
```

Content reserves 32px of left-side internal space. With the surface's 16px outer padding, readable content begins at x=48 while the Dismiss hit area ends at x=40, preserving an 8px safe gap.

Dismiss must not participate in the normal flow or reduce the horizontal reading width of the Notification. `Dismissible=False` hides the Icon Button but does not change the content geometry.

## Toast Contrast Treatments

Toast is a transient Notification presentation with two contrast treatments:

```text
Contrast = Normal
Container    → surface/default
Message/body → fg/primary
Status icon  → fg/{severity}
Action Link  → link/default
Elevation    → Shadow/Floating

Contrast = High
Container    → surface/inverse
Message/body → fg/on-inverse
Status icon  → fg/{severity}-inverse
Action Link  → link/inverse
Elevation    → Shadow/Floating
```

`Normal` is the default treatment. `High` is an alternate high-contrast treatment; it is not a severity.

Approved inverse Support foregrounds:

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

- Final Toast duration, stacking, placement, dismissal, and announcement behavior
- Shared Link/Icon Button inverse-surface treatment is still missing from those primitives. High-contrast Toast currently uses inverse semantic overrides on the nested canonical instances; move that treatment into the shared primitives before runtime handoff.
- Final content-writing guideline and examples
- Final contrast validation after palette aliases are resolved

## Related Documents

- `../patterns/notifications.md`
- `../tokens/semantic-tokens.md`
- `../tokens/usage-rules.md`
- `../tokens/jobvision-color-tokens-v4-surface-model.md`
