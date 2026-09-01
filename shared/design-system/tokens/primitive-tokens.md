---
id: design-system.token.primitive-tokens
collection: design-system
type: token
title: Primitive Tokens
summary: '> Status: partial value catalog'
knowledge_state: unverified
document_maturity: draft
related: []
---

# Primitive Tokens

> Status: partial value catalog

## Color

Primitive color scales are context-free and are named by hue rather than product ownership.

Current opaque families:

```text
color/neutral/*
color/blue/*
color/yellow/*
color/red/*
color/purple/*
color/green/*
color/emerald/*
color/orange/*
```

Product-specific Primitive families such as the former `color/brand/jobvision/*` and `color/brand/cando/*` are removed in v4. Product identity is resolved in the Brand collection.

Current brand color anchors:

```text
JobVision blue  → #0053FF
Cando yellow    → #FFC400
```

These anchors do not yet define a numbered scale step. The final 50–950 opaque values remain an open decision and will be built as a separate palette pass.

The `green/*` versus `emerald/*` inventory also remains open until that pass; do not remove either family from implementation solely from this draft.

A Primitive palette may feed multiple Semantic or Component roles. For example, the same `blue/*` scale may feed JobVision Brand, Accent, Link, Info, and categorical Blue without merging those meanings.

### Alpha primitives

Alpha primitives store direct RGBA values and support transparent interaction, overlay, and loading treatments:

| Primitive variable | Direct value |
|---|---|
| `color/black-alpha/4` | `rgba(0, 0, 0, 0.04)` |
| `color/black-alpha/8` | `rgba(0, 0, 0, 0.08)` |
| `color/black-alpha/40` | `rgba(0, 0, 0, 0.40)` |
| `color/white-alpha/8` | `rgba(255, 255, 255, 0.08)` |
| `color/white-alpha/12` | `rgba(255, 255, 255, 0.12)` |

See `color-token-aliases.md` for mode-specific alias targets and unresolved mappings.

## Typography
## Spacing
## Radius
## Elevation
## Motion
