# PM to PRD

The PRD lives in Jira. No separate Brief document is required.

## Minimum Jira input

- Problem
- Why it matters or supporting evidence
- Affected users
- Desired outcome
- Known constraints

## Retrieval

1. Read `manifest.generated.json`.
2. Filter by product, kind, title, summary, and topics.
3. Read the relevant Product Overview.
4. Read only the Product Areas, Shared Product Concepts, product standards, and content guidance needed for the change.
5. Follow related IDs only when they materially affect scope or behavior.

Do not scan the entire repository by default.

## Process

1. Summarize current behavior, rules, permissions, states, and known gaps.
2. Ask only blocking questions that materially change scope or behavior.
3. Record the PM's decisions.
4. Draft the PRD using `templates/jira-prd.md`.
5. Keep current behavior, intended behavior, assumptions, and open questions separate.
6. Add links to the Product Knowledge documents used.
7. Stop for PM review and approval.

## Rules

- Do not invent product rules.
- Do not treat an AI recommendation as an approved decision.
- Do not hide contradictions or missing Product Knowledge.
- Do not create or store a separate Brief file.
