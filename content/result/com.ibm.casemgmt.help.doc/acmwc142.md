# To-Do List widget incoming events

## Create Quick Task event

| Description   | Create a quick task and display in the To-Do List widget.                                                                                                                                                                                                                                                                                                                   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.QuickTaskCreate                                                                                                                                                                                                                                                                                                                                                         |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case for which the quick task is to be created. quickTaskName A string that contains the name of the quick task. description A string that contains a description for the quick task. dueDate A string that contains the date that the quick task must be complete. The date is in the format MM/DD/YYYY. |

## Receive work item event

| Description   | Displays the to-do list associated with the case containing the work         item that is contained in the event payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendWorkItem                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Payload       | workItemEditable An icm.model.WorkItemEditable object that represents the work item            to be opened. coordination An icm.util.Coordination object that is used internally by the            widgets in the same page. UIState A Dojo Stateful object that is used internally by the widgets. This            object can contain the following properties: GetNext This property determines whether the next work item is to be opened               automatically. workitemReadonly This property determines whether the work item is to be opened in view mode. GetNextCfg This property determines the configuration of the Open Next Work Item action. |

## Receive case event

| Description   | Displays the to-do list associated with the case that is contained in         the event payload.                                                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendCaseInfo                                                                                                                                                                                                            |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case that is            to be displayed. coordination An icm.util.Coordination object that is used internally by the            widgets in the same page. |

## Select case event

| Description   | Displays the to-do list associated with the case that is                 contained in the event payload.              |
|---------------|-----------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SelectCase                                                                                                        |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case                       that is to be displayed. |

## To-do task added event

| Description   | Adds the to-do task to display in the To-Do List widget.                                           |
|---------------|----------------------------------------------------------------------------------------------------|
| Event ID      | icm.ToDoTaskAdded                                                                                  |
| Payload       | ToDoTaskEditable A TaskEditable object that represents the added to-do                       task. |

## Refresh to-do list event

| Description        | Refreshes the list of to-do tasks in the To-Do List widget.                                                                                                                                                                 |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID           | icm.RefreshToDoTaskList                                                                                                                                                                                                     |
| Payload (optional) | caseEditable An icm.model.CaseEditable object that represents the case that is            to be displayed. coordination An icm.util.Coordination object that is used internally by the            widgets in the same page. |

## Optional payloads

The following
payloads are optional for all To-Do List widget incoming events: