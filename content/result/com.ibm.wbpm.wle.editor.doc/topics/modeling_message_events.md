# Modeling message events

Incoming messages can originate from a message event in a process, from
starting an undercover agent (UCA) in a service from a Service Component Architecture (SCA) service,
from a web service that you create, or from a message that you post to the JMS Listener. If you want
to create web services to initiate inbound requests from external systems, see Publishing IBM Business Automation Workflow web services.

If you want to post a message to the JMS Listener, the Event Manager has a
defined XML message structure that it must receive from an external system. For more information
about the required message structure, see Posting a message to IBM Business Automation Workflow Event Manager.

Outgoing messages can be received by a message event in a process, can be sent to call an
external service, or can be received by the start event in another process or processes. To learn
how to configure message events to send messages, see Using intermediate message events and message end events to send messages.

You can include the following types of message events in your process:

| Event type         | Implementation                                                                 | When to use                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Start event        | Message that is configured to receive (Start events can only receive messages) | Use to model the start of a process if you want an incoming message event to kick off the process. A process can include more than one start message event.Use as the start event for an event subprocess when you want the event subprocess to be triggered upon receipt of a message.                                                                                                                          |
| Intermediate event | Message that is configured to receive                                          | Use to receive a message event. Intermediate events can be attached to activities within your process or they can be included in the process flow, which is connected with sequence flows. An intermediate event that is attached to an activity, rather than the swimlane, is known as a boundary event. Boundary events can optionally either interrupt and complete the activity, or be triggered repeatedly. |
| Intermediate event | Message that is configured to send                                             | Use to send a message event. Intermediate events can be included in the process flow, which is connected with sequence flows.                                                                                                                                                                                                                                                                                    |
| End event          | Message that is configured to send (End events can only send messages)         | Use to send a message event at the end of a path.                                                                                                                                                                                                                                                                                                                                                                |

When you create a message event, you can cut and paste or copy and paste that message event
within the same process or from one process into another process. A message can cause a process
instance to be created, and can be received by a running process that contains one or more
appropriate message events.

Before you include any type of message event that uses an undercover agent as the triggering
mechanism, you should be aware of the following:

- You can configure message events to consume messages. If you do, when a message is delivered to
a running process, the message is consumed by the first message event in the process that can accept
it (as determined by the undercover agent that is attached to the message event). When a message is
consumed, it will not be processed again by that message event, or any other message event in the
process instance that can accept it, should the execution of the process instance loop back and
reach the same message event(s). If a new instance of the message is delivered to the process
instance, this message is available for consumption again and is accepted by the message event.
- Message events can be used to enable roll-forward scenarios in which the same message needs to
be passed through multiple steps until it reaches the appropriate step in the process where it is to
be consumed. To enable rolling a message forward through multiple message events, enable the Consume
Message option only for the last message event in the chain of roll-forward message events. You can
also use conditions to further control message consumption.
- Occasionally, you might need to set conditions on the processing of incoming messages. If the
condition that you specify evaluates to true, the message is accepted and processing
continues-otherwise, it is stopped. Because the message condition is evaluated before the message
values can be passed to the input variables of the process definition, the message values are passed
to the condition in a special namespace, tw.message. If the message condition
evaluates to true, the values are passed from the tw.message namespace to the
process input variables.

- Using start message events

If you want a process or event subprocess to start when a message is received, use a Start Message Event in your process or your event subprocess.
- Using intermediate and boundary message events to receive messages

You can include an intermediate message event in your process when you want to model a message event that is received during execution of a process. When the process execution reaches an intermediate message event, if a matching message is stored in the system, it is passed to the message event, otherwise, further execution along that path is blocked until an incoming message arrives that matches.
- Using intermediate message events and message end events to send messages

You can include an intermediate message event in your process when you want to model a message event that is sent during execution of a process, or a message end event when you want to send a message at an end of a path.
- Using message end events

You can use a message end event when you want to send a message at an end of a path.