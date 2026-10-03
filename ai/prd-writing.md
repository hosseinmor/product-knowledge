# PRD Writing

This file defines the PRD process. The execution wrapper is
`ai/skills/prd-writing/SKILL.md`; the output contract is
`templates/jira-prd.md`.

## Source gate

1. Read `product-knowledge-sources.yml`.
2. For JobVision, open <https://docs-jv.jvoffice.ir/> through the internal VPN
   and load the smallest relevant domains.
3. For Cando, disclose that canonical Product Knowledge is unavailable and use
   only explicit owner input, reviewed evidence, or approved decisions.
4. Use `manifest.generated.json` only for relevant Content, Design System, and
   product-standard guidance.

If the required JobVision source is inaccessible, stop product-claim work or
ask for the relevant material. Do not substitute this repository.

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
