<!-- image -->

# State transition diagrams for activities in BPEL processes

- Short-lived
activities, such as assign, empty, reply, rethrow, throw, terminate,
and Java snippet activities
- Activities
that wait for an external event, such as receive and wait activities
- Pick (receive
choice) activities
- Invoke
activities
- Human
task activities for tasks with single or sequential ownership
- Human
task activities for tasks with parallel ownership

In contrast to the state diagrams for process instances, activity
end states are not explicitly exposed. The lifecycle of an activity
depends on the enclosing process. Activities are always deleted with
the process instance.

## Conventions used in these diagrams

| Symbol   | Explanation                                                                                  |
|----------|----------------------------------------------------------------------------------------------|
|          | Transient state. These states are not visible.                                               |
|          | Persistent state.                                                                            |
|          | State transitions that are triggered automatically by Business Flow Manager.                 |
|          | State transitions that are the result of a user interaction, for example, by an API request. |
|          | State transitions that are controlled by Business Flow Manager or by a user interaction.     |

## State transition diagram for short-lived
activity types

<!-- image -->

- The join condition evaluates to false and the suppressJoinFailure attribute
is set to true. The state of the activity changes
to skipped (2), and the links leaving the activity are navigated as
dead paths.
- The join condition evaluates to false and the suppressJoinFailure attribute
is set to false. The activity remains in the inactive
state because it has not been started, and a bpws:joinFailure standard
fault is raised.
- The join condition evaluates to true . Foractivities that are not enclosed in a flow, this is the expected behavior.The subsequent behavior of the activity depends on whether it hasan exit condition that is evaluated on entry of the activity.
    - If the exit condition evaluates to true, the
state of the activity changes to skipped (2), and the transition conditions
of the links leaving the activity are evaluated.
    - If the exit condition evaluates to false or ifan exit condition is not specified, the activity is activated, andit state changes to running (3a). The activity implementation is runand when it successfully completes, the subsequent behavior of theactivity depends on whether it has an exit condition that is evaluatedon entry of the activity. If the Continue On Error setting is setto yes and the implementation fails, for example,when the syntax of a copy statement in an assign activity is incorrect,the state of the activity changes to failed (3c). All short-livedactivities are non-interruptible. As a result, the running state isnever visible.
        - If such an exit condition is specified and it evaluates to true or
if it is not specified, the state of the activity changes to finished
(3b), and the transition conditions of the links leaving the activity
are evaluated.
        - If the exit condition evaluates to false the
activity state changes to stopped (9b).

An activity instance can be skipped in any state, including
the inactive state. If the activity is in the inactive state, the
state changes from inactive to skipped (2) when the activity is reached
by the navigation, regardless of the outcome of the join condition.
The transition conditions of the links that leave the activity are
also evaluated. If the activity is automatically skipped, the conditions
are not evaluated.

- The activation of the activity fails, for example, if an exception
occurs during the evaluation of the join condition.The state of the activity changes from inactive
to stopped (9a). The activity can be repaired by an administrator
with the help of a forceRetry or forceJoinCondition API
request. For a forceRetry API request, the state
of the activity changes to inactive (10a) and the activation of the
activity is tried again. If the retry is successful, the state changes
to running (3a), and finally to finished (3b). If the retry is not
successful, the activity is put into the stopped state again (14).
For a forceJoinCondition API request, the state
of the activity changes to inactive (10a) and then, depending on the
condition value passed as an API parameter, the state changes to running
(3a) or skipped (2).
You can change the continue-on-error behavior
with the API repair request. If this is done and the activation fails
again, the activity ends in the inactive state (10a), and the fault
is propagated to the fault handlers of the enclosing scope.
- The implementation of the activity fails, for example, because
the XPath expression in an assign statement causes an exception.The
state of the activity changes from running to stopped (9b). Because
the state change occurs in a single transaction, the running state
is not visible.
The activity can be repaired by an administrator
with the help of a forceRetry API request. The
activity is put back into the running state (10b). The activity can
also be repaired with a forceComplete API request.
In this case, the activity is put into the finished state (11), and
the navigation of the process continues.
If the activity is
repaired, the stopped state can be reached again (14) if the implementation
of the activity fails again during the repair step. If the continue-on-error
behavior is changed with the API repair request and the implementation
fails again, the activity ends in the failed state, and the fault
is propagated to the fault handlers of the enclosing scope.
- The evaluation of the transition conditions on a link leaving
the activity fails.The state of the activity was finished or skipped
before the error occurred (9c or 9d). The activity can be repaired
by an administrator with the help of a forceComplete API
request. If the evaluation is then successful, the state is finished
again (11). If the evaluation is not successful, the state of the
activity is either stopped (14) or failed (12).
Alternatively,
the activity can be repaired with the help of a forceNavigate API
request. In this case, the administrator can determine which outgoing
links of the activity should be followed. The state of the activity
changes back to finished (11), the transition conditions are not evaluated,
but the transition condition of the specified links are considered
to be evaluated to true. This means that if the activity
is in a parallel flow, all other links are navigated as dead paths.

If an activity is in the stopped state and the enclosing scope
is terminated, for example, because of an uncaught fault in a parallel
branch, the activity is terminated. Its state changes to the terminated
state (13).

## State transition diagram for activities
that wait for an external event

<!-- image -->

The
starting phase of receive and wait activities, and the state transitions
to and from the stopped state are the same as for short-lived activities.
However, after receive and wait activities are activated, the state
changes to waiting instead of running (3). The receive or wait activity
is now ready to receive an external request, or to wait for the specified
timeout, before it can complete and move to the finished state (4).
For a receive activity, the transition to the finished state is triggered
by the message that is received. For a wait activity, this transition
is done automatically after the specified wait time elapses, or it
can be forced using a force-complete API request. However, if the
receive or wait activity has an exit condition with the condition
evaluation attribute set to on exit and the exit
condition evaluates to false, the activity state
changes to stopped (9b) and not to finished. If an expiration
is defined for the activity, an administrator of the activity or an
enclosing scope or process can reschedule (21) when it expires without
changing the state of the activity.

The wait or receive activity might fail before the start of the
activity completes, for example, when the evaluation of the wait time
of a wait activity fails. If the Continue On Error setting
is set to yes or the fault is handled by a fault
link or fault handler on the enclosing scope, the failure causes the
activity state to change to failed (6) before it can reach the waiting
state.

While the activity is in the waiting state, the enclosing
process might receive a terminate request, or a fault occurs in a
branch that is parallel to the wait or receive activity. If any of
these events occur, the wait or receive activity is terminated, and
the state of the activity changes to terminated (5).

A wait
or receive activity can be skipped while it is in the waiting state.
The state of the activity changes immediately to the skipped state
(20). In this case, the transition conditions of the links that leave
the activity are evaluated.

## State transition diagram for pick (receive
choice) activities

The states and state transitions for
pick activities (also known as receive choice activities) are shown
in the following state diagram.

For pick activities,
the states and state transitions (1) through (6), and the transitions
to and from the stopped and skipped states are the same as for receive
activities.

In addition, a pick activity can expire when the
on-alarm branch of a waiting pick activity is activated before a request
for the pick activity arrives. The activity is then in the expired
state (7).

## State transition diagram for invoke activities

For
invoke activities, the state diagrams depend on whether the corresponding
service is invoked synchronously or asynchronously. The following
diagram shows the states and the state transitions that can occur
during the lifecycle of an invoke activity with an asynchronous implementation.
The implementation is asynchronous if the service reply happens in
a subsequent transaction to the service request transaction.

The activation
of an invoke activity is the same as the activation of all of the
other activity types (1), (2).

When an invoke activity runs
normally through to completion, the activity is started and the state
changes to running (3). If the service invocation returns successfully,
the activity is put into the finished state (4).

As long as
the service has not replied or the activity is in the stopped state,
an administrator can force retry or force complete the activity. This
can be useful if the service cannot reply, for example, because of
a system outage. The state transitions from running to stopped (9),
failed (8), and finished (4) can also be caused by the corresponding
API.

As with all other activities, an invoke activity can stop
(9). It can then be repaired by administrative actions or terminated
because the enclosing scope or process is also terminated (13).

Activities
in the running state can expire if expiration is defined for the activity.
The activity state is then expired (7) and a timeout fault is thrown.
This fault can be handled by a fault handler.

If the enclosing
scope of the activity is terminated, for example, because of a failure
in a parallel path in the process, and the activity is in the running
state, the activity is also terminated and put into the terminated
state (5).

- The running state for invoke activities with synchronous service
calls is never visible.
- Expiration is not applicable for invoke activities with synchronous
calls; the expired  state can never be reached.
- An invoke activity with a synchronous service call is never terminated.

## State transition diagram for human task
activities with single or sequential ownership

<!-- image -->

The runtime
behavior of a human task activity is similar to that of an invoke
activity. The running state of an invoke activity corresponds to the
ready and claimed states of a human task activity. The ready state
indicates that the activity is available to be worked on by a person.
When someone claims the activity to work on it, the activity is put
into the claimed state (15).

The person working on the activity
provides the information that is required and completes the activity.
The activity is then in the finished, failed, or stopped state. Alternatively,
the person who claimed the activity might decide that it cannot be
completed. The person then releases the activity for someone else
to work on. In this case, the activity is returned to the ready state
(16).

A human task activity can be skipped while it is in the
ready or claimed state. In both cases, the state changes to skipped
and the inline human task is terminated. In the following navigation
step, the transition conditions of the links leaving the activity
are evaluated.

The other state transitions are the same as for
invoke activities with asynchronous service calls.

## State transition diagram for human task
activities with parallel ownership

The state diagram for
tasks with parallel ownership is similar to the state diagram for
asynchronous invoke activities. The human task activity is put into
the running state when the activity is activated. When all of the
required potential owners have completed their work, the activity
is finished. The ready and claimed states are not used for activities
associated with a task with parallel ownership.

<!-- image -->