---
id: design-system.component.tooltip
collection: design-system
type: component
title: Tooltip
summary: '> Status: structure only'
knowledge_state: unverified
document_maturity: scaffold
related:
  - design-system.component.icon-button
---

# Tooltip

> Status: structure only

Tooltip is not yet finalized. HOS-17 owns its complete visual, behavioral, accessibility, RTL, placement, timing, touch, and runtime contract.

## Known Consumer Contract — Icon Button

The finalized Icon Button contract establishes one upstream requirement that Tooltip must support:

- every operable Icon Button requires a visible Tooltip label;
- the Tooltip appears on pointer hover and keyboard focus;
- Tooltip content is non-interactive and does not become a focus destination;
- it can be dismissed with `Escape`;
- moving focus away dismisses it;
- by default, its text matches the Icon Button accessible action name;
- Tooltip does not replace the Icon Button's programmatic accessible name;
- Tooltip must not be the only source of essential instructions or state;
- touch interaction must not depend on Tooltip discovery.

This section is a consumer requirement, not a completed Tooltip implementation contract.

HOS-17 must still define:

- open/close delay;
- placement and collision/flip behavior;
- supported positions;
- arrow/pointer rules;
- max width and wrapping;
- typography, padding and radius;
- color, border/elevation and contrast;
- animation/reduced-motion behavior;
- touch/mobile behavior;
- label vs description semantics;
- RTL details;
- boundaries with Popover and Coachmark/Tour;
- runtime API and implementation strategy when the owning source becomes available.

Disabled Icon Buttons must not depend on Tooltip as the only explanation for why an action is unavailable.

## Purpose
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
