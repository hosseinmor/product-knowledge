---
id: content.content-guidelines
collection: content
type: content-guideline
title: Content Guidelines
summary: Routes shared product-content decisions across voice, terminology, localization, patterns, component contracts, contexts, and executable evaluations.
knowledge_state: unverified
document_maturity: draft
related:
  - content.product-voice
  - content.terminology
  - content.localization
  - content.pattern.error
---

# Content Guidelines

This document is the shared human entry point. Detailed voice is owned by
[`product-voice.md`](product-voice.md), terminology by
[`terminology.md`](terminology.md), and machine-readable terms by
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

Use [`product-voice.md`](product-voice.md) for the evidence-backed voice,
precedence order, operational tone dimensions, and surface matrix. Use
[`product-voice.yml`](product-voice.yml) when an AI or validator needs the
structured contract.

Voice remains consistent; tone changes with task, risk, and user state. Do not
apply warmth or brand expression at the expense of product truth, recovery, or
accessibility.

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

Use [`patterns/errors.md`](patterns/errors.md) for error structure, placement,
tone, recovery, and accessibility. Its machine-readable rules and eval cases
are in [`patterns/errors.yml`](patterns/errors.yml) and
[`evals/error-cases.yml`](evals/error-cases.yml).

Minimum contract:

- identify the problem;
- identify recovery when it is known and safe;
- reuse the visible field or object terminology;
- do not blame the user, expose internal code as the explanation, or add brand
  personality.

## Confirmation Messages

## Empty States

## Notifications

## AI-Generated Content

AI-generated product content follows the same terminology, localization,
pattern, component, and product-truth constraints as human-authored content.
