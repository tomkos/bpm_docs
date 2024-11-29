<!-- image -->

# Changes to the expiration, deletion, and due times for tasks
at run time

- Using a specific time
- Using a duration, for example, 2 days, based on a calendar, such
as a business calendar. You can also use the following constants in
duration expressions:
DURATION\_ZERO
The task becomes due or it expires immediately after it starts,
or it is deleted immediately after it completes (depending on the
auto delete setting of the task and the task end state). If the task
has started, it becomes due immediately, or it expires immediately.
If the task is in an end state, it is deleted immediately if auto
deletion is set for the task.
DURATION\_INFINITE
The task does not become due, it does not expire, or it is not
deleted.

For a chain of tasks, each task in the chain has its own due time.
However, only the first task in the chain has an expiration time and
this is shared by all of the other tasks in the chain. Subtasks have
their own due time and expiration time. If deletion is supported for
the task kind, you can change the deletion time.

## Due time

You can set a due time or reschedule it
by setting either the dueTime property or the durationUntilDue property
to a valid value for the calendar that is used by the task. To cancel
the due time, set the durationUntilDue property to DURATION\_INFINITE.
To force the task to become due immediately, for example, because
it is associated with an urgent customer request, set the durationUntilDue
property to DURATION\_ZERO.

## Expiration time

You can set an expiration
time or reschedule it by setting either the expirationTime property
or the durationUntilExpires property to a valid value for the calendar
used by the task. To cancel the expiration time, set the durationUntilExpires
property to DURATION\_INFINITE. To force the task to expire immediately,
for example, because it is no longer required, set the durationUntilExpires
property to DURATION\_ZERO.

## Deletion time

You can set a deletion
time or reschedule it by setting either the deletionTime property
or the durationUntilDeleted property to a valid value for the calendar
used by the task. To cancel the deletion time, set the durationUntilDeleted
property to DURATION\_INFINITE. To force the task to be deleted immediately,
set the durationUntilDeleted property to DURATION\_ZERO.