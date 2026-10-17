---
id: design-system.audit.field-family-2026-10-17
collection: design-system
type: audit
title: Field Family Consistency Audit — HOS-41
summary: Verified structural drift across the current field-family Figma components, with prioritization and explicit exceptions.
knowledge_state: verified
document_maturity: draft
related:
- design-system.component.text-input
- design-system.component.search
- design-system.component.select
- design-system.component.autocomplete
- design-system.accessibility.forms
---

# Field Family Consistency Audit — HOS-41

**Date:** 2026-10-17  
**Scope:** shared Job Vision NEXT fields in live Figma, current Design System Knowledge, and any registered runtime only when independently inspected.  
**Tracking:** [HOS-41](https://linear.app/hossein-mor/issue/HOS-41/audit-and-standardize-field-family-across-figma-and-design-system)  
**Live QA:** [QA · Field Family · HOS-41](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23915-841)

This is a **verified design-source audit**, not an assertion that the corresponding Angular or Storybook implementation has been tested. The matrix uses live linked component instances. Open decisions are labeled as proposals, not canonical commitments.

## Scope and hierarchy

| Tier | Components | Rationale |
|---|---|---|
| Core — shared single-line | Text Input, Password Input, Search, Autocomplete / Single, Select / Single, Select / Multiple | Shared 32/40/48px control foundation; distinct semantics |
| Core — multiline | Textarea | Shared label/error/focus, specialized multiline height and optional count |
| Specialized | Rich Text Editor | Toolbar/editor semantics, intentional exclusion of generic one-line size axis |
| Migration | Number Input, Date Picker / Time Picker | Legacy topology, tokens and state vocabulary; do not silently promote to ready-for-dev |
| Adjacent only | Selection Panel, Option, Form, File Uploader | Review only where they share field anatomy or popup behavior |

## Confirmed structural observations

| ID | Severity | Evidence in Figma | Proposed reconciliation | Status |
|---|---|---|---|---|
| FF-01 | P1 | Select / Single `20552:3939` and Multiple `23742:5660`: `Filled` is a Variant axis (3 sizes × 8 states × 2 values = **48 variants each**). Text Input `22780:548` / Autocomplete `23861:24` / Search `22827:261` / Password `22823:128654` use a Boolean authoring property. | Move filled/empty display to a Boolean authoring property **only after instance override regression testing**; keep selected value semantics independent at runtime. | Open — breaking-risk analysis |
| FF-02 | P1 | Select states include Default, Hover, Focus, Disabled, Error, **Warning**, Read only, Read only focus; no **Error focus**. New Text Input, Autocomplete, Password and Textarea expose Error focus. | Support independent Focus + Error visual composition. Decide whether to migrate Select's Warning to a form-level pattern rather than requiring every field to expose Warning. | Open |
| FF-03 | P1 | Select has its own Label row, Helper and `Mandatory` name; Text Input/Autocomplete/Password/Textarea use nested `_Field Label` plus contextual supporting parts and `Required`. | Reconcile authoring names and visual layout; preserve independently insertable public components, rather than requiring manually assembled Field shells. | Open |
| FF-04 | P1 migration | Number Input / Outline `12046:265141` has measured **4px** control radius; expected shared Medium radius is **6px**. Number Input / Fill `16956:281046` retains a filled-style legacy variant. | Redesign legacy Number Input as a separate pilot; use border-only field treatment unless explicitly warranted by a verified product case. | Open — migration |
| FF-05 | P2 | Default `Size` is Medium on Text Input, Search, Autocomplete, Password; Large on Select, Number Input and Date Picker. | Use Medium default on standard controls, subject to product exceptions and existing consumer migration. | Open |
| FF-06 | P2 | Number Input and Date Picker use legacy state labels Enabled, Skeleton, Active, Filled, Warning, Error. | Normalize a shared semantic model and record intentional specialized exceptions; avoid converting `Filled` or `Open` into CSS interaction state. | Open — migration |
| FF-07 | P1 docs | `shared/design-system/components/select.md` was a scaffold and `autocomplete.md` absent on main at audit start. | Provide verified-as-observed Figma contracts and explicitly mark unresolved runtime/accessibility choices. | Draft docs on HOS-41 branch |
| FF-08 | QA | Select and Autocomplete reuse `Selection Panel` `20619:306`, with visible panel separation 2px and floating radius 12px. Popup instances overlap the supporting-content region visually when open. | Check anchored overlay stacking, clipping, helper/error accessibility, and real runtime portal positioning with a dedicated regression. Do not treat visual occlusion as a definite runtime defect without testing. | Needs runtime/visual test |
| FF-09 | QA | Text Input/Password/Autocomplete/Search apply shared Focus effect `S:5c95b61d670ff12aa3df0239375089cca68a0d15`; sampled focus component roots do not clip. | Keep effect model; verify keyboard-only focus in browser before reporting a focus-ring defect. | No confirmed defect |
| FF-10 | P2 docs | Text Input, Password, Search and Textarea have detailed verified/draft docs; Select and Autocomplete lacked equivalents on main. | Keep docs per specialized component, with this audit as a shared contract/decision matrix. | Draft docs |
| FF-11 | QA | Search `22827:261` exposes Default, Hover, Focus, Disabled only. | **Intentional exception** for a query-only control; do not add Error, Required, or Read only solely for symmetrical axes. Consumers needing validated form entry should use Text Input. | Accepted as audit guideline |
| FF-12 | QA | Textarea `22800:128313` has State × Supporting, no Size axis, and uses a 120px high sample Control. Rich Text Editor `22866:134455` has Toolbar + Supporting axes. | **Intentional difference**; do not force single-line size axes onto multiline/specialized editors. | Accepted as audit guideline |

**Not audited as runtime fact:** exact Angular selector, inputs/outputs, filtering pipeline, keyboard event handling, DOM structure, overlay positioning engine, browser autofill, or portal behavior.

## Proposed shared Field contract

These are the proposed family defaults; specialized exceptions remain explicit.

| Dimension | Baseline | Approved exception / responsibility |
|---|---|---|
| Public composition | Directly insertable field per use case | Internal `_Field Label`, helper/error subcomponents may be shared |
| Standard sizes | Small 32px, Medium 40px (default), Large 48px | Textarea/Rich Text Editor keep content-specific height; migration fields TBD |
| Control geometry | Radius 6px; border-based surface; no layout shift on state | Floating popup shell radius 12px, 2px trigger-to-panel gap |
| Standard focus | 2px visible ring + 1px offset independent from border | Applied to relevant focusable controls; no global forced Focus state prop |
| Error | 2px error border + textual error + programmatic invalid relationship | Error/focus may coexist; error policy and copy from Form/Product |
| Field label | Label/Required/optional Info; visible or valid accessible alternative | Search standalone may omit visible label only with proper accessible name |
| Supporting | Helper non-error; textual Error when invalid | Count optional for multiline controls |
| Value display | Empty/filled authoring property in Figma when useful | Runtime always derives from actual value/query; separate Selected for options |
| Adornments | Semantic leading/trailing in RTL, 16px icon, 8px icon/content gap where applicable | Search icon fixed; password visibility action specialized; Select chevron |
| Disabled / Read only | Semantically different; readonly value stays legible | Whether readonly is exposed is component-specific, not mandatory across every control |
| Tokens | Shared semantic roles for surface/fg/line/focus | No field-specific token family for restating shared roles |
| Accessibility | Native semantics where appropriate; associations for label/description/error; visible keyboard focus | Select/Autocomplete must document combobox/listbox strategy when runtime is registered |

## QA matrix

The Figma QA page contains **linked live instances** to detect visual drift without modifying canonical component sets:

- 6 columns: Text Input, Password Input, Search, Select / Single, Autocomplete, Select / Multiple.
- Default, Focus + value, Error + message, Disabled, Read only. For Search, Error and Read only are deliberately N/A.
- Three open popup comparisons, with helper text and reserved overlay area.
- Four specialization/migration samples: Textarea, Rich Text Editor, Number Input, Date Picker.

### Required follow-up checks

1. Verify actual Select defaults and instance variant override preservation before reducing `Filled` variants.
2. Compare Error + Focus and readonly behavior for Select and Autocomplete at Small/Medium/Large; preserve focus ring.
3. Verify popup behavior with Helper and Error (open, closed, flipped above, keyboard and screen reader), not just static visuals.
4. Verify Latin/Persian bidirectional values, long options, truncation, dynamic text height and RTL leading/trailing affordances.
5. Audit Angular/Storybook once the owning runtime source is identified; document actual public API rather than inferring it from Figma.
6. Follow up as separate pilots on Number Input and Date/Time Picker; do not turn legacy migration into a silent broad redesign.

## Owner decisions to confirm

- FF-01: whether reducing Select's `Filled` axis is worth a migration and how override preservation will be tested.
- FF-02: whether Warning is field-owned, or a cross-form/status pattern, and how Error focus is represented.
- FF-05: whether to change default Select size on existing sets now or with explicit downstream migration.
- FF-08: popup Helper/Error visibility and stacking/accessibility contract on runtime.
