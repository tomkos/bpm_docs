<!-- image -->

# Generic JMS bindings overview

## Generic JMS bindings

- Listener port: enables non-JCA-based JMS providers to receive
messages and dispatch them to a Message Driven Bean (MDB)
- Connections: encapsulate a virtual connection between a client
and a provider application
- Destinations: used by a client to specify the target of messages
it produces or the source of messages it consumes
- Authentication data: used to secure access to the binding

## Generic JMS import bindings

Generic JMS
import bindings allow components within your SCA module to communicate
with services provided by external non-JCA 1.5-compliant JMS providers.

The
connection part of a JMS import is a connection factory. A connection
factory, the object a client uses to create a connection to a provider,
encapsulates a set of connection configuration parameters defined
by an administrator. Each connection factory is an instance of the ConnectionFactory, QueueConnectionFactory,
or TopicConnectionFactory interface.

Interaction
with external JMS systems includes the use of destinations for sending
requests and receiving replies.

Two types of usage scenarios
for the Generic JMS import binding are supported, depending on the
type of operation being invoked:

- One-way: The Generic JMS import puts a message on the send destination
configured in the import binding. Nothing is sent to the replyTo field
of the JMS header.
- Two-way (request-response): The Generic JMS import puts a message
on the send destination and then persists the reply it receives from
the SCA component. The receive destination is
set in the replyTo header property of the outbound
message. A message driven bean (MDB) is deployed to listen on the
receive destination, and when a reply is received, the MDB passes
the reply back to the component. 
The import binding
can be configured (using the Response correlation scheme field
in Integration Designer)
to expect the response message correlation ID to have been copied
from the request message ID (the default) or from the request message
correlation ID.

For both one-way and two-way usage scenarios, dynamic and
static header properties can be specified. Static properties can be
set from the Generic JMS import method binding. Some of these properties
have special meanings to the SCA JMS runtime.

It is important
to note that Generic JMS is an asynchronous binding. If a calling
component invokes a Generic JMS import synchronously (for a two-way
operation), the calling component is blocked until the response is
returned by the JMS service.

Figure 1 illustrates
how the import is linked to the external service.

Figure 1. Generic JMS import binding
resources

<!-- image -->

## Generic JMS export bindings

Generic JMS
export bindings provide the means for SCA modules to provide services
to external JMS applications.

The connection part of a JMS export
is composed of a ConnectionFactory and a ListenerPort.

- The receive destination is where the incoming
message for the target component should be placed.
- The send destination is where the reply will
be sent, unless the incoming message has overridden this using the replyTo header
property.

An MDB is deployed to listen to requests incoming to the receive destination
specified in the export binding.

- The destination specified in the send field
is used to send the reply to the inbound request if the invoked component
provides a reply.
- The destination specified in the replyTo field
of the incoming message overrides the destination specified in the send field.
- For request/response scenarios, the import binding can be
configured (using the Response correlation scheme field
in Integration Designer)
to expect the response to copy the request message ID to
the correlation ID field of the response message
(default), or the response can copy the request correlation
ID to the correlation ID field of the
response message.

Figure 2 illustrates
how the external requester is linked to the export.

Figure 2. Generic JMS export binding
resources

<!-- image -->