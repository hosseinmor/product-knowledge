# AI Tool Setup

This repository is tool-agnostic, but Product Knowledge retrieval depends on
the product's approved source.

## One-time bootstrap instruction

Configure the AI workspace or project with this instruction:

```text
Read product-knowledge-sources.yml and AGENTS.md before product work, then route
through ai/router.md. JobVision Product Knowledge is canonical only at
https://docs-jv.jvoffice.ir/ and requires the internal VPN and browser. Cando
has no canonical Product Knowledge source. Never use repository files, Git
history, Figma, screenshots, observed UI, or memory as a Product Knowledge
fallback. Use this repository only for Product Content, Design System, reusable
standards, workflows, and templates.
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

The AI must disclose that no canonical source exists. It may structure explicit
owner input, reviewed evidence, or approved decisions, but must preserve their
authority and unresolved gaps. It must not save them as canonical Product
Knowledge in this repository.

## Setup verification

The setup passes when the AI:

- names <https://docs-jv.jvoffice.ir/> as the only JobVision Product Knowledge
  source;
- states that Cando has no canonical source;
- refuses to use deleted repository Product Knowledge as fallback;
- uses the repository manifest only for Content, Design System, and standards;
- separates documented truth, decisions, evidence, observations, hypotheses,
  recommendations, and unknowns.
