# Authorized roles for actions on escalation instances

Access to the HumanTaskManager interface does not guarantee
that the caller can perform all of the actions on an escalation. The
caller must be logged on to the client application with a role that
is authorized to perform the action.

The following table shows the actions on an escalation instance
that a specific role can take.

| Action                | Caller's principal role   | Caller's principal role   | Caller's principal role   | Caller's principal role   | Caller's principal role   |
|-----------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
|                       | Administrator             | Escalation Receiver       | Reader                    | TaskSystemAdministrator   | TaskSystemMonitor         |
| CREATEWORKITEM        | Yes                       | No                        | No                        | Yes                       | No                        |
| DELETEWORKITEM        | Yes                       | No                        | No                        | Yes                       | No                        |
| GETCUSTOMPROPERTY     | Yes                       | Yes                       | Yes                       | Yes                       | Yes                       |
| GETDOCUMENTATION      | Yes                       | Yes                       | Yes                       | Yes                       | Yes                       |
| GETESCALATION         | Yes                       | Yes                       | Yes                       | Yes                       | Yes                       |
| GETESCALATIONTEMPLATE | Yes                       | Yes                       | Yes                       | Yes                       | Yes                       |
| GETROLEINFO           | Yes                       | Yes                       | Yes                       | Yes                       | Yes                       |
| SETCUSTOMPROPERTY     | Yes                       | Yes                       | No                        | Yes                       | No                        |
| TRANSFERWORKITEM      | Yes                       | No                        | No                        | Yes                       | No                        |
| TRIGGERESCALATION     | Yes                       | No                        | No                        | Yes                       | No                        |
| UPDATE                | Yes                       | No                        | No                        | Yes                       | No                        |