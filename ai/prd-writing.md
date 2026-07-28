# PRD Writing with Product Knowledge

The PRD lives in Jira. No separate Brief document is required.

## Minimum Jira input

- Problem
- Why it matters or supporting evidence
- Affected users
- Desired outcome
- Known constraints

## Retrieval

1. Read `manifest.generated.json`.
2. Filter by group, product, kind, title, summary, and topics.
3. Read the relevant Product Group and Product Overview.
4. Read only the Product Areas, Shared Product Concepts, Shared Product Services, product standards, and content guidance needed for the change.
5. Follow related IDs only when they materially affect scope or behavior.

Do not scan the entire repository by default.

## Process

1. Summarize current behavior, rules, permissions, states, service dependencies, and known gaps.
2. Separate shared service behavior from product-specific use, thresholds, permissions, fallback, and presentation.
3. Ask only blocking questions that materially change scope or behavior.
4. Record the responsible product owner's decisions.
5. Draft the PRD using `templates/jira-prd.md`.
6. Keep current behavior, intended behavior, assumptions, and open questions separate.
7. Add links to the Product Knowledge documents used.
8. Stop for owner review and approval.

## Rules

- Do not invent product or shared-service rules.
- Do not treat an AI recommendation as an approved decision.
- Do not hide contradictions or missing Product Knowledge.
- Do not create or store a separate Brief file.
