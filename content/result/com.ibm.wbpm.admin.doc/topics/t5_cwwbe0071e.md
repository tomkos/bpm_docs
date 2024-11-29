<!-- image -->

# Standard fault exception "missingReply" (message: CWWBE0071E)

## Reason

- The reply activity is skipped.
- A fault occurs and corresponding fault handler does not contain a reply
activity.
- A fault occurs and there is no corresponding fault handler.

## Resolution

Correct the model to ensure that a reply
activity is always performed before the process ends.