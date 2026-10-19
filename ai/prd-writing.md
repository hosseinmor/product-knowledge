# PRD Writing

This file defines the PRD process. The execution wrapper is
`ai/skills/prd-writing/SKILL.md`; the output contract is
`templates/jira-prd.md`.

## Source gate

1. Read `product-knowledge-sources.yml`.
2. For JobVision, open <https://docs-jv.jvoffice.ir/> through a verified
   internal-browser path and load the smallest relevant domains.
3. For Cando, open <https://docs-cd.jvoffice.ir/> through a verified
   internal-browser path and load the smallest relevant domains.
4. Use `manifest.generated.json` only for relevant Content, Design System, and
   product-standard guidance.

If the required canonical source is inaccessible, preserve the access limitation
and ask for the relevant material when needed. Do not substitute this repository
or the other product's canonical source.

## Minimum input

- Problem
- Why it matters or supporting evidence
- Affected users
- Desired outcome
- Known constraints

## Process

1. Record the Product Knowledge pages and authorised inputs used.
2. Summarize current behavior, rules, permissions, states, dependencies, and
   known gaps at their actual authority level.
3. Separate current behavior, intended behavior, assumptions,
   recommendations, and open questions.
4. Ask only questions whose answers materially change scope or behavior.
5. Record human product decisions explicitly.
6. Draft with `templates/jira-prd.md`.
7. Validate every product claim against a source, approved decision, or clearly
   labelled input.
8. Stop for human review and approval.

## Rules

- Do not invent product or service behavior.
- Do not treat observed UI, Figma, screenshots, or walkthroughs as canonical
  policy.
- Do not hide missing Product Knowledge.
- Do not author or update canonical Product Knowledge in this repository.
- Do not claim Jira writes or approval unless they actually occurred.
