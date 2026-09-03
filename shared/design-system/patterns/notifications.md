---
id: design-system.pattern.notifications
collection: design-system
type: pattern
title: Notifications
summary: Defines shared feedback severity and when feedback appears inline or as a transient Toast.
knowledge_state: unverified
document_maturity: draft
related:
- design-system.accessibility.dynamic-content-and-feedback
---

# Notifications

## Problem and Use

Notifications communicate system feedback without turning every success, warning, or failure into a different interaction model.

Use this pattern when the interface needs to communicate a system state or result such as:
- information;
- success;
- warning;
- error.

Standard feedback severities are:

```text
Info
Success
Warning
Error
```

`Danger` is **not** a fifth notification severity. Danger describes destructive intent before an action; Error describes a failure/problem state.

## Structure / Flow

The shared pattern has two common presentations:

### Inline Notification

Use when the message should remain visible near the affected content or when users may need time to read or act on it.

Baseline visual semantics:
- muted severity surface;
- readable neutral title/body;
- severity cue through icon and/or line when the anatomy uses one.

Do not color all text simply because the message has a severity.

### Toast

Toast is a transient presentation of a Notification, not a semantic role and not another severity.

Use for short feedback that does not need to remain in the layout, such as routine confirmation after an action.

A Toast may use an inverse presentation when that is the approved component treatment. Exact visual mappings belong to the current token/component implementation rather than this pattern.

## Rules and States

### Severity is not urgency

Visual severity and assistive-technology announcement urgency are separate decisions.

For example:
- an Error does not automatically require an assertive announcement;
- a Success does not automatically need a live announcement if focus/context already communicates the result.

Use the least interruptive mechanism that still communicates the change.

### Destructive warning vs Error

```text
“This action permanently deletes the job.”
→ Danger / destructive pattern

“Deleting the job failed.”
→ Error Notification
```

Do not use Error merely because destructive actions and errors may share a red hue.

### Actions

Notification actions reuse existing Button/Link semantics. Do not create notification-specific action styles only because an action appears inside feedback.

If a transient Toast includes an action, users must have enough opportunity to perceive and operate it. A Toast should not steal focus merely because it appeared.

### Close / dismissal

Dismissibility and timing belong to the concrete Notification/Toast component contract. They must be consistent enough that users can predict whether a message persists, disappears, or can be manually dismissed.

## Components

This pattern composes:
- `Notification` for the feedback container/presentation;
- existing Button/Link/Icon Button components for actions or dismissal when needed;
- semantic Support/Danger tokens according to the message meaning.

The component owns anatomy and implementation mechanics; this pattern owns severity meaning and presentation choice.

## Accessibility

- Severity must not rely on color alone when the distinction affects understanding.
- A Toast is a visual pattern; choose status/live semantics from message importance, not from the fact that it is a Toast.
- Routine confirmation should normally be non-interruptive.
- Do not move focus to a Toast or spinner merely to announce it.
- Interactive Toast controls must be keyboard accessible without automatic autofocus.
- If a message disappears automatically, applicable timing requirements must still be met.
- Avoid duplicate feedback such as focus movement + alert + Toast for the same event unless deliberately justified and tested.

Programmatic status/alert behavior is owned by `accessibility/dynamic-content-and-feedback.md`.

## Variations and Gaps

Current reusable decisions still needed before this pattern is `reviewed`:
- Toast timing and persistence policy;
- stacking/queue behavior;
- maximum simultaneous Toasts;
- dismissibility defaults;
- actionable Toast persistence/fallback;
- responsive placement;
- final relationship between inline Notification and Toast component variants;
- executable announcement/focus tests.

Do not invent a full matrix of strong severity surfaces or notification-specific token families to fill these gaps.

## Live References

- Figma: use the current Notification/Toast component when available
- Storybook / Code: not yet linked
- Related component: `../components/notification.md`
- Destructive behavior: `destructive-actions.md`
