# Product Knowledge Authoring

## Goal

Turn a small amount of owner-supplied product knowledge into a structured, reviewable Product Area and correctly routed Product Concept knowledge without making the owner fill the full canonical Product Knowledge schema manually.

This workflow is optimized for the current phase where:

- Product Knowledge structure may still be revised
- Walkthrough coverage may be incomplete
- Existing draft documents may be incomplete or experimental
- Important current product knowledge still lives with product owners

The default direction is:

```text
Product Area Owner Input or owner conversation
→ focused AI follow-up
→ AI classification and structuring
→ Product Area draft + routed Concept knowledge
→ owner review
→ AI normalization
→ approved canonical update
```

The Owner Input is intentionally less structured than canonical Product Knowledge. This keeps the human-captured knowledge reusable even if the canonical Area or Concept schema changes later.

AI owns documentation structure and classification. The owner remains responsible for current product truth and final approval.

## Product Area Owner Input

Use:

```text
templates/product-area-owner-input.md
```

The Owner Input is not canonical Product Knowledge.

It exists to help the owner capture what they know using product language rather than repository taxonomy.

It asks about:

1. What the Product Area does
2. Main behavior and flows
3. Important rules and limits
4. Important behavioral differences
5. Real unusual or failure cases
6. Unknowns
7. Sources or knowledgeable people

The owner does not need to identify:

- Boundaries
- Main Concepts
- Permissions in canonical form
- State ownership
- Data Behavior classification
- Alternate Flow vs Error vs Edge Case
- Area vs Concept ownership

AI derives or classifies those later.

The same questions can be used conversationally. A filled document is helpful but not mandatory.

## Source model

Use sources distinctly.

```text
Explicit responsible-owner input
→ Primary proposed current product truth for the authoring draft

status: reviewed Product Knowledge on main
→ Trusted current canonical context

Reviewed or authoritative supporting evidence
→ Supporting evidence with its original authority and limitations

status: draft Product Knowledge
→ Not product truth by default; ignore during normal authoring unless explicitly needed for history, conflict investigation, or recovery of earlier notes

External research
→ Use only when explicitly requested; never use it to establish undocumented internal product behavior
```

Do not assume every document on `main` is trustworthy merely because it is in the repository.

When reviewed Product Knowledge conflicts with explicit owner input, surface the conflict. Do not silently overwrite either one.

Do not use incomplete walkthrough or repository coverage to infer missing behavior.

## Authoring modes

### Product Area mode

Use when the target is a meaningful product capability, outcome, or business process whose behavior is defined by flows, rules, actors, permissions, validations, state transitions, variations, and recovery behavior.

Mental model:

> Area is where behavior happens.

### Product Concept mode

Use when the target is a business concept, entity, or actor with independent meaning, attributes, relationships, intrinsic rules, or lifecycle that needs a canonical definition across Product Areas.

Mental model:

> Concept is something the product talks about; Area is where the product does something with it.

### Mixed intake mode

This is common when an owner explains an Area.

Raw owner knowledge may contain both:

- Area behavior
- Concept meaning or intrinsic truth

Do not force all facts into the Product Area document.

Return the requested Area draft and route Concept-owned knowledge to:

- Existing Product Concepts
- Candidate Product Concepts
- Other existing Product Areas when the behavior belongs elsewhere

## Core ownership rules

### Area vs Concept

```text
Meaning or intrinsic truth of a thing
→ Product Concept

Behavior of things in a specific product context
→ Product Area
```

Example:

```text
Application connects a Candidate to a Job Post.
→ Application Concept

After successful Apply, an Application is created.
→ Candidate Apply Area
```

### Attributes vs contextual behavior

```text
An attribute exists and has a business meaning
→ Product Concept / Attributes

An attribute is required, optional, editable, restricted, or validated in a specific context
→ Product Area / Validation or Business Rules
```

A universal intrinsic invariant may belong in Concept Business Rules.

### States and lifecycle

```text
Canonical states, state definitions, and main lifecycle
→ Product Concept

Transitions created, used, or controlled by one Area
→ Product Area / Relevant State Transitions
```

A creation event is not automatically a State Transition.

Do not invent an initial State when it is unknown.

### Relationships vs related knowledge

```text
Semantic business relationship between Concepts
→ Product Concept / Relationships

Navigation to another useful Area, Concept, or Service
→ Product Area / Related Knowledge
```

### Roles, user states, plans, and segments

- Actor or Role describes who participates in an Area.
- Anonymous / Logged-in are user states, not Roles.
- Pro / Premium are Plans or Segments, not Roles.
- Behavioral differences caused by these contexts belong in Flow, Permissions, Business Rules, or Known Variations.

### Main, alternate, and failure flows

- Main Flow = baseline successful path.
- Alternate / Conditional Flow = valid conditional path that can still reach the same Goal.
- Error & Recovery = operation failed or normal path cannot continue.

Do not create separate Main Flows merely because Entry Points differ.

### Entry Points

Entry Point means:

> The last surface outside the Area + the action that enters Area behavior.

Do not capture the whole upstream journey as an Entry Point.

Multiple Entry Points may feed the same Flow.

Differentiate Entry Points by surface and Flows by behavior.

### Known Variations

Use when base behavior differs because of a relatively stable context such as:

- Plan
- Platform
- Location
- User Segment
- Role
- Organization Type

Temporary conditions such as incomplete data, authentication checks, or validation failure are not Known Variations.

### Edge Cases

An Edge Case is a real, known, unusual domain condition with defined behavior.

Do not classify:

- Normal alternate branches
- Validation conditions
- Ordinary retry behavior

as Edge Cases.

### Business Rules

- Context-independent intrinsic Concept rules belong to the Concept.
- Rules governing behavior inside an Area belong to that Area.
- Do not duplicate Concept rules in every Area.

## Workflow

### 1. Load contracts

Read:

```text
templates/product-area-owner-input.md
templates/product-area.md
templates/shared-product-concept.md
manifest.generated.json
```

Read `README.md` when product hierarchy or repository placement matters.

Load `ai/knowledge-update.md` only when an approved draft is being applied to canonical repository content.

### 2. Resolve the target

Identify:

- Product Group and Product
- Product Area or Concept being documented
- Named owner when known
- Whether input comes from a filled Owner Input, conversation, notes, or a combination

If the user names a Product Area, treat Product Area as the primary output even when Concept knowledge appears inside the intake.

### 3. Retrieve only trusted current context

Use `manifest.generated.json` to find the smallest relevant set of `status: reviewed` Product Knowledge needed to understand:

- Established naming
- Existing reviewed Area boundaries
- Existing reviewed Product Concepts
- Direct canonical relationships
- Trusted adjacent behavior

Do not scan the repository broadly.

Do not use `status: draft` Areas or Concepts as current product truth by default.

If the repository currently contains few or no reviewed documents, continue with owner knowledge and templates rather than lowering the trust threshold.

### 4. Decompose owner input into atomic claims

Interpret the owner's wording without requiring canonical terminology.

For each meaningful claim, determine internally:

- What object or behavior it is about
- Area behavior or Concept truth
- Flow / Rule / Permission / Validation / State / Transition / Attribute / Relationship / Variation / Data Behavior / Error-Recovery / Edge Case / Unknown
- Source authority: owner input, reviewed Product Knowledge, reviewed evidence, inference, unresolved

Do not expose a large classification table unless it helps resolve a conflict.

### 5. Identify material gaps

Before drafting, check whether missing information can materially change the Area model.

High-value gap categories are:

- Main Flow or Goal
- Important Business Rule or limit
- Eligibility or Permission
- Important stable-context variation
- Real exception, failure, or recovery behavior
- Material ambiguity in Area vs Concept ownership

Do not mechanically ask about every canonical section.

### 6. Ask focused product questions

When material gaps exist, ask one focused batch of questions before drafting.

Default limit:

> No more than five material follow-up questions in one batch.

If additional low-confidence gaps remain, keep them in Unknowns instead of turning the process into a long interview.

Ask product questions, not template questions.

Bad:

> What are the Known Variations?

Good:

> Does this behavior differ for any Plan, Role, user type, Platform, or other stable context? If so, how?

Bad:

> Please complete Permissions.

Good:

> Who can complete this action, and are there conditions such as Plan, access level, quota, or eligibility?

Do not ask about information already available in the Owner Input, conversation, or reviewed Product Knowledge.

### 7. Build the semantic model

For a Product Area, first understand:

- Main outcome
- Actors
- Main and alternate behavior
- Rules
- Permissions and eligibility
- Concepts involved
- Validations
- Relevant state changes
- Errors/recovery
- Stable variations
- Real edge cases
- Adjacent behavior and handoffs

Only after this model is coherent should AI derive:

- Overview
- Boundaries
- Main Concepts
- Related Knowledge

Boundaries appear near the beginning of the final document because they help readers, but they should be derived late from the full Area model.

For Product Concepts, first understand:

- Definition
- Business Meaning
- Attributes
- Relationships
- Intrinsic rules
- Canonical states/lifecycle when known
- Meaningful variants

Then derive concise Boundaries and Terminology.

### 8. Produce the review draft

Use the canonical template for the primary output.

For Product Area:

```text
templates/product-area.md
```

For Product Concept:

```text
templates/shared-product-concept.md
```

Do not fabricate content simply to make every section look complete.

If no confirmed information exists for a section, leave it empty, state that no confirmed behavior is known, or route the gap to Unknowns as appropriate.

### 9. Route Concept knowledge

When owner input contains Concept-owned facts:

- Do not duplicate them inside the Area.
- Reference an existing reviewed Product Concept when one exists.
- Mark a new Concept as `[Candidate Concept]` when it appears to need an independent canonical definition.
- Keep a short `Knowledge routing` note in the review output when facts were moved conceptually to another destination.

A Concept can deserve promotion when it has independent business meaning, attributes, relationships, intrinsic rules, or lifecycle and is reused or expected to be reused across Product Areas. Cross-product reuse is not required.

### 10. Owner review

Return the useful draft first.

Ask the owner to review correctness of product behavior, not documentation formatting.

Surface only important review items such as:

- Potentially missing major Flow
- Rule or limit that remains unconfirmed
- AI-derived boundary that may be wrong
- Candidate Concept needing confirmation
- Conflict with reviewed Product Knowledge
- Material Unknown that owner may be able to resolve

Do not ask the owner to re-fill the canonical template.

### 11. Reconcile corrections

When corrections arrive:

- Treat explicit owner corrections as human decisions for the draft.
- Reclassify misplaced Area/Concept knowledge.
- Remove duplication.
- Regenerate Overview and Boundaries if underlying behavior changed.
- Preserve unresolved conflicts and Unknowns.

### 12. Canonical update

A review draft is not canonical merely because AI structured it.

Before writing to Product Knowledge:

- Owner confirms correctness and scope.
- Determine the smallest affected document set.
- Load `ai/knowledge-update.md`.
- Use a dedicated branch and pull request.
- Regenerate `manifest.generated.json` whenever indexed Product Knowledge documents change.

## Product Area quality checks

Before delivery, verify:

- The Area is a meaningful capability, outcome, or process, not a page, modal, navigation node, Jira Epic, or team boundary.
- Overview describes the Area without becoming a Flow transcript.
- Boundaries follow from the actual documented behavior.
- Users & Roles do not contain user states, Plans, or Segments as Roles.
- Entry Points are surfaces + actions, not full upstream journeys.
- Main Concepts are referenced, not redefined.
- Main Flow and Alternate / Conditional Flows are separated correctly.
- Concept-intrinsic rules are not duplicated as Area rules.
- Relevant State Transitions do not redefine the entire Concept lifecycle.
- Validation is separate from UI error presentation.
- Error & Recovery describes actual failure/recovery behavior.
- Known Variations represent stable context differences.
- Edge Cases are unusual real cases, not normal branches.
- Unknowns remain explicit.

## Product Concept quality checks

Before delivery, verify:

- The Concept has independent business meaning beyond one UI or Flow.
- Definition explains what the Concept is, not what one Area does with it.
- Attributes include business/product-meaningful properties needed to understand the Concept.
- Relationships are semantic business relationships, not technical ERD details.
- Business Rules are intrinsic and context-independent.
- States and lifecycle are canonical only when known.
- Types / Variations are business-semantic variants rather than ordinary Attribute values.
- Used In Product Areas is AI-maintained from Area references.
- Unknowns remain visible.

## Human responsibility

Humans are responsible for:

- Supplying current tacit product knowledge
- Correcting AI misunderstanding
- Resolving contradictions
- Confirming important rules and exceptions
- Approving final canonical Product Knowledge

AI is responsible for:

- Interpreting Owner Input
- Retrieving trusted reviewed context
- Asking focused follow-up questions
- Classifying knowledge
- Applying Area/Concept ownership
- Drafting and normalization
- Deriving Boundaries and Related Knowledge
- Detecting gaps, conflicts, and Candidate Concepts

## Rules

- Do not invent product behavior.
- Do not convert inference into product fact without owner confirmation or authoritative evidence.
- Do not force owner input to match the canonical template.
- Do not use `status: draft` Product Knowledge as current truth by default.
- Do not duplicate the same fact across Area and Concept documents.
- Do not treat a polished AI draft as evidence of completeness.
- Do not over-trust incomplete walkthrough or repository coverage.
- Do not silently overwrite reviewed Product Knowledge when owner input conflicts with it.
- Keep the Owner Input independent enough that it remains useful if the canonical Product Knowledge schema changes.
