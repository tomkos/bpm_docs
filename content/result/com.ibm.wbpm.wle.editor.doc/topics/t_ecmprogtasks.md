# Performing modeling tasks for inbound events

## About this task

- An event subscription for the process application
- An attached service for the event subscription that will
invoke the Content undercover agent (UCA)
- A Content UCA to trigger a content event
- A content event for the process
or business process definition (BPD), such as a content start
or intermediate event, which will catch or throw interactions with
an ECM server.

Although information about creating the required components
is found in the modeling topics below, it is generally recommended
to use an end-to-end approach where you create all of the components
at the same time. This is a simpler approach than creating each component
separately on a stand-alone basis and it automatically creates some
resources that you would otherwise need to create manually.

- Subscribing to document and folder events

To detect and respond to document and folder events that are produced when content changes occur on an Enterprise Content Management (ECM) server, you must create several components in the Process Designer. Using this end-to-end approach, you will find that creating the required components is more automated and less complex than creating them one at a time on a stand-alone basis.
- Subscribing to document and folder events using the desktop Process Designer (deprecated)

To detect and respond to document and folder events that are produced when content changes occur on an Enterprise Content Management (ECM) server, you need to create several components in the desktop  Process Designer. Using the end-to-end approach described in this topic, you will find that creating the required components is more automated and less complex than creating them one at a time on a stand-alone basis.
- Content event types

When you configure an event subscription in Process Designer, you must specify the type of content event that you want to receive when a specific content change occurs on an Enterprise Content Management (ECM) server. For example, if you want an event to be received when a user creates a document on an ECM server, you would select the Created event type.
- Creating attached services

To enable an event subscription to respond to events from your Enterprise Content Management server, you need to create an attached service that can be used to invoke a content undercover agent (UCA).
- Creating and configuring an undercover agent for a content event

To obtain information about document or folder events on an Enterprise Content Management (ECM) server, you must create and configure a content undercover agent that works with your event subscription. A content undercover agent (UCA) is used to initiate a start or intermediate event when specific content changes occur on an ECM server. It is conceptually similar to a message undercover agent, but it has a specialized content marker to differentiate it from a message marker.
- Adding a content event to a process

In a process, a content event is used to catch or throw interactions with an enterprise content management (ECM) system. You can add one of several types of content events, such as a start event, intermediate event, boundary event, or event subprocess start event.
- The ECMContentEvent business object

The ECMContentEvent business object is included in the Content Management toolkit, which is used to gain access to Enterprise Content Management (ECM) types and services. The resources of the toolkit are required to allow a business process developed in Process Designer to work with an Enterprise Content Management system. The ECMContentEvent business object is used to pass generic ECM event data to an event subscription service and content undercover agent (UCA). The business object is passed unchanged as BPMN event data into the process if it is not modified, mapped, or replaced by the service or UCA.