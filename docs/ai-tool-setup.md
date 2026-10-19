# AI Tool Setup

This repository is tool-agnostic, but Product Knowledge retrieval depends on
the product's approved source.

## One-time bootstrap instruction

Configure the AI workspace or project with this instruction:

```text
Read product-knowledge-sources.yml and AGENTS.md before product work, then route
through ai/router.md. JobVision Product Knowledge is canonical only at
https://docs-jv.jvoffice.ir/. Cando Product Knowledge is canonical only at
https://docs-cd.jvoffice.ir/. Verify access to each internal source in the
current execution environment. Never use repository files, Git history, Figma,
screenshots, observed UI, memory, or the other product's source as a canonical
Product Knowledge fallback. Use this repository only for Product Content,
Design System, reusable standards, workflows, and templates.
```

## Capability levels

### Browser and repository access

The preferred setup can:

1. open the relevant JobVision domains in the authenticated internal site;
2. read `shared/content/`, `shared/design-system/`, and relevant standards;
3. keep source-backed truth separate from evidence and recommendations;
4. write repository changes only on a dedicated branch and pull request.

### Repository access without the internal site

The AI may work on Content or Design System contracts, but it must stop or ask
for source material before making JobVision product claims. Repository access
does not provide Product Knowledge.

### Cando work

The AI must use <https://docs-cd.jvoffice.ir/> as canonical Cando Product
Knowledge when access is available. If access is unavailable or the source does
not establish a material claim, it must preserve that limitation and keep owner
input, reviewed evidence, observations, and implementation evidence in their
actual authority class. It must not save them as canonical Product Knowledge in
this repository.

## Setup verification

The setup passes when the AI:

- names <https://docs-jv.jvoffice.ir/> as the only JobVision Product Knowledge
  source;
- names <https://docs-cd.jvoffice.ir/> as the only Cando Product Knowledge
  source;
- refuses to use deleted repository Product Knowledge or the other product's
  source as canonical fallback;
- uses the repository manifest only for Content, Design System, and standards;
- separates documented truth, decisions, evidence, observations, hypotheses,
  recommendations, and unknowns.
