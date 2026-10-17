---
id: design-system.audit.chip-final-2026-10-17
collection: design-system
type: audit
title: Chip family — final Figma and interaction audit (2026-10-17)
knowledge_state: verified
document_maturity: reviewed
design_status: handoff-ready
related:
  - design-system.component.chip
  - design-system.component.tag
  - design-system.pattern.anchored-disclosure
---

# Chip family — final Figma audit

**Scope:** The four published Chip component sets and the private nested Remove target, Figma presentation/playground, authoring properties, visual tokens/states, RTL and interface contracts. This is **Figma/design validation**, not a pass for production Angular behavior or screen readers.

**Source:** [Chip Figma canonical page](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23900-128061). Related task: [HOS-30](https://linear.app/hossein-mor/issue/HOS-30/pilot-chip-component-across-figma-and-design-system-knowledge). Related, currently held pattern: [Disclosure / Anchored](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23945-728).

## 1. Final public inventory

| Capability | Figma component set | Axes | Count |
|---|---|---|---:|
| Selectable | `20783:128158` | Size 3 × Selected 2 × State 5 | 30 |
| Removable | `23124:358` | Size 3 × State 5 × Open 2 | 30 |
| Disclosure | `20783:534` | Size 3 × Applied 2 × State 5 × Open 2 | 60 |
| Action | `23123:125056` | Size 3 × State 5 | 15 |
| Private remove target | `23193:372` | Size 3 × State 5 | 15 |

**All 135 public variants and 15 internal variants are present.** No unrelated Type/UseCase/Color mega axis has been added.

Sizes: Extra Small **28px**, Small **32px**, Medium **40px**. Current radius is the *shared bound* Radius/Full variable, not a literal local shape radius; all original and new variants use it. Item/content gap: bound shared **8px**. Label type: **Label/XS** for Extra Small, **Label/SM** for Small/Medium; Detail/Summary uses Body/Compact/XS or SM respectively.

## 2. Changes carried out

- New `Open=False/True` Figma **Variant** property on Chip / Disclosure and Chip / Removable, independent of State and Applied.
- **Disclosure, Open=True:** use `Icon/chevron_up`, equivalent semantic Active surface for the correct Applied family; keyboard Focus styling remains visible in the Focus/True combination.
- **Removable, Open=True:** use Accent Active surface while preserving the independent nested `__Chip Remove Action` target, including its own hover/focus/disabled treatment.
- All **30 prior Disclosure** and **15 prior Removable** Variant node identities were preserved as Open=False. Added 30+15 new Open=True variants.
- Canonical Chip Figma page updated: variant counts, axes, source descriptions, playground examples. Industry disclosure has Open=True; committed software editing example has Removable/Open=True.
- Existing anchored Disclosure Pattern examples were reconciled with the new canonical trigger `Open=True` on Disclosure and Removable. The Pattern remains on Hold as a separate development item; no new Surface Slot was added inside Chip.
- Temporary override-test instances were deleted.

**Why Variant, not Figma BOOLEAN:** One toggle must update multiple different visual fields (semantic surface and up/down chevron), and a single Boolean visibility reference cannot safely express both complementary icon instances and token behavior. Figma's two-value Variant axis supplies an authorable Open control with reliable coupled styling. **Runtime Open remains an independent Boolean.**

## 3. Final QA, verified in live Figma

| Area | Result | Evidence |
|---|---|---|
| Variant coverage | **PASS** | 30 + 30 + 60 + 15 public + 15 private |
| Variant geometry | **PASS** | Zero overlapping pairs and no variants outside Component Set bounds |
| Geometry and typography | **PASS** | 28/32/40 height; 8px bound gap; Label/XS, Label/SM style; Radius/Full bound for all 150 |
| Open states | **PASS** | Open=True defaults to chevron up for enabled Disclosure; active semantic fill for Disclosure/Removable |
| Open/Applied independence | **PASS** | Applied true/false × Open true/false all covered for every Size×State |
| Persistent and transient states | **PASS** | Selected, Applied and Open are not collapsed into Hover/Focus/Active |
| Focus | **PASS (Figma)** | All Focus variants retain shared outside focus effect, including Open=True |
| Disabled | **PASS (Figma)** | Disabled/Open=True appears disabled. Runtime must prevent opening; no live action implied by authoring combination |
| Remove target | **PASS (Figma)** | Size-matched 28/32/40 private component; exists in all Removable variants, including Open=True |
| Semantic styling | **PASS** | Shared surface/foreground/line variables, no Chip-specific or Tag color axis |
| RTL anatomy | **PASS (Figma)** | Logical start/end maintained; disclosure icon and remove action retained; mixed Persian/Latin software sample retained |
| Figma override preservation | **PASS** | Toggled Open False→True→False→True for a Chip / Disclosure with custom Label and for a Chip / Removable; custom label persisted, chevron swapped correctly |
| Linked Pattern compatibility | **PASS (visual)** | Pattern Open=True triggers now select the published Chip Open=True variants |
| Page presentation | **PASS (visual)** | Full canonical page and linked Disclosure Pattern playground visually inspected |

## 4. Interaction/a11y contract by capability

- **Selectable:** direct selection/deselection; `Selected` is persistent; check is logical start; group/choice semantics are external. Keyboard-operable, selected state must be programmatically exposed by consuming pattern/runtime.
- **Action:** a value-level action to add/start/configure. No Open/Selected/Applied axis. Add Microsoft Word can launch the level panel *as an action*; that is not a reason to rename this Chip to Disclosure.
- **Disclosure:** a trigger for a secondary surface. `Applied` reflects persistent criteria; `Open` reflects temporary visibility. The owning pattern/overlay handles placement, dismissal, selection, focus return, Escape, responsive fallback and accessibility roles. Runtime body reports expanded state. Disabled forces Open false.
- **Removable:** represents a committed item (e.g., Microsoft Word · متوسط). A separately operable body can reopen the editor (`Open=True` while the panel is visible); `×` only removes. **Never nest interactive buttons**; keyboard focus and accessible names for Body versus Remove must be independent. `aria-expanded` belongs on the body only for popup actions, not on ×. Remove must not toggle popup.
- **Tag boundary:** descriptive/passive metadata uses Tag, not Chip; no tag-specific hue semantics on Chips.

## 5. Risk register / known limitations

| Priority | Item | Disposition |
|---|---|---|
| P0 for production | Angular/Storybook keyboard, ARIA, hit targets, Popover anchoring and focus-return have **not been run** against the owning runtime | **Runtime QA required before production certification** |
| P1 | Canonical Figma 60 Disclosure / 30 Removable axes include logical `State=Disabled, Open=True` combinations | Acceptable authoring matrix; application must force `open=false` when disabled |
| P1 | `Chip / Removable` body and × have distinct focus semantics in runtime; Figma visual alone cannot prove valid DOM | Implement compound interaction targets as siblings and test keyboard/screen reader |
| P2 | Full/Pill radius is the current Figma decision, but global control radius is 6px | Not a new defect; **do not unilaterally change** until Chip-family radius direction is explicitly reapproved |
| P2 | Long-label truncation and max-width behavior require container/runtime constraints | Visual sample exists; verify actual overflow handling in Storybook |
| P2 | Pattern-level draft vs committed selection, apply/clear and mobile fallback | Owned by the currently held Disclosure Pattern, not the Chip component |
| P2 | Figma variant count grew intentionally rather than creating brittle inverted-Boolean icon controls | Reevaluate only if component complexity materially impairs authoring; old IDs retained |

## 6. Final decision

**Figma + Design System Knowledge:** Handoff-ready from the design side, with no detected visual or structural blocker. **Runtime/Production:** not yet certified. Keep the independent Disclosure Pattern on Hold; do not block use of Selectable / Action / Removable / Disclosure triggers in design while Storybook QA is pending. This audit should be revisited when verified Angular runtime and Code Connect sources are registered.
