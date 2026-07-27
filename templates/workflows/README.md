# Workflow Output Templates

These templates define temporary, reviewable outputs used in `product-work`.

```text
initiative-template.md
→ Structures a proposed initiative and its current-context analysis

prd-template.md
→ Structures intended product behavior and delivery requirements

decision-question-template.md
→ Structures one blocking human decision

product-knowledge-update-proposal-template.md
→ Structures the reviewed handoff from released evidence to canonical documentation changes
```

Workflow outputs are not canonical Product Knowledge and are not included in `manifest.generated.json`.

Use `artifact_type` and workflow-specific states rather than the canonical Product Knowledge `collection` and `type` fields.

Skills own the process and stop conditions. Templates own the output shape. Do not copy template structures back into `SKILL.md` because that creates two sources of truth.
