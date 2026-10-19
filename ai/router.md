# AI Intent Router

This file routes a request to the smallest appropriate workflow and repository
guidance. It does not establish product truth.

## Mandatory source gate

Read [`../product-knowledge-sources.yml`](../product-knowledge-sources.yml)
before selecting a route.

```text
JobVision product claim
→ open https://docs-jv.jvoffice.ir/ through the internal VPN and browser
→ load the smallest relevant domain pages
→ record the URLs used

Cando product claim
→ open https://docs-cd.jvoffice.ir/ through a verified internal-browser path
→ load the smallest relevant domain pages
→ record the URLs used

Content or Design System request
→ use this repository for language and interface guidance
→ never let repository guidance invent product behavior
```

If the owning product's canonical site cannot be accessed, preserve the access
limitation and ask for relevant source material when needed. Never use the other
product's canonical source, Git history, deleted repository documents, Figma,
screenshots, observed UI, or memory as a canonical replacement.

## Routing sequence

1. Identify the product and requested outcome.
2. Pass the mandatory source gate.
3. Select one primary workflow.
4. Retrieve only the relevant repository-owned Content, Design System, and
   product-standard documents from `manifest.generated.json`.
5. Keep canonical truth, approved decisions, evidence, observations,
   hypotheses, recommendations, and unknowns separate.
6. Ask a focused question only when a missing decision materially changes the
   result.

## Write or review product content

Load first:

```text
shared/content/content-guidelines.md
shared/content/product-voice.md
shared/content/terminology.md
shared/content/localization.md
```

Then load only the relevant Content Context, pattern, component-copy contract,
and Design System component.

### JobVision Candidate

Load:

```text
shared/content/contexts/jobvision-candidate.md
shared/content/contexts/jobvision-candidate.yml
shared/content/evals/jobvision-candidate-context-cases.yml
```

Product behavior must come from the relevant domain at
<https://docs-jv.jvoffice.ir/>. The Context governs terminology, tone, and
claim boundaries only. Its legacy behavioral routing is under revalidation and
must not be treated as product truth.

### JobVision Employer

Load:

```text
shared/content/contexts/jobvision-employer.md
shared/content/contexts/jobvision-employer.yml
shared/content/evals/jobvision-employer-context-cases.yml
```

For job-post work, start with the internal JobVision documentation root and its
«حوزهٔ آگهی» domain. Load other internal domains only when they materially
affect the request. The Context cannot establish permissions, states, quotas,
moderation, publication behavior, or Candidate-side effects.

### Cando

Use <https://docs-cd.jvoffice.ir/> as canonical Product Knowledge for Cando
current-product meaning and behavior. Do not use draft Cando documents from Git
history, Content Contexts, or unmerged work as canonical truth. If the canonical
site is inaccessible or insufficient for a material claim, keep the limitation
visible and use any supporting evidence only with its actual authority.

## Content pattern routing

| Need | Content source |
|---|---|
| labels, instructions, helper text, placeholders | `shared/content/patterns/instructions-and-helper-text.*` |
| errors and recovery | `shared/content/patterns/errors.*` |
| consequential confirmation | `shared/content/patterns/confirmations.*` |
| empty or zero-result state | `shared/content/patterns/empty-states.*` |
| outcome feedback | `shared/content/patterns/notifications.*` |
| loading or progress | `shared/content/patterns/loading-and-progress.*` |
| AI output, disclosure, automation | `shared/content/patterns/ai-content-and-disclosure.*` |

Load the matching eval file from `shared/content/evals/`.

## Component-copy routing

| Need | Content contract | Design System source |
|---|---|---|
| action label or accessible name | `shared/content/components/button.*` | `shared/design-system/components/button.md` |
| field label, instruction, helper, placeholder | `shared/content/components/text-input.*` | `shared/design-system/components/text-input.md` |
| blocking task or confirmation | `shared/content/components/modal.*` | `shared/design-system/components/modal.md` |
| inline or transient feedback | `shared/content/components/notification.*` | `shared/design-system/components/notification.md` |

Component contracts inherit the product behavior supplied by the approved
source; they do not create an action, consequence, state, or validation.

## Persian and localization

For Persian/English language, RTL, mixed-direction content, numbers, dates,
times, units, amounts, identifiers, names, translation, or runtime variables,
load:

```text
shared/content/localization.md
shared/content/localization.yml
shared/content/evals/localization-cases.yml
```

## PRD writing

Route to:

```text
ai/skills/prd-writing/SKILL.md
ai/prd-writing.md
templates/jira-prd.md
```

Product context comes from the mandatory source gate, not from the repository
manifest. For Cando, current behavior must be grounded in `docs-cd` when the
canonical source establishes it; evidence or owner input may supplement gaps but
must keep their actual authority.

## Research and benchmarking

Route to [`research.md`](research.md). Establish internal context through the
mandatory source gate before external research. When Product Knowledge is
missing or inaccessible, state that limitation instead of filling it with
external patterns.

## Start product design

Route to [`design-start.md`](design-start.md) only after the required product
decisions are available. Product truth comes from the mandatory source gate;
this repository supplies Content and Design System constraints.

## Product Knowledge authoring or update

This repository no longer authors or stores canonical Product Knowledge.

- JobVision changes belong in the workflow and source repository behind
  <https://docs-jv.jvoffice.ir/>.
- Cando changes belong in the workflow and source repository behind
  <https://docs-cd.jvoffice.ir/>.
- Do not author canonical Product Knowledge in this Content/Design repository.

## Multiple intents

Use one primary route and sequence secondary work explicitly. A Content,
Design, PRD, or research request must not silently update Product Knowledge.

## Routing rules

- Route by requested outcome, not only filenames or user role.
- Do not run every workflow for every task.
- Do not treat observed UI as current product policy.
- Do not use archived or deleted Product Knowledge as active context.
- Preserve product-scoped authority: `docs-jv` does not establish Cando
  internals and `docs-cd` does not establish JobVision internals.
