# Repository workflows

## Manifest quality

The `manifest-quality.yml` workflow regenerates and validates `manifest.generated.json` for internal pull requests.

When indexed knowledge changes in an internal pull request, the workflow:

1. installs the manifest generator dependencies;
2. regenerates the manifest;
3. validates metadata, IDs, related IDs, and freshness;
4. commits the generated manifest back to the pull request branch when needed.

Pull requests from forks remain read-only and are validated without an automated push.

## Accessibility knowledge quality

The `accessibility-quality.yml` workflow validates deterministic structural invariants for the canonical accessibility corpus and its production retrieval integration.

It runs when accessibility docs, Design System governance/components/patterns, accessibility routing, or the accessibility gate itself change. The workflow verifies canonical corpus identity/maturity/ownership, required WCAG ownership markers, and explicit routing from `ai/design-start.md`.

This workflow does not replace the manual component, flow, keyboard, screen-reader, standards, or complete-process regression gate defined in `shared/design-system/accessibility/testing.md`.
