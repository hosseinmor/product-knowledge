---
id: design-system.component.progress-bar
collection: design-system
type: component
title: Progress Bar
summary: Continuous operation-progress component with measured determinate values, public Figma Indeterminate variants, and explicit success/error feedback.
knowledge_state: verified
document_maturity: final
design_status: ready-for-dev
design_maturity: handoff-ready
status: reviewed
owner: Design System team
last_reviewed: '2026-10-17'
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

> **Document status: Final — HOS-37.** The **Determinate / Indeterminate / Success / Error** design contract and corresponding public Figma variants are ready for development handoff. In Figma, Indeterminate is a **static visual reference**, not verified animation. "Final" applies to the documented design contract, not to finished runtime code, production motion, or tested accessibility.

## Purpose

Progress Bar shows the advancement of an identifiable **continuous, asynchronous operation**. It helps users understand either the reliable completed proportion or the fact that processing is still underway.

Use cases include uploading a resume, processing applications in a batch, or preparing a report.

### Component boundaries

| Need | Use | Why |
| --- | --- | --- |
| Known completed proportion of one operation | **Progress Bar — Determinate** | Actual completed amount can be compared to a total |
| Operation ongoing; completed proportion unknown | **Progress Bar — Indeterminate** or an appropriate Loading pattern | No trustworthy percentage exists |
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

**Figma authoring decision (v1, verified 2026-10-17):** Retain the `0%`, `25%`, `50%`, and `75%` design-time `Progress` presets as **illustrative snapshots**; do not create a variant for every possible percentage. Figma's component property model in this file exposes no numeric Value property. Testing direct nested Fill geometry overrides did **not** provide a reliable editable numeric percentage in a component instance. Consequently, the current public component does **not** support exact arbitrary-percentage authoring in Figma. Do not label a 50% visual as “37%” or treat these presets as measured data. A precise one-off illustration needs separate, explicitly non-canonical visual composition and review, not a claimed Progress Bar instance API. **Runtime must accept and render actual validated numeric values, including 1%, 37%, 99% and 100%.** The lack of a numeric Figma property is intentionally **not** a development blocker.

### Indeterminate — implemented as static public Figma variants

Use Indeterminate when an operation is active but its completed proportion, remaining work, or ETA **cannot be measured reliably**.

**Required contract:**

- Communicate ongoing activity, **not how much work is complete**.
- Do **not** show a numeric percentage, completed/total count, guessed step, or invented time remaining.
- Give the user enough context to identify the action and object, for example «در حال آماده‌سازی گزارش…».
- An animated moving segment can reinforce busy feedback, but its motion must not be interpreted as measured progress or a promise of completion.
- When reduced-motion preferences are active, preserve the busy meaning using readable status text without motion-dependent information.
- Switch to Determinate only when trustworthy values become available. Switch to Success/Error only after the operation actually reaches that outcome.

**Figma status (2026-10-15):**

- The nested `_Progress bar track item` retains `Progress=Indeterminate` in **Small 4px** and **Big 8px**; no internal Track master was duplicated.
- The public `Progress bar` now exposes **five** `State=Active, Progress=Indeterminate` variants: `Default/Small`, `Default/Big`, `Inline/Small`, `Inline/Big`, and `Indent/Big`. These match currently supported Active size/alignment combinations; `Indent/Small` was not invented.
- Each Indeterminate master nests its corresponding Track and preserves linked Label/Helper text authoring where present. Indeterminate is a **Progress axis value**, not a separate Mode axis.
- **Verified in Figma:** component links, both sizes, available alignment treatments, RTL/Persian Playground, neutral Track stroke, accent **static segment**, and absence of numeric progress copy. The segment must move appropriately at runtime, not act as a static 25% claim.
- **Runtime QA needed:** actual animation, reduced-motion handling, accessible progress naming/value/announcements, and long/mixed-script responsive behavior.

## Current Figma implementation — verified source

Figma: [Progress bar / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23867-126381)

| Source | Verified identifier |
| --- | --- |
| File | `[DS] Job Vision NEXT` — `rROD8ctH9UfPGAMrRrOzHe` |
| Page | `Progress bar` — `8930:400384` |
| **Public component set** | `Progress bar` — node `12603:272925`; component key `1d9983588bb228a44ca2b3af89195bd1e2b51c9d` |
| **Nested track set** | `_Progress bar track item` — node `12603:273022`; component key `b765a10f45d8d3ad69489a266bc6e623ba94d5b1` |
| Presentation | `Progress bar / Documentation` — node `23867:126381`, 1600px shared presentation system |

The Figma source has **25 public variants** (20 preserved, 5 Indeterminate additions) and **14 nested Track variants**. Under the [Figma Component Presentation Guideline](../integrations/figma-component-presentation.md), the **original public Component Set** (unchanged node ID/key) is physically placed in the presentation's **01 · Component set** section and the **original internal Track Component Set** in **03 · Anatomy & composition**. Both canonical sources retain all their variants, token bindings, and connected instances. Their variants have a more compact two-column *canvas arrangement*, not new APIs or duplicate sources. **02 · Playground** uses actual source-linked instances. Superseded IBM/Carbon documentation artboards and the redundant instance-only visual matrix/anatomy copies were removed. Source keys establish design identity; they do not prove library publication, Code Connect, or implementation.

### Actual authoring properties

| Component | Property | Existing values/type |
| --- | --- | --- |
| Parent | `Size` | `Small` (4px), `Big` (8px) |
| Parent | `Alignment` | `Default`, `Inline`, `Indent` |
| Parent | `State` | `Active`, `Success`, `Error` |
| Parent | `Progress` | `0%`, `25%`, `50%`, `75%`, `Indeterminate`, `Success`, `Error` |
| Parent | Text | `Label text`, `Helper text`, `Success text`, `Error text` |
| Nested Track | `Size` | `Small` (4px), `Big` (8px) |
| Nested Track | `Progress` | `0%`, `25%`, `50%`, `75%`, `Success`, `Error`, `Indeterminate` |

**Do not assume a full Cartesian variant matrix.** In particular, `State`, `Progress`, `Alignment`, and `Size` have only the 25 authored parent combinations. `Indeterminate` is an option of the existing `Progress` axis, not a separate Mode. There is no separate `Value`, `Show helper`, or `RTL` parent property. Hide any unneeded copy through supported instance authoring/layer visibility rather than assuming a Boolean property exists.

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

**Text resilience (Figma-verified 2026-10-17):** Default and Indent parent variants use content-hug vertical sizing with height-autoresizing Label/Helper; longer Persian strings can wrap and increase the component's height without clipping. Inline keeps a compact 20px row; its Label is fixed width and single-line truncated with an ending ellipsis. The presentation Playground includes **real source-linked long-Persian and mixed-script instances** demonstrating both strategies. In runtime, the full operation name must remain available to assistive technology even if visually truncated; do not depend on a tooltip alone for the accessible name.

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
| Public Figma variants | 25 parent variants (20 preserved, 5 new Indeterminate), same component-set ID/key | **Verified in Figma** |
| Nested Figma variants | 14 original Track variants, including Indeterminate Small/Big | **Verified in Figma** |
| Track semantic token / Scope | `line/default` on inside Stroke; 4/8px; no Track background Fill | **Verified in Figma** |
| Visual presentation | One 1600px documentation frame with **original** public Master in 01, original Track Master in 03, and five real RTL Playground instances in 02; no stray legacy artboards | **Verified in Figma** |
| Status appearance | Active, Success and Error render with semantic color and supporting text | **Verified in Figma** |
| RTL sample | Representative Persian content and orientation shown | **Verified in Figma** (design only) |
| Numeric dynamic progress | Any validated numeric value maps to matching fill/value semantics; not limited to fixed Figma percentages | **Required in development** |
| Determinate edge cases | 0%, intermediate, 100%, missing total/invalid input handled truthfully | **Required in development** |
| Indeterminate behavior | No numeric value, named busy state, sensible motion/reduced-motion fallback | **Specified; runtime verification required** |
| Parent Figma Indeterminate | Public `Progress=Indeterminate` includes Default Small/Big, Inline Small/Big, Indent Big; nested Track connected | **Verified in Figma** |
| Parent Figma Indeterminate QA | Both sizes/layouts, Persian RTL and mixed-script truncation samples, no percentage, static segment | **Verified in Figma** (animation still requires runtime QA) |
| Screen-reader semantics | Accurate determinate/unknown progress; terminal states announced; no update spam | **Required in development** |
| Figma overflow composition | Long Persian Label/Helper reflow in Default/Indent; Inline ellipsis stays one line; Playground QA shows unclipped cards | **Verified in Figma** |
| Runtime responsive composition | Long Persian/mixed-script labels remain accessible and readable at actual product widths | **Required in development** |
| Runtime/Storybook | Owning Angular API, tests and Storybook link | **Unregistered / bypassed for design handoff** |

Storybook is **not a prerequisite for the current design handoff**. Product runtime QA, browser and assistive-technology tests remain development responsibilities; they must not be represented as already passing.

## Verified design work and implementation boundary

1. **Done — public Figma:** 25 original/new public variants and 14 nested Track variants; Indeterminate is connected and static in Figma.
2. **Done — size consistency:** Existing `Inline/Big` 0/25/50 variants were fixed to use the correct **8px Big Track**, preserving all original IDs and keys. Every public parent now embeds a nested Track matching its `Size`.
3. **Done — robust text authoring:** Default/Indent instances grow vertically for long Persian text; Inline is fixed 20px height with a one-line ending ellipsis. The Figma presentation has overflow regression cases.
4. **Decision — exact numeric values in Figma:** v1 intentionally uses illustrative 0/25/50/75 snapshots instead of a misleading or combinatorially large numeric variant family. No existing public numeric Figma control is claimed. **Runtime supports arbitrary valid values**, not these presets.
5. **Pending development/runtime verification — [HOS-40](https://linear.app/hossein-mor/issue/HOS-40):** Indeterminate animation and reduced-motion fallback, runtime numeric geometry, Angular component/API registration, accessible name/value/status announcements, responsive content and browser/assistive-technology tests. These are not design-source defects and must be completed in the owning runtime code.


The **Indeterminate Figma state is implemented**. Its Figma visual is a static reference; motion and accessibility implementation are not yet verified.

## Sources and handoff status

- Figma [canonical Progress Bar presentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23867-126381) — editable design source.
- [Design-to-Code Component Mapping](../integrations/component-mapping.md) — verified design identity, pending runtime mapping.
- [Progress Indicator](progress-indicator.md) — discrete workflow boundary.
- [Loading and Progress Content](../../content/patterns/loading-and-progress.md) — canonical content constraints.
- [Dynamic Content and Feedback](../accessibility/dynamic-content-and-feedback.md) — accessible status requirements.
- HOS-37: https://linear.app/hossein-mor/issue/HOS-37/pilot-progress-bar-component-across-figma-and-design-system-knowledge

**Handoff status:** Documentation **final**; Progress Bar Figma composition and content/size QA **ready for development**. Indeterminate is **static in Figma** and Figma numeric presets are **illustrative only**; runtime animation, numeric API, accessibility behavior and tests remain **unverified**. Original 20 variant masters and both component-set identities are preserved.
