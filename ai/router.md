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

### Write or review product content

Examples:

- Write or review labels, helper text, errors, notifications, or AI disclosures
- Check whether product copy uses the correct JobVision concept and audience label
- Adapt content tone for a product surface without changing product behavior
- Evaluate generated UI copy against deterministic content rules

Route first to:

```text
shared/content/content-guidelines.md
shared/content/product-voice.md
shared/content/terminology.md
shared/content/localization.md
```

Then load only the relevant pattern, component contract, Product Area, and
machine-readable source.

When the copy is for the JobVision Candidate product or addresses a jobseeker,
also load:

```text
shared/content/contexts/jobvision-candidate.md
shared/content/contexts/jobvision-candidate.yml
shared/content/evals/jobvision-candidate-context-cases.yml
products/jobvision/candidate/overview.md
```

Then load only the owning Candidate Product Area for the behavior in question:

```text
job search                         → products/jobvision/candidate/areas/job-search.md
job details and actions            → products/jobvision/candidate/areas/job-post-experience.md
recommendations and preferences    → products/jobvision/candidate/areas/recommended-jobs.md
application submission/tracking    → products/jobvision/candidate/areas/application-management.md
resume and AI assessment           → products/jobvision/candidate/areas/resume-management.md
```

When the copy is for the JobVision Employer product or an employer-side
operational surface, also load:

```text
shared/content/contexts/jobvision-employer.md
shared/content/contexts/jobvision-employer.yml
shared/content/evals/jobvision-employer-context-cases.yml
products/jobvision/employer/overview.md
```

For job-post creation, editing, publication, or management behavior, also load:

```text
products/jobvision/employer/areas/job-post-management.md
```

Employer Account and Access, Candidate/Application Management, and
Products/Plans do not yet have substantive Product Areas. Preserve unknowns
instead of inferring permissions, states, quotas, or entitlement behavior.

For Persian/English language changes, RTL or mixed-direction content, numbers,
dates, times, units, amounts, translation, or runtime variables, also load:

```text
shared/content/localization.yml
shared/content/evals/localization-cases.yml
```

For Button labels, CTA wording, action-versus-navigation decisions, Button
Loading labels, confirmation actions, or Button accessible names, also load:

```text
shared/content/components/button.md
shared/content/components/button.yml
shared/content/evals/button-content-cases.yml
shared/design-system/components/button.md
shared/design-system/experience-rules/action-hierarchy.md
```

For error content, load:

```text
shared/content/patterns/errors.md
shared/content/patterns/errors.yml
shared/content/evals/error-cases.yml
```

For labels, instructions, helper text, placeholders, examples, requirement
indicators, or field guidance, load:

```text
shared/content/patterns/instructions-and-helper-text.md
shared/content/patterns/instructions-and-helper-text.yml
shared/content/evals/instruction-helper-cases.yml
```

When that content is composed inside a single-line Text Input, also load:

```text
shared/content/components/text-input.md
shared/content/components/text-input.yml
shared/content/evals/text-input-content-cases.yml
shared/design-system/components/text-input.md
shared/design-system/accessibility/forms.md
```

For confirmations or destructive actions, load:

```text
shared/content/patterns/confirmations.md
shared/content/patterns/confirmations.yml
shared/content/evals/confirmation-cases.yml
```

When the confirmation, focused task/form, or response-required information is
inside a blocking Modal, also load:

```text
shared/content/components/modal.md
shared/content/components/modal.yml
shared/content/evals/modal-content-cases.yml
shared/design-system/components/modal.md
shared/design-system/accessibility/focus-management.md
```

For empty states or zero-result experiences, load:

```text
shared/content/patterns/empty-states.md
shared/content/patterns/empty-states.yml
shared/content/evals/empty-state-cases.yml
```

For notifications, Toasts, or outcome feedback, load:

```text
shared/content/patterns/notifications.md
shared/content/patterns/notifications.yml
shared/content/evals/notification-cases.yml
```

When that feedback is composed inside an Inline Notification or Toast, also
load:

```text
shared/content/components/notification.md
shared/content/components/notification.yml
shared/content/evals/notification-content-cases.yml
shared/design-system/components/notification.md
shared/design-system/accessibility/dynamic-content-and-feedback.md
```

For loading, async status, or determinate/indeterminate progress, load:

```text
shared/content/patterns/loading-and-progress.md
shared/content/patterns/loading-and-progress.yml
shared/content/evals/loading-progress-cases.yml
```

For AI entry points, generated or suggested content, assistants, automation, or
AI disclosure, load:

```text
shared/content/patterns/ai-content-and-disclosure.md
shared/content/patterns/ai-content-and-disclosure.yml
shared/content/evals/ai-content-cases.yml
```

Product Knowledge owns what the product does. Shared Content owns how that
truth is named and communicated. The Design System owns component and
interaction mechanics. Do not invent missing product behavior while improving
copy.

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
