---
id: design-system.reference.figma
collection: design-system
type: reference
title: Figma Reference
summary: Operational reference for the current JV Design System Figma file, its Foundation collections, component identities, and live-source boundaries.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: '2026-09-13'
related:
  - design-system.reference.source-of-truth
  - design-system.reference.component-mapping
---

# Figma Reference

Figma is the live source for **current editable visual construction**: component anatomy, variants/properties, Variables, Styles, spacing/layout construction, and the current design asset itself.

It does not own semantic usage rules, product business behavior, or runtime API names.

## Current library source

Primary Design System file:

- File: `-DS--Job-Vision-NEXT`
- File key: `rROD8ctH9UfPGAMrRrOzHe`
- URL: https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT

Use the live file for exact visual facts instead of copying those facts into Markdown.

## Current Foundation collections

Verified from the live file on 2026-09-13:

| Collection | Modes | Current role |
|---|---|---|
| `01 Primitives` | `Value` | Primitive Color values |
| `02 Brand` | `JobVision / Cando` | Product-aware Brand identity inputs |
| `03 Semantic` | `light / dark` | Semantic Color resolution |
| `04 Component` | `Light / Dark` | approved component-owned Color contracts |
| `Spacing` | `Mode 1` | shared spacing values |
| `Radius` | `Mode 1` | shared radius roles/values |
| `Typography breakpoint` | `LG / SM` | design-time Fluid Heading resolution |
| `Responsive layout` | `Value` | breakpoint/container/padding foundation values |

Exact values and bindings remain live Figma facts. Knowledge documents explain meaning and usage.

## Canonical Foundation pages

Relevant live pages include `🎨 Color`, `Spacing block`, `Effects`, `Responsive layout`, and `💬 Typography`.

Component pages are organized by component name, for example `🔘 Button`, `Checkbox`, `Modal`, `Tag`, and `Tooltip`.

Page names are navigation aids, not stable runtime identifiers.

## Component identity example: Button

Verified live source:

- Page: `🔘 Button` — node `0:1`
- Component set: `Button / Default`
- Node ID: `1854:1776`
- Component key: `be5d0d9cd5fdd02f9d7afa1e371c2f2a23acb329`

Current Figma variant properties include:

```text
Style → Accent | Primary | Secondary | Tertiary | Ghost | Danger primary | Danger tertiary | Danger ghost
Type  → Text + Icon | Icon only
Size  → Expressive | Large | Medium | Small | Extra Small
State → Enabled | Hover | Active | Focus | Disabled | Skeleton
```

The component also exposes text, icon visibility, and icon-swap component properties.

These are **Figma property names**. Do not infer that runtime component props use the same names or values until a code mapping is registered.

## Code/documentation links inside Figma

Some existing components still contain historical external documentation links. For example, the current Button component set links to Carbon Button usage.

Such links are reference/history only unless Design System Knowledge explicitly designates them as an owning source. They are not evidence of current runtime API parity.

## Publishing and availability

The live Figma file is the design source inspected by the Design System team.

Per-component library publishing status is not currently registered in Design System Knowledge. When published availability matters, inspect the live Figma library state instead of inferring publication from this document.

## Figma → code mapping

Mapping status is tracked in `component-mapping.md`.

Current rule:

- Figma component key / node ID identifies the design asset.
- Code repository/package/component and prop mapping must come from the real implementation source.
- Storybook story IDs/URLs must come from the real Storybook source.
- Do not invent code names from Figma page/component/property names.
- Code Connect may become the mapping mechanism, but no Code Connect contract is currently registered.

## AI retrieval rule

```text
semantic meaning / usage
→ Design System Knowledge

current visual value / anatomy / property / binding
→ live Figma file

runtime prop / default / behavior
→ registered Code source

runnable state / interaction / accessibility evidence
→ registered Storybook/test source
```

If the required live source is unavailable, report the integration gap rather than substituting a Markdown guess.
