# Attachments widget incoming events

## Add document attachment

| Description   | Add the document that is contained in the event payload to the attachment that is specified in the event payload.                                                                                                                               |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.AddAttachment                                                                                                                                                                                                                               |
| Payload       | attachmentName A string that contains the identifier of the attachment to which the document is to be added. documents One or more ecm.model.ContentItem objects that represent the documents that are to be added to the specified attachment. |

## Clear content event

| Description   | Clear the content in the Case List widget.   |
|---------------|----------------------------------------------|
| Event ID      | icm.ClearContent                             |
| Payload       | null                                         |

## Receive work item

| Description   | Display the attachments for the work item that is specified in the event payload.                                                                                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendWorkItem                                                                                                                                                                                                     |
| Payload       | workitem An icm.model.WorkItem object that represents the work item for which attachments are to be displayed. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |

## Receive new task event

| Description   | Display the attachment that is associated with the task in the event payload.                                                                                                                         |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendNewTaskInfo                                                                                                                                                                                   |
| Payload       | taskEditable An icm.model.TaskEditable object that represents the task that is to be displayed. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |