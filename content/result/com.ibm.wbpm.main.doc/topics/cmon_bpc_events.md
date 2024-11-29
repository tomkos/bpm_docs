<!-- image -->

# Business Process Choreographer events

- Business process events

Events are emitted for BPEL processes if monitoring is requested for the BPEL process elements in IBM Integration Designer. A process can cause process events, activity events, activity scope events, link events, and variable events to be emitted.
- Extension names for business process events

The extension name indicates the payload of the event. A list of all the extension names for business process events and their corresponding payload can be found here.
- Structure of BPEL process events for AuditLog

The Audit Log State Observer is one of the creators of BPEL process events. It stores the events into a database table (AUDIT\_LOG\_T) that you can see in the AUDIT\_LOG database view.
- Human task events overview

Events that are emitted on behalf of human tasks consist of situation-independent data and data that is specific to human task events. The attributes and elements that are specific to human task events are described.