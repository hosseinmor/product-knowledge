---
id: design-system.foundation.radius
collection: design-system
type: foundation
title: Radius
summary: Defines the small role-based radius system shared by controls, surfaces, large surfaces, and fully rounded shapes.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: 2026-09-12
related:
  - design-system.reference.tailwind
---

# Radius

## Model

Radius is role-based rather than a dense visual-size scale. Choose the role from the UI anatomy instead of selecting a radius only because it looks larger or smaller.

## Canonical roles

| Role | Value | Typical use | Tailwind-facing name |
|---|---:|---|---|
| None | 0px | Square edges and explicit no-radius cases | `rounded-none` |
| Control | 6px | Button, Input, Select, Search, dropdown trigger | `rounded-control` |
| Surface | 12px | Card, Tile, Panel, independent content surface | `rounded-surface` |
| Large surface | 20px | Dialog, Modal, Drawer, Sheet and other prominent large surfaces | `rounded-large` |
| Full | 9999px / fully rounded behavior | Tag, Chip, Avatar, Toggle track, circular/pill controls | `rounded-full` |

`Full` is a shape behavior, not the next step in a numeric progression.

## Usage rules

- Use `Control` for standard interactive controls.
- Use `Surface` for ordinary independent content containers.
- Use `Large surface` only for prominent large surfaces; do not use it merely to make a Card feel more expressive.
- Use `Full` only when the component is intentionally pill-shaped or circular.
- Parent/child containment should preserve hierarchy. A containing surface may use a larger radius than nested controls when that relationship is visually useful.
- Component-internal geometry may use a local radius without promoting that value into the Foundation.
- Avoid raw/arbitrary radius values when an approved role already expresses the intended anatomy.

## Tailwind boundary

Product Tailwind may expose the approved role names directly as `rounded-*` utilities. Tailwind's default radius scale is not the Design System source of truth.

The Design System package itself does not depend on Tailwind; Product tooling consumes a generated, framework-agnostic radius artifact. Exact preset/config mechanics remain Frontend-owned.

## Migration

Legacy Figma radius variables may remain hidden temporarily when required to preserve existing bindings. New work should use the canonical role set above.
