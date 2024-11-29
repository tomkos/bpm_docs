# Case Information widget outgoing events

## Document opened event

| Description   | The user opened a document                                                                                                                                                                                       |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.OpenDocument                                                                                                                                                                                                 |
| Type          | BroadcastNote: This event is only broadcast when there is a Viewer widget on the page and when the Open documents in a separate browser window setting on the widget is disabled.                                |
| Payload       | contentItem An ecm.model.ContentItem that represents the document that was opened. action A string that indicates whether the document was opened for viewing or for editing. The valid values are view or edit. |

## Document selected event

| Description   | The user selected a document.                                                        |
|---------------|--------------------------------------------------------------------------------------|
| Event ID      | icm.SelectDocument                                                                   |
| Type          | Wired                                                                                |
| Payload       | contentItem An ecm.model.ContentItem that represents the document that was selected. |

## Folder opened event

| Description   | The user opened a folder                                                         |
|---------------|----------------------------------------------------------------------------------|
| Event ID      | icm.OpenFolder                                                                   |
| Type          | Wired                                                                            |
| Payload       | contentItem An ecm.model.ContentItem that represents the folder that was opened. |

## Folder selected event

| Description   | The user selected a folder.                                                        |
|---------------|------------------------------------------------------------------------------------|
| Event ID      | icm.SelectFolder                                                                   |
| Type          | Wired                                                                              |
| Payload       | contentItem An ecm.model.ContentItem that represents the folder that was selected. |

## Task selected event

| Description   | The user selected an activity from the Activities view. If the Case Information widget is wired to the Process History widget, the event payload includes the milestones for the selected activity.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.TaskSelect                                                                                                                                                                                        |
| Type          | Wired                                                                                                                                                                                                 |
| Payload       | task An icm.model.Task object that represents the activity that the user selected.                                                                                                                    |

## Send case history event

| Description   | The user selected a history item from the History view.                                                                                                                                                                                                                                                                                                      |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendCaseHistory                                                                                                                                                                                                                                                                                                                                          |
| Type          | Wired                                                                                                                                                                                                                                                                                                                                                        |
| Payload       | caseHistory An object that represents the item the user selected in the History view. contentItem For a document history item only: An ecm.model.ContentItem that represents the document that was selected. action For a document history item only: A string containing the value open to indicate that the document is to be opened in the Viewer widget. |

## Activity status updated event

| Description   | The activity status is updated.                                                                                                                                                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.TaskStatusUpdated                                                                                                                                                                                                                                      |
| Type          | Wired                                                                                                                                                                                                                                                      |
| Payload       | action A string that indicates the action that the user performed on the activity. For example, the action might be start, disable, enable, or so on. taskObj An icm.model.Task object that represents the activity on which the user performed an action. |