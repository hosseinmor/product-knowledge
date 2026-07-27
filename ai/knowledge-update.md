# Product Knowledge Update

## Purpose

Let AI suggest focused documentation improvements while keeping review and editing under a human owner.

## When to suggest an update

- research reveals missing current context;
- PRD work exposes an undocumented rule, permission, state, or flow;
- design work reveals a gap or contradiction;
- a reviewed walkthrough finds missing or outdated behavior;
- a Product Area has become difficult to understand.

## AI proposal

The proposal should identify:

```text
Document to update
Sections to add or change
Current statement when relevant
Suggested statement
Reason
Source or evidence
Unknowns that must remain visible
Recommended owner or reviewer
```

## Owner workflow

1. Review the AI suggestion.
2. Confirm whether the information describes current agreed behavior.
3. Reject, revise, or accept each proposed change.
4. Edit the document manually on a dedicated branch.
5. Ask one relevant PM, designer, or domain owner to review material behavior changes.
6. Merge the documentation change.

## Document status

Use only when useful:

```text
Draft
Reviewed
```

Do not add a complex lifecycle to every document.

## Rules

- AI does not update Product Knowledge automatically.
- Proposed or undecided behavior must not be written as current truth.
- Keep one clear owner for each Product Area or shared concept.
- Prefer editing an existing document over creating a new document type.
- Split a Product Area only when the single document has become hard to use.
