# Additional restrictions when deleting task work items

Even though a user may be logged on to the client application
with a role that is authorized to delete work items, there may be
additional restrictions on which type of work item is authorized.

The following table shows the assignment reasons on a task instance
that a specific role may delete.

| Caller’s principal role   | Assignment reasons   | Assignment reasons   | Assignment reasons   | Assignment reasons   | Assignment reasons   |
|---------------------------|----------------------|----------------------|----------------------|----------------------|----------------------|
|                           | Administrator        | Editor               | Potential Owner      | Potential Starter    | Reader               |
| Administrator             | Yes                  | Yes                  | Yes                  | Yes                  | No                   |
| Originator                | No                   | Yes                  | Yes                  | Yes                  | No                   |
| TaskSystemAdministrator   | Yes                  | Yes                  | Yes                  | Yes                  | No                   |