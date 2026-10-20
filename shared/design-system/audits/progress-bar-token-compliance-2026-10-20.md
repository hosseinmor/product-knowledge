---
id: design-system.audit.progress-bar-token-compliance-2026-10-20
collection: design-system
type: audit
title: Progress Bar Token Compliance — 2026-10-20
summary: Verifies semantic line-stroke construction and canonical typography; binds shared Spacing and corrects Success text foreground.
knowledge_state: verified
document_maturity: reviewed
design_status: figma-source-token-qa-complete
owner: Design System team
last_reviewed: '2026-10-20'
related:
  - design-system.component.progress-bar
  - design-system.component.progress-circle
  - design-system.reference.figma-token-compliance
---

# Progress Bar Token Compliance — 2026-10-20

Source: [Progress bar Figma page](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=8930-400384). Canonical master identifiers, original keys and variant axes retained:

| Canonical source | Node ID | Component key | Variants |
|---|---|---|---:|
| Public Progress bar | `12603:272925` | `1d9983588bb228a44ca2b3af89195bd1e2b51c9d` | **30** |
| Internal _Progress bar track item | `12603:273022` | `b765a10f45d8d3ad69489a266bc6e623ba94d5b1` | **16** |

This audit includes **owned source layers only**. Source-linked track instances are not counted again as owned public Color/Spacing choices, and the parent Component Set's canvas presentation Stroke Style is not a product component decision. Indeterminate remains a static Figma reference for runtime animation.

## Changes applied in Figma

### 46 new canonical Spacing bindings

All affected values were already on the shared scale and were rebound **without numeric changes**:

| Role | Properties | Existing value |
|---|---:|---|
| Public parent variant `itemSpacing` — Default/Indent | 22 | 8px |
| Public parent variant `itemSpacing` — Inline | 8 | 16px |
| `Label + Icon` internal `itemSpacing` — Success/Error | 4 | 16px |
| `Label` internal frame `paddingRight` — Indent | 6 | 16px |
| `Helper text` internal frame `paddingRight` — Indent | 6 | 16px |
| **Total** | **46** | |

All 30 public variants and all 16 internal Track variants kept their source IDs/keys and their exact recorded layer widths/heights, including active 100% and indeterminate snapshots. No component, axis, value or content property was regenerated.

### Success message Color correction

Two `Success message text` source layers (Small and Big Default) previously consumed `fg/secondary`, although the Progress Bar guideline explicitly requires `fg/success` for result text. Both were rebound to public **`fg/success`**. Existing typography remains **Body/Compact/XS** (12px/16px Regular) and the Icon/Track continue to use Success roles. Error message text was already on `fg/error` and was left intact.

Resolved Figma alias graphs for JobVision and Cando on `surface/default`:

| Text role | Light contrast | Dark contrast |
|---|---:|---:|
| `fg/success` | 5.02:1 | 6.98:1 |
| `fg/error` | 6.29:1 | 5.91:1 |

These calculated ratios exceed 4.5:1 for ordinary-size text. They do **not** certify arbitrary product backgrounds, browser-rendered visuals or assistive-technology behavior.

## Stroke and state architecture verified unchanged

The **16** internal Track variants have **44 semantic Stroke paints**; no visible Fill-based progress path, non-semantic Stroke color or incorrectly aligned/bottom-weighted line was observed.

| Stroke role | Occurrences | Token |
|---|---:|---|
| Neutral Track | 16 | `line/default` |
| Active path (including 100%, static Indeterminate) | 18 | `line/accent` |
| Settled Success path | 5 | `line/success` |
| Settled Error path | 5 | `line/error` |
| **Total** | **44** | |

Every Track/segment uses bottom-only **inside Stroke** (`strokeTopWeight=0`, `strokeRightWeight=0`, `strokeLeftWeight=0`), with **4px** for Small and **8px** for Big. Progress segment colors and shape already matched the shared Progress Circle roles. **No Track geometry or color role was changed.** Retain square ends and correct RTL progress direction.

## Final structural read-only QA

| Check | Result |
|---|---|
| Public variants | **30/30** retained |
| Internal Track variants | **16/16** retained |
| Nonzero effective public Spacing properties bound | **46/46** |
| Public owned Text layers with Text Styles | **52/52** |
| Internal Stroke paints using approved `line/*` roles | **44/44** |
| Stroke bottom thickness/alignment mismatches | **0** |
| Public Success message text using `fg/success` | **2/2** |
| Public Error message text using `fg/error` | **2/2** |
| Unresolved Color bindings on public owned layers | **0** |
| Detected source layer geometry changes during binding | **0** |

Source screenshots sampled before and after for Active 50%, Indeterminate, Success, Error and Indent. Sampled source sizes remain 220×56, 220×60 and 220×56 for Default Small, Indent Big and active/error examples respectively; Inline source height remains 20px.

### Presentation-only Paint Style exclusion

The two source Component Set wrappers carry an old canvas-level Stroke/Paint Style for the Figma variant grid; they are **not renderable instance geometry**. They must not be treated as canonical component Stroke or as a reason to replace the real Track's `line/*` bindings. The generic read-only audit should exclude **Component Set wrapper paints** from product source-color counts, just as it excludes matrix spacing and wrapper radii.

## Limitations and follow-up

- **Design-source token compliance is complete** for the inspected public/Track masters. No new token or API is needed.
- Full JobVision/Cando × Light/Dark screenshot matrix, RTL and long/mixed-script runtime QA, published-instance override compatibility, and browser-accessibility verification are not yet certified.
- Figma Indeterminate remains a **static visual reference**. Actual moving segment, reduced-motion fallback and truthful accessible progress semantics are runtime work.
- The Figma percentage presets are **illustrative snapshots**, not an arbitrary numeric value API. Do not reinterpret them as runtime numeric support.
- Legacy presentation resources outside the two source masters and the **Image Uploader** were not touched.

**Status:** Progress Bar canonical Spacing, semantic Stroke, Typography and outcome Text Color source checks pass. Runtime/consumer signoff is a separate gate.
