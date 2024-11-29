<!-- image -->

# Enhanced dynamic behavior in a process

## About this task

To
set up dynamic runtime behavior on a collaboration scope or a scope
activity, proceed as follows:

## Procedure

1. Confirm that the process is long-running. Because
this involves human tasks, the process on which it is enabled cannot
be modeled in a microflow.
2. Drop a collaboration scope or a scope activity onto the
canvas of the process editor and configure it according to your business
needs.
3. In the Properties area, select the collaboration scope
or scope activity, click the Administration tab.
4. Create or configure a new administration task. For
a collaboration scope, a new administration task is automatically
created for you. The default setting of this administration task is
that Everybody is an administrator. In realistic
situations you will want to limit who has administrative control over
the activities in the collaboration scope to a specific user or group.
For
a scope activity, no administration task is generated automatically
and you must create and configure a human task to act as the administration
task.
5. Configure the administrators of the Human Task to be the
group of people that should have administrative authority over the
collaboration scope or scope activity. For instructions
on how to work with the human task editor, see Human Task editor, and The building blocks of the business state machine editor

## Results

When this process is deployed to a runtime environment,
the authorized user will see a graphical process view of the Business
Process Choreographer Explorer. The user will be able to right-click
an activity that is nested in a scope for which enhanced dynamicity
is configured, and see a menu displaying the various kinds of behavior
that can be influenced.