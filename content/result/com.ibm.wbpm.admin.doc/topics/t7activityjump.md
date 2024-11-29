<!-- image -->

# Jumping activities

## Before you begin

To perform this action, you must either be a system administrator
or be a process or scope administrator of the scope or a parent scope
to which the source and target activities belong. However,
if Business Flow Manager is using the alternative process administration
mode that restricts process administration to system administrators,
then only users in the BPESystemAdministrator role can perform this
action.

## About this task

## Procedure

1. In the Views tab,
navigate to the Process State page of the process instance.
2. Click the relevant activity in the process state diagram. 
Note that jump actions are only available if the Detail
level slider of the process state diagram is at the most
detailed level.
3. To go to another activity, click Jump to Another
Activity.  This option only available for
activities in the running state (for example, ready, claimed, running,
stopped, or waiting).
The process state diagram is displayed
again, and only activities that qualify as target activities are selectable.
For information on target activities, refer to the related information
on activity jump targets.
4. Select a target activity to choose an action to perform.
The actions that are available depend on the source activity.
5 Choose an action to perform.
    - To complete the source activity before you jump to the target
activity, click Complete Source Activity and Jump. The Complete
Source Activity and Jump option is only available for
target activities if the source activity is a human task activity
in the claimed state. This option completes the source activity before
you jump to a target activity.
    - To force the completion of the source activity before you jump
to the target activity, click Force Complete Source Activity
and Jump. Then click Force Complete and Jump to
complete the activity with the data that you provide. The Force
Complete Source Activity and Jump option is available
for target activities if the source activity is a human task activity
in the ready, claimed, or stopped state. It is also available for
an invoke activity in the running or the stopped state, a receive
or a wait activity in the waiting or the stopped state, and all other
basic activities in the stopped state. This option forces the completion
of the source activity before you jump to a target activity.
    - To skip the activity and jump to another activity, click Skip
Source Activity and Jump.
    - Click Cancel Jump to cancel the jump action.

- Activity jump targets

When you jump from one activity to another activity in the BPEL process instance using Business Process Choreographer Explorer, you can select the target activity from a list of possible target activities. Certain restrictions apply when you select an activity that serves as a target activity for a jump action.

<!-- image -->