# Karbon · JobVision Group Design Language

**کاربن، زبان طراحی محصولات گروه جاب‌ویژن**

Karbon is the **internal**, shared Design Language of JobVision Group. Shared
foundations, components and reusable interaction rules coexist with explicit,
approved JobVision/Cando product identity variations. The scope includes tokens,
foundations, components, patterns, accessibility, governance and usage/implementation
guidance connected to live Figma, Code and Storybook sources. Iconography, motion
and illustration can evolve here as needed; empty future scaffolds are not required.

**Migration status:** this is still the existing `product-knowledge` GitHub
repository until the administrative rename to `karbon-design-language` occurs.
The Content System and its validators also **remain here temporarily** until
they are fully copied and validated in independent `product-content-system`.
No file is treated as transferred or retired merely because of this plan.
See [migration ownership and cutover](migration/ownership-and-cutover.md).

## Two Karbon usage paths

- **Designing with Karbon:** [DESIGN.md](shared/design-system/DESIGN.md)
  → relevant component/pattern → specialized accessibility/variation rule
  → live Figma/Code/Storybook facts as applicable.
- **Building and maintaining Karbon:** [STRUCTURE.md](shared/design-system/STRUCTURE.md)
  → [governance](shared/design-system/governance/README.md),
  [integrations](shared/design-system/integrations/README.md) and
  source-owned quality checks.

For multi-step Product work (PRD, research, Design Exploration, review, readiness),
use the separate [Product Development Harness](https://github.com/hosseinmor/product-development-harness)
starting at its `AGENTS.md`. This repository does not own a parallel general
Product workflow. Its former `ai/` and `templates/` routes are retained only
until their consumers and replacements are reconciled.

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

## Transitional source boundaries

- Current Product Knowledge remains external and product-scoped:
  JobVision <https://docs-jv.jvoffice.ir/>, Cando <https://docs-cd.jvoffice.ir/>.
  Verify access; neither the legacy repository nor design/copy sources are
  fallback authorities for current behavior.
- Design Language: `shared/design-system/DESIGN.md` and only related docs.
- Content System until independent cutover: `shared/content/README.md` and
  only related docs/evals.
- Existing combined `manifest.generated.json` and `product-knowledge-sources.yml`
  remain transitional compatibility assets; they must be split or retired only
  after the new owners can validate and retrieve their own content.

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
→ transitional generic routes awaiting replacement by the Harness

templates/
→ legacy Jira PRD template awaiting retirement; the Harness PRD contract is authoritative

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
