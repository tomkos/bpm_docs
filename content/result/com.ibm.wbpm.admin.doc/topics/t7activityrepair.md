<!-- image -->

# Repairing stopped activities

## Before you begin

- An activity stopped because the evaluation of a join condition
failed. The stopReason is Activation failed.
- A switch activity stopped because the evaluation of a case condition
failed. The stopReason is Implementation failed.
- A while or repeatUntil activity stopped because the evaluation
of a loop condition failed. The stopReason is Implementation
failed.
- A forEach activity stopped because the evaluation of a loop condition
failed. The stopReason is Implementation failed.
- An activity stopped because the evaluation of a transition condition
failed. The stopReason is Follow-on navigation
failed.
- An activity stopped because the exit condition evaluated to false when
evaluated on the completion of the activity. The stopReason is Exit
condition is false.

## About this task

Usually the administrator tries to force a retry of the
activity or to force the completion of the activity. For activity
failures that cannot be repaired with these actions, you can override
the navigation of the activity using Business Process Choreographer
Explorer.

For details about the problem, click Error
Details on the Activity page. You might need to modify
variable values before you continue with the repair action. Furthermore,
you can jump from one activity of a process instance to another activity,
which is described in the topic on jumping activities. You might want
to use a skip activity option to mark a failing activity to be skipped
in subsequent process instances. Also, you might want to skip the
processing of a stopped activity or mark it to be skipped when it
gets processed again.

To repair a stopped activity, complete
the relevant step in Business Process Choreographer Explorer.

## Procedure

1. To view stopped activities, click Stopped Activities under Activity
Instances in the navigation pane, and then click the relevant
activity.
2 You can now take the relevant action to repair the pendingactivity.
    - An activity stopped because the evaluation of a join conditionfailed. The stopReason is Activation failed .Complete the following steps:
        1. In the Views tab,
navigate to the Activity page for the activity, and click Repair
Join.
        2. Select the relevant option to continue processing. You can specify
that the join condition is reevaluated, and the navigation of the
process instance continues. Alternatively, you can specify that the
value of the join condition for the activity is set to true or false
to determine if the navigation of the current branch continues.If
a value of True is specified, the activity is started.
If a value of False is specified, the behavior depends
on the suppressJoinFailure process attribute. If this attribute is
set to yes, the activity is skipped and the status
of all outgoing links of this activity is set to false.
Otherwise, the joinFailure standard fault of Business Process Execution
Language is given.
        3. Click Continue to force the activity navigation.
- A switch activity stopped because the evaluation of a case conditionfailed. The stopReason is Implementation failed .Complete the following steps:
    1. In the Views tab,
navigate to the Activity page for the activity, and click Force
Case Navigation.
    2. Select the branch that is to be followed during the navigation.
The branches are enumerated according to their position in the model.
You can only select one branch.
    3. Click Submit to force the case navigation.
- A while or repeatUntil activity stopped because the evaluationof a loop condition failed. The stopReason is Implementationfailed . Complete the following steps:

1. In the Views tab,
navigate to the Activity page for the activity, and click Next
Iteration or End Loop to force
the navigation of the activity.
- A forEach activity stopped because the evaluation of a loop conditionfailed. The stopReason is Implementation failed .Complete the following steps:

1. In the Views tab,
navigate to the Activity page for the activity, and click Repair
For Each.
2. Specify the relevant values to continue processing. Specify a
value for the start counter and the final counter. If the forEach
activity has an early exit condition, also specify a value for the
number of iterations to be completed.
3. Click Continue to force the activity navigation.
- An activity stopped because the evaluation of a transition conditionfailed. The stopReason is Follow-on navigationfailed . Complete the following steps:

1. In the Views tab,
navigate to the Activity page for the activity, and click Force
Navigation.
2. Select the names of the links that are to be followed during navigation.
The displayed names of the links are the names that are determined
in IBM® Integration
Designer during
the modeling of the process. You can select an arbitrary number of
links.
3. Click Submit to force the activity navigation.
- An activity stopped because the exit condition evaluated to false whenevaluated on the completion of the activity. The stopReason is Exitcondition is false . Complete the following steps:

1. In the Views tab,
navigate to the Activity page for the activity, and click Restart or Force
Complete.
2. Specify the data that is needed to restart or complete the activity.
3. Click Restart or Force Complete to
force the activity navigation.

<!-- image -->