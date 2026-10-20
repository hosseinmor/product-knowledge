---
id: design-system.audit.button-spacing-2026-10-20
collection: design-system
type: audit
title: Button Source Spacing Migration — 2026-10-20
summary: Canonical Button spacing bindings corrected in Figma without changing dimensions, variant APIs or visuals.
knowledge_state: verified
document_maturity: reviewed
design_status: figma-source-spacing-qa-complete
owner: Design System team
last_reviewed: '2026-10-20'
related:
  - design-system.component.button
  - design-system.reference.figma-token-compliance
---

# Button Spacing Migration — 2026-10-20

Source: [Button / Default master](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=1854-1776), ID `1854:1776`, component key `be5d0d9cd5fdd02f9d7afa1e371c2f2a23acb329`. Existing **320** variants: 8 Styles × 4 Sizes × 5 interaction States × 2 Loading states. This audit examines canonical owned source layers; nested Instance children and Figma Component Set matrix presentation are not counted as owned Button spacing.

## Changes applied in place

| Bound source property | New bindings |
|---|---:|
| Button content paddingLeft | 244 |
| Button content paddingRight | 244 |
| Button content itemSpacing | 320 |
| **Total** | **808** |

**152** effective spacing properties were already correctly bound. After this migration, **960/960** effective nonzero Button content spacing properties are connected to the correct existing **Spacing** variables: 320 gaps and 640 left/right padding values. Nothing was renumbered, no variable was created, no component was recreated, and no instance was detached.

New binding values: **8px × 480, 12px × 8, 16px × 160, 20px × 160**. Preserve the documented sizing matrix:

| Size | Fixed height | Content horizontal padding | Icon–label gap | Variants |
|---|---:|---:|---:|---:|
| Extra Small | 28px | 8px | 8px | 80 |
| Small | 32px | 12px | 8px | 80 |
| Medium | 40px | 16px | 8px | 80 |
| Large | 48px | 20px | 8px | 80 |

Post-change read confirmed **zero mismatched content padding/gap bindings**, **zero layout size mismatches**, unchanged published Component Set ID/key and **320** variants. The source has **320/320 Text nodes bound to Text Styles** and **320/320 radii bound to a Radius variable**. The representative Primary enabled source screenshots retained heights 28 / 32 / 40 / 48px. Focus screenshot was also captured; it did not indicate layout regression.

## Explicit inactive-gap exception

Each Button variant contains a `Start Icon` wrapper and `End Icon` wrapper, each with **exactly one child** and an authored `itemSpacing=8px`. These are **640 inert gap properties** (2 wrappers × 320 variants). A gap cannot separate siblings in a single-child Auto Layout frame; the visible label-to-icon gap belongs to **Button content** and is now bound.

Do not treat these inactive gap properties as active spacing debt and do not rename, detach or restructure the icon slots to chase an audit percentage. They remain unbound and numerically unchanged. The shared read-only auditor was updated to skip one-child non-wrapping itemSpacing from effective spacing compliance. If a wrapper gains multiple direct children, re-audit its gap.

## Paint Style migration separated

The canonical Button source uses semantic variable-bound Color paints and some legacy **Transparent/Transparent** Paint Style applications in the Focus states (approximately **68** occurrences in owned layers). The Component Set presentation wrapper also contains a historical style not belonging to a consumer Button variant. These are **paint-style review candidates, not automatic violations**: the transparent style uses special blending, so replacing it with an opaque semantic surface could change Focus/Loading visuals. No Button Color changes were made in this spacing pass.

## QA and limitations

- Structural property-level validation on the 808 writes: **zero failures**.
- Canonical source-only audit: **960 bound / 0 unbound effective scale spacing**, 320 bound radii, 320 styled texts; no unresolved semantic color bindings.
- Reviewed screenshots of Primary Enabled in all four sizes, plus Medium Focus.
- **Not yet certified**: all Products/Appearances visually, published consumer overrides, Storybook/Angular runtime behavior, accessibility focus/contrast and every icon/layout combination. No assumption of actual runtime release.
- Image Uploader is explicitly outside audit scope and remains untouched.

**Status:** Button **owned-source effective Spacing bindings** are QA-complete. The legacy transparency Paint Styles and broader runtime acceptance belong to separate follow-up work.
