---
id: design-system.component.timeline
collection: design-system
type: component
title: Timeline
summary: A compositional vertical RTL sequence of chronological events or scheduled time groups, shared by Job Vision My Applications and employee Onboarding.
knowledge_state: verified
document_maturity: draft
design_status: in-progress
design_maturity: visual-pilot
related:
  - design-system.component.progress-indicator
  - design-system.accessibility.core
---

# Timeline

## Purpose

Timeline presents **what happened** or **what is scheduled at specific points in time**, in a vertical chronological sequence. The number and content of items are not predetermined. It is primarily read-only.

Current pilot supports two verified product use cases:

1. **Onboarding — scheduled task groups:** each relative date/time group is a Timeline Item, with one or more tasks composed inside the Content slot. Examples: «۷ روز قبل از شروع کار» and «روز شروع کار».
2. **Job Vision / My Applications — event history:** each application event is a Timeline Item, usually with a title, timestamp, and event-type icon. Examples: application sent, resume seen, review prioritized, application approved.

Both use the same Figma primitives. Do not create `ScheduleTimeline` or `ApplicationTimeline` variant axes.

## Not for

- **Progress Indicator / Stepper (HOS-31):** fixed sequence of known workflow steps with complete/current/upcoming/blocked statuses (e.g. hiring request approval). Use the Stepper, whether showing a workflow preview or the progress of an actual request.
- **Activity Feed:** comment/mention/reaction-centric interactions and conversations.
- **Audit Log:** technical before/after change records, actor/field-level audit, or immutable compliance history.
- Horizontal, alternating, or two-sided sequences in v1.

The Timeline must not acquire Stepper's completed/current/upcoming state model.

## Verified Figma identity

- Figma file: `[DS] Job Vision NEXT`
- File key: `rROD8ctH9UfPGAMrRrOzHe`
- Page: `Timeline`, node `23509:9`
- Component set: `Timeline Item`, node `23509:48`
- Parent component: `Timeline`, node `23509:49`
- Unified documentation frame: `23530:140`, containing Header, Component Set, Playground, Anatomy & usage, and Responsive QA.
- Playground with both product use cases: `23511:13370`
- Narrow/long-title QA: `23519:121`, verified at 360px width

Figma link: https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23509-9

Exact published component keys are **not yet verified**; do not invent them.

## Component contract (Figma)

### Timeline

`Timeline` is a vertical auto-layout container with a native **Items Slot**. The consumer inserts any number of `Timeline Item` instances in chronological order. It does not have an event-count variant and does not sort data.

### Timeline Item

Structure:

```
Timeline Item
├── Content (vertical, RTL right-aligned)
│   ├── Title (TEXT property)
│   ├── Timestamp (TEXT property, optional via BOOLEAN)
│   └── Content slot (native Figma SLOT, optional and hidden by default)
└── Axis (24px, right-hand side in RTL)
    ├── Marker (Dot or icon)
    └── Connector (BOOLEAN visibility)
```

| Property | Contract |
|---|---|
| `Density` | `Default`, `Compact` |
| `Marker` | `Dot`, `Icon` |
| `Title` | Editable string |
| `Timestamp` | Editable display string |
| `Show timestamp` | Boolean |
| `Show connector` | Boolean. Normally false on last visible item |
| `Show content` | Boolean; default false. Enable only when the Content slot is needed. Empty history events do not reserve slot space |
| `Icon` | Instance-swap property, available for Icon marker |
| `Content slot` | Native Figma SLOT for optional descriptions, task lists, metadata, links, or actions |

Four main visual variants: `Density=Default/Compact × Marker=Dot/Icon`. Icon identity, task count, event count, content presence, semantic status, and ordering **are not variant axes**.

### Anatomy, tokens, and geometry

- Axis: fixed 24px wide, on the **right** of content in RTL.
- Dot: neutral 8px circle.
- Icon: 20px visual inside the 24px axis; use the approved DS Icon component and override its fixed source color to the appropriate semantic foreground.
- Connector: 1px, `line/default`; stretches with item content, hidden on the final item. Its start is separated from the 24px marker container by 8px, and the axis reserves 8px beneath the connector. Never attach the line directly to an icon.
- Text: title uses `Label/SM`; timestamp uses `Body/XS`; both use Vazirmatn text styles.
- Foreground: `fg/primary` for title, `fg/tertiary` for timestamp, `fg/secondary` for the default marker/icon.
- Spacing: axis–content gap 12px Default / 8px Compact; content vertical gap 8px Default / 4px Compact; marker–connector gap 8px and axis bottom padding 8px. Base content bottom spacing is 16px Default / 12px Compact. Derive these from existing Spacing variables.
- The 560px Figma component canvas width is an example, **not** a required runtime width; content, title, timestamp and slots support fill and wrap.
- Use the DS radius variables for any surrounding cards. Timeline itself has no card surface or border.

Avoid a color scale tied to relative timing ("before / starting day / after") as generic Timeline state; those distinctions belong to the use case/content semantics, not the Timeline component contract.

## Use case composition

### Onboarding — Schedule Timeline

Each time bucket such as `۷ روز قبل از شروع کار` is one item. Date goes in Timestamp; related scheduled tasks are a list inside Content slot with `Show content=true`. A time bucket with three tasks still has **one** marker. Task rows do not get Timeline connectors or individual Timeline markers.

The task list, status of individual tasks, task type icons, navigation targets and whether a task is completed are the responsibility of the composed task content, not the Timeline Item.

### My Applications — Event History

Each actual event is one item. Keep `Show content=false` unless a real explanation, action, or additional metadata is needed; no empty placeholder space should appear. Keep the event title primary and date/time secondary; type-appropriate icons may replace the neutral dot. The icon must not be the sole carrier of meaning. The title should describe the event in words. These event records are not fixed process steps.

## Ordering and grouping

- The product passes items in the intended order; Figma and runtime Timeline do **not** automatically reverse or sort.
- History may be oldest-first or newest-first depending on consumer context; the application must choose deliberately.
- Onboarding is ordered by scheduled relative time.
- Grouping by date is composition (group heading or time-bucket item), not a `Grouped=true` variant.
- One empty date group must not produce a false event. Empty states and loading skeletons are owned by the product container, not the Timeline primitive.

## Interaction

- Timeline Item is noninteractive by default; do not turn the full item into a generic clickable surface.
- Interactive links/buttons may be composed in Content slot and must keep native focus, accessible names and keyboard behavior.
- Markers and connectors are decorative unless additional programmatically exposed meaning is explicitly designed.
- No built-in approval decision, task completion action, status transition, or navigation API.

## Accessibility and RTL

- Preserve a meaningful chronological reading order independent from the visuals.
- In implementation, prefer ordered sequence semantics such as an ordered list of events, with a machine-readable date/time when available. Exact HTML, props and event schema are **unverified runtime implementation recommendations**, not registered API facts.
- Ensure relative date labels have an understandable absolute date for assistive technology where meaningful.
- Hide decorative connector from screen readers; avoid announcing both marker icon and redundant title.
- In RTL, axis is on the right, content is right-aligned, vertical order is unchanged.
- Long event titles wrap rather than truncate; markers align to the beginning/first line of each item. Text and Content slot fill available width.

## Figma QA performed

- [x] Four variant components and named axes.
- [x] Native Figma Items and Content slots.
- [x] Real Onboarding time groups with 1–3 tasks per item.
- [x] Real My Applications event types with icon swapping.
- [x] Last-item connector hidden in both product examples.
- [x] Vazirmatn styles and semantic color/spacing bindings.
- [x] Responsive 360px example with a two-line event title and correctly stretching connector.
- [x] RTL alignment and variable-height item composition visually reviewed.
- [ ] Final product-owner approval of visual design.
- [ ] Runtime/Storybook registration, DOM semantics, API and dynamic data verification.
- [ ] Published component keys / full component mapping registration.

## Status of runtime and sources

This is a **Figma-verified visual/design contract**. No owning runtime or Storybook Timeline source has been verified in this task. Do not infer production TypeScript prop names, exact DOM hierarchy, sorting behavior or event payloads from the Figma implementation. Implement/runtime QA as a distinct follow-up once an owning source is registered.
