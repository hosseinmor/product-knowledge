---
name: product-knowledge-authoring
description: Turn Product Area Owner Input or a natural-language owner conversation into a reviewable Product Area and correctly routed Product Concept knowledge using the repository's authoring workflow and canonical templates.
---

# Product Knowledge Authoring

## Purpose

Turn compact owner knowledge into structured Product Knowledge without requiring the owner to complete the full canonical Product Area or Product Concept template manually.

The default authoring path is owner-knowledge-first. Walkthrough and repository coverage may be incomplete, so AI should structure, classify, and ask focused product questions rather than reconstruct undocumented behavior from sparse evidence.

AI performs classification, Area/Concept ownership, focused follow-up, drafting, gap detection, boundary derivation, and normalization. The responsible human supplies current product knowledge, resolves conflicts, and approves the final result.

## Activate this skill when

The user asks to:

- Create a Product Area from `Product Area Owner Input`
- Create a Product Area from a product-owner explanation or conversation
- Turn unstructured PM/owner notes into Product Knowledge
- Create or complete a Product Concept from raw product knowledge
- Review a Product Area or Product Concept for wrong classification, duplication, missing knowledge, or Area/Concept ownership
- Convert mixed product facts into the correct Area and Concept destinations

Typical requests include:

- "این Owner Input رو تبدیل کن به Product Area"
- "می‌خوام Product Area مربوط به Candidate Apply رو مستند کنیم"
- "این بخش محصول رو توضیح می‌دم، ازم سؤال‌های لازم رو بپرس و Area رو بساز"
- "این Factها کدومش Area است و کدوم Concept؟"

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

templates/product-area-owner-input.md
→ Owner-facing intake guide; useful for a filled document or conversational interview

templates/product-area.md
→ Product Area output contract

templates/shared-product-concept.md
→ Product Concept output contract

manifest.generated.json
→ Retrieval entry point for reviewed Product Knowledge
```

Read `README.md` when product hierarchy or repository placement matters.

Load `ai/knowledge-update.md` only when the user asks to apply an approved result to canonical repository files.

## Owner experience

The owner should not need to understand the canonical document structure.

The intended experience is:

```text
Owner names the Product Area
→ Owner fills Product Area Owner Input or explains the product in their own words
→ AI asks only material product questions
→ AI produces Product Area draft and routes Concept knowledge
→ Owner corrects / approves
→ AI normalizes the final draft
```

Do not ask the owner to fill sections such as `Permissions`, `State Transitions`, `Main Concepts`, or `Boundaries` in canonical terminology.

Ask about the product itself.

Bad follow-up:

> لطفاً بخش Known Variations را کامل کنید.

Good follow-up:

> آیا رفتار این Flow برای Plan یا نوع کاربر خاصی متفاوت است؟ اگر بله، چه تفاوتی دارد؟

## Minimum input

Do not require a full form.

Obtain from the conversation, supplied Owner Input, or the owner only enough to identify:

- Product context
- The Product Area or subject being documented
- Some actual current product knowledge about its behavior or meaning

Free-form input is acceptable.

The Owner Input template asks about:

- What the Area does
- Main behavior / flows
- Important rules and limits
- Important behavioral differences
- Real unusual/failure cases
- Unknowns
- Sources or knowledgeable people

The owner may leave sections empty when they do not know or do not apply.

## Source handling

Treat source roles explicitly:

1. Explicit responsible-owner input → primary proposed current product truth for the authoring draft
2. `status: reviewed` Product Knowledge on `main` → trusted current canonical context
3. Supplied reviewed evidence or other authoritative sources → supporting evidence with their original authority
4. `status: draft` Product Knowledge → not current truth; ignore by default during authoring unless the user explicitly asks to inspect it for history, conflicts, or recovery of prior notes
5. External research → only when explicitly requested and never as internal product truth

Do not let a clean-looking draft document override explicit owner knowledge merely because it is already in the repository.

When reviewed Product Knowledge and owner input conflict, preserve the conflict and ask for resolution when it materially affects the result. Never silently choose one.

Sparse evidence is not permission to fabricate missing behavior.

## Workflow

### 1. Load contracts and choose mode

Read the workflow, Owner Input guide, both canonical templates, and the manifest.

Choose one primary mode:

```text
Product Area
Product Concept
Mixed intake
```

Use the workflow's ownership rules rather than the user's wording alone.

### 2. Retrieve only trusted relevant context

Use the manifest to find the smallest relevant set of `status: reviewed` Product Knowledge needed to understand:

- Established naming
- Existing reviewed Area boundaries
- Existing reviewed Concepts
- Potential duplicate canonical knowledge
- Trusted adjacent behavior

Do not use draft Areas or Concepts as product truth by default.

Do not scan the full repository.

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

### 4. Ask focused follow-up questions only when material

Before drafting, identify missing information that can materially change the Area model.

Prioritize gaps about:

- Main Flow or outcome
- Important Business Rule or limit
- Eligibility / Permission
- Important stable-context variation
- Real exception, failure, or recovery behavior
- A material ambiguity that changes Area vs Concept ownership

Ask questions about the product, not about template sections.

By default, ask one focused batch of no more than five material questions. If more low-confidence gaps remain, keep them as Unknowns instead of turning the interaction into a long interview.

Do not ask questions whose answers are already present in the Owner Input, current conversation, or trusted reviewed Product Knowledge.

### 5. Draft the semantic model before deriving boundaries

For Product Areas, understand flows, rules, actors, concepts, validations, transitions, variations, errors, and adjacent areas first.

Then derive `Overview` and `Boundaries` from the complete model.

Display Boundaries near the beginning because they help readers, even though AI should derive them late in the reasoning process.

For Product Concepts, understand definition, business meaning, attributes, relationships, intrinsic rules, lifecycle, and meaningful variants before deriving boundaries and terminology.

### 6. Produce the canonical review draft

Use the matching canonical template.

Do not require the owner to manually provide sections AI can derive from supplied knowledge and trusted context, such as:

- Overview
- Boundaries
- Main Concepts / Used In Product Areas
- Related Knowledge
- Terminology normalization
- Source formatting
- Gap-derived Unknowns

Do not fill substantive missing behavior merely because the template contains a section.

If raw input contains facts owned by another document, route them conceptually rather than duplicating them. Return a short `Knowledge routing` note showing the affected destination when useful.

### 7. Run the owner-review pass

Return the useful draft first.

Then surface only high-value corrections or unresolved Unknowns, for example:

- A potentially missing important Flow
- A rule or limit that still needs confirmation
- An AI-derived boundary that needs owner confirmation
- A Concept candidate that may need canonical definition
- A conflict with reviewed Product Knowledge

Do not turn review into another full template form.

### 8. Reconcile corrections

When the owner responds:

- Apply explicit corrections
- Reclassify misplaced knowledge
- Regenerate derived Overview/Boundaries when behavior changes
- Remove duplication
- Keep unresolved contradictions visible
- Preserve unknowns rather than guessing

### 9. Canonical write only after approval

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
3. Important conflicts with reviewed Product Knowledge
4. Remaining material Unknowns
5. Sources used

For a mixed intake, return the primary requested document first, then a compact routing list for other affected canonical destinations.

Use the template's canonical section names. Write body content in Persian unless the user uses another language. Preserve established English product/domain terms such as Application, Job Post, Flow, State, Plan, and Permission when translation would reduce precision.

## Validation

Before delivery, verify that:

- No unsupported product behavior was invented.
- Owner input was not lost merely because it did not match template wording.
- Draft Product Knowledge was not used as canonical truth.
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

- Supplying tacit current product knowledge when trusted sources are incomplete
- Resolving contradictions
- Confirming important rules, exceptions, and boundaries
- Approving final canonical Product Knowledge

## Rules

- Do not make the owner fill the complete canonical template unless they explicitly want to.
- Do not assume AI-generated completeness from sparse walkthrough or repository evidence.
- Do not treat `status: draft` Product Knowledge as current truth by default.
- Do not invent a Product Concept solely to fill a template slot.
- Do not create competing definitions of the same Concept in multiple Areas.
- Do not silently overwrite reviewed Product Knowledge.
- Do not update canonical repository content as a side effect of drafting.
- Keep this Skill as orchestration; detailed classification rules belong in `ai/product-knowledge-authoring.md` and document structure belongs in the templates.
