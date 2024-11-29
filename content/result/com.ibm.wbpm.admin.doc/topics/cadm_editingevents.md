<!-- image -->

# Working with data in failed events

To browse failed event data, click any failed event ID. The failed event manager displays the
data about the failed event data. For SCA events, you can edit the expiration and trace detail
information from this detail page. If an event contains business data, the detail page has an
Edit business data button. Click that button to open the business data
editor, where you can browse and edit the business data. Note that you can edit only simple data
types (for example, String, Long, Integer, Date, Boolean). If a data type is complex (for example,
an array or a business object), you must navigate through the business data hierarchy until you
reach the simple data types that make up the array or business object. Refer to the online help in
the failed event manager for more information about viewing and editing this data.

## Data associated with the failed event

- The event ID, type, and status
- The time the event failed
- The deployment target associated with the event

- Business Process Choreographer
- Business Flow Manager hold queue
- JMS
- SCA
- WebSphere MQ

| Event type                              | Available data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SCA events                              | The session ID The type of service invocation used between SCA components The names of the module and component from which the event originated (the source) The names of the destination module, component and method for the event Whether an event sequencing qualifier has been declared for this event The destination module where the event has been or will be resubmitted The correlation ID, if one exists The exception thrown when the event failed The expiration date for resubmitted events (this data can be edited) The trace control set for the event (this data can be edited)                                                  |
| JMS events                              | The type of service invocation used The names of the destination module, component and method for the event The exception thrown when the event failed The destination module where the event has been or will be resubmitted The correlation ID, if one exists The expiration date for resubmitted events (this data can be edited) The JMS-specific properties associated with the failed event:  The message type and priority The JMS destination The delivery mode Redelivery data, including the redelivered count and redelivered indicator (true or false) The destination replies are sent to for request-response or two-way interactions |
| WebSphere MQ events                     | The type of service invocation used The names of the destination module, component and method for the event The exception thrown when the event failed The destination module where the event has been or will be resubmitted The correlation ID, if one exists The expiration date for resubmitted events (this data can be edited) The WebSphere MQ-specific properties associated with the failed event:  The message type, format, and priority The WebSphere MQ destination The delivery mode Redelivery data, including the redelivered count and redelivered indicator (true or false) The reply-to queue and queue manager                  |
| Business Process Choreographer events   | The names of the destination module and component for the event The process instance name associated with the event The process ID associated with the event                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Business Flow Manager hold queue events | The process instance ID (if the process instance does not exist, 0 is returned) The name and state of the process instance The name of the associated process template The activity instance name and ID The activity template ID                                                                                                                                                                                                                                                                                                                                                                                                                   |

## Business data

SCA and Business Process Choreographer failed events typically include business data. Business
data can be encapsulated in a business object, or it can be simple data that is not part of a
business object. Business data for SCA failed events can be edited with the business data editor
available in the failed event manager.