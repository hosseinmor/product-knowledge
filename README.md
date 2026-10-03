# Product Content and Design Knowledge

This repository contains JobVision and Cando Product Content guidance, Design
System knowledge, reusable product standards, and AI workflow contracts. It is
not the canonical store for product behavior.

## Product Knowledge sources

Read [`product-knowledge-sources.yml`](product-knowledge-sources.yml) and
[`docs/product-knowledge-sources.md`](docs/product-knowledge-sources.md) before
product work.

| Product | Canonical Product Knowledge | Repository fallback |
|---|---|---|
| JobVision | <https://docs-jv.jvoffice.ir/> — internal VPN and browser required | Forbidden |
| Cando | No canonical source yet | Forbidden |

When JobVision documentation is inaccessible, stop product-claim work or ask
for the relevant source. For Cando, preserve behavior as unknown unless the
user supplies explicit owner input, reviewed evidence, or an approved decision.
Those inputs do not silently become canonical Product Knowledge in this
repository.

The previous repository Product Knowledge was removed from `main`. It remains
recoverable through Git history and archive refs; do not restore it as a
fallback or copy it into an indexed `legacy/` directory.

## Repository role

```text
Internal Product Knowledge source
→ What the product means and how it behaves

Shared Content
→ How approved product truth is named and communicated

Design System
→ How reusable interfaces are structured and behave

Product standards
→ Reusable cross-product principles and operating guidance
```

This separation is mandatory. Content Contexts can choose language and set
claim boundaries, but they cannot establish lifecycle, permission, validation,
eligibility, consequence, or flow.

## Start here

```text
AGENTS.md
→ source-authority and repository rules

ai/router.md
→ route the requested outcome

product-knowledge-sources.yml
→ machine-readable Product Knowledge authority

manifest.generated.json
→ retrieve repository-owned Content, Design System, and standards only
```

## Active structure

```text
shared/content/
→ Product Content System: voice, terminology, localization, patterns,
  component-copy contracts, contexts, and evals

shared/design-system/
→ foundations, tokens, components, patterns, accessibility, and governance

shared/product-standards/
→ reusable product and documentation standards

ai/
→ routing and workflow contracts that consume external Product Knowledge

templates/
→ repository-owned output templates such as the Jira PRD template

docs/
→ source authority, retrieval, setup, and repository documentation
```

These active Product Knowledge roots are forbidden:

```text
products/
shared/product-concepts/
shared/product-services/
```

## Product work

### JobVision

1. Open <https://docs-jv.jvoffice.ir/> with the internal VPN and browser.
2. Start from its product map and load the smallest relevant domains.
3. Record the source pages used.
4. Load the relevant Content and Design System guidance from this repository.
5. Separate documented truth from observed UI, hypotheses, and recommendations.

### Cando

Cando has no canonical Product Knowledge source. Until one is approved:

- label owner input, approved decisions, and reviewed evidence explicitly;
- preserve unresolved product behavior as unknown;
- do not use Content Contexts, Figma, screenshots, observed UI, or deleted files
  as product truth;
- do not write canonical Cando Product Knowledge into this repository.

The recommended long-term solution is a dedicated internal Cando knowledge
repository and site with independent ownership and a clear Cando URL.

## Validation

Install the development dependency and run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/generate_manifest.py generate
python scripts/generate_manifest.py check
python scripts/check_product_knowledge_sources.py
python scripts/check_content_terminology.py
python scripts/check_content_localization.py
python scripts/check_content_components.py
python scripts/check_content_contexts.py
python scripts/check_content_patterns.py
python scripts/check_accessibility_knowledge.py
```

The source-authority validator rejects active files under the forbidden Product
Knowledge roots and verifies the JobVision URL, Cando unavailable state, and
required entry-point references. The manifest indexes only repository-owned
guidance; it is not a Product Knowledge index.

## Contribution boundary

- Use a dedicated branch and pull request; never write directly to `main`.
- Preserve source authority in every workflow and artifact.
- Product decisions belong in the approved Product Knowledge source, not in
  Content or Design System documentation.
- Content and Design System changes may cite product truth but must not copy or
  silently redefine it.
