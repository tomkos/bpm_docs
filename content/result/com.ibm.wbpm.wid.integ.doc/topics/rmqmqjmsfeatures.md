<!-- image -->

# MQ and MQ JMS features

This section examines these MQ and MQ JMS features in
relation to SCA artifacts.

- Using the correlation ID
- Using a URL to reference a client channel definition table (CCDT)
- Using binding or client transports (MQ JMS only)

## Using the correlation ID

A
correlation ID is used to correlate response messages with request
messages when an application invokes a request-response operation.
With WebSphere® MQ and WebSphere MQ JMS, you can
correlate using either a correlation ID or a message ID. In most cases,
the caller lets the queue manager select a message ID and expects
the application to copy this message ID into the correlation ID of
the response message. But there are other possibilities. A caller
could specify a specific value in the correlation ID and expect this
value to be copied into the response correlation ID. The caller might
also require that the message ID of the request message be copied
to the message ID of the response message.

When
you configure the MQ or MQ JMS bindings, you are given selections
that reflect the basic choice of copying the correlation ID to the
response correlation ID or copying the message ID to the response
correlation ID.

## Using a URL to reference a client channel
definition table (CCDT)

The client channel definition table
(CCDT) is created when you create the queue manager on the WebSphere MQ server. This
table contains the details of all the client-connection channels defined
at the WebSphere MQ server.
The table itself is a binary file with the name amqclchl.tab and it
is created automatically when you create one or more client connection
channels.

When you create MQ bindings, you must specify a CCDT
if you selected the "Use client channel definition table (CCDT)" option
when configured your bindings. When you create MQ JMS bindings, it
is an optional selection if you have chosen the client transport instead
of the bindings transport, which is the default.

1. Define your CLNTCONN channels using WMQ administration
2. Copy the amqclchl.tab file to the file system of the server where
the SCA application is running.
3. In the client channel definition table (CCDT) field, enter the
explicit path to the file on the server in the form of a URL. For
example, if the file was in this path, C:\mquser\ccdt\amqclchl.tab,
then the URL for the CCDT field would be file://C:/mquser/ccdt/amqclchl.tab.

## Using binding or client transports
(MQ JMS only)

You can select between two transport modes,
bindings (default) or client, when you use the MQ JMS bindings. A
transport mode is a way of connecting to the WebSphere MQ server. The following table
summarizes the difference.

| Transport          | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bindings (default) | Using bindings is a simpler set up. You do not need to specify host name, channel or port as WebSphere MQ JMS classes use the Java™ Native Interface (JNI) to call directly into the existing queue manager API rather than communicating through a network. Bindings is a shared memory protocol and may offer better performance. Bindings can only be used when the queue manager is on the same node as the JMS client. To use the bindings connection, WebSphere MQ JMS classes must be installed on the WebSphere MQ server. |
| Client             | Using client gives you more control, but it also means you must specify the values for the client configuration including host name, channel and port and optionally the client channel definition table. The WebSphere MQ client connection is used to connect to the queue manager.                                                                                                                                                                                                                                              |