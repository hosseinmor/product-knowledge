# Product Knowledge Update

## Purpose

Update Product Knowledge after an approved product change has been released, or after missing current behavior has been recovered through a reviewed walkthrough.

The AI prepares the changes. Humans validate meaning and approve the final diff.

## Inputs

At least one change source:

- Approved PRD
- Released implementation summary
- Reviewed product decision
- Reviewed walkthrough output
- Confirmed correction to existing documentation

And:

- Product identifier
- Initiative or change identifier
- Access to relevant Product Knowledge

Optional:

- Design specification
- Technical notes
- Release notes
- Screenshots
- Recordings
- Jira tickets
- QA findings

## Core principle

```text
Source material = evidence and approved change intent
Product Knowledge = permanent canonical understanding
```

Observed production behavior must not automatically become an intended business rule.

Every durable fact must have one canonical owner. Related documents may reference or apply the fact, but should not independently redefine it.

## Workflow

### 1. Establish scope

Extract:

- Product
- Capability or affected product area
- Released change
- Actors and roles
- Usage contexts covered
- Source documents
- Release status

Do not update Product Knowledge for unreleased work unless the repository explicitly supports future-state documentation.

### 2. Find relevant Product Knowledge

Follow `ai/retrieval-rules.md`.

Use the generated manifest to discover the smallest sufficient set of documents, then read only relevant documents from:

- Shared knowledge
- Product overview
- Capability
- Flow
- Domain when stable business truth is involved
- Accepted Decision when durable rationale is involved

Check document metadata before using the content:

- Prefer `knowledge_state: canonical`
- Surface `observed` content as unconfirmed
- Ignore `deprecated` content as current behavior
- Use `document_maturity` as a review signal, not as truth status

### 3. Classify each change

Use:

- `confirmed`
- `observed`
- `unknown`
- `suspected-bug`

Route them as follows:

```text
confirmed
→ Product Knowledge patch

observed
→ observed knowledge or open question

unknown
→ open question

suspected-bug
→ proposed bug ticket, not a canonical rule
```

### 4. Determine canonical ownership and documentation impact

For each changed fact, first identify its canonical owner:

```text
Product overview
→ product purpose, boundaries, major Capabilities, and major user journeys

Domain
→ stable business rules, permissions, lifecycle constraints, and entity relationships

Capability
→ product ability, actors, entry points, Capability-specific states, and high-level behavior

Flow
→ actor, user outcome, trigger, preconditions, steps, transitions, validations, alternate paths, errors, and recovery

Decision
→ durable approved rationale requiring historical context

Shared
→ cross-product knowledge whose meaning and ownership are consistent across products
```

For each relevant document choose:

- `update`
- `reference update only`
- `no change`
- `review required`
- `new document required`

Do not duplicate the changed fact across all related documents. Update the owner, then update references or applications only where needed.

Do not create standalone Journey, User Goal, Scenario, Rule, State, Lifecycle, or Subdomain documents. Represent those concepts inside their owning Product overview, Capability, Flow, or Domain.

### 5. Evaluate Decision impact

A working decision, Jira item, meeting outcome, or PRD statement does not automatically require a canonical Decision document.

Create or update a Decision only when the approved rationale is durable, such as when the change:

- Establishes a significant rule or intentional exception
- Changes permission, lifecycle, ownership, or product boundaries
- Resolves a material trade-off between reasonable alternatives
- Is likely to be questioned or reopened later
- Affects several Product Knowledge documents

The Decision records why the choice was made. The relevant Product overview, Domain, Capability, or Flow still owns the resulting current behavior.

When a new Decision replaces an old one:

- Mark the previous Decision as `superseded`
- Reference the new Decision with `superseded_by`
- Reference the previous Decision from the new one with `supersedes`
- Preserve the historical rationale

### 6. Prepare patches

Edit only affected sections.

For every patch include:

- Reason
- Source
- Classification
- Canonical owner
- Required reviewer

When a file is created or materially updated:

- Add or validate required frontmatter
- Keep its stable `id`
- Update `related` IDs
- Update `last_verified` only when the content was actually reviewed
- Keep `knowledge_state` separate from `document_maturity`

Do not rewrite entire documents unless their structure is fundamentally unusable.

### 7. Stop on sensitive semantic changes

Require explicit human review for:

- New business rules
- Permission changes
- Lifecycle changes
- Entity relationship changes
- Removal of an existing rule
- Change from current to intended behavior
- Generalization from one role or usage context to all users
- Conflicts between PRD and production
- Moving product-specific knowledge into `shared/`
- Changing canonical ownership of an existing fact
- Accepting, superseding, or deprecating a Decision

### 8. Present a reviewable diff

Use:

```md
# Product Knowledge Update Proposal

## Scope
## Sources Reviewed
## Documentation Impact
## Canonical Ownership
## Proposed Patches
## Decision Impact
## Metadata and Relationship Changes
## Open Questions
## Suspected Bugs
## Review Required
## Files With No Change
```

When repository access is available:

```text
create branch
→ edit files
→ rebuild the generated manifest when available
→ show diff
→ wait for approval
→ merge only after human approval
```

### 9. Complete the update

The update is complete when:

- All confirmed changes are reflected in their canonical owner documents
- Related documents reference rather than redefine owned facts
- Unknowns remain visible
- Suspected bugs are not recorded as rules
- Sensitive changes are approved
- Durable rationale is preserved in Decisions when required
- Metadata and relationships remain valid
- No important confirmed knowledge remains only in a PRD or walkthrough output
- The documentation diff is merged

## Human responsibilities

Humans are responsible for:

- Confirming semantic meaning
- Approving business rules and permissions
- Resolving conflicts
- Approving durable Decisions
- Approving the final documentation diff
