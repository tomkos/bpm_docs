# Case Stages widget

| Action      | Description                                                                                                                                                                                                           |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Complete    | Completes the active current stage. The case automatically moves to the next stage. If there is no next stage, all stages are marked as complete. The Complete action cannot be used if the current stage is on hold. |
| Restart     | Restarts the case stage that is previous to the active current stage. If all case stages are complete, the Restart action restarts the last stage. This action cannot be used if the current stage is on hold.        |
| Toggle Hold | Places the active current stage on hold. If the current stage is already on hold, this action returns the stage to the active state.                                                                                  |

- Case Stages widget events

The Case Stages widget handles events to display the current state of the stages for a case.