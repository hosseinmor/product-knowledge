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
| JobVision | <https://docs-jv.jvoffice.ir/> — internal source | Forbidden |
| Cando | <https://docs-cd.jvoffice.ir/> — internal source | Forbidden |

When the owning product's canonical documentation is inaccessible, preserve the
access limitation and ask for relevant source material when needed. Explicit
owner input, reviewed evidence, approved decisions, observations, and
implementation evidence may support bounded investigation, but they do not
silently replace the owning product's canonical Product Knowledge.

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

1. Open <https://docs-cd.jvoffice.ir/> through a verified internal-browser path.
2. Load the smallest relevant domains.
3. Record the source pages used.
4. Load the relevant Content and Design System guidance from this repository.
5. Keep Cando canonical truth separate from JobVision truth, reviewed evidence,
   observations, hypotheses, and recommendations.
6. If the canonical source is inaccessible or insufficient for a material claim,
   preserve that limitation or uncertainty rather than using this repository,
   JobVision Product Knowledge, Figma, screenshots, or observed UI as canonical
   fallback.

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
Knowledge roots and verifies the JobVision and Cando canonical URLs plus the
required entry-point references. The manifest indexes only repository-owned
guidance; it is not a Product Knowledge index.

## Contribution boundary

- Use a dedicated branch and pull request; never write directly to `main`.
- Preserve source authority in every workflow and artifact.
- Product decisions belong in the approved Product Knowledge source, not in
  Content or Design System documentation.
- Content and Design System changes may cite product truth but must not copy or
  silently redefine it.
