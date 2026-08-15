# Product Knowledge Authoring

## Goal

Turn a small amount of owner-supplied product knowledge into a structured, reviewable Product Area or Product Concept without making the owner fill the full canonical template manually.

This workflow is optimized for the current state where walkthrough coverage may be incomplete and important product knowledge still lives with product owners.

The default direction is:

```text
Owner knowledge
+ current Product Knowledge
+ optional supporting sources
→ AI classification and structuring
→ owner review
→ AI normalization
→ approved canonical update
```

The AI is responsible for documentation structure and classification. The owner remains responsible for product truth and final approval.

## Input model

Accept owner input in natural language. Do not require the owner to know repository taxonomy or template section names.

A compact intake may contain any of the following:

- What this part of the product does
- Main flows or behaviors
- Important rules or limits
- Permissions or eligibility conditions
- Known differences by plan, role, platform, segment, location, or other stable context
- Real exceptions or edge cases
- Things the owner is unsure about
- Links or references to Figma, Jira, production, analytics, research, walkthroughs, or existing docs

Do not require all fields before producing useful work. Free-form notes are valid input.

## Source model

Use these sources distinctly:

```text
Current Product Knowledge on main
→ Existing canonical product model

Explicit owner input
→ Proposed current product truth from the responsible human; eligible for the draft but still requires final owner review

Supplied supporting evidence
→ Corroboration or additional context; preserve its authority and limitations

External research
→ Use only when explicitly requested; never use it to invent internal product behavior
```

If explicit owner input conflicts with current Product Knowledge, do not silently overwrite either one. Surface the conflict for owner resolution.

If a source does not support a claim, do not present the claim as source-derived.

## Authoring modes

### Product Area mode

Use when the target is a meaningful product capability, outcome, or business process whose behavior is defined by flows, rules, actors, permissions, validations, and state transitions.

Mental model:

> Area is where behavior happens.

### Product Concept mode

Use when the target is a business concept, entity, or actor with an independent meaning, attributes, relationships, intrinsic rules, or lifecycle that may be used across multiple Product Areas.

Mental model:

> Concept is something the product talks about; Area is where the product does something with it.

### Mixed intake mode

Use when the owner provides raw knowledge that contains both Area behavior and Concept facts.

Do not force all facts into the requested document. Split each fact by canonical ownership and return:

- The requested primary draft
- Facts that belong in existing Concepts or Areas
- Candidate Concepts that may need promotion
- Related canonical documents that may need follow-up updates

## Core ownership rules

Use these rules consistently.

### Area vs Concept

```text
Meaning or intrinsic truth of a thing
→ Product Concept

Behavior of things in a specific product context
→ Product Area
```

Examples:

```text
"Application connects a Candidate to a Job Post."
→ Application Concept

"After successful Apply, an Application is created."
→ Candidate Apply Area
```

### Attributes vs contextual validation

```text
An attribute exists and has a business meaning
→ Product Concept / Attributes

An attribute is required, optional, restricted, or validated in a specific flow
→ Product Area / Validation or Business Rules
```

### States and lifecycle

```text
Canonical states, state definitions, and main lifecycle of a Concept
→ Product Concept

Transitions created, used, or controlled by one Area
→ Product Area / Relevant State Transitions
```

A creation event is not automatically a state transition. Do not invent an initial state when it is unknown.

### Relationships vs related knowledge

```text
Semantic business relationship between Concepts
→ Product Concept / Relationships

Navigation to another useful Area, Concept, or service
→ Product Area / Related Knowledge
```

Do not duplicate semantic relationships in Related Knowledge.

### Roles, user states, and plans

- Actor or Role describes who participates in the Area.
- Anonymous / Logged-in are user states, not Roles.
- Pro / Premium are plans or segments, not Roles.
- Put behavioral differences caused by those contexts in Flow, Permissions, Business Rules, or Known Variations.

### Main, alternate, and failure flows

- Main Flow = baseline successful path.
- Alternate / Conditional Flow = a valid conditional path that can still reach the same goal.
- Error & Recovery = an operation failed or the normal path cannot continue.

Do not inflate every condition into a separate Main Flow.

### Entry Points

Entry Point means:

> The last surface outside the Area + the action that enters the Area behavior.

Do not document the entire upstream journey as an Entry Point.

Multiple Entry Points may feed the same Flow. Differentiate Entry Points by surface and Flows by behavior.

### Known Variations

Use Known Variations only when base behavior differs because of a relatively stable context such as:

- Plan
- Platform
- Location
- User Segment
- Role
- Organization Type

Temporary flow conditions such as incomplete data, authentication checks, or validation failures are not Known Variations.

### Edge Cases

An Edge Case is a real, known, unusual domain condition with defined behavior.

Do not classify normal alternate branches, validation conditions, or ordinary retry behavior as Edge Cases.

### Business Rules

- Context-independent intrinsic rules of a Concept belong to the Concept.
- Rules governing behavior inside a Product Area belong to the Area.
- Do not duplicate a Concept rule inside every Area; reference it when needed.

## Workflow

### 1. Load contracts

Read:

```text
templates/product-area.md
templates/shared-product-concept.md
manifest.generated.json
```

Read `README.md` when repository placement or product hierarchy matters.

If the task is about updating existing canonical files after approval, also load `ai/knowledge-update.md`.

### 2. Resolve target and mode

Identify:

- Product group and product
- Primary subject
- Requested output: Area, Concept, or mixed knowledge intake
- Named owner when known

If the target could materially be either an Area or Concept, use the ownership rules above before asking the user. Ask only if the classification remains genuinely ambiguous and would change the output materially.

### 3. Retrieve the smallest relevant current context

Use `manifest.generated.json` to find only the Product Knowledge documents that materially affect the target:

- Product Group Overview
- Product Overview
- Adjacent Product Areas
- Existing Product Concepts
- Shared Product Services when relevant

Do not scan the whole repository by default.

The purpose of retrieval is to understand current naming, boundaries, relationships, and potential conflicts. In the absence of strong evidence, current Product Knowledge does not replace missing owner knowledge.

### 4. Decompose owner input into atomic claims

Extract individual claims before drafting.

For each claim, determine:

- What object or behavior it is about
- Whether it is Area behavior or Concept truth
- Whether it is a Flow, Rule, Permission, Validation, State, Transition, Attribute, Relationship, Variation, Data Behavior, Error/Recovery, Edge Case, or Unknown
- Whether it is explicit owner knowledge, existing Product Knowledge, supplied evidence, inference, or unresolved

Do not expose this internal classification table unless it materially helps review.

### 5. Build the semantic model before writing sections

For an Area, first understand:

- Main behavior and outcome
- Main and alternate flows
- Important rules
- Actors and permissions
- Concepts involved
- Validations and state changes
- Variations, errors, and real edge cases
- Adjacent Areas and handoffs

Then derive `Overview` and `Boundaries` from the whole model. Boundaries are written near the beginning of the final document for readability, but they should be derived after the Area behavior is understood.

For a Concept, first understand:

- Independent definition and business meaning
- Business-meaningful attributes
- Relationships
- Intrinsic rules
- Canonical states/lifecycle when applicable
- Business-semantic variations
- Product Areas that use it

Then derive concise boundaries and terminology.

### 6. Produce a complete review draft

Use the canonical template for the selected mode.

AI should derive and normalize sections that do not require new product decisions, including when possible:

- Overview
- Boundaries
- Main Concepts or Used In Product Areas
- Related Knowledge
- Terminology normalization
- Sources formatting
- Unknowns discovered from gaps or conflicts

Do not fabricate missing flows, rules, permissions, states, or edge-case behavior merely to make every section look complete.

When a template section is not applicable, leave it explicitly empty or state that no confirmed behavior is known rather than inventing content.

### 7. Run the completeness pass

After the first draft, identify only missing information that materially affects understanding of the product model.

Useful owner-review questions commonly cover:

- Is any important Flow missing?
- Is an important Business Rule or limit missing?
- Are there permissions or eligibility conditions not visible in the sources?
- Does behavior differ by a stable context such as Plan, Role, Platform, Segment, or Location?
- Are there real exceptions or edge cases the draft missed?
- Is any AI-derived boundary wrong?
- Can any Unknown be resolved from owner knowledge now?

Do not make the owner review every template field mechanically.

Prefer a short, prioritized review list over a second full questionnaire.

### 8. Reconcile owner corrections

When the owner responds:

- Apply explicit corrections as human decisions.
- Reclassify facts if the correction reveals wrong Area/Concept ownership.
- Remove duplicates across sections.
- Keep unresolved conflicts and unknowns visible.
- Regenerate derived sections such as Overview and Boundaries when underlying behavior changed.

### 9. Prepare canonical update

A review draft is not canonical merely because AI structured it.

Before repository write:

- Owner confirms correctness and scope.
- Determine the smallest affected document set.
- Use `ai/knowledge-update.md` for the repository update process.
- Do not silently update neighboring Areas or Concepts.
- Regenerate `manifest.generated.json` whenever indexed Product Knowledge documents change.

## Product Area quality checks

Before delivery, verify:

- The Area is a capability, outcome, or process, not a page, modal, navigation node, Jira Epic, or team boundary.
- Overview describes the behavior without becoming a flow transcript.
- Boundaries are consistent with flows and adjacent Areas.
- Users & Roles do not contain user states, plans, or segments as Roles.
- Entry Points are surfaces + actions, not full upstream journeys.
- Main Concepts are referenced, not redefined.
- Main Flow and Alternate / Conditional Flows are distinct.
- Concept-intrinsic rules are not duplicated as Area rules.
- Relevant State Transitions do not redefine the whole Concept lifecycle.
- Validation is separate from UI error presentation.
- Known Variations represent stable context differences.
- Edge Cases are unusual real cases, not normal branches.
- Unknowns are explicit.

## Product Concept quality checks

Before delivery, verify:

- The Concept has an independent business meaning beyond one UI or Flow.
- Definition says what the Concept is, not what one Area does with it.
- Attributes include the business/product-meaningful properties needed to understand the Concept, not implementation-only fields.
- Relationships are semantic business relationships, not technical ERD details.
- Business Rules are intrinsic and context-independent.
- States and lifecycle are canonical only when actually known.
- Types / Variations are business-semantic variants, not merely values already represented by an Attribute.
- Used In Product Areas is derived from Area references and should not require manual owner maintenance.
- Unknowns remain visible.

## Human responsibility

Humans are responsible for:

- Supplying or correcting tacit product knowledge
- Resolving contradictions and ambiguous current behavior
- Confirming important product rules and exceptions
- Approving the final canonical Product Knowledge update

AI is responsible for:

- Retrieval
- Classification
- Area/Concept ownership
- Drafting and normalization
- Deriving boundaries and related knowledge
- Detecting gaps, conflicts, and candidate concepts
- Producing focused review questions

## Rules

- Do not invent product behavior.
- Do not convert an inference into a product fact without owner confirmation or authoritative evidence.
- Do not force owner input to match the canonical template.
- Do not duplicate the same fact across Area and Concept documents.
- Do not treat a clean-looking AI draft as evidence of completeness.
- Do not use incomplete walkthrough coverage as a reason to over-trust AI-generated behavior.
- Do not silently overwrite current Product Knowledge when owner input conflicts with it.
- Keep the canonical templates as the output contract; keep this workflow focused on how raw owner knowledge becomes that output.