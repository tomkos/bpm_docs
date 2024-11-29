<!-- image -->

# WebSphere MQ JMS
bindings

Use the WebSphere MQ
JMS export and import bindings to integrate directly with
external JMS or MQ JMS systems from your server environment.  This
eliminates the need to use MQ Link or Client Link features of the
Service Integration Bus.

When a component interacts with a WebSphere MQ JMS-based service by way of
an import, the WebSphere MQ
JMS import binding utilizes a destination to which data will
be sent and a destination where the reply can be received.
Conversion of the data to and from a JMS message is accomplished through
the JMS data handler or data binding edge component.

When an SCA module provides a service to WebSphere MQ JMS clients, the WebSphere MQ JMS export binding utilizes
a destination where the request can be received and the response can
be sent. The conversion of the data to and from a JMS message is done
through the JMS data handler or data binding.

The function selector provides a mapping to the operation on the
target component to be invoked.

- WebSphere MQ JMS bindings overview

The WebSphere MQ JMS binding provides integration with external applications that use the WebSphere MQ JMS provider.
- Key features of WebSphere MQ JMS bindings

Key features of WebSphere MQ JMS bindings include headers, Java EE artifacts, and created Java EE resources.
- JMS headers

A JMS message contains two types of headers-the JMS system header and multiple JMS properties. Both types of headers can be accessed either in a mediation module in the Service Message Object (SMO) or by using the ContextService API.
- External clients

The server can send messages to, or receive messages from, external clients using WebSphere MQ JMS bindings.
- Troubleshooting WebSphere MQ JMS bindings

You can diagnose and fix problems with WebSphere MQ JMS bindings.
- Handling exceptions

The way in which the binding is configured determines how exceptions that are raised by data handlers or data bindings are handled. Additionally, the nature of the mediation flow dictates the behavior of the system when such an exception is thrown.