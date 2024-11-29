# Chart widget incoming events

## Clear content event

| Description   | Clear the content in the Chart widget.   |
|---------------|------------------------------------------|
| Event ID      | icm.ClearContent                         |
| Payload       | null                                     |

## Open work item event

| Description   | Display task-related data from the payload in the chart that is configured for the Chart widget.                                                                                                                                         |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendWorkItem                                                                                                                                                                                                                         |
| Payload       | workItemEditable An icm.model.WorkItemEditable object that represents the work item for which case information is to be displayed. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |

## Send case information event

| Description   | Display case-related data from the payload in the chart that is configured for the Chart widget.                                                                                                      |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendCaseInfo                                                                                                                                                                                      |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case that is to be displayed. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |