<!-- image -->

# Mediation flows

A mediation flow is created in the Mediation
Flow editor by including a number of mediation primitives that define
processing steps. Connections represent the flow of the message between
the mediation primitives.

- A request flow begins with a single input node for the source
operation, followed by one or more mediation primitives in sequence
and optionally a callout node for each target operation, all wired
together. If a message is to be returned to the source directly after
processing, it can be wired to an input response node in the request
flow. If fault messages are defined in the source operation, an input
fault node is also created.

- A response flow begins with a callout response node for each target
operation, followed by one or more mediation primitives in sequence
and a single input response node representing the source operation,
all wired together. If fault messages are defined in the source operation,
an input fault node is also created.  If fault messages are defined
in the target operation, a callout fault node is also created. Errors
that are returned by the operation but are not defined as fault messages
are propagated to the fail terminal of the callout response node.
Response flows for request-only operations consist of a callout response
node that has a fail terminal to handle faults, and no output terminal.
- Within the request and response flows, you can invoke a service
inline within the flow. This operation sends a message outside the
flow and waits for its return before continuing. This is done through
the Service Invoke primitive.
- An error flow begins with a single input node for the source operation,
followed by one or more mediation primitives in sequence or a subflow
and optionally an input response node that can be used to return the
error message to the source. You can use an error flow to capture
any unhandled exception.

When multiple targets return a response, the returning
messages are processed into a single message, which is then returned
to the source.

In a mediation flow, you can re-use logic that
has been pre-configured as a mediation subflow.