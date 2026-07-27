# Product Knowledge Update

## Goal

Keep Product Knowledge useful without introducing a separate release-handoff system.

## Process

1. AI or a team member identifies missing, outdated, contradictory, or newly decided knowledge.
2. AI proposes exact changes to one or more Product Overview, Product Area, or Shared Product Concept documents.
3. The proposal must state:
   - What should change
   - Why
   - Which source supports it
   - What remains unknown
4. The named owner reviews the proposal.
5. The owner edits the document through a normal branch and pull request.
6. After review, set the document status to `Reviewed` and update `Last reviewed` when appropriate.

## Rules

- Do not write assumptions as confirmed behavior.
- Do not update unrelated documents.
- Keep unknowns and untested behavior visible.
- Product-specific behavior stays in the Product Area.
- Genuinely shared definitions and rules belong in Shared Product Concepts.
- Reusable UI behavior belongs in the Design System.
