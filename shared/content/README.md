# Shared Content System

This directory contains reusable product-language decisions for JobVision and
Cando. It complements Product Knowledge and the Design System:

```text
Product Knowledge
→ What the product means and how it behaves

Shared Content
→ How those concepts are named and communicated

Design System
→ How reusable interfaces are structured and behave
```

## Current structure

```text
shared/content/
├── README.md
├── content-guidelines.md
├── localization.md
├── product-voice.md
├── product-voice.yml
├── terminology.md
├── terminology/
│   └── terms.yml
├── patterns/
│   ├── confirmations.md
│   ├── confirmations.yml
│   ├── empty-states.md
│   ├── empty-states.yml
│   ├── errors.md
│   ├── errors.yml
│   ├── notifications.md
│   └── notifications.yml
└── evals/
    ├── confirmation-cases.yml
    ├── empty-state-cases.yml
    ├── error-cases.yml
    └── notification-cases.yml
```

- `content-guidelines.md` is the human entry point for shared voice and UI-copy
  rules.
- `product-voice.md` explains the evidence-backed voice and tone model;
  `product-voice.yml` is its machine-readable contract.
- `localization.md` owns language, directionality, number, date, translation,
  and variable-formatting rules.
- `terminology.md` explains terminology governance and selection rules.
- `terminology/terms.yml` is the machine-readable semantic lexicon used by AI,
  validation, and future generated views.
- `patterns/` contains complete human and machine-readable content patterns;
  `evals/` holds their regression cases.

## Growth rule

Keep this structure small. Create a subdirectory only after it has real content:

```text
patterns/
→ Reusable message and interaction language such as errors, confirmations,
  empty states, loading, and AI disclosures

components/
→ Content contracts specific to reusable Design System components

contexts/
→ Approved language variations for audiences or products when the shared rule
  is not sufficient

evals/
→ Executable content examples and regression cases
```

Do not create empty placeholder directories. Product-specific business wording
belongs in the relevant Product Area when it cannot be expressed as a shared
terminology or content rule.

## Source boundaries

The terminology system intentionally separates:

```text
Product truth and code mapping
→ Internal JobVision product glossary and Product Concepts

User-facing label decisions
→ Shared Content terminology rules

Exact runtime behavior
→ Product Areas and implementation sources
```

The internal product glossary is evidence and a mapping source. It does not
automatically determine the best user-facing label for every audience.

Keeping a term in the central lexicon does not make its product behavior shared.
Each entry declares its domains and visibility; product-specific behavior stays
in the owning Product Area.

## Validation

Run:

```bash
python scripts/check_content_terminology.py
python scripts/check_content_patterns.py
python scripts/generate_manifest.py check
```

The first command validates the machine-readable lexicon. The second validates
product voice, content patterns, and eval coverage. The third validates
the indexed Markdown knowledge documents and manifest freshness.
