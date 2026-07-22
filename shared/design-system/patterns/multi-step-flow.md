# Multi-Step Flow

## Intermediate Steps

Default combination:

- Forward action → Primary
- Back action → Ghost

Example:

```text
[Continue]  Back
```

Do not use Accent for every forward action. Use Accent only at the step where an approved product conversion actually occurs.

## Final Step

The final Button label must describe the result rather than repeat “Continue.”

Examples:

- Submit request
- Create job
- Send for approval
- Pay
- Submit resume

Preset selection:

- Operational result → Primary
- Defined product conversion → Accent
- Destructive result → Danger Filled

## Back, Cancel, Close, and Exit

| Action | Meaning |
|---|---|
| Back | Move to the previous step without leaving the flow |
| Cancel | Cancel the current operation |
| Close | Close the current surface |
| Exit | Leave the entire flow |

When Close or Exit causes data loss, show a confirmation. Button styling alone is not sufficient to communicate the risk.

## RTL Placement

- Place the forward or main action on the right side of the action group.
- Place Back, Cancel, or an alternative after it, toward the left.
- A third or exit action may be separated from the main group.

## Mobile

- The main action may become full width.
- Place the secondary action below it.
- Preserve visual hierarchy after stacking.

## Submission State

When the current step is submitting:

- The triggered Button enters Loading.
- Repeated submission is blocked.
- Back and competing actions are disabled until the request completes.

## Related Documents

- `../components/button.md`
- `../experience-rules/action-hierarchy.md`
- `confirmation.md`
