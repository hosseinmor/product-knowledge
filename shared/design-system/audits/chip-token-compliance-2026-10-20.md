---
id: design-system.audit.chip-token-compliance-2026-10-20
collection: design-system
type: audit
title: Chip Token Compliance — 2026-10-20
summary: Corrects canonical Removable spacing bindings and obsolete Disabled surface references across four Chip component families.
knowledge_state: verified
document_maturity: reviewed
design_status: figma-source-token-qa-complete
owner: Design System team
last_reviewed: '2026-10-20'
related:
  - design-system.component.chip
  - design-system.reference.figma-token-compliance
---

# Chip Token Compliance — 2026-10-20

Live source: [JobVision NEXT Figma — Chip](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=13500-300199). This audit intentionally covers four **canonical public component sets and their owned source layers only**, excluding Playground, inherited/nested instances, the private Chevron helper, and \`__Legacy Chip Open=True variants\` retained for linked instances. It does not migrate old detached consumer references.

## Canonical master inventory and source validation

| Source | Stable node ID | Variants | Effective owned Spacing bindings after |
|---|---|---:|---:|
| Chip / Selectable | 20783:128158 | 30 | 90/90 |
| Chip / Removable | 23124:358 | 15 | 60/60 |
| Chip / Disclosure | 20783:534 | 30 | 120/120 |
| Chip / Action | 23123:125056 | 15 | 45/45 |
| **Total** | | **90** | **315/315** |

The current \`Radius / Full\` recipe is explicitly approved in chip.md; no 6px Medium migration was attempted. The existing sizes **Extra Small 28px**, **Small 32px** and **Medium 40px** were verified across all state variants. Canonical source text-style references and public Semantic Color references were inspected and preserved. No variant count, component key, API axis, content property, or authoring Slot was recreated.

## 45 Spacing bindings migrated in place

Only **Chip / Removable** had unbound effective scale spacing in its owned source. Its 15 \`Body / Edit action target\` frames previously used correct numeric values without bindings:

| Property | Changed bindings | Existing geometry |
|---|---:|---|
| paddingRight | 15 | 8px Extra Small, 12px Small, 16px Medium |
| paddingLeft | 15 | 8px |
| itemSpacing | 15 | 8px |
| **Total** | **45** | Unchanged |

Each Body frame has three direct children; unlike a one-child icon wrapper, its \`itemSpacing\` is effective. The body remains independently actionable from the trailing \`__Chip Remove Action\`. The latter, its hover/focus target and compound-control contract were **not** changed. All 15 source body frames kept their width and height. Source binding validation passed with zero failures.

## Nine obsolete Disabled surface bindings corrected

A separate Color inspection found that nine Disabled variants still referenced \`surface/surface-selected-disabled\` in the public 03 Semantic collection, an obsolete role **not in the current Token Usage Rules**. It appeared in three sizes for each of:

- Selectable / Selected=true / Disabled;
- Removable / Disabled;
- Disclosure / Applied=true / Disabled.

All nine source root fills now consume the current public **\`surface/disabled\`** variable; Action had no such obsolete reference. **This intentionally changes the Disabled fill appearance**, unlike the spacing-only bindings.

The old role resolved to approximately #EBEBEB in both Light and Dark. By contrast, current \`surface/disabled\` resolves to approximately #F2F2F2 in Light and #3F3F3F in Dark for both JobVision and Cando. Thus the legacy role was specifically wrong in Dark, in addition to violating naming/usage policy. The legacy variable itself was **not deleted or redefined**, since other consumers may depend on it.

## Final mechanical QA

Post-change direct-source scan, borrowed instance wrappers excluded:

| Category | Verified count |
|---|---:|
| Effective shared Spacing properties bound | **315/315** |
| Canonical variant heights, 28/32/40px | **90/90** |
| Positive Radius properties bound to Full | **90/90** |
| Text layers with Text Styles | **180/180** |
| Solid visible fills/strokes bound to public 03 Semantic | **378/378** |
| Remaining obsolete selected-disabled root fill references | **0** |
| Unbound effective scale Spacing properties | **0** |

Reviewed visual snapshots before/after of canonical Removable Small and Medium Body, and Disabled Selectable/Removable examples; source widths/heights and component keys stayed unchanged. Actual visual review across all **JobVision/Cando × Light/Dark** and full runtime behavior is not claimed.

### Open work not conflated with this audit

- Run appearance/contrast, hover, active, focus, selection, disabled and RTL composition tests in the actual editor and runtime.
- Preserve the separate keyboard/focus targets of Removable Body and Remove in implementation.
- \`__Legacy Chip Open=True variants\` remain retained for existing linked instances, untouched; they must be managed through an explicit compatibility plan.
- Do not modify File/Image Uploader as part of Chip remediation. In particular, **Image Uploader is explicitly out of scope**.

**Status:** canonical four Chip component sets pass owned-source mechanical Color/Spacing/Typography/Radius checks. Consumer/runtime and four-mode visual QA remain separate acceptance activities.