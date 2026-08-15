---
name: product-knowledge-authoring
description: Turn short or free-form product-owner knowledge into a reviewable Product Area or Product Concept using the repository's canonical Product Knowledge, authoring workflow, templates, and retrieval manifest.
---

# Product Knowledge Authoring

## Purpose

Turn compact, natural-language owner input into structured Product Knowledge without requiring the owner to complete the full canonical template manually.

This Skill is intentionally owner-knowledge-first. It assumes walkthrough and evidence coverage may be incomplete, so AI should structure and classify knowledge rather than pretend it can reconstruct the product from sparse evidence.

AI performs retrieval, classification, Area/Concept ownership, drafting, gap detection, boundary derivation, and normalization. The responsible human supplies tacit product knowledge, resolves conflicts, and approves the canonical result.

## Activate this skill when

The user asks to:

- Create a Product Area from short notes or a product-owner explanation
- Create or complete a Product Concept from raw product knowledge
- Turn unstructured PM/owner notes into canonical Product Knowledge
- Review a Product Area or Product Concept for wrong classification, duplication, missing knowledge, or Area/Concept ownership
- Convert a mixed set of product facts into the correct Area and Concept destinations
- Reduce the amount of template-filling required from a product owner

Typical requests include:

- "این بخش محصول رو توضیح می‌دم، تبدیلش کن به Product Area"
- "از این توضیحات Product Knowledge بساز"
- "این Factها کدومش Area است و کدوم Concept؟"
- "این Concept رو با توجه به اطلاعاتی که می‌دم کامل کن"

## Do not activate this skill for

- Writing or reviewing a PRD → use `ai/skills/prd-writing/SKILL.md`
- General product Q&A with no authoring outcome
- External research or benchmarking with no Product Knowledge authoring outcome
- Product Walkthrough capture or evidence review
- Design-only work
- A focused post-release reconciliation from already reviewed evidence when no owner-intake authoring is needed → use `ai/knowledge-update.md`

## Required repository sources

Always use these files as contracts:

```text
ai/product-knowledge-authoring.md
→ Authoring and classification workflow

templates/product-area.md
→ Product Area output contract

templates/shared-product-concept.md
→ Product Concept output contract

manifest.generated.json
→ Retrieval entry point
```

Read `README.md` when product hierarchy or repository placement matters.

Load `ai/knowledge-update.md` only when the user asks to apply the reviewed result to canonical repository files.

## Minimum input

Do not require a full form.

Obtain from the conversation, supplied notes, or the owner only enough to identify:

- Product context
- The subject being documented
- Some actual product knowledge about its behavior or meaning

Free-form input is acceptable.

Useful but optional owner input includes:

- Main flows
- Important rules and limits
- Eligibility or permission conditions
- Variations by stable context
- Real exceptions
- Unknowns
- Sources or links

Do not ask the owner to restate information already available in the conversation or current Product Knowledge.

## Source handling

Treat source roles explicitly:

1. Current `main` Product Knowledge → current canonical model and terminology
2. Explicit responsible-owner input → proposed current product truth for the draft
3. Supplied evidence or links → supporting evidence with its original authority
4. External research → only when explicitly requested and never as internal product truth

When current Product Knowledge and owner input conflict, preserve the conflict and ask for resolution if it materially affects the draft. Never silently choose one.

Sparse evidence is not permission to fabricate missing behavior.

## Workflow

### 1. Load contracts and choose mode

Read the workflow, both canonical templates, and the manifest.

Choose one primary mode:

```text
Product Area
Product Concept
Mixed intake
```

Use the workflow's ownership rules rather than the user's wording alone.

### 2. Retrieve only relevant current Product Knowledge

Use the manifest to read the smallest relevant set of current documents needed to understand:

- Established naming
- Existing Area boundaries
- Existing Concepts
- Potential duplicate knowledge
- Adjacent behavior

Do not scan the full repository by default.

### 3. Interpret owner input without forcing template language

Accept the owner's wording as-is.

Break it into product claims and classify each claim by semantic ownership.

Use these core tests:

```text
"What is this thing?"
→ Product Concept

"What happens to this thing in this context?"
→ Product Area
```

Also enforce:

- Attribute meaning → Concept
- Contextual requiredness/validation → Area
- Canonical state/lifecycle → Concept
- Contextual transition → Area
- Semantic Concept relationship → Concept
- Related-document navigation → Area Related Knowledge
- User state/plan/segment ≠ Role
- Temporary flow condition ≠ Known Variation
- Normal alternate path/retry ≠ Edge Case

### 4. Draft the semantic model before deriving boundaries

For Product Areas, understand flows, rules, actors, concepts, validations, transitions, variations, errors, and adjacent areas first.

Then derive `Overview` and `Boundaries` from the complete model.

Display Boundaries near the beginning because they help readers, even though AI should derive them late in the reasoning process.

For Product Concepts, understand definition, business meaning, attributes, relationships, intrinsic rules, lifecycle, and meaningful variants before deriving boundaries and terminology.

### 5. Produce the canonical review draft

Use the matching template.

Do not require the owner to manually provide sections AI can derive from supplied knowledge and current context, such as:

- Overview
- Boundaries
- Main Concepts / Used In Product Areas
- Related Knowledge
- Terminology normalization
- Source formatting
- Gap-derived Unknowns

Do not fill substantive missing behavior merely because the template contains a section.

If raw input contains facts owned by another document, move them conceptually rather than duplicating them. Return a short `Knowledge routing` note showing the affected destination when useful.

### 6. Run a focused owner-review pass

After producing a useful draft, surface only high-value gaps or corrections.

Prioritize questions such as:

- Is a main Flow missing?
- Is an important rule or limit missing?
- Are there permission or eligibility conditions the sources cannot reveal?
- Does behavior differ by Plan, Platform, Role, Segment, Location, or another stable context?
- Is a real exception missing?
- Is an AI-derived boundary wrong?
- Which Unknowns can the owner resolve now?

Do not turn review into another full template form.

When no blocking clarification is needed, deliver the draft first and include the focused review items after it.

### 7. Reconcile corrections

When the owner responds:

- Apply explicit corrections
- Reclassify misplaced knowledge
- Regenerate derived Overview/Boundaries when behavior changes
- Remove duplication
- Keep unresolved contradictions visible
- Preserve unknowns rather than guessing

### 8. Canonical write only after approval

The authoring draft is not canonical until the responsible human approves it.

If the user asks to apply it to the repository:

1. Load `ai/knowledge-update.md`.
2. Modify only the smallest affected document set.
3. Use a dedicated branch and pull request.
4. Regenerate `manifest.generated.json` when indexed Product Knowledge documents change.
5. Do not claim approval on behalf of the owner.

## Output contract

For a normal authoring request, return:

1. The reviewable Product Area or Product Concept draft using the canonical template
2. `Knowledge routing` only when facts belong in other Areas/Concepts or a Candidate Concept emerged
3. Important conflicts with current Product Knowledge
4. Focused owner-review questions / remaining Unknowns
5. Sources used

For a mixed intake, return the primary requested document first, then a compact routing list for other affected canonical destinations.

Use the template's canonical section names. Write body content in Persian unless the user uses another language. Preserve established English product/domain terms such as Application, Job Post, Flow, State, Plan, and Permission when translation would reduce precision.

## Validation

Before delivery, verify that:

- No unsupported product behavior was invented.
- Owner input was not lost merely because it did not match template wording.
- Area behavior and Concept truth are not duplicated.
- Main Concepts are referenced rather than redefined inside Areas.
- Intrinsic Concept rules are not rewritten as Area rules.
- User states/plans/segments are not modeled as Roles.
- Main, alternate, and error/recovery behavior are separated.
- Entry Points are surfaces + actions, not full journeys.
- Known Variations represent stable contexts.
- Edge Cases are real unusual cases rather than normal branches.
- Canonical lifecycle stays in Concepts and only relevant transitions stay in Areas.
- Boundaries agree with the actual documented behavior.
- Unknowns and contradictions remain visible.

## Human responsibilities

Humans are responsible for:

- Supplying tacit current product knowledge when sources are incomplete
- Resolving contradictions
- Confirming important rules, exceptions, and boundaries
- Approving final canonical Product Knowledge

## Rules

- Do not make the owner fill the complete canonical template unless they explicitly want to.
- Do not assume AI-generated completeness from sparse walkthrough or repository evidence.
- Do not invent a Product Concept solely to fill a template slot.
- Do not create competing definitions of the same Concept in multiple Areas.
- Do not silently overwrite current Product Knowledge.
- Do not update canonical repository content as a side effect of drafting.
- Keep this Skill as orchestration; detailed classification rules belong in `ai/product-knowledge-authoring.md` and document structure belongs in the templates.