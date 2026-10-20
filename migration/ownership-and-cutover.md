# Karbon / Content / Harness migration map — stage 1 (non-destructive)

**Decision:** rename this existing GitHub repository from `product-knowledge` to `karbon-design-language` (retain repository history); introduce independent `product-content-system`; keep `product-development-harness` as the multi-step Product workflow owner. Repository creation/rename are administrative cutover actions, **not** performed by this PR.

## Snapshot inspected

- Source: `hosseinmor/product-knowledge`, `main`, recursive tree `6b0214530b80f858c7d1c5f120135a1f5dc3d0d6` (233 tracked files; no truncated tree).
- Harness: `hosseinmor/product-development-harness`, `main`, recursive tree `a8fd406bb3df605285c2bfa1db4c4c3a98b3b240`.
- Product Knowledge already lives **outside** this GitHub repository; the existing source contract identifies JobVision `https://docs-jv.jvoffice.ir/` and Cando `https://docs-cd.jvoffice.ir/`. Actual internal browser access must be verified during execution.
- Source PR inventory at this **pinned historical snapshot** included [#83](https://github.com/hosseinmor/product-knowledge/pull/83), [#106](https://github.com/hosseinmor/product-knowledge/pull/106), and [#108](https://github.com/hosseinmor/product-knowledge/pull/108). **2026-10-20 disposition update:** #108 has since merged; #83 was intentionally closed without merge and must be preserved as pinned Content migration source (`8068647d829270a694292f4511a35171229660c8`); #106 remains open. Do not assume the initial snapshot reflects current PR states.

## Inventory and ownership (classify by purpose, not folder spelling)

| Existing file group | Stage-1 disposition | Permanent owner / destination | Gate and reason |
|---|---|---|---|
| `shared/design-system/DESIGN.md`, `README.md`, `STRUCTURE.md`, `overview.md` | Keep unchanged | Karbon Design Language | Current compact semantic entry is already suitable; brand/title refresh in separate indexed-doc PR |
| `shared/design-system/foundations/`, `tokens/`, `components/`, `patterns/`, `experience-rules/`, `accessibility/`, `product-variations/` | Keep | Karbon | Reusable design/interaction semantics, a11y and allowed product identities |
| `shared/design-system/integrations/`, `governance/`, `templates/`, `handoffs/`, `audits/` | Keep; audit case-by-case for stale temporary handoffs | Karbon | Design documentation, Figma/Code/Storybook integration, change governance and evidence |
| `scripts/check_accessibility_knowledge.py`, `.github/workflows/accessibility-quality.yml` | Keep and later update obsolete `ai/design-start.md` trigger references | Karbon | Tests Karbon-owned Accessibility invariants |
| `shared/content/**` including voice, tone, terminology, localization, audience/product contexts, component copy, patterns and 14 current eval files | **Copy before remove**; no changes in stage 1 | `product-content-system` | Move complete corpus with schema identities, evidence boundaries and eval coverage preserved; PR #83 reconciled explicitly |
| `scripts/check_content_terminology.py`, `check_content_localization.py`, `check_content_components.py`, `check_content_contexts.py`, `check_content_patterns.py` | **Copy/retarget before remove** | `product-content-system` | Content-owned semantic validation; hard-coded paths and registered cases need review after copying |
| `ai/prd-writing.md`, `ai/skills/prd-writing/SKILL.md`, `templates/jira-prd.md` | Keep temporarily, then compatibility pointer or retire | Harness: `workflows/prd-draft-clarification.md` + `artifacts/prd.md` | Legacy Jira template is **not** the authoritative Harness PRD contract; do not port competing sections/requirements |
| `ai/design-start.md`, generic sections of `ai/router.md` | Temporary legacy route; replace after consumers and accessibility validator are updated | Harness: `workflows/design-exploration.md` + `artifacts/design.md` | Specialized design-language usage continues to be owned by Karbon |
| `ai/research.md` | Temporary; integrate process rather than copy a second workflow | Task-selected Harness workflow | Research is evidence gathering. No new workflow without demonstrated independent requirement |
| `docs/ai-context-retrieval-flow.md`, generic workflow parts of `docs/ai-tool-setup.md` | Retain until cross-source links verified, then replace with source-specific setup or redirect | Harness: `context-sources.yml` + source-integration guidance | Cross-source orchestration belongs to Harness; local Figma/DS setup belongs to Karbon |
| `product-knowledge-sources.yml`, `docs/product-knowledge-sources.md`, `scripts/check_product_knowledge_sources.py` | Keep unchanged in transitional repository; retire/replace at cutover | Harness source registry (product authority), plus source-owned non-canonical reminder where needed | Existing script hard-codes the transitional `repository_role` and legacy `ai/router.md` path. Must not be removed while CI still calls it |
| `scripts/generate_manifest.py`, `manifest.generated.json`, `docs/manifest.md` | Keep until both destinations have working generators | **Split** into separate Karbon and Content-owned discovery indexes, preserving IDs and related links | Current index scans both `shared/design-system/` and `shared/content/`. Do not copy the combined manifest to each destination as a false authority |
| `.github/workflows/manifest-quality.yml`, `.github/workflows/README.md`, `requirements-dev.txt` | Keep temporarily, then split jobs and dependencies | Each destination owns checks for its files | CI currently mixes manifest, Content, Product Knowledge source gate, and Karbon in one PR workflow; PR #83 and #108 both touch the combined manifest |
| `shared/product-standards/interaction-standards.md` | Do not promote as normative; only a structural draft | Karbon *if* a reusable non-duplicate rule is actually supplied | Existing file points to `experience-rules/`; no substantive independent guidance now |
| `shared/product-standards/product-principles.md`, `analytics-standards.md` | Keep as inactive, unverified scaffolds until an explicit owner determines whether they are needed | Product governance / analytics owner, **not** assumed Karbon or Harness | Empty headings are not approved product principles or event instrumentation standards |
| `shared/README.md`, root `README.md`, root `AGENTS.md` | Reframe for staged Karbon ownership without pretending cutover occurred | Karbon; cross-system entry is Harness | No active Product Knowledge is reintroduced |

## Order and verification gates

1. **PR A — ownership / route inventory**: document decision, brand, temporary status and source-only responsibilities in the existing repository; no deletes, moves, renamed repository, or indexed semantic edits.
2. **PR B — Harness federation**: register present URLs/entry points and pending destinations with explicit access checks; consolidate where generic PRD, design and research routes must eventually point. Do not copy source guidance into Harness.
3. **Content independent copy**: create and populate `product-content-system` with full content corpus, validators, evals and its own minimal entry point/manifest. Compare inventory and file hashes against a pinned source commit **plus** the reviewed status of #83. Run all five content validators, manifest freshness checks, duplicate-key checks and a standalone content-task retrieval smoke test.
4. **Karbon cutover**: after Content is verified, separate the combined manifest/CI and remove migrated Content and legacy general workflow files *in a distinct deletion PR*. Ensure all old links, current consumer paths and Accessibility checker triggers have replacements.
5. **GitHub repository rename**: rename this same repository (not recreate) to `karbon-design-language` using admin UI. Git history remains; verify URLs/redirects and update current URLs in Harness, Content, CI, Figma/document links. Do not assume repository URL exists before rename.
6. **Final reconciliation**: rerun offline validators first and then selective integration smoke checks. Model-backed evals only if a semantic invariant is altered. Merge each PR only after separate review.

## Cross-cutting correctness constraints

- Preserve exact product-scope authority; JobVision documentation cannot establish Cando policy or vice versa.
- Content Contexts and lexical data cannot create product permissions, lifecycles, eligibility or system state.
- Figma defines editable construction; Code/Storybook define runtime implementation; Karbon documents durable reusable rules, not product business logic.
- PM owns current durable PRD; Designer owns current Design Artifact; Harness owns process, not their storage. No undocumented GitLab URL/AI access assumption.
- For cross-repo paths, maintain a before/after link inventory and compare manifest `id`, `related`, and provenance values instead of string-replacing every path without review.
- No semantic rule changes in the move/rename PRs; any desired normative change receives a separate reviewable diff.

## Blocking external operations

This GitHub connector supports branch and PR/file work, but **does not expose GitHub create-repository or rename-repository administration actions**. `product-content-system` currently returned 404 for `hosseinmor/product-content-system`; this is an availability result for the checked account/path, not proof that no similarly named repository exists elsewhere. Do not infer a new repository location or silently create it in another namespace.
