# Authorized roles for actions on task templates

Access to the HumanTaskManager interface does not guarantee
that the caller can perform all of the actions on a task template.
The caller must be logged on to the client application with a role
that is authorized to perform the action.

The following table shows the actions on a task template that a
specific role can take.

| Action                      | Caller's Principal Role   | Caller's Principal Role    | Caller's Principal Role   | Caller's Principal Role   | Caller's Principal Role   |
|-----------------------------|---------------------------|----------------------------|---------------------------|---------------------------|---------------------------|
|                             | Administrator             | Potential Instance Creator | Reader                    | TaskSystemAdministrator   | TaskSystemMonitor         |
| COMPLETEWITHNEWFOLLOWONTASK | Yes                       | Yes                        | No                        | Yes                       | No                        |
| CREATEANDCALLTASK           | Yes                       | Yes                        | No                        | Yes                       | No                        |
| CREATEANDSTARTTASK          | Yes                       | Yes                        | No                        | Yes                       | No                        |
| CREATEANDSTARTTASKASSUBTASK | Yes                       | Yes                        | No                        | Yes                       | No                        |
| CREATEFAULTMESSAGE          | EVERYBODY 1               | EVERYBODY 1                | EVERYBODY 1               | EVERYBODY 1               | EVERYBODY 1               |
| CREATEINPUTMESSAGE          | EVERYBODY 1               | EVERYBODY 1                | EVERYBODY 1               | EVERYBODY 1               | EVERYBODY 1               |
| CREATEOUTPUTMESSAGE         | EVERYBODY 1               | EVERYBODY 1                | EVERYBODY 1               | EVERYBODY 1               | EVERYBODY 1               |
| CREATETASK                  | Yes                       | Yes                        | No                        | Yes                       | No                        |
| DELETETEMPLATE              | Yes                       | No                         | No                        | Yes                       | No                        |
| GETCUSTOMPROPERTY           | Yes                       | Yes                        | Yes                       | Yes                       | Yes                       |
| GETDOCUMENTATION            | Yes                       | Yes                        | Yes                       | Yes                       | Yes                       |
| GETFAULTNAMES               | Yes                       | Yes                        | Yes                       | Yes                       | Yes                       |
| GETROLEINFO                 | Yes                       | Yes                        | Yes                       | Yes                       | Yes                       |
| GETTEMPLATE                 | Yes                       | Yes                        | Yes                       | Yes                       | Yes                       |
| GETUISETTINGS               | Yes                       | Yes                        | Yes                       | Yes                       | Yes                       |
| STARTTEMPLATE               | Yes                       | No                         | No                        | Yes                       | No                        |
| STOPTEMPLATE                | Yes                       | No                         | No                        | Yes                       | No                        |