---
id: design-system.component.file-uploader
collection: design-system
type: component
title: File Uploader
summary: Carbon-derived file selection and drag-and-drop component with composable file list and file-level states.
knowledge_state: draft
document_maturity: draft
design_status: review-ready
design_maturity: figma-source-reconciled
owner: Design System team
last_reviewed: '2026-10-17'
related:
  - design-system.component.progress-bar
  - design-system.reference.component-mapping
  - design-system.accessibility.dynamic-content-and-feedback
  - content.pattern.loading-and-progress
  - content.pattern.errors
topics:
  - file-uploader
  - file-item
  - dropzone
  - upload
  - rtl
  - accessibility
  - validation
---

# File Uploader

> **HOS-39 — Carbon Figma source is canonical for design authoring.** The editable component and presentation have been standardized; this is **not yet a development/runtime acceptance**. The former experimental HOS-39 pilot is retained in Archive as a noncanonical exploration. All runtime props/endpoints, network transfer, retry/cancel and accessibility implementation claims remain unregistered or unverified.

## Purpose

Use **File Uploader** for selecting one or more files, optionally by dragging into the drop target, and displaying selected-file feedback. Do not use it for passive attachments with no selection/transfer workflow. Image/avatar crop or preview is a separate product pattern.

The root component coordinates the entry control and visible list. Its nested **File Item** owns one file's name and presentational status. The Dropzone is the drag-target treatment, not a second parallel uploader API. Progress semantics, persistent errors and network handling remain product/runtime concerns.

## Canonical Figma sources — verified October 17, 2026

| Role | Original preserved node | Contract visible in Figma |
| --- | --- | --- |
| 1600px documentation | `24020:785` | Actual sources, Playground, Anatomy, handoff |
| Public `File uploader` Component Set | `5465:294860` | **15 variants:** Type × Size × supported State |
| Internal `_File uploader file item` Component Set | `3199:35182` | **18 variants:** Size × File Item State |
| Internal `_File uploader - Drag and drop box states` Component Set | `3183:29103` | **4 states** |
| Internal `_File uploader file list item` Component | `4188:102462` | **1 native `File list` Slot** containing 3 real File Item instances |
| Source Slot | `24003:831` | Editable, variable count, Auto Layout Hug |
| Exploratory HOS-39 pilot | `23907:394` | **Archived / not canonical**, do not use its API in place of Carbon |

[Open File Uploader / Documentation (Carbon canonical)](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24020-785)

The original Carbon master/node identities, instance connections, tokens and each component variant are preserved. The public and nested masters were **reparented** to the documentation frame, not recreated. Their variant children were laid out into compact grids for inspection without changing the variant contracts. The old IBM documentation frames remain in Archive for link compatibility; the previous experimental pilot has also been archived.

### Public Figma authoring properties

| Property | Type | Observed options / purpose |
| --- | --- | --- |
| `Type` | Variant | `Default`, `Drag and drop` |
| `Size` | Variant | `Large`, `Medium`, `Small` |
| `State` | Variant | `Enabled`, `Disabled`; `Skeleton` only for `Drag and drop` |
| `Label text` | Text | Field label |
| `Desc. text` | Text | Help/constraints copy; requires real product rules |
| `Files` | Boolean | Show or hide nested File List |

This is the **actual Carbon property model**. It intentionally differs from the abandoned single-size experimental pilot. Do not infer a `Mode` or separate public `Dropzone State` prop from the archived pilot.

### Original internal sources

**File Item** exposes Size (Large/Medium/Small), states `Uploaded`, `Loading`, `Success`, `Focus`, `Error short`, `Error long`, and text properties `File name`, `Short desc.`, `Long desc.`. The short/long error names are presentational legacy states, not proof of separate business errors. Exactly which state means selected, uploading, persisted success, validation failure or transfer failure must be reconciled with product/runtime before implementation.

**Dropzone** source has `Enabled`, `Drag + Hover`, `Focus` and `Disabled`. These are original Carbon visuals, **not** the six states of the archived pilot. Whether the whole target is clickable, and whether drag validation/reject feedback is possible, remain runtime decisions.

**File List** now owns only **one native Slot** named `File list`; the original three uploaded-file Item instances have been moved inside it and the four previously hidden extra items removed. Every consuming enabled parent still shows the corresponding Large/Medium/Small File Item style. The list uses Hug height: **Large 160px, Medium 136px, Small 112px** with three items and an 8px gap. Designers can keep, delete, replace or append File Item instances for a specific scenario. The **three items are authoring examples**, never preselected user data at runtime.

## Composition and intended use

- **Browse only:** the `Type=Default` entry provides a visible file-selection button and may show the File List via `Files`.
- **Drag and drop:** the `Type=Drag and drop` entry displays the Carbon drop target. Users must also have a keyboard/touch-accessible file picker; do not make dragging mandatory.
- **One file:** use a parent Uploader instance and retain one Item in the nested Slot.
- **Several files:** add individual Items to the Slot. Each file can have independent state and error copy; no special file-count variant is needed.
- **Disabled:** original disabled source removes access to selection; the current visual hides File List. Product decisions about existing files and whether Remove remains available are not specified by this visual.
- **File validation error:** attach information about an affected file to its File Item. A batch-wide failure can use appropriate field-level feedback when owned by a product requirement.
- **Responsive / RTL:** RTL content should read naturally in Persian and preserve file extensions. The Carbon source uses 288px specimen widths; a dynamic Fill Container runtime behavior has **not** been verified and must not be assumed.

### Source-linked Figma QA examples

Playground demonstrates: (1) browse with one file, (2) drag-and-drop with three files, (3) Persian file-level validation error, (4) disabled selection. All are live instances of the **original public Carbon variants**, not detached copies. They establish Figma authoring and layout coverage, not end-to-end working upload behavior.

## Copy and error ownership

- **Constraints:** the old Carbon helper `Max file size is 500kb. Supported file types are .jpg and .png.` remains visible in the preserved original source. It is **legacy sample copy**, not a JobVision limit or approved product rule. Before product use, set `Desc. text` from verified constraints and the Content System.
- Explain the known problem and feasible recovery; do not promise supported types/sizes or a retry that the product cannot perform.
- Keep `File Item` errors about individual files separate from transfer failures affecting the whole uploader.
- Filename truncation, duplicate files, maximum count, replacement after single selection and whether a failed upload can be retried are **product/runtime decisions**, not guaranteed by Carbon visual state names.

## Accessibility and runtime contract — requirements, not executed tests

- Use a native, correctly labeled file input or a fully accessible trigger; keep keyboard/touch Browse regardless of optional drag-and-drop.
- Associate true format/size/count constraints and actionable errors with the input; `accept` is only a file-picker hint and does not replace server validation.
- Give each Remove/Retry/Cancel control a file-specific accessible label where supported; never show an inert action.
- Announce selection, completion, failure and removal appropriately; avoid spamming status updates.
- If progress is implemented, use genuine measured values for a determinate Progress Bar or a correctly named indeterminate indicator; Carbon `Loading` visuals do not establish actual transfer progress.
- Preserve focus predictably when file items are removed, test RTL/LTR long filenames, 320–360px layouts and zoomed views.

## Finalization status and follow-up

**Verified in Figma:** canonical original Carbon master in Section 01; all original reusable internal masters in Section 03; 15 / 18 / 4 original variants retained; one native File List Slot with exactly three existing items; 4 connected Playground scenarios; 1600px standard _Docs presentation; source layout and page-link reconciliation.

**Not verified or approved:** product-specific type/size/count rules, actual network upload, cancel/retry/replace, whether Carbon error variants map cleanly onto business statuses, exact responsive production behavior, assistive-technology/runtime QA, Storybook/code mapping, and whether older helper/drag copy meets current Product Content standards. Those are blockers for declaring **ready for development**, not blockers for adopting the Carbon source as the current Figma authoring reference.

The previously discussed Uploading Cancel, Tertiary/XS Retry, six-state Dropzone with Drag-reject, 176px/12px size and Illustration TBD **belong to the archived experimental pilot only**. They have **not** been retroactively applied to the original Carbon component. Transfer those decisions only through an explicit scope/owner review.

**Design System Knowledge remains a Draft PR until owner approves the functional contract**. Do not represent completed Figma presentation cleanup as verified runtime behavior.
