# Product Walkthrough

## Purpose

Systematically explore current product behavior and produce reviewable evidence with explicit coverage, gaps, and uncertainty.

This skill does not create canonical Product Knowledge directly. Its output is temporary source material that must be reviewed by a human before the Product Knowledge Update workflow uses it.

## Required inputs

- Product identifier
- Product area or investigation scope
- Actor or role
- Authentication and permission state
- Environment
- Known entry points
- Explicit exclusions and safety limits

## Expected workspace

```text
product-work/
└── walkthroughs/
    └── {walkthrough-id}/
        ├── output.md
        └── evidence/
```

Create `output.md` from `templates/walkthrough-output-template.md`.

## Core rules

- Define scope before interacting with the product.
- Do not assume visible navigation represents the complete product area.
- Do not treat a visible control as evidence that its full behavior is understood.
- Follow each safe action to its observable outcome.
- Separate observation from inference.
- Record blocked and untested cases instead of silently omitting them.
- Do not infer intended business rules from production behavior.
- Do not perform destructive, irreversible, privacy-sensitive, financial, or externally visible actions without explicit human approval.
- Do not write directly to Product Knowledge.

## Workflow

### 1. Establish scope

Record:

- Product and product area
- Actor and role
- Logged-in, logged-out, or mixed state
- Available permissions
- Environment
- Known entry points
- Included areas
- Excluded areas
- Data-integrity and safety limits

Do not begin broad exploration until the scope is visible in `output.md`.

### 2. Build a surface inventory

Inventory discovered:

- Pages and routes
- Navigation items
- Entry points
- Primary and secondary actions
- Forms and fields
- Filters and sorting
- Dialogs, sheets, drawers, menus, and popovers
- Empty, loading, success, disabled, and error states
- Authentication and permission gates
- External redirects and cross-product handoffs

The inventory is a discovery aid, not a Capability taxonomy.

### 3. Create and maintain a coverage matrix

Use only these statuses:

```text
observed
blocked
not-tested
not-applicable
unknown
```

Track coverage by area, actor, authentication state, entry point, state, and branch.

A discovered surface is not covered merely because it was viewed. Material behavior must be executed safely or marked with an honest non-observed status.

### 4. Follow actions to outcomes

For each safe action observe and record:

```text
starting context
→ action
→ immediate response
→ navigation
→ state change
→ success or validation result
→ cancellation or recovery
→ persistence after refresh or revisit
→ final observable state
```

Do not stop after the first visual response when the action starts a longer flow.

### 5. Search for branches deliberately

Test safely or explicitly mark these cases when relevant:

- Success
- Empty state
- Validation failure
- Authentication required
- Permission denied
- Cancellation and exit
- Retry and recovery
- Network or server error when safely observable
- Already completed state
- Duplicate action
- Boundary values
- Refresh, revisit, back-navigation, and return behavior

Do not manufacture unsafe failures or corrupt production data to increase coverage.

### 6. Capture evidence

Connect each material observation to evidence such as:

- Walkthrough step
- Screen or route
- Screenshot or recording reference
- Visible message or state
- Test account and access state
- Timestamp when relevant

Evidence supports what was observed. It does not prove the observed behavior is intended.

### 7. Separate epistemic states

Keep these sections distinct:

```text
Observed facts
Inferences
Unknowns
Blocked areas
Untested material cases
Suspected bugs
```

Rules:

- `Observed` means directly demonstrated in the walkthrough.
- `Inference` means an interpretation from observed evidence.
- `Unknown` means the answer is not established.
- `Blocked` means access, permissions, missing data, or safety limits prevented inspection.
- `Not tested` means the case was in scope but was not executed.
- `Suspected bug` means observed behavior may conflict with expected intent, but is not a canonical rule.

### 8. Identify candidates without promoting them

Propose candidate:

- Capabilities
- Flows
- Domain rules
- Decision questions

Label all of them as candidates. Do not assign `knowledge_state: canonical` and do not create files under `products/` during this workflow.

### 9. Assess completeness

The completeness assessment must state:

- Scope actually reviewed
- Actors and access states reviewed
- Entry points and branches covered
- Material blocked, unknown, and not-tested cases
- Evidence limitations
- Confidence in the inventory and behavior descriptions

Do not claim that a product area is complete while material gaps are undisclosed. A walkthrough may be complete for a narrow declared scope even when the whole product is not covered.

### 10. Stop for human review

Present:

- `output.md`
- Coverage matrix
- Evidence index
- Material unknowns and gaps
- Candidate Product Knowledge documents
- Suspected bugs
- Recommended follow-up walkthroughs

A human reviewer must confirm, correct, or reject observations before the Product Knowledge Update skill consumes the output.

## Quality gate

A walkthrough output is ready for review only when:

- Scope, actor, authentication state, environment, and exclusions are explicit
- A surface inventory exists
- Actions are connected to outcomes
- Coverage statuses are explicit
- Material branches are observed or disclosed as gaps
- Evidence supports material observations
- Observation and inference are separated
- Blocked, unknown, not-tested, and suspected-bug cases are visible
- Completeness is assessed against the declared scope

## Human responsibilities

Humans are responsible for:

- Approving risky or externally visible actions
- Providing required accounts, roles, and test data
- Clarifying intended behavior
- Reviewing observations and inferences
- Deciding whether suspected behavior is a bug
- Approving the walkthrough output for Product Knowledge recovery
