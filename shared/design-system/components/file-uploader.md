---
id: design-system.component.file-uploader
collection: design-system
type: component
title: File Uploader
summary: Composable browse and drag-and-drop file selection with per-file upload status, validation and feedback.
knowledge_state: draft
document_maturity: draft
design_status: in-progress
design_maturity: pilot
owner: Design System team
last_reviewed: '2026-10-17'
related:
  - design-system.component.progress-bar
  - design-system.reference.component-mapping
  - design-system.accessibility.dynamic-content-and-feedback
  - content.pattern.loading-and-progress
topics:
  - file-uploader
  - file-item
  - dropzone
  - upload
  - validation
  - accessibility
  - rtl
---

# File Uploader

> **HOS-39 draft — not approved for development handoff.** The new Figma pilot is a proposed authoring model. Original Carbon-era File Uploader and Image Uploader masters remain intact until migration and behavioral boundaries are approved. Code/Storybook sources are not registered; do not infer runtime props, endpoints, transfer or storage mechanics.

## Purpose and boundaries

File Uploader enables users to select one or more files for an upload workflow, learn actual file requirements, monitor per-file outcome, and recover from errors. A browse action is a first-class path; drag and drop is optional enhancement.

| Need | Owner / pattern |
| --- | --- |
| Browse files, drag/drop entry, selection rules, list of file transfers | **File Uploader** (composite) |
| Drag target and drag-over feedback | **Dropzone** (nested target, not an independent uploader API) |
| One file's name, metadata, state and recovery actions | **File Item** (reusable within uploader) |
| Determinate/indeterminate operation progress | Shared **Progress Bar**; file item composes the track/indicator |
| Uploader-level persistent failure / global instruction | Shared **Inline Notification** when semantically appropriate |
| Passive downloadable attachment with no transfer workflow | A separate **Attachment** / file-list pattern, not File Uploader |
| Image crop/preview or avatar media workflow | Product-specific image upload pattern; current legacy image uploader is not automatically a File Uploader variant |

Do not put a multi-file uploader in a constrained modal unless the list remains fully usable. Do not require drag-and-drop as the only input.

## Authoring model — proposal

- Public pilot master: `File Uploader / HOS-39 Pilot`.
- `Mode`: **Browse / Dropzone**. Both must support the native file picker.
- `State`: **Enabled / Disabled**; disabled blocks new selection. The label, instruction and entry control all use explicit disabled semantic tokens, never hand-applied alpha. Existing uploaded content does not necessarily become disabled: its action policy belongs to the product.
- **Label** and **Helper**: TEXT properties. Helper must describe *actual*, enforced format, size and count limits; never copy the placeholder limits blindly.
- **File list / Slot**: a Figma native Slot. Compose zero, one, or multiple `File Item` instances; **file count is not a visual variant axis**.
- **Single vs multiple** is a selection/business-behavior setting, not a size variant. Single-file designs may replace/remove then browse again. When a single-file selection is complete, retaining or suppressing the trigger depends on the flow; examples should not imply a universal rule.
- **Sizing**: **No `Size` variant axis** in File Uploader, Dropzone or File Item. Preserve the former Medium spec as the only default: Tertiary Browse Button **40px**, File Item base row **40px** (content-driven taller when progress/error is present), Dropzone **192px** with **12px Large radius**. Dropzone width follows its container; runtime should allow its minimum content height to grow when text wraps. `Size` is not a runtime or Figma authoring choice.
- **RTL**: name, file status and metadata align to the right; primary file actions occupy the left side. Do not force RTL ordering on the English Figma documentation scaffold.

### Figma pilot identities (verified 2026-10-17)

| Asset | Node ID | Variant axes / count |
| --- | --- | --- |
| Presentation | `23907:394` | 1600px; Header, Component set, Playground, Anatomy, Handoff |
| File Uploader | `23905:614` | Mode × State; **4 variants**; one shared File list Slot; no Size axis |
| File Item | `23903:127017` | Status; **5 variants**; editable File name and Error message; 40px base row |
| Dropzone | `23905:565` | State; **5 variants** (Default / Hover / Drag-over / Focus / Disabled); editable Instruction; 192px / 12px radius |
| Existing legacy File Uploader | `5465:294860` | 18 legacy variants; preserved, not migrated |
| Existing image uploader | `19337:1420` | Image-specific legacy; preserved |

[View the pilot in Figma](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23907-394)

The refactored File Item keeps Carbon's compact neutral-filled row, separates error text as expandable content, uses shared Ghost **Icon Button** for Remove, shared labeled Button for Retry, and composes an instance of the shared Progress Bar track for its illustrative 50% state. Figma's 50% progress is a static specimen, not an automatically measured transfer. Public Figma component keys and published-library status are pending verification. Runtime API and Storybook remain **unregistered/unverified**.

### Dropzone size and shape — single-size decision (2026-10-17)

The Drag & Drop target is a large, distinct interaction area, not another 40px input. It uses the existing **`12px · Large`** foundation radius; nested Button and File Item retain **6px · Medium**.

**One default:** Dropzone **192px**, Tertiary Browse Button **40px**, File Item **40px minimum/base row** (height grows for file progress and error). The Figma source measures 480px wide as an illustration; use responsive width and content-aware height in actual layouts. There is no Small/Medium/Large toggle and no Size property on the three component sets.

The original 3-size pilot (Small 160, Medium 192, Large 224) was consolidated to the former Medium size because no distinct product use cases justified the variant matrix. This **does not establish Carbon or Polaris product-size specifications**.

**Benchmarks:** [Carbon File Uploader](https://www.carbondesignsystem.com/building-blocks/core/components/file-uploader/guidelines) specifies button/file-row sizes but does not require a global Dropzone height; [PatternFly multiple file upload](https://www.patternfly.org/components/file-upload/multiple-file-upload/design-guidelines/) and [Polaris Drop Zone](https://polaris-react.shopify.com/components/selection-and-input/drop-zone) support a spacious area relative to content; [GOV.UK File Upload](https://design-system.service.gov.uk/components/file-upload/) recommends an improved larger drop target. **192px is a JV design decision**, not an externally mandated measurement.

Content should remain readable when wrapped and in narrow widths; runtime responsive/focus/drop behavior is still unverified. Nested browse-button vs clickable-full-target policy remains to be decided.

### Button and Dropzone surface contract — owner-directed update (2026-10-17)

The **default file-picker trigger uses the shared `Button / Tertiary`**, at the standard **40px Medium height**, across Browse-only and Dropzone entry and Enabled/Disabled. This is a supporting utility to choose a file, not the page's main Submit/Save action. Avoid using a Brand or Primary Button for routine file selection. A stronger Button style in a particular product context requires product-design review; it is **not** a separate File Uploader variant axis.

| Dropzone State | Background | Border / effect | Meaning |
| --- | --- | --- | --- |
| Default | `surface/default` | Dashed 1px `line/emphasis` | Clear drop target without competing with inputs |
| Hover | **`surface/transparent-hover` overlay over `surface/default`** | Dashed 1px `line/emphasis` | Subtle pointer-hover feedback, no product-colored emphasis |
| Drag-over | `surface/accent-muted` | Solid **2px** `line/accent` | File actively dragged over a valid drop target |
| Focus | `surface/default` | Dashed 1px `line/emphasis` + shared `Focus/Default` effect | Keyboard focus, not equivalent to Drag-over |
| Disabled | `surface/disabled` | Dashed 1px `line/disabled` | Browse and drop are unavailable |

**Hover token semantics:** `surface/transparent-hover` resolves to a translucent neutral overlay (4% black in the verified Light JobVision mode). It must be composited **over** the default surface, not replaced by the opaque `surface/muted` token. Semantic token binding must remain intact for Dark mode and Product routing. Do not introduce a File-Uploader-only Hover color.

`Hover` is a variant of the **nested Dropzone** for design authoring. The parent File Uploader has only the `Mode × State` axes; runtime pointer-hover styling should follow actual pointer events, not become a required application prop. Actual event behavior is not verified by the Figma representation.

## File-item states

| State | Meaning | Proposed feedback / next step |
| --- | --- | --- |
| Selected | File selected, not necessarily committed to network transfer | Filename, type and optional size; remove before upload |
| Uploading | A real transfer is underway | Operation label plus **measured** determinate Progress Bar; unknown progress uses indeterminate without a percentage |
| Uploaded | Server/product confirms a usable uploaded file | Success status and optional remove/replace according to product |
| Validation error | Type, size, count or other selection constraints violated | Specific problem and how to fix it; file cannot be treated as successfully uploaded |
| Upload error | Transfer failed or product could not accept it | Explain recoverable error; retry the same selected file if supported; remove always distinguishable |

`Canceled` is **TBD** pending confirmation that runtime supports canceling an active transfer. Do not portray a failed upload as a successful cancel. Progress, selected, uploaded and error are file-level data; one failure must not silently mark other files as failed.

### Validation and recovery

- Check type, byte size, count and product rules as early as possible during selection/drop. Server must enforce authoritative validation again; `accept` is only a picker hint, not a security gate.
- Keep format, maximum size and maximum file count visible *only when genuinely enforced*.
- Validate a batch per file so good files are not silently lost because one failed. Also communicate aggregate limits or an entire rejected batch when necessary.
- Duplicate handling is product-owned. Draft default: identify duplicates among the same current selection and explain the rejected duplicate, without assuming filename alone is a unique file identity. Re-selection of a file after removal may be legitimate.
- Remove deletes the item from the current uploader selection; whether it also removes a persisted remote object is a separate product/runtime decision.
- Retry applies to recoverable **upload errors** and retains the file context. For validation errors, require a corrected file instead of retrying the same invalid content.
- Replace in a single-file flow should be an explicit, understandable action or a remove + browse sequence. Avoid silently replacing a completed file without signaling the change.
- Do not infer storage, chunking, upload endpoint, virus scanning, cancellation strategy, retry backoff or automatic upload timing from design.

### Filename and metadata

- Always show the identifiable filename, with its extension preserved where feasible.
- Name occupies flexible space and truncates to one visual line when necessary, while status and Remove/Retry remain visible. The source-linked Playground contains a **360px RTL sample** with a very long LTR filename and multiline Persian validation feedback; Figma visual layout passed without clipping. Mixed-script bidirectional isolation and full accessible filename exposure remain runtime QA requirements.
- Full untruncated name remains available to assistive technologies; optional tooltip can supplement visual overflow but must not be the only way to recover the name.
- Optional byte size, file type and progress should not dominate the name or be mistaken for successful upload.

## Accessibility contract — requirements, not implementation claims

- Use a properly labeled native `<input type="file">` or an accessible trigger tied to one. Activate via keyboard using Tab and Enter/Space; provide an obvious focus-visible state.
- Drag-and-drop is supplemental. A user with keyboard, switch access or touch must be able to complete the task without dragging. Do not force a nested button inside a button-like entire drop region; define one unambiguous interaction model.
- Associate field label, actual constraints, and validation messages programmatically with the input. Expose specific file and uploader errors.
- Each file Remove/Retry control requires an accessible name identifying the file (e.g., «حذف رزومه-نهایی.pdf»).
- Use a real, named determinate progressbar with measured value/min/max, or a named indeterminate progress indicator **without fictitious values**.
- Announce new selection, completion, failure and removal in an appropriate polite status/live region. Do not flood screen readers with every byte or every percentage point. Maintain keyboard focus predictably when items disappear.
- Keep file/status relationship understandable in a list; inspect long and mixed RTL/LTR strings, zoom, reduced motion and 360px layouts before handoff.

## Responsive behavior / edge scenarios

- At narrow widths, uploader and drop target fill available width; instructions and buttons remain usable on touch.
- File rows must not crop Remove/Retry or progress; allow deliberate metadata wrapping or truncation rather than fixed-row overflow.
- Recheck focus ring, error association and tooltip clipping on white and nonwhite hosting surfaces.
- Representative QA: zero files, one completed file, three mixed statuses, long Latin filename in Persian UI, invalid file, interrupted upload, disabled input and drag-over.

## Benchmarks consulted

- [Carbon File Uploader](https://www.carbondesignsystem.com/building-blocks/core/components/file-uploader/guidelines) — browse vs drag-and-drop, file-level loading and error.
- [Carbon Accessibility](https://www.carbondesignsystem.com/building-blocks/core/components/file-uploader/accessibility) — keyboard actions and contextual delete naming.
- [Shopify Polaris Drop Zone](https://polaris-react.shopify.com/components/selection-and-input/drop-zone) — pre-upload validation and feedback.
- [GOV.UK File Upload](https://design-system.service.gov.uk/components/file-upload/) — browse-first, type/size errors and improved drop target.
- [W3C WAI ARIA25](https://w3c.github.io/wcag/techniques/aria/ARIA25) — progress updates via live region; status announcement is not automatic just because progressbar value changes.

## Open decisions and implementation gaps

1. Approve Browse vs Dropzone input and whether whole dropzone or only its Browse button is clickable.
2. Decide single-file completed state, replacement action and selection-count limit.
3. Decide upload timing (immediate after selection vs after form submission), cancellation and retry policy from product requirements.
4. Approve the currently implemented **one-line visual truncation** after Figma 360px QA, and verify full-name access and bidirectional text in runtime.
5. Review per-file vs uploader-level errors and persistent feedback.
6. Verify image uploader boundary, then migrate or archive legacy masters without breaking existing consumers.
7. Register runtime/Storybook sources and map actual API names; perform keyboard, assistive-technology and upload-network tests before handoff.

**Figma page cleanup:** the 1600px pilot documentation frame (`23907:394`) now starts at the page origin. Preserved Carbon File Uploader/File Item and the prior Image Uploader live in a separate, visible `Archive — legacy & scratch` frame (`23931:643`). Legacy source sets and their original node IDs remain intact and accessible; no consumer migration or publication cutover was performed.

**Current Figma refactor QA (2026-10-17):** Original legacy masters remain intact. Existing HOS-39 pilot Component Set IDs and all former Medium child Component IDs are preserved: **File Uploader 4 variants** (Mode × State); **Dropzone 5 variants** (State); **File Item 5 variants** (Status). **Size is absent from all three variant APIs**. Uploader retains exactly one shared File list Slot across four variants and Label/Helper props; Dropzone keeps Instruction; File Item keeps File name/Error message. Dropzone uses bound `12px · Large` radius and `192px` specimen height, File Item keeps 6px Medium radius and a 40px base row. All default Browse triggers use 40px Tertiary Button. Semantic state tokens and Focus/Default remain. The 1600px documentation frame still contains source masters; four real linked Playground scenarios include mixed file statuses, 360px long filename, and disabled Dropzone. Figma rendering verifies layout and identity, **not** keyboard, upload, networking, or assistive technology behavior.

**Open visual review:** owner feedback on Carbon-derived compact rows, icon/action placement and error treatment. One Dropzone size (192px base, 12px Large radius) now exists in Figma; responsiveness and runtime interaction remain unverified. Do not replace the public Carbon master or merge the draft without approval.

This document is intentionally **draft** until owner approval, canonical master cutover and runtime integration checks.
