<!-- image -->

# Combining results from different services

## About this task

You use the Fan Out primitive to either fire a single
input message once or to iterate through the input message and fire
each occurrence of a given element, producing multiple output messages.

- Simple Count - fires the output terminal when a set number of
messages are received. The operation does not stop Fan Out from sending
messages which means the decision point may be reached, and the output
terminal may be fired, more than once.
- XPath Decision - output will be fired if XPath evaluation of messages
is true.
- Iterate - waits for all messages produced by the corresponding
Fan out primitive then fires the output terminal.

Important: For every Fan In primitive you use,
you must have a related Fan Out primitive.

To stop the Fan In
operation you can wire the Stop Input terminal. You can also specify
a time period in which the operation must complete. If the decision
point has not been met by this time, the Incomplete terminal will
fire and the Fan Out and Fan In operation will stop.

<!-- image -->

1. The shared context business object is set in the input node. The
Message Element Setter primitives, StoreReponse\_A and StoreResponse\_B
will place responses from InvokeService\_A and InvokeService\_B in the
shared context. The Fan In primitive will aggregate the contents of
the shared context and will fire the output terminal.
2. A Fan Out primitive is placed on the canvas and is configured
to fire its output only once.
3. When the Fan Out primitive fires, the message body and the transient
and correlation contexts are copied into a new message that is created
for each path coming from the output terminal. These messages still
point to the same shared context.
4. The message goes through the path to InvokeService\_A first. A
a Mapping primitive, CreateInput\_A, creates the input message in the
form that service A requires and propagates it to the Service Invoke
primitive.
5. The Message Element Setter primitive named StoreResponse\_A adds
the response from the service to the shared context after which the
response is propagated to the Fan in primitive.
6. Fan In has been configured to fire after it receives two messages
and has only received one. The flow backtracks to where the message
was split and then follows the path to InvokeService\_B.
7. Just like for InvokeService\_A, a Mapping primitive creates the
message for the service and a Message Element Setter primitive adds
the response from the service to the shared context.
8. When the path through service B completes and the Fan In primitive
receives the second message, the Fan In primitive fires its output
terminal. The shared context now contains the responses from service
A and B.
9. The last a Mapping primitive, CreateNewMessage, maps the contents
of the shared context to the body of the message as needed.