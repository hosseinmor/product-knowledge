---
id: design-system.audit.file-uploader-token-migration-2026-10-20
collection: design-system
type: audit
title: File Uploader — Token Migration Audit (HOS-39)
summary: Canonical Carbon File Uploader foundation and semantic token changes implemented in Figma; focus and runtime QA remain.
knowledge_state: verified
document_maturity: reviewed
design_status: figma-semantic-fixes-applied-runtime-qa-open
owner: Design System team
last_reviewed: '2026-10-20'
related:
  - design-system.component.file-uploader
  - design-system.reference.figma-token-compliance
---

# File Uploader Token Migration — 2026-10-20

## Source and scope

Source file: [JobVision NEXT / File uploader](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24020-785).

The original Carbon master, **not** the archived pilot, is the currently documented v1 File Uploader source. Four component masters are in this migration:

| Canonical master | Node ID | Stable key | Variants |
|---|---|---|---:|
| File uploader (public) | 5465:294860 | 550906ded6eb1a21c6e467a1cd16c372fc801e5e | 15 |
| _File uploader file item | 3199:35182 | d86837858cc4bacfc082e4a169868be548b3c83a | 18 |
| _File uploader - Drag and drop box states | 3183:29103 | ccd8c2385525cc058899057b741a9be85332cf3a | 4 |
| _File uploader file list item | 4188:102462 | 6bded647d4ceb35c9a692a0f835ed753cb343247 | 1 |

The separately located **image uploader**, master 19337:1420, key 3634f336f7fbb8a85cba95f1c555a2d72f23b648, **9 variants**, is an adjacent component, not one of these canonical File Uploader sources; it needs its **own** owner/purpose and token migration plan. Its historical/raw dependencies were explicitly **not** edited as part of this File Uploader pass. Similarly, archived pilot 23907:394 is out of scope.

The public 15 variants, internal 18 file-item variants, 4 Dropzone states, File list Slot ID 24003:831 with 3 connected example items, and all source identities were preserved. No instances were detached, no new component variants were introduced and no workflow/API change is implied.

## Completed in-place binding migration

| Source | Shared Spacing bindings added | Radius bindings corrected |
|---|---:|---:|
| Public File uploader | 27 | 0 |
| File Item | 102 | 0 |
| Dropzone States | 0 | **16 corners** (4 components × 4 corners): Deprecated 12px Surface → 12px Large |
| File list source + native Slot | 2 | 0 |
| **Total** | **131** | **16** |

**147 property bindings** were updated on **75 unique source layers**. Original spacing/radius numbers were preserved; the migration did not regenerate the 15/18/4/1 component sets. The 12px target value equals the deprecated source value. Exact canonical scale values used in File Item include 2/8/12/16px; 7/11/15px optical padding was intentionally left local. Dropzone base 10px and 50px geometry was intentionally left unchanged and is a documented local-layout review candidate.

**Color:** Dropzone Disabled helper text, node 11348:324933, previously used an unresolved legacy external color VariableID 16871:59467. It was rebound to the public **fg/disabled**, consistent with the public File Uploader Disabled label/description. This was an intentional semantic foreground fix; unlike numeric rebinding, the visually resolved text color can change.

**Post-scan of owned nodes:**

| Component | Shared scale values left unbound | Deprecated radius left | Raw radius left | Unstyled product text |
|---|---:|---:|---:|---:|
| File uploader | 0 | 0 | 0 | 0 |
| File Item | 0 | 0 | **0 after semantic follow-up** (18 old 4px variants migrated to Medium 6px) | 0 |
| Dropzone States | 0 | 0 | 0 | 0 |
| File list | 0 | 0 | 0 | 0 |

The Dropzone master contains 8 non-scale optical padding observations (10px/50px). The File Item has 36 non-scale observations (7px/11px/15px). Component Set presentation layout properties were excluded from canonical component geometry counts. Borrowed nested instances were not double-counted as owned source properties.

## Semantic decisions and follow-up fixes — 2026-10-20

The original 147 bindings were value-preserving Foundation cleanup. The following changes are a **subsequent intentional semantic and visual refinement**, not part of those 147:

| Finding | Source modification | Result |
|---|---|---|
| FU-01 File Item passive surface | 18 File Item variant fills: surface/neutral-muted → **surface/muted** | 18/18 bound to public semantic token |
| FU-02 Dropzone Focus | Variant 3183:29118: 2px line/accent → **1px line/emphasis**; shared **Focus/Default** Effect Style added | Two effect layers bind focus/default (outside ring) and surface/default (1px gap); identical Effect Style ID to canonical Text Input |
| FU-03 File Item corner Radius | 18 variants × 4 corners: 4px raw → **6px Medium** | **72/72** canonical corner bindings, 18/18 component widths/heights retained |
| FU-07 Error text contrast | 3 Error short text layers → **fg/primary**; 3 Error long descriptions → **fg/secondary** | 6/6 roles rebound; icon and border keep Error semantics |

**FU-04 optical padding still local:** File Item 7/11/15px vertical padding and Dropzone 10/50px construction offsets remain intentionally outside the shared spacing scale pending component-height/optical review.

**FU-05 legacy Paint Styles pending:** Transparent/Transparent is currently a white Multiply paint and must not be replaced by an opaque color without appearance review. Existing icon Accessibility/White is inherited from another source. These are tracked migration debts.

**FU-06 image uploader separately scoped:** nine Image Uploader variants still have deprecated Radius, raw spacing and unresolved colors; no edits were made to that neighboring component.

### Theme, contrast and focus QA

Resolved actual Figma token alias graph across **JobVision × Light, JobVision × Dark, Cando × Light, Cando × Dark**; both Products currently yield the same evaluated numeric contrasts:

| Foreground versus File Item surface/muted | Light | Dark |
|---|---:|---:|
| fg/primary normal text | 18.48:1 | 8.83:1 |
| fg/secondary normal text | 7.41:1 | 5.85:1 |
| fg/error icon (non-text) | 5.87:1 | 3.91:1 |

The original 12px fg/error explanatory text would have had **3.91:1 in Dark**, below the standard 4.5:1 normal-text ratio. The new text styles exceed 4.5:1. The status icon exceeds 3:1. The text styles and content characters were not changed.

**Focus/default contrast:** on surface/default, **4.59:1 Light / 4.31:1 Dark**. On surface/muted, **4.29:1 Light / 2.85:1 Dark**, so the shared ring needs contextual contrast evaluation if the Dropzone is placed on a muted dark background. The intended normal backdrop is surface/default.

The Dropzone Focus has the same Figma Effect Style as canonical Text Input Control 22780:357. The screenshot renderer did not visibly draw the bound focus-shadow ring on **either** reference; this prevents screenshot-based certification of its visual outline. The style has two active effects and the correct colors/spreads in Figma source. **Do not infer real editor/browser focus visibility or keyboard access from that source evidence alone.** No additional custom ring was added to sidestep this renderer limitation.

## Visual and structural checks

- Before and after screenshots of representative public enabled Drag and drop (node 5465:297738): **289 × 290px**, unchanged after numeric rebinding.
- Before and after Dropzone Drag + Hover: **288 × 100px**, original 12px geometry retained.
- Before and after File Item Error long: **288 × 96px**, original 4px corners and 2px line/error retained.
- Additional post-change screenshot: Dropzone Disabled, helper text visually legible after binding to fg/disabled.
- Property-level verification: 147/147 numeric bindings retained original values; **zero binding failures**.
- Component Set counts verified: 15/18/4 and File list Slot one with three connected example Item instances.

These are Figma source and screenshot checks. **No actual browser upload, screen-reader, Storybook, Product x Appearance matrix or published consumer override test has been certified.**

## Root-cause diagnosis

1. The original Carbon implementation predates the simplified Radius and Spacing Foundations; visual compatibility was prioritized without a recorded token-migration inventory.
2. Local geometry and shared scale spacing were mixed as raw numbers. The lack of a binding-specific gate allowed the correct numbers to remain detached.
3. The File Uploader page contains two different product concepts (File Uploader and image uploader), plus an archived pilot; page-wide checks inflated findings and confused ownership.
4. Color role and focus semantics are not reducible to token binding checks: a bound surface/neutral-muted can still violate passive-vs-interactive meaning; an Accent border is not necessarily the required Focus indicator.
5. External/legacy text color references survived because they rendered plausibly, not because a public semantic binding was verified.

## Next actions

1. Confirm shared Focus/Default visual appearance in the actual Figma editor/browser, keyboard focus-within ownership and background-dependent focus contrast.
2. Run Figma visual matrix across all four Product/Appearance contexts after the intentional File Item fill/radius change.
3. Regression-test published instances, text/slot overrides, RTL/narrow 320–360px layouts and long filenames.
4. Audit the separate Image Uploader masters and their asset-color exceptions.
5. Keep local optical spacing and legacy Paint Styles tracked for a controlled follow-up; runtime upload and assistive-technology tests remain code-owned.

**Outcome:** Foundation and the three agreed **semantic design fixes have been applied in Figma**. FU-01/FU-03 structurally pass; FU-02 has the shared correct effect/border token but needs live visual/editor and keyboard QA. Full appearance matrix, published-instance compatibility and browser accessibility are **not yet certified**.