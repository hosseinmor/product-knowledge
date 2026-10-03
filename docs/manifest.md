# Lightweight Retrieval Manifest

`manifest.generated.json` indexes repository-owned guidance for AI retrieval.
It is not Product Knowledge and must not be used to establish product behavior.

Product Knowledge authority is defined in
[`../product-knowledge-sources.yml`](../product-knowledge-sources.yml):

- JobVision: <https://docs-jv.jvoffice.ir/>
- Cando: no canonical source

## Indexed collections

```text
shared/content/
shared/design-system/
shared/product-standards/
```

The manifest records document ID, kind, title, summary, status, owner, review
date, related IDs, topics, and path. It supports retrieval of the smallest
relevant Content, Design System, and standards set after the Product Knowledge
source gate has been applied.

## Retrieval sequence

```text
1. Read product-knowledge-sources.yml and AGENTS.md.
2. Resolve Product Knowledge through the approved external source.
3. Select the workflow through ai/router.md.
4. Filter the manifest by kind, title, summary, topics, and related IDs.
5. Read only the relevant repository guidance.
```

## Commands

```bash
python -m pip install -r requirements-dev.txt
python scripts/generate_manifest.py generate
python scripts/generate_manifest.py check
python scripts/generate_manifest.py report
```

Validation checks parseable frontmatter, required metadata, unique IDs,
resolvable related IDs, review-date format, and manifest freshness. Source
authority and forbidden Product Knowledge roots are validated separately by
`scripts/check_product_knowledge_sources.py`.
