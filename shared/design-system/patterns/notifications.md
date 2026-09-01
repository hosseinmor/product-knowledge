---
id: design-system.pattern.notifications
collection: design-system
type: pattern
title: Notifications
summary: System feedback uses Info, Success, Warning, and Error; Toast is a transient notification presentation.
knowledge_state: unverified
document_maturity: draft
related: []
---

# Notifications

## Problem

System feedback needs a consistent severity model across inline feedback and transient Toast presentations without creating a separate strong color matrix for every severity.

## Taxonomy

`Notification` is the shared feedback pattern. A `Toast` is a transient notification presentation, not a fifth severity and not a separate semantic color family.

Standard system-feedback severities are:

```text
Info
Success
Warning
Error
```

`Danger` is intentionally not part of this severity list. Danger communicates destructive intent/action, while Error communicates a validation failure or system/problem state.

## Inline Notification

A baseline inline notification uses a muted Support surface with readable neutral text and a severity cue:

```text
Container    → surface/{severity}-muted
Status icon  → fg/{severity}
Title        → fg/primary
Description  → fg/secondary
Border       → line/{severity} only when the anatomy uses a semantic border
```

Do not color every text element with the severity color merely because the notification has a status. Neutral readable content should remain neutral unless the anatomy has a specific reason for colored text.

Only muted Support surfaces are approved globally. Do not generate `surface/{severity}-emphasis*` without a repeated, reviewed use case.

## Inverse Toast

The approved inverse Toast composition provides the concrete use case for Support inverse foregrounds:

```text
Container    → surface/inverse
Title/body   → fg/on-inverse
Status icon  → fg/{severity}-inverse
Action Link  → link/inverse
```

Approved inverse status roles:

```text
fg/info-inverse
fg/success-inverse
fg/warning-inverse
fg/error-inverse
```

These roles mean **colored Support content on `surface/inverse`**. They do not establish Support inverse surfaces or inverse line families.

If a future Toast presentation uses a non-inverse container, map it through the corresponding documented surface contract rather than inventing new inverse semantics.

## Destructive Callouts

A pre-action destructive warning is not an Error Notification. Use Danger semantics when the message explains destructive consequences before the action occurs:

```text
surface/danger-muted
fg/danger       # status/destructive icon when needed
fg/primary      # main readable text
line/danger     # only when anatomy requires a danger outline
```

Example meaning:

```text
“This action permanently deletes the job.”
→ Danger

“Deleting the job failed.”
→ Error
```

## Actions and Close Controls

Notification actions reuse existing interaction semantics; they do not need Notification-specific action tokens.

On a normal inline notification:

```text
Close/action control → normal neutral/Link semantics
```

On an inverse Toast:

```text
Close control Hover → surface/transparent-inverse-hover
Close content       → fg/on-inverse
Navigation action   → link/inverse
```

The exact component anatomy and timing behavior remain component/pattern implementation decisions.

## Accessibility

- Severity must not be communicated by color alone when the distinction affects understanding.
- Status icons need appropriate accessible treatment when they convey meaning.
- Text and interactive controls must meet the system's eventual approved contrast targets after palette values are finalized.
- Toast announcements and focus behavior must be defined by the final Notification/Toast component implementation; Color tokens alone do not define accessibility behavior.

## Anti-Patterns

- Treating Danger as a standard fifth Notification severity
- Using `surface/error-muted` for a pre-action destructive warning solely because both Error and Danger may be red
- Creating strong Support surface matrices without a repeated need
- Creating `notification/*` Color tokens that merely alias the existing Support semantics
- Assuming the inverse Support foreground roles imply inverse Support surfaces

## Related Documents

- `../components/notification.md`
- `../tokens/semantic-tokens.md`
- `../tokens/usage-rules.md`
- `../tokens/jobvision-color-tokens-v4-surface-model.md`
- `destructive-actions.md`
