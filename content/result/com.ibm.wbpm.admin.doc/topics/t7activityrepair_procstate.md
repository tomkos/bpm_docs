<!-- image -->

# Repairing stopped activities using the process state view

## Before you begin

To
perform this task, you must be a process administrator or system administrator. However,
if Business Flow Manager is using the alternative process administration
mode that restricts process administration to system administrators,
then only users in the BPESystemAdministrator role can perform this
action.

## About this task

To repair a stopped activity using the process state view,
complete the relevant step in Business Process Choreographer Explorer.

## Procedure

1. To view the stopped activities of a process instance, click Process Instances > Critical Processes in the navigation pane. Then select the check box next
to the relevant process instance, and click View Process
State. One or more stopped activities or activity gateways
might be listed. Alternatively, select Activity
Instances > Stopped Activities.
2 Depending on the problem that occurred, you can now userepair actions to repair the activity.
    - An activity stopped because the evaluation of a join conditionfailed. The stopReason is Activation failed .Complete the following steps:
        1. Click the activity gateway or, for a single incoming link, click
the activity.
        2. Click Repair Join and choose to either
reevaluate the condition or to force the result of the evaluation
to true or false.
- The evaluation of the loop condition failed for a While or RepeatUntil activity. The stopReason is Implementation failed . Complete the following step:
    - Click the activity, and select either Next Iteration  to
continue the loop or End Loop and to end the
loop.
- The evaluation of a case condition failed for a switch activity.The stopReason is Implementation failed .Complete the following steps::

- Click the activity, and click Force Case Execution.
Select the case to be executed.
- An activity stopped because the evaluation of a transition conditionfailed. The stopReason is Follow-on navigationfailed . Complete the following steps::

1. Click the activity gateway or, for a single outgoing link, click
the link.
2. Click Repair Follow-on Navigation . The
target nodes and links of the available branches are highlighted.
3. To select one or more branches, click the target nodes or links,
and select Select this Branch.
4. Then click a target node, link, or the source node, and click Force
Navigation to force the navigation of the selected branches.
- The evaluation of counter values failed for a forEach activity.The stopReason is Implementation failed .Complete the following steps::

1. Click the activity, and click Repair For Each.
2. Enter start and final counter values and, optionally, the number
of iterations to run to either continue or end the loop.

<!-- image -->