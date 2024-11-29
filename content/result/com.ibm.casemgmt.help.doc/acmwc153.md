# Case Stages widget incoming events

## Complete stage event

| Description   | Complete the current stage.   |
|---------------|-------------------------------|
| Event ID      | icm.CompleteStage             |
| Payload       | null                          |

## Open case event

| Description   | Display the stages for the case that is being opened.                                                                                                                                                                  |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendCaseInfo                                                                                                                                                                                                       |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case for which the stages are to be displayed. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |

## Receive work item event

| Description   | Display the stages for the case that is related to the work item in the event payload.                                                                    |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendWorkItem                                                                                                                                          |
| Payload       | WorkItemEditable An icm.model.WorkItemEditable object that represents the work item that is related to the case for which the stages are to be displayed. |

## Refresh stages event

| Description   | Refresh and redisplay the stages from the current case.   |
|---------------|-----------------------------------------------------------|
| Event ID      | icm.RefreshStage                                          |
| Payload       | Any value                                                 |

## Restart stage event

| Description   | Restart the previous stage.   |
|---------------|-------------------------------|
| Event ID      | icm.RestartStage              |
| Payload       | null                          |

## Select case event

| Description   | Display the stages for the case that is currently selected.                                                      |
|---------------|------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SelectCase                                                                                                   |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case for which the stages are to be displayed. |

## Stage changed event

| Description   | The current stage has been changed.   |
|---------------|---------------------------------------|
| Event ID      | icm.StageChanged                      |
| Payload       | null                                  |

## Toggle the current stage event

| Description   | Place the stage to the on-hold state if the stage is currently working. Place the stage to the working state if the state is currently on hold.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.ToggleOnHoldStage                                                                                                                             |
| Payload       | null                                                                                                                                              |