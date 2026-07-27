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

Opaque color scales currently used by the alias graph:

```text
color/neutral/*
color/blue/*
color/purple/*
color/red/*
color/green/*
color/emerald/*
color/orange/*
color/yellow/*
color/brand/jobvision/*
color/brand/cando/*
```

The final direct values of the opaque scales remain an open decision. Alias mappings must reference these Primitive variables rather than duplicate their direct values.

### Alpha primitives

Alpha primitives store direct RGBA values and support transparent interaction states:

| Primitive variable | Direct value |
|---|---|
| `color/black-alpha/4` | `rgba(0, 0, 0, 0.04)` |
| `color/black-alpha/8` | `rgba(0, 0, 0, 0.08)` |
| `color/white-alpha/8` | `rgba(255, 255, 255, 0.08)` |
| `color/white-alpha/12` | `rgba(255, 255, 255, 0.12)` |

See `color-token-aliases.md` for every mode-specific alias target.

## Typography
## Spacing
## Radius
## Elevation
## Motion
