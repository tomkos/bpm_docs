# Authorized roles for actions on escalation templates

Access to the HumanTaskManager interface does not guarantee
that the caller can perform all of the actions on an escalation template.
The caller must be logged on to the client application with a role
that is authorized to perform the action.

| Action                | Caller's principal role   | Caller's principal role    | Caller's principal role   | Caller's principal role   | Caller's principal role   |
|-----------------------|---------------------------|----------------------------|---------------------------|---------------------------|---------------------------|
|                       | Administrator             | Potential Instance Creator | Reader                    | TaskSystemAdministrator   | TaskSystemMonitor         |
| GETCUSTOMPROPERTY     | Yes                       | Yes                        | Yes                       | Yes                       | No                        |
| GETDOCUMENTATION      | Yes                       | Yes                        | Yes                       | Yes                       | No                        |
| GETESCALATIONTEMPLATE | Yes                       | Yes                        | Yes                       | Yes                       | Yes                       |
| GETROLEINFO           | Yes                       | Yes                        | Yes                       | Yes                       | Yes                       |
| GETTASKTEMPLATE       | Yes                       | Yes                        | Yes                       | Yes                       | Yes                       |