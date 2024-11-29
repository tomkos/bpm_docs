# Key features of WebSphere MQ JMS bindings

## Headers

A JMS message header contains a
number of predefined fields containing values used by both clients
and providers to identify and to route messages. You can use binding
properties to configure these headers with fixed values, or the headers
can be specified dynamically at run time.

## Correlation schemes

The WebSphere MQ
JMS bindings provide various correlation schemes that are used to
determine how to correlate request messages with response messages.

## Java EE resources

A number of Java EE resources
are created when an MQ JMS import is deployed to a Java EE environment.

Parameters

- Send destination:
    - Imports: Where the request or outgoing message is sent.
    - Exports: Where the response message will be sent if it is not
superseded by the JMSReplyTo header field of the
incoming message.
- Receive destination:

- Imports: Where the response or incoming message should be placed.
- Exports: Where the incoming or request message should be placed.