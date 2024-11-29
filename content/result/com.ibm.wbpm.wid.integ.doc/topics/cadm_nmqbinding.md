<!-- image -->

# WebSphere MQ bindings

Use the WebSphere MQ
export and import bindings to integrate directly with a WebSphere MQ-based system from your server
environment.  This eliminates the need to use MQ Link or Client Link
features of the Service Integration Bus.

When a component interacts with a WebSphere MQ service by way of an import,
the WebSphere MQ import
binding uses a queue to which data will be sent and a queue where
the reply can be received.

When an SCA module provides a service to WebSphere MQ clients, the WebSphere MQ export binding uses a queue
where the request can be received and the response can be sent. The
function selector provides a mapping to the operation on the target
component to be invoked.

Conversion of the payload data to and from an MQ message is done
through the MQ body data handler or data binding. Conversion of the
header data to and from an MQ message is done through the MQ header
data binding.

For information about the WebSphere MQ versions supported, see
the  detailed system requirements web page.

- WebSphere MQ bindings overview

 The WebSphere MQ binding provides integration with native MQ-based applications.
- Key features of a WebSphere MQ binding

Key features of a WebSphere MQ binding include headers, Java EE artifacts, and created Java EE resources.
- WebSphere MQ headers

WebSphere MQ headers incorporate certain conventions for conversion to the service component architecture (SCA) messages.
- Adding MQCIH statically in a WebSphere MQ binding

IBM® Integration Designer supports adding MQCIH header information statically without using a mediation module.
- External clients

IBM Integration Designer can send messages to, or receive messages from, external clients using WebSphere MQ bindings.
- Troubleshooting WebSphere MQ bindings

You can diagnose and fix faults and failure conditions that occur with WebSphere MQ bindings.
- Handling exceptions

The way in which the binding is configured determines how exceptions that are raised by data handlers or data bindings are handled. Additionally, the nature of the mediation flow dictates the behavior of the system when such an exception is thrown.