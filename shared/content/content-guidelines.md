---
id: content.content-guidelines
collection: content
type: content-guideline
title: Content Guidelines
summary: Routes shared product-content decisions across voice, terminology, localization, patterns, component contracts, contexts, and executable evaluations.
knowledge_state: unverified
document_maturity: scaffold
related:
  - content.terminology
  - content.localization
---

# Content Guidelines

This document is the shared human entry point. Detailed terminology is owned by
[`terminology.md`](terminology.md), and machine-readable terms are owned by
[`terminology/terms.yml`](terminology/terms.yml).

Use the smallest relevant layer:

```text
Foundation
→ Voice, Persian language, terminology, localization

Pattern
→ Errors, confirmations, empty states, loading, AI content

Component contract
→ Button, input, modal, notification, and other component-specific copy

Context
→ Approved JobVision/Cando or Candidate/Employer/ATS variation

Eval
→ Executable examples and regression cases
```

Do not copy Product Knowledge into this directory. Product concepts and behavior
remain canonical in Product Concepts and Product Areas; Content owns naming and
communication rules.

## Voice and Tone

Status: not yet authored. Use confirmed brand guidance as intent, not as a
replacement for surface-specific content rules.

## UI Copy Principles

- Prefer explicit outcomes over generic labels.
- Preserve product truth; do not improve tone by changing meaning.
- Apply terminology for the current audience and surface.
- Keep unknown product behavior explicit.

## Labels

Use the preferred label for the concept and surface from the terminology source.
Do not use implementation names as labels merely because they exist in code.

## Instructions

## Error Messages

## Confirmation Messages

## Empty States

## Notifications

## AI-Generated Content

AI-generated product content follows the same terminology, localization,
pattern, component, and product-truth constraints as human-authored content.
