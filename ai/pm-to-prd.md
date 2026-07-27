# PM to PRD

## Purpose

Help a PM turn a small initial Jira input into a complete PRD using current Product Knowledge.

The PRD remains in Jira. No separate Brief file is required.

## Minimum initial input

```text
Problem
Why now or supporting evidence
Affected users
Desired outcome
Known constraints
```

## Workflow

1. Read the initial Jira input.
2. Read the product `overview.md`.
3. Read the smallest relevant set of Product Area documents.
4. Read related shared Product Concepts, product rules, content guidance, and Design System documentation when relevant.
5. Summarize current behavior, known rules, constraints, and gaps.
6. Ask only questions that materially change scope, behavior, rules, permissions, states, data, or feasibility.
7. Record the PM's answers as product decisions for this PRD.
8. Draft or complete the PRD in Jira using `templates/jira-prd.md`.
9. Validate that current behavior, proposed behavior, assumptions, and open questions are separate.
10. Suggest exact Product Knowledge updates when gaps or outdated information are found.

## Required output before the PRD

```text
Current product context
Relevant rules and constraints
Knowledge gaps
Blocking questions
```

## Rules

- Do not invent a product decision.
- Do not treat incomplete Product Knowledge as proof that no rule exists.
- Do not create or maintain a separate Brief document.
- Do not update Product Knowledge automatically.
- Keep unresolved questions visible in the Jira PRD.
