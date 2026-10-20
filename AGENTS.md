# Karbon Design Language — AI Entry Point

Use this file for **this repository's own** reusable Design Language knowledge,
authoring and maintenance work. This repository is scheduled to retain its Git
history and be renamed `karbon-design-language`; the admin rename has not yet
occurred. The intended full title is **Karbon · JobVision Group Design Language**
(کاربن، زبان طراحی محصولات گروه جاب‌ویژن). Karbon is an internal shared design
language of JobVision Group, not a standalone public brand.

- **Using Karbon to design products:** start at
  `shared/design-system/DESIGN.md`, then the relevant component/pattern,
  accessibility or product-variation document. Verify exact Figma/Code/Storybook
  facts in their respective live sources.
- **Building or maintaining Karbon:** start with
  `shared/design-system/STRUCTURE.md`, relevant governance,
  integrations, templates, and validators. Keep meaningful JobVision/Cando
  product-identity variations.
- **Independent Content work (temporary):** use `shared/content/README.md`
  and relevant files while `product-content-system` is being created,
  copied and validated. Do not treat it as permanent Karbon ownership.
- **Multi-step Product/PRD/Design work:** start instead at
  `https://github.com/hosseinmor/product-development-harness` `AGENTS.md`.
  The Harness owns generic workflows, artifacts, review and clarification.
  Legacy `ai/` and `templates/` routes here are transitional, not competing
  workflow contracts.
- See `migration/ownership-and-cutover.md` for the staged non-destructive plan.

Do not assert that the rename or content transfer has already happened.

## Source authority — read first

Read [`product-knowledge-sources.yml`](product-knowledge-sources.yml) before
every product task.

This repository is **not** the canonical Product Knowledge source.

- JobVision Product Knowledge is canonical only at
  <https://docs-jv.jvoffice.ir/>. It requires the internal VPN and browser
  access.
- Cando Product Knowledge is canonical only at
  <https://docs-cd.jvoffice.ir/>. Verify access to the internal source in the
  current execution environment before relying on it.
- Repository files under `shared/content/`, `shared/design-system/`, and
  `shared/product-standards/` cannot establish product behavior.
- Figma, screenshots, runtime UI, and walkthroughs are evidence, not canonical
  Product Knowledge.
- Never substitute Git history, deleted repository documents, memory, or an
  observed interface when the approved source is missing or inaccessible.

## Transitional source use (until content and general routes are cut over)

1. For product-behavior claims, read `product-knowledge-sources.yml` and
   verify access to the owning JobVision/Cando internal source.
2. For a Karbon task, retrieve only relevant Design Language documents using
   the local entry point and, if needed, `manifest.generated.json`.
3. For a Product Content task, retrieve only relevant Content System documents
   while they remain in this repository. The separate repo must pass its own
   validators before these source files are removed.
4. For generic PRD, research or Product Design workflows, follow the Harness;
   do not execute the duplicate legacy `ai/router.md` as an independent
   contract.
5. Keep canonical product truth, decisions, evidence and hypotheses separated.

## Capability fallback

```text
JobVision internal site accessible
→ Read the relevant canonical domains through the authenticated browser

JobVision internal site inaccessible
→ Ask for the relevant source material or stop product-claim work
→ Never fall back to this repository

Cando internal site accessible
→ Read the relevant canonical domains from https://docs-cd.jvoffice.ir/

Cando internal site inaccessible
→ Preserve the access limitation and use explicitly authorised evidence only
→ Never fall back to JobVision Product Knowledge or this repository

Repository read access available
→ Use shared Content, Design System, standards, workflows, and templates

Repository read access unavailable
→ Ask for the minimum relevant files; do not claim repository-backed guidance
```

## Human authority

AI may retrieve context, identify gaps, ask blocking questions, recommend
options, draft outputs, and structure evidence. Humans remain responsible for
product decisions, scope approval, artifact approval, and Product Knowledge
governance for each product.

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
