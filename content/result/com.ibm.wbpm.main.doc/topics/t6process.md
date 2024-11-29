<!-- image -->

# Developing applications for BPEL processes

## About this task

- Microflows are short running BPEL processes that are
executed synchronously. After a very short time, the result is
returned to the caller.
- Long-running, interruptible processes are executed as
a sequence of activities that are chained together. The use of certain constructs
in a process causes interruptions in the process flow, for example, invoking
a human task, invoking a service using an synchronous binding, or using timer-driven
activities.Parallel branches of the process are usually navigated asynchronously,
that is, activities in parallel branches are executed concurrently. Depending
on the type and the transaction setting of the activity, an activity can be
run in its own transaction.

- Required roles for actions on BPEL process instances

Access to the BusinessFlowManager interface does not guarantee that the caller can perform all of the actions on a process. The caller must be logged on to the client application with a role that is authorized to perform the action.
- Required roles for actions on BPEL process activities

Access to the BusinessFlowManager interface does not guarantee that the caller can perform all of the actions on an activity. The caller must be logged on to the client application with a role that is authorized to perform the action.
- Managing the lifecycle of a BPEL process

A BPEL process instance comes into existence when a Business Process Choreographer API method that can start a process is invoked. The navigation of the process instance continues until all of its activities are in an end state. Various actions can be taken on the process instance to manage its lifecycle.
- Processing human task activities

Human task activities in business processes are assigned to various people in your organization through work items. When a BPEL process is started, work items are created for the potential owners.
- Processing a page flow that starts with the BPEL process

Some workflows are performed by only one person, for example, ordering books from an online bookstore. This type of workflow has no parallel paths. This example shows how to use the initiateAndClaimFirst and completeAndClaimSuccessor APIs to process this type of workflow.
- Sending a message to a waiting activity

You can use inbound message activities (receive activities, onMessage in pick activities, onEvent in event handlers) to synchronize a running process with events from the "outside world". For example, the receipt of an email from a customer in response to a request for information might be such an event.
- Handling events

An entire BPEL process and each of its scopes can be associated with event handlers that are invoked if the associated event occurs. Event handlers are similar to receive or pick activities in that a process can provide web service operations using event handlers.
- Analyzing the results of a process

A process can expose web services operations that are modeled as Web Services Description Language (WSDL) one-way or request-response operations. The results of long-running processes with one-way interfaces cannot be retrieved using the getOutputMessage method, because the process has no output. However, you can query the contents of variables, instead.
- Repairing activities

A long-running process can contain activities that are also long running. These activities might encounter uncaught errors and go into the stopped state. An activity in the running state might also appear to be not responding. In both of these cases, a process administrator can act on the activity in a number of ways so that the navigation of the process can continue.
- BusinessFlowManagerService interface

The BusinessFlowManagerService interface exposes business-process functions that can be called by a client application.