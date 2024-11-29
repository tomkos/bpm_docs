<!-- image -->

# Dealing with faults in your BPEL process

A fault is any exceptional condition that can change the normal
processing of a BPEL process and, if not handled, can lead to unexpected
conditions or results. A well designed process is one that anticipates
possible faults with fault handlers that are designed to lead to predictable
outcomes. To this end, when you are planning your process, you will
need to be able to anticipate as many potential control issues as
possible, predict what the result of the exception will be, and what
action must take place.

- Use a terminate activity to stop the execution of a process or
an activity altogether so that somebody can step in and make the necessary
repairs.
- Use a reply activity with a fault name associated with it so that
it will respond with a fault.
- Use a throw activity to signal an internal fault.
- Use a fault handler to catch a fault and attempt to deal with
it.
- Use compensation to rollback or "undo" a process that has failed
after committing either itself as a whole (a microflow) or at least
one of its activities (a long-running process).

## Business faults

Business faults are exceptions
that are known and declared within the application. These faults occur
at specific points in a BPEL process because of application issues,
for example, because of data content problems. The fault can be the
result of a business rule violation, or a constraint violation. For
example, invoking a bank service to transfer funds can result in an
insufficient-funds fault.

When a business fault occurs, the
transaction is not rolled back, and failed events are also not produced.
So, when you design a process, you must define fault handlers to deal
with business faults.

In the SCA programming model, business
faults are propagated by ServiceBusinessException objects.

## System faults

These faults can occur because
of system-related issues, such as the unavailability of a service,
or a network failure. These faults are unexpected and they can occur
at anytime when a process runs. They can trigger other system actions,
such as transaction rollback, failed events, and log entries.

These
failures can be short-term, such as a temporary disconnection from
the network, or long-term failures, such as a disk failure. To resolve
short-term failures, you can sometimes use failure-handling logic,
such as retries. Long-term failures might require human intervention
to correct the system failure, followed by a recovery mechanism.

In
the SCA programming model, system faults are propagated by ServiceRuntimeException
objects.

## Standard Faults

The web services Business
Process Execution Language (WS-BPEL) specification defines standard
fault types for common system failures. You can add these built-in
fault types to your process definition. These faults are only available
within BPEL processes and they do not have an equivalent In the SCA
programming model. Business Process Choreographer recognizes additional
error situations, resulting in the faults: bpc:timeout, bpc:serviceTerminated, bpc:runtimeFailure, bpc:splitFailure, bpc:cannotResolveEndpoint.

| Fault name                  | Description                                                                                                                                                                                                                                            |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| completionConditionFailure  | Thrown if upon completion of a directly enclosed scope activity within the forEach activity it can be determined that the completion condition can never be true.                                                                                      |
| conflictingReceive          | Thrown when more than one receive activity or its equivalent (currently, onMessage branch in a pick activity) is enabled simultaneously for the same partner link, port type, operation, and correlation sets.                                         |
| conflictingRequest          | Thrown when more than one synchronous inbound request on the same partner link for a particular port type, operation, and correlation sets are active.                                                                                                 |
| correlationViolation        | Thrown when the contents of the messages that are processed in an invoke, receive, or reply activity do not match the specified correlation information.                                                                                               |
| forcedTermination           | Thrown as the result of a fault in an enclosing scope.                                                                                                                                                                                                 |
| invalidBranchCondition      | Thrown if the integer value that is used in the branches completion condition of the forEach activity is larger than the number of directly enclosed scope activities.                                                                                 |
| invalidExpressionValue      | Thrown when an expression that is used within an forEach activity returns an invalid value with respect to the expected XML Schema type.                                                                                                               |
| invalidReply                | Thrown when a reply is sent on a partner link, portType, and operation for which the corresponding receive activity with the same correlation has not been carried out.                                                                                |
| joinFailure                 | Thrown when the join condition of an activity evaluates to false. You can suppress the fault by setting the process or activity attribute suppressJoinFailure to yes.                                                                                  |
| mismatchedAssignmentFailure | Thrown when incompatible types are encountered in an assign activity.                                                                                                                                                                                  |
| missingReply                | Thrown when an inbound message activity has run, and the process instance or scope instance reaches the end of its execution without a corresponding reply activity having run.                                                                        |
| repeatedCompensation        | Thrown when an installed compensation handler is invoked more than once.                                                                                                                                                                               |
| selectionFailure            | Thrown when a selection operation that is performed either in a function, such as bpws:getVariableData, or in an assignment, encounters an error. You can suppress the fault by setting the IBM® extension process attribute ignoreMissingData to yes. |
| uninitializedPartnerRole    | Thrown when an invoke activity or an assign activity references a partner link that has a partnerRole endpoint reference that is not initialized.                                                                                                      |
| uninitializedVariable       | Thrown when there is an attempt to access the value of an uninitialized part in a message variable. You can suppress the fault by setting the IBM extension process attribute ignoreMissingData to yes.                                                |

| Fault name            | Description                                                                                                                                                                                                                                                                                       |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cannotResolveEndpoint | Thrown if the endpoint of a process cannot be resolved, for example, when a process invokes a subprocess using late-binding and the interface of the subprocess has no export defined.                                                                                                            |
| runtimeFailure        | Thrown when an invoked service returns an SCA ServiceRuntimeException or the execution of a customer code snippet written in a sublanguage (XPath or Java™) results in a runtime exception. For example, if the execution of a Java snippet activity results in a java.lang.NullPointerException. |
| serviceTerminated     | Thrown when a human task that is part of a business process is terminated by the user.                                                                                                                                                                                                            |
| splitFailure          | Thrown when an activity that is part of a generalized flow activity is completed, and the transition conditions of all outgoing links evaluate to false.                                                                                                                                          |
| timeout               | Thrown when an expiration is specified for an asynchronous service call in a long-running process, and a response is not received within the specified time.                                                                                                                                      |

- Fault activities

You can deal with potential faults in your BPEL process using a combination of the activities, handlers, and elements that are described in this topic.
- Using fault handlers

A fault handler is a collection of specific activities that run when a fault is thrown on the activity with which the handler is associated.
- Raising faults

You can raise faults in a BPEL process with throw and rethrow activities, or send a fault to the caller with a reply activity.
- Continue processing upon unhandled faults

The Continue processing upon unhandled faults setting determines how the process should proceed when a fault is not caught on the enclosing scope, or handled through a local fault handler.
- BPEL process compensation

Compensation is just another execution path of a process; it is coupled to fault handling in order to redress the operations that have already taken place.
- Typing fault variables

A fault variable stores data in the event of a standard or a system fault.
- Fault handling and compensation handling in BPEL processes

A fault is any exceptional condition that can change the normal processing of a BPEL process. A fault can be returned from a service invocation, raised explicitly by the process, or it can be system fault raised by the runtime environment. A well-designed process should consider faults, and handle them whenever possible. Compensation is one way of handling faults.