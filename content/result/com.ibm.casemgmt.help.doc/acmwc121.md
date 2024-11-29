# Select Case Documents widget incoming events

## Clear content event

| Description   | Clear the content in the Select Case Document widget. The original case documents are not displayed and the list of selected case documents is cleared.   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.ClearContent                                                                                                                                          |
| Payload       | null                                                                                                                                                      |

## Clear selected documents event

| Description   | Clear the documents that the user has selected in the Select Case Documents widget.   |
|---------------|---------------------------------------------------------------------------------------|
| Event ID      | icm.ClearSelectedDoc                                                                  |
| Payload       | null                                                                                  |

## Send case information event

| Description   | Display the documents from the original case that the user can add to the new case.                                                                                                                                                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendSplitCaseInfo                                                                                                                                                                                                                                                                                          |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case that is to be created. caseType An icm.model.CaseType object that represents the type of case that is to be created.  coordination An icm.util.Coordination object that is used internally by widgets in the same page for cooperation. |