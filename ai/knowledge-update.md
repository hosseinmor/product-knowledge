# Product Knowledge Update

## Goal

Keep Product Knowledge useful without introducing a separate release-handoff system.

## Process

1. AI or a team member identifies missing, outdated, contradictory, or newly decided knowledge.
2. Read `manifest.generated.json` to find the affected Product Group Overview, Product Overview, Product Area, Shared Product Concept, Shared Product Service, Design System, or shared-guidance documents.
3. AI proposes exact changes to the smallest relevant document set.
4. The proposal must state:
   - What should change
   - Why
   - Which source supports it
   - What remains unknown
5. The named owner reviews the proposal.
6. The owner edits the document through a normal branch and pull request.
7. After review, set `status: reviewed` and update `last_reviewed` when appropriate.
8. Regenerate `manifest.generated.json` in the same branch.
9. Run `python scripts/generate_manifest.py check` before merging.

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
- Do not update unrelated documents.
- Keep unknowns and untested behavior visible.
- The manifest is generated; do not edit it manually.
