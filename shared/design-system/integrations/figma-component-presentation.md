---
id: design-system.integration.figma-component-presentation
collection: design-system
type: integration
title: Figma Component Presentation
summary: Defines a consistent, AI-readable presentation layout for JobVision Design System component pages without duplicating canonical component or runtime contracts.
knowledge_state: draft
document_maturity: draft
owner: Design System team
related:
  - design-system.structure
  - design-system.governance.documentation-maintenance
  - design-system.reference.source-of-truth
---

# Figma Component Presentation

> **Status: draft for Design System owner review.** This is a rule for **presenting** existing components in Figma, not a redesign of any component API or a release/production approval.

## Purpose and authority

The Figma component page should let a designer locate and inspect the canonical sources, understand the main authoring choices, and test typical/edge compositions without searching an unstructured canvas.

- **Figma** owns editable sources, variant organization, presentation, and real instances.
- **Component documentation** owns intended usage, semantic distinctions, important non-obvious behavior, and component-specific gaps.
- **Code/Storybook** owns implementation behavior, runtime coverage, and executed tests.
- **Accessibility corpus** owns cross-component accessibility standards.

Do not replicate full API/state tables, token inventories, keyboard specifications, or runtime tests in this presentation. Link to their owning sources when needed. Refer to `DESIGN.md` and the relevant component contract before proposing substantive changes.

## Standard page structure

Use **one visually dominant documentation frame** per component. The presentation frame may coexist with the original canonical Component Sets and legacy materials while migration is underway. Existing Master IDs and connected instances must not be broken.

| Order | Section name | Required | Content |
| --- | --- | --- | --- |
| 00 | **Header** | Yes | Component name, one-line purpose, optional category/task/source link |
| 01 | **Component set** | Yes | Canonical source reference, clear presentation of main variant axes, concise authoring/property summary |
| 02 | **Playground** | Yes | Real component instances in representative usages and meaningful edge cases |
| 03 | **Anatomy & composition** | For composite components | Nested components, slots, relationships, and key composition rules |
| 04 | **Usage & handoff** | Only when needed | Essential do/don't, known boundary, source links, and implementation caveats |

**Keep section numbers fixed even when optional sections are absent** (for example: Radio has 00, 01, 02, 04). Do not fill the canvas with an empty optional section.

### Source vs presentation distinction

A matrix constructed from connected **instances** is a *visual index*, **not** a new Component Set or replacement for the canonical Masters.

The source may be in the documentation frame or elsewhere on the same component page. When it is elsewhere, identify the canonical set by name and preserve its node identity. Never clone a master merely to make the page appear symmetrical; avoid multiple live sources. In authoring and AI summaries, distinguish **source Component Set** from **presentation matrix**.

The canonical public component must be searchable in Figma and remain attached to its expected file/library identity.

## Layout rules (v1)

| Rule | Default |
| --- | --- |
| Documentation frame | **1600 px** wide, vertical Auto Layout, white `surface/default` |
| Outer page padding | **64 px** on all sides (content width **1472 px**) |
| Space between main sections | **48 px** |
| Section heading | `Heading/2XL` with brief `Body/SM` summary |
| Page title | `Heading/3XL` |
| Card heading | `Heading/MD` or `Heading/LG` according to hierarchy |
| Body and captions | Shared `Body/SM`, `Body/Compact/XS`, and `Label/XS` styles |
| Surface | Neutral / `surface/muted`; `surface/neutral-muted` for the spec panel |
| Color | Semantic `fg/primary`, `fg/secondary`, and small `fg/accent` accents |
| Container shape | Use system `Large` radius for independent documentation cards (12 px) |
| Borders | Avoid repeated section borders; use only when needed for separation |
| Layout behavior | Auto Layout, fixed intentional widths, Hug content height, no clipping of content |

The **1600 px frame is a documentation canvas convention**, not a product breakpoint. For components with genuinely wider interaction patterns, give the content a full-width playground or a clearly labeled exception; do not silently shrink, crop, or detach source instances.

### Alignment and responsive presentation

- Use one left-aligned frame grid for documentation labels; product content inside samples keeps its own RTL behavior.
- Do not mirror the whole English documentation scaffold merely because sample content is Persian.
- For examples, use meaningful widths. A subcomponent that is 976 px wide must not be put into a 477 px anatomy card.
- Use full-width examples or **textual source references** for large nested components.
- Size/density axes are about the **product component**, not arbitrary documentation card sizes.

## Required section details

### 00 · Header

Show the component's official Figma name, a concise purpose and (when known) task ID. Optional: a category and a link to the owner document. Avoid dumping the full developer contract into the header.

### 01 · Component set

- Display primary variant axes as a legible labeled matrix; when all permutations are too large, show meaningful representatives and identify the full canonical source.
- Identify secondary component families separately (e.g., Radio Group under Radio).
- Put the *Axes & properties* panel beside the matrix when width permits; avoid a long standalone text section.
- Show true `Variant` axes separately from Text, Boolean, Instance Swap, and Slot authoring properties.
- Do not generate a variant explosion for layout direction, full content permutations, or purely authoring choices unless the canonical component actually has those axes.

### 02 · Playground

- All UI examples must be **live Figma instances** of existing components.
- Prefer three useful categories: **typical usage**, **alternate composition**, **meaningful edge case**. Change the count when the component needs fewer or more.
- Exercise RTL/Persian content, long labels and wrapping, focus/disabled/selected states where relevant, and component-specific constraints.
- Never duplicate the complete variant matrix in the Playground.
- Name scenarios by **behavior or use case**, not `Example 1`, `Example 2`.
- The examples explain intended use; they do not certify runtime behavior.

### 03 · Anatomy & composition (conditional)

Use for composite elements, such as Data Table, Select, Timeline, or complex overlays. Show the public parent first, then relevant internal responsibilities and slots.

Keep internal information short. For a full-width Row or Header Row, include its purpose and a reference to its actual source; show it at full width elsewhere rather than scaling or clipping it inside a narrow card.

### 04 · Usage & handoff (conditional)

Use concise cards or short notes for decisions designers and developers might otherwise miss. Link to canonical component and accessibility/runtime documents. Mark unverified implementation behavior explicitly. Avoid copying extensive interaction contracts.

## Reusable documentation utilities

The Figma file has a separate page, **`__DS Docs Utilities · internal`**, containing:

- `_Docs / Page Header` — Text properties for eyebrow, title and description.
- `_Docs / Section Heading` — Text properties for title and description.
- `_Docs / Spec Panel` — Title property and content Slot.
- `_Docs / Example Card` — Title/description properties and content Slot.
- `_Docs / Handoff Note` — Title and description properties.

These are **documentation-only utilities**, not product UI primitives. Keep the underscore naming convention, exclude them from product-library publication, and maintain them in the internal page. A Slot should accept source-linked content, rather than detached screenshot facsimiles.

A change to one of these utilities may affect every presentation instance; inspect at least a simple and a composite component after changing it.

## Canonical reference pilots

- [Radio Button / Presentation Template v1](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23835-186): six Radio states, two Radio Group directions, a simple Playground.
- [Data Table / Presentation Template v1](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23835-127556): composable public table presets, wide playground, conditional Anatomy.
- [Internal utilities](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23840-10): shared presentation-only components.

These are **presentation pilots**, not component maturity or runtime approval signals. The original canonical component sources remain untouched.

## Migration / cleanup protocol

1. Identify published masters, nested source components, existing component-set IDs, slots, and connected instances.
2. Identify the *single* current canonical source per public component family.
3. Add or compose the presentation frame **without creating duplicate masters**.
4. Build Matrix and Playground from instances. Apply reusable `_Docs` blocks for repeated scaffold elements.
5. If legacy assets exist, move them only after checking consumers and migration requirements; preserve source identity.
6. Perform visual and structural QA (below) before accepting the new presentation.
7. Update the relevant component documentation only for a **real contract change**, not presentation-only rearrangement.

### QA checklist

- [ ] One recognizable 1600 px documentation frame; no unexplained loose content around it
- [ ] Header + Section 01 + Section 02 present; optional sections conditional, numbering stable
- [ ] Titles and section descriptions readable at practical Figma zoom
- [ ] Auto Layout governs all documentation groups; text uses shared styles and hugs height
- [ ] No overlap, clipped text, or narrow-card overflow
- [ ] Semantic token bindings used for documentation surfaces/foreground where available
- [ ] Main source Component Sets and nested dependencies are preserved with their current IDs
- [ ] Visual matrix and playground items are genuine source-linked instances
- [ ] Primary variant axes and non-variant properties are distinguished
- [ ] Playground covers representative product use, RTL and relevant edge behavior
- [ ] Documentation-only `_Docs` components are not published as product components
- [ ] Correct authoritative links; no unsupported runtime or accessibility claims
- [ ] Simple-component and composite-component sample screenshots pass after scaffold edits

## Guidance for AI authoring

When asked to standardize a Figma component page:

1. Read this rule **only when editing the Figma presentation**, then read the target component contract and inspect the actual current Figma nodes.
2. Treat existing canonical Masters, published IDs, variable bindings and nested component contracts as protected; ask for owner review before changing them.
3. First build a clean documentation layout using **existing** instances and `_Docs` utilities.
4. Never infer undocumented axis/state options from a generic template. Display only the target's real options.
5. Add conditional Anatomy/Handoff sections only when necessary.
6. Return the changed presentation link, affected node IDs, exceptions, and a short audit result. A passing Figma screenshot is not evidence of working runtime interaction.

## Open review points

- Confirm whether all component pages adopt 1600 px, or whether an explicitly defined **wide exception** is needed for unusual editors/data views.
- Confirm publication-exclusion enforcement for internal `_Docs` sources in library settings (the naming convention alone must not be treated as technical enforcement).
- Decide the order and governance for migrating already published legacy documentation frames. Never silently substitute published component sources.
