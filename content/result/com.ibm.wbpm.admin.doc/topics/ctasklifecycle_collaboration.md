<!-- image -->

# State transition diagrams for collaboration tasks

The state transitions that occur during the lifecycle  of the task
also depend on whether the task has single ownership or parallel ownership.

## Collaboration tasks with single ownership

<!-- image -->

After the task is
created, it is put into the inactive state. In this state, the task
cannot be claimed, but you can update task properties or set custom
properties. To work on a collaboration task, it must be started.

- The task is escalated if it is not claimed or completed in time,
or an authorized user triggers the escalation manually. The task is
put into the escalated substate, and it stays in this substate for
the rest of the task lifecycle.
- The task can be suspended manually. It is put into the suspended
substate. Most actions on the task are blocked in this state. It can
be resumed manually, or automatically by a timer that is set with
the suspend action.
- The task can expire. This state change ends the task.
- To reschedule a task when it is due, expires,
or is deleted, the originator, starter, or administrator of the task
can edit the appropriate property for the duration or point in time.
- The task can be terminated manually using the terminate action.
This state change ends the task.
- The task can be restarted. If the task is suspended, the suspended
substate is cleared. If the task is escalated, the escalated substate
is cleared. If the task has escalations, all of the escalations are
put back into the inactive state and all of the running escalations
are canceled. If the expiration timer is set, it is canceled and restarted,
and the due time is recalculated. If the task is waiting for subtasks,
the waiting-for-subtask substate is cleared, and the subtasks are
deleted.

- If they need support for their work, they can create subtasks
to delegate parts of the work to other people. These subtasks can
be either collaboration tasks or invocation tasks. The parent task
then enters the waiting-for-subtask substate and remains in this state
until all of its subtasks reach an end state. The parent task can
be suspended while waiting for subtasks, but it cannot be completed
and the claim cannot be canceled. If the parent task is suspended,
all of its subtasks are also suspended.
- If they want to delegate the completion of the work to someone
else, they can create, for example, a collaboration task as a follow-on
task to complete the work. The parent task is put into the forwarded
end state.
- If they want to delegate the overall responsibility for tasks,
they can transfer owner work items to another potential owner, or
an administrator.
- If they want to give up ownership of a task, they can cancel the
claim of the task. The task is put into the ready state again, and
it can be claimed by one of the potential owners. If the claim of
the task is canceled, this action does not affect the due time or
expiration time of the task, or the timing of the escalations.

- The task can be escalated because it is not completed in time,
or if it waits too long for subtasks to complete. An authorized user
can also trigger the escalation manually. The task is put into the
escalated substate.
- The task can be suspended manually. It is put into the suspended
substate. Most actions on the task are blocked in this state. It can
be resumed manually, or automatically by a timer that is set with
the suspend action. Alternatively, when the timer expires, the claim
on the task is canceled and it is put into the ready state again.
- The task can expire. This is a state change that ends the task.
- The task can be terminated manually using the terminate action.
This is a state change that ends the task.
- The task can be restarted. The task is put back into the ready
state. If the task has substates, these are canceled. Escalations
associated with the task are reset to the inactive state, and begin
their normal lifecycle. If the task has subtasks, they are terminated
and deleted.

When the owner finishes work on the task, they complete
it. The task is then put into the finished state if it completes successfully,
or the failed state if an error occurs.

The failed, terminated,
finished, and expired states are end states in which work cannot be
performed. If the task template specifies automatic deletion, the
task is either deleted immediately, or after the deletion timer expires.
Without automatic deletion, the task remains in its end state until
it is explicitly deleted. When the parent task is deleted, its subtasks
and follow-on tasks are also deleted.

The forwarded state indicates
that work is still required on the follow-on task. Automatic deletion
of the parent task applies as soon as the follow-on task reaches an
end state. Without automatic deletion, both the parent and the follow-on
task remain in their states until the parent task is explicitly deleted.
When the parent task is deleted, the follow-on task is deleted as
well.

A task in one of the end states can be restarted, if
it is not a follow-on task of a to-do task. The task is put back into
the ready state. Escalations associated with the task are canceled
and put into the inactive state, and the deletion timer is also canceled.

## Collaboration tasks with parallel ownership

<!-- image -->

The
parent task cannot be claimed or manually completed. The parent task
goes into the running state and stays there until its completion condition
becomes true, or expiration is reached.