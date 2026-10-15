---
id: design-system.component.progress-bar
collection: design-system
type: component
title: Progress Bar
summary: A continuous operation-progress component with real determinate values and explicit success/error feedback; Indeterminate is specified semantically but pending in the public Figma parent.
knowledge_state: verified
document_maturity: final
design_status: ready-for-dev
design_maturity: handoff-ready
status: reviewed
owner: Design System team
last_reviewed: '2026-10-15'
related:
  - design-system.component.progress-indicator
  - design-system.pattern.loading-and-progress
  - content.pattern.loading-and-progress
  - design-system.accessibility.dynamic-content-and-feedback
  - design-system.reference.component-mapping
topics:
  - progress
  - progress-bar
  - determinate
  - indeterminate
  - feedback
  - accessibility
  - rtl
---

# Progress Bar

> **Document status: Final — HOS-37.** The current **Determinate / Success / Error** visual and semantic contract is ready for development handoff. **Indeterminate is part of the documented intended behavior, but exposing it in the public Figma component remains TBD.** "Final" applies to this documentation, not to finished runtime code, visual implementation of the deferred state, or tested accessibility.

## Purpose

Progress Bar shows the advancement of an identifiable **continuous, asynchronous operation**. It helps users understand either the reliable completed proportion or the fact that processing is still underway.

Use cases include uploading a resume, processing applications in a batch, or preparing a report.

### Component boundaries

| Need | Use | Why |
| --- | --- | --- |
| Known completed proportion of one operation | **Progress Bar — Determinate** | Actual completed amount can be compared to a total |
| Operation ongoing; completed proportion unknown | **Progress Bar — Indeterminate** (parent Figma **TBD**) or an appropriate Loading pattern | No trustworthy percentage exists |
| Current position in a known sequence of workflow steps | **Progress Indicator / Stepper** | Represents ordered workflow states, not a continuous proportion |
| Short/local busy feedback without meaningful linear operation progress | **Loading / Spinner pattern** | An inline or localized busy indicator is sufficient |
| Historical sequence of events | **Timeline** | Describes what occurred and when |
| Capacity, static KPI, score, confidence, or rating | **Not Progress Bar** | Not progress through an ongoing operation |

Do not invent a fixed time threshold for choosing a Spinner versus a Progress Bar. The amount of useful progress/context, not a universal duration, drives the choice. The broader Design System Loading pattern remains scaffold/unverified; do not invent its specific runtime behavior.

## Modes and status semantics

Mode describes **knowledge of progression**. Outcome describes **what happened to the operation**. These are conceptual concerns; Figma's existing `State` / `Progress` axes are not a runtime API.

### Determinate — supported in the public Figma component

- Render measured advancement based on a real total and a real completed value.
- A determinate runtime control must accept **arbitrary valid numeric progress**, not only the illustrated percentages in Figma.
- Conceptually, when `max > min`, normalized proportion is `(value - min) / (max - min)`. Render it within 0–100% of the visual track.
- The default conceptual percentage domain may be 0–100. A product using other units (count or bytes) must provide a valid min/max/value relationship.
- For missing, invalid, or unreliable values, do **not** display a fabricated percentage. Use an indeterminate/busy presentation when that is the true state; do not silently treat unknown as 0%.
- Visible numeric progress text is **optional** and must be based on the same true source as the fill. Do not show a visual percentage that disagrees with the fill.
- A long-running action may remain determinate even when its measured progress is temporarily unchanged. Do not fake incremental advancement to reassure users.

**Figma authoring limitation:** The public parent currently offers only `0%`, `25%`, `50%`, and `75%` visual `Progress` choices for Active. Its text properties provide Label/Helper/Success/Error copy, but **no public numeric Value text property**. This Figma authoring limitation is **not** a runtime requirement. Arbitrary-percentage authoring in Figma is deferred; developers should implement real data-driven progress.

### Indeterminate — documented behavior; public Figma **TBD**

Use Indeterminate when an operation is active but its completed proportion, remaining work, or ETA **cannot be measured reliably**.

**Required contract:**

- Communicate ongoing activity, **not how much work is complete**.
- Do **not** show a numeric percentage, completed/total count, guessed step, or invented time remaining.
- Give the user enough context to identify the action and object, for example «در حال آماده‌سازی گزارش…».
- An animated moving segment can reinforce busy feedback, but its motion must not be interpreted as measured progress or a promise of completion.
- When reduced-motion preferences are active, preserve the busy meaning using readable status text without motion-dependent information.
- Switch to Determinate only when trustworthy values become available. Switch to Success/Error only after the operation actually reaches that outcome.

**Figma status (2026-10-15):**

- `_Progress bar track item` already has `Progress=Indeterminate` in **Small 4px** and **Big 8px**.
- **The public parent `Progress bar` does not contain an Indeterminate variant** or a complete parent composition exposing this state.
- **TBD — Figma (deferred by design decision):** expose Indeterminate on the public parent using the existing Track source, retaining the original master identities; ensure appropriate Label/Helper composition and **no numeric value**.
- **TBD — Figma QA:** validate both sizes, applicable alignments, RTL, long/mixed-script labels, text visibility, and representation of the moving segment.
- **This documentation finalization does not authorize or make any Figma changes.**

### Terminal outcomes — currently represented in Figma

| Outcome | Meaning | Representation |
| --- | --- | --- |
| `Success` | Operation is **confirmed completed successfully** | Success color/icon and meaningful text; not a guessed 100% |
| `Error` | Operation **failed** | Error color/icon and meaningful description or recovery guidance when supported |
| `Cancelled` | Operation was **actually cancelled** | Product-level status; **no current Progress Bar Figma state** — do not invent a visual variant |

The current Error and Success foreground fills are full-width status treatments, **not literal determinate values**. Do not announce Error as 100% completion. On a runtime transition to an outcome, communicate the outcome explicitly; avoid leaving an indefinite “processing” message visible.

## Current Figma implementation — verified source

Figma: [Progress bar / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23867-126381)

| Source | Verified identifier |
| --- | --- |
| File | `[DS] Job Vision NEXT` — `rROD8ctH9UfPGAMrRrOzHe` |
| Page | `Progress bar` — `8930:400384` |
| **Public component set** | `Progress bar` — node `12603:272925`; component key `1d9983588bb228a44ca2b3af89195bd1e2b51c9d` |
| **Nested track set** | `_Progress bar track item` — node `12603:273022`; component key `b765a10f45d8d3ad69489a266bc6e623ba94d5b1` |
| Presentation | `Progress bar / Documentation` — node `23867:126381`, 1600px shared presentation system |

The Figma source has **20 public variants** and **14 nested Track variants**. The presentation includes source-connected instances, not replacement master component sets. Source keys establish design identity; they do not prove library publication, Code Connect, or implementation.

### Actual authoring properties

| Component | Property | Existing values/type |
| --- | --- | --- |
| Parent | `Size` | `Small` (4px), `Big` (8px) |
| Parent | `Alignment` | `Default`, `Inline`, `Indent` |
| Parent | `State` | `Active`, `Success`, `Error` |
| Parent | `Progress` | `0%`, `25%`, `50%`, `75%`, `Success`, `Error` |
| Parent | Text | `Label text`, `Helper text`, `Success text`, `Error text` |
| Nested Track | `Size` | `Small` (4px), `Big` (8px) |
| Nested Track | `Progress` | `0%`, `25%`, `50%`, `75%`, `Success`, `Error`, `Indeterminate` |

**Do not assume a full Cartesian variant matrix.** In particular, `State`, `Progress`, `Alignment`, and `Size` have only the 20 authored parent combinations. There is no separate `Indeterminate`, `Value`, `Show helper`, or `RTL` parent property. Hide any unneeded copy through supported instance authoring/layer visibility rather than assuming a Boolean property exists.

### Anatomy

```text
Progress bar (public)
├── Label (+ status icon on outcome variants)
├── _Progress bar track item (nested)
│   ├── Neutral Track stroke
│   └── Progress Fill segments (when applicable)
└── Helper / Success message / Error message
```

`Default` places text around the bar; `Inline` uses a horizontal arrangement; `Indent` is another documented authoring arrangement. These are **layout choices**, not operation modes. Preserve the existing layout semantics in implementation only where the product uses them.

### Visual and token contract

| Role | Token / approved treatment |
| --- | --- |
| Track background | `line/default` bound to **Stroke**, `STROKE_COLOR` scope |
| Track construction | **Inside bottom Stroke** with weight **4px Small / 8px Big**; no Track background Fill |
| Active Fill | `surface/accent-emphasis` |
| Success Fill/icon | `fg/success` |
| Error Fill/icon/text | `fg/error` |
| Label | `fg/primary` |
| Ordinary helper | `fg/secondary` |

The original track has **square ends** in the current master. Do not introduce Full/Pill radii as part of this documentation update. Respect the current typography and sizing found in the owning Figma source; no independent component-specific color tokens are required.

## Content and status text

Content rules belong to [Loading and Progress Content](../../content/patterns/loading-and-progress.md); use its writing rules and machine-readable evaluation where relevant.

- If text is needed, name the operation and object: «در حال بارگذاری رزومه…», not just «لطفاً منتظر بمانید».
- For Determinate, show a percentage/count **only** when verified: «در حال پردازش ۱۸ درخواست از ۳۶ درخواست».
- For Indeterminate, do not invent numbers, timing, or proximity to completion.
- Do not use Success or Error copy until the result is known.
- Only present Cancel, Retry, background continuation, or completion notification when the product supports it.
- Prefer concise helper text with no duplicate status announcement.

## RTL and localization

- Progress Bar belongs to an RTL product context; **0% starts at the logical start (right in RTL)** and a larger determinate value extends toward the left. Do not reverse the **numeric** meaning of progress.
- Label and Helper should align for Persian reading; percentages and mixed Latin/Persian strings must remain readable with correct bidirectional isolation where applicable.
- Match the value text to the localized units and numerals chosen by the product's localization rules. Never hard-code progress values into the layout.
- Figma has **no separate RTL variant**, so QA RTL on real instances and runtime logical properties instead of creating new directional Cartesian axes.

## Motion and interaction

This component is **passive and not keyboard-interactive**. It has no Hover, Pressed, Focus or Disabled operation state.

- Determinate fill transitions must reflect **real progress value changes**, not an independent timer.
- Indeterminate may use a visibly moving segment on a stationary track. The exact timing, curve, and mechanics are **runtime-owned and unverified**.
- When `prefers-reduced-motion: reduce` is active, disable nonessential looping motion and convey the busy state via text/semantics.
- Do not move keyboard focus merely because progress starts or stops.
- The source does not define cancellation or other controls inside the Progress Bar; any action is product-owned.

## Accessibility — required implementation behavior

Use semantic progress exposure appropriate to the measured/unknown status. Because this is not yet tested against a registered runtime source, all items here are **requirements**, not claims of implementation.

| Case | Accessible contract |
| --- | --- |
| Name | Provide an accessible name identifying the action/object; use visible text via `aria-labelledby` where suitable |
| Determinate | Expose `role="progressbar"` or equivalent native semantics, valid `aria-valuemin`, `aria-valuemax`, and measured `aria-valuenow` |
| Unit-heavy values | If numbers alone are unclear, provide true descriptive `aria-valuetext` or associated text; never fabricate a percentage |
| Indeterminate | Expose a named progress indication **without `aria-valuenow`**; do not substitute 0 or a fake value |
| Busy region | Use `aria-busy` for the affected region only when appropriate; do not apply it indiscriminately to the entire application |
| Success / Error | Announce important terminal status without moving focus; color or icon must not be the only indicator |
| Noise | Avoid live-region announcements for every tiny increment; announce meaningful transitions/milestones without duplicate competing live regions |
| Motion | Busy meaning and outcome must remain clear with reduced motion and without relying on animation |
| Focus | No additional Tab stop for a passive progress display |

Follow the canonical [Dynamic Content and Feedback](../accessibility/dynamic-content-and-feedback.md) requirements for status-announcement strategy. Preserve ordinary reading order and announce outcomes with the least interruptive sufficient mechanism. UI/assistive-technology verification is a development acceptance requirement.

## Acceptance plan — Storybook bypass

| Test | Acceptance condition | Verification status |
| --- | --- | --- |
| Public Figma variants | 20 original parent variants, same master ID | **Verified in Figma** |
| Nested Figma variants | 14 original Track variants, including Indeterminate Small/Big | **Verified in Figma** |
| Track semantic token / Scope | `line/default` on inside Stroke; 4/8px; no Track background Fill | **Verified in Figma** |
| Visual presentation | Shared 1600px documentation layout with linked matrix and RTL Playground | **Verified in Figma** |
| Status appearance | Active, Success and Error render with semantic color and supporting text | **Verified in Figma** |
| RTL sample | Representative Persian content and orientation shown | **Verified in Figma** (design only) |
| Numeric dynamic progress | Any validated numeric value maps to matching fill/value semantics; not limited to fixed Figma percentages | **Required in development** |
| Determinate edge cases | 0%, intermediate, 100%, missing total/invalid input handled truthfully | **Required in development** |
| Indeterminate behavior | No numeric value, named busy state, sensible motion/reduced-motion fallback | **Specified; runtime verification required** |
| Parent Figma Indeterminate | Public component exposes nested Indeterminate without changing canonical source identity | **TBD — Figma** |
| Parent Figma Indeterminate QA | Both sizes, supported layouts, RTL and status copy | **TBD — Figma** |
| Screen-reader semantics | Accurate determinate/unknown progress; terminal states announced; no update spam | **Required in development** |
| Responsive composition | Long Persian/mixed-script labels stay readable, no unacceptable overlap/clipping | **Required in development** |
| Runtime/Storybook | Owning Angular API, tests and Storybook link | **Unregistered / bypassed for design handoff** |

Storybook is **not a prerequisite for the current design handoff**. Product runtime QA, browser and assistive-technology tests remain development responsibilities; they must not be represented as already passing.

## Deferred work and explicit TBDs

1. **TBD — Figma Indeterminate:** Add Indeterminate to the public `Progress bar` without replacing the existing canonical masters; reuse the nested track. Confirm what Parent `Progress`/State properties should expose before creating combinations.
2. **TBD — Figma Indeterminate QA:** Size, layout, RTL, no percentage, Label/Helper, and any visible motion sample.
3. **TBD — Figma value authoring:** Decide whether/how designers should author intermediate numeric values beyond the four fixed illustrative variants. Runtime **must not** be restricted to them.
4. **Runtime verification:** Define exact Angular inputs, DOM layout, motion timing, reduced-motion fallback and screen-reader outputs when implementation exists. Register the owning repository/Storybook identity later.

These are **tracked implementation/authoring gaps**, not missing definitions of Indeterminate meaning or permission to claim the feature currently exists in the parent Figma component.

## Sources and handoff status

- Figma [canonical Progress Bar presentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23867-126381) — editable design source.
- [Design-to-Code Component Mapping](../integrations/component-mapping.md) — verified design identity, pending runtime mapping.
- [Progress Indicator](progress-indicator.md) — discrete workflow boundary.
- [Loading and Progress Content](../../content/patterns/loading-and-progress.md) — canonical content constraints.
- [Dynamic Content and Feedback](../accessibility/dynamic-content-and-feedback.md) — accessible status requirements.
- HOS-37: https://linear.app/hossein-mor/issue/HOS-37/pilot-progress-bar-component-across-figma-and-design-system-knowledge

**Handoff status:** Documentation **final**; existing Figma visual scope **ready for development**; public-parent Indeterminate **deferred/TBD**; runtime source/API, implementation and test results **unverified**. No additional Figma edits were made to finalize this documentation.
