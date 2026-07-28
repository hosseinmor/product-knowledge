# Repository workflows

## Manifest quality

The `manifest-quality.yml` workflow regenerates and validates `manifest.generated.json` for internal pull requests.

When indexed knowledge changes in an internal pull request, the workflow:

1. installs the manifest generator dependencies;
2. regenerates the manifest;
3. validates metadata, IDs, related IDs, and freshness;
4. commits the generated manifest back to the pull request branch when needed.

Pull requests from forks remain read-only and are validated without an automated push.
