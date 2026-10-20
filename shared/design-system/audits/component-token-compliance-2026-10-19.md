---
id: design-system.audit.component-token-compliance-2026-10-19
collection: design-system
type: audit
title: Figma Component Token Compliance Audit — 2026-10-19
summary: Baseline of cross-component token bindings and first in-place remediations; remaining migration and runtime QA.
knowledge_state: verified
document_maturity: draft
design_status: in-progress
owner: Design System team
last_reviewed: '2026-10-19'
---

# Figma Component Token Compliance Audit — 2026-10-19

## Scope and measurement boundary

Live source: [Job Vision NEXT Figma](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT). Baseline survey: 62 component/pattern-related pages, 58 with at least one master component. This included some legacy, archived and borrowed instance content. These are **discovery totals**, not a canonical compliance percentage. Direct-owned master-layer counters and nested instance counters must stay separate. Visual semantic correctness, Product x Appearance contrast and runtime implementation have **not** been fully audited.

The applicable contract is [Figma Component Token Compliance](../integrations/figma-token-compliance.md).

## Completed changes — Figma authoring source

| Location | Change | Result / validation |
|---|---|---|
| Radius collection | Hide five Deprecated variables from publishing/selection; keep IDs and numeric values intact | hiddenFromPublishing=true, scopes=[] for 6px Control, 12px Surface, Legacy 12px, 20px Large surface, 8px Group |
| Toggle | Rebind all unstyled 14px/20px regular labels to Body/Compact/SM | 24 source node IDs changed; 24/24 subsequently confirmed styled |
| Select required markers | Bind existing 14px/20px Regular Mandatory stars in both sets to visually identical Body/Compact/SM Text Style | 108 layers; 54 Single + 54 Multiple, checked after write |
| Shared Field Label | Bind required star to same 14px/20px Regular Body/Compact/SM recipe | 1 source node in _Field Label; existing fg/error unchanged |
| Dialog / Default | Change private 02 Product semantic/* bindings to public 03 Semantic roles | 19 direct source bindings changed |
| Alert Dialog / Default | Change private color bindings to public semantic roles | 4 bindings changed |
| Confirmation Dialog / Default | Change private color bindings to public semantic roles | 4 bindings changed |
| Dialog Close Button / Default | Update public fg/primary and fg/disabled fills inside five source icon instances | 5 more nested icon paint bindings changed |
| Select / Single + Multiple + Selection Panel + Option + Select All | Replace deprecated 6px Control corner aliases with 6px Medium and bind the 12px Selection Panel source layers to 12px Large | 544 old corner bindings migrated; 12 panel source layers bound; 148 source node IDs affected; follow-up read found 0 deprecated bindings across the scanned Select masters and their instances |
| Data Table source masters | Replace eligible non-zero raw spacing values with existing Spacing variables, without changing geometry | 162 bindings on 60 owned nodes, values: 2/4/8/12/16/24/96px; after scan: 0 remaining raw owned layout props; 110 raw observations still inherited inside nested instances |

No canonical public component set was recreated or detached. Publication/consumer and runtime regression tests remain to be performed.

See also the [2026-10-20 File Uploader migration audit](file-uploader-token-migration-2026-10-20.md): first 147 Foundation bindings corrected, then 18 File Item surfaces, 72 radius corners, one shared Focus treatment and 6 Dark-contrast error-text roles. Structural token QA passed; actual Focus render/keyboard, Theme matrix and published-instance QA remain open.

**Chip follow-up (2026-10-20):** canonical Selectable, Removable, Disclosure and Action are structurally compliant for active owned-source Spacing (315/315), Text Styles (180/180), Full radius (90/90) and public Semantic Color paints (378/378). Nine obsolete selected-disabled Color bindings were corrected in place; Dark appearance is intentionally different. See [dedicated Chip audit](chip-token-compliance-2026-10-20.md). The legacy Open=True linked-component archive was not modified.

## Open discrepancy register

| ID | Priority | Finding | Disposition |
|---|---|---|---|
| TC-01 | P1 | Dialog private semantic collection | Source and Close Button corrected; post-read found **0** residual private semantic/* bindings across scanned Dialog masters and nested instances; Product x Appearance still open |
| TC-02 | P1 | Select Deprecated radius source | Rebound in place; test published overrides, all error/focus/open variants and responsive layout |
| TC-03 | P1/P2 | Select missing Text Styles in required markers, Option metadata/secondary content and Panel title | **Resolved at canonical source:** 108 Mandatory + 1 shared Field Label, then 16 Option metadata → Label/XS, 16 Option secondary → Body/Compact/XS, 12 Selection Panel titles → Heading/SM. The inspected masters now have **0 unstyled owned Text layers**. **Open:** visible metadata/secondary Playground example and mixed-script, long-content visual QA. |
| TC-04 | P2 | Data Table raw shared spacing | Owned master source corrected; investigate 110 nested-instance inherited raw observations upstream |
| TC-05 | P1/P2 | File Uploader semantic roles, legacy styling and separate Image Uploader | **Resolved in Figma:** 131 Spacing, 16 Dropzone Large Radius corners, 72 File Item Medium Radius corners, 18 passive surface/muted fills, 6 readable error-text semantic fills, and shared Focus/Default on Dropzone. **Remaining:** verify Focus ring visually/keyboard and on muted Dark backdrop, review all Product × Appearance and published overrides, preserve local optical values; separately audit image uploader. [Details](file-uploader-token-migration-2026-10-20.md) |
| TC-06 | P2 | Button, Chip, Progress Bar and other input families: correct shared spacing numbers without bindings | **Button resolved:** 808 new bindings → 960/960 effective Spacing; **Chip resolved:** 45 new bindings → 315/315 effective Spacing across four canonical sets, and 9 retired selected-disabled surface aliases replaced with surface/disabled. [Button](button-spacing-2026-10-20.md) / [Chip](chip-token-compliance-2026-10-20.md). **Open:** Progress Bar and other source migrations; review transparency styles, published overrides and Product × Appearance. |
| TC-07 | P2 | Autocomplete Selection Panel open instances initially displayed raw 12px radius | **Resolved by inheritance:** 24/24 Autocomplete / Open panels now bound to 12px Large |
| TC-08 | P1 migration | Number Input and Date Picker (already tracked in HOS-48/49), Pagination, Structured List, UI Shell, Slider and other legacy assets | Compatibility migration; no indiscriminate palette/radius replacement |
| TC-09 | P2 | Typography guideline pointed to obsolete 02 Brand variable name | Correct to 02 Product / typography/font-family in governance branch |
| TC-10 | QA | Semantic meaning, Light/Dark, JobVision/Cando, contrast and runtime accessibility cannot be certified by an automated scan | Open manual and runtime acceptance gate |

## Approved exceptions

- Toggle white Thumb: fixed Primitive palette/bw/white is explicitly approved.
- Chip current radius is Full under its present documented family decision.
- Content Switcher Track 8px is component-local; its Item radius uses 6px Medium.
- Local optical spacing may be raw with documented justification; do not confuse construction geometry with shared layout spacing.
- Tag categorical tokens belong to Tag. An inserted Tag in a Slot does not license the use of tag/* for a non-Tag element.

## Root cause and governance control

- **Deprecated discoverability:** old Radius variables were still selectable; now hidden but retained for existing consumers.
- **Binding not checked:** visual/numeric correctness allowed raw values to survive. A new Figma QA gate requires authored binding evidence.
- **Public/private alias confusion:** the internal 02 Product semantic/* router was used directly by Dialog variants. The documented 03 Semantic API is now mandatory.
- **Legacy overlap:** historical components, variants and nested instances polluted raw counts. Future reports distinguish direct source nodes, borrowed instances and migration references.
- **Stale docs:** Typography reference had an outdated variable name; updated separately in this branch.

## Acceptance sequence

1. Inspect meaningful states (including error + focus, open/popup and disabled), visual appearance and source node IDs after rebinding.
2. Check JobVision x Cando and Light x Dark for color role, contrast, visual equivalence and font identity.
3. Regression-test Select published property overrides, Dialog Close Button icon overrides, and Data Table nested source instances.
4. Audit remaining canonical masters before their next handoff; migrate legacy without breaking live consumers.
5. Validate runtime behavior and accessibility only after owning Angular/Storybook sources are registered.

**Status:** Stage 1 governance and targeted authoring corrections underway; this report is not final signoff.