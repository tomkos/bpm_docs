# Limitations of the JMS, MQ JMS, and generic JMS bindings

## Implications of generating default bindings

The limitations of using the JMS, MQ JMS, and generic
JMS bindings are discussed in the following sections:

- Implications of generating default bindings
- Response correlation scheme
- Bidirectional support

When
you generate a binding, several fields will be filled in for you as
defaults, if you do not choose to enter the values yourself. For example,
a connection factory name will be created for you. If you know that
you will be putting your application on a server and accessing it
remotely with a client, you should at binding creation time enter
JNDI names rather than take the defaults since you will likely want
to control these values through the administrative console at run
time.

However, if you did accept the defaults and then find
later that you cannot access your application from a remote client,
you can use the administrative console to explicitly set the connection
factory value. Locate the provider endpoints field in the connection
factory settings and add a value such as <server\_hostname>:7276
(if using the default port number).

## Response correlation scheme

If you use the
CorrelationId To CorrelationId response correlation scheme, used to
correlate messages in a request-response operation, you must have
a dynamic correlation ID in the message.

To create a dynamic
correlation ID in a mediation module using the mediation flow editor,
add a Mapping mediation primitive before the import with the JMS binding.
Open the mapping editor. The known service component architecture
headers will be available in the target message. Drag a field containing
a unique ID in the source message onto the correlation ID in the JMS
header in the target message.

## Bidirectional support

Only ASCII characters
are supported for Java™ Naming
and Directory Interface (JNDI) names at run time.

## Shared receive queues

- Each import binding must have a different receive queue because
the import binding assumes all messages on the receive queue are responses
to requests that it sent. If the receive queue is shared by more than
one import, responses could be received by the wrong import and will
fail to be correlated with the original request message.
- Each export should have a different receive queue, because otherwise
you cannot predict which export will get any particular request message.
- Imports and exports can point to the same send queue.