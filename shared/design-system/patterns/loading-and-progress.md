---
id: design-system.pattern.loading-and-progress
collection: design-system
type: pattern
title: Loading and Progress
summary: Loading usage pattern using Progress Circle Indeterminate directly, with measured progress, Skeleton boundaries, stable Button composition and announcement ownership.
knowledge_state: verified
document_maturity: draft
design_status: in-review
status: draft
owner: Design System team
last_reviewed: '2026-10-19'
related:
  - design-system.component.progress-circle
  - design-system.component.progress-bar
  - button
  - design-system.accessibility.dynamic-content-and-feedback
  - content.pattern.loading-and-progress
  - design-system.reference.component-mapping
topics: [loading, progress, busy, spinner, skeleton, feedback]
---

# Loading and Progress

**Loading is a usage pattern, not a separate component.** Compose [Progress Circle](../components/progress-circle.md) in **Indeterminate** mode directly with the action or region's task context. Button consumes the same component directly; no Loading wrapper is required.

## Problem

Users need to understand which operation is pending, whether useful progress can be measured, and which actions remain available. An activity indicator must not imply an invented percentage or automatically block the whole interface.

## When to Use

| Available information / context | Feedback |
|---|---|
| Local busy action, no reliable total | Progress Circle / Indeterminate |
| Known completed work and reliable total | Progress Circle / Determinate or Progress Bar / Determinate |
| Operation already represented by a linear track, progress unknown | Progress Bar / Indeterminate |
| Expected content structure is useful while initial data is pending | Skeleton |
| Ordered workflow steps | Progress Indicator / Stepper |

Choose by useful context and the affected area. No universal time threshold is defined. Static capacity, ratings and scores are not operation progress.

## Structure

The pattern consists of an indicator, understandable task context and a clear busy scope. The context can be the existing Button name, adjacent status text, or the labelled content region; every spinner does not require a new message or live region.

## Behavior

- Use Indeterminate for unknown or unreliable progress; expose no guessed percentage or ETA. Switch to Determinate when a trustworthy value and total become available.
- Keep known zero distinct from unknown work. Fill and visible percentage must share the same real source. Reaching 100% does not establish success; show the operation's actual result separately.
- Block only dependent interactions and prevent duplicate activation. The flow owns whether other actions are blocked; the indicator does not define that policy.
- Preserve keyboard focus and the operation's accessible name. Loading must not itself move focus.
- Rotation remains clockwise in RTL and LTR. Respect reduced-motion preferences while keeping readable busy context. Figma's four-phase reference does not establish validated production animation or final shared motion timing.

## Component Composition

- **Button:** directly nest Progress Circle / Indeterminate / Small, 16px at every Button size. Preserve width, height and label/icon layout space while visually hiding the replaced content. Keep the ring centered when labels and optional icons change.
- **Inline status:** Small ring at logical start, with an 8px gap to text. In RTL it appears to the right. Let long text wrap without shrinking the ring or changing its position.
- **Local content region:** Medium is the normal choice; Large fits an appropriately large area. Center feedback within the affected region and identify the pending operation.
- Use existing semantic colors and full opacity. Accent keeps a neutral unfilled track; arc endpoints are flat. No Loading-specific color tokens, LoopState property, Inline size or outcome variant family is introduced.
- In Button, match the arc to the label foreground. Track uses `line/inverse` for filled Brand/Primary/Danger Primary styles, `line/default` for other enabled styles and `line/disabled` for every disabled style. Preserve the busy style's identity rather than automatically restyling it as Disabled.

## Variations

Neutral is the default; Accent emphasizes an active operation, and On color is for a contrasting emphasis surface. Size and color are choices of Progress Circle itself. Loading does not add another public component API.

## Accessibility

The consuming action or region owns its accessible name, busy state and announcements. Treat its nested ring as decorative when that context already communicates the operation. Avoid duplicate status messages or competing live regions. When exposing progressbar semantics, provide a truthful numeric value/range for determinate work and omit the current value for indeterminate work. Do not announce animation frames. Follow [dynamic content and feedback](../accessibility/dynamic-content-and-feedback.md) and [Loading and Progress content](../../content/patterns/loading-and-progress.md).

## Product Examples

The [Figma Loading · Pattern page](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24144-128998) demonstrates RTL inline status, local regions, larger areas, real Button styles, Light/Dark and long mixed-script text. These are design compositions, not evidence of product-specific behavior.

## Anti-Patterns

- Fabricated progress or a percentage on indeterminate activity.
- A separate Loading wrapper duplicating Progress Circle.
- Success/Error/Inactive variants on the activity indicator.
- Layout shifts or loss of the Button's operation name/focus.
- One live region for the Button and another announcing the same nested ring.

## Verification and Live Sources

HOS-46: all 160 loading Button masters and three File Uploader spinner sources directly use Progress Circle; current examples were migrated. Old Loading masters were removed after their instance count reached zero. The unused legacy Inline status family was also removed. Figma geometry and contextual semantic bindings are verified; runtime/Storybook identities, production motion, reduced motion and executed assistive-technology behavior remain unregistered or untested.

- [Progress Circle / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24203-116)
- [Loading · Pattern](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24144-128998)
- Stable source identities: [component mapping](../integrations/component-mapping.md).
