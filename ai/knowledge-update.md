# Product Knowledge Update

## Goal

Keep Product Knowledge useful without introducing a separate release-handoff system, while preserving a clear distinction between evidence, owner knowledge, product decisions, and canonical product knowledge.

Use `ai/product-knowledge-authoring.md` first when raw owner knowledge still needs to be interpreted, structured, or split between Product Area and Product Concept ownership. Use this workflow when the intended canonical changes are already reviewable and need to be reconciled into the repository.

## Evidence eligibility

Walkthrough capture artifacts are evidence, not Product Knowledge.

Use this gate for walkthrough-derived knowledge:

```text
draft or unreviewed walkthrough evidence
→ cannot establish canonical Product Knowledge

reviewed evidence accepted by the walkthrough owner
→ eligible for reconciliation

owner-confirmed knowledge from another authoritative source
→ eligible for reconciliation when the source is recorded
```

Narrated or inferred claims do not become product truth merely because they appear in an evidence package. Their final reviewed claim and owner decision determine whether they are eligible for reconciliation.

An owner-reviewed Product Knowledge Authoring draft is also eligible for reconciliation when the responsible owner has explicitly confirmed its current-product claims.

## Process

1. AI or a team member identifies missing, outdated, contradictory, or newly decided knowledge.
2. Read `manifest.generated.json` to find the affected Product Group Overview, Product Overview, Product Area, Product Concept, Shared Product Service, Design System, or shared-guidance documents.
3. If the source is a walkthrough package, verify that the relevant evidence is reviewed before using it to establish Product Knowledge.
4. If the source is an authoring draft, verify that the responsible owner reviewed the product claims before treating them as canonical.
5. Reconcile each eligible claim against the current product model before drafting document changes.
6. AI proposes exact changes to the smallest relevant document set.
7. The proposal must state:
   - What should change
   - Why
   - Which source supports it
   - The source authority or provenance when it matters
   - What remains unknown
8. The named owner reviews the proposal.
9. Apply approved changes through a normal branch and pull request.
10. After review, set `status: reviewed` and update `last_reviewed` when appropriate.
11. Regenerate `manifest.generated.json` in the same branch when indexed documents changed.
12. Run `python scripts/generate_manifest.py check` before merging.
13. When the change affects the Design System accessibility corpus, accessibility routing, accessibility governance, or a Component/Pattern maturity state used by accessibility retrieval, run `python scripts/check_accessibility_knowledge.py` and the applicable manual regression gate in `shared/design-system/accessibility/testing.md` before merging.

## Reconciliation taxonomy

For every eligible claim, choose the smallest appropriate knowledge impact before editing documents:

```text
confirm-existing
→ supports current documented behavior; add or strengthen provenance only when useful

extend-existing
→ adds a rule, state, permission, validation, edge case, flow step, variation, attribute, relationship, or other knowledge to an existing document

correct-contradiction
→ conflicts with current Product Knowledge and requires explicit owner review before replacement

add-unknown
→ reveals an unresolved question, untested behavior, or scope limitation that should remain visible

update-another-area
→ the claim belongs primarily to a different Product Area than the source context

candidate-concept
→ reveals a concept with potentially independent meaning, attributes, relationships, intrinsic rules, or lifecycle that may deserve a canonical Product Concept

promote-concept
→ a recurring or important concept should move from local Area wording into a canonical Product Concept used by multiple Product Areas

shared-service
→ reveals durable cross-product service behavior used by several products

no-canonical-change
→ useful evidence that does not require a Product Knowledge change
```

A walkthrough does not create a Product Area by default. Product Area creation is a product-modeling decision made during reconciliation. One walkthrough may update multiple Product Areas, and several walkthroughs may contribute to one Product Area.

Likewise, do not create one Product Concept for every noun. Promote a Concept when an independent definition materially improves consistency, especially when it is reused across Areas, has its own attributes or relationships, has intrinsic rules or lifecycle, or changes in its definition would affect several Areas.

## Product model check

Before creating a new Product Area, verify:

- The Area represents a meaningful and relatively independent user outcome, capability, or business process, not a page, modal, navigation destination, Jira Epic, team, or walkthrough scope.
- Existing Product Areas cannot own the behavior cleanly without becoming incoherent.
- The proposed `Includes` and `Does Not Include` boundary is consistent with adjacent Areas.
- Shared Concepts do not imply Area overlap. Area overlap exists only when two Areas claim canonical ownership of the same behavior.

Before creating or promoting a Product Concept, verify:

- The Concept has an independent business meaning beyond one Flow or UI surface.
- Its definition, attributes, relationships, intrinsic rules, or lifecycle should be canonical rather than repeated locally.
- Area-specific behavior is not being moved into the Concept merely because the Concept appears in that Area.

## Area and Concept ownership

Use this rule:

```text
Meaning and intrinsic truth of a thing
→ Product Concept

Behavior of things in a context
→ Product Area
```

More specifically:

- Attribute existence and meaning → Product Concept.
- Context-dependent requiredness or validation → Product Area.
- Canonical States and lifecycle → Product Concept.
- Transitions created, used, or controlled in one context → Product Area.
- Semantic relationships between Concepts → Product Concept.
- Navigation to related docs → Product Area `Related Knowledge`.
- Intrinsic context-independent rules → Product Concept.
- Contextual behavior rules → Product Area.

Do not duplicate the same canonical rule or definition in both documents.

## Provenance

Keep canonical knowledge, observations, and unknowns distinguishable without making documents noisy.

- Owner-confirmed current product knowledge can become canonical after review.
- Reviewed walkthrough evidence is eligible supporting evidence, but observations should not be generalized beyond what the evidence and owner review support.
- Draft, inferred, contradictory, and untested behavior must remain explicit.
- Use `Sources & Evidence` to record material provenance and source authority when useful.
- Use `Unknowns & Unverified Behavior` for unresolved behavior.

Do not add per-sentence metadata unless traceability needs justify the maintenance cost.

## Placement rules

- Product-group relationships belong in the Product Group Overview.
- Product-specific contextual behavior stays in Product Areas.
- Canonical business definitions, attributes, relationships, intrinsic rules, and lifecycle belong in Product Concepts when promoted.
- Cross-product service behavior belongs in Shared Product Services.
- Product-specific use of a shared service stays in the consuming Product Area.
- Reusable UI behavior belongs in the Design System.
- The owning team appears in `owner`; team structure does not define repository hierarchy.

## Rules

- Do not write assumptions as confirmed behavior.
- Do not use draft or unreviewed walkthrough evidence to establish canonical Product Knowledge.
- Do not treat walkthrough scope or UI navigation as Product Area boundaries by default.
- Do not update unrelated documents.
- Keep unknowns and untested behavior visible.
- Preserve contradictions until an owner resolves them; do not silently overwrite current knowledge.
- Do not redefine Product Concepts inside Product Areas.
- The manifest is generated; do not edit it manually.
- Accessibility audit reports and stress-test evidence must not silently become ordinary operational Design System retrieval content.
