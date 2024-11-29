# Creating an unstructured (ad hoc) activity

## About this task

## Procedure

To create an unstructured (ad hoc) activity, complete the following
steps.

1. Drag the activity from the palette to your process diagram.

Important: Do not add any input or output wiring to the activity. If
you add any wiring to the activity, the activity is no longer unstructured. The
Behavior section is only displayed for unstructured activities that have User
Task, Subprocess, or Linked Process implementations. For these implementations, make sure that the
check box The activity runs even though it does not have an inbound flow is
selected.
2 Specify the behavior properties of the activity.
    1. In the Properties pane, select the General tab and
expand the Behavior section.
    2 Indicate how the activity is started.
        - If the activity is started by the system, select Automatically by the
system.
        - If the activity must be started manually by the user, select Manually by the
user.
3 Indicate whether the activity must be completed.
    - If the activity must be completed before the process can complete, select Yes. The
activity is required.
    - If the activity does not have to be completed for the process to complete, select No.
The activity is optional.
4. If the activity can be run multiple times, select Repeatable: The activity
can be invoked multiple times.
5. If the activity is started by the system, and must be hidden from users, select
Hidden. This is a background activity that users will not
see.
6. If preconditions must be met before the user or system can start the
activity, select the Preconditions tab, and specify the conditions that must
be met. See Setting preconditions for ad hoc activities.
3. Click Save or Finish Editing.

- Setting preconditions for ad hoc activities

You can specify preconditions that must be met before the activity is ready to start. Activities can start automatically after all the preconditions are met or manually by a user after all the preconditions are met. If you do not set any preconditions, automatic activities start as soon as the process is started and manual activities must be started by a user.
- Example: Starting an unstructured (ad hoc) activity (JavaScript API)

This example shows you how to start an unstructured (ad hoc) activity.