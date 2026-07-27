# Product Knowledge

This repository contains the permanent, canonical knowledge of the product ecosystem.

It is organized into four main layers:

```text
shared/
→ Knowledge that is consistent across multiple products

products/
→ Product-specific overviews, capabilities, flows, domains, and decisions

templates/
→ Canonical document, evidence, and workflow output shapes

ai/
→ Stable AI workflows that discover, consume, validate, and update Product Knowledge
```

Temporary product work, initiative drafts, PRD drafts, recordings, screenshots, raw walkthrough notes, and walkthrough outputs belong in the separate `product-work` repository.

## Main principles

- Canonical documentation describes approved current product behavior.
- Proposed or unreleased behavior is not canonical.
- The default documentation set is Product overview, Capability, and Flow.
- Domain and Decision documents are created only when their additional responsibility is needed.
- Major user journeys live inside the Product overview; Journey is not a separate canonical document type, template, or folder.
- Feature is not a canonical Product Knowledge type; use Capability for durable product abilities.
- User outcomes, usage contexts, rules, states, and lifecycles are content inside their owning documents, not separate document types.
- Shared knowledge belongs in `shared/` only when its meaning and ownership are genuinely cross-product.
- Every durable product fact has one canonical owner; related documents reference rather than redefine it.
- Evidence, coverage limitations, unknowns, and blocked areas must remain visible.
- Document truth state is separate from document maturity.
- Stable metadata and the generated manifest drive discovery and relationship resolution.
- AI prepares evidence, drafts, and documentation changes; humans approve semantic decisions and final diffs.

## Knowledge model

The repository uses a minimal product model centered on Product overview, Capability, Flow, Domain, and Decision.

The repository also indexes Design System, Content, Product Standard, and Shared Domain documents through separate manifest collections and type vocabularies.

See [`knowledge-model.md`](knowledge-model.md) for canonical definitions and ownership rules.

See [`ai/retrieval-rules.md`](ai/retrieval-rules.md) for document discovery and context expansion.

## Manifest and validation

`manifest.generated.json` is generated from frontmatter. It is an index, not a second source of truth.

All current indexable documents have migrated to the common metadata envelope. CI runs strict validation on every pull request and push to `main`.

```bash
python -m pip install -r requirements-dev.txt
python scripts/knowledge.py generate
python scripts/knowledge.py check --strict
python scripts/knowledge.py report
```

Strict validation checks metadata, collection/type compatibility, ID uniqueness, related-ID resolution, truth and maturity states, empty canonical documents, and manifest freshness.

The manifest `unindexed` list must remain empty unless an explicit migration plan is reviewed and accepted.

See [`docs/manifest.md`](docs/manifest.md) for the manifest schema, collection taxonomy, and maintenance rules.

## Templates

### Canonical Product Knowledge

```text
templates/product-overview-template.md
templates/capability-template.md
templates/flow-template.md
templates/domain-template.md
templates/decision-template.md
```

### Reviewed walkthrough evidence

```text
templates/walkthrough-output-template.md
```

### Temporary workflow outputs and handoff

```text
templates/workflows/initiative-template.md
templates/workflows/prd-template.md
templates/workflows/decision-question-template.md
templates/workflows/product-knowledge-handoff-template.yaml
templates/workflows/product-knowledge-update-proposal-template.md
```

Templates define output structure and metadata. Skills define collection, reasoning, validation, stop conditions, and handoff.

## Cross-repository handoff

Released work and reviewed walkthrough evidence should enter this repository through a versioned `knowledge-handoff.yaml` rather than an informal request.

The handoff records source commit, approval or review readiness, release state, affected IDs, evidence, coverage gaps, and completion acknowledgement.

See:

```text
docs/product-work-handoff.md
templates/workflows/product-knowledge-handoff-template.yaml
```

The `product-work` repository is not currently connected here. The source-side trigger and acknowledgement must be implemented and reviewed there before the complete cross-repository lifecycle can be considered verified.

## Main workflows

### Product walkthrough

```text
A bounded product area is selected
→ AI records scope, actor, role, authentication state, and environment
→ AI inventories surfaces and entry points
→ AI follows actions through outcomes and meaningful branches
→ AI records evidence and a coverage matrix
→ Humans review gaps, unknowns, and suspected bugs
→ Reviewed walkthrough output becomes eligible input for Product Knowledge update
```

See:

```text
ai/skills/product-walkthrough/SKILL.md
```

### Initiative to PRD

```text
PM creates a short initiative brief
→ AI reads the generated manifest and relevant repository knowledge
→ AI prepares initiative.md from the approved workflow template
→ AI asks only blocking questions using the decision template
→ Humans make required decisions
→ AI generates prd.md from the approved workflow template
→ Humans approve the PRD
```

See:

```text
ai/skills/initiative-to-prd/SKILL.md
```

### Product Knowledge update

```text
Approved and released work or reviewed walkthrough evidence produces a handoff
→ AI validates handoff readiness and repository coverage
→ AI identifies canonical owners
→ AI prepares an update proposal and template-compliant patches
→ AI regenerates the manifest and runs strict validation
→ Humans review the semantic diff
→ Approved changes are merged
→ The source handoff records the PR and merge commit
```

See:

```text
ai/skills/product-knowledge-update/SKILL.md
docs/product-work-handoff.md
```
