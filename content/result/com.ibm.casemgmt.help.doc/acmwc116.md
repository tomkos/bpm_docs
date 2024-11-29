# Process History widget incoming events

## Clear Content event

| Description   | Clear the content from the Process History widget.   |
|---------------|------------------------------------------------------|
| Event ID      | icm.ClearContent                                     |
| Payload       | null                                                 |

## Open work item event

| Description   | Display the process history for the work item that is contained in the event payload.                             |
|---------------|-------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendWorkItem                                                                                                  |
| Payload       | workItem An icm.model.WorkItem object that represents the work item for which process history is to be displayed. |

## Receive task information event

| Description   | Display the process history for the task that is contained in the event payload.                                                              |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.TaskSelect                                                                                                                                |
| Payload       | task An icm.model.Task object that represents the task for which process history is to be displayed.  Alternatively, the payload can be null. |