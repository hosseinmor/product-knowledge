# AI Entry Point

Use this file as the tool-agnostic starting point for AI-assisted work in this repository.

## Canonical source

- Treat the `main` branch as the current approved repository state.
- Use Product Knowledge from this repository before relying on assumptions or external research.
- Treat the archive branch as historical context only unless the user explicitly asks for it.

## Start every product task

1. Read `ai/router.md`.
2. Determine the user's intent from their request and supplied files or links.
3. Load the matching Skill or workflow.
4. Use `manifest.generated.json` to find the smallest relevant Product Knowledge set.
5. Read only the documents that materially affect the task.
6. Keep current product truth, requested change, assumptions, open questions, and AI recommendations separate.
7. Do not invent missing product behavior or human decisions.

## Capability fallback

Tools have different capabilities. Follow this fallback model:

```text
Repository read access available
→ Read the required files from current main

Repository read access unavailable
→ Ask the user to provide AGENTS.md, the selected Skill or workflow, the relevant template, manifest entries, and selected Product Knowledge documents

Jira or destination write access available
→ Write only after the user requests the write and the required review or approval is complete

Destination write access unavailable
→ Return a destination-ready result without claiming it was saved
```

## Human authority

AI may retrieve context, identify gaps, ask blocking questions, recommend options, draft outputs, and propose Product Knowledge changes.

Humans remain responsible for product decisions, scope approval, final artifact approval, and approval of canonical Product Knowledge updates.

## Repository changes

- Do not write directly to `main`.
- Make approved changes on a dedicated branch and pull request.
- Do not modify unrelated files.
- Regenerate `manifest.generated.json` whenever indexed documents change.
