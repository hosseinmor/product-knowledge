# Generated Manifest

`manifest.generated.json` is the deterministic discovery index for Product Knowledge and shared knowledge collections.

It is generated from document frontmatter by:

```bash
python -m pip install -r requirements-dev.txt
python scripts/knowledge.py generate
```

Validate metadata and relationships with:

```bash
python scripts/knowledge.py validate
```

After the metadata migration is complete, CI uses strict validation and checks that the committed manifest is current:

```bash
python scripts/knowledge.py check --strict
```

## Manifest responsibilities

The manifest contains discovery metadata only. It does not own product or design-system truth.

Each indexed entry contains:

```text
id
path
collection
type
product when relevant
title
summary
knowledge_state
document_maturity
related IDs
selected retrieval fields
```

Documents that cannot yet be indexed appear in `unindexed` with an explicit reason. Agents must treat `unindexed` as a coverage gap and must not infer that an absent document or fact does not exist.

## Collections and types

`collection` identifies the knowledge family and its retrieval rules. `type` identifies the document type within that family.

```text
product
→ product, capability, flow, domain, decision

design-system
→ overview, foundation, token, component, pattern, experience-rule,
  accessibility, product-variation, reference, governance, ui-template

content
→ content-guideline

product-standard
→ product-standard, documentation-guideline

shared-domain
→ domain
```

`shared` is placement and ownership, not a universal document type.

## Truth and maturity

All indexed documents use:

```yaml
knowledge_state: canonical | observed | unverified | deprecated
document_maturity: scaffold | draft | reviewed | stable
```

A scaffold cannot be canonical. A canonical document must contain substantive owned facts.

## Stable identifiers

Relationships use stable document IDs, not paths. The manifest resolves IDs to current repository paths. Moving a file must not change its ID.

## Determinism

The manifest excludes generation timestamps and sorts entries by ID and unindexed paths by path. Running the generator twice without source changes must produce an identical file.
