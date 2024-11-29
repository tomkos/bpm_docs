# Timeline Visualizer widget incoming events

## Clear content event

| Description   | Clear the content of the Timeline Visualizer widget.   |
|---------------|--------------------------------------------------------|
| Event ID      | icm.ClearContent                                       |
| Payload       | null                                                   |

## Open work item event

| Description   | Display the extended history                                                   in the Timeline Visualizer for the case that is                                                   contained in the event payload.  This event is                                                   used when the Timeline Visualizer widget is                                                   included on a Work Details                                                   page.                                  |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendWorkItem                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Payload       | workItemEditable An icm.model.WorkItemEditable                                                    object that represents the work item                                                   for which the case history is to be                                                   displayed. coordination An icm.util.Coordination                                                   object that is used internally by the widgets in                                                   the same page. |

## Select case event

| Description   | Display the extended history in the Timeline Visualizer for the case that is         contained in the event payload. This event is used when the Timeline Visualizer widget is         included on a Case Details page.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SelectCase                                                                                                                                                                                                            |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case for which the extended history is to be displayed.                                                                                                 |

## Send case information event

| Description   | Display the extended history in the Timeline Visualizer for the case that is contained in the event payload. This event is used when the Timeline Visualizer widget is included on a Case Details page.                                    |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendCaseInfo                                                                                                                                                                                                                           |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case for which the extended history is to be displayed. coordination An icm.util.Coordination object that is used internally by the widgets in the            same page. |