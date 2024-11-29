# Additional restrictions when transferring escalation work items

Even though a user may be logged on to the client application
with a role that is authorized to transfer work items, there may be
additional restrictions on which type of work item may be transferred
and to whom.

The following table shows who can transfer roles from one user
to another.

| Property name          | Caller's principal role   | Caller's principal role   | Caller's principal role   | Caller's principal role   | Caller's principal role   |
|------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
|                        | Administrator             | Escalation Receiver       | Reader                    | TaskSystemAdministrator   | TaskSystemMonitor         |
| durationUntilRepeated  | Yes                       | No                        | No                        | Yes                       | No                        |
| durationUntilEscalated | Yes                       | No                        | No                        | Yes                       | No                        |
| escalationTime         | Yes                       | No                        | No                        | Yes                       | No                        |
| name                   | Yes                       | No                        | No                        | Yes                       | No                        |