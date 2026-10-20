---
id: design-system.audit.file-uploader-token-migration-2026-10-20
collection: design-system
type: audit
title: File Uploader — Token Migration Audit (HOS-39)
summary: Canonical Carbon File Uploader bindings migrated in place; local geometry, semantic color and focus decisions explicitly tracked.
knowledge_state: verified
document_maturity: reviewed
design_status: figma-binding-qa-complete-semantic-review-open
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
| File Item | 0 | 0 | **18 × 4px** | 0 |
| Dropzone States | 0 | 0 | 0 | 0 |
| File list | 0 | 0 | 0 | 0 |

The Dropzone master contains 8 non-scale optical padding observations (10px/50px). The File Item has 36 non-scale observations (7px/11px/15px). Component Set presentation layout properties were excluded from canonical component geometry counts. Borrowed nested instances were not double-counted as owned source properties.

## Semantic and exception decisions still open

**FU-01 / P1 — File Item background role:** All 18 source variants currently use surface/neutral-muted on the File Item container. The Carbon file item generally displays file/status information and separate remove/other actions; the **whole container is not established as an interactive neutral control**. The Semantic Surface contract says surface/neutral-muted is for interactive neutral treatment and surface/muted is for passive supporting structure. Recommend reviewing whether **surface/muted** better represents the anatomy, including Light/Dark appearance and contrast. Do not silently change a long-standing Carbon fill: the current v1 contract explicitly preserves original visual treatment. If kept, record an anatomy-specific, reviewed exception explaining interactivity/meaning.

**FU-02 / P1 — Dropzone Focus:** Focus state 3183:29118 has **2px inside line/accent** and no effect/style layer for a separate focus/default ring. The shared Focus contract expects a distinct focus role. Review keyboard interaction ownership (Browse action vs Dropzone target), then add an approved focus/default indication with compatible geometry and test keyboard only, error coexistence and Theme contrasts. Do not assume changing the border token alone satisfies this.

**FU-03 / P2 — File Item Radius:** Every File Item variant has a literal **4px** corner radius (18/18). This is outside the canonical Radius scale (None/3/6/12/Full) and is not bound. Current file-uploader.md specifically preserves original Carbon radii in v1. **Compatibility debt, not a silently approved global exception.** Decide explicitly between migrating all 18 in place to 6px Medium with visual signoff, or documenting a temporary File Item geometry exception with an owner/retirement date. No change performed.

**FU-04 / P2 — Local construction geometry:** File Item 7/11/15px vertical padding and Dropzone 10/50px optical offsets remain literal. All documented scale spacing is now bound. Confirm that each non-scale value is actually needed for fixed-height 160/136/112px File Item specimens and Dropzone composition; do not round independently, which could damage height/vertical centering.

**FU-05 / P2 — Legacy Paint Style:** Some canonical variants still use the old Transparent/Transparent Paint Style (white Multiply paint) to achieve a neutral/transparent-looking base; at least one error-item icon inherits Accessibility/White. Neither should be replaced mechanically by surface/default or another opaque Semantic fill, because that can alter contrast or blending on nonwhite surfaces. Resolve Paint Style migration only after appearance matrix and nested-source ownership checks.

**FU-06 / separate migration — image uploader:** Its 9 variants still show 9 deprecated 12px radius bindings, 46 exact-scale nonzero spacing properties without variables (at owned-source level), 3 raw colors and 18 unresolved variable references in the current source inventory. Some image/placeholder coloration may be intentional assets. Treat it as a distinct component ownership/migration audit; do not use the Carbon File Uploader counts to certify it.

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

1. Review FU-01 surface role and FU-02 Focus semantics with Light/Dark and keyboard behavior; design decision required before changing appearance.
2. Decide FU-03 raw 4px File Item radius compatibility vs migration to 6px.
3. Validate the original File Item size/height matrix, 3-file Slot and all error states at narrow widths.
4. Audit image uploader separately; preserve its distinct usage model and required asset/color exceptions.
5. Perform Product × Appearance and published-instance override QA; runtime accessibility and real upload operations remain code-owned.

**Outcome:** Canonical Carbon File Uploader foundation **binding hygiene** is fixed for shared spacing and deprecated radius; semantic color/focus and intentional local-radius exceptions remain open. Do **not** declare complete token-compliance signoff until FU-01 through FU-03 are decided.