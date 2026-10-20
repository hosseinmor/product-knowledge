---
id: design-system.audit.autocomplete-token-compliance-2026-10-20
collection: design-system
type: audit
title: Autocomplete Token Compliance — 2026-10-20
summary: Canonical Autocomplete source and shared Selection Panel inheritance pass token audit without component edits.
knowledge_state: verified
document_maturity: reviewed
design_status: figma-source-token-qa-complete
owner: Design System team
last_reviewed: '2026-10-20'
related:
  - design-system.component.autocomplete
  - design-system.component.select
  - design-system.reference.figma-token-compliance
---

# Autocomplete Token Compliance — 2026-10-20

Figma source: [Autocomplete / Single](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23861-24), page `23859:9`. **Component Set ID:** `23861:24`; **stable key:** `f87299126ca49639cfbc021a3ac112eb0664a320`. This report checks the **24 existing canonical variants** (3 Sizes × 8 States) and the three real linked Autocomplete examples in the presentation page. It explicitly excludes legacy/scratch frames and treats borrowed nested instances as belonging to their upstream source, not as new Autocomplete-owned styling decisions.

## Result: no Autocomplete-source rebinds needed

The current Autocomplete master already meets the active shared token-binding contract.

| Check | Canonical source result |
|---|---:|
| Public variants (Size Small/Medium/Large × 8 States) | **24/24** retained |
| Effective nonzero Auto Layout Spacing properties | **96/96** bound to Spacing |
| Owned TEXT layers | **48/48** bound to Text Styles |
| Owned positive Radius properties | **48/48** bound to `6px · Medium` |
| Owned visible SOLID paint/stroke instances | **120/120** bound to public `03 Semantic` |
| Owned raw Color, unsupported Color collection or deprecated Radius | **0** |
| Borrowed nested Selection Panel instances | **24/24** top-left Radius `12px · Large` |
| Source mutations made during this audit | **0** |

The `12px · Large` panel inheritance is already repaired upstream by the canonical **Selection Panel** source migration under the same branch; **no independent 12px raw radius remains to fix in Autocomplete**. This reuse is desirable: do not duplicate the panel or create Autocomplete-specific surface/radius tokens.

## State and behavior-role validation

Inspected all eight existing states in Small/Medium/Large. Input Control heights remain **32/40/48px** and the canonical Border/Focus mapping is:

| State | Border | Focus Style |
|---|---|---|
| Default | `line/default`, 1px | None |
| Hover | `line/emphasis`, 1px | None |
| Focus | `line/emphasis`, 1px | `Focus/Default` |
| Error | `line/error`, 2px | None |
| Error focus | `line/error`, 2px | `Focus/Default` |
| Disabled | `line/disabled`, 1px | None |
| Read only | `line/muted`, 1px | None |
| Read only focus | `line/muted`, 1px | `Focus/Default` |

All 24 match this intended state contract; the 3 Error focus variants have their shared **Error** helper visible with a text property, and Read only focus does not artificially use Disabled styling. All 24 embed the standard **Selection Panel / Open** component with `Selection=Single`, `Filterable=False` and the existing options Slot; those nested components were not detached or regenerated. The Panel is hidden in the default master state and is controlled in consumer instances via **Open**, so a canvas scan must not mistake `visible=false` for broken composition.

## Live presentation samples

The documentation includes three linked **Medium / Focus / Open=true** examples:

| Sample | Instance ID | Observed example |
|---|---|---|
| Job-title free-form | `23867:90` | Typing/committing arbitrary job-title string and candidate suggestions |
| City selection-required | `23868:1991` | City query with suggestions/committed label |
| Job Group selection-required | `23868:2187` | Job-group candidates and optional chevron |

Screenshots show a correctly anchored open Selection Panel, stable RTL right-alignment and real Persian suggestions for all three presentations. Focus Error (Medium) and Read only focus (Medium) were also sampled; error border and helper are rendered while component radius/layout remain stable.

**Screenshot caveat:** the existing shared `Focus/Default` Effect Style is attached to the input Control in Focus, Error focus and Read only focus, but the Figma screenshot renderer may omit its outside shadow-ring. This is the same known renderer limitation seen in Text Input / File Uploader. Validate focus ring in the actual Figma editor and runtime keyboard navigation before declaring accessible focus QA complete.

## Implementation and acceptance boundary

The visual token audit does **not** prove the Sandbox/Angular editable combobox behavior. Requirements already recorded in `components/autocomplete.md` and `handoffs/select-autocomplete-sandbox.md` remain binding:

- Preserve **free-form** versus **selection-required** commit/revert policy, and separate query text, active suggestion, and committed ID.
- Confirm ArrowUp/Down, Enter, Escape, Tab, IME text input, RTL and mixed-script caret behavior; no Form submit on invalid selection-required Enter.
- Validate popup placement under scroll/zoom and short viewport, asynchronous loading/error/empty result states, long suggestion content, and accessible listbox/active-descendant announcements.
- Check actual JobVision/Cando × Light/Dark and real focus-ring rendering. The source binding scan does not certify browser contrasts.
- Check published instance overrides/Slots after the shared upstream Selection Panel migration. No source changes were made in this Autocomplete audit.

**Status:** Figma source **Color, Spacing, Typography and Radius binding QA passes**. No node, variable, master ID, component property, or variant was modified here. Runtime/consumer QA remains separate.

**Scope exclusion:** Image Uploader is explicitly excluded and untouched.
