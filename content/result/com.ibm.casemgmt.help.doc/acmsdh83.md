# Creating and configuring stages for a case type

## Procedure

To create and configure case stages:

1. After you create a case type, open the Stages page and click
Add Stage.
2. Enter a name, a unique identifier, and, optionally, a duration for the stage.
3. Repeat steps 1 and 2 for each case stage that you add to the case type.
The sequence in which the case stages occur is determined by the order in which the stages are
listed on the Stages page. That is, the first stage in the list is the first
stage to start. When that stage completes, the second stage in the list starts. To change the
sequence in which a case stage occurs, click the Move Up or Move
Down arrow to move that stage. Alternatively, you can drag the stage in the new
position.
4. To display case stage information in Case Client, add the Case
Stages widget to the Case Details page.
For more information about this widget, see Case Stages widget.
5 Configure the ways in which state of the case stage is changed at run time. You can change the case stage state in the following ways:
    - Add the following actions to a menu or toolbar in Case List widget or Case Toolbar widget:
        - Complete Stage
        - Restart Stage
        - Toggle Stage
- Add stage steps to System lane of the workflow for a task.
- Implement the following case operations:
    - completeCurrentCaseStage
    - placeCurrentCaseStageOnHold
    - releaseCurrentOnHoldCaseStage
    - restartPreviousCaseStage