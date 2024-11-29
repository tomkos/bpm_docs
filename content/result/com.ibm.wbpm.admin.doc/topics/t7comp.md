<!-- image -->

# Administering compensation for microflows using Business Process
Choreographer Explorer

## Before you begin

## About this task

If a compensation action for a microflow fails, the process
administrator must intervene to resolve the problem.

In Business
Process Choreographer Explorer, complete the following steps to administer
failed compensation actions.

## Procedure

1. Display a list of the compensation actions that failed.
Click Failed Compensations under Process
Instances in the Views tab navigation
pane.
The Failed Compensations page is displayed.
This page contains information about why the named compensation action
failed. This information can help you to decide what actions to take
to correct the failed compensation.
2. Select the check box next to the activity and then click
one of the available actions.  The following administrative
actions are available:

Skip
Skips the current compensating action and continues with compensating
the microflow. This action might result in a non-compensated activity.
Retry
If you have taken action to correct the failed compensation action,
click Retry to try the compensation action
again.
Stop
Stops the compensation processing.

<!-- image -->