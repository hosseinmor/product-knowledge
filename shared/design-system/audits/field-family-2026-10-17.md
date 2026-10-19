---
id: design-system.audit.field-family-2026-10-17
collection: design-system
type: audit
title: Field Family Consistency Audit — HOS-41
summary: Current field-family decisions, verified Figma discrepancies, intentional exceptions, migration debt and runtime QA boundary.
knowledge_state: verified
document_maturity: draft
design_status: audit-in-progress
related:
  - design-system.component.text-input
  - design-system.component.search
  - design-system.component.select
  - design-system.component.autocomplete
  - design-system.accessibility.forms
---

# Field Family Consistency Audit — HOS-41

**First audit:** 2026-10-17 · **Updated against live Figma and main:** 2026-10-19  
**Tracker:** [HOS-41](https://linear.app/hossein-mor/issue/HOS-41/audit-and-standardize-field-family-across-figma-and-design-system)  
**Live comparison:** [QA · Field Family](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23915-841)  
**Status:** In progress. The core Select and Autocomplete **design handoffs** have been approved for Sandbox independently; this audit does not re-open those approvals or claim Angular/Storybook implementation has been tested.

## Scope and separation of responsibilities

| Area | Included | Decision |
|---|---|---|
| Core, single-line | Text Input, Password Input, Search, Select / Single and Multiple, Autocomplete / Single | Audit shared Field anatomy, semantics and visual tokens while keeping distinct interaction models |
| Multiline | Textarea | Shared supporting/validation semantics, but not obliged to adopt single-line size axis |
| Specialized | Rich Text Editor | Separate editing/toolbar structure |
| Migration | Number Input, Date Picker / Time Picker | Register inconsistencies and **separate migration**; do not redesign quietly as part of the core pilot |
| Supporting | Label/Required/Info, helper/error, Selection Panel/Option, Form | Audit shared boundary and authored/accessible error/focus/required states |
| Excluded | **Anchored Disclosure Pattern and Chip popup composition** | Hold; not a blocker for this audit, Select or Autocomplete |

**Authoritative current source:** [Select](../components/select.md), [Autocomplete](../components/autocomplete.md) and their [Sandbox acceptance handoff](../handoffs/select-autocomplete-sandbox.md), merged in [PR #93](https://github.com/hosseinmor/product-knowledge/pull/93). The old Select/Autocomplete files on PR #92 are **superseded and must not be merged**. Disclosure Pattern remains in the held Figma prototype and is not published by this audit.

## Verified current Figma baseline

| Component | Node | Verified authoring axes / current condition |
|---|---|---|
| Text Input | `22780:548` | Shared standard field anatomy; size and required authoring differ from legacy Select |
| Password Input | `22823:128654` | Text Input-related field with reveal action |
| Search | `22827:261` | Purposefully small State set (Default/Hover/Focus/Disabled) |
| Select / Single | `20552:3939` | **54 variants** = Size 3 × State 9 × Filled 2; **Error focus added**, six combinations |
| Select / Multiple | `23742:5660` | **54 variants** = Size 3 × State 9 × Filled 2; **Error focus added**, six combinations |
| Autocomplete / Single | `23861:24` | **24 variants** = Size 3 × State 8, including Error focus and Read only focus |
| Textarea | `22800:128313` | Multiline control; size axis not required |
| Rich Text Editor | `22866:134455` | Toolbar/editor semantics, independent of standard single-line State list |
| Number Input / Outline | `12046:265141` | **18 variants** = Size 3 × legacy State 6 (Enabled, Focus, Disabled, Error, Warning, Skeleton); older audit measured **4px** Control radius (recheck before migration) |
| Date Picker / Single calendar | `3697:51812` | **33 variants** = Size 3 × State 11; default Size **Large**, legacy states `Enabled`, `Focus + Open`, `Active + Open`, `Filled`, `Skeleton` and a separate Open axis. Specialized migration needed |
| Selection Panel | `20619:306` | Shared Select/Autocomplete surface, not an Anchored Disclosure dependency |

Select Figma's default Size remains **Large** for compatibility; the approved **new-usage/runtime design default is Medium (40px)**. The `Filled` Figma variant and `Mandatory` authoring name are **non-blocking legacy authoring debt**, not separate production flags.

## Discrepancy register

| ID | Priority | Decision / observation | Current status | Next action and owner |
|---|---|---|---|---|
| FF-01 | P2 design authoring | Select `Filled` is a 2-valued variant axis, whereas peer controls use a Boolean preview property. This doubles Select's variant count, but is **not** a runtime value state. | **Accepted compatibility debt**, not Sandbox blocker | Design System: evaluate migration only after an override-preservation audit of existing consumer instances |
| FF-02 | P1 → resolved in Figma | Both Select sets were missing `Error focus`. | **Resolved**: 6 new Error focus per set; 54 variants/set; red error border + focus ring | Runtime/QA: verify keyboard-only Focus+Error, helper/error announcement in Storybook |
| FF-03 | P1 authoring → P2 migration | Select Label row/Helper and `Mandatory` naming differ from shared `_Field Label`/`Required` authoring patterns. | **Runtime semantics approved**, visual/API migration **open** | Design System: standardize shared contract and separately test compatibility before renaming/restructuring Figma |
| FF-04 | P1 specialized migration | Number Input / Outline historically measured 4px field radius vs 6px standard; Fill legacy presentation conflicts with border-only field baseline. | **Open**; current Outline's 18 legacy variants verified; radius measurement from earlier audit | Number Input pilot: verify actual Control radius/token, choose retirement or migration for Fill, test validation states |
| FF-05 | P2 compatibility | Text Input and Autocomplete Medium default; Select Figma Large default. Number Input and Date Picker also use legacy defaults. | **Decided:** Medium for new standard runtime usages; Figma published defaults left unchanged | Migrate Figma default only with existing-instance and override plan; no Sandbox block |
| FF-06 | P1 specialized migration | Date Picker has State strings `Focus + Open`/`Active + Open` alongside a separate `Open` axis, and `Filled`, `Skeleton`, Warning state labels. | **Open** — live 33-variant structure confirmed | Date/Time pilot: simplify semantic axes, map keyboard/calendar semantics and responsive behavior |
| FF-07 | P1 docs → resolved | Select was scaffold, Autocomplete docs missing at the time of PR #92. | **Resolved in main** via PR #93 | Maintain source-of-truth docs there; do not backport old PR #92 files |
| FF-08 | P1 runtime QA | Selection Panel open-state examples visually overlap supporting text; **visual overlay does not prove broken accessibility**. | **Runtime/unverified**; Sandbox cases already specified | Dev/QA: test portal positioning, flipped placement, Escape, focus return, helper/error screen-reader access |
| FF-09 | QA → no defect | Shared Focus effect exists across sampled field controls; root clipping not confirmed as a bug. | **No Figma blocker found** | Dev/QA: test keyboard-only focus and contrast in actual browser |
| FF-10 | P2 docs → resolved | Component-specific Select and Autocomplete design contracts absent from main at original audit. | **Resolved** via PR #93 | Keep per-component docs and shared handoff |
| FF-11 | Exception → approved | Search is query-only; does not require Error/Required/Readonly axes solely for symmetry. | **Accepted intentional exception** | Maintain a valid accessible name; validated form text uses Text Input |
| FF-12 | Exception → approved | Textarea and Rich Text Editor do not share single-line control size taxonomy. | **Accepted intentional exception** | Share only relevant label/supporting/validation/accessibility rules |
| FF-13 | P2 Figma QA | Representative cross-control Playground and Label/Required/Info alignment are not yet fully reconciled after recent component changes. | **Open** | Design System: refresh QA instances and verify five states, RTL, error/required, helper geometry without editing controls unnecessarily |
| FF-14 | P1 runtime | Exact Angular/Storybook props, DOM role strategy, ControlValueAccessor wiring and automated tests have not been verified here. | **Unverified — not a confirmed defect** | Dev/QA: run and record Sandbox acceptance matrix; do not fabricate runtime facts |

**Critical distinction:** `Resolved in Figma`, `Approved design semantics`, `Runtime verified`, and `Closed migration` are different statuses. This document does not conflate them.

## Shared Field contract — current decisions

| Dimension | Normative default | Legitimate specialization |
|---|---|---|
| Insertable control | Public component must be usable directly with label and supporting anatomy | Shared private Field primitives allowed |
| Height | Small 32px, Medium 40px **new default**, Large 48px | Textarea and Rich Text Editor content-driven |
| Control radius and surface | 6px; border-only input/select | Legacy Number/Date migrations tracked separately |
| Floating surface | Radius 12px, 2px trigger gap | Selection Panel; may flip/portal without covering assistive-tech access to errors |
| Focus | Visible semantic Focus effect, independent of validation error | Readonly focus where the platform keeps readonly focusable |
| Validation | Error border 2px + text message + programmatic association; Error and Focus coexist | Warning reserved for approved use cases, not mandatory on every Field |
| Label/Required/Info | Consistent visible label or accessible equivalent; semantic `required` | Historical Figma `Mandatory` maps to required, not a second runtime flag |
| Helper/Error priority | Error supersedes helper in validated-invalid state | Textarea count is optional; product controls own exact copy |
| Filled | Figma visual preview, not runtime boolean | Runtime derives from value/query; Select Filled migration optional |
| Disabled vs readonly | Distinct semantics and legible readonly value | Specialized controls can justify deliberate exceptions |
| RTL | Logical start/end, icons and controls consistent; mixed Persian/Latin tests | Popup/list navigation semantics tested in runtime |
| Select / Autocomplete | Different non-editable-select vs editable-query semantics | Refer to separate approved handoff; keep runtime value policies explicit |

## Independent migration and held Pattern follow-ups

- [HOS-48 — Number Input migration](https://linear.app/hossein-mor/issue/HOS-48/audit-and-migrate-number-input-to-field-family) (Backlog): validate the historical 4px radius finding, Filled/Outline topology, numerical semantics and safe migration.
- [HOS-49 — Date/Time Picker migration](https://linear.app/hossein-mor/issue/HOS-49/audit-and-migrate-datetime-picker-field-contract) (Backlog): resolve legacy `State + Open` axes, calendar/time keyboard behavior and specialized validation.
- [HOS-50 — Anchored Disclosure Pattern review](https://linear.app/hossein-mor/issue/HOS-50/review-anchored-disclosure-pattern-and-slot-contract) (**ON HOLD**): own Trigger/Surface Slot architecture and reopen decisions **outside** HOS-41. The Figma prototype and old PR #92 content remain references, not approved current documentation.

These are separate items. Their implementation or review is **not required** to close the core Field Family consistency audit once the unresolved core differences are documented, assigned and non-blocking.

## Cross-component QA plan

Use [Field Family QA board](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23915-841) as a **live instance dashboard**, not a replacement for component-level tests.

- **Static Figma**: Text Input / Password / Search / Select Single / Autocomplete / Select Multiple at Default, Focus, Error+Focus (where valid), Disabled, Read only, filled and empty values. Audit Control geometry, typography, leading/trailing, helper/error, RTL and parent clipping.
- **Dynamic/runtime**: use [Select + Autocomplete handoff](../handoffs/select-autocomplete-sandbox.md) for 27 acceptance cases; run keyboard, screen reader, 200% zoom, long mixed-language labels, portal flip, loading/empty/error, selected vs highlighted vs query.
- **Migration**: separate Number Input and Date Picker tickets/matrix; do not silently fold their redesign into the core Field consistency audit.

### Closure gates

- [x] Initial discrepancy register and shared baseline written.
- [x] Confirm Select/Autocomplete have final component docs and Sandbox criteria merged in main.
- [x] Add and visually QA Select Error focus in Figma.
- [x] Approve Standard Size 32/40/48 and runtime/default usage = Medium, with compatibility exception documented.
- [x] Accept intentional Search, Textarea, Rich Text Editor differences.
- [ ] Validate shared Label/Required/Info and support/error anatomy across core controls on current Figma QA board.
- [ ] Review current Figma defaults and Filled migration **risk**, record whether further Figma refactor is worth it.
- [ ] Refresh the representative Form Playground and test long text / bidi / visual overflow.
- [x] Split Number Input and Date/Time migration into independently tracked HOS-48 and HOS-49.
- [ ] Confirm any remaining core visual discrepancy and its owner/severity; leave none silently open.
- [ ] Record Angular/Storybook QA outcome when runtime is registered; missing runtime checks must remain explicitly unverified (not assumed PASS).
- [ ] Review and merge this **audit-only PR**. This is independent of the held Disclosure Pattern.

## PR provenance / governance

Original [PR #92](https://github.com/hosseinmor/product-knowledge/pull/92) included early Select/Autocomplete documentation and Anchored Disclosure Pattern drafts that are now superseded or held. It was **not** a safe merge candidate. This audit is migrated onto a **fresh branch from current main**, containing only the Field Family discrepancy register; it does not touch `components/select.md`, `components/autocomplete.md`, `manifest.generated.json`, or `patterns/anchored-disclosure.md`.

The separate Anchored Disclosure Pattern remains **on Hold** for review of its interaction contract; no new design decision is asserted by this PR.
