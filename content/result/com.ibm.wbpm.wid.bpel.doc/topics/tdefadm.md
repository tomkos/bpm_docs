<!-- image -->

# Defining administration in a BPEL process

## About this task

## Procedure

1 To configure administration on a BPEL process:
    1. Select the process as a whole by clicking any empty
area on the canvas.
    2. In the Properties area, click
the Administration tab.
    3. Create or configure a human task. You will
have two options:

Option
Description

An administrative task for the process
Use this task to define the individuals or group
that will have administrative rights for the process as a whole.

A default activity administrative task
This task would define the default administration
settings for all of the activities within that process. For example,
if a service call fails an activity may not be completed successfully,
the user will need administrative rights to recover the process instance.
Although these administrative rights can be given for each activity
individually, an activity that does not have an administrator attached
will need to be able to fall back to this default administrative task.
    4. Configure the administrators of the Human Task to be
the group of people that should have administrative authority over
the process. For instructions on how to work with the Human
Task editor, see Human Task editor, and The building blocks of the business state machine editor.
2 To configure administration on an invoke, scope, collaborationscope or snippet activity: Note: Configuring administration for an invoke, scope, collaborationscope or snippet activity overrides any default activity administrativetask defined for this BPEL process. Other activities in the processwill still use the default activity administrative task.

1. Drop an invoke, scope, collaboration scope or snippet
activity onto the canvas.
2. In the Properties area, click
the Administration tab.
3. Create or configure a human task. For the
collaboration scope the administration task is automatically generated.
The default setting gives administrative authority to Everybody, which will not be an appropriate setting in most cases.
4. Configure the administrators of that human task to be
the group of people that should have administrative authority over
the activity. For instructions on how to work with the
human task editor, see Human Task editor, and The building blocks of the business state machine editor.