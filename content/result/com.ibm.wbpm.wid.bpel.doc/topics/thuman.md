<!-- image -->

# Adding a human task

## About this task

For
a more detailed introduction to people interaction, see Human tasks.

There
are two ways to implement a human task. If the task is implemented
within a BPEL process, it is called an inline task. Otherwise,
it is referred to as a stand-alone task. Although the
inline task is the only one actually implemented within a BPEL process,
both kinds of tasks are related to BPEL processes. Consider the following
scenarios:

To add a human task to a BPEL process, choose one
of the following options:

## Procedure

1 Creating an inline to-do human task that will send a messageto a human: Note: This is an inline task, but it can also be modeledas a stand-alone task by creating a to-do task in the human task editor,and then wiring it to a BPEL process in the assembly editor.
    1. From the palette, drop a human task activity () onto the canvas.
    2. On the window that appears, specify a name for the human
task, select the interface that the human task will implement, and
click OK. The human task editor
will open.
    3. Use the settings in the human task editor to configure
this human task. For instructions on how to use the editor,
follow the links in the Related information section
below.
2 Creating an inline invocation task where a person can senda message to a BPEL process: Note: This task can also be modeled as stand-alone invocationtask by creating an invocation task in the human task editor, andthen wiring it to a BPEL process in the assembly editor.

1 On the canvas, select one of the following elements:
    - a receive activity,
    - a receive case element within a receive choice activity,
    - an OnEvent element within an event handler.
2. Click the Authorization tab in
the properties area.
3. Click New to create a human task,
and configure it as necessary in the human task editor.
3 Granting a human administrative power over a BPEL process:

1. Chose the process as a whole, and click the Administration tab
in the properties area.
2. You can create the following two administrative settings:

Option
Description

An administration task for the process
Use this task to define the group of people
that will have administrative rights in for the process as a whole.

A default activity administrative task.
This task would define the default administration
settings for all of the activities within that process. For example,
if an activity gets stuck during execution (perhaps a service call
failed), the user will need administrative rights to recover the process
instance. Although these administrative rights can be given for each
activity individually, an activity that does not have an administrator
attached will need to be able to fall back to this default administrative
task.

## Example

- Human Task features  > Single-person
workflow
- Human Task features > Dynamic
staff assignment and 4-eyes principle