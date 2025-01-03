<!-- image -->

# Advanced events

Use the information presented in this section as reference material that enables you to
understand how individual events are structured. This knowledge helps you decipher the information
contained in each event, so that you can quickly identify the pieces of information you need from
the relatively large amount of data generated by each event.

Service components contain one or more elements, which are sets of different steps processed in
each service component. In turn, each element has its own set of event natures, that are key points
that are reached when processing a service component element. All service components, their elements
and associated event natures, and the extended data elements unique to each event are listed.

- The structure and standard elements of the Common Base Event
- The list of events for the Business Process Choreographer service components
- The list of IBM Business Automation Workflow-specific service components
- The extensions to the Common Base Event unique to each event type

When an event of a given type is fired across the Common Event Infrastructure bus to the CEI
server or to a logger, it takes the form of a Common Base Event - which is, essentially, an XML
encapsulation of the event elements created according to the event's specification. The Common Base
Event includes a set of standard elements, server component identification elements, Event
Correlation Sphere identifiers, and additional elements unique to each event type. All of these
elements are passed to the CEI server or logger whenever an event is fired by a service component
monitor, with one exception: if the event includes the business object code within the payload, you
may specify the amount of business object data that you want to include in event.

- Business objects in events

Business object data is carried within the event in XML format. The Common Base Event format (deprecated) includes an xs:any schema, which encapsulates the business object payload in XML elements. By default, events are no longer delivered in a Common Base Event wrapper.
- Business Process Choreographer events

IBM Business Automation Workflow  incorporates the Business Process Choreographer service components for BPEL processes and human tasks. Both BPEL processes and human tasks have their own set of event points that can be monitored.
- Binding events

The event types available for the IBM Business Automation Workflow bindings (JMS, JAX-WS, HTTP, EJB, and EIS) are listed.
- Business rule events

The event types available for the business rule component are listed.
- Business state machine events

The event types available for the business state machine component are listed.
- Map events

The event types available for the map component are listed.
- Mediation events

The event types available for the mediation component are listed.
- Recovery events

The event types available for the recovery component are listed.
- Service Component Architecture events

The event types available for the Service Component Architecture are listed.
- Selector events

The event types available for the Selector component are listed.