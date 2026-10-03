# AI Entry Point

Use this file as the tool-agnostic starting point for AI-assisted work in this
repository.

## Source authority — read first

Read [`product-knowledge-sources.yml`](product-knowledge-sources.yml) before
every product task.

This repository is **not** the canonical Product Knowledge source.

- JobVision Product Knowledge is canonical only at
  <https://docs-jv.jvoffice.ir/>. It requires the internal VPN and browser
  access.
- Cando currently has no canonical Product Knowledge source.
- Repository files under `shared/content/`, `shared/design-system/`, and
  `shared/product-standards/` cannot establish product behavior.
- Figma, screenshots, runtime UI, and walkthroughs are evidence, not canonical
  Product Knowledge.
- Never substitute Git history, deleted repository documents, memory, or an
  observed interface when the approved source is missing or inaccessible.

## Start every product task

1. Read `product-knowledge-sources.yml`.
2. Read `ai/router.md` and select the smallest relevant workflow.
3. For JobVision product claims, open the internal documentation site in a
   browser and load only the relevant domains.
4. For Cando, state that canonical Product Knowledge is unavailable. Use only
   explicit owner input, reviewed evidence, or approved decisions, with their
   authority clearly labelled.
5. Load only the relevant Content System, Design System, and product-standard
   documents from this repository.
6. Keep canonical truth, approved decisions, evidence, observations,
   hypotheses, recommendations, and unknowns separate.
7. Do not invent missing product behavior or human decisions.

## Capability fallback

```text
JobVision internal site accessible
→ Read the relevant canonical domains through the authenticated browser

JobVision internal site inaccessible
→ Ask for the relevant source material or stop product-claim work
→ Never fall back to this repository

Cando request
→ State that no canonical source exists
→ Use explicitly authorised inputs only and preserve unresolved behavior

Repository read access available
→ Use shared Content, Design System, standards, workflows, and templates

Repository read access unavailable
→ Ask for the minimum relevant files; do not claim repository-backed guidance
```

## Human authority

AI may retrieve context, identify gaps, ask blocking questions, recommend
options, draft outputs, and structure evidence. Humans remain responsible for
product decisions, scope approval, artifact approval, and approving any future
canonical Cando knowledge source.

## Repository changes

- Do not write directly to `main`.
- Make approved changes on a dedicated branch and pull request.
- Do not modify unrelated files.
- Regenerate `manifest.generated.json` whenever indexed repository guidance
  changes.
- Never restore active Product Knowledge under `products/`,
  `shared/product-concepts/`, or `shared/product-services/`.
- Historical Product Knowledge belongs only in Git history or archive refs, not
  in an indexed `legacy/` directory on `main`.
