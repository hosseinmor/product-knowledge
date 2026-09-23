---
id: design-system.reference.component-mapping
collection: design-system
type: reference
title: Design-to-Code Component Mapping
summary: Registry contract for mapping stable Figma component identities to runtime components and Storybook; records current verified mappings and gaps.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: 2026-09-23
related:
  - design-system.reference.figma
  - design-system.reference.code
  - design-system.reference.storybook
---

# Design-to-Code Component Mapping

This registry prevents AI and humans from guessing runtime component APIs from Figma names.

A mapping is considered verified only when both sides are supported by their owning live sources.

## Mapping fields

For each mapped component record:

```text
Design System component
Figma file key
Figma component key
Figma node ID
Code repository
Code package
Runtime component/API identifier
Figma property → code prop mapping
Storybook stable story/docs identifier
Mapping mechanism
Last verified
Known mismatch/gap
```

`Mapping mechanism` may be Figma Code Connect or another explicit registry. The mechanism is less important than having a stable, reviewable mapping.

## Current mapping registry

### Button

| Field | Current value |
|---|---|
| DS component | Button |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Button / Default` |
| Figma component key | `be5d0d9cd5fdd02f9d7afa1e371c2f2a23acb329` |
| Figma node ID | `1854:1776` |
| Figma variant properties | `Style / Size / State / Loading` |
| Figma content properties | `Button text / Start Icon / End Icon / Swap Start Icon / Swap End Icon` |
| Figma styles | `Brand / Primary / Secondary / Tertiary / Ghost / Danger Primary / Danger Tertiary / Danger Ghost` |
| Figma sizes | `Extra Small 28 / Small 32 / Medium 40 / Large 48` |
| Figma states | `Enabled / Hover / Active / Focus / Disabled` |
| Loading representation | `False / True`, separate from interaction State; uses shared `Loading / Small / Active` component |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer code prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

The Button design identity and current Figma property model are verified. Runtime API, Storybook identity, and Figma-to-code prop mapping remain deliberately unverified because the owning runtime Design System repository/package and Storybook source are not yet registered. Track that source gap through the integration contract rather than guessing from Figma.


### Icon Button

| Field | Current value |
|---|---|
| DS component | Icon Button |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Icon Button / Default` |
| Figma component key | `f9b7af4bd9afaf768ae955c51ccddd29833c5ca7` |
| Figma node ID | `22685:1410` |
| Figma variant properties | `Style / Size / State` |
| Figma content properties | `Icon` instance swap |
| Figma styles | `Brand / Primary / Secondary / Tertiary / Ghost / Danger Tertiary / Danger Ghost` |
| Figma sizes | `Extra Small 28 / Small 32 / Medium 40 / Large 48` |
| Figma states | `Enabled / Hover / Active / Focus / Disabled` |
| Icon size | Fixed `18px` |
| Tooltip contract | Required for operable Icon Buttons on hover/focus; Tooltip does not replace the accessible name |
| Loading / Selected | Not part of the current Icon Button contract |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer code prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

The Icon Button design identity and current Figma property model are verified. Its accessible-name, Tooltip, sizing, destructive-action, and state boundaries are defined in `../components/icon-button.md`. Runtime API, Storybook identity, Tooltip composition strategy, and Figma-to-code prop mapping remain deliberately unverified until the owning runtime Design System source is registered.



### Menu

| Field | Current value |
|---|---|
| DS component | Menu |
| Knowledge document | `../components/menu.md` |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Menu / Default` |
| Figma component key | `5b8278235b0cefb99927a2507739afb15ace8f3b` |
| Figma node ID | `17332:167748` |
| Figma variant properties | `Size / Layout` |
| Figma content properties | `Content` native SLOT |
| Variant count | `8 = 4 Size × 2 Layout` |
| Figma sizes | `Extra Small 28 / Small 32 / Medium 40 / Large 48` item baseline; default `Medium` |
| Menu layouts | `Simple / Complex`; default `Simple`; Simple collapses leading, Complex reserves a `16px` leading column across items; default Complex authoring content shows the shared Start icon |
| Menu width | `160px min / 200px default / 320px max` |
| Menu surface | `surface/raised + Shadow/Floating + 12px Large radius` |
| Menu Item set | `Menu Item / Default` |
| Menu Item key | `77d84f9c0d0377652a87f13ef915c65412655073` |
| Menu Item node ID | `17332:167436` |
| Menu Item variants | `40 = 4 Size × 5 State × 2 Tone` |
| Menu Item states | `Default / Hover / Active / Focus / Disabled` |
| Menu Item tones | `Default / Danger`; Disabled is State and visually overrides Tone |
| Menu Item content properties | `Label / Leading / Checked / Show start icon / Start icon / Show shortcut / Shortcut / Submenu` |
| Submenu depth | JV v1 authoring supports `Root Menu → one child Submenu` only; no submenu trigger inside the child submenu |
| Submenu composition | Child surface reuses `Menu / Default`, matches parent Size, keeps independent `160–320px` width, uses 2px surface gap, opens toward logical End and may flip on collision |
| Menu Item anatomy | Flat direct children: `Trailing + Label + Leading`; no active nested Menu Item Content component |
| Leading rule | `Leading=false` collapses the Start column; `Leading=true` reserves `16px`; Leading/Trailing containers are transparent; Menu Layout controls the default composition |
| Width ownership | Menu owns `160–320px` shell width; Menu Item has no independent min/max width and fills the Menu content slot |
| Icon color override | Shared icon components keep a fixed base color; Menu Item explicitly overrides icons by Tone/State: Default → `fg/primary`, Danger → `fg/danger`, Disabled → `fg/disabled`; re-check after icon swap |
| Group Label | `Menu Group Label / Default`, node `23038:129820`, key `ae3dbe7236e339083cccd60ad047306201c0f6c6` |
| Divider | `Menu Divider / Default`, node `23038:129822`, key `8cb217e111f87fa16785890815d769083ac7e5ec` |
| Legacy migration assets | `Legacy / Menu Item Content` key `3c4735684b5eb1146dab273119bcc59dbceee8aa`; `Legacy / Keyboard shortcut` key `e2113c87df4d0d02d41477f4c706fb6b30a6437a`; `Legacy / Overflow menu` key `89d20a2413e0b877ce2d9c358ce75bb903155bfb`; retained Overflow Open uses an absolute Menu overlay, `clip content = false`, 2px trigger gap, and unchanged trigger bounds |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-23 |

The Menu design identity, action/command boundary, Size × Layout model, flat Menu Item anatomy, Size × State × Tone Menu Item model, one-level submenu composition/depth, grouping helpers, RTL geometry, semantic visual treatments, width/truncation rules, and accessibility contract are verified in `../components/menu.md`. Runtime API, exact DOM/focus implementation, overlay/positioning engine, Storybook identity, and Figma-to-code prop mapping remain deliberately unverified until the owning runtime source is registered.

### Menu Button

| Field | Current value |
|---|---|
| DS component | Menu Button |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Menu Button / Default` |
| Figma component key | `166f62776a8c17f3ccdc9f4891892fcd380be68c` |
| Figma node ID | `22930:811` |
| Figma variant properties | `Size / Open` |
| Variant count | `8 = 4 Size × 2 Open` |
| Figma content properties | `Menu content` native SLOT; exposed nested `Trigger / Button` |
| Figma sizes | `Extra Small 28 / Small 32 / Medium 40 / Large 48` |
| Default trigger | Canonical Button / Tertiary; approved Menu Button styles: Primary / Tertiary / Ghost |
| Open representation | `Open=True` maps Trigger to Active + chevron-up; Menu remains outside trigger layout |
| Anchor gap | `2px` per shared contextual-surface rule |
| Loading | No top-level Loading state; loading content belongs inside Menu |
| Menu size alignment | Extra Small / Small / Medium / Large map 1:1 to canonical Menu 28 / 32 / 40 / 48 |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-20 |

The Menu Button design identity, Button composition, native Menu Slot, Size × Open matrix, 2px anchoring rule, RTL geometry, and Menu Button accessibility contract are verified in `../components/menu-button.md`. Runtime popup API, exact prop names, collision/portal implementation, and Storybook identity remain unverified.


### Combo Button

| Field | Current value |
|---|---|
| DS component | Combo Button |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Combo Button / Default` |
| Figma component key | `c6f34b8a4294241844d10349881d8264b1c072eb` |
| Figma node ID | `22932:134187` |
| Figma variant properties | `Style / Size / Open` |
| Variant count | `24 = 3 Style × 4 Size × 2 Open` |
| Figma styles | `Primary / Secondary / Tertiary` |
| Figma sizes | `Extra Small 28 / Small 32 / Medium 40 / Large 48` |
| Composition | Canonical `Primary Action / Button` instance + canonical `Menu Trigger / Icon Button` instance + native `Menu content` SLOT; no wrapper/custom separator node; `0px` layout gap |
| Inter-segment treatment | No standalone Divider/custom separator and no layout gap; Primary/Secondary use a 1px inside `palette/bw/white` stroke on the Menu Trigger touching edge in normal filled states; Tertiary composes `line/default` borders from the two canonical instances, with the Primary Action left edge as the single visible joining border and the Menu Trigger touching right edge removed |
| Open representation | Only Menu Trigger maps to Active + chevron-up; Primary Action state remains independent |
| Anchor gap | `2px` |
| Loading | Owned by nested Primary Action; no outer Loading axis |
| RTL | Primary Action logical Start/right; Menu Trigger logical End/left |
| Menu size alignment | Extra Small / Small / Medium / Large map 1:1 to canonical Menu 28 / 32 / 40 / 48 |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-20 |

The Combo Button design identity, canonical Button/Icon Button instance composition, connected-segment geometry, native Menu Slot, Style × Size × Open matrix, fixed internal Menu Trigger authoring model, instance-owned filled-style join stroke, independent segment behavior, 2px anchoring rule, RTL geometry, loading boundary, and accessibility contract are verified in `../components/combo-button.md`. Runtime component/API, Storybook identity, and exact Figma-to-code property mapping remain unverified.


### Tooltip

| Field | Current value |
|---|---|
| DS component | Tooltip |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Tooltip / Default` |
| Figma component key | `e29f8f48a0b3ec52f9490d4a9c101df5fba9d769` |
| Figma node ID | `22773:127299` |
| Figma variant properties | `Side / Align` |
| Figma content properties | `Text` |
| Figma matrix | `4 Sides × 3 Alignments = 12 variants` |
| Anatomy | Inverse Surface + text; no caret / arrow |
| Anchor offset | Fixed `2px` Surface-to-trigger gap |
| Visual roles | `surface/inverse + fg/on-inverse`; no border; no shadow |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer code prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

Tooltip design identity, arrowless anatomy, placement matrix, RTL mapping, 2px anchor offset, and Icon Button consumer contract are verified. Runtime delay, collision/flip, portal/layering, package/API identity, Storybook identity, and Figma-to-code mapping remain deliberately unverified until the owning runtime source is registered.


### Accordion

| Field | Current value |
|---|---|
| DS component | Accordion |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component | `Accordion` |
| Figma component key | `649891c2bfc1413f60f04011bc71a05576d12738` |
| Figma node ID | `22821:129502` |
| Figma content properties | `Items` native SLOT |
| Items Slot | 1+ children, zero gap, preferred/allowed content = `Accordion Item` |
| Default authoring content | 3 collapsed Accordion Item instances; count is not fixed |
| Group behavior | Multiple-open default; Single-open explicit runtime option; both allow all-collapsed |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

### Accordion Item

| Field | Current value |
|---|---|
| DS component | Accordion Item / standalone Disclosure |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Accordion Item` |
| Figma component key | `2728144865f9616dd66228719b4fb71936e3062a` |
| Figma node ID | `22794:548` |
| Figma variant properties | `Size / State / Expanded / Indicator position` |
| Variant count | 48 |
| Figma content properties | `Title / Content` |
| Content | Native Figma SLOT with editable default Body text; accepts arbitrary frames/text/component instances |
| Figma sizes | `Large 48 / Medium 40 / Small 32` minimum Trigger heights |
| Figma states | `Enabled / Hover / Focus / Disabled`; Active is runtime-only |
| Indicator position | `Start / End`; in RTL Start=right and End=left |
| Composition | Same Item may be used alone as Disclosure or inside Accordion Items Slot |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

Accordion and Accordion Item design identities, native Slot composition, visual state model, RTL geometry, and current Figma property models are verified. Runtime API, exact DOM/animation implementation, Storybook identity, and Figma-to-code property mapping remain deliberately unverified until the owning runtime Design System source is registered.

### Link

| Field | Current value |
|---|---|
| DS component | Link |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Link / Default` |
| Figma component key | `f31eac5461a0d8a608089f696b3b1402590be8a9` |
| Figma node ID | `22920:125581` |
| Figma variant properties | `Style / Size / State` |
| Variant count | `27 = 3 Style × 3 Size × 3 Figma State` |
| Figma content properties | `Link text / End icon / Swap end icon` |
| Figma styles | `Default / Subtle / Inverse` |
| Figma sizes | `Small 12/16 / Medium 14/20 / Large 16/24`; Medium default |
| Figma states | `Enabled / Hover / Focus`; Active is runtime-only and visually matches Hover |
| Background | Transparent component and Label wrapper in every variant |
| Underline behavior | Enabled none; Hover / Active / Focus underlined at runtime |
| Figma underline implementation | Responsive 1px label-width helper; Enabled opacity 0, Hover/Focus opacity 1; runtime uses real text-decoration |
| Icon geometry | Optional End icon only; fixed `18px`, `8px` label gap |
| Deliberate exclusions | No Underline axis, Start icon, Disabled, Visited, Bold, or legacy Inline axis |
| Inline / multiline Figma authoring | Native Text range using Link semantic token + persistent underline; inherits surrounding typography |
| Legacy Figma component | `Link / Legacy`, node `3245:28722`; migration only |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer code prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

The Link design identity, Style × Size × State Figma model, transparent anatomy, semantic token mapping, state-driven underline behavior, End-icon geometry, and native-Text inline/multiline authoring boundary are verified in `../components/link.md`. Runtime API, Storybook identity, and Figma-to-code prop mapping remain deliberately unverified until the owning runtime Design System source is registered.


### Breadcrumb

| Field | Current value |
|---|---|
| DS component | Breadcrumb |
| Knowledge document | `../components/breadcrumb.md` |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component | `Breadcrumb` |
| Figma component key | `b0fb38288d8b84e0ff6e1d5ded6eeb31574581fa` |
| Figma node ID | `22973:282463` |
| Figma content properties | `Items` native SLOT |
| Default authoring content | 3 visible Breadcrumb Item instances |
| Items Slot | min 2 children; preferred/allowed content = `Breadcrumb Item / Default`; default content visible on insertion |
| Breadcrumb Item set | `Breadcrumb Item / Default` |
| Breadcrumb Item key | `e0fcea8c52b6deb183c6d2c4624243875ae21425` |
| Breadcrumb Item node ID | `22986:407` |
| Breadcrumb Item variants | `Type = Link / Current / Overflow` |
| Breadcrumb Item content property | `Current label` |
| Link composition | canonical `Link / Subtle / Medium`; interaction states delegated to Link |
| Overflow composition | canonical `Icon Button / Ghost / Extra Small`; popup/menu behavior delegated to owning runtime pattern |
| Current page | always present, non-interactive, semantic current-page item |
| Layout | single-line; 8px Items Slot gap; deep paths use Root / Overflow / Parent / Current |
| Legacy Figma | `Breadcrumb / Legacy` and `Breadcrumb Item / Legacy`; migration/reference only |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names or overflow algorithm from Figma |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

The Breadcrumb design identity, Item composition, Link/Icon Button reuse, current-page treatment, single-line truncation/collapse model, RTL behavior, native Slot authoring, and accessibility contract are verified in `../components/breadcrumb.md`. Runtime API, exact DOM/popup implementation, collapse measurement algorithm, Storybook identity, and Figma-to-code mapping remain deliberately unverified until the owning runtime Design System source is registered.


### Inline Notification

| Field | Current value |
|---|---|
| DS component | Inline Notification |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Inline Notification` |
| Figma component key | `eb09e1db167646902904f70dfd4e3a194a8a265d` |
| Figma node ID | `22838:3046` |
| Figma variant properties | `Status` |
| Figma content properties | `Message / Description / Show description / Action / Dismissible / Action content` |
| Variant count | 4 = Info / Success / Warning / Error |
| Action composition | Native `Action content` SLOT; current preferred components are shared Link and Tertiary Small Button |
| Dismiss composition | Shared `Icon Button / Ghost / Medium`, absolute top-left in RTL |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

The Inline Notification design identity, severity matrix, content anatomy, native Action Slot, RTL dismiss geometry, typography, and semantic token mapping are verified in `../components/notification.md`.

### Toast

| Field | Current value |
|---|---|
| DS component | Toast |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Toast` |
| Figma component key | `5c164a8b212650d4e9e322a9088fbc4fc4e7628f` |
| Figma node ID | `22839:3058` |
| Figma variant properties | `Status / Contrast` |
| Figma content properties | `Title / Message / Show title / Action / Dismissible / Timeout indicator / Action content` |
| Variant count | 8 = 4 Status × 2 Contrast |
| Contrast | `Normal / High`; High is inverse-surface treatment, not severity |
| Action composition | Native `Action content` SLOT; Normal defaults to Default Link, High defaults to Inverse Link |
| Dismiss composition | Shared `Icon Button / Ghost / Medium`, absolute top-left in RTL |
| Elevation | `Shadow/Floating` |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

The Toast design identity, Status × Contrast matrix, native Action Slot, timeout-indicator capability, RTL dismiss geometry, typography, elevation, and semantic token mapping are verified in `../components/notification.md`. Exact runtime timing, queue/stack behavior, placement, announcement behavior, and High-Toast Button treatment remain unverified.


### Checkbox

| Field | Current value |
|---|---|
| DS component | Checkbox |
| Knowledge document | `../components/checkbox.md` |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Checkbox / Default` |
| Figma component key | `af1fdbe97bf103d8ae5e4540d36f4ffb284cc35b` |
| Figma node ID | `3193:29303` |
| Figma variant properties | `Selection / State` |
| Variant count | `9 = 3 Selection × 3 State` |
| Figma content properties | `Label / Show label` |
| Figma selections | `Unchecked / Checked / Indeterminate` |
| Figma states | `Default / Focus / Disabled` |
| Visual size | `20px` Checkbox icon instance; source icon artwork scales proportionally inside the nested instance |
| Label gap | `8px` |
| Selection semantics | Exact local Icons-page components: unchecked node `15087:365340` key `b4b5e8aad25d7be4009568638bc86a3b85a6a185`; checked node `15087:365337` key `a9b3101d611597626af94d5f3a63a08058bbceab`; indeterminate node `15087:365343` key `ae823e542df2e4ac6c644e4ce8b97fe13aaa5b89`; Unchecked = `fg/secondary`, Checked/Indeterminate = `fg/accent` |
| Focus | shared `focus/default` 2px outside ring with 1px gap; independent from selection |
| RTL | logical inline-start control / inline-end label; no Position variant |
| Checkbox Group set | `Checkbox Group / Default` |
| Checkbox Group key | `9c6f915d8bc3399d2f02fd0aad20218757b0749f` |
| Checkbox Group node ID | `23020:127117` |
| Checkbox Group properties | `Direction / Group label / Show group label` |
| Checkbox Group directions | `Vertical / Horizontal` |
| Horizontal group sizing | item instances Hug contents; `16px` inter-item gap |
| Validation | owned by surrounding form-field composition; no Error/Warning Checkbox variants |
| Loading | outside base Checkbox state matrix; use Skeleton composition rather than Skeleton variants |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

The Checkbox design identity, exact local icon-library sources, Selection × State matrix, 20px icon sizing, first-line/top-aligned multiline behavior, semantic color mapping, focus treatment, flexible-width/multiline behavior, Checkbox Group direction contract, validation/loading boundaries, RTL geometry, Indeterminate semantics, and accessibility contract are verified in `../components/checkbox.md`. Runtime API, exact DOM/event semantics, Storybook identity, and Figma-to-code prop mapping remain deliberately unverified until the owning runtime Design System source is registered.


### Radio

| Field | Current value |
|---|---|
| DS component | Radio |
| Knowledge document | `../components/radio.md` |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Radio / Default` |
| Figma component key | `a1e6b8ca998c57f78abd75b97b190aacbd662f44` |
| Figma node ID | `2930:23442` |
| Figma variant properties | `Selected / State` |
| Variant count | `6 = 2 Selected × 3 State` |
| Figma content properties | `Label / Show label` |
| Figma states | `Default / Focus / Disabled` |
| Visual size | `20px` Radio icon instance; source icon artwork scales proportionally inside the nested instance |
| Label gap | `8px` |
| Selection semantics | Exact local Icons-page components: unchecked node `15087:365350` key `c8005abc2598ad492de5ac17df5cfb9dc1a4509b`; checked node `15087:365346` key `5acf2d061791622a49c9826cd671f165d6648f73`; Unselected = `fg/secondary`, Selected = `fg/accent` |
| Focus | shared `focus/default` 2px outside ring with 1px gap; independent from selection |
| RTL | logical inline-start control / inline-end label; no Position variant |
| Radio Group set | `Radio Group / Default` |
| Radio Group key | `8a24b1caa72671235a5c9d26706efcc845f45eee` |
| Radio Group node ID | `2927:28166` |
| Radio Group properties | `Direction / Group label / Show group label` |
| Radio Group directions | `Vertical / Horizontal` |
| Validation | owned by surrounding form-field composition; no Error/Warning Radio variants |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

The Radio design identity, exact local icon-library sources, Selected × State matrix, 20px icon sizing, first-line/top-aligned multiline behavior, semantic color mapping, focus treatment, flexible-width/multiline behavior, Radio Group direction contract, validation boundary, RTL geometry, and accessibility contract are verified in `../components/radio.md`. Runtime API, exact DOM/event semantics, Storybook identity, and Figma-to-code prop mapping remain deliberately unverified until the owning runtime Design System source is registered.


### Toggle

| Field | Current value |
|---|---|
| DS component | Toggle |
| Knowledge document | `../components/switch.md` (legacy path/id retained for compatibility) |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Toggle` |
| Figma component key | `0c632b79747ffac5f05a4f2c762f81ddcb8293d7` |
| Figma node ID | `22928:125569` |
| Figma variant properties | `Size / State / Toggled` |
| Variant count | `24 = 2 Size × 6 State × 2 Toggled` |
| Figma content properties | `Label / Show label` |
| Figma sizes | `Medium 48×24, thumb 18` / `Small 32×16, thumb 10` |
| Figma states | `Default / Hover / Active / Focus / Disabled / Read-only` |
| Off visual | `surface/neutral-muted*` track; fixed white `palette/bw/white` thumb; no persistent border |
| On visual | `surface/accent-emphasis*` track; fixed white `palette/bw/white` thumb |
| Focus | `focus/default` 2px outside ring, independent from On/Off |
| RTL | Authored Off thumb right / On thumb left; runtime mirrors in LTR rather than adding an RTL variant |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

The Toggle design identity, Size × State × Toggled matrix, label contract, neutral/accent visual treatment, fixed-white Thumb, focus behavior, RTL geometry, motion guidance, and accessibility contract are verified in `../components/switch.md`. Runtime API, exact DOM/event semantics, Storybook identity, exact motion constants, and Figma-to-code prop mapping remain deliberately unverified until the owning runtime Design System source is registered.


### Content Switcher

| Field | Current value |
|---|---|
| DS component | Content Switcher |
| Knowledge document | `../components/content-switcher.md` |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Content Switcher` |
| Figma component key | `2d44a4df734823788a122e9a9c73fec3bd6e4ff2` |
| Figma node ID | `23083:1746` |
| Figma variant properties | `Size / Content` |
| Figma content property | `Items` native SLOT |
| Variant count | `6 = 3 Size × 2 Content` |
| Figma sizes | `Small 32 / Medium 40 / Large 48` total control height; no XS |
| Content modes | `Text / Icon`; Icon + Text intentionally unsupported |
| Default authoring content | 3 equal-width Items; exactly one Selected |
| Composition | 2–5 Items; count is Slot composition rather than a variant axis; single-line, no wrap |
| Internal Item set | `_Content Switcher Item`, node `23038:127212`, key `17b39a5fe6a7b1fbd1679202f90e2ca2a45aba35` |
| Item properties | `State / Label / Icon` |
| Item states | `Default / Hover / Active / Focus / Disabled / Selected`; Selected is terminal |
| Size inheritance | Parent Size controls hidden Item height/padding modes; customized Slots continue to inherit Size |
| Geometry | Track radius 8; Item radius 6; 2px inset; 2px Item gap; no divider |
| Track | `surface/muted` |
| Selected | `surface/default + fg/primary` |
| Icon color override | Shared Icons retain purple guard source color; Item overrides Default → `fg/secondary`, Hover/Active/Focus/Selected → `fg/primary`, Disabled → `fg/disabled`; verified to survive Icon swap |
| Responsive | Never wrap; Icon-only only when unambiguous, otherwise use Menu/Select |
| RTL | No RTL/Position variant; compose in logical reading order |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names or DOM/ARIA roles from Figma |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-21 |

The Content Switcher design identity, Size × Content parent model, native Items Slot, State-only internal Item model, inherited sizing, Text/Icon boundary, selected treatment, semantic foreground mapping, equal-width composition, responsive rule, RTL behavior, and accessibility contract are verified in `../components/content-switcher.md`. Runtime API, exact DOM/ARIA and keyboard implementation, Storybook identity, and Figma-to-code property mapping remain deliberately unverified until the owning runtime source is registered.


### Chip

| Field | Current value |
|---|---|
| DS component | Chip |
| Knowledge document | `../components/chip.md` |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Selectable set | `Chip / Selectable` |
| Selectable key / node | `5571e8e324b47155d7e9fd384aaea289c2e54d89` / `20783:128158` |
| Selectable variants | `20 = 2 Size × 2 Selected × 5 State` |
| Selectable properties | Variant: `Size / Selected / State`; content: `Label` |
| Removable set | `Chip / Removable` |
| Removable key / node | `193062043a2194024cc06c6d45f11b96b4a238b3` / `23124:358` |
| Removable variants | `10 = 2 Size × 5 State` |
| Removable properties | Variant: `Size / State`; content: `Label / Detail / Show detail / Show leading visual / Leading visual` |
| Removable behavioral capability | Body may be independently actionable; body and trailing Remove are separate runtime interaction/focus targets; Body action is not a Figma variant |
| Disclosure set | `Chip / Disclosure` |
| Disclosure key / node | `3ba6c8dc36a76632d1569108e024ae47c841a50c` / `20783:534` |
| Disclosure variants | `20 = 2 Size × 2 Applied × 5 State` |
| Disclosure properties | Variant: `Size / Applied / State`; content: `Label / Summary / Show summary` |
| Disclosure Open | Runtime-only; removed from Figma variants because reviewed Open treatment duplicated Hover visually |
| Disclosure Applied surface | `surface/selected` base; Hover/Active layer `surface/transparent-hover/active`; Focus preserves base + `Focus/Default` |
| Action set | `Chip / Action` |
| Action key / node | `876535cdb18030fe2d38c6c6221036d770838586` / `23123:125056` |
| Action variants | `10 = 2 Size × 5 State` |
| Action anatomy | Optional add/action icon at logical End — visually left of the label in RTL |
| Action properties | Variant: `Size / State`; content: `Label / Show trailing icon / Trailing icon` |
| Shared states | `Default / Hover / Active / Focus / Disabled` |
| Figma sizes | `Small 32 / Medium 40` |
| Label text style | `Body/Compact/SM` across all four Chip sets |
| Radius | shared `Radius / Full` — current Chip visual direction |
| Focus | shared `Focus/Default` outside focus-visible ring |
| Color | Semantic tokens only; every Chip Hover/Active preserves its semantic base and layers `surface/transparent-hover/active`: default-base families use `surface/default`, Selectable Selected uses `surface/accent-muted`, Disclosure Applied uses `surface/selected`; no public Color axis or Chip-specific color tokens |
| Usage mapping | Choice + Direct Filter → Selectable; Faceted/Popover Filter → Disclosure; committed/input value → Removable; add/start available value → Action |
| Visual grammar | `✓ selected at logical Start before label / ▾ disclose / × remove / + add-start` |
| Product-pattern boundary | Selection mode, required/allow-empty, filter composition, tokenized-input behavior, and software Available→Selected layout live at Group/Pattern level |
| Tag boundary | Tag remains passive/descriptive/categorical and owns `tag/{color}/*`; Chip is interactive and must not consume Tag color tokens |
| Legacy Figma | old Carbon-derived Chip sets, Control-chip artifacts, and old Chip Group components are reference-only; published identities preserved where safe |
| Documentation frame | `Chip / Documentation`, node `23143:531`; includes Component Set, Playground, real Disclosure+Popover composition, and migration note |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime props, DOM/ARIA roles, compound-control structure, or popup implementation from Figma |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-23 |

The Chip design identity is verified as four capability-specific public component sets that share one visual recipe without a mega Type matrix. Selectable, Removable, Disclosure, and Action contracts, current Full radius, shared structured-surface Hover/Active overlays across all Chip families, leading selected check anatomy, Action icon at logical End, focus-visible behavior, RTL anatomy, software lifecycle, Tag/Button/selection-control boundaries, real Disclosure + Popover composition, and legacy migration are documented in `../components/chip.md`. Runtime API, exact DOM/ARIA implementation, compound Removable structure, Storybook identity, and Figma-to-code property mapping remain deliberately unverified until the owning runtime Design System source is registered.


## Rules

- Figma property labels do not automatically become code prop names.
- Figma variant options do not prove equivalent runtime enums/states exist.
- A code component with a similar display name is not a verified mapping by name alone.
- Storybook title/path similarity is not enough; link it to the owning code component.
- Record meaningful mismatches rather than forcing one-to-one parity.
- Component mapping should be maintained as integration metadata, not copied into every component guideline.

## Mapping priority

When runtime sources become available, map high-usage foundation components first:

```text
Button
Text Input
Select / Dropdown
Checkbox / Radio
Modal
Menu / Popover / Tooltip
Tabs
Tag
Data Table
```

Then expand based on product usage and migration risk.
