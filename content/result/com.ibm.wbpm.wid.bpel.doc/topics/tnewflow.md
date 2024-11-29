<!-- image -->

# Creating a BPEL process

## About this task

## Procedure

1. Switch to the Business Integration view.
2. To create a default business process, from the main menu, click File > New > BPEL Process.
3 To create a new process from scratch:
    1. Browse to an existing module (or click New to create one), and then
specify a folder (optional) and a name for the new process, and click
Next.

Tip: If you want to select a namespace other than the one provided by default, clear the
Default check box, and enter a new value in the
Namespace field.
    2. Select one of the following process types:

Option
Description

Long-running process

A long-running process is a business flow that runs over an extended period of time, and is much more flexible and resilient than a microflow. It is used most commonly with services that may not respond immediately, in particular human tasks. IBM® Integration

Designer enhances BPEL capabilities through the use of BPEL extension. For information, see Working with BPEL extensions. If you would like to create a process without the use of these extensions, then disable the Use IBM Workflow

Server extensions check box.

Microflow
A microflow is a process that is contained within a single transaction.
Because it runs automatically from start to finish, it is ideal for situations where the user is
expecting an immediate response, and does not require the use of a human task.
    3. In the Select an Interface window, you can specify an existing interface
or have the system generate one for you.

Tip: If you specify an existing interface that has more than one operation defined then
you must implement each of these operations in your process. If these operations must be implemented
in a specific order, then you must implement each of these operations in your process in the
required sequence.
4. Click Finish.

## Results

- BPEL process editor

The BPEL process editor is a graphical programming environment that you use to visually create and manipulate BPEL processes.
- Lifecycle of a business process

A process goes through a number of stages from its start to its finish.
- Defining administration in a BPEL process

When you define administrative rights in a BPEL process, you involve human tasks and grant organizational control over some or all of the BPEL process to a select group of users.
- Refactoring and business state machines

When you refactor parts of your business state machine, dependencies on those parts are automatically and universally updated throughout the product as a whole.
- Creating a BPEL process from a component

You can generate a BPEL process from components in the assembly editor.

## Related concepts

- Best Practice: When to not use the BPEL extensions
- Working with BPEL extensions