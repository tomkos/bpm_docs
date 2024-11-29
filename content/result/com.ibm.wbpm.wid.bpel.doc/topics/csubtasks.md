<!-- image -->

# Subtasks

Subtasks can be created from stand-alone task templates that are
stored in the Business Process Choreographer database, from task templates
created at run time, or by providing a new task model at run time.
The parent task can be a to-do task or a collaboration task, and it
must have the supportsSubtask attribute set to true.
The subtasks that are created can be either collaboration tasks or
invocation tasks. These subtasks can, in turn, have subtasks or follow-on
tasks.

There are no restrictions on either the input message type or the
output message type. However, the starter of the subtask must provide
an input message. When the subtask is finished, the owner of the parent
task can map the subtask output data to the output message of the
parent task.

1. The staff member claims the parent task in the runtime environment
through a user interface.
2. The staff member then initiates a subtask from an existing definition,
and provides an input message for the subtask.
3. The parent task enters the WAITING\_FOR\_SUBTASK state, and will
remain there until all of its subtasks, are complete. Subtasks cannot
be deleted unless the parent task is first deleted. If the parent
task suspends, resumes, terminates, or expires, all subtasks will
be as well.
4. The subtask will enter the work queue, where it can be claimed
by anyone in the authorized group.
5. When all subtasks have entered an end state, the parent task can
then be completed.

## Authorization considerations

## Lifecycle considerations

When the first
subtask is started, the parent task enters the waiting-for-subtask
substate. It remains in this substate until all of the subtasks reach
one of the end states finished, failed, expired, or terminated. Some
lifecycle operations (state changes) of the parent task are propagated
to its subtasks. So, when the parent task is suspended, resumed, terminated,
deleted, or it expires, all of its subtasks are also suspended, resumed,
terminated, deleted, or expire. The escalated substate of a parent
task is not propagated; subtasks are not escalated when the parent
task is escalated. Subtasks have their own escalations and their escalated
substate is set only when one of their own escalations is triggered.

- Operations that do not conflict with the parent task are always
supported. These are operations, such as claim, cancel claim, complete,
creation and start of subtasks or further follow-on tasks.
- Subtasks can expire.
- Subtasks can be suspended and resumed because work on a subtask
might need to be stopped although work on the parent task continues.
- Subtasks can be terminated.
- Subtasks can have their own escalations so that the parent task
owner and the subtask originator can better control the progress of
the subtask.

Some lifecycle operations on a subtask can conflict with
the lifecycle operations of the parent task, and are therefore not
allowed. These are mainly operations that influence the end of the
lifecycle of a subtask and need coordination with the parent task.
Auto-deletion settings are ignored for tasks that are started as subtasks.
Subtasks are deleted when their parent task is deleted or restarted.
The deletion of individual subtasks using the Business Process Choreographer
APIs is not supported.

## Example: Interaction between a parent task and a collaboration
task

<!-- image -->

In a book publishing process, the "Review Book" task
is claimed by Linda. She realizes that the book is too large for her
to review alone, and specialized knowledge is required for some parts
of it. She decides to deviate from the standard publishing process,
and assigns parts of her task to some of her colleagues. She creates
three additional tasks from the "Review book section" template: "Review
Part 1", "Review Part 3", and "Review Appendix". She will review part
2 of the book herself.

She includes the complete book as input
to the subtasks so that her colleagues have enough context information,
but adds a note to the task description to tell her colleagues to
review only the parts of the book that are assigned to them. She assigns
the tasks to her colleagues: John to review part 1, Cindy part 3,
and Mary the appendix. Then she starts the three tasks as subtasks
of her own "Review Book" task. Her task that was in the claimed state
is put into the waiting-for-subtask substate until all three subtasks
are complete.

Cindy, John, and Mary claim their subtasks and
start reviewing their parts of the book. In the meantime, Linda reviews
part 2 of the book. When she finishes her part of the review, she
checks on the progress of her colleagues. Cindy and John have completed
their review, but Mary is still reviewing the large appendix. Linda's
task is still in the waiting-for-subtask substate. Although, Linda
cannot complete her task, she starts consolidating the review comments
based on the output of Cindy and John's subtasks.

In the meantime,
Mary completes her subtask too, and Linda's "Review Book" task leaves
the waiting-for-subtask substate. Now, Linda consolidates Mary's review
comments with the rest of the book, and completes her task. The book
publishing process continues. Because the "Review Book" task is
an inline human task, it is deleted with its subtasks when the BPEL
process instance is deleted.

## Example: Interaction between a parent task and an
invocation task

The interaction between a parent task and
an invocation task is similar to that of a parent task and a collaboration
task. The task owner creates a task from an existing invocation task
template, and starts it as a subtask of her own task. The parent task
enters the waiting-for-subtask substate and waits for the invocation
subtask to return. When the subtask is complete, the parent task leaves
the waiting-for-subtask substate and it can be completed.

- Creating subtasks

In the runtime environment, if a person who claims a task finds that they are not able to complete it by themselves, they can delegate portions of that original task to other people in the form of subtasks.