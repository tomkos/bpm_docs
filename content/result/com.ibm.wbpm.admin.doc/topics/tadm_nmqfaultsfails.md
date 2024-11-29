# Troubleshooting WebSphere MQ bindings

## Primary failure conditions

The
primary failure conditions of WebSphere MQ bindings are
determined by transactional semantics, by WebSphere MQ
configuration, or by reference to existing behavior in other components.
The primary failure conditions include:

- Failure to connect to the WebSphere MQ queue manager
or queue. A failure to connect to WebSphere MQ
to receive messages will result in the MDB Listener Port failing to
start. This condition will be logged in the WebSphere Application
Server log. Persistent
messages will remain on the WebSphere MQ queue until they
are successfully retrieved (or expired by WebSphere MQ). 
A
failure to connect to WebSphere MQ to send outbound
messages will cause rollback of the transaction controlling the send.
- Failure to parse an inbound message or to construct an outbound
message. A failure in the data binding causes rollback of the transaction
controlling the work.
- Failure to send the outbound message.A failure to send a message
causes rollback of the relevant transaction.
- Multiple or unexpected response messages. The import expects
only one response message for each request message. If more than
one response arrives, or if a late response (one for which the SCA
response expiration has expired) arrives, a Service Runtime Exception
is thrown. The transaction is rolled back, and the response message
is backed out of the queue or handled by the failed event manager.

## Misusage scenarios: comparison with WebSphere MQ
JMS bindings

The WebSphere MQ import and export
are principally designed to interoperate with native WebSphere MQ
applications and expose the full content of the WebSphere MQ
message body to mediations. The WebSphere MQ
JMS binding, however, is designed to interoperate with JMS applications
deployed against WebSphere MQ, which exposes messages according
to the JMS message model.

The following scenarios should be
built using the WebSphere MQ JMS binding, not the WebSphere MQ binding:

- Invoking a JMS message-driven bean (MDB) from an SCA module, where
the MDB is deployed against the WebSphere MQ
JMS provider. Use a WebSphere MQ JMS import.
- Allowing the SCA module to be called from a Java EE component
servlet or EJB by way of JMS. Use a WebSphere MQ
JMS export.
- Mediating the contents of a JMS MapMessage, in transit across WebSphere MQ. Use a WebSphere MQ
JMS export and import in conjunction with the appropriate data binding.

There are situations in which the WebSphere MQ
binding and WebSphere MQ JMS binding might be expected
to interoperate. In particular, when you are bridging between Java
EE and non-Java EE WebSphere MQ applications,
use a WebSphere MQ export and WebSphere MQ
JMS import (or vice versa) in conjunction with appropriate data bindings
or mediation modules (or both).

## Undelivered messages

If WebSphere MQ cannot deliver a message to
its intended destination (because of configuration errors, for example),
it sends the messages instead to a nominated dead-letter queue.

In
doing so, it adds a dead-letter header to the start of the message
body. This header contains the failure reasons, the original destination,
and other information.

## MQ-based SCA messages not appearing in the failed
event manager

If SCA messages originated because of a WebSphere
MQ interaction failure, you would expect to find these messages in
the failed event manager. If these messages are not showing in the
failed event manager, check that the underlying WebSphere MQ destination
has a maximum failed deliveries value greater than 1. Setting this
value to 2 or more allows interaction with the failed event manager
during SCA invocations for the WebSphere MQ bindings.

## MQ failed events are replayed to
the wrong queue manager

When a predefined connection factory
is to be used for outbound connections, the connection properties
must match those defined in the activation specification used for
inbound connections.

The predefined connection factory is used
to create a connection when replaying a failed event and must therefore
be configured to use the same queue manager from which the message
was originally received.