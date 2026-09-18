---
id: accordion
collection: design-system
type: component
title: Accordion
summary: Accordion groups related disclosure items so users can reveal supporting content in place while keeping the page scannable.
knowledge_state: verified
document_maturity: draft
related: []
design_status: ready-for-dev
design_maturity: handoff-ready
source_figma: https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=22794-548
source_node: 22794:548
---

# Accordion

## Purpose

Accordion organizes related supporting content as a vertical set of expandable sections.

Use it when users benefit from scanning section titles before deciding which details to read. Do not use it to hide information that is required to understand or complete the current task.

## Accordion vs Disclosure

The shared design unit is **Accordion Item**.

- Two or more related items stacked together form an **Accordion**.
- One item used by itself is a **Disclosure / Collapsible section** pattern.
- Do not create a duplicate Figma component only to represent the standalone case; the same Accordion Item owns the interaction and anatomy.
- Accordion is not navigation. Use Tabs, navigation, Tree, or another navigation pattern when changing sections changes destination/context rather than revealing content in place.

## Canonical Figma source

Current design source:

- File: `-DS--Job-Vision-NEXT`
- File key: `rROD8ctH9UfPGAMrRrOzHe`
- Component set: `Accordion / Item`
- Node ID: `22794:548`
- Component key: `2728144865f9616dd66228719b4fb71936e3062a`

The older `Accordion`, `_Accordion item`, and Accordion skeleton constructions on the same page are legacy assets retained for migration compatibility. Do not use them as the source for new work.

## Anatomy

Each Accordion Item contains:

1. **Trigger** — the full interactive header row.
2. **Title** — the accessible visible label of the Trigger.
3. **Indicator** — decorative expand/collapse Chevron.
4. **Panel** — content region controlled by the Trigger.
5. **Body** — optional standard body copy.
6. **Custom content** — optional instance-swap region for richer Panel content.
7. **Divider** — structural separation between adjacent items.

The Trigger owns expand/collapse interaction. The Chevron is not a separate control.

Do not place arbitrary interactive controls inside the Trigger. If a persistent action must sit beside an Accordion heading, keep it outside the heading/Trigger as a sibling control with its own semantics and focus target.

## Figma API

### Variant properties

| Property | Values | Meaning |
|---|---|---|
| `Size` | `Large / Medium / Small` | Minimum Trigger height and title typography |
| `State` | `Enabled / Hover / Focus / Disabled` | Design-time interaction state |
| `Expanded` | `False / True` | Panel visibility and Indicator direction |

There are 24 visual variants: `3 Size × 4 State × 2 Expanded`.

`Alignment` and `Skeleton` are intentionally not variant axes.

### Content properties

| Property | Type | Default |
|---|---|---|
| `Title` | Text | `عنوان آکاردئون` |
| `Body` | Boolean | `True` |
| `Body text` | Text | sample Panel copy |
| `Custom content` | Boolean | `False` |
| `Content swap` | Instance swap | shared Slot placeholder |

The Panel may contain Body only, custom content only, or both.

The Figma Slot placeholder is authoring scaffolding, not part of the runtime Accordion appearance. Swapped content follows its own component contract.

## Size and layout

| Size | Trigger min-height | Title style | Vertical padding |
|---|---:|---|---:|
| Large | 48 px | `Label/MD` — 16/24, 500 | 8 px |
| Medium | 40 px | `Label/SM` — 14/20, 500 | 8 px |
| Small | 32 px | `Label/SM` — 14/20, 500 | 4 px |

Shared Trigger construction:

- horizontal padding: 16 px;
- Title–Indicator gap: 16 px;
- Indicator: 16 px;
- Trigger width: fill container;
- title: wrapping allowed, no truncation by default;
- listed heights are minimums; multiline titles increase Trigger height.

Panel construction:

- typography: `Body/SM` — 14/24, 400;
- top padding: 8 px;
- logical Start inset: 48 px;
- logical End inset: 16 px;
- bottom padding: 16 px;
- Body ↔ custom-content gap: 12 px.

The Start inset aligns Panel content with the Title rather than the Indicator.

The 400 px width used in the component-set variants is a presentation width only. Product instances should fill the available container.

## Visual treatment

Accordion is intentionally low-decoration:

- no card background by default;
- no outer surface border;
- no radius;
- no elevation shadow;
- a 1 px `line/muted` divider separates items;
- expanded is disclosure state, not selection state, so it does not receive Brand, Accent, or Selected treatment.

## States

| State | Trigger treatment | Title / Indicator | Divider |
|---|---|---|---|
| Enabled | transparent | normal semantic foreground | `line/muted` |
| Hover | `surface/transparent-hover` | normal semantic foreground | `line/muted` |
| Active | runtime-only `surface/transparent-active` feedback | normal semantic foreground | `line/muted` |
| Focus | shared Focus treatment on Trigger only | normal semantic foreground | `line/muted` |
| Disabled | transparent | `fg/disabled` | `line/muted` |

Focus uses the shared `focus - Outer/Border all` Effect Style, bound to `focus/default`. It must not resize the Trigger or wrap the Panel.

Active is a transient runtime pseudo-state and is intentionally not a Figma variant axis.

If a Disabled item is already expanded, Panel content remains readable. Avoid a collapsed Disabled item when disabling it would make otherwise necessary content inaccessible.

## Loading

Loading is not an Accordion interaction state and is not part of the Accordion variant matrix.

- If the whole Accordion is unavailable while data loads, use the shared loading/skeleton pattern outside the interactive Accordion contract.
- If only expanded Panel content is loading, the Panel may contain an appropriate Loading/Skeleton component.
- Do not expose placeholder Accordion headers as operable controls.

This avoids multiplying every interactive state by a loading representation.

## Expanded and collapsed behavior

Default initial state is **collapsed** unless product context has a clear reason to reveal specific content initially.

Collapsed:
- Panel hidden;
- Indicator points down;
- accessible expanded state is false.

Expanded:
- Panel visible directly below the Trigger;
- Indicator points up;
- accessible expanded state is true.

Opening/closing must not change horizontal alignment.

## Group behavior

Accordion supports both group policies:

- **Multiple-open — default.** Items own independent expanded state and any number may remain open.
- **Single-open — explicit option.** Opening one item closes another open item in the same group.

Both policies allow all items to be collapsed. A “one item must always remain open” model is not part of the default Accordion contract and requires a product-specific reason.

Use Single-open only when limiting simultaneous expansion is materially useful. Do not use it only to make the interface look tidier.

Figma does not add a group-behavior variant because this behavior does not change the visual anatomy of an individual item. QA examples on the Accordion page demonstrate grouped multiple-open usage.

## RTL and direction

Persian/RTL is the primary authored context.

- Indicator sits at logical **Start**: right in RTL.
- Title is right-aligned for Persian content.
- Panel Start inset follows the Title alignment.
- Chevron up/down expresses expanded state and does not need horizontal mirroring.
- Runtime implementations should use logical Start/End layout rather than physical left/right rules.

The Figma candidate is RTL-first and intentionally does not restore the old physical `Alignment=Right/Left` axis. If a product later needs first-class LTR authoring in Figma, add a direction-aware authoring mechanism rather than reintroducing a physical alignment property.

## Accessibility contract

Follow the current WAI-ARIA Accordion pattern.

### Semantics

- Use a native `button` for each Trigger.
- Place the Trigger in the appropriate heading level when the items represent document sections.
- Keep the heading limited to the Trigger; persistent sibling actions do not belong inside that heading/button.
- Reflect Panel visibility with `aria-expanded`.
- Associate Trigger and Panel with `aria-controls` and a stable Panel ID.
- Indicator is decorative and hidden from assistive technology.
- Add `role="region"` + `aria-labelledby` only when the extra landmark structure is useful; avoid landmark proliferation in large groups where many Panels can be open.

### Keyboard

- `Enter` and `Space` toggle the focused Trigger.
- `Tab` and `Shift+Tab` follow normal page focus order through all focusable controls.
- Focus remains on the Trigger after expand/collapse.
- Do not automatically move focus into the Panel.
- Do not add Arrow/Home/End navigation or a roving-focus model to the base Accordion contract.

### Disabled

Disabled suppresses Trigger operation but does not make required explanatory content unreadable. If only controls inside a Panel are unavailable, keep the Accordion itself operable and disable those inner controls instead.

External reference: https://www.w3.org/WAI/ARIA/apg/patterns/accordion/

## Motion

Motion should explain disclosure, not delay access to content.

The shared Motion foundation does not yet define a verified duration/easing contract, so Accordion does not invent component-specific timing.

When runtime motion is implemented:
- animate only the disclosure change, not unrelated layout;
- keep the transition short;
- do not use motion as the only state cue;
- respect reduced-motion preferences.

Exact duration, easing, DOM measurement technique, and animation implementation remain runtime-owned and unverified until the shared Motion/runtime source is registered.

## Usage

Use Accordion for:
- FAQs;
- optional supporting information split into clear sections;
- settings/details users may inspect selectively;
- secondary content where simultaneous comparison may be useful.

Do not use Accordion for:
- small content that is clearer when shown directly;
- primary page messaging or critical task requirements;
- sequential step flows;
- navigation between destinations;
- content whose collapsed state would hide an error or required action;
- deeply nested disclosure structures.

## Content guidance

- Titles should be short, specific, and unique within a group.
- Avoid generic repeated labels such as “More information”.
- Keep essential status/error information outside collapsed Panels.
- Panel content can be richer than text, but nested interactive content must follow normal focus order and its own component rules.
- Avoid nested Accordions unless the information architecture clearly requires another disclosure level.

## Semantic token mapping

Accordion uses shared Semantic roles and introduces no Accordion-specific Color tokens.

| Need | Semantic role |
|---|---|
| Title | `fg/primary` |
| Indicator | `fg/secondary` |
| Panel copy | `fg/primary` |
| Disabled Trigger content | `fg/disabled` |
| Divider | `line/muted` |
| Hover | `surface/transparent-hover` |
| Active | `surface/transparent-active` |
| Focus | `focus/default` |

## Runtime boundary

Current Code and Storybook sources are not registered.

Therefore this document does **not** assert:
- exact Angular component names;
- prop/input names;
- DOM wrapper structure beyond the accessibility contract;
- animation library or implementation;
- exact class names;
- Storybook story IDs.

Conceptually, runtime must support item expanded/disabled state and group Multiple/Single policy, but exact API naming is implementation-owned.

## QA checklist

Verify:
- 24 Figma variants exist with only `Size / State / Expanded`;
- Trigger fills the available width;
- Large/Medium/Small min-heights are 48/40/32;
- multiline titles grow rather than truncate;
- Expanded changes Indicator and Panel visibility without horizontal shift;
- Focus appears on Trigger only;
- Disabled mutes Trigger content while readable expanded Panel content remains readable;
- Body-only, custom-only, and combined Panel content work;
- grouped items can show more than one expanded Panel;
- RTL Indicator and Panel inset align with the Title;
- no legacy Alignment/Skeleton axis is introduced into the canonical set.

## Open implementation items

- Publish/migrate away from the legacy Accordion assets after product migration risk is reviewed.
- Register runtime Design System repository/package and Storybook.
- Verify Figma ↔ runtime property mapping from the actual implementation source.
- Adopt shared Motion timing/easing when the Motion foundation is finalized.
- Add an explicit Figma direction-authoring control only if first-class LTR product design becomes a real requirement.
