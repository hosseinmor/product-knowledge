---
id: design-system.audit.data-table-token-compliance-2026-10-20
collection: design-system
type: audit
title: Data Table Token Compliance and Nested Instance Provenance — 2026-10-20
summary: Resolves the prior 110 apparent nested spacing violations as inactive Icon Button gaps, verifies all ten canonical Data Table sources and their semantic roles without Figma edits.
knowledge_state: verified
document_maturity: reviewed
design_status: figma-source-token-qa-complete
owner: Design System team
last_reviewed: '2026-10-20'
related:
  - design-system.component.table
  - design-system.reference.figma-token-compliance
---

# Data Table — Token Compliance and Nested Instance Provenance

Source: [Data Table / Documentation · canonical sources](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23835-127556), page `24:0`. This read-only follow-up closes **TC-04** from the [cross-component audit](component-token-compliance-2026-10-19.md).

## Background

An earlier broad traversal noted **110 positive raw spacing observations under nested instances**, after the first in-place Data Table spacing migration (162 shared-scale binding assignments recorded in the main audit). Those 110 observations were not yet assigned to upstream sources or assessed for whether they affected layout. The canonical source audit now distinguishes (1) owning source layers, (2) inherited instance descendants, and (3) positive but **inert** spacing.

**No new Data Table source mutations were made during this follow-up.**

## Root-cause resolution: all 110 belong to a one-child Icon Button wrapper

Every one of the 110 residual raw properties is:

- `itemSpacing=8px`, inside a **`Start Icon` Frame**;
- that Frame has **exactly one direct child** and is not a wrapping multi-child layout;
- the Frame is inherited from **Icon Button** (typically Ghost / Extra Small, including Sort, Disclosure and row Actions), not owned by a Table Cell/Row;
- there is therefore **no second child for the gap to separate**. The gap does not affect the position, visual appearance or hit target of the Button icon.

The same upstream Icon Button wrapper occurs repeatedly across nested Table sources; these are **observations per nested occurrence, not 110 distinct authored Button masters**.

| Table source in which inherited instances were observed | Inactive `Start Icon/itemSpacing=8px` observations |
|---|---:|
| Data Table / Default | 42 |
| Data Table Header Cell / Default | 3 |
| Data Table Row / Default | 39 |
| Data Table Row Item / Default | 24 |
| Data Table Disclosure / Default | 2 |
| **Total** | **110** |

This is consistent with the independent [Button Spacing Audit](button-spacing-2026-10-20.md), which documents one-child icon-wrapper Gap as structurally inert. **Do not change the nested instances**, detach them, create 110 redundant variable binds or mark Table Source as failing merely because those raw values exist. If Icon Button's `Start Icon` Frame later gains two or more direct children, the upstream source must be re-audited.

All other **effective** nonzero spacing properties in the traversed canonical Table source and borrowed instance descendants were bound to Spacing variables at the time of this follow-up.

## Final mechanical audit — ten canonical master sources

Read-only `figma-token-compliance-audit.js` invoked on the Data Table page with an **explicit 10-master whitelist**, excluding Figma Component Set presentation-only geometry and borrowed Instance wrappers.

| Direct-owned-source check | Result |
|---|---:|
| Canonical master sets/components audited | **10** |
| Owned source layers (excluding borrowed instances) | **146** |
| Effective positive Spacing properties | **94/94 bound** |
| Nonzero shared-scale Spacing missing variable | **0** |
| Owned Text layers using Text Styles | **13/13** |
| Visible SOLID fills/strokes bound to public `03 Semantic` | **50/50** |
| Raw Color, private/primitive Color, legacy Paint Style | **0** |
| Positive Radius needing a binding | **0** (Table's source containers are intentionally square) |
| Inherited non-bound **active** shared-scale spacing observations | **0** |
| Inherited non-bound **inactive** one-child Icon Button gaps | **110** |
| Source changes made during this follow-up | **0** |

Direct-owned source counts deliberately do not include Text Styles, Color paints or Spacing inherited from nested **Checkbox, Icon Button, Tag, Row, Header Row, Cell, Content, or other reusable instances**. Those are audited at their own source. No new Radius token was necessary: the Table Shell, Rows and Cells intentionally have zero corner radius. The table may appear inside a separate Card surface when framing is required.

## Semantic Color and typography review

| Anatomy | Existing public token/style | Assessment |
|---|---|---|
| Table shell | `surface/default` | Appropriate neutral content surface |
| Header Row | `surface/muted`, 1px Divider via `line/muted` | Appropriate passive header and divider |
| Header Cell label | `Label/SM` + `fg/secondary` | Correct header information hierarchy |
| Row Default/Hover | `surface/default` / `surface/transparent-hover` | Appropriate row interaction states |
| Row Selected/Selected Hover | `surface/selected` / `surface/selected-hover` | Correct selection state roles |
| Row separator | `line/muted` | Appropriate structural border |
| Cell plain text | `Body/Compact/SM` + `fg/primary` | Correct data reading role |
| Text + Description | `Body/Compact/SM` + `Body/Compact/XS`, `fg/primary` / `fg/secondary` | Appropriate readable hierarchy |
| Expanded Content | `surface/muted`, `Label/SM`, `Body/Compact/SM` | Appropriate passive detail view |

The row/header Divider is a 1px absolutely positioned geometric line currently expressed with a `line/muted`-colored rectangle Fill in the authored Figma source; **token meaning is correct**, but the visual/implementation technique remains separate from the Progress Bar's bottom-only Stroke recipe. Do not convert the divider indiscriminately, risking dynamic row-height alignment, merely because Progress Bar paths use Stroke.

## Source structure and visual evidence

Validated stable canonical sets/masters, including:

- Table `23524:15759`: **6** Size × Selection variants.
- Header Row `23523:14084`: **3** variants.
- Header Cell `23514:13393`: **4** Sort variants.
- Cell `23514:13381`: **3** sizes.
- Row `23522:14296`: **12** Size × State variants.
- Row Item `23600:127401`: **6** Size × Expanded variants.
- Text Content `23618:15999`: **2** Overflow variants.
- Text + Description `23577:15033`, Disclosure `23522:13764` (2 variants), Expanded Content `23526:15123`.

Representative screenshots were inspected: normal Medium Table, Multiple Selection with indeterminate Header selection, a Selected Row, and an Expanded Row Item. The source matrix continues to show 32/40/48px single-line Row and Header heights; the cell content and expanded row examples preserve their documented composition. This does not substitute for an automated visual-diff test or a live browser test.

## Remaining acceptance outside token-binding QA

- Confirm RTL column alignment, horizontal overflow at constrained widths, dynamic two-line row heights and bottom Divider anchoring in actual Angular/Storybook.
- Verify accessible native Table semantics, sortable Header controls, partial selection, action-button labels, row expansion, and keyboard/AT interaction using the [Table Runtime Contract](../components/table-runtime-contract.md).
- Check Product × Appearance visual/contrast combinations and real published Figma Slot/instance overrides after Foundation migrations.
- Manage old archived Carbon Data Table sources under their own compatibility/migration workflow; do not reclassify archives as current source violations.

**Decision:** **TC-04 resolved, no Table-side or Icon Button-side Figma edits needed**. The 110 raw observations are legitimate, inactive presentation properties inherited from a known upstream single-child Icon Button wrapper. Keep the rule documented and re-audit if that wrapper anatomy changes.

**Exclusion:** Image Uploader is not part of this audit and was not touched.
