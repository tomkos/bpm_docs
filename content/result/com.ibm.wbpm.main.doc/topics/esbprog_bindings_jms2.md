<!-- image -->

# Configuring the JMS binding

## JMS Messaging Domain

You can configure the binding to use point to point, or publish subscribe messaging paradigms.
This determines the type of J2EE resources created by the binding.

## End-Point Configuration

- Activation Specification connects to the JMS provider, receives messages and delivers them to
the JMS binding (the MQ JMS binding, in versions of previous to version 7, and the Generic JMS
binding use listener ports instead of activation specifications).
- Connection Factory is used to connect to the JMS provider to send messages.
- Destinations are used to configure the queue, or topic on the JMS provider, that messages are
received from, or sent to. The destination specified in the replyTo field of
the incoming message, overrides the send destination specified in the binding. A callback
destination is required for storing message correlation information, which is on the local Service
Integration Bus. Different imports or exports cannot share receive destinations, because potential
failures to process the message and transaction rollbacks occur.

## Security Attributes

A J2C authentication alias can be selected, for JMS providers that require authentication.

## Message Correlation

- The message ID of the request message is copied to the correlation ID of the response
message.
- The correlation ID of the request message is copied to the correlation ID of the response
message.
- A temporary dynamic response destination, correlates responses with requests.

A temporary destination is created for each request, and the import receives the response using
this destination. This method of correlation, results in the send and receive occurring outside any
existing global transaction. The temporary destination does not provide persistent messaging,
therefore the messages will not be stored on it and the server will not restart.

## Recovery

The JMS binding provides the option for messages that failed, to be processed and forwarded to
the failed event manager. This behavior is described in more detail in the Imports and exports chapter. It is the default behavior from version 6.2 of WebSphere®
ESB. In previous versions, messages that fail are rolled back and they are
processed to the JMS provider receive destination. The JMS provider handles the failure. This option
is still available but must be selected explicitly in the binding configuration from version 6.2 of
WebSphere
ESB. When using the WebSphere MQ JMS and Generic JMS binding, you must
configure an additional connection factory when using failed event manager, so that messages can be
replayed to correct destination.

## Event Sequencing

The option to support event sequencing is provided in the JMS export binding. This option limits
the number of threads, that can receive messages concurrently, to 1. In a clustered environment when
the application is started, only one activation specification in the cluster is started. This
prevents multiple servers to process messages concurrently which preserves the message sequence.