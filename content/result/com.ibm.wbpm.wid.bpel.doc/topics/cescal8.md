<!-- image -->

# Escalations

You can use IBM® Integration
Designer to
model escalations for tasks that are in the activation states of ready,
running, claimed, or subtask.

You can define escalations for any task during modeling or, dynamically,
when you create a task at run time.

Escalations are activated at a certain task state. The task will
normally only be escalated because the expected task state has not
been reached when the time limit for the escalation expires. However,
it can also be triggered manually any time before the time limit expires
by a user who has the appropriate authority. The time limit for the
escalation is interpreted by the calendar that is specified for the
task. You can specify multiple escalations (or escalations chains)
that have the same activation state. An escalated task is put into
the escalated substate.

- Escalate when the task is not claimed in time using the expected
task state of claimed.
- Escalate when the task is not completed in time using the expected
task state of ended.

When an escalation is raised, the people affected by the escalation
(the escalation receivers) receive work items. Depending on the definition
of the escalation, the escalation receivers might also receive an
email notifying them that the task is escalated. The list of users
to be notified is defined by a people query. This query must resolve
to a set of individual user IDs.

You can define the escalation in the task model so that the priority
of the task is automatically increased either for the first iteration
only, or for every iteration of the escalation. In the administrative
console, you can specify how you define priorities in your organization,
by setting values for the Task.Priority.Highest and
the Task.Priority.Lowest custom properties for
Human Task Manager. For example, in your organization, you might use 0 to
indicate the highest priority, other organizations might use 5 to
express this priority.

## Designing an escalation

- to whom the resulting work item should be assigned,
- the period of time before it should be escalated,
- the state that you want the task to be in when the escalation
value times out (if it is not in this state, then an escalation is
thrown),
- the action that should be taken in the case of an escalation,
- the mode of notification,
- whether the escalation should be performed again, and if so, how
soon,
- whether the task priority should be increased during the escalation.

## Lifecycle of an escalation

Here is a brief
description of the stages that a typical escalation will go through.

1. An instance of a task is created and, if it has an associated
escalation, it remains inactive until the task reaches the activation
state.
2. When the task reaches the activation state, the first escalation
of each chain is initialized with the starting of the Escalate timer,
and the escalation moves to the waiting state.
3. When a timeout occurs, the system checks to see if the expected
task state has been reached. If the task has reached or passed
it, the escalation state is changed to superfluous. If the
expected state has not yet been reached, the escalation state is changed
to escalated, and the escalation action is invoked, and one
of the three possible actions occur (work item, email notification,
or event handler notification).
4. The escalation is repeated according to the Repeat notification
every value.
5. The escalation's priority is increased according to the Increase
task priority value. The priority can be increased repeatedly
if an auto-repeat duration is set.

## Chained escalations

A chain of escalations
is a series of escalations with the same activation state that are
processed sequentially so that only one is active at any one time.
The wait duration for each of the escalations in a chain is cumulative.
That is, the timer on the second escalation in a chain will not start
until the first escalation has timed out. This prevents escalations
that are further along in the chain from timing out before the ones
at the beginning. Also, keep in mind that an escalation with an expected
state of end, cannot precede another escalation. Such a situation
would never escalate, and you will receive a validation error if one
exists in your diagram.

## Parallel escalations

Parallel escalations
are two or more escalations that are processed at the same time as
opposed to sequentially. Each of the escalations has the same activation
state but, in contrast to a chained escalation, its wait duration
fires independently, and any one of them can have an end state as
the expected state.

## Escalations and task ownership

You have
two choices of ownership pattern for your human tasks: single or parallel.
One consequence of the choice of single or parallel ownership is in
the handling of escalations. For single ownership you can define escalations
that are triggered when the task is in the ready or claimed state.
Such escalations are not applicable to a parallel ownership task.
If you change the ownership of a task from single to parallel, you
will be prompted for what to do with escalations that you have defined
for the ready or claimed states. You can use them in a modified form,
or you can delete them. See the related topic on Ownership Patterns
for more details.

- Creating an escalation for your human task

An escalation is a notification that is sent out when an expected result from a task has not been achieved within a set period of time. For example, an escalation could be used to alert a manager when a staff member is unable to complete a task by the deadline.

## Related tasks

- Creating subtasks