<!-- image -->

# Suspending and resuming BPEL process instances

## Before you begin

To
suspend a process instance, the process instance must be in either
the running or failing state. To resume a process, the process instance
must be in the suspended state.

## About this task

To suspend or resume a process instance, complete the
following steps in Business Process Choreographer Explorer.

## Procedure

1. Display a list of process instances. For
example, click Administered By Me under Process
Instances in the Views tab navigation
pane.
2. Suspend the process. Select the check box
next to the process instance and click Suspend.
3 Choose one of the options to suspend the process instance.
    - To suspend the process until it is manually resumed, select Suspend.
    - To suspend the process until a certain time, select Suspend
process until, and specify the date and time.
    - To suspend the process for a period of time, select Suspend
process for, and specify the duration.
4. To confirm your selection, click Submit.
This action suspends the specified parent process instance. The process instance is put into the
suspended state. Subprocesses with the autonomy attribute set to child are also suspended
if they are in the running, failing, terminating, or compensating state. However, you can still
complete any active activities and tasks that belong to the process instance.

## What to do next

<!-- image -->