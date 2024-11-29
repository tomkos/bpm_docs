<!-- image -->

# WebSphere MQ JMS
bindings overview

## WebSphere MQ
administrative tasks

The WebSphere MQ
system administrator is expected to create the underlying WebSphere MQ Queue Manager,
which the WebSphere MQ
JMS bindings will use, before running an application containing these
bindings.

## WebSphere MQ
JMS import bindings

The WebSphere MQ
JMS import allows components within your SCA module to communicate
with services provided by WebSphere MQ
JMS-based providers. You must be using a supported version of WebSphere MQ. Detailed hardware
and software requirements can be found on the IBM® support
pages.

Two types of usage scenarios for WebSphere MQ JMS import bindings are supported, depending
on the type of operation being invoked:

- One-way: The WebSphere MQ
JMS import puts a message on the send destination configured in the
import binding. Nothing is sent to the replyTo field
of the JMS header.
- Two-way (request-response): The WebSphere MQ JMS import puts a message
on the send destination. The receive destination
is set in the replyTo header field. A message-driven
bean (MDB) is deployed to listen on the receive destination, and when
a reply is received, the MDB passes the reply back to the component.
The
import binding can be configured (using the Response correlation
scheme field in Integration Designer) to expect
the response message correlation ID to have been copied from the request
message ID (the default) or from the request message correlation ID.

For both one-way and two-way usage scenarios, dynamic and
static header properties can be specified.Static properties can
be set from the JMS import method binding. Some of these properties
have special meanings to the SCA JMS runtime.

It is important
to note that WebSphere MQ
JMS is an asynchronous binding. If a calling component invokes a WebSphere MQ JMS import synchronously
(for a two-way operation), the calling component is blocked until
the response is returned by the JMS service.

Figure 1 illustrates how
the import is linked to the external service.

Figure 1. WebSphere MQ
JMS import binding resources

<!-- image -->

## WebSphere MQ
JMS export bindings

The WebSphere MQ
JMS export binding provides the means for SCA modules to provide
services to external JMS applications on the WebSphere MQ-based JMS provider.

An
MDB is deployed to listen to requests incoming to the receive destination
specified in the export binding. The destination specified in the send field
is used to send the reply to the inbound request if the invoked component 
provides a reply. The destination specified in the replyTo field
of the response message overrides the destination specified
in the send field.

Figure 2 illustrates how
the external requester is linked to the export.

Figure 2. WebSphere MQ
JMS export binding resources

<!-- image -->