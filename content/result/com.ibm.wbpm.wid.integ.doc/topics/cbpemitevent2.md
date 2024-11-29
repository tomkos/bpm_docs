<!-- image -->

# When not to use an Event Emitter

In the following example flow, two event emitter primitives are used in
the main path of the flow. The first event emitter will always run to notify
that a message has been logged. The second event emitter will frequently be
run to notify that the message has been routed to a service in the normal
path of the flow. Both event emitters run in frequently used
normal branch conditions of the flow.

<!-- image -->