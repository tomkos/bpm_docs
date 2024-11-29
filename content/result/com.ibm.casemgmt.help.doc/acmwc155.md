# Task Toolbar widget incoming events

## Receive work item event

| Description   | Display the work item that is contained in the event payload.                                                                                                                                                                        |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendWorkItem                                                                                                                                                                                                                     |
| Payload       | WorkItemEditable An icm.model.WorkItemEditable object that represents the work item to be opened. Action An attribute that is used internally by the widget. It can contain the following values: viewInstance viewAudit viewDiagram |