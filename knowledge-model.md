# Product Knowledge Model

This document defines the vocabulary used to organize canonical Product Knowledge in this repository.

Its purpose is to keep different kinds of knowledge separate without forcing them into one strict hierarchy.

## Core principle

The model describes the product from several complementary perspectives:

```text
Business truth   → Domain
User experience  → Journey
User intent      → Task
Concrete context → Scenario
Product ability  → Feature
Behavioral path  → Flow
Decision history → Decision
```

These concepts are related, but they are not interchangeable.

A Feature can operate inside a Domain, appear in several Journeys, and have multiple Flows. A Flow may coordinate more than one Feature. A Journey may cross several Domains.

## Relationship model

```text
Product
├── Business model
│   ├── Domain
│   └── optional Subdomain
├── Experience model
│   ├── Journey
│   ├── Task
│   ├── Scenario
│   └── Flow
├── Capability model
│   └── Feature
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
- Cross-feature constraints
- Approved exceptions

A Domain should remain meaningful even if the interface is redesigned.

Do not use a Domain document to describe screen layout, click-by-click interaction, local copy, or temporary implementation detail.

## Subdomain

A Subdomain is an optional decomposition of a large Domain into a coherent business area with distinct vocabulary, rules, or ownership.

Create a Subdomain only when the parent Domain has become difficult to understand or maintain as one subject.

A Subdomain is justified when several of these are true:

- It has a distinct set of entities or terms
- It has independent business rules
- It has a separate lifecycle
- It has meaningfully different ownership
- It can be discussed without repeatedly explaining the whole parent Domain

Do not create a Subdomain merely to mirror navigation, teams, pages, or Feature groups.

Subdomain is not a required first-class folder in the current repository structure. It may be represented as a section or a separate Domain document when needed.

## Journey

A Journey describes how an actor reaches an end-to-end outcome across major stages, touchpoints, Features, or products.

A Journey answers:

- Who is pursuing the outcome
- What starts the Journey
- What outcome completes it
- Which major stages the actor passes through
- Where responsibility or context changes
- Which Features and Flows support each stage

Journey documentation stays at a high level. It describes stages and major transitions, not every interaction step.

A Journey may include:

- Actor and goal
- Trigger and completion condition
- Major stages
- Cross-feature transitions
- Cross-product handoffs
- Important states or dependencies
- Related Tasks, Features, and Flows

Do not create a Journey for every page, modal, or short interaction. A Journey should represent a meaningful user outcome that usually spans more than one local action.

## Task

A Task is an immediate goal an actor is trying to accomplish.

Examples of Task shapes include:

- Submit a request
- Compare two options
- Add an approver
- Review a candidate
- Correct an invalid field

A Task describes user intent, not the interface action used to perform it.

For example, “choose an approval workflow” is a Task. “Click the dropdown” is an interaction step.

Tasks normally appear inside Journey, Feature, or Flow documents. They do not require a standalone canonical document unless they are reused broadly and need independent definition.

## Scenario

A Scenario is a concrete situation in which an actor attempts a Task or uses a Feature.

A Scenario combines:

- Actor or role
- Goal
- Trigger
- Preconditions
- Relevant context
- Expected outcome

A Scenario narrows a general capability into a case that can be described as a Flow.

For example, the same Feature may have different Scenarios for:

- A first-time user and a returning user
- An owner and an approver
- A valid submission and an incomplete submission
- A connected entity and a standalone entity

Scenarios usually live inside Feature or Flow documents rather than in a separate folder.

## Feature

A Feature is a coherent product capability that enables a user or the system to achieve a recognizable outcome.

A Feature answers:

- What the product enables
- Who can use it
- Why it exists
- Where it can be entered
- What major states it has
- What high-level behavior it provides
- What its boundaries and dependencies are

Typical Feature content includes:

- Purpose and value
- Actors
- Entry points
- Main capabilities
- High-level states
- Feature-specific rules
- Dependencies
- Boundaries and exclusions
- Related Domains, Journeys, and Flows

A Feature is not necessarily one page. It may span several screens, entry points, or system operations.

A Feature document should not duplicate stable business truth owned by a Domain. It should reference the Domain rule and explain how the capability uses it.

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

One Feature can have several Flows. One Flow can coordinate several Features when the Scenario crosses capability boundaries.

## State and lifecycle

State describes the current condition of an entity, Feature, or interaction. Lifecycle describes the valid progression between states over time.

Ownership depends on scope:

- Stable entity states and transition rules belong in the relevant Domain
- Feature-level presentation or availability states belong in the Feature
- Step-level transitions and validation outcomes belong in the Flow

Do not define the same lifecycle independently in several documents. Keep the canonical lifecycle in the Domain and reference it elsewhere.

## Rule

A Rule is a constraint that determines allowed product behavior.

Rule placement depends on its stability and scope:

- Cross-feature business invariant → Domain
- Capability-specific constraint → Feature
- Scenario-specific validation or branch → Flow
- Cross-product rule with consistent meaning → Shared knowledge

A visual convention is not a business rule. Design-system behavior belongs in `shared/design-system/`.

## Decision

A Decision records a durable, approved choice that requires historical context.

A Decision answers:

- What problem or ambiguity existed
- Which options were considered
- What was approved
- Why it was approved
- What consequences or constraints follow

Use a Decision document when the rationale will matter later, especially for trade-offs, exceptions, ownership boundaries, lifecycle changes, or choices that may otherwise be repeatedly reopened.

Do not use a Decision as the only record of current behavior. The approved result must also be reflected in the relevant Domain, Journey, Feature, or Flow document.

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

They belong under `shared/design-system/`, not under product Features or Domains.

A Product Feature may consume a Component or Pattern, but the two remain separate kinds of knowledge.

## Screen, page, modal, and UI artifact

A screen, page, modal, wireframe, prototype, screenshot, or recording is usually a representation or source of evidence, not the primary canonical knowledge unit.

Document product behavior as Domain, Journey, Feature, or Flow knowledge. Reference the UI artifact when it helps locate or verify the behavior.

Temporary design exploration and unreleased specifications belong in the separate `product-work` repository.

## Choosing the right document type

| Question | Use |
|---|---|
| Would this remain true if the entire interface changed? | Domain |
| Does this describe an end-to-end outcome across major stages or capabilities? | Journey |
| What immediate goal is the actor trying to accomplish? | Task |
| Under which concrete actor, trigger, and preconditions does this happen? | Scenario |
| What capability does the product provide? | Feature |
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

### Split a Feature when

- The capabilities have independent value or entry points
- They have materially different actors, states, or dependencies
- They can change independently without making one document contradictory

### Split a Flow when

- Actor, trigger, preconditions, or outcome differ materially
- Branches have become large enough to obscure the main path
- The same path is reused independently by several Features

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
Related Features and Journeys
```

### Journey

```text
Actor and goal
Trigger
Completion condition
Major stages
Cross-feature or cross-product transitions
Related Tasks, Features, and Flows
```

### Feature

```text
Purpose
Actors
Entry points
Capability and high-level behavior
States
Feature-specific rules
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
Related Feature and Domain rules
```

### Decision

```text
Context
Options
Approved decision
Rationale
Consequences
Status and date
Affected canonical documents
```

## Illustrative example

The following example is only for understanding the model; it does not establish canonical product rules.

```text
Domain
→ Recruitment Request
→ Request, workflow, approval step, approver, permissions, and lifecycle rules

Journey
→ An employer recognizes a hiring need and continues until the need is fulfilled

Feature
→ Create recruitment request
→ Review and approve request
→ Manage approval workflow

Task
→ Choose a workflow
→ Add an approver
→ Submit the request

Scenario
→ A request owner submits a complete draft that is connected to an approval workflow

Flow
→ Validate the draft
→ Submit it
→ Move it to the first approval step
→ Handle approval, rejection, or error paths

Decision
→ Record why editing an active workflow is restricted and which changes remain allowed
```

## Canonical placement summary

```text
products/{product-id}/product-overview.md
→ Product purpose, users, boundaries, capabilities, and key concepts

products/{product-id}/domains/
→ Stable business truth

products/{product-id}/journeys/
→ End-to-end user outcomes and stages

products/{product-id}/features/
→ Product capabilities

products/{product-id}/flows/
→ Scenario-specific behavioral paths

products/{product-id}/decisions/
→ Durable approved decision history

shared/
→ Genuinely cross-product knowledge

shared/design-system/
→ Reusable UI foundations, components, patterns, and standards
```
