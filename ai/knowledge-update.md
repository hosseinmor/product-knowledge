# Product Knowledge Update

## Goal

Keep Product Knowledge useful without introducing a separate release-handoff system, while preserving a clear distinction between evidence, product decisions, and canonical product knowledge.

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

## Process

1. AI or a team member identifies missing, outdated, contradictory, or newly decided knowledge.
2. Read `manifest.generated.json` to find the affected Product Group Overview, Product Overview, Product Area, Shared Product Concept, Shared Product Service, Design System, or shared-guidance documents.
3. If the source is a walkthrough package, verify that the relevant evidence is reviewed before using it to establish Product Knowledge.
4. Reconcile each eligible claim against the current product model before drafting document changes.
5. AI proposes exact changes to the smallest relevant document set.
6. The proposal must state:
   - What should change
   - Why
   - Which source supports it
   - The source authority or provenance when it matters
   - What remains unknown
7. The named owner reviews the proposal.
8. The owner edits the document through a normal branch and pull request.
9. After review, set `status: reviewed` and update `last_reviewed` when appropriate.
10. Regenerate `manifest.generated.json` in the same branch.
11. Run `python scripts/generate_manifest.py check` before merging.

## Reconciliation taxonomy

For every eligible claim, choose the smallest appropriate knowledge impact before editing documents:

```text
confirm-existing
→ supports current documented behavior; add or strengthen provenance only when useful

extend-existing
→ adds a rule, state, permission, validation, edge case, flow step, variation, or other behavior to an existing document

correct-contradiction
→ conflicts with current Product Knowledge and requires explicit owner review before replacement

add-unknown
→ reveals an unresolved question, untested behavior, or scope limitation that should remain visible

update-another-area
→ evidence belongs primarily to a different Product Area than the walkthrough's candidate scope

local-concept
→ introduces a concept needed to understand one Product Area; keep it in that Product Area

shared-concept
→ reveals a business concept whose identity, definition, lifecycle, or rules are genuinely shared across products

shared-service
→ reveals durable cross-product service behavior used by several products

no-canonical-change
→ useful evidence that does not require a Product Knowledge change
```

A walkthrough does not create a Product Area by default. Product Area creation is a product-modeling decision made during reconciliation. One walkthrough may update multiple Product Areas, and several walkthroughs may contribute to one Product Area.

## Product model check

Before creating a new Product Area, verify:

- The area represents a meaningful and relatively independent user or product outcome, not a page, modal, navigation destination, Jira Epic, or walkthrough scope.
- Existing Product Areas cannot own the behavior cleanly without becoming incoherent.
- The proposed boundary has a clear `Owns`, `Does not own`, and handoff relationship with adjacent areas.
- Concepts that are merely local stay in the Product Area; genuinely cross-product concepts or services are promoted to the appropriate shared location.

When evidence spans several areas, update the existing areas instead of creating a container that mirrors the walkthrough or UI navigation.

## Provenance in Product Areas

Keep canonical and observational knowledge distinguishable:

- `Confirmed product behavior` is backed by the named owner or another authoritative product source.
- `Observed but not yet confirmed` is backed by reviewed production walkthrough evidence but is not yet established as canonical policy.
- Unknown, inferred, draft, and untested behavior stays explicit and must not be phrased as confirmed product truth.
- Sources should identify their authority when that distinction affects interpretation.

Do not add per-sentence metadata unless traceability needs justify the extra maintenance cost. Prefer section-level provenance plus explicit source references.

## Placement rules

- Product-group relationships belong in the Product Group Overview.
- Product-specific behavior stays in the Product Area.
- Genuinely shared definitions and rules belong in Shared Product Concepts.
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
- The manifest is generated; do not edit it manually.
