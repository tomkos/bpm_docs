<!-- image -->

# Working with failed events in IBM Business Automation Workflow

Actions for handling failed events include examining the types of data associated with the event
(business, trace, or expiration data) to determine the cause of the failure. Actions also include
editing the data, resubmitting the event, or both.

- Service Component Architecture (SCA) events
- WebSphere® MQ events
- Java™ Message Service (JMS) events
- Business Process Choreographer events
- Business Flow Manager hold queue events

To view, modify, resubmit, or delete any failed event, the first step is to display the failed
event manager. Click Servers > Deployment Environments > deployment\_environment\_name > Failed Event Manager.

- Security considerations for recovery

If you have enabled security for your IBM Business Automation Workflow applications and environment, it is important to understand how role-based access and user identity affect the Recovery subsystem.
- Finding failed events

Use the failed event manager to help you search for failed events on all of the servers within the deployment environment. You can search for all failed events, or for a specific subset of events.
- Managing failed SCA events

When problems processing a Service Component Architecture (SCA) request or response message create a failed SCA event in the Recovery subsystem, you must decide how to manage that event. Use the information in this topic to help you identify and fix the error and clear the event from the Recovery subsystem.
- Managing failed JMS events

The Java Message Service (JMS) binding type and configuration determine whether a failed event is generated and sent to the failed event manager. When problems processing a JMS request or response message create a failed JMS event in the Recovery subsystem, you must decide how to manage that event. Use the information in this topic to help you identify and fix the error and clear the event from the Recovery subsystem.
- Managing failed WebSphere MQ events

A WebSphere MQ event might fail if there is a problem such as a data-handling exception in the WebSphere MQ binding export or import used by an SCA module. When problems processing a WebSphere MQ request or response message create a failed WebSphere MQ event in the Recovery subsystem, you must decide how to manage that event. Use the information in this topic to help you identify and fix the error and clear the event from the Recovery subsystem.
- Managing stopped Business Process Choreographer events

 Stopped events occur if a Business Process Execution Language (BPEL) instance encounters an exception and one or more activities enter the Stopped state. Use the failed event manager and Business Process Choreographer Explorer to manage stopped Business Process Choreographer events in any process state. You can view, compensate, or terminate the process instance associated with a stopped Business Process Choreographer event. In addition, you can work with the activities associated with the event, viewing, modifying, retrying, or completing them as appropriate.
- Managing Business Flow Manager hold queue messages

You can use the failed event manager to manage navigation messages that are stored in the Business Flow Manager hold queue. A navigation message might be stored in the hold queue if an infrastructure, such as a database, is unavailable or if the message is damaged.
- Working with data in failed events

Each failed event has data about the event to help you identify when and where the failure occurred, including the event ID and status, the time it failed, and its deployment target. In addition, some types of failed events contain business data. You can browse the data for all failed events. In some cases, you can edit the data before resubmitting the event.
- Resubmitting failed events in IBM Business Automation Workflow

You can resubmit a failed event in IBM Business Automation Workflow from the failed event manager. You can resubmit an event without changes, or, in some cases, you can edit the trace and expiration data or the business data before you resubmit the event. In addition, you can use the failed event manager to resubmit failed events with a process response qualifier to either the request queue or the response queue.
- Troubleshooting the failed event manager

You might encounter problems while using the failed event manager.
- Disabling communication with IBM Business Automation Insights

Disable communication to IBM Business Automation Insights to restore your IBM Business Automation Workflow environment.