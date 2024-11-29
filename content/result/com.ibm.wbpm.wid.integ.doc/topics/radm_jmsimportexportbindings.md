# JMS import and export bindings

## JMS import bindings

Connections to the associated
JMS provider of JMS destinations are created by using a JMS connection
factory. Use connection factory administrative objects to manage JMS
connection factories for the default messaging provider.

Interaction
with external JMS systems includes the use of destinations for sending
requests and receiving replies.

Two types of usage scenarios
for the JMS import binding are supported, depending on the type
of operation being invoked:

- One-way: The JMS import puts a message on the send destination
configured in the import binding. Nothing is set in the replyTo field
of the JMS header.
- Two-way (request-response): The JMS import puts a message
on the send destination and then persists the reply it receives
from the SCA component. The import binding can be configured (using
the Response correlation scheme field in Integration Designer) to expect
the response message correlation ID to have been copied from the request
message ID (the default), or from the request message correlation
ID. The import binding can also be configured
to use a temporary dynamic response destination to correlate responses
with requests. A temporary destination is created for each request
and the import uses this destination to receive the response.
The receive destination
is set in the replyTo header property of the outbound
message. A message listener is deployed to listen on the receive destination,
and when a reply is received, the message listener passes the
reply back to the component.

For both one-way and two-way usage scenarios, dynamic and
static header properties can be specified. Static properties can
be set from the JMS import method binding. Some of these properties
have special meanings to the SCA JMS runtime.

It is important
to note that JMS is an asynchronous binding. If a calling component
invokes a JMS import synchronously (for a two-way operation), the
calling component is blocked until the response is returned by the
JMS service.

Figure 1 illustrates how the import is linked to the external service.

Figure 1. JMS import binding resources

<!-- image -->

## JMS export bindings

JMS export bindings
provide the means for SCA modules to provide services to external
JMS applications.

The connection that is part of a JMS
export is a configurable activation specification.

- The receive destination is where the incoming
message for the target component should be placed.
- The send destination is where the reply will
be sent, unless the incoming message has overridden this
using the replyTo header property.

A message listener is deployed to listen to requests incoming
to the receive destination specified in the export
binding. The destination specified in the send field
is used to send the reply to the inbound request if the invoked component provides
a reply. The destination specified in the replyTo field
of the incoming message overrides the destination specified
in the send.

Figure 2 illustrates how the external requester is linked to the export.

Figure 2. JMS export binding resources

<!-- image -->