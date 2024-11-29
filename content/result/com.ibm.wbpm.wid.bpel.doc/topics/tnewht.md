<!-- image -->

# Creating human tasks

## Procedure

1. In the workbench, switch to the business integration perspective.
2. From the main menu, click File > New > Human Task.
3. Specify a module (if necessary), a folder, and a name for
the new human task, and click Next.
4. In the Select Type of Interaction and Interface
Definition window, choose from these three options:

Option
Icon
Description

To-do task

This is where a service component
(such as a BPEL process) assigns a task to a human as something for
that person to do.

Invocation task

This is where a human can "assign"
a task to a service component. In such a case, a human is invoking
an automated service such as a BPEL process.

Collaboration task

This is where a human assigns
a task to another human.
5. If you have an existing interface to reference, then choose
it here, otherwise select to have one automatically generated for
you.
6. Click Next. If you selected
an invocation task, Next is disabled and you
should click Finish.
7. On the Select the Type of Human Task Ownership panel,
select Single or Parallel. 
Single ownership means that a task should need only one person
to complete it. The first potential owner to claim the task becomes
the sole owner. Parallel ownership allows multiple people to work
on a task simultaneously. Each potential owner is assigned a subtask
and the results of each of these subtasks are aggregated when completion
criteria are met.
8. Click Finish to create your human
task.

## Results

- Creating human tasks

To create a new human task, follow these instructions.
- Human Task editor

The Human Task editor is a graphical programming environment that you use to configure the interaction between a service and identified people, or between two people.
- The building blocks of the business state machine editor

Compose your own business state machine using a combination of the following building blocks.
- Replacement variables and context variables

While working with templates, you might want to refer to a variable that will not be resolved until the instance has been started in the runtime environment. This variable is known as a context variable, because its value is dependent upon the task context in which it is exists (or the process context for inline tasks). If you want to refer to such a context variable in a template, you must use a replacement variable.
- Replacing a stand-alone task with an inline task in the BPEL process

You can take an existing stand-alone task that is invoked by an invoke activity in a business process and transform it into an inline task that is implemented by a human task activity.
- Refactoring and business state machines

When you refactor parts of your business state machine, dependencies on those parts are automatically and universally updated throughout the product as a whole.
- Supporting other languages

You can display client-based information in multiple languages.