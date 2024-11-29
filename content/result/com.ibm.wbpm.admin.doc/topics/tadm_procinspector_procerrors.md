# Troubleshooting errors and failures in a failed process instance

## About this task

Failures can be of two types: system failures or failures
that are caused by invalid or corrupted data. A process instance might
fail because the network connection is down or a power failure occurs.
Or it might fail because changes occur in the execution environment
after the instance migrates, and those changes cause data to become
invalid or corrupted.

## Procedure

1. Open the Process Inspector and filter the search to find
failed process instances only. Click Search.
You can apply other filters to scope the results to make it
easier to process the failures. For example, you might want to process
the failures for one process application at a time.
2. In the results section of the Process Inspector, select
a failed instance.
3. In the details section, start by reviewing what caused the failure. Next to the status, click
Error details.
4. In the window that opens, review the error details including
the Java trace. If you want to save the error details to
a file, click Export Error.
5 Based on what caused the failure and what information youfind in the error details, take the appropriate action for the instance,its tasks, or its activities. For information about theimpact of a particular action, see Actions in the Process Inspector . For example: Fixing the problem might take a number of actions. For example,to skip a task, you might want to first edit its output data. Becauseskipping a task means that it does not update its output data, youcan edit this data so that it is valid for steps that are later inthe flow. Tip: If you suspect thata number of failed instances were caused by a common error, you canselect multiple process instances to take a bulk action on all ofthem. For example, if you are sure that a network problem caused 50process instances to fail, you can select those instances and thenclick the Retry failed steps action. If thebulk action you want to take is not available, then the action isnot available in at least one of the selected instances.
    - If a system going offline caused the error and the system is now
running, click Retry failed steps.
    - If a task is assigned to a user who is not valid, select the task
and then select Reassign to user and then assign
that task to an appropriate user.
    - If the data for the instance, task, or activity is not valid,
edit it to set it to an appropriate value.

Fixing the problem might take a number of actions. For example,
to skip a task, you might want to first edit its output data. Because
skipping a task means that it does not update its output data, you
can edit this data so that it is valid for steps that are later in
the flow.