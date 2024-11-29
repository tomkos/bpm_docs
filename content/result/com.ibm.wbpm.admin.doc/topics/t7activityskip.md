<!-- image -->

# Skipping activities in BPEL processes

## About this task

## Procedure

1. In the Views tab,
navigate to the Process State page of the process instance.
2. Click the relevant activity in the process state diagram. 
Note that skip and jump actions are only available if the Detail
level slider of the process state diagram is at the most
detailed level.
3 Perform one of these skip actions.
    - Click Skip Activity to mark this activity
to be skipped. The activity is then indicated by the skip requested
icon . Activities that are skipped are indicated by the skipped
icon .To
perform this action, you must be a process administrator or a scope
administrator of the scope or a parent scope to which the source and
target activities belong.
The Skip Activity action
is available for any activity state. An activity that is in an end
state is marked to be skipped but the state of the activity remains
unchanged until it is reached again by the navigation. Therefore,
if an activity is already in an end state, the activity is skipped
as soon as it is activated again.
    - To unmark the activity to be skipped, click Cancel
Skip. This cancels a previously selected skip activity
request.
    - Alternatively, to skip the activity and jump to another activity,
click Jump to Another Activity. The diagram
is displayed again, and only activities that qualify as target activities
are selectable. Note that the options available depend on the source
activity.
To skip the activity and jump to another activity,
click Skip Source Activity and Jump.

<!-- image -->