---
id: design-system.experience-rule.action-hierarchy
collection: design-system
type: experience-rule
title: Action Hierarchy
summary: Every action group should have one clear visual leader.
knowledge_state: unverified
document_maturity: draft
related: []
---

# Action Hierarchy

## Principle

Every action group should have one clear visual leader.

Only one action in a group may use the strongest visual presence:

- Accent
- Primary
- Danger Filled

All other actions must be at least one level lower.

## Recommended Combinations

| Situation | Combination |
|---|---|
| Accent CTA with exit or supporting information | Accent + Ghost |
| Accent CTA with an independent alternative | Accent + Tertiary |
| Operational action with Cancel | Primary + Ghost |
| Operational action with a valid alternative | Primary + Tertiary |
| Two important paths with clear hierarchy | Primary + Secondary |
| Final destructive confirmation with Cancel | Danger Filled + Ghost |

## Limited Combinations

Accent + Secondary and Primary + Secondary are allowed, but require caution because two filled Buttons may compete visually.

Accent and Primary must not appear as equal competing actions in the same group.

## Three Actions

Keep an action group to two Buttons whenever possible.

When three actions are necessary:

- Main action → Accent, Primary, or Danger Filled
- Supporting action → Tertiary or Secondary
- Exit or third action → Ghost, visually separated from the first two

Example:

```text
[Submit request] [Save draft]                    Cancel
```

## Context Convention

In dense tool-oriented interfaces such as ATS, Tertiary is commonly used for independent neutral actions.

In editorial and consumer interfaces, Secondary is more common for medium-emphasis standalone actions.

The nature of the control still takes priority:

- Dropdown, filter, toolbar → Tertiary
- Medium-emphasis standalone action → Secondary
- Exit or low-emphasis action → Ghost

## Scope

This document owns hierarchy across action groups.

Preset meaning and token mapping remain in `../components/button.md`.

Placement inside specific patterns belongs in:

- `../patterns/multi-step-flow.md`
- `../patterns/confirmation.md`
- `../patterns/destructive-actions.md`
