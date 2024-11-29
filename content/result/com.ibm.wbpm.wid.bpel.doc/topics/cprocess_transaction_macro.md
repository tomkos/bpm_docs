<!-- image -->

# Transactional behavior of long-running BPEL processes

- Overview
- Influencing transaction boundaries
- Concurrent navigation of parallel branches in flow activities
- Concurrent navigation of branches of a parallel forEach activity
- Invoked services and transactions in long-running processes
- Recovery from transaction failures
- Recovery of a successful service invocation when a transaction rolls back
- Recovery of a service invocation that results in a runtime exception

## Overview

<!-- image -->

To
allow navigation across transaction boundaries, the states of the
process instance and its activity instances are persisted in the database.
You can influence transaction boundaries by using the transactional
behavior attribute. However, Business Process Choreographer can add
or remove transaction boundaries at any time.

- When waiting for an external request, that is, upon reaching a
receive activity or pick activity (also known as a receive choice
activity) in the process navigation for which a corresponding request
has not been received yet
- When scheduling a timer for a wait activity
- When invoking a service asynchronously using an invoke activity
- When invoking a human task activity

- When a fault is raised during process navigation
- Before and after an invoke activity is started that invokes a
service synchronously, and this service does not participate in the
transaction of the process
- When propagating lifecycle operations to child processes, for
example, when a parent process is suspended, its child processes are
suspended in subsequent transactions
- When the process instance is to be deleted automatically upon
completion of the process
- When trying to recover from a failure that causes the rollback
of a transaction spanning a series of activities
- Where specified using the transactional behavior attribute

- Your process design must not rely on these boundaries because
they can be overridden during process navigation, or they might change
in the future.
- The dynamic introduction of transaction boundaries can also influence
the behavior of APIs such as completeAndClaimSuccessor.
In this example, if a transaction boundary is dynamically introduced
in front of the next human task, then the API request returns without
claiming it.

## Influencing transaction boundaries

When
you model a business process, you can suggest transaction boundaries
for certain types of activities, such as, invoke, snippet, and human
task activities by changing the transactional behavior attribute of
the activity. The transactional behavior attribute is ignored if an
invoke activity calls a synchronous service that does not participate
in the current transaction. In this case, there is always a transaction
boundary before the invoke activity is started, and after the invoke
activity completes.

- If the invoke activity invokes the service asynchronously, the
arrival of the response message triggers a new transaction. The transaction
is short because it commits immediately after the status of the invoke
activity is updated.
- In a sequence of human task activities, two transactions are needed
for each human task activity, one to activate the human task activity
and another to complete the human task activity. If you change the
setting to Participates, you can reduce the number
of transactions to one for each human task activity. This is because
the completion of the previous human task activity, and the activation
of the following activity are performed in the same transaction.
- To enable server-controlled page flows that use the completeAndClaimSuccessor API.

- Set the attribute of the initiating receive or receive choice
activity to Commit after
- Set the attribute of the invoke activity to Commit before or Requires
own

## Concurrent navigation of parallel
branches in flow activities

To achieve concurrency in the
navigation of parallel branches in a flow activity, a new transaction
boundary is needed at the beginning of each branch so that each parallel
activity is processed in a separate transaction. This means that the
transactional behavior attribute of the first activity of each parallel
branch must be set to Commit before or Requires
own to achieve parallelism from the beginning of the flow.

## Concurrent navigation of branches
of a parallel forEach activity

The processing of each branch
of a parallel forEach activity is started in its own, separate transaction.
Thus parallel execution of these branches is enabled.

## Invoked services and transactions
in long-running processes

A service that is called within
a long-running process using an invoke activity can either participate
in the current transaction of the long-running process, or it can
run in its own transaction.

- The interaction style that is used to call the service.The
interaction style can be synchronous or asynchronous. The style is
determined by the preferred interaction style of the target SCA component
or SCA import, as shown in the following table:
Table 1. 

Preferred interaction style of target component
or import 
One-way operation 
Request-response operation 

Any
Asynchronous invocation
Asynchronous invocation

Synchronous
Synchronous invocation
Synchronous invocation

Asynchronous
Asynchronous invocation
Asynchronous invocation
- The Service Component Architecture (SCA) transaction qualifiersthat are specified for the process and the service that is called:
    - The suspendTransaction qualifier on the reference
of the process component specifies whether the transaction context
of the process is propagated to the services to be invoked.
    - The joinTransaction qualifier on the service
interface specifies whether a service participates in the transaction
of its caller if a transaction is propagated. Depending on the
settings of the interaction style and the SCA qualifiers, the following
rules apply to the invoked service:

Synchronous invocation

 joinTransaction
suspendTransaction = true
suspendTransaction = false

 joinTransaction = true
The service does not participate in the transaction
of the long-running process
The service participates in the transaction
of the long-running process

 joinTransaction = false
The service does not participate in the transaction
of the long-running process
The service does not participate in the transaction
of the long-running process

If a service participates in the current transaction of
the long-running process, the changes that are made by the service
to the transactional resources are persisted only if the current transaction
commits.

Asynchronous invocation
The service always runs in its own transactions.

## Recovery from transaction failures

- A server outage, for example, because of a power failure. The
transaction is rolled back when the server is restarted.
- A failure in the Business Process Choreographer infrastructure,
for example, a deadlock that causes a successful service invocation
to roll back. Business Process Choreographer uses its internal queues
to handle the failure. For more information, see Recovery of a successful service invocation when a transaction rolls back
- A rollback enforced by a service that was called from the process.
For more information, see Recovery of a service invocation that results in a runtime exception.

## Recovery of a successful service invocation
when a transaction rolls back

The recovery behavior depends
on whether the called service participates in the current transaction.

An
invoke activity calls a service that participates in the current transaction.
The execution of the service is complete. If an error occurs after
completion of the service and the transaction is rolled back to the
state that the process was in before the transaction started, the
effect of the called service is also rolled back. When the transaction
is retried, the service is called again.

In contrast, if the
called service does not participate in the current transaction and
the called service returns a response, the response is stored in a
separate transaction. If an error occurs after the response is stored,
the current transaction is rolled back and the transaction is retried.
During the retry the service is not called again, however, the stored
response is restored and the navigation continues.

## Recovery of a service invocation
that results in a runtime exception

The subsequent
processing of the activity An depends on the value of the Continue
processing upon unhandled faults setting for the activity.