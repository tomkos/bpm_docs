<!-- image -->

# Replacement variables in human tasks

Only certain task elements can contain replacement variables. These
task elements are defined for the task template, or for a task model
that was created at run time using the Business Process Choreographer
APIs. These definitions are inherited by the task instance when it
is created. The following task elements can include replacement variables.

- Duration until delete
- Duration until expires
- Duration until overdue
- Escalation custom properties
- Escalation description
- Escalation duration
- Email subject and body for escalation notification emails
- People assignment for administrators
- People assignment for editors
- People assignment for escalation receivers
- People assignment for potential instance creators
- People assignment for potential owners
- People assignment for readers
- People assignment for potential starters
- Task custom properties
- Task inline custom properties
- Task description
- Task priority
- Task type

- Actions that initialize or change replacement variables for human task elements

This describes which Human Task Manager replacement variables can be considered to be initialized before the completion of specific task-related actions. This allows both replacement variable initialization and task element evaluation to be done in the same task action.
- Evaluation of task elements and their replacement variables at run time

Task elements can be queried by client applications to expose task-related information. The definition of these elements can contain replacement variables. For these variables to be replaced with values at run time, certain conditions must be met.
- Replacement variables: Examples of usage patterns in task elements

You can use replacement variables in many different ways. At run time, the values used for the variables can come from many sources. For example, they can originate from previous staff resolutions, custom properties and, in the case of inline tasks, from the surrounding BPEL process.