<!-- image -->

# Required roles for actions on BPEL process instances

| Action                    | Caller's principal role   | Caller's principal role   | Caller's principal role   |
|---------------------------|---------------------------|---------------------------|---------------------------|
| Action                    | Reader                    | Starter                   | Administrator             |
| createMessage             | x                         | x                         | x                         |
| createWorkItem            |                           |                           | x                         |
| delete                    |                           |                           | x                         |
| deleteWorkItem            |                           |                           | x                         |
| forceTerminate            |                           |                           | x                         |
| getActiveEventHandlers    | x                         |                           | x                         |
| getActivityInstance       | x                         |                           | x                         |
| getAllActivities          | x                         |                           | x                         |
| getAllWorkItems           | x                         |                           | x                         |
| getClientUISettings       | x                         | x                         | x                         |
| getCustomProperties       | x                         | x                         | x                         |
| getCustomProperty         | x                         | x                         | x                         |
| getCustomPropertyNames    | x                         | x                         | x                         |
| getFaultMessage           | x                         | x                         | x                         |
| getInputClientUISettings  | x                         | x                         | x                         |
| getInputMessage           | x                         | x                         | x                         |
| getOutputClientUISettings | x                         | x                         | x                         |
| getOutputMessage          | x                         | x                         | x                         |
| getProcessInstance        | x                         | x                         | x                         |
| getVariable               | x                         | x                         | x                         |
| getWaitingActivities      | x                         | x                         | x                         |
| getWorkItems              | x                         |                           | x                         |
| restart                   |                           |                           | x                         |
| resume                    |                           |                           | x                         |
| setCustomProperty         |                           | x                         | x                         |
| setVariable               |                           |                           | x                         |
| suspend                   |                           |                           | x                         |
| transferWorkItem          |                           |                           | x                         |