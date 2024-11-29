# Undercover agents

An undercover agent is started by an event. For example, when a
message event is received from an external system, an undercover agent
is needed to start the appropriate service in response to the message.

- processes
- web services that you create
- messages that you post to the JMS listener

When an undercover agent runs, it starts a service or process in response to the event.

When you use message event or a content event, you must attach an undercover agent to the event.
For example, when a message event is received from an external system, an undercover agent is needed
to trigger the message event in a process in response to the message.

If you want to run the startBpdWithName application programming interface
(API) to start a process instance inside an undercover agent, set the
<enable-start-bpd-from-uca> property to true in the
100Custom.xml file or another override file. Restart the product, and check the
TeamworksConfiguration.running.xml file to ensure that the setting has the
appropriate value. The property is set to false by default, and if you don't change it, you might
have errors that prevent the process from starting.

- Creating and configuring an undercover agent for a message event

You can create an undercover agent (UCA) that invokes a particular service as the result of an incoming or an outgoing message event.
- Creating and configuring an undercover agent for a scheduled message event

You can create an undercover agent (UCA) that invokes a service as the result of a message event that occurs on a regular schedule.
- Creating and configuring an undercover agent for a content event

To obtain information about document or folder events on an Enterprise Content Management (ECM) server, you must create and configure a content undercover agent that works with your event subscription. A content undercover agent (UCA) is used to initiate a start or intermediate event when specific content changes occur on an ECM server. It is conceptually similar to a message undercover agent, but it has a specialized content marker to differentiate it from a message marker.
- Setting the target for a UCA message event

While you are configuring an undercover agent (UCA) message event in a process or BPD or configuring an Invoke UCA step in a service to use a message event, you can exercise some control over which snapshots use the event. You can override the default target by selecting a check box in the implementation settings for the UCA that carries the event.