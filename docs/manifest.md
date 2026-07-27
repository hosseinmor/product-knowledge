# Generated Manifest

`manifest.generated.json` is the deterministic discovery index for Product Knowledge and shared knowledge collections.

Generate and validate it with:

```bash
python -m pip install -r requirements-dev.txt
python scripts/knowledge.py generate
python scripts/knowledge.py check --strict
```

Use `report` for repository quality counts:

```bash
python scripts/knowledge.py report
```

CI runs strict validation and checks that the committed manifest is current on every pull request and push to `main`.

## Manifest responsibilities

The manifest contains discovery metadata only. It does not own product, Design System, content, or shared business truth.

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

The repository has completed its common-metadata migration. The `unindexed` list is expected to remain empty.

A new unindexed document is a validation failure unless an explicit migration exception is approved and CI is deliberately changed. Agents must never infer that an absent document or fact does not exist.

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

Migration does not establish semantic truth. Documents migrated without human verification remain `unverified` even when their metadata is structurally valid.

## Stable identifiers

Relationships use stable document IDs, not paths. The manifest resolves IDs to current repository paths. Moving a file must not change its ID.

## Determinism

The manifest excludes generation timestamps and sorts entries by ID and unindexed paths by path. Running the generator twice without source changes must produce an identical file.

## Pull-request requirement

Any change to indexed Markdown files, metadata, IDs, or relationships must include the regenerated `manifest.generated.json`. CI rejects stale manifests, invalid IDs, broken relationships, and collection/type mismatches.
