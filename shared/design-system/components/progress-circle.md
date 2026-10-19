---
id: design-system.component.progress-circle
collection: design-system
type: component
title: Progress Circle
summary: Shared circular progress component for measured work and unknown activity; Loading consumes its indeterminate preset.
knowledge_state: verified
document_maturity: draft
design_status: in-review
status: draft
owner: Design System team
last_reviewed: '2026-10-19'
related:
  - design-system.component.loading
  - design-system.component.progress-bar
  - design-system.accessibility.dynamic-content-and-feedback
  - content.pattern.loading-and-progress
  - design-system.reference.component-mapping
topics: [progress, progress-circle, determinate, indeterminate, feedback]
---

# Progress Circle

## Purpose and Use

Progress Circle communicates an ongoing operation in a compact circular form. Use Determinate when completed work and a reliable total are known; use Indeterminate when they are unknown. Prefer Progress Bar when a horizontal track supports reading and comparison. Use [Loading](loading.md) for a standard local busy indicator and Button integration.

Workflow steps belong to Progress Indicator / Stepper. Static capacity, scores and ratings are not operation progress. Completion and failure require their own result feedback; a circle reaching 100% does not establish success.

## Choices

Choose Small, Medium or Large to fit the surrounding composition. Neutral is the default; Accent emphasizes the active operation while keeping a neutral track; On color is for a contrasting emphasis surface. Place any operation label and visible percentage outside the ring, especially at compact sizes.

Determinate Figma instances expose the nested **Progress value** with 0, 25, 50, 75 and 100% snapshots. These are design illustrations, not a numeric API or a limit on runtime precision. Do not label a 50% illustration as 37%. Loading intentionally hides this authoring choice.

## Behavior and States

- Runtime must accept actual validated values throughout the valid range, including intermediate percentages. Derive the fill and any percentage text from the same completed/total source; never invent advancement or remaining time.
- Unknown or unreliable values remain indeterminate. Switch to determinate when reliable values become available. Zero is a known value and must not represent unknown work.
- At 0% show the neutral track without a foreground arc; at 100% show the complete foreground circle. Partial arcs start at the top and progress clockwise in RTL and LTR, with flat endpoints.
- Reuse existing semantic roles: Neutral arc `fg/primary`, Accent arc `fg/accent`, On color arc `fg/on-color`; track `line/default`, or `line/inverse` for On color. Preserve full opacity. No new component color tokens or LoopState API are introduced.
- Indeterminate rotation shares the existing four-phase source. Its Figma wiring is a motion reference; runtime should use appropriate shared motion guidance and support reduced motion with readable status context.

## Accessibility

Provide an accessible name for the operation. When exposing progressbar semantics, provide the truthful current value and valid range for determinate work; omit the current value for indeterminate work. A nested decorative ring must not duplicate an already accessible Button/region busy indication. Announce meaningful changes without announcing every animation frame. See [dynamic content and feedback](../accessibility/dynamic-content-and-feedback.md) and [WAI-ARIA progressbar](https://www.w3.org/TR/wai-aria-1.2/#progressbar).

## Known Gaps

Figma variants, snapshot swapping, source composition and token bindings are verified. Arbitrary numeric authoring in Figma, runtime/Storybook identities, production motion, reduced-motion handling and executed accessibility tests remain unsupported or unverified. This is a design-review draft.

## Live References

- [Progress Circle / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24203-116)
- Stable public/private source identities: [component mapping](../integrations/component-mapping.md).
- Storybook / code: unregistered.
