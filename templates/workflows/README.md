# Workflow Output Templates

These templates define temporary, reviewable outputs used in `product-work` or at the boundary between `product-work` and `product-knowledge`.

```text
initiative-template.md
→ Structures a proposed initiative and its current-context analysis

prd-template.md
→ Structures intended product behavior and delivery requirements

decision-question-template.md
→ Structures one blocking human decision

product-knowledge-handoff-template.yaml
→ Identifies a reviewed or released source and routes it to Product Knowledge update

product-knowledge-update-proposal-template.md
→ Structures the reviewable proposal from source evidence to canonical documentation changes
```

Workflow outputs and handoffs are not canonical Product Knowledge and are not included in `manifest.generated.json`.

Use `artifact_type`, handoff fields, and workflow-specific states rather than canonical Product Knowledge `collection` and `type` fields.

Skills own process and stop conditions. Templates own output shape. Do not copy template structures back into `SKILL.md` because that creates two sources of truth.

See `docs/product-work-handoff.md` for readiness, idempotency, acknowledgement, and failure rules across repositories.
