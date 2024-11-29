<!-- image -->

# Business state machine events

| Event Name                                   | Event Nature                   | Event Contents                 | Type                           |
|----------------------------------------------|--------------------------------|--------------------------------|--------------------------------|
| StateMachineDefinition element               | StateMachineDefinition element | StateMachineDefinition element | StateMachineDefinition element |
| bsm:WBI.BSM.StateMachineDefinition.ALLOCATED | ALLOCATED                      | instanceID                     | string                         |
| bsm:WBI.BSM.StateMachineDefinition.RELEASED  | RELEASED                       | instanceID                     | string                         |
| Transition element                           | Transition element             | Transition element             | Transition element             |
| bsm:WBI.BSM.Transition.ENTRY                 | ENTRY                          | instanceID                     | string                         |
| bsm:WBI.BSM.Transition.ENTRY                 | ENTRY                          | name                           | string                         |
| bsm:WBI.BSM.Transition.EXIT                  | EXIT                           | instanceID                     | string                         |
| bsm:WBI.BSM.Transition.EXIT                  | EXIT                           | name                           | string                         |
| bsm:WBI.BSM.Transition.FAILURE               | FAILURE                        | ErrorReport                    | Exception                      |
| bsm:WBI.BSM.Transition.FAILURE               | FAILURE                        | instanceID                     | string                         |
| bsm:WBI.BSM.Transition.FAILURE               | FAILURE                        | name                           | string                         |
| State element                                | State element                  | State element                  | State element                  |
| bsm:WBI.BSM.State.ENTRY                      | ENTRY                          | instanceID                     | string                         |
| bsm:WBI.BSM.State.ENTRY                      | ENTRY                          | name                           | string                         |
| bsm:WBI.BSM.State.EXIT                       | EXIT                           | instanceID                     | string                         |
| bsm:WBI.BSM.State.EXIT                       | EXIT                           | name                           | string                         |
| bsm:WBI.BSM.State.FAILURE                    | FAILURE                        | ErrorReport                    | Exception                      |
| bsm:WBI.BSM.State.FAILURE                    | FAILURE                        | instanceID                     | string                         |
| bsm:WBI.BSM.State.FAILURE                    | FAILURE                        | name                           | string                         |
| Guard element                                | Guard element                  | Guard element                  | Guard element                  |
| bsm:WBI.BSM.Guard.ENTRY                      | ENTRY                          | instanceID                     | string                         |
| bsm:WBI.BSM.Guard.ENTRY                      | ENTRY                          | name                           | string                         |
| bsm:WBI.BSM.Guard.EXIT                       | EXIT                           | instanceID                     | string                         |
| bsm:WBI.BSM.Guard.EXIT                       | EXIT                           | name                           | string                         |
| bsm:WBI.BSM.Guard.EXIT                       | EXIT                           | result                         | boolean                        |
| bsm:WBI.BSM.Guard.FAILURE                    | FAILURE                        | ErrorReport                    | Exception                      |
| bsm:WBI.BSM.Guard.FAILURE                    | FAILURE                        | instanceID                     | string                         |
| bsm:WBI.BSM.Guard.FAILURE                    | FAILURE                        | name                           | string                         |
| Action element                               | Action element                 | Action element                 | Action element                 |
| bsm:WBI.BSM.Action.ENTRY                     | ENTRY                          | instanceID                     | string                         |
| bsm:WBI.BSM.Action.ENTRY                     | ENTRY                          | name                           | string                         |
| bsm:WBI.BSM.Action.EXIT                      | EXIT                           | instanceID                     | string                         |
| bsm:WBI.BSM.Action.EXIT                      | EXIT                           | name                           | string                         |
| bsm:WBI.BSM.Action.FAILURE                   | FAILURE                        | ErrorReport                    | Exception                      |
| bsm:WBI.BSM.Action.FAILURE                   | FAILURE                        | instanceID                     | string                         |
| bsm:WBI.BSM.Action.FAILURE                   | FAILURE                        | name                           | string                         |
| EntryAction element                          | EntryAction element            | EntryAction element            | EntryAction element            |
| bsm:WBI.BSM.EntryAction.ENTRY                | ENTRY                          | instanceID                     | string                         |
| bsm:WBI.BSM.EntryAction.ENTRY                | ENTRY                          | name                           | string                         |
| bsm:WBI.BSM.EntryAction.EXIT                 | EXIT                           | instanceID                     | string                         |
| bsm:WBI.BSM.EntryAction.EXIT                 | EXIT                           | name                           | string                         |
| bsm:WBI.BSM.EntryAction.FAILURE              | FAILURE                        | ErrorReport                    | Exception                      |
| bsm:WBI.BSM.EntryAction.FAILURE              | FAILURE                        | instanceID                     | string                         |
| bsm:WBI.BSM.EntryAction.FAILURE              | FAILURE                        | name                           | string                         |
| ExitAction element                           | ExitAction element             | ExitAction element             | ExitAction element             |
| bsm:WBI.BSM.ExitAction.ENTRY                 | ENTRY                          | instanceID                     | string                         |
| bsm:WBI.BSM.ExitAction.ENTRY                 | ENTRY                          | name                           | string                         |
| bsm:WBI.BSM.ExitAction.EXIT                  | EXIT                           | instanceID                     | string                         |
| bsm:WBI.BSM.ExitAction.EXIT                  | EXIT                           | name                           | string                         |
| bsm:WBI.BSM.ExitAction.FAILURE               | FAILURE                        | ErrorReport                    | Exception                      |
| bsm:WBI.BSM.ExitAction.FAILURE               | FAILURE                        | instanceID                     | string                         |
| bsm:WBI.BSM.ExitAction.FAILURE               | FAILURE                        | name                           | string                         |
| Timer element                                | Timer element                  | Timer element                  | Timer element                  |
| bsm:WBI.BSM.Timer.START                      | START                          | instanceID                     | string                         |
| bsm:WBI.BSM.Timer.START                      | START                          | name                           | string                         |
| bsm:WBI.BSM.Timer.START                      | START                          | duration                       | string                         |
| bsm:WBI.BSM.Timer.STOPPED                    | STOPPED                        | instanceID                     | string                         |
| bsm:WBI.BSM.Timer.STOPPED                    | STOPPED                        | name                           | string                         |
| bsm:WBI.BSM.Timer.STOPPED                    | STOPPED                        | duration                       | string                         |