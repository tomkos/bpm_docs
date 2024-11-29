<!-- image -->

# Scenarios for invoking tasks

## Invocation of task components using the
Human Task Manager API

- Stand-alone and inline invocation tasks
- Stand-alone to-do tasks
- Collaboration tasks

- Synchronous invocation of the task and the associated serviceThis
interaction style uses the callTask method. For
one-way operations, the invocation returns after triggering the execution
of the task and the service component. For request-response operations,
the invocation waits until the service and task are complete and the
result of the invocation is returned.
This style of interaction
can be applied to invocation tasks only.
- Asynchronous invocation of the task and the associated serviceThis
interaction style uses the startTask method. For
both one-way and request-response operations, the invocation returns
after triggering the execution of the task and the service component.
In addition, for request-response operations, the invocation returns
a result asynchronously that is stored as an output or fault message
in the context of the invocation task. The invoking API client must
retrieve the result programmatically using the API methods. Alternatively,
you can use a reply handler to ensure that the asynchronous response
is returned to the client as soon as the response becomes available. 
This
style of interaction can be applied to to-do, collaboration, and invocation
tasks.

The Human Task Manager API is provided as an Enterprise
JavaBeans (EJB) implementation, a web service implementation, a JMS
message implementation, and a REST implementation. The API methods
are similar for all implementations, but differ in their functional
scope.

## Invocation of to-do tasks as SCA service components

- Wires that connect an SCA client reference and the interface of
a component representing a to-do task
- SCA qualifier settings for component references and interfaces
that control aspects, such as interaction style, transaction behavior,
and interaction reliability

In addition, a stand-alone to-do task can be invoked by
an SCA client that is implemented as a BPEL process. In this case,
the connection must be considered on both the SCA and process levels.
Viewed on the SCA level, the SCA client reference is connecting to
the interface of an SCA service. Viewed on the process level, the
partner link of an invoke activity is connected to a to-do task.

## Invocation of inline to-do tasks

A to-do
task can be specified in the context of a human task activity in a
long-running BPEL process. In this case, the task does not have a
representation on the SCA level, instead it is part of the SCA component
representing the BPEL process. The task acts as a service provider
to the human task activity. Whenever the activity is reached during
process navigation, the to-do task is invoked asynchronously.

## Invocation of an SCA service with an invocation task

A
stand-alone invocation task serves as an access component to an associated
SCA service. The association with the service is defined on the SCA
level: the task represents an SCA client that is wired to an SCA service
component. The invocation of an invocation task involves both Human
Task Manager and SCA levels. The invocation task itself is invoked
by the Human Task Manager API, either synchronously or asynchronously.
The task (SCA client) then invokes the associated SCA service component
in the same way as the task was invoked.

- Wires that connect an SCA client reference and the interface of
a service component
- SCA qualifier settings for component references and interfaces
that control aspects, such as interaction style, transaction behavior,
and interaction reliability

In addition, a stand-alone invocation task can be connected
to an SCA component that is implemented by a BPEL process.

## Invoking a BPEL process through an inline invocation
task

An inline invocation task can be specified in the context
of a receive or pick activity, or an event handler in a BPEL process.
The task does not get a representation on the SCA level, instead it
is part of the SCA component that represents the BPEL process. Nonetheless,
the task acts as a client to the BPEL process. Whenever the task is
invoked by the Human Task Manager API, the task in turn invokes the
BPEL process in the same way as it was invoked.

- Factors affecting the behavior of stand-alone invocation tasks and their service components

You can use a stand-alone invocation task to run an Service Component Architecture (SCA) service component that is associated with the SCA component of the task. The association of the invocation task and service component is modeled at an SCA level by wiring the reference of the task component to the interface of the associated service component. A number of factors affect the behavior of the invocation task and its associated service component.
- Scenario: stand-alone invocation tasks that support the asynchronous invocations of services

This scenario considers the asynchronous invocations of tasks and services only. It describes the Service Component Architecture (SCA) settings and the expected transactional and fault behavior for this type of invocation.
- Scenario: stand-alone invocation tasks that support asynchronous and synchronous invocations of services

This scenario considers both the asynchronous and synchronous invocation of a task and its associated service. It describes the Service Component Architecture (SCA) settings and the expected transactional and fault behavior for these types of invocation.