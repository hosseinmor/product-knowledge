# AI Workflows and Skills

AI workflows in this repository consume Product Knowledge from the authority
defined in [`../product-knowledge-sources.yml`](../product-knowledge-sources.yml).
They do not retrieve product behavior from this repository.

```text
AGENTS.md
→ Product Knowledge source gate

ai/router.md
→ Intent routing

product-knowledge-sources.yml
→ JobVision external authority and Cando missing-source state

manifest.generated.json
→ Repository-owned Content, Design System, and standards only
```

## Active workflows

- [`prd-writing.md`](prd-writing.md)
- [`research.md`](research.md)
- [`design-start.md`](design-start.md)

The PRD execution Skill is in [`skills/prd-writing/SKILL.md`](skills/prd-writing/SKILL.md).

Product Knowledge authoring and update workflows were removed because
canonical Product Knowledge is no longer stored here. JobVision updates belong
in the source behind <https://docs-jv.jvoffice.ir/>. Cando requires a separate
approved repository and internal site before canonical authoring can resume.

Every workflow must separate canonical truth, approved decisions, evidence,
observations, hypotheses, recommendations, and unknowns.
