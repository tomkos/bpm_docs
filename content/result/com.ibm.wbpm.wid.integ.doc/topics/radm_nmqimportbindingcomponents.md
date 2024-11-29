# Key features of a WebSphere MQ
binding

## Correlation schemes

A WebSphere MQ request/reply application
can use one of a number of techniques to correlate response messages
with requests, built around the MQMD MessageID and CorrelID fields.
In the vast majority of cases, the requester lets the queue manager
select a MessageID and expects the responding application
to copy this into the CorrelID of the response.
In most cases, the requester and responding application implicitly
know which correlation technique is in use. Occasionally the responding
application will honor various flags in the Report field
of the request that describe how to handle these fields.

Export
bindings for WebSphere MQ
messages can be configured with the following options:

Response
MsgId options:

Response CorrelId
options:

Import bindings for WebSphere MQ messages can be configured
with the following options:

Request MsgId options:

Response correlation options:

## Java EE resources

A number of Java EE resources
are created when a WebSphere MQ
binding is deployed to a Java EE environment.

Parameters

- Send destination: where the request or outgoing message is sent
(import); where the response message will be sent (export), if not
superseded by the MQMD ReplyTo header field in
the incoming message.
- Receive destination: where the response/request or incoming message
should be placed.