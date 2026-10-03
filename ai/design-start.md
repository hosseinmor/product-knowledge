# Design Start with AI

## Inputs

- Approved Jira PRD or explicit approved product decisions
- Product Knowledge from the approved source
- Relevant Design System and Product Content guidance

## Source gate

For JobVision, load the smallest relevant domains from
<https://docs-jv.jvoffice.ir/> through the internal VPN and browser. For Cando,
state that no canonical source exists and distinguish authorised inputs from
unknowns. Never use this repository, Figma, or observed UI as product truth.

## Repository retrieval

Use `manifest.generated.json` to retrieve only the smallest relevant set from:

```text
shared/design-system/
shared/content/
shared/product-standards/
```

For web work, use `shared/design-system/accessibility/router.md` to load the
smallest sufficient accessibility subset. Use the owning live source for exact
Figma or runtime facts.

## Process

1. Summarize the user goal and source-backed product context.
2. Separate current behavior, intended change, PRD requirements, evidence,
   unknowns, and recommendations.
3. Identify relevant components, patterns, accessibility rules, and content
   contracts.
4. Flag blocking Product Knowledge or PRD gaps before committing to UI behavior.
5. Produce the requested flow, IA, screen inventory, state matrix, wireframe,
   component mapping, or copy draft.
6. Treat the result as a review draft, not an approved product decision.
7. Link the Product Knowledge pages and repository guidance used.
