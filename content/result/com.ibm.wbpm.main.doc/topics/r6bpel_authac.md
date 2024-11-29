<!-- image -->

# Required roles for actions on BPEL process activities

| Action                 | Caller's principal role   | Caller's principal role   | Caller's principal role   | Caller's principal role                     | Caller's principal role   |
|------------------------|---------------------------|---------------------------|---------------------------|---------------------------------------------|---------------------------|
| Action                 | Reader                    | Editor                    | Potential owner           | Owner                                       | Administrator             |
| cancelClaim            |                           |                           |                           | x                                           | x                         |
| claim                  |                           |                           | x                         |                                             | x                         |
| complete               |                           |                           |                           | x                                           | x                         |
| createMessage          | x                         | x                         | x                         | x                                           | x                         |
| createWorkItem         |                           |                           |                           |                                             | x                         |
| deleteWorkItem         |                           |                           |                           |                                             | x                         |
| forceComplete          |                           |                           |                           |                                             | x                         |
| forceRetry             |                           |                           |                           |                                             | x                         |
| getActivityInstance    | x                         | x                         | x                         | x                                           | x                         |
| getAllWorkItems        | x                         | x                         | x                         | x                                           | x                         |
| getClientUISettings    | x                         | x                         | x                         | x                                           | x                         |
| getCustomProperties    | x                         | x                         | x                         | x                                           | x                         |
| getCustomProperty      | x                         | x                         | x                         | x                                           | x                         |
| getCustomPropertyNames | x                         | x                         | x                         | x                                           | x                         |
| getFaultMessage        | x                         | x                         | x                         | x                                           | x                         |
| getFaultNames          | x                         | x                         | x                         | x                                           | x                         |
| getInputMessage        | x                         | x                         | x                         | x                                           | x                         |
| getOutputMessage       | x                         | x                         | x                         | x                                           | x                         |
| getVariable            | x                         | x                         | x                         | x                                           | x                         |
| getVariableNames       | x                         | x                         | x                         | x                                           | x                         |
| getInputVariableNames  | x                         | x                         | x                         | x                                           | x                         |
| getOutputVariableNames | x                         | x                         | x                         | x                                           | x                         |
| getWorkItems           | x                         | x                         | x                         | x                                           | x                         |
| setCustomProperty      |                           | x                         |                           | x                                           | x                         |
| setFaultMessage        |                           | x                         |                           | x                                           | x                         |
| setOutputMessage       |                           | x                         |                           | x                                           | x                         |
| setVariable            |                           |                           |                           |                                             | x                         |
| transferWorkItem       |                           |                           |                           | xTo potential owners or administrators only | x                         |