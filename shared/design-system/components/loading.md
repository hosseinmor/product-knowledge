---
id: design-system.component.loading
collection: design-system
type: component
title: Loading
summary: Compact indeterminate activity feedback composed from Progress Circle, including dimensionally stable Button loading.
knowledge_state: verified
document_maturity: draft
design_status: in-review
status: draft
owner: Design System team
last_reviewed: '2026-10-19'
related:
  - design-system.component.progress-circle
  - button
  - design-system.component.progress-bar
  - design-system.accessibility.dynamic-content-and-feedback
  - content.pattern.loading-and-progress
  - design-system.reference.component-mapping
topics: [loading, spinner, busy, feedback]
---

# Loading

## Purpose and Use

Loading communicates that an identifiable local action or region is busy when reliable progress is unavailable. Use [Progress Circle](progress-circle.md) or [Progress Bar](progress-bar.md) for measured work, and Skeleton when the expected content structure provides more useful context. Choose by the information available and the affected area; no universal duration threshold is defined.

## Choices

Use Small for inline status and every Button size, Medium for a local content region, and Large for an appropriately large loading area. Neutral is the default, Accent provides interaction emphasis, and On color is for a contrasting emphasis surface. Pair the indicator with understandable task context.

Loading is the **indeterminate preset of Progress Circle**. Its public choices remain Size and Color; it exposes no progress value, interaction State, LoopState or Inline size. Inline is composition. Success, failure and inactivity belong to the task's result feedback rather than spinner variants.

## Behavior and Composition

- Accent retains a neutral unfilled track. All arcs have flat endpoints, full paint/layer opacity and existing semantic colors; no component-specific color tokens are required.
- In Button, retain the original Loading Small source at 16px. Match the arc to the Button label foreground. Use `line/inverse` on enabled/hover/active/focus filled Brand, Primary and Danger Primary styles, `line/default` on other enabled styles, and `line/disabled` on every disabled style.
- Preserve Button width, height, label/icon layout space and focus. Center the spinner and suppress repeated activation while busy. Busy feedback does not itself decide whether other actions are blocked.
- Rotation remains clockwise in RTL and LTR. Reduced motion must retain readable busy context without relying on movement. Figma's four-phase loop is a prototype reference, not runtime motion validation.

## Accessibility

Keep the operation's accessible name and expose the busy state on the relevant action or region. Treat the nested spinner as decorative when that context already conveys the same information; avoid duplicate announcements or a second competing live region. Indeterminate activity must not expose a fabricated numeric value. Follow [dynamic content and feedback](../accessibility/dynamic-content-and-feedback.md) and the [content pattern](../../content/patterns/loading-and-progress.md).

## Known Gaps

Figma composition and semantic bindings are verified. Runtime/Storybook identities, production animation, reduced-motion behavior and assistive-technology behavior remain unregistered or untested. This is a design-review draft.

## Live References

- [Loading / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24144-128998)
- [Progress Circle / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24203-116)
- Stable source identities and migration boundaries: [component mapping](../integrations/component-mapping.md).
- Storybook / code: unregistered.
