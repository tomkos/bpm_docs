# Case Information widget incoming events

## Clear content event

| Description   | Clear the content in the Case Information widget.   |
|---------------|-----------------------------------------------------|
| Event ID      | icm.ClearContent                                    |
| Payload       | null                                                |

## Filter History event

| Description   | Filter the entries on the History tab based on the criteria that is specified in the event payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.FilterHistory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Payload       | show A string that contains the label for the filter that determines how much information is displayed in the History tab. By default, the values are Summary and All. showValue A string that contains the value for the filter that determines how much information is displayed in the History tab. The valid values areSummary and All. forEntry A string that contains the label for the filter that determines the category of items to be displayed in the History tab. The valid values are All, Case, Comments, Documents, Activities, and Folders. forValue A string that contains the filter that determines the category of items to be displayed in the History tab. The valid values are All, Case, Comments, Documents, Activities, and Folders. |

## Receive new task event

| Description   | Display the case information for the case that is related to the activity in the event payload.                                                                                                       |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendNewTaskInfo                                                                                                                                                                                   |
| Payload       | taskEditable An icm.model.TaskEditable object that represents the activity that is to be added. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |

## Receive work item event

| Description   | Display the case information for the case that is related to the work item in the event payload.                                   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendWorkItem                                                                                                                   |
| Payload       | workItemEditable An icm.model.WorkItemEditable object that represents the work item for which case information is to be displayed. |

## Refresh event

| Description   | Refresh the tab that is specified in the event payload.                                                                                         |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.RefreshTab                                                                                                                                  |
| Payload       | tabId A string containing the identifier of the tab that is to be refreshed. The valid values are: Documents, History, Summary, and Activities. |

## Select Case event

| Description   | Display the case information for the case that is contained in the event payload.               |
|---------------|-------------------------------------------------------------------------------------------------|
| Event ID      | icm.SelectCase                                                                                  |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case that is to be displayed. |

## Select folder event

| Description   | Open the case subfolder that is specified in the event payload.         |
|---------------|-------------------------------------------------------------------------|
| Event ID      | icm.SelectInitialFolder                                                 |
| Payload       | folderPath A string containing the path to the selected case subfolder. |

## Select tab event

| Description   | Open the tab that is specified in the event payload.                                                                                         |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SelectTab                                                                                                                                |
| Payload       | tabId A string containing the identifier of the tab that is to be opened. The valid values are: Documents, History, Summary, and Activities. |

## Send Case Information event

| Description   | Display the case that is specified in the event payload.                                                                                                                                              |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendCaseInfo                                                                                                                                                                                      |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case that is to be displayed. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |