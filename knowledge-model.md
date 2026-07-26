# Product Knowledge Model

This document defines the vocabulary and ownership rules used to organize canonical Product Knowledge in this repository.

The repository is designed to act as a durable, machine-readable product memory. AI workflows should be able to discover and read only the relevant knowledge needed to support research, product design, specification, and implementation work without mixing current product truth with temporary or proposed work.

## Core principle

The model describes the product from several complementary perspectives:

```text
Business truth      → Domain
End-to-end outcome  → Journey
User intent         → User Goal
Concrete context    → Scenario
Product ability     → Capability
Behavioral path     → Flow
Decision history    → Decision
```

These concepts are related, but they are not interchangeable and do not form one strict hierarchy.

A Capability can operate inside a Domain, support several Journeys, and have multiple Flows. A Flow may coordinate several Capabilities. A Journey may cross several Domains. A Decision may affect any of these documents.

## Relationship model

```text
Product
├── Business model
│   ├── Domain
│   └── optional Subdomain
├── Experience model
│   ├── Journey
│   ├── User Goal
│   ├── Scenario
│   └── Flow
├── Capability model
│   └── Capability
└── Decision history
    └── Decision
```

This diagram is a classification model, not a required folder tree.

## Product

A Product is a coherent product boundary with its own purpose, primary users, capabilities, and product-specific rules.

A Product overview answers:

- Why the product exists
- Who primarily uses it
- What major capabilities it provides
- What is inside or outside its boundary
- Which Domains and Journeys define it

Product-specific knowledge belongs under `products/{product-id}/`.

## Domain

A Domain is a stable business area with its own vocabulary, entities, rules, permissions, lifecycles, and relationships.

A Domain answers:

- What business concepts exist
- What each concept means
- Which rules must always hold
- Who may perform which operations
- Which states an entity can have
- Which transitions are valid
- How entities relate to one another

Typical Domain content includes:

- Definitions and terminology
- Entities and value objects
- Business rules and invariants
- Permissions
- Lifecycle and status transitions
- Entity relationships
- Cross-capability constraints
- Approved exceptions

A Domain should remain meaningful even if the interface is redesigned.

Do not use a Domain document to describe screen layout, click-by-click interaction, local copy, or temporary implementation detail.

## Subdomain

A Subdomain is an optional decomposition of a large Domain into a coherent business area with distinct vocabulary, rules, lifecycle, or ownership.

Create a Subdomain only when the parent Domain has become difficult to understand or maintain as one subject.

A Subdomain is justified when several of these are true:

- It has a distinct set of entities or terms
- It has independent business rules
- It has a separate lifecycle
- It has meaningfully different ownership
- It can be discussed without repeatedly explaining the whole parent Domain

Do not create a Subdomain merely to mirror navigation, teams, pages, or groups of Capabilities.

Subdomain is not a required first-class folder in the current repository structure. It may be represented as a section or as a separate Domain document when needed.

## Journey

A Journey describes how an actor reaches an end-to-end outcome across major stages, touchpoints, Capabilities, or products.

A Journey answers:

- Who is pursuing the outcome
- What starts the Journey
- What outcome completes it
- Which major stages the actor passes through
- Where responsibility or context changes
- Which Capabilities and Flows support each stage

Journey documentation stays at a high level. It describes stages and major transitions, not every interaction step.

A Journey may include:

- Actor and goal
- Trigger and completion condition
- Major stages
- Cross-capability transitions
- Cross-product handoffs
- Important states or dependencies
- Related User Goals, Capabilities, and Flows

Do not create a Journey for every page, modal, or short interaction. A Journey should represent a meaningful user outcome that usually spans more than one local action.

## User Goal

A User Goal is an immediate outcome an actor is trying to achieve.

Examples include:

- Submit a request
- Compare two options
- Add an approver
- Review a candidate
- Correct invalid information

A User Goal describes user intent, not the interface action used to achieve it.

For example, “choose an approval workflow” is a User Goal. “Click the dropdown” is an interaction step.

User Goals normally appear inside Journey, Capability, or Flow documents. They do not require a standalone canonical folder unless they are reused broadly and need independent definition.

Use `User Goal` instead of `Task` in Product Knowledge. In delivery tools such as Jira, Task commonly means a unit of team work and should not be confused with user intent.

## Scenario

A Scenario is a concrete situation in which an actor attempts a User Goal or uses a Capability.

A Scenario combines:

- Actor or role
- Goal
- Trigger
- Preconditions
- Relevant context
- Expected outcome

A Scenario narrows a general Capability into a case that can be described as a Flow.

The same Capability may have different Scenarios for:

- A first-time user and a returning user
- An owner and an approver
- A valid submission and an incomplete submission
- A connected entity and a standalone entity

Scenarios usually live inside Capability or Flow documents rather than in a separate folder.

## Capability

A Capability is a coherent and durable product ability that enables a user or the system to achieve a recognizable outcome.

A Capability answers:

- What the product enables
- Who can use it
- Why it exists
- Where it can be entered
- What major states it has
- What high-level behavior it provides
- What its boundaries and dependencies are

Typical Capability content includes:

- Purpose and value
- Actors
- Entry points
- Main user goals
- High-level behavior
- Capability-specific states
- Capability-specific rules
- Dependencies
- Boundaries and exclusions
- Related Domains, Journeys, and Flows

A Capability is not necessarily one page. It may span several screens, entry points, or system operations.

A Capability document should not duplicate stable business truth owned by a Domain. It should reference the Domain rule and explain how the product ability uses it.

Use `Capability` instead of `Feature` in canonical Product Knowledge. In planning tools, Feature may describe a proposed change, Epic, or backlog item. Capability describes what the product is durably able to do, independent of how many initiatives or backlog items created it.

## Flow

A Flow describes the ordered behavior for one Scenario from trigger to outcome.

A Flow answers:

- What starts the behavior
- What preconditions must hold
- Which steps occur
- Where decisions or branches happen
- Which validations apply
- What alternate or error paths exist
- Which end states are possible

Typical Flow content includes:

- Actor and Scenario
- Trigger
- Preconditions
- Main path
- Decision points
- State transitions
- Validations
- Alternate paths
- Error and recovery paths
- Completion and cancellation outcomes

A Flow is behavioral documentation, not a wireframe. It may reference screens and components, but the documented behavior should remain understandable without the current layout.

One Capability can have several Flows. One Flow can coordinate several Capabilities when the Scenario crosses capability boundaries.

## State and lifecycle

State describes the current condition of an entity, Capability, or interaction. Lifecycle describes the valid progression between states over time.

Ownership depends on scope:

- Stable entity states and transition rules belong in the relevant Domain
- Capability-level presentation or availability states belong in the Capability
- Step-level transitions and validation outcomes belong in the Flow

Do not define the same lifecycle independently in several documents. Keep the canonical lifecycle in the Domain and reference it elsewhere.

## Rule

A Rule is a constraint that determines allowed product behavior.

Rule placement depends on stability and scope:

- Cross-capability business invariant → Domain
- Capability-specific constraint → Capability
- Scenario-specific validation or branch → Flow
- Cross-product rule with consistent meaning → Shared knowledge

A visual convention is not a business rule. Design-system behavior belongs in `shared/design-system/`.

## Canonical fact ownership

Every durable product fact must have one canonical owner.

Other documents may summarize or apply the fact, but they should reference its owner instead of redefining it independently.

Examples:

```text
A recruitment request may move from Draft to In Review
→ Domain owns the lifecycle rule

The submit action is available only while the request is Draft
→ Capability owns the availability behavior and references the Domain state

Submitting an incomplete request returns validation errors
→ Flow owns the scenario-specific validation path
```

When two documents disagree, the document that owns the fact by scope is authoritative. The conflict must still be reviewed rather than silently resolved by AI.

## Decision

A Decision records a durable, approved choice whose rationale will remain useful after the original initiative, meeting, or release is no longer active.

A Decision answers:

- What problem, ambiguity, or trade-off existed
- Which options were materially considered
- What was approved
- Who approved it
- Why it was approved
- Which constraints or consequences follow
- Which canonical documents were affected
- Whether the Decision is still active or has been superseded

Create a Decision document when one or more of these are true:

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

A Decision is not the owner of current product behavior. The approved outcome must also be reflected in the relevant Domain, Journey, Capability, or Flow document.

For example:

```text
Decision
→ Records why editing an active approval workflow is restricted and which alternatives were rejected

Domain
→ Owns the approved rule describing which changes are allowed

Capability and Flow
→ Explain how the restriction appears and behaves in the product
```

Recommended Decision lifecycle:

```text
proposed
→ accepted
→ superseded | deprecated
```

Only `accepted` Decisions are canonical. Proposed decisions remain in `product-work` until approved.

A superseding Decision must reference the previous Decision. Do not rewrite historical rationale to make it appear that the new choice was always intended.

## Shared knowledge

Shared is a placement rule, not a separate behavioral concept.

Knowledge belongs in `shared/` only when:

- More than one product uses it
- Its meaning is consistent across those products
- Its ownership is genuinely shared
- Product-specific exceptions do not change the core definition

Do not move knowledge into `shared/` merely to avoid duplication.

## Design-system component and pattern

A Component is a reusable interface building block. A Pattern is a reusable interaction or composition rule made from one or more components.

Components and Patterns define interface behavior, anatomy, states, accessibility, and usage rules. They do not define product-specific business capability.

They belong under `shared/design-system/`, not under product Capabilities or Domains.

A Product Capability may consume a Component or Pattern, but the two remain separate kinds of knowledge.

## Screen, page, modal, and UI artifact

A screen, page, modal, wireframe, prototype, screenshot, or recording is usually a representation or source of evidence, not the primary canonical knowledge unit.

Document product behavior as Domain, Journey, Capability, or Flow knowledge. Reference the UI artifact when it helps locate or verify the behavior.

Temporary design exploration and unreleased specifications belong in the separate `product-work` repository.

## Knowledge state and document maturity

The truth status of the content must be separated from the quality or completeness of the document.

Use:

```yaml
knowledge_state: canonical | observed | deprecated
document_maturity: draft | reviewed | stable
```

Definitions:

- `canonical`: approved current product truth
- `observed`: current behavior has been observed but its intended meaning is not yet confirmed
- `deprecated`: no longer current, retained only when historical context is useful
- `draft`: the document is incomplete or awaiting review
- `reviewed`: the document has been semantically reviewed
- `stable`: the document is reviewed and expected to change infrequently

Examples:

```yaml
knowledge_state: canonical
document_maturity: draft
```

The content describes current approved behavior, but the documentation is incomplete.

```yaml
knowledge_state: observed
document_maturity: reviewed
```

The observation is documented accurately, but it has not been confirmed as intended product behavior.

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
  - ats.recruitment-request.domain
  - ats.recruitment-request.create
owner: ats-product
last_verified: 2026-07-26
---
```

Required fields:

- `id`: stable repository-wide identifier
- `type`: product, domain, journey, capability, flow, decision, or shared
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
- `journeys`
- `capabilities`
- `last_verified`
- `source_refs`
- `design_refs`
- `supersedes`
- `superseded_by`

IDs must remain stable when a file is moved. Relationships should use IDs rather than relative paths.

## Manifest and AI retrieval

The repository should generate `manifest.generated.json` from document frontmatter.

The generated manifest should contain only discovery information:

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
4. Read the smallest sufficient set of Domains, Journeys, Capabilities, Flows, and Decisions
5. Follow explicit relationships only when additional context is needed
6. Surface conflicts, observed knowledge, stale verification dates, and missing documents
```

AI should not read the entire repository by default. It should expand context only when the current documents indicate a dependency or unresolved ambiguity.

Detailed operational rules belong in `ai/retrieval-rules.md`.

## Choosing the right document type

| Question | Use |
|---|---|
| Would this remain true if the entire interface changed? | Domain |
| Does this describe an end-to-end outcome across major stages or capabilities? | Journey |
| What immediate outcome is the actor trying to achieve? | User Goal inside another document |
| Under which actor, trigger, and preconditions does this happen? | Scenario inside a Capability or Flow |
| What durable ability does the product provide? | Capability |
| What exact path, branch, validation, or error behavior occurs? | Flow |
| Why was a durable choice approved? | Decision |
| Is the meaning genuinely consistent across products? | Shared placement |
| Is this reusable interface behavior rather than business behavior? | Design-system Component or Pattern |

## Splitting rules

Split a document when keeping the subject together makes ownership, rules, or behavior ambiguous.

### Split a Domain when

- Vocabulary and entities form clearly independent groups
- Lifecycles or permissions are separate
- Different owners can change one area without changing the other

### Split a Journey when

- Actors pursue materially different outcomes
- Triggers or completion conditions differ
- The stages no longer form one understandable end-to-end story

### Split a Capability when

- The abilities have independent value or entry points
- They have materially different actors, states, or dependencies
- They can change independently without making one document contradictory

### Split a Flow when

- Actor, trigger, preconditions, or outcome differ materially
- Branches have become large enough to obscure the main path
- The same path is reused independently by several Capabilities

Do not split documents for every screen, click, API call, or minor variant.

## Minimum document responsibilities

### Domain

```text
Purpose and boundaries
Vocabulary
Entities and relationships
Business rules
Permissions
States and lifecycle
Exceptions
Related Capabilities and Journeys
```

### Journey

```text
Actor and end-to-end goal
Trigger
Completion condition
Major stages
Cross-capability or cross-product transitions
Related User Goals, Capabilities, and Flows
```

### Capability

```text
Purpose
Actors
Entry points
User Goals
High-level behavior
Capability-specific states and rules
Dependencies and boundaries
Related Domain, Journey, and Flows
```

### Flow

```text
Scenario
Trigger and preconditions
Main path
Branches and validations
Alternate and error paths
End states
Related Capability and Domain rules
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

Concepts such as Domain, Journey, Capability, Flow, Scenario, and Decision are not Scrum artifacts. They provide persistent context for creating, refining, implementing, and reviewing Product Backlog items.

Recommended mapping:

| Product Knowledge | Delivery relationship |
|---|---|
| Product overview | Context for Product Goal and product boundaries |
| Domain | Business rules and constraints that backlog items must respect |
| Journey | End-to-end outcome context for discovery and prioritization |
| Capability | Current durable product ability that one or more backlog items may change |
| Scenario and Flow | Input to requirements, acceptance criteria, design, and testing |
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

The organization may include Product Knowledge updates in its Definition of Done or release checklist when an Increment changes a rule, permission, lifecycle, Journey, Capability, or Flow.

Do not mirror a Jira hierarchy such as Epic → Feature → Story → Task inside Product Knowledge. Delivery hierarchy describes work. Product Knowledge describes the product.

## Illustrative example

The following example is only for understanding the model; it does not establish canonical product rules.

```text
Domain
→ Recruitment Request
→ Request, workflow, approval step, approver, permissions, and lifecycle rules

Journey
→ An employer recognizes a hiring need and continues until the need is fulfilled

Capability
→ Create recruitment request
→ Review and approve request
→ Manage approval workflow

User Goal
→ Choose a workflow
→ Add an approver
→ Submit the request

Scenario
→ A request owner submits a complete draft connected to an approval workflow

Flow
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
→ Product purpose, users, boundaries, capabilities, and key concepts

products/{product-id}/domains/
→ Stable business truth

products/{product-id}/journeys/
→ End-to-end user outcomes and stages

products/{product-id}/capabilities/
→ Durable product abilities

products/{product-id}/flows/
→ Scenario-specific behavioral paths

products/{product-id}/decisions/
→ Durable approved decision history

shared/
→ Genuinely cross-product knowledge

shared/design-system/
→ Reusable UI foundations, components, patterns, and standards
```
