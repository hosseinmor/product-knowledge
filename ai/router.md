# AI Intent Router

This file routes a user request to the smallest appropriate Skill or workflow. It does not replace those files or duplicate their full instructions.

## Routing sequence

1. Identify the primary user outcome.
2. Select one primary Skill or workflow from the routes below.
3. Load supporting workflows only when they materially affect the primary outcome.
4. Use `manifest.generated.json` for Product Knowledge retrieval after the route is selected.
5. When intent is ambiguous and the route would materially change the result, ask one focused clarification question.

## Routes

### Create, complete, structure, or review Product Knowledge from owner input

Examples:

- "این بخش محصول رو توضیح می‌دم، تبدیلش کن به Product Area"
- "از این توضیحات Product Knowledge بساز"
- "این Factها کدومش Area است و کدوم Concept؟"
- "این Product Concept را با دانشی که می‌دم کامل کن"
- "این Area را بررسی کن و knowledgeهای misplaced یا missing را مشخص کن"

Route to:

```text
ai/skills/product-knowledge-authoring/SKILL.md
```

The Skill loads:

```text
ai/product-knowledge-authoring.md
templates/product-area.md
templates/shared-product-concept.md
manifest.generated.json
```

Use this route when the main task is turning compact or free-form human product knowledge into the canonical Area/Concept structure. Do not require complete walkthrough coverage before producing a review draft.

### Create, complete, revise, or review a PRD

Examples:

- "برای این موضوع PRD بنویسیم"
- "این Jira item را کامل کن"
- "این PRD چه چیزهایی کم دارد؟"
- "بعد از این تصمیم‌ها PRD را اصلاح کن"

Route to:

```text
ai/skills/prd-writing/SKILL.md
```

The Skill loads:

```text
ai/prd-writing.md
templates/jira-prd.md
manifest.generated.json
```

### Research or benchmarking

Examples:

- Investigate a product problem
- Compare external patterns or competitors
- Gather evidence before defining a change

Route to:

```text
ai/research.md
```

When the research will directly produce a PRD, use the PRD Skill as the primary route and use the research workflow only as supporting work.

### Start product design from an approved PRD

Examples:

- Prepare a user flow
- Define information architecture
- Create a screen inventory or state matrix
- Prepare an initial UI or component mapping

Route to:

```text
ai/design-start.md
```

Do not route incomplete product definition to design-start when unresolved blocking product decisions should be handled through PRD writing first.

### Update canonical Product Knowledge from reviewed evidence or approved decisions

Examples:

- Apply newly approved product behavior to existing canonical docs
- Correct outdated or contradictory documentation after owner resolution
- Reconcile a reviewed walkthrough evidence package
- Apply an already reviewed Product Knowledge authoring draft to the repository

Route to:

```text
ai/knowledge-update.md
```

Use `product-knowledge-authoring` first when raw owner knowledge still needs to be interpreted, structured, or split between Area and Concept ownership.

Do not silently update Product Knowledge as a side effect of another workflow. Present the proposed update separately and follow the normal owner-reviewed branch and pull-request process.

Walkthrough capture and evidence review are maintained in the separate `hosseinmor/product-walkthrough` repository. This router handles only later authoring or knowledge-update work after evidence or owner knowledge is available.

## Multiple intents

Use one primary route and sequence secondary work explicitly.

Common sequences:

```text
Owner explains current product behavior
→ Primary: Product Knowledge Authoring Skill
→ Owner reviews structured draft
→ If approved for repository write: knowledge-update workflow

Research needed for a PRD
→ Primary: PRD Skill
→ Supporting: research workflow
→ Return to PRD blocking decisions and draft

Approved PRD moves to design
→ Complete PRD Skill and human approval
→ Then use design-start

A completed task or reviewed evidence package exposes missing Product Knowledge
→ Finish the primary task
→ Then use knowledge-update as a separate proposal
```

## Routing rules

- Do not route based only on filenames or the user's role.
- Route based on the requested outcome.
- Do not run every workflow for every task.
- Do not treat workflows as mandatory sequential gates.
- Do not use archived Skills as active instructions unless explicitly requested.
- Keep human decision and approval points visible.
