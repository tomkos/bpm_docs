<!-- image -->

# WebSphere MQ bindings overview

## WebSphere MQ
administrative tasks

The WebSphere MQ
system administrator is expected to create the underlying WebSphere MQ Queue Manager,
which the WebSphere MQ
bindings will use, before running an application containing these
bindings.

## WebSphere administrative
tasks

You must set the Native library path property
of the MQ resource adapter in Websphere to the WebSphere MQ version supported by the server,
and restart the server. This ensures that the libraries of a supported
version of WebSphere MQ
are being used. Detailed hardware and software requirements can be
found on the IBM® support
pages.

## WebSphere MQ
import bindings

The WebSphere MQ
import binding allows components within your SCA module to communicate
with services provided by external  WebSphere MQ-based applications. You must
be using a supported version of WebSphere MQ.
Detailed hardware and software requirements can be found on the IBM support
pages.

Interaction with external WebSphere MQ systems includes the use of queues for
sending requests and receiving replies.

Two types of usage
scenarios for the WebSphere MQ
import binding are supported, depending on the type of operation
being invoked:

- One-way: The WebSphere MQ
import puts a message on the queue configured in the Send
destination queue field of the import binding.
Nothing is sent to the replyTo field of the MQMD
header.
- Two-way (request-response): The WebSphere MQ import puts a message on the queue
configured in the Send destination queue field The receive queue is
set in the replyTo MQMD header field. A message
driven bean (MDB) is deployed to listen on the receive queue,
and when a reply is received, the MDB passes the reply back to
the component. 
The import binding can be configured
(using the Response correlation scheme field)
to expect the response message correlation ID to have been copied
from the request message ID (the default) or from the request message
correlation ID.

It is important to note that WebSphere
MQ is an asynchronous binding. If a calling component invokes
a WebSphere MQ import synchronously (for
a two-way operation), the calling component is blocked until the response
is returned by the WebSphere MQ service.

Figure 1 illustrates how the
import is linked to the external service.

Figure 1. WebSphere MQ import binding
resources

<!-- image -->

## WebSphere MQ
export bindings

The WebSphere MQ
export binding provides the means for SCA modules to provide services
to external  WebSphere MQ-based
applications.

An MDB is deployed to listen to requests incoming
to the Receive destination queue specified
in the export binding. The queue specified in the Send
destination queue field is used to send the reply
to the inbound request if the invoked component provides
a reply. The queue specified in the replyTo field
of the response message overrides the queue specified
in the Send destination queue field.

Figure 2 illustrates how the
external requester is linked to the export.

Figure 2. WebSphere MQ export
binding resources

<!-- image -->