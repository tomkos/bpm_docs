<!-- image -->

# Best Practices: When to use an Event Emitter

Think of an Event Emitter as a notification mechanism that is used
to indicate an unusual event, such as a significant failure within
a flow or an unusual path ran in the flow. Avoid placing an Event
Emitter in the normal path of a flow as this could affect performance
by causing a large number of events to be generated.

In the following flow, an Event Emitter is used when there is a
failure in the message log, which is a significant failure in the
flow.

The following example shows an Event Emitter used to notify that
an unusual path has run in a flow.