# Optional Product Walkthrough

Product Walkthrough is an optional framework for filling gaps in Product Knowledge.

Use it when a Product Area is missing, incomplete, disputed, outdated, or difficult to understand from current sources.

## Preparation

1. Read `manifest.generated.json`.
2. Select the relevant Product Overview and existing Product Area documents.
3. Use their unknowns, topics, and related IDs to define the walkthrough scope.
4. Do not treat existing documents as evidence that production behavior was observed.

## Process

1. Define a bounded Product Area, actor, role, account, authentication state, and environment.
2. Inventory entry points, screens, actions, states, and permission gates.
3. Follow important actions through outcomes, alternate paths, validation, cancellation, persistence, and recovery.
4. Record evidence and mark each important case as:
   - observed
   - blocked
   - not tested
   - unknown
5. Separate observation from inference and suspected bugs.
6. Produce a concise list of:
   - confirmed behavior
   - gaps
   - contradictions
   - suspected bugs
   - recommended updates to the Product Area document
7. The Product Area owner reviews the findings and updates Product Knowledge manually.
8. Regenerate the manifest after approved document changes.

A walkthrough is evidence, not automatic product truth.
