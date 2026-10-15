---
id: design-system.component.progress-bar
collection: design-system
type: component
title: Progress Bar
summary: Continuous progress for asynchronous operations; documents the current Figma component and a proposed indeterminate mode that is not yet exposed on the public parent.
knowledge_state: draft
document_maturity: draft
owner: Design System team
last_reviewed: '2026-10-15'
related:
  - design-system.component.progress-indicator
  - design-system.pattern.loading-and-progress
  - content.pattern.loading-and-progress
  - design-system.accessibility.dynamic-content-and-feedback
  - design-system.reference.component-mapping
---

# Progress Bar

> **Status: draft / HOS-37.** This document records currently verified Figma construction and the agreed semantic requirement for **Indeterminate**. It is **not** a claim that the full component, animation, Storybook, runtime API, or accessibility testing is finished.

## Purpose and boundary

Progress Bar displays the advancement or ongoing activity of **one continuous operation**, such as uploading a resume, processing a batch of applications, or preparing a report.

- Use **Determinate** when measured progress and the total are reliable.
- Use **Indeterminate** when the operation is ongoing but no reliable completion proportion is available.
- Use **Progress Indicator / Stepper** for a known ordered sequence of workflow steps rather than continuous operation progress.
- Use a local Loading/Spinner pattern when a localized action or region needs only brief busy feedback and a linear operation display adds no value. Duration thresholds are not defined here.
- Do not use this component as a static KPI, capacity gauge, or confidence score; those are not operation progress.

For status copy, transitions, truthfulness, and AI-writable content rules, refer to `shared/content/patterns/loading-and-progress.md`.

## Operation modes

### Determinate — current parent Figma coverage

A meaningful completed amount and total are known. A progress bar may show a calculated percentage or other verified completed/total text.

- Progress value must come from actual product data, not a timed animation or an invented estimate.
- Conceptual normalized progress is `(value - min) / (max - min)`; clamp only the visual rendering as appropriate, while product validation owns invalid or missing input data.
- The exact numeric range/value API is **unverified** until the runtime source is registered.
- In Figma, the public parent currently offers only **0%, 25%, 50%, 75%** as illustrative `Progress` variant options; **these are not intended to be a runtime restriction**.
- `Success` and `Error` appear as outcome choices in the existing `Progress` axis alongside separate `State` variants; preserve this existing authoring model until a separate design decision explicitly changes it.

### Indeterminate — design intent agreed; **parent Figma implementation TBD**

**Meaning:** the operation is in progress, but its percentage, completed amount, or time remaining cannot be stated reliably.

**Required semantic behavior:**
- Show that an identifiable operation is ongoing, not how much has been completed.
- **Do not display a numeric percentage, completed/total count, or invented ETA.**
- Name the action and object when context is not sufficiently explicit (for example, «در حال آماده‌سازی گزارش…»).
- A moving segment may communicate ongoing activity, but movement is **not** a representation of measured advancement and does not guarantee completion.
- Success, failure, and cancellation must be represented only after the underlying operation actually enters that state.
- Animation behavior and reduced-motion fallback must be specified and verified during runtime development; do not infer duration or exact animation timing from the Figma sample.

**Figma coverage — 2026-10-15:**
- The nested internal component set `_Progress bar track item` already contains `Progress=Indeterminate` for both `Small` and `Big`.
- The **public parent `Progress bar` does not expose Indeterminate** in its current `Progress` variants.
- **TBD — HOS-37:** expose an Indeterminate option on the public parent, composing its existing label/helper with the nested Indeterminate Track. Preserve the existing master IDs and avoid duplicate public component sources.
- **TBD — Figma QA:** check both sizes, applicable alignments, mixed Persian/English labels, absence of numeric progress, and legible status text. Decide the least complex authoring property model before changing component variants.
- **No Figma update is authorized by this documentation change**; the component is intentionally left as-is for now.

## Current verified Figma authoring model

File: `rROD8ctH9UfPGAMrRrOzHe` — `[DS] Job Vision NEXT`

- Page: `Progress bar`, node `8930:400384`.
- Public parent component set: `Progress bar`, node `12603:272925` — **20 variants**.
- Nested track component set: `_Progress bar track item`, node `12603:273022` — **14 variants**.
- Documentation presentation: `Progress bar / Documentation`, node `23867:126381`; uses the shared 1600px documentation layout and source-connected instances.
- [Open the Figma presentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23867-126381)

| Existing Figma property | Current values / type |
| --- | --- |
| `Size` | `Small` (4px), `Big` (8px) |
| `Alignment` | `Default`, `Inline`, `Indent` |
| `State` | `Active`, `Success`, `Error` |
| `Progress` (parent) | `0%`, `25%`, `50%`, `75%`, `Success`, `Error` |
| Text properties | `Label text`, `Helper text`, `Success text`, `Error text` |
| `Progress` (nested track only) | `0%`, `25%`, `50%`, `75%`, `Success`, `Error`, `Indeterminate` |

The current source is intentionally **not a complete Cartesian expansion** of every axis. Do not infer missing combinations or treat unexposed parent Indeterminate as already shipped.

### Anatomy and visual tokens

- **Track background:** `line/default`, applied as an **inside Stroke** on the nested Track; weight matches 4px or 8px. Keep the token's `STROKE_COLOR` scope; do not expand it to Fill solely for this component.
- **Active fill:** `surface/accent-emphasis`.
- **Success visual:** `fg/success`; **error visual:** `fg/error`.
- **Primary text:** `fg/primary`; **supporting text:** `fg/secondary`; error text uses `fg/error`.
- Preserve current typography and geometry unless separately reviewed.
- The bar's visual reading direction must work in RTL; component layout and source/data semantics must not rely on an assumed physical LTR sequence.

### Outcome and content treatment

- `Success` and `Error` report **confirmed outcomes**, not different progress percentages.
- Communicate outcome through meaningful text and/or accessible state; do not depend on color alone.
- Avoid redundant labels or misleading “almost done” messaging.
- Do not promise background processing, cancellation, notifications, or time remaining unless the owning product feature confirms those capabilities.

## Runtime and accessibility contract — required at implementation, not yet verified

A continuous operation display should have an accessible name identifying the operation and use appropriate progress semantics (for example, `role="progressbar"`).

- **Determinate:** expose meaningful `aria-valuemin`, `aria-valuemax`, and `aria-valuenow` from real progress values; derive intelligible value text if numeric units are not self-explanatory.
- **Indeterminate:** omit `aria-valuenow` rather than reporting a fabricated zero/percentage; provide an accessible operation name and, when needed, separate status context.
- Do not announce every tiny incremental change via an intrusive live region.
- Respect reduced-motion preferences and ensure busy meaning remains understandable without relying on animation.
- Avoid introducing an unnecessary keyboard focus stop for this non-interactive visual indicator.

Exact DOM structure, Angular API, animation implementation, motion timing, status announcements, and screen-reader QA are **unverified**, not existing implementation claims. Storybook is bypassed for the current design-handoff stage.

## Open decisions and acceptance checklist

- [x] Clarify the meaning and copy rules for Determinate vs Indeterminate.
- [x] Verify nested Indeterminate Track variants exist for Small / Big.
- [x] Preserve existing public parent variants and layout for now.
- [x] Reconcile Track background to the stroke-only `line/default` token.
- [x] Rebuild Figma documentation presentation with connected instances.
- [ ] **TBD — Figma:** expose Indeterminate on the public parent, without changing existing source identities.
- [ ] **TBD — Figma:** QA Indeterminate in supported sizes / alignments and RTL, without misleading numeric value.
- [ ] Approve arbitrary numeric progress value authoring/contract beyond the existing fixed Figma visual variants.
- [ ] Define/verify animation and reduced-motion behavior with the runtime owner.
- [ ] Verify accessible progress semantics and status messaging in implemented UI.
- [ ] Register runtime/Storybook source and reconcile Design-to-Code component mapping.
- [ ] Owner review to mark this component documentation final / ready for dev.
