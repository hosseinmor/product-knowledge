# AI Tool Setup

This repository is tool-agnostic. Its Product Knowledge, workflows, Skills, templates, and manifest do not depend on one AI vendor or interface.

Tool-agnostic does not mean zero-configuration. Each AI environment needs a one-time instruction that points it to the repository entry point.

## Desired user experience

After one-time setup, a product owner should be able to provide files or a short problem statement and say:

```text
می‌خواهیم برای این موضوع PRD بنویسیم.
```

The AI should then:

```text
Read AGENTS.md
→ route through ai/router.md
→ load ai/skills/prd-writing/SKILL.md
→ load the workflow and template
→ retrieve relevant Product Knowledge through the manifest
→ summarize context and ask blocking questions
→ draft the PRD after human decisions
```

The product owner should not need to paste a long routing prompt, the PRD template, or repository paths into every conversation.

## One-time bootstrap instruction

Configure the AI workspace, project, agent, repository rule, or system instruction with the following minimal instruction:

```text
Use the current main branch of hosseinmor/product-knowledge as the canonical source for product work.
Start by reading AGENTS.md and route each request through ai/router.md.
Use manifest.generated.json to retrieve only the smallest relevant Product Knowledge set.
Do not invent missing product behavior or approve human decisions.
```

Use equivalent wording when the tool has a different instruction format. Do not copy the full workflows or templates into tool-specific configuration.

## Capability levels

### Level 1 — Repository-connected AI

The AI can read the repository directly.

Expected behavior:

1. Read `AGENTS.md`.
2. Route the request.
3. Read the selected Skill or workflow.
4. Read the relevant template.
5. Read the manifest and selected Product Knowledge documents.
6. Produce or update the requested artifact.

This is the preferred setup.

### Level 2 — File-upload AI

The AI cannot browse the repository but can read uploaded files.

Provide a small context pack containing:

```text
AGENTS.md
ai/router.md
selected Skill or workflow
relevant template
relevant manifest entries
selected Product Knowledge documents
```

Do not upload the entire repository by default. A repository-connected user or helper should select the smallest relevant context pack.

### Level 3 — Plain chat without repository or file access

The AI cannot use the canonical repository directly.

The user may still discuss or structure work, but the AI must clearly state that current Product Knowledge has not been verified. It must not claim current product behavior as repository-supported truth.

## Tool-specific adapters

Some tools automatically discover particular instruction filenames or support project-level instructions. These are adapters, not the canonical workflow.

Use this pattern:

```text
Tool-specific instruction
→ Read AGENTS.md
→ Follow ai/router.md
```

Possible adapters may include project instructions, workspace rules, repository instructions, or agent configuration supported by the chosen tool.

Do not duplicate Skill, workflow, template, or Product Knowledge content inside adapters. Duplication creates conflicting versions and weakens tool independence.

## Automatic Skill activation

Automatic activation requires both:

1. The tool or agent receives the bootstrap instruction.
2. It has access to the current repository files or an equivalent uploaded context pack.

The repository cannot force an unrelated AI tool to discover its Skills without that one-time connection.

After setup, the user's request should be enough for routing. For example:

```text
این مسئله و داده‌های اولیه است. می‌خواهیم PRD بنویسیم.
```

The router should select the PRD Skill based on the requested outcome.

## Write access

Read access and write access are separate capabilities.

```text
Read access only
→ Produce a Jira-ready or repository-ready artifact

Jira write access
→ Write only when the user requests it and required decisions are resolved

Repository write access
→ Use a dedicated branch and pull request; never write directly to main
```

Never claim an artifact was saved, updated, or merged when the corresponding operation did not succeed.

## Setup verification

Test each configured tool with this small scenario:

```text
We want to write a PRD for a product change. Here is the problem, affected users, desired outcome, evidence, and known constraints.
```

The setup passes when the AI:

- Selects the PRD Skill without being given its path
- Uses the manifest before scanning the repository
- Reads only relevant Product Knowledge
- Separates current behavior from the requested change
- Asks only blocking questions
- Uses the Jira PRD template
- Stops for human product decisions and final approval

Record tool-specific setup defects outside Product Knowledge. Change the central router or Skill only when the issue is common across tools.
