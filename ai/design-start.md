# Design Start with AI

## Inputs

- Approved Jira PRD
- Relevant Product Knowledge
- Relevant Shared Product Services
- Relevant Design System and content guidance

## Retrieval

1. Read `manifest.generated.json`.
2. Select the relevant Product Group, Product Overview, and Product Areas by group, product, title, summary, topics, and related IDs.
3. Add Shared Product Concepts only when their shared definition or rule affects the design.
4. Add Shared Product Services when product behavior depends on a cross-product service such as an AI fit or matching model.
5. Select only the relevant Design System components, patterns, foundations, accessibility rules, and content guidance.
6. Do not read the entire Design System or repository by default.

## Process

1. Summarize the user goal, product context, current behavior, intended change, rules, permissions, states, edge cases, service dependencies, and open questions.
2. For every shared service dependency, separate:
   - Shared inputs, outputs, limitations, confidence, and fallback
   - Product-specific presentation, thresholds, permissions, copy, and flow
3. Identify the selected Design System components, patterns, foundations, and content rules.
4. Flag PRD or Product Knowledge gaps before producing UI.
5. Produce the requested initial design artifacts, such as:
   - User flow
   - Information architecture
   - Screen inventory
   - State matrix
   - Wireframe or UI draft
   - Component mapping
   - Copy draft
6. Clearly distinguish Product Knowledge, PRD requirements, shared-service behavior, and AI recommendations.
7. Treat the result as a starting draft for Designer review, not a final design decision.
8. Link the Product Knowledge, Shared Product Service, and Design System documents used.
