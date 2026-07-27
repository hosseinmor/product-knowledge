# Product Work to Product Knowledge Handoff

This document defines the interface between temporary product work and the canonical `product-knowledge` repository.

The `product-work` repository is not currently connected to this environment, so this file defines the expected contract but does not prove that the source repository implements it.

## Boundary

```text
product-work
→ Proposed work, research, walkthrough evidence, initiative decisions, PRDs, and release evidence

product-knowledge
→ Reviewed durable current understanding after release or evidence review
```

An approved PRD is not enough to update canonical knowledge. The change must also be released or otherwise confirmed as current product behavior.

A walkthrough output is not enough by itself. It must meet the Product Walkthrough coverage contract and receive human review.

## Handoff artifact

The source workflow should create:

```text
knowledge-handoff.yaml
```

using:

```text
templates/workflows/product-knowledge-handoff-template.yaml
```

The handoff is a routing and readiness record. It is not a source of product truth by itself.

## Required identity

```yaml
schema_version: 1
handoff_id: product.change-id.release-id
product: product-id
source:
  repository: product-work
  artifact_type: prd-release | walkthrough
  path:
  commit:
  artifact_id:
```

`handoff_id` must be stable and unique. Re-running the same handoff should update or reuse the existing documentation PR rather than create unrelated duplicate changes.

The source commit must identify the reviewed source state exactly. A mutable branch name is not sufficient.

## Readiness requirements

### Released-change handoff

Require:

```yaml
approval_state: approved
release_state: released
review_state: not-applicable
```

And:

- Approved PRD or equivalent requirements source
- Released implementation evidence
- Release date or release identifier
- Human approver identity
- Known differences between intended and released behavior
- Relevant QA, analytics, or rollout evidence when available

Do not trigger a canonical update for planned, in-development, QA-only, or cancelled work.

### Walkthrough handoff

Require:

```yaml
approval_state: not-applicable
release_state: not-applicable
review_state: reviewed
```

And:

- Explicit scope, actor, role, account, authentication state, and environment
- Surface inventory
- Coverage matrix
- Evidence index
- Observed, inferred, unknown, blocked, not-tested, and suspected-bug separation
- Human reviewer identity

Do not treat a reviewed walkthrough as proof of intended business rules. It may establish observed knowledge and identify facts requiring product-owner confirmation.

## Change routing

The handoff should identify known affected stable IDs:

```yaml
affected_knowledge_ids:
  - ats.domain.recruitment-request
  - ats.capability.manage-recruitment-request
```

IDs are hints for discovery, not an authorization to edit every listed document.

The Product Knowledge update workflow must still determine canonical ownership fact by fact.

When the source cannot identify an existing owner, use an empty list and describe the affected product area. Do not invent IDs or paths.

## Evidence references

`evidence_refs` may point to:

- Approved PRD
- Released implementation summary
- Release note
- Reviewed walkthrough output
- Design specification
- QA evidence
- Screenshot or recording
- Jira item

Each reference should be stable enough to review later. A link to a mutable working page is insufficient unless paired with a source commit or version.

## Coverage and suspected bugs

The source must preserve:

```yaml
known_coverage_gaps: []
suspected_bugs: []
```

A Product Knowledge update must not erase those lists merely because the main path is understood.

A suspected bug remains a bug candidate. It does not become a canonical rule unless humans confirm that the behavior is intended.

## Product Knowledge workflow

```text
1. Receive knowledge-handoff.yaml
2. Verify source identity and readiness
3. Read manifest.generated.json
4. Retrieve affected canonical owners and relevant shared collections
5. Classify findings
6. Prepare product-knowledge-update-proposal.md
7. Create or update a dedicated branch and PR
8. Regenerate manifest.generated.json
9. Run python scripts/knowledge.py check --strict
10. Receive semantic human approval
11. Merge the documentation PR
12. Write the PR and merge commit back to the source handoff record
```

Use:

```text
ai/skills/product-knowledge-update/SKILL.md
templates/workflows/product-knowledge-update-proposal-template.md
```

## Completion acknowledgement

After merge, update the source handoff:

```yaml
repository_update:
  status: completed
  pull_request: https://github.com/hosseinmor/product-knowledge/pull/123
  merge_commit: full-commit-sha
  completed_at: YYYY-MM-DD
```

This acknowledgement prevents repeated releases or automation retries from creating duplicate documentation updates.

## Failure and stop conditions

Stop the handoff when:

- The source commit cannot be identified.
- Approval, release, or walkthrough review state is missing.
- Intended and released behavior conflict without resolution.
- Relevant evidence is inaccessible.
- The Product Knowledge manifest is missing or stale.
- Canonical ownership is ambiguous and requires a human decision.
- The requested change would mark inference as canonical truth.

Record the failure in the source handoff rather than silently skipping the Product Knowledge update.

## Automation boundary

Automation may validate the handoff, retrieve documents, create a proposal, regenerate the manifest, and open a PR.

Automation must not:

- Mark a PRD or walkthrough as approved.
- Decide intended behavior from production observation alone.
- Merge a semantic product-rule change without the required human approval.
- Write directly to `main`.

## Implementation gap

This contract is implemented on the `product-knowledge` side through templates and Skills.

The source-side trigger, handoff-file creation, and completion acknowledgement must also be implemented in `product-work`. Until that repository is reviewed, the end-to-end lifecycle remains only partially verified.
