# Shared Content System

This directory contains reusable product-language decisions for JobVision and
Cando. It complements Product Knowledge and the Design System:

JobVision Product Knowledge is external at <https://docs-jv.jvoffice.ir/>.
Cando currently has no canonical Product Knowledge source. This directory must
not be used as a fallback for either product.

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
├── localization.yml
├── product-voice.md
├── product-voice.yml
├── terminology.md
├── terminology/
│   └── terms.yml
├── components/
│   ├── README.md
│   ├── button.md
│   ├── button.yml
│   ├── modal.md
│   ├── modal.yml
│   ├── notification.md
│   ├── notification.yml
│   ├── text-input.md
│   └── text-input.yml
├── contexts/
│   ├── README.md
│   ├── jobvision-candidate.md
│   ├── jobvision-candidate.yml
│   ├── jobvision-employer.md
│   └── jobvision-employer.yml
├── patterns/
│   ├── ai-content-and-disclosure.md
│   ├── ai-content-and-disclosure.yml
│   ├── confirmations.md
│   ├── confirmations.yml
│   ├── empty-states.md
│   ├── empty-states.yml
│   ├── errors.md
│   ├── errors.yml
│   ├── instructions-and-helper-text.md
│   ├── instructions-and-helper-text.yml
│   ├── loading-and-progress.md
│   ├── loading-and-progress.yml
│   ├── notifications.md
│   └── notifications.yml
└── evals/
    ├── ai-content-cases.yml
    ├── button-content-cases.yml
    ├── confirmation-cases.yml
    ├── empty-state-cases.yml
    ├── error-cases.yml
    ├── instruction-helper-cases.yml
    ├── jobvision-candidate-context-cases.yml
    ├── jobvision-employer-context-cases.yml
    ├── localization-cases.yml
    ├── loading-progress-cases.yml
    ├── modal-content-cases.yml
    ├── notification-content-cases.yml
    ├── notification-cases.yml
    └── text-input-content-cases.yml
```

- `content-guidelines.md` is the human entry point for shared voice and UI-copy
  rules.
- `product-voice.md` explains the evidence-backed voice and tone model;
  `product-voice.yml` is its machine-readable contract.
- `localization.md` owns the human language, directionality, number, date,
  translation, and variable-formatting contract; `localization.yml` is its
  machine-readable source and `evals/localization-cases.yml` its regression set.
- `terminology.md` explains terminology governance and selection rules.
- `terminology/terms.yml` is the machine-readable semantic lexicon used by AI,
  validation, and future generated views.
- `patterns/` contains complete human and machine-readable content patterns.
- `components/` contains copy contracts specific to reusable Design System
  components; Button, Text Input, Modal, and Notification are currently
  registered.
- `contexts/` contains approved product- and audience-specific variations;
  JobVision Candidate and Employer are currently registered.
- `evals/` holds foundation, pattern, component, and context regression cases.

## Growth rule

Keep this structure small. Create a subdirectory only after it has real content:

```text
patterns/
→ Reusable message and interaction language such as instructions, errors,
  confirmations, empty states, notifications, loading, and AI disclosures

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
→ Internal JobVision documentation site; no canonical Cando source yet

User-facing label decisions
→ Shared Content terminology rules

Exact runtime behavior
→ Approved external Product Knowledge and implementation sources
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
python scripts/check_content_localization.py
python scripts/check_content_components.py
python scripts/check_content_patterns.py
python scripts/generate_manifest.py check
```

The first command validates the machine-readable lexicon. The second validates
the Persian localization foundation and eval coverage. The third validates
registered component contracts and their eval coverage. The fourth validates
the registered human/machine pattern inventory, product voice, pattern and eval
identities, rule families and keys, pattern-to-eval links, and blocking-rule
coverage. All content validators reject duplicate YAML keys. The final command
validates the indexed Markdown knowledge documents and manifest freshness.
