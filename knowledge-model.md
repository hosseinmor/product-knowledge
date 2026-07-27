# Product Knowledge Model

This document defines the canonical vocabulary, ownership rules, metadata contract, and discovery model used in this repository.

The repository is a durable, machine-readable memory for current product and shared organizational knowledge. Temporary exploration, proposed behavior, initiative drafts, PRDs, raw research, and walkthrough evidence remain in `product-work` until they are reviewed and eligible to update canonical knowledge.

## Product Knowledge model

Product-specific knowledge uses five document types:

```text
Product overview
→ What the product is, who it serves, its boundaries, major abilities, and major user journeys

Capability
→ What the product is durably able to do

Flow
→ How a concrete behavior proceeds from trigger to outcome

Domain
→ Stable business concepts, rules, permissions, relationships, and lifecycle constraints

Decision
→ Why an important durable choice was approved
```

The default documentation set is:

```text
Product overview
Capability
Flow
```

Create Domain and Decision documents only when their additional responsibility is needed.

This model is not a hierarchy. A Capability may use several Domains and have several Flows. A Flow may coordinate more than one Capability. A Decision may affect any canonical document.

### Product overview

A Product overview defines the product boundary and the context needed to interpret the remaining documents.

It owns:

- Product purpose
- Primary users
- In-scope and out-of-scope boundaries
- Main Capabilities
- Major user journeys
- Key business areas and integrations

Major user journeys remain high-level sections inside the Product overview:

```text
Actor and desired outcome
→ trigger
→ major stages
→ important Capability transitions
→ completion condition
```

Journey is not a standalone canonical document type, template, or folder. A complex journey should be expanded inside the Product overview and linked to supporting Capabilities and Flows.

### Capability

A Capability is a coherent and durable product ability that enables a user or the system to achieve a recognizable outcome.

It owns:

- Purpose and value
- Actors and user outcomes
- Entry points
- Availability and permissions when Capability-specific
- High-level behavior
- Capability-specific states and restrictions
- Boundaries and dependencies
- Links to supporting Flows and governing Domain rules

Use Capability instead of Feature in Product Knowledge. Feature may be used in planning tools for proposed work; Capability describes what the current product is durably able to do.

### Flow

A Flow describes ordered product behavior for one concrete usage context from trigger to outcome.

It owns:

```text
Actor and user outcome
Trigger
Preconditions
Relevant context
Main path
Decision points and branches
State transitions
Validations
Alternate paths
Error and recovery paths
Cancellation and exit behavior
Persistence and return behavior
End states
```

Actor, user outcome, trigger, preconditions, relevant context, and expected outcome provide the information that might elsewhere be called a Scenario. Scenario is not a standalone canonical type or folder.

A Flow is behavioral documentation, not a wireframe. It may reference screens and components, but its behavior should remain understandable when the layout changes.

### Domain

A Domain is a stable business area with its own vocabulary, entities, rules, permissions, lifecycle, and relationships.

Create a Domain document only when the subject has one or more of these characteristics:

- Several related business entities
- A meaningful entity lifecycle
- Permission rules
- Rules reused by several Capabilities or Flows
- Relationships or invariants that must remain consistent
- Business terminology that requires one canonical definition

A Domain should remain meaningful when the interface is redesigned. Do not create Domains merely to mirror navigation, a team, a page, or a group of screens.

Subdomain is not a formal type. Split an oversized Domain directly into separate coherent Domain documents.

### Decision

A Decision records a durable approved choice whose rationale remains useful after the original initiative, meeting, or release is no longer active.

Create a Decision only when the choice:

- Establishes or changes a significant rule or intentional exception
- Affects permissions, lifecycle, ownership, or product boundaries
- Resolves a material trade-off between reasonable alternatives
- Is likely to be questioned or reopened later
- Affects several canonical documents

Do not create a Decision for every UI detail, copy change, unresolved proposal, meeting note, Sprint plan, backlog item, or implementation task.

A Decision owns rationale, not current behavior. The approved outcome must also be reflected in the Product overview, Domain, Capability, or Flow that owns the resulting truth.

Decision lifecycle:

```text
proposed in product-work
→ accepted and canonical
→ superseded | deprecated
```

A superseding Decision must reference the previous Decision without rewriting historical rationale.

## Embedded content, not document types

The following concepts remain structured content inside their owning documents:

- User outcome or intent
- Usage context
- Scenario fields
- Rule
- State
- Lifecycle
- Validation
- Error and recovery behavior

Ownership depends on scope:

```text
Stable business rule, permission, entity relationship, or lifecycle
→ Domain

Capability-specific restriction or availability state
→ Capability

Context-specific branch, validation, state transition, error, or recovery behavior
→ Flow
```

Task is not a Product Knowledge concept because delivery tools commonly use it for a unit of team work.

## Shared knowledge and Design System

`shared/` is a placement and ownership boundary, not a universal document type.

Knowledge belongs in `shared/` only when:

- More than one product uses it
- Its meaning is consistent across those products
- Its ownership is genuinely shared
- Product-specific exceptions do not change its core definition

The Design System is a separate knowledge family under `shared/design-system/`. It defines reusable interface foundations, tokens, Components, Patterns, accessibility rules, experience rules, product variations, governance, and UI templates. It does not define product-specific business Capabilities.

A screen, page, modal, wireframe, prototype, screenshot, or recording is evidence or representation, not a primary canonical knowledge unit.

## Canonical fact ownership

Every durable fact has one canonical owner. Related documents may explain how they use a fact, but should reference the owner rather than redefine it.

```text
Product purpose, boundary, main Capabilities, and major user journeys
→ Product overview

Stable business rule, permission, entity relationship, or lifecycle
→ Domain

Durable product ability, entry point, availability, or Capability-specific state
→ Capability

Behavioral step, branch, validation, error, recovery, persistence, or end state
→ Flow

Approved rationale and historical trade-off
→ Decision

Reusable UI foundation, token, Component, Pattern, or interaction rule
→ Design System document with the matching type

Cross-product content or product rule
→ The matching shared collection
```

When documents disagree, the document that owns the fact by scope is authoritative. The conflict must still be surfaced for human review rather than silently resolved by AI.

## Collections and document types

Metadata separates the knowledge family from the document type.

```text
collection
→ Determines ownership boundary, allowed types, and retrieval rules

type
→ Identifies the document type inside that collection
```

Supported combinations:

```text
collection: product
type: product | capability | flow | domain | decision

collection: design-system
type: overview | foundation | token | component | pattern | experience-rule |
      accessibility | product-variation | reference | governance | ui-template

collection: content
type: content-guideline

collection: product-standard
type: product-standard | documentation-guideline

collection: shared-domain
type: domain
```

`shared` is not an allowed catch-all type.

## Knowledge state and document maturity

Truth state and documentation completeness are separate dimensions.

```yaml
knowledge_state: canonical | observed | unverified | deprecated
document_maturity: scaffold | draft | reviewed | stable
```

Definitions:

- `canonical`: approved current truth
- `observed`: behavior or evidence has been observed but intended meaning is not confirmed
- `unverified`: the document or migrated metadata has not yet been semantically confirmed
- `deprecated`: no longer current, retained only when historical context is useful
- `scaffold`: headings or placeholders exist, but substantive owned facts do not
- `draft`: substantive content exists but is incomplete or awaiting review
- `reviewed`: content has been semantically reviewed
- `stable`: reviewed content expected to change infrequently

A scaffold cannot be canonical. A canonical document must contain substantive owned facts.

Proposed or unreleased behavior remains in `product-work` and must not be marked canonical.

## Common metadata envelope

All indexable documents use YAML frontmatter with a shared envelope:

```yaml
---
id: ats.recruitment-request.submit
collection: product
type: flow
product: ats
title: Submit recruitment request
summary: Describes submission, validation, and transition to approval.
knowledge_state: canonical
document_maturity: reviewed
related:
  - ats.recruitment-request
  - ats.recruitment-request.create
owner: ats-product
last_verified: 2026-07-26
---
```

Required fields:

- `id`: stable repository-wide identifier
- `collection`
- `type`
- `title`: human-readable title
- `summary`: concise retrieval description
- `knowledge_state`
- `document_maturity`
- `related`: directly related stable document IDs

Documents in the `product` collection also require `product`.

Optional fields may include:

- `owner`
- `actors`
- `domains`
- `capabilities`
- `last_verified`
- `source_refs`
- `design_refs`
- `figma_file`
- `figma_node`
- `code_refs`
- `supersedes`
- `superseded_by`

Collection-specific metadata may be added after the common envelope.

IDs must remain stable when files move. Relationships use IDs rather than relative paths.

Legacy `status` and `maturity` fields are not part of the common envelope and must be migrated deliberately.

## Generated manifest

`manifest.generated.json` is generated deterministically from frontmatter by `scripts/knowledge.py`.

The manifest contains discovery metadata only:

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

Documents that cannot yet be indexed appear in `unindexed` with an explicit reason such as missing, legacy, incomplete, or invalid metadata.

`unindexed` is a migration and coverage signal. Agents must not infer that an absent fact or document does not exist, and must not silently fall back to filename-based repository globbing.

The manifest is not a second source of product or design-system truth.

Default retrieval sequence:

```text
1. Read repository guidance and manifest.generated.json
2. Check collection coverage and the unindexed list
3. Select documents by collection, product, type, summary, and related IDs
4. Read the relevant Product overview or collection overview
5. Read the smallest sufficient set of related documents
6. Inspect evidence, coverage, unknowns, and last verification
7. Surface conflicts, stale verification, and unindexed coverage gaps
```

Detailed operational behavior belongs in `ai/retrieval-rules.md`. Manifest maintenance belongs in `docs/manifest.md`.

## Validation and CI

Repository automation validates:

- Frontmatter parsing
- Required metadata
- Collection and type compatibility
- Stable ID uniqueness
- Related-ID resolution
- Valid truth and maturity states
- `last_verified` date format
- Forbidden `.DS_Store` files
- Empty canonical documents
- Manifest freshness

During migration, missing and legacy metadata may be reported as warnings. After migration, strict validation treats them as errors.

## Choosing the right Product Knowledge type

| Question | Use |
|---|---|
| What is this product, who uses it, and what are its major journeys and boundaries? | Product overview |
| What durable ability does the product provide? | Capability |
| What exact path, branch, validation, persistence, or error behavior occurs? | Flow |
| Would this rule remain true if the entire interface changed? | Domain |
| Why was an important durable choice approved? | Decision |
| Is this reusable interface behavior rather than product behavior? | Design System collection |

## Splitting rules

Split a document only when keeping the subject together makes ownership or behavior ambiguous.

### Split a Capability when

- The abilities have independent value or entry points
- They have materially different actors, states, or dependencies
- They can change independently without making one document contradictory

### Split a Flow when

- Actor, trigger, preconditions, or outcome differ materially
- Branches obscure the main path
- The same behavior is reused independently by several Capabilities

### Split a Domain when

- Vocabulary and entities form independent groups
- Lifecycles or permissions are separate
- Different owners can change one area without changing the other

Do not split documents for every screen, click, API call, minor variant, user outcome, or usage context.

## Minimum Product Knowledge responsibilities

### Product overview

```text
Purpose
Primary users
Product boundaries
Main Capabilities
Major user journeys
Key business concepts and Domains
Integrations
Related Decisions
Evidence, coverage, and open questions
```

### Capability

```text
Purpose and value
Actors and user outcomes
Entry points
Availability and permissions
High-level behavior
Capability-specific states and rules
Dependencies and boundaries
Related Product overview, Domains, Flows, and Decisions
Evidence, coverage, and open questions
```

### Flow

```text
Actor and user outcome
Trigger and preconditions
Relevant context
Main path
Branches and validations
State transitions
Alternate, error, and recovery paths
Persistence and return behavior
End states
Related Capability and Domain rules
Evidence, coverage, and untested cases
```

### Domain

```text
Purpose and boundaries
Vocabulary
Entities and relationships
Business rules
Permissions
States and lifecycle
Exceptions
Related Capabilities
Evidence and open questions
```

### Decision

```text
Context
Problem or ambiguity
Options considered
Approved decision
Approver and date
Rationale
Consequences
Status
Affected canonical documents
Superseded or superseding Decisions
```

## Relationship with Scrum and delivery work

Product Knowledge describes durable current understanding. Scrum manages empirical delivery through the Product Backlog, Sprint Backlog, and Increment.

Product overview, Domain, Capability, Flow, and Decision are not Scrum artifacts. They provide persistent context for creating, refining, implementing, and reviewing Product Backlog items.

| Product Knowledge | Delivery relationship |
|---|---|
| Product overview | Context for Product Goal, boundaries, and major user journeys |
| Domain | Business rules and constraints that backlog items must respect |
| Capability | Current durable product ability that one or more backlog items may change |
| Flow | Input to requirements, acceptance criteria, design, and testing |
| Decision | Durable rationale for an approved choice; not a backlog item |
| Product Backlog item | Proposed unit of product change; not canonical current behavior |
| Increment | Done product change that may require Product Knowledge updates |

Recommended lifecycle:

```text
Product Knowledge
→ current product context

Initiative and PRD in product-work
→ proposed change and human decisions

Product Backlog and Sprint Backlog
→ selected delivery work

Done or released Increment
→ changed product behavior

Product Knowledge update
→ new canonical product truth and regenerated manifest
```

Product Knowledge updates may be part of the Definition of Done or release checklist when an Increment changes a rule, permission, lifecycle, Capability, Flow, product boundary, or major user journey.

Do not mirror a Jira hierarchy such as Epic → Feature → Story → Task inside Product Knowledge. Delivery hierarchy describes work; Product Knowledge describes the product.

## Canonical placement summary

```text
products/{product-id}/product-overview.md
→ Product purpose, users, boundaries, main Capabilities, and major user journeys

products/{product-id}/capabilities/
→ Durable product abilities

products/{product-id}/flows/
→ Concrete behavioral paths

products/{product-id}/domains/
→ Stable business truth when independent Domain documentation is needed

products/{product-id}/decisions/
→ Durable approved rationale when independent Decision documentation is needed

shared/design-system/
→ Reusable UI foundations, tokens, Components, Patterns, and standards

shared/content/
→ Cross-product content guidance

shared/product-standards/
→ Cross-product product and documentation standards

shared/domains/
→ Genuinely shared business Domains
```
