# Case List widget outgoing events

## Open case event

| Description   | The user selected a case that is to be opened in the Case Details page.                                                                                                                              |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.OpenCase                                                                                                                                                                                         |
| Type          | Broadcast                                                                                                                                                                                            |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case that the user selected. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |

## Select case event

| Description   | The user selected a case in the list or no case is selected in the list. If one or more cases are selected, the event is broadcast for the first case selected by the user.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SelectCase                                                                                                                                                                |
| Type          | Broadcast                                                                                                                                                                     |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the first case that the user selected.  The payload is null if no case is selected.                             |