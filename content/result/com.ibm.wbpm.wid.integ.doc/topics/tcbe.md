<!-- image -->

# Emitting common base events

## About this task

When you create an Event Emitter primitive in a mediation
flow, you specify a label for the event, and the part of the message
that should be included in the event. At run time, when the Event
Emitter primitive runs the mediation flow, a common base event is
emitted, and the event label and message information is included in
the Extended Data Elements of the common base event.

Common
base events and event definitions can be used in a number of ways
and can be consumed by various IBM® products.

After you define a custom event in an Event
Emitter primitive, you can perform these tasks in IBM Integration
Designer:

- Generating event definitions

You can generate an event definition from an Event Emitter primitive. You can then test the event definitions in the integrated test client, or create a monitor model from the event definition.
- Choosing properties of an event

The name given in the Event Emitter primitive's Label property identifies the event to the event consumers; viewer and monitor applications. Use an event label that is meaningful and unique to that particular event, so that consumers of the event can process it effectively.
- Best Practices: When to use an Event Emitter

The Event Emitter primitive provides a way to generate significant business events from within a mediation flow.
- When not to use an Event Emitter

Consider where you place an Event Emitter in your flow, and what data you choose to be stored in the event. Avoid placing an Event Emitter in the normal run path of a flow as this could affect performance by causing a large number of events to be generated.
- Content of the Event Emitter primitive's event

The Event Emitter primitive defines the application specific event data that is placed into the extendedDataElements section of the common base event. This topic summarizes the mapping between the properties defined in the Event Emitter primitive and the elements of the common base event as formatted in V6.1 and later releases.