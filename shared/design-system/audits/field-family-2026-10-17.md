---
id: design-system.audit.field-family-2026-10-17
collection: design-system
type: audit
title: Field Family Consistency Audit — HOS-41
summary: Current field-family decisions, verified Figma discrepancies, intentional exceptions, migration debt and runtime QA boundary.
knowledge_state: verified
document_maturity: reviewed
design_status: audit-complete
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
**Status:** Core **design/Figma audit complete** with recorded non-blocking authoring debt, independently tracked follow-ups and remaining **runtime QA**. Select and Autocomplete design handoffs remain Ready for Sandbox; this report neither reopens those decisions nor certifies Angular/Storybook.

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
| FF-01 | P2 design authoring | Select `Filled` remains a 2-value Variant axis (54 variants per set); peers use Boolean. The current runtime contract derives filled from value. | **Decision: retain Figma Filled axis for now**; removing it would require remapping published component IDs and overrides, with no approved visual benefit | [HOS-51](https://linear.app/hossein-mor/issue/HOS-51/align-select-field-label-and-authoring-properties): optional migration study after inventory of consumers; not a Sandbox blocker |
| FF-02 | P1 → **fully resolved in Figma** | Both Select sets have 6 Error focus variants. **QA discovered those 12 variants had lost 108 component-property references** during earlier variant authoring: Label/Mandatory/Error message/Open/Clear/Leading and related controls. | **Fixed in canonical sets in place**; all 108 references repaired; **12/12** authoring override tests PASS; IDs/counts unchanged (54 each). Red border + focus ring preserved. | Runtime/QA: screen reader/error relation and keyboard-only Focus+Error remain implementation acceptance cases, not Figma failures |
| FF-03 | P2 authoring | Text Input, Password and Autocomplete use `_Field Label` with Label, Required and Show info; Select uses its own Label row, `Mandatory` and a `Helper` text node with Error message binding in error states. **Select has no Show info**. | **Confirmed P2 gap**, but shared Label type style/20px row, red marker, helper/error colors and 4px anatomy are visually consistent. Runtime required semantics remain approved. | [HOS-51](https://linear.app/hossein-mor/issue/HOS-51/align-select-field-label-and-authoring-properties) for API/component-composition migration; preserve existing 108 Select variant IDs and published consumer overrides |
| FF-04 | P1 specialized migration | Number Input / Outline historically measured 4px field radius vs 6px standard; Fill legacy presentation conflicts with border-only field baseline. | **Open**; current Outline's 18 legacy variants verified; radius measurement from earlier audit | Number Input pilot: verify actual Control radius/token, choose retirement or migration for Fill, test validation states |
| FF-05 | P2 compatibility | Text Input and Autocomplete Medium default; Select Figma Large default. Number Input and Date Picker also use legacy defaults. | **Decided:** Medium for new standard runtime usages; Figma published defaults left unchanged | Migrate Figma default only with existing-instance and override plan; no Sandbox block |
| FF-06 | P1 specialized migration | Date Picker has State strings `Focus + Open`/`Active + Open` alongside a separate `Open` axis, and `Filled`, `Skeleton`, Warning state labels. | **Open** — live 33-variant structure confirmed | Date/Time pilot: simplify semantic axes, map keyboard/calendar semantics and responsive behavior |
| FF-07 | P1 docs → resolved | Select was scaffold, Autocomplete docs missing at the time of PR #92. | **Resolved in main** via PR #93 | Maintain source-of-truth docs there; do not backport old PR #92 files |
| FF-08 | P1 runtime QA | Selection Panel open-state examples visually overlap supporting text; **visual overlay does not prove broken accessibility**. | **Runtime/unverified**; Sandbox cases already specified | Dev/QA: test portal positioning, flipped placement, Escape, focus return, helper/error screen-reader access |
| FF-09 | QA → no defect | Shared Focus effect exists across sampled field controls; root clipping not confirmed as a bug. | **No Figma blocker found** | Dev/QA: test keyboard-only focus and contrast in actual browser |
| FF-10 | P2 docs → resolved | Component-specific Select and Autocomplete design contracts absent from main at original audit. | **Resolved** via PR #93 | Keep per-component docs and shared handoff |
| FF-11 | Exception → approved | Search is query-only; does not require Error/Required/Readonly axes solely for symmetry. | **Accepted intentional exception** | Maintain a valid accessible name; validated form text uses Text Input |
| FF-12 | Exception → approved | Textarea and Rich Text Editor do not share single-line control size taxonomy. | **Accepted intentional exception** | Share only relevant label/supporting/validation/accessibility rules |
| FF-13 | QA → **resolved in Figma** | Original State matrix contained an outdated Select Error focus warning and lacked a comparative Required/Info + bidi view and composed form example. | **Fixed:** [six-column Required/Info/Error focus/RTL comparison](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24186-129333), [RTL Form Playground](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24190-1516), discrepancy captions revised. No card overlap; error labels and messages verified after FF-02 repair. | Runtime visual regression for long mixed bidi content and overlay/zoom remains separate; Figma QA is complete |
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
- [HOS-51 — Select Field Label/Info authoring migration](https://linear.app/hossein-mor/issue/HOS-51/align-select-field-label-and-authoring-properties) (Backlog): address `Mandatory` vs `Required`, missing `Show info`, and optionally evaluate Filled authoring axis only with migration safety tests.\n- [HOS-50 — Anchored Disclosure Pattern review](https://linear.app/hossein-mor/issue/HOS-50/review-anchored-disclosure-pattern-and-slot-contract) (**ON HOLD**): own Trigger/Surface Slot architecture and reopen decisions **outside** HOS-41. The Figma prototype and old PR #92 content remain references, not approved current documentation.

These are separate items. Their implementation or review is **not required** to close the core Field Family consistency audit once the unresolved core differences are documented, assigned and non-blocking.

## Current Figma QA execution — completed 2026-10-19

**Structural comparison:** [Six-column cross-control board](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24186-129333). Linked real component instances for Text Input, Password, Search, Select / Single, Autocomplete / Single and Select / Multiple. Three scenarios: **Required + Info**, **Error + Focus**, and **mixed Persian/Latin long content**. Search legitimately has no Required or form Error axis.

**Form Playground:** [Composed RTL form](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24190-1516), with editable Text Input/Autocomplete labels, Select Error focus, required markers and contextual error copy. Live instances remain linked to canonical published sources; no speculative new Field shell was added. Example text includes `Senior Product Designer — تهران / Remote`.

**Verified observations**
- Shared `_Field Label` supports Label, Required, Show info in Text Input/Password/Autocomplete. Select renders Label/Mandatory with equivalent measured type style and 20px row but has **no Show info**. This is a P2 authoring gap, now owned by HOS-51.
- Text Input/Password/Autocomplete use shared `_Field Helper` / `_Field Error`; Select's direct `Helper` text layer uses the appropriate error foreground in Error and Error focus, but the layer name/composition is legacy and must not be treated as a second separate helper at runtime.
- **High-priority defect resolved:** 12 Select Error focus components initially lacked 108 Property bindings inherited from the corresponding Error variants. All mappings were restored in place, including Label, Mandatory, custom Error message, Clear, Leading and Open. **12/12 temporary real-instance override tests passed**, and test instances were removed. The Form Playground now correctly displays customized city label/error.
- Figma screenshot and geometry checks: **0 overlapping QA cards**, **28px vertical spacing** between board sections, no label overflow in the displayed mixed-language **label** specimen (observed 272px label text within 288px field boundary). Input/Search/Autocomplete long **values** have visual truncation in the specimen. Long Select option **values** and keyboard bidi behavior are not certified without runtime tests.
- Reviewed Default, Focus and Error focus with helper/error messaging plus Disabled and Read only in the original five-state matrix; no confirmed residual core Figma visual blocker. The existing open Selection Panel specimen is a visual stacking check only; accessibility still needs runtime QA.

**Accepted non-blocking authoring debt:** published Select `Filled` variant axis; Large default in Figma vs Medium new runtime usage; shared Label/Info migration (HOS-51). Do not alter 108 published component IDs to chase API symmetry without consumer override migration. Search/textarea/rich-editor specialized exceptions remain intentional.

**Outcome:** Core **Figma/authoring audit PASS**; runtime implementation/keyboard/a11y QA **NOT VERIFIED** and not implied by this document.

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
- [x] Validate shared Label/Required/Info and support/error anatomy across core controls on current Figma QA board (P2 Select Info gap delegated to HOS-51).
- [x] Review Filled/default migration risk; retain compatibility, defer optional Select authoring migration to HOS-51.
- [x] Refresh live RTL Form Playground and bilingual long-text specimens; record residual runtime-only cases.
- [x] Split Number Input and Date/Time migration into independently tracked HOS-48 and HOS-49.
- [x] Resolve discovered P1 Select Error focus authoring binding regression; assign remaining P2 Label/Info gap to HOS-51.
- [ ] **Runtime-owned follow-up:** record Angular/Storybook acceptance results when implementation is available. Not a Figma-audit closure gate; status stays unverified.
- [x] Complete QA review of the audit-only PR and prepare it for merge; independent of held Disclosure Pattern.

## PR provenance / governance

Original [PR #92](https://github.com/hosseinmor/product-knowledge/pull/92) included early Select/Autocomplete documentation and Anchored Disclosure Pattern drafts that are now superseded or held. It was **not** a safe merge candidate. This audit is migrated onto a **fresh branch from current main**, containing only the Field Family discrepancy register; it does not change `components/select.md`, `components/autocomplete.md`, or `patterns/anchored-disclosure.md`. The repository automatically regenerates `manifest.generated.json` to index this new audit document; its extra diff is an expected documentation-index update, not a manual component or Pattern change.

The separate Anchored Disclosure Pattern remains **on Hold** for review of its interaction contract; no new design decision is asserted by this PR.
