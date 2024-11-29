# Case Toolbar widget incoming events

## Create case event

| Description   | Display the properties for the specified case type so the user can create a case.                                                                                                                                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendNewCaseInfo                                                                                                                                                                                                                                                                                |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case that is to be created. caseType An icm.model.CaseType object that represents the type of case that is to be created.  coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |

## Open case event

| Description   | Open the case that is specified in the event payload.                                                                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.handleSendCaseInfoEvent                                                                                                                                                                        |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case that is to be opened. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |

## Split case event

| Description   | Display the information for the original case that is being split to create a new case.                                                                                                           |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendSplitCaseInfo                                                                                                                                                                             |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case that is to be split. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |