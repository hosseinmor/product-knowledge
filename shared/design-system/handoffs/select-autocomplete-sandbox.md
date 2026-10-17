---
id: design-system.handoff.select-autocomplete-sandbox
collection: design-system
type: development-handoff
title: Select & Autocomplete — Sandbox Handoff
summary: Implementation-ready decisions, source mapping, event/state model, acceptance tests, and explicit non-blocking Figma migration debt.
knowledge_state: verified
document_maturity: implementation-ready
design_status: ready-for-sandbox
related:
  - design-system.component.select
  - design-system.component.autocomplete
  - design-system.component.text-input
  - design-system.accessibility.forms
---

# Select & Autocomplete — Sandbox Development Handoff

**Date:** 2026-10-17  
**Tickets:** [HOS-32 Select](https://linear.app/hossein-mor/issue/HOS-32/pilot-select-component-across-figma-and-design-system-knowledge), [HOS-38 Autocomplete](https://linear.app/hossein-mor/issue/HOS-38/pilot-autocomplete-component-across-figma-and-design-system-knowledge).  
**Scope:** Angular/Tailwind Sandbox, component behavior, component Storybook tests, visual/a11y smoke tests. This handoff does **not** sign off production and does not infer existing runtime API names.  
**Dependencies:** Field-family shared label/helper/error and Selection Panel/Option primitives. **Disclosure Pattern HOS-30 is on Hold and is NOT a dependency.**

## Authoritative order for implementation

1. This handoff's decisions and component contracts [Select](../components/select.md), [Autocomplete](../components/autocomplete.md) (behavior + expected states).
2. Canonical live [Select / Single](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=20552-3939), [Select / Multiple](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23742-5660), [Autocomplete / Single](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23861-24), [Selection Panel](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=20619-306), [Field Family QA](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23915-841).
3. Existing registered Angular component architecture, package conventions, Storybook, forms/ControlValueAccessor and theme semantic tokens: inspect the runtime repository first, preserve compatible APIs and report conflicts before unapproved breaking changes.

**No duplication**: do not rebuild Selection Panel/Option styling from scratch inside every consumer if the runtime can share appropriate primitives. Do not wrap full Selection Panel inside a second Popover shell.

## Scope decisions — frozen for Sandbox v1

| ID | Decision |
|---|---|
| H-01 | Select and Autocomplete are two distinct field controls. Select has a non-editable trigger; Autocomplete owns an editable query input. |
| H-02 | Select supports Single ID, Multiple ID[]; Autocomplete v1 supports only Single. |
| H-03 | Autocomplete `valuePolicy` has two explicit modes: `free-form` (job title) and `selection-required` (city/job group). `creatable` postponed. |
| H-04 | Medium control 40px default for **new usage**, Small 32px, Large 48px. Radius 6px, label/helper semantics shared. Popup 12px radius, 2px anchored offset. |
| H-05 | Error and Focus coexist. Select Single/Multiple Error focus variants added in Figma; Autocomplete already supports Error focus. |
| H-06 | Readonly ≠ Disabled; readonly keeps value visible, cannot open/edit/clear; focus remains visible if the platform uses focusable readonly. |
| H-07 | Figma `Filled` describes authoring-only value/placeholder previews. Runtime uses real selected value/query; no runtime `filled` Boolean. |
| H-08 | Figma `Mandatory` is historical. Runtime/public contract uses `required`, without forcing a breaking rename of published Figma properties. |
| H-09 | Select Single commits on choosing option, then closes. Multiple supports staged/confirmed and immediate modes; confirm footer requires real draft selection. |
| H-10 | Search within Select's Panel can be filterable; Autocomplete reuses Panel with `Filterable=False` to avoid nested queries. |
| H-11 | Select Multiple display policy is count or labels+`+N` overflow. Use ID[] as source of truth in either display policy. |
| H-12 | Input/Suggestion errors, empty state and loading are distinct from form Validation Error. |
| H-13 | RTL is baseline, with mixed Persian/Latin option labels and stable logical start/end. |
| H-14 | No coupling to the separately held Disclosure / Anchored pattern. |
| H-15 | Angular public props/events and exact DOM/ARIA role strategy follow runtime architecture, subject to functional and accessibility acceptance tests below. |

## Interaction acceptance matrix

Implement each test as an automated Storybook play test, unit test, integration test or equivalent where possible; verify manual screen-reader and viewport cases on actual Runtime. Mark Pass/Fail/Blocked with evidence in the Sandbox handoff.

| Test | Scenario / steps | Expected |
|---|---|---|
| S-01 | Single empty, open with pointer | Placeholder visible, options rendered once, overlay anchored, no layout jump |
| S-02 | Single arrow down then Enter | Highlight moves without changing committed value; Enter commits ID, closes, displays label |
| S-03 | Single Escape/Tab with pending highlight | Original committed value unchanged; Escape closes; Tab exits predictably |
| S-04 | Single clear, required + invalid, Error + Focus | Clear follows validation policy; textual error and focus ring both visible; proper invalid association |
| S-05 | Single readonly / disabled | Readonly keeps readable value, no popup/clear; disabled inert and visibly distinct |
| M-01 | Multiple open, select 2, dismiss without Confirm | If confirm mode: draft discarded and last committed values unchanged |
| M-02 | Multiple select 2, Confirm | IDs committed exactly once; summary count = 2; popup closes; outside + escape work |
| M-03 | Multiple immediate mode | Each choice immediately commits, panel stays open, no dead Confirm |
| M-04 | Multiple filter, Select All | Selects enabled filtered options only; hidden prior selections retained; Indeterminate accurate |
| M-05 | Multiple display labels +N overflow, long values | Correct count, truncation, ID fidelity; no unintended wrapping |
| P-01 | Selection Panel Results, Empty, fetch Error | Appropriate mode, retry affordance when applicable; no loss of selected value |
| P-02 | Panel open below/above with helper/error, scroll, viewport edge | Overlay not clipped and does not push form; field helper/error accessible |
| A-01 | `free-form` type arbitrary title, Enter without highlight | Commits free-form text, closes; no option ID required |
| A-02 | `free-form` blur with pending query | Commits normalized query; product text retained |
| A-03 | `selection-required` city: type unmatched text, blur | No invalid free text committed; restores last selected city/placeholder |
| A-04 | `selection-required` city: move active option, Enter | Selected option ID committed; correct label; closes |
| A-05 | Autocomplete Escape with pending query | Restores last committed value and closes without change event |
| A-06 | Autocomplete clear, reopen, disabled, readonly | Value/query cleared as specified, no stale highlight; disabled and readonly cannot edit/open |
| A-07 | Autocomplete rapid async q1 → q2 with q1 response last | q1 ignored/aborted; q2 results only; no stale active-descendant |
| A-08 | Loading → Empty → Error from results provider | Distinct polite announcements; invalid form styling unaffected by transport failure |
| A-09 | Autocomplete optional chevron off/on | Off by default; on opens list without compromising editable query or causing duplicate input |
| F-01 | Each control Small/Medium/Large, Default/Hover/Focus/Disabled | Figma sizes, semantic tokens, readable text and focus ring |
| F-02 | Each control Error focus, readonly + value | Correct error border+focus ring, helper/error priority, no dead actions |
| F-03 | Keyboard end-to-end: Tab, Enter, Space, Up/Down, Escape | No keyboard trap or accidental form submit; highlight ≠ committed selection |
| F-04 | VoiceOver or NVDA smoke test | Meaningful label, required/invalid, selected state, expanded state, active option, updates announced |
| F-05 | Persian/Latin, mixed bidi numbers, long strings, 200% zoom, narrow viewport | Stable logical RTL anatomy; no clipping, overflow or blocked touch controls |
| F-06 | Existing consumer forms and CVA integration | No backward-incompatible existing public API; controlled and reactive form value updates correct |

## Runtime implementation checklist for Claude / Developer

- [ ] Find current owning package/repository; inspect Angular, Tailwind and Storybook conventions, field primitive/component architecture, ControlValueAccessor and existing Select API before writing new code.
- [ ] Implement Select Single and Multiple preserving option identity separate from label.
- [ ] Implement Autocomplete Single with explicit `valuePolicy`.
- [ ] Reuse Selection Panel and Option rendering/styling and semantic tokens; do not duplicate Popover shell.
- [ ] Support local + remote suggestion sources; ignore stale response and expose Loading/Empty/Error independently from validation.
- [ ] Implement keyboard, focus management, ARIA, accessible error/helper, disabled/readonly, RTL.
- [ ] Create explicit Storybook variants for states and both value policies, Single/Multiple and overflow.
- [ ] Run tests S/M/P/A/F above and report deviations with screenshot/log evidence.
- [ ] QA display at small/medium/large and light/dark if themes are supported by the product.
- [ ] Document runtime API actually implemented and reconcile it with the conceptual contracts before Production/Ready for Dev status.

## Deliberately non-blocking authoring debt

- Figma Select `Filled` remains a 2-valued variant axis; avoid an unnecessary destructive 54→27 migration while bootstrapping Sandbox. If replaced later, test overrides across existing product instances.
- Figma Select `Mandatory` will be migrated to Required in a separate authoring change, not implemented as a distinct runtime API.
- Figma Select default variant remains Large to preserve references. New product usage and runtime default choose Medium explicitly.
- Figma Select Warning is a legacy optional visual; v1 does not need a warning prop unless product evidence requires it.
- Disclosure / Anchored Pattern, Chip / Disclosure Open authoring API, Select Multiple as Chips, Autocomplete Multiple / creatable, advanced remote ranking, and mobile bottom sheet alternate layout remain separate future scopes.

## Readiness gate

**Ready for Sandbox** = normative interaction/visual/RTL/a11y specification published and Figma canonical sources documented; **NOT** proof of runtime implementation. **Ready for Dev/Production** only once implementation, Storybook, keyboard/a11y, visual and regression checks above pass. Report deviations as blockers, do not silently treat intended designs as tested code.
