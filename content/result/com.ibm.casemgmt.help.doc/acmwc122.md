# Viewer widget incoming events

## Clear content event

| Description   | Clear the content of Viewer widget and the cached identifiers, and then close all tabs.   |
|---------------|-------------------------------------------------------------------------------------------|
| Event ID      | icm.ClearContent                                                                          |
| Payload       | null                                                                                      |

## Open document event

| Description   | Open the document that is contained in the event payload in the Viewer widget.                                                                                                                                                                                                                                                                                                          |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.OpenDocument                                                                                                                                                                                                                                                                                                                                                                        |
| Payload       | contentItem An ecm.model.ContentItem that represents the document that is to be opened. action A string that identifies the action that the Viewer widget is to execute as Open or Preview. If the Viewer widget executes the Open action, the document is opened for editing. If the Viewer widget executes the Preview action, the document is converted to HTML and is not editable. |

## Receive work item event

| Description   | Save the work item ID in the cache and close the currently viewed attachments to prepare for opening the attachments for another work item.                                                                                |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendWorkItem                                                                                                                                                                                                           |
| Payload       | workitemEditable An icm.model.WorkItemEditable object that represents the work item for which the ID is to be saved. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |

## Select case event

| Description   | Save the case ID in the cache and close the currently viewed document to prepare for opening another case.   |
|---------------|--------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SelectCase                                                                                               |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case for which the ID is to be saved.      |

## Send case information event

| Description   | Save the case ID in the cache and close currently viewed documents to prepare for opening documents from another case.                                                                                        |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendCaseInfo                                                                                                                                                                                              |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case for which the ID is to be saved. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |