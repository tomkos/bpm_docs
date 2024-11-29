<!-- image -->

# Restarting task instances using Business Process Choreographer
Explorer

You can restart task instances using
Business Process Choreographer Explorer. You might want to do this,
for example, for a human task that is already running but not progressing
as expected, or for a task that has reached an unexpected or undesired
end state, such as failed or expired.

Additionally,
you can change the input message values of tasks before you restart
them. You can restart a task that you want to reuse in order to initiate
the same work again. This could be a human task that has finished,
for example an invocation task or a collaboration task. Typically,
you would restart this task with a changed input message.

## Before you begin

- An invocation task cannot be in the running state.
- A to-do task cannot be in an end state, that is, it cannot be
finished, failed, terminated, or expired. If the to-do task is forwarded,
then the follow-on task cannot be in an end state.
- An inline to-do task cannot be in the ready state.

The task instance can be escalated, suspended, or waiting
for subtasks. The caller must be the starter, originator, or an administrator
of the task instance.

Restarting the task instance causes the
people resolution to be newly performed and all timers to be reset.
Any subtasks or follow-on tasks are deleted. Any escalations are canceled
and reset into the inactive state. For invocation tasks, the logged-on
user becomes the starter of the restarted task instance.

## About this task

To restart a task instance, complete the following steps
in Business Process Choreographer Explorer.

## Procedure

1. In the Views tab,
navigate to the Task page for the task, and click Restart.
2. Click Restart to start the task
again with the information you provide.

<!-- image -->