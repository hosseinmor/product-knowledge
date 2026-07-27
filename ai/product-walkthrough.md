# Optional Product Walkthrough

Product Walkthrough is an optional framework for filling gaps in Product Knowledge.

Use it when a Product Area is missing, incomplete, disputed, outdated, or difficult to understand from current sources. A walkthrough may also test how a product uses a Shared Product Service, but it does not replace model or technical evaluation of the service itself.

## Preparation

1. Read `manifest.generated.json`.
2. Select the relevant Product Group, Product Overview, Product Area, and Shared Product Service documents.
3. Use their unknowns, topics, and related IDs to define the walkthrough scope.
4. Do not treat existing documents as evidence that production behavior was observed.

## Process

1. Define a bounded Product Area, actor, role, account, authentication state, and environment.
2. Inventory entry points, screens, actions, states, permission gates, and visible service dependencies.
3. Follow important actions through outcomes, alternate paths, validation, cancellation, persistence, fallback, and recovery.
4. Record evidence and mark each important case as:
   - observed
   - blocked
   - not tested
   - unknown
5. Separate observation from inference and suspected bugs.
6. For a shared-service dependency, separate visible product behavior from claims about the underlying service or model.
7. Produce a concise list of:
   - confirmed product behavior
   - gaps
   - contradictions
   - suspected bugs
   - recommended Product Area updates
   - recommended Shared Product Service questions or updates
8. The relevant owners review the findings and update Product Knowledge manually.
9. Regenerate the manifest after approved document changes.

A walkthrough is evidence, not automatic product truth.
