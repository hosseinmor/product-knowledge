# Product Walkthrough

## Purpose

Systematically inspect current product behavior and produce a reviewable evidence-based walkthrough output for later Product Knowledge updates.

This skill collects evidence. It does not directly create canonical Product Knowledge or approve intended behavior.

## Required inputs

- Product identifier
- Product area or bounded scope
- Actor or role
- Authentication state
- Environment
- Known entry points

## Optional inputs

- Existing Product Knowledge
- Test accounts and roles
- Known flows
- Design references
- PRDs or release notes
- Prior walkthroughs
- Excluded areas

## Output

Create a temporary walkthrough document in `product-work` using:

```text
templates/walkthrough-output-template.md
```

The output is evidence for review and for the `product-knowledge-update` skill. It is not canonical Product Knowledge.

## Workflow

### 1. Establish scope before interaction

Record:

- Product
- Product area
- Actor and role
- Authentication state
- Environment
- Known entry points
- Known restrictions
- Excluded areas

Do not claim coverage outside this scope.

### 2. Read existing context

Read the relevant Product overview and the smallest sufficient set of existing Capabilities, Flows, Domains, and accepted Decisions.

Use them as hypotheses and coverage guides, not as substitutes for observing current behavior.

### 3. Build a surface inventory

Before drafting Capabilities or Flows, inventory discoverable:

- Pages and views
- Navigation items
- Entry points
- Primary and secondary actions
- Forms and fields
- Filters, sorting, and search
- Dialogs, sheets, drawers, and popovers
- Empty, loading, success, and error states
- Authentication and permission gates
- External redirects

Keep the inventory in the walkthrough output.

### 4. Build a coverage matrix

For every important area, action, state, and branch, assign one status:

```text
observed
blocked
not-tested
not-applicable
unknown
```

Do not use `complete` as a substitute for branch-level coverage.

### 5. Follow each action to an outcome

For every action, observe or record as untested:

```text
Immediate response
State change
Navigation
Success behavior
Validation behavior
Error behavior
Cancellation or exit
Persistence after refresh
Return behavior
```

Do not stop after discovering a button, field, or page.

### 6. Explore meaningful branches

Actively inspect or explicitly mark untested:

- Success
- Empty state
- Validation
- Authentication required
- Permission denied
- Cancellation
- Retry and recovery
- Already-completed or duplicate action
- Boundary values
- Relevant loading and server-error behavior when safely observable

Do not manufacture destructive data or unsafe errors merely to increase coverage.

### 7. Record evidence

Connect each important observation to evidence such as:

- Walkthrough step number
- URL or route
- Screenshot
- Recording timestamp
- Visible system response
- Approved source document

A statement without evidence must be labeled as inference or unknown.

### 8. Separate knowledge classes

Use these categories consistently:

```text
Observed
Inferred
Unknown
Blocked
Suspected bug
```

Observed behavior must not automatically become an intended business rule.

### 9. Identify candidates

Based on the evidence, propose only candidates for:

- Capabilities
- Flows
- Domain rules

Do not declare these canonical. Preserve screen-level details as evidence while expressing candidates as durable product abilities and behavior.

### 10. Assess completeness

Before handing off, verify:

- Scope, actor, role, and authentication state are explicit
- Known entry points were checked or marked untested
- Surface inventory exists
- Coverage matrix exists
- Main paths and meaningful branches are distinguished
- Authentication and permission gates are recorded
- Observation is separated from inference
- Evidence is linked
- Blocked and untested areas remain visible

Do not claim completeness while material `not-tested`, `blocked`, or `unknown` items remain without an explicit reviewer decision accepting the limitation.

### 11. Stop for human review

Present:

- Walkthrough output
- Coverage gaps
- Blocked areas
- Suspected bugs
- Candidate Product Knowledge documents
- Questions requiring PM, Designer, or Tech confirmation

Only a reviewed walkthrough output may be passed to `product-knowledge-update`.

## Rules

- Do not equate navigation structure with Capability structure.
- Do not treat every page or action as a Capability.
- Do not treat UI text as proof of the underlying business rule.
- Do not generalize behavior from one actor, role, account, or state to all users.
- Do not hide incomplete coverage.
- Do not write directly to `main`.
- Do not create Journey, Feature, User Goal, Scenario, Rule, State, Lifecycle, or Subdomain documents.
