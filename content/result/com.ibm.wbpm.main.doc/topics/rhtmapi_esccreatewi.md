# Additional restrictions when creating escalation work items

Even though a user may be logged on to the client application
with a role that is authorized to create work items, there may be
additional restrictions on which type of work item is authorized.

| Caller’s principal role   | Assignment reasons   | Assignment reasons   | Assignment reasons   |
|---------------------------|----------------------|----------------------|----------------------|
|                           | Administrator        | Escalation Receiver  | Reader               |
| Administrator             | Yes                  | Yes                  | Yes                  |
| TaskSystemAdministrator   | Yes                  | Yes                  | Yes                  |