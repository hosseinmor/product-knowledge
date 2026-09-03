---
id: design-system.component.modal
collection: design-system
type: component
title: Modal
summary: Modal creates a temporary blocking interaction context for a focused decision or task.
knowledge_state: unverified
document_maturity: draft
related:
- design-system.accessibility.focus-management
- design-system.accessibility.keyboard-navigation
- design-system.accessibility.screen-reader-semantics
---

# Modal

## Purpose

Modal creates a temporary **blocking interaction context** when the user must complete, confirm, or dismiss a focused task before returning to the underlying interface.

Use the Design System component name **Modal**. In accessibility semantics and standards references, the same component is a **modal dialog**.

## Use / Avoid

Use Modal for:
- confirmations and consequential decisions;
- focused forms or edits that reasonably fit in a temporary context;
- short tasks that must be resolved before the underlying page is used again;
- important information that requires an explicit response.

Avoid Modal when:
- the user should keep interacting with the underlying page — use a non-modal pattern such as Popover or Drawer where appropriate;
- the task is long, navigation-heavy, or benefits from a persistent URL/history state — prefer a page or dedicated flow;
- the message is passive feedback — use Notification/Toast instead;
- disclosure alone is needed — use an inline disclosure pattern.

Do not choose Modal only because content needs visual emphasis.

## Choices

The final shared size/variant model is not yet canonical. Until it is defined:
- do not invent reusable size names from one product screen;
- choose the smallest layout that supports the content without forcing unnecessary scrolling;
- move complex or long-running work to a page/flow rather than growing Modal indefinitely.

Dismissibility is a behavior decision, not a visual variant. A flow that cannot be dismissed must make that constraint explicit rather than merely hiding a close icon.

## Behavior and States

### Open

Opening Modal creates a new interaction scope:
- focus moves inside;
- background content becomes unavailable for interaction;
- sequential keyboard focus remains inside while Modal is active.

Do not open a Modal and leave focus on the obscured page.

### Initial focus

There is no universal target such as “first input” or “Primary Button”. Choose the logical target for the task, for example:
- first meaningful control;
- suitable static heading/content near the start of a long structured Modal;
- acknowledgement/continue action for a simple message;
- least-destructive action for a difficult-to-reverse decision.

The final component API/mechanism for selecting that strategy is still open.

### Close

Default post-close behavior is to return focus to the invoker.

If the invoker was removed or the workflow intentionally advanced, move focus to the most logical next target instead.

Dismissal rules for close button, `Escape`, backdrop interaction, and blocking workflows must be defined consistently in the final component contract. Do not let different screens invent incompatible dismissal behavior without an explicit reason.

### Loading and submit

A Modal may contain an action that enters loading/submit state. The containing flow owns business submission rules; Button/Form components own their local behavior. Do not close the Modal optimistically when failure would leave the user without a clear recovery path unless the flow explicitly defines that behavior.

## Composition and Content

A Modal normally contains:
- a clear title that identifies the task or decision;
- body/content appropriate to the task;
- actions when a response is required;
- an explicit close/dismiss control when the interaction is dismissible.

Use action hierarchy from the shared action/confirmation patterns rather than creating Modal-specific Button variants.

Keep the main decision understandable without requiring users to inspect background content that has become unavailable.

Long forms, deep navigation, dense data exploration, and multi-step workflows should be challenged before being placed in a Modal.

## Accessibility

Modal is a composite/overlay component and requires a full accessibility contract.

### Semantics

- Expose the active overlay as a modal dialog only when it actually behaves modally.
- Provide an accessible name, normally from the visible title.
- Keep programmatic name/description relationships synchronized with visible content.
- Make background content unavailable for interaction while the Modal is active; `aria-hidden` alone is not a substitute for focus containment/inertness.

### Keyboard and focus

- Focus **MUST** enter the Modal when it opens.
- `Tab` / `Shift+Tab` **MUST** remain within the active Modal interaction scope.
- Focus **MUST** remain visibly identifiable.
- On close, restore or deliberately relocate focus to preserve the user's point of work.
- Do not make static content a routine Tab stop; static content may receive programmatic focus when it is the best orientation target.

Exact dismissal keys/behavior remain part of the open dismissibility contract and must be resolved before this component is accessibility-ready.

See the shared Accessibility docs for focus, keyboard, semantics, forms, and testing requirements rather than duplicating those standards here.

## Known Gaps

The component remains `draft` because these reusable decisions are not yet complete:
- canonical anatomy and visual variants;
- size model and responsive/mobile behavior;
- scroll and sticky-header/footer behavior;
- exact dismissibility model including `Escape` and backdrop behavior;
- initial-focus configuration mechanism;
- nested/stacked Modal policy;
- action-layout defaults;
- exact Figma properties and code API;
- executable keyboard/focus/screen-reader tests.

Until these are resolved, AI and implementation work must fail open to the relevant specialized Accessibility guidance rather than treating Modal as a complete contract.

## Live References

- Figma: not yet linked in canonical metadata
- Storybook / Code: not yet linked
