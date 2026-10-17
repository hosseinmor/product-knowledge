---
id: design-system.audit.chip-open-simplification-2026-10-17
collection: design-system
type: audit
title: Chip — Chevron-only Open and reduced variant architecture
knowledge_state: verified
document_maturity: reviewed
design_status: ready-for-sandbox
related:
  - design-system.component.chip
  - design-system.pattern.anchored-disclosure
---

# Chip — final Open simplification and migration audit (2026-10-17)

**Decision:** Opening a secondary surface **does not change Chip background, border or focus treatment**. The only Open appearance in the Chip family is the down/up Chevron direction on `Chip / Disclosure`. `Chip / Removable` contains no Chevron; there is no special Open appearance or Open Figma property. This decision supersedes the prior full `Open × State` variant model and follows the airline/stops filter examples reviewed on 2026-10-17.

## Canonical inventory

| Component set | Figma source node | Canonical axes | Current variants | Earlier variants |
|---|---|---|---:|---:|
| Chip / Selectable | `20783:128158` | Size 3 × Selected 2 × State 5 | 30 | 30 |
| Chip / Removable | `23124:358` | Size 3 × State 5 | 15 | 30 |
| Chip / Disclosure | `20783:534` | Size 3 × Applied 2 × State 5 | 30 | 60 |
| Chip / Action | `23123:125056` | Size 3 × State 5 | 15 | 15 |
| Private Remove Action | `23193:372` | Size 3 × State 5 | 15 | 15 |

**Total:** 90 public variants + 15 internal variants = **105 canonical variants** (previously 135 public + 15 internal = 150).

Original 30 Closed Disclosure source IDs and original 15 Closed Removable source IDs were retained **in place** inside the canonical Component Sets. The 45 historical `Open=True` components were **not deleted**: they were moved to an isolated `__Legacy Chip Open=True variants · retained for linked instances` frame, node `24080:308`, preserving their component IDs and existing external linked references. Treat this as compatibility-only, not a new public variant matrix. Local known Chip page and Anchored Disclosure Pattern examples were migrated to canonical components.

## Figma implementation

### Disclosure

- Two private sets: `__Chip Chevron / Neutral`, node `24077:128087`, and `__Chip Chevron / Accent`, node `24077:128094`.
- Each has **two direction variants**: `Open=false` (down) and `Open=true` (up), with original semantic Chevron foreground colors.
- Every one of the 30 canonical Disclosure components embeds an **exposed nested instance** `Chevron / Open`, with the correct Neutral/Accent helper for its Applied condition.
- Designers control only the **nested Open direction** on the Chip Instance. The canonical Chip's own Variant axes remain Size, Applied and State. No Chip background, border or focus property is controlled by nested Open.
- The direction helper is `18px`, matching the existing Chevron layout footprint. When `State=Disabled`, runtime must prevent the popup opening; no user-visible expanded-state behavior should occur.
- The opened Industry and custom Popover Figma examples now use original linked Chip component IDs plus nested `Chevron / Open=true`; no active/open background change.

### Removable

- No `Open` property in Figma, because **Open/Closed look identical**.
- A new Auto Layout `Body / action target` is a sibling of the existing nested `Remove action` in each of 15 canonical Removable variants, not a nested button.
- Body gets independent Hover/Active/Focus, whereas Remove retains its own hover/focus/disabled state. In source Focus variants the shared `Focus/Default` effect is on Body, not the entire compound root.
- Original `Label`, `Detail`, divider, Show detail and Leading visual child node identities/property references are retained after reparenting. The root remains 28 / 32 / 40px tall, and its width HUG behavior is preserved.
- Runtime can set `aria-expanded` on the actionable body when it opens an editor without introducing new Figma visual variants. The Remove control only removes.

### Presentation

- Canonical [Chip Figma page](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23900-128061) shows the 30/15 matrices and corrected axes/property descriptions.
- Held [Disclosure Pattern Figma examples](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23945-788) have been reconciled visually, but the separate Disclosure Pattern remains on Hold.

## Chevron color regression correction — 2026-10-17

The post-simplification audit identified **6 mismatches** (3 sizes × Applied false/true) in `State=Disabled`: the neutral/accent nested Chevron helper retained `fg/secondary` or `fg/accent`, while the adjacent Label used `fg/disabled`.

**Fix in canonical Figma:** added `__Chip Chevron / Disabled` (`24087:577`), with closed/up direction variants bound to `fg/disabled` (`VariableID:16871:59440`). Swapped the six Disabled original Disclosure components to this helper **in place**, preserving their IDs and the publicly exposed nested Open control. Neutral and Accent helpers were retained for enabled states.

**Regression:** 30 canonical Disclosure variants × 2 Chevron directions = **60/60 PASS** for icon type, icon semantic color == Label semantic color, and unchanged Chip width/height. Applied false/true, Default/Hover/Active/Focus/Disabled, all three sizes included. Playground **5/5 PASS** and linked Disclosure Pattern **6/6 PASS** for icon/Label token equality; archived older Disabled variant colors **6/6 already correct**. Disabled helper both directions are bound to semantic color (including themes), not a literal RGB.

## Verified QA

| Test | Result |
|---|---|
| Every Disclosure variant has exposed Chevron Open nested instance | **PASS — 30/30** |
| Toggle nested Open false→true changes glyph down→up | **PASS — 30/30** |
| Toggle nested Open does **not** change Chip fills, height or width | **PASS — 30/30** |
| All Removable variants have independent Body and Remove with valid summed width | **PASS — 15/15** |
| Removable dimensions unchanged from original state specimens | **PASS — 15/15** |
| Removable Body Focus vs Remove Focus remain independent | **PASS** |
| Disclosure nested Chevron Open survives Size Medium→Small→Extra Small and State Default→Hover→Focus with custom label and Applied=true | **PASS** |
| Removable Label/Detail overrides survive Size/State changes; Remove Focus independent from Body Focus | **PASS** |
| Canonical published component set identities retained | **PASS** |
| Historical Open=True source identities archived rather than destroyed | **PASS — 45/45** |
| Light/Dark source semantic variable tokens inherited | **PASS (structural)** — runtime visual regression still required |
| Rendered canonical Chip and linked Pattern previews | **PASS (Figma visual)** |

## Outstanding production checks and caveats

1. **External consumer migration:** archival source identities avoid deleting historical variant sources, but consumers outside this file have **not been exhaustively scanned**. Identify any external `Open=True` instances before deprecating/removing archive. Do not assume automatic remapping to nested Chevron.
2. **Keyboard and ARIA:** Android/web/Angular runtime DOM must implement appropriate trigger/expanded semantics and non-nested Body/Remove actions. Figma visuals cannot certify accessibility or keyboard event handling.
3. **Chevron Open on disabled:** Figma exposed nested direction can technically be overridden independently. Runtime must enforce `open=false` when disabled.
4. **No extra Open state in Removable:** the popup/owner state remains runtime-only; changing open does not force Focus/Active.
5. **Themes/RTL:** canonical variable links, RTL anatomy and Figma previews remain intact; run light/dark Storybook, keyboard, touch targets, long mixed Persian/Latin labels, theme regressions.
6. **Archival housekeeping:** 45 legacy source nodes remain separately in the Figma file by design. They must not be used for new screens.

**Readiness:** Canonical design and handoff **Ready for Sandbox**. Angular/Storybook/production release is **not** certified. This audit supersedes [earlier full-Open-axis report](chip-final-2026-10-17.md).
