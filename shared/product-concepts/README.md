# Shared Product Concepts

Use this directory for a business concept whose definition, data, lifecycle, or core rules are genuinely shared across products.

Examples may include:

```text
Job Post
Organization
User Account
```

A shared Product Concept does not own product-specific behavior.

Example:

```text
job-post.md
→ shared definition, shared data, lifecycle, and cross-product rules

products/employer/areas/job-post-management.md
→ employer-side behavior

products/jobseeker/areas/job-post-experience.md
→ jobseeker-side behavior
```

Do not create a shared concept merely because two products use the same word. The meaning and ownership must actually be shared.

Use `templates/shared-product-concept.md`.
