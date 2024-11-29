# Additional restrictions when transferring task work items

Even though a user may be logged on to the client application
with a role that is authorized to transfer work items, there may be
additional restrictions on which type of work item may be transferred
and to whom.

The following table shows who can transfer roles from one user
to another.

| Caller’s principal role   | Assignment reasons from   | Assignment reasons from   | Assignment reasons from                  | Assignment reasons from       | Assignment reasons from   | Assignment reasons from   | Assignment reasons from         |
|---------------------------|---------------------------|---------------------------|------------------------------------------|-------------------------------|---------------------------|---------------------------|---------------------------------|
|                           | Administrator             | Editor                    | Owner                                    | Potential Owner               | Potential Starter         | Reader                    | Starter                         |
| Administrator             | anybody                   | anybody                   | anybody                                  | anybody                       | anybody                   | anybody                   | anybody                         |
| Originator                | No                        | anybody                   | Potential Instance Creator Administrator | anybody                       | No                        | anybody                   | No                              |
| Owner                     | No                        | No                        | No                                       | Potential Owner Administrator | No                        | No                        | No                              |
| Starter                   | No                        | No                        | No                                       | No                            | No                        | No                        | Potential Starter Administrator |
| TaskSystemAdministrator   | anybody                   | anybody                   | No                                       | anybody                       | anybody                   | anybody                   | anybody                         |

For example, the table is read as:

- The task owner can transfer his ownership to a user who is already
a potential owner of the task or a task administrator.
- The task administrator can transfer the ownership from the present
owner to anybody.