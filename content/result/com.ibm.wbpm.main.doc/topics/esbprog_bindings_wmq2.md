<!-- image -->

# Configuring the WebSphere MQ binding

## End-point configuration

- Activation Specification connects to WebSphere MQ, receives messages and
delivers them to the binding.
- Listener ports connect to WebSphere MQ, receive messages and deliver
them to the binding.
- To send messages, use the Connection Factory to create a connection to
WebSphere MQ.
- Use the Destinations to configure the queue or topic, that messages are
received from, or sent to. The destination specified in the replyTo field of
the incoming message, overrides the send destination specified in the binding, unless configured
otherwise in the binding. Different imports or exports cannot share receive destinations, because
potential failures to process the message and transaction rollbacks occur.

## Message correlation

- The message ID of the response message, is copied from the message ID of the request, or from
the SCA message. You can be generate or define it using the report options specified in the
message.
- The correlation ID of the response message, is copied from the message ID, or correlation ID of
the request from the SCA message. You can define it using the report options specified in the
message.

## Message recovery

The WebSphere MQ binding provides the option to forward messages to the
failed event manager, if they fail to be processed. This behavior is described in more detail in the
Imports and exports section. It is the default behavior from version 6.2 of WebSphere®
ESB. In previous versions, messages
 that fail are rolled back, and they are processed to the
WebSphere MQ receive destination. WebSphere MQ handles the failure. This option
is still available but must be selected explicitly in the binding configuration from version 6.2 of
WebSphere
ESB.

## Security attributes

You can select a J2C authentication alias for WebSphere MQ connections that require
authentication. SSL configuration parameters are also available, for providing secure
connections.

## Event sequencing

The WebSphere MQ export binding provides the option to support event sequencing. This option
limits the number of threads, that receive messages concurrently, to 1. In a clustered environment,
when the application is started, only one activation specification in the cluster is started. This
prevents multiple servers from processing messages concurrently. In turn, this preserves the message
sequence.