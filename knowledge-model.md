# Product Knowledge Model

This document defines the minimal vocabulary and ownership rules used to organize canonical Product Knowledge in this repository.

The repository is a durable, machine-readable product memory. AI workflows should be able to discover and read only the knowledge needed for a task without mixing current product truth with temporary or proposed work.

## Minimal model

Use five primary document types:

```text
Product overview
→ What the product is, who it serves, its boundaries, major abilities, and major user journeys

Capability
→ What the product is durably able to do

Flow
→ How a specific behavior proceeds from trigger to outcome

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

The model is not a hierarchy. A Capability may use rules from several Domains, appear in several user journeys, and have several Flows. A Flow may coordinate more than one Capability. A Decision may affect any canonical document.

## Product overview

A Product overview defines the product boundary and supplies the context needed to interpret all other documents.

It answers:

- Why the product exists
- Who primarily uses it
- What major Capabilities it provides
- What is inside and outside its boundary
- What the major user journeys are
- Which Domains are important

Product-specific knowledge belongs under `products/{product-id}/`.

Major user journeys should normally be documented as a section of the Product overview:

```text
Trigger
→ major stages
→ important capability transitions
→ completion outcome
```

Create a separate Journey document only when an end-to-end journey is too complex to remain understandable in the Product overview, crosses several products, or requires independent ownership and maintenance.

Journey is therefore an optional extension, not a required primary document type or folder.

## Capability

A Capability is a coherent and durable product ability that enables a user or the system to achieve a recognizable outcome.

A Capability answers:

- What the product enables
- Why the ability exists
- Who can use it
- Where it can be entered
- What high-level behavior it provides
- What capability-specific states or restrictions apply
- What its boundaries and dependencies are

Typical Capability content includes:

- Purpose and value
- Actors
- User outcomes
- Entry points
- High-level behavior
- Capability-specific states and rules
- Dependencies
- Boundaries and exclusions
- Related Product overview, Domains, Flows, and Decisions

A Capability is not necessarily one page. It may span several screens, entry points, or system operations.

Use `Capability` instead of `Feature` in canonical Product Knowledge. In planning tools, Feature may describe proposed work, an Epic, or a backlog item. Capability describes what the current product is durably able to do, independent of how many initiatives or backlog items created it.

A Capability must not duplicate stable business truth owned by a Domain. It should reference the Domain rule and explain how the product ability applies it.

## Flow

A Flow describes ordered product behavior for one concrete usage context from trigger to outcome.

A Flow answers:

- Who performs or initiates the behavior
- What starts it
- What preconditions must hold
- Which steps occur
- Where decisions or branches happen
- Which validations apply
- What alternate or error paths exist
- Which end states are possible

Typical Flow content includes:

```text
Actor
Goal or expected outcome
Trigger
Preconditions
Main path
Decision points
State transitions
Validations
Alternate paths
Error and recovery paths
Completion and cancellation outcomes
```

Actor, goal, trigger, preconditions, and expected outcome provide the context that might elsewhere be called a scenario. They remain fields inside the Flow rather than a separate canonical concept or folder.

A Flow is behavioral documentation, not a wireframe. It may reference screens and components, but the behavior should remain understandable if the current layout changes.

One Capability may have several Flows. One Flow may coordinate several Capabilities when the behavior crosses capability boundaries.

## Domain

A Domain is a stable business area with its own vocabulary, entities, rules, permissions, lifecycle, and relationships.

Create a Domain document when the subject has one or more of these characteristics:

- Several related business entities
- A meaningful entity lifecycle
- Permission rules
- Rules reused by several Capabilities or Flows
- Relationships or invariants that must remain consistent
- Business terminology that requires one canonical definition

A Domain answers:

- What business concepts exist
- What each concept means
- Which rules must always hold
- Who may perform which operations
- Which states an entity can have
- Which transitions are valid
- How entities relate to one another

Typical Domain content includes:

- Purpose and boundaries
- Vocabulary
- Entities and relationships
- Business rules and invariants
- Permissions
- States and lifecycle
- Approved exceptions
- Related Capabilities and Product overview

A Domain should remain meaningful even if the interface is redesigned.

Do not create a Domain merely to mirror navigation, a team, a page, or a group of screens. Do not create a formal Subdomain type. When a Domain becomes too large, split it directly into separate coherent Domain documents.

## Decision

A Decision records a durable, approved choice whose rationale will remain useful after the original initiative, meeting, or release is no longer active.

A Decision answers:

- What problem, ambiguity, or trade-off existed
- Which options were materially considered
- What was approved
- Who approved it and when
- Why it was approved
- Which constraints or consequences follow
- Which canonical documents were affected
- Whether the Decision is active or has been superseded

Create a Decision document only when one or more of these are true:

- The choice establishes or changes a significant business rule
- The choice creates an intentional exception
- The choice affects permissions, lifecycle, ownership, or product boundaries
- Several reasonable alternatives existed
- The trade-off is likely to be questioned or reopened later
- Understanding the rationale prevents an apparently simpler but incorrect future change
- The choice affects several canonical documents

Do not create a Decision document for:

- Every UI detail or copy change
- An unresolved proposal
- A meeting note with no approved outcome
- A temporary Sprint plan
- A backlog item or implementation task
- A fact that needs no historical rationale

A Decision is not the owner of current product behavior. The approved outcome must also be reflected in the document that owns the resulting current truth.

For example:

```text
Decision
→ Records why editing an active approval workflow is restricted and which alternatives were rejected

Domain
→ Owns the approved rule describing which changes are allowed

Capability and Flow
→ Explain how the restriction is available and behaves in the product
```

Recommended Decision lifecycle:

```text
proposed
→ accepted
→ superseded | deprecated
```

Only accepted Decisions are canonical. Proposed decisions remain in `product-work` until approved.

A superseding Decision must reference the previous Decision. Do not rewrite historical rationale to make it appear that the new choice was always intended.

## Concepts that are not standalone document types

The following concepts are useful inside documents but do not require their own folders or canonical document types.

### User outcome or goal

Describe the immediate outcome an actor is trying to achieve inside the relevant Product overview, Capability, or Flow.

Use user intent rather than interface actions:

```text
Submit a request
```

not:

```text
Click the submit button
```

Do not use `Task` as a Product Knowledge concept. In Jira and other delivery tools, Task commonly means a unit of team work.

### Usage context

Represent a concrete situation through fields inside a Flow:

```text
Actor
Goal
Trigger
Preconditions
Relevant context
Expected outcome
```

Do not maintain Scenario as a separate canonical type or folder.

### Rule

A Rule is a constraint that determines allowed product behavior. Its owner depends on scope:

- Stable or cross-capability business invariant → Domain
- Capability-specific restriction → Capability
- Context-specific validation or branch → Flow
- Cross-product rule with consistent meaning and ownership → Shared knowledge

A Rule is a content element, not a standalone document type.

### State and lifecycle

State describes the current condition of an entity, Capability, or interaction. Lifecycle describes valid progression between states.

Ownership depends on scope:

- Stable entity states and transition rules → Domain
- Capability availability or presentation states → Capability
- Step-level transitions and validation outcomes → Flow

State and lifecycle are content elements, not standalone document types.

### Shared knowledge

Shared is a placement rule, not a behavioral document type.

Knowledge belongs in `shared/` only when:

- More than one product uses it
- Its meaning is consistent across those products
- Its ownership is genuinely shared
- Product-specific exceptions do not change the core definition

Do not move knowledge into `shared/` merely to avoid duplication.

### Design-system Component and Pattern

A Component is a reusable interface building block. A Pattern is a reusable interaction or composition rule made from one or more Components.

Components and Patterns define interface behavior, anatomy, states, accessibility, and usage rules. They do not define product-specific business capabilities.

They belong under `shared/design-system/`.

### Screen and UI artifact

A screen, page, modal, wireframe, prototype, screenshot, or recording is a representation or source of evidence, not the primary canonical knowledge unit.

Document product behavior as Product overview, Capability, Flow, or Domain knowledge. Reference the UI artifact when it helps locate or verify behavior.

Temporary design exploration and unreleased specifications belong in the separate `product-work` repository.

## Canonical fact ownership

Every durable product fact must have one canonical owner.

Other documents may summarize or apply the fact, but they should reference its owner rather than redefine it independently.

```text
Product boundary and major user journey
→ Product overview, unless a complex Journey has a dedicated document

Stable business rule, permission, entity relationship, or lifecycle
→ Domain

Durable product ability, entry point, availability, or capability-specific state
→ Capability

Behavioral step, branch, validation, error, or recovery path
→ Flow

Approved rationale and historical trade-off
→ Decision

Cross-product rule with genuinely shared meaning
→ Shared knowledge
```

When two documents disagree, the document that owns the fact by scope is authoritative. The conflict must still be reviewed rather than silently resolved by AI.

## Knowledge state and document maturity

The truth status of content must be separated from the quality or completeness of its documentation.

Use:

```yaml
knowledge_state: canonical | observed | deprecated
document_maturity: draft | reviewed | stable
```

Definitions:

- `canonical`: approved current product truth
- `observed`: current behavior has been observed but its intended meaning is not confirmed
- `deprecated`: no longer current, retained only when historical context is useful
- `draft`: the document is incomplete or awaiting review
- `reviewed`: the document has been semantically reviewed
- `stable`: the document is reviewed and expected to change infrequently

Proposed or unreleased behavior does not use these states in Product Knowledge. It remains in `product-work`.

## Document metadata

Canonical documents should use YAML frontmatter so humans and AI workflows can identify, filter, and relate knowledge without reading every file.

Minimum metadata:

```yaml
---
id: ats.recruitment-request.submit
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
- `type`: product, domain, capability, flow, decision, journey (optional), or shared
- `title`: human-readable title
- `summary`: concise retrieval description
- `knowledge_state`
- `document_maturity`
- `related`: IDs of directly related canonical documents

Product-specific documents also require `product`.

Optional metadata may include:

- `owner`
- `actors`
- `domains`
- `capabilities`
- `last_verified`
- `source_refs`
- `design_refs`
- `supersedes`
- `superseded_by`

IDs must remain stable when a file is moved. Relationships should use IDs rather than relative paths.

## Manifest and AI retrieval

The repository should generate `manifest.generated.json` from document frontmatter.

The generated manifest contains discovery information only:

```text
id
path
type
product
title
summary
knowledge_state
document_maturity
related IDs
last_verified
```

The manifest is generated output and must not become a second source of product truth.

Default retrieval sequence:

```text
1. Read repository guidance and the generated manifest
2. Select documents by product, type, summary, and related IDs
3. Read the relevant Product overview
4. Read the smallest sufficient set of Capabilities and Flows
5. Read Domain rules and accepted Decisions only when relevant
6. Read a separate Journey only when the Product overview or relationships identify one
7. Surface conflicts, observed knowledge, stale verification dates, and missing documents
```

AI should not read the entire repository by default. Detailed operational rules belong in `ai/retrieval-rules.md`.

## Choosing the right document type

| Question | Use |
|---|---|
| What is this product, who uses it, and what are its major journeys and boundaries? | Product overview |
| What durable ability does the product provide? | Capability |
| What exact path, branch, validation, or error behavior occurs? | Flow |
| Would this rule remain true if the entire interface changed? | Domain |
| Why was an important durable choice approved? | Decision |
| Is an end-to-end journey too complex for the Product overview? | Optional Journey |
| Is this reusable interface behavior rather than product behavior? | Design-system Component or Pattern |

## Splitting rules

Split a document only when keeping the subject together makes ownership or behavior ambiguous.

### Split a Capability when

- The abilities have independent value or entry points
- They have materially different actors, states, or dependencies
- They can change independently without making one document contradictory

### Split a Flow when

- Actor, trigger, preconditions, or outcome differ materially
- Branches have become large enough to obscure the main path
- The same behavior is reused independently by several Capabilities

### Split a Domain when

- Vocabulary and entities form independent groups
- Lifecycles or permissions are separate
- Different owners can change one area without changing the other

Do not split documents for every screen, click, API call, minor variant, user goal, or scenario.

## Minimum document responsibilities

### Product overview

```text
Purpose
Primary users
Product boundaries
Main Capabilities
Major user journeys
Key business concepts and Domains
```

### Capability

```text
Purpose
Actors and user outcomes
Entry points
High-level behavior
Capability-specific states and rules
Dependencies and boundaries
Related Product overview, Domain, Flows, and Decisions
```

### Flow

```text
Actor and goal
Trigger and preconditions
Main path
Branches and validations
Alternate and error paths
End states
Related Capability and Domain rules
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

Product Knowledge and Scrum serve different purposes.

Product Knowledge describes durable current understanding. Scrum manages empirical delivery work through the Product Backlog, Sprint Backlog, and Increment.

Product overview, Domain, Capability, Flow, and Decision are not Scrum artifacts. They provide persistent context for creating, refining, implementing, and reviewing Product Backlog items.

| Product Knowledge | Delivery relationship |
|---|---|
| Product overview | Context for Product Goal, boundaries, and major user journeys |
| Domain | Business rules and constraints that backlog items must respect |
| Capability | Current durable product ability that one or more backlog items may change |
| Flow | Input to requirements, acceptance criteria, design, and testing |
| Decision | Durable rationale for an approved choice; not a backlog item |
| Product Backlog item | Proposed unit of product change; not canonical current behavior |
| Increment | Done product change that may require canonical documentation updates |

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
→ new canonical product truth
```

The organization may include Product Knowledge updates in its Definition of Done or release checklist when an Increment changes a rule, permission, lifecycle, Capability, Flow, product boundary, or major user journey.

Do not mirror a Jira hierarchy such as Epic → Feature → Story → Task inside Product Knowledge. Delivery hierarchy describes work. Product Knowledge describes the product.

## Illustrative example

The following example is only for understanding the model; it does not establish canonical product rules.

```text
Product overview
→ ATS purpose, users, boundaries, main capabilities, and the journey from hiring need to fulfillment

Domain
→ Recruitment Request
→ Request, workflow, approval step, approver, permissions, and lifecycle rules

Capability
→ Create recruitment request
→ Review and approve request
→ Manage approval workflow

Flow
→ A request owner submits a complete draft connected to an approval workflow
→ Validate the draft
→ Submit it
→ Move it to the first approval step
→ Handle approval, rejection, or error paths

Decision
→ Record why editing an active workflow is restricted and which alternatives were rejected
```

## Canonical placement summary

```text
products/{product-id}/product-overview.md
→ Product purpose, users, boundaries, major capabilities, and major journeys

products/{product-id}/capabilities/
→ Durable product abilities

products/{product-id}/flows/
→ Concrete behavioral paths

products/{product-id}/domains/
→ Stable business truth when independent Domain documentation is needed

products/{product-id}/decisions/
→ Durable approved rationale when independent Decision documentation is needed

products/{product-id}/journeys/
→ Optional complex end-to-end journeys only

shared/
→ Genuinely cross-product knowledge

shared/design-system/
→ Reusable UI foundations, components, patterns, and standards
```