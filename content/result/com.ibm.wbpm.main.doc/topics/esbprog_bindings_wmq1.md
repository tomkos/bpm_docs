<!-- image -->

# WebSphere MQ binding

## What is WebSphere MQ

- Messaging: programs communicate by sending each other data in messages rather than by calling
each other directly.
- Queuing: the messages are placed on queues in storage. As a result, programs run independently
of each other, at different speeds and times, in different locations, and without having a logical
connection between them.
- Publish/subscribe: a program sends (publishes) data to a single destination, and WebSphere MQ
distributes the data to other programs (subscribers). The publisher defines a topic for the
information, and the subscriber specifies what topics it wants to receive.

## WebSphere MQ binding

Use the WebSphere MQ import and export bindings to integrate directly with a WebSphere MQ-based
system from your server environment. This removes the need to use MQ Link or Client
Link features of the Service Integration Bus.

When a component interacts with a WebSphere MQ service through an import, the WebSphere MQ import
binding uses a queue, to which data is sent, and a queue where the reply can be received.

When a SCA module provides a service to WebSphere MQ clients, the WebSphere MQ export binding
uses a queue in which the request is received and the response is sent. The function selector
provides a mapping to the operation on the target component that is invoked.

Conversion of the payload data to and from a WebSphere MQ message is done through the WebSphere
MQ body data handler or data binding. Conversion of the header data to and from a WebSphere MQ
message is done through the WebSphere MQ header data binding.

- Configuring the WebSphere MQ binding

You can configure the WebSphere MQ binding to customize its behavior.
- Accessing the WebSphere MQ header

You can access the WebSphere MQ header using Java, or the mediation flow component.
- Using dynamic WebSphere MQ endpoints

You can dynamically invoke services using WebSphere MQ import bindings. The import that you invoke is decided at run time and does not need to be wired directly to a component. During a dynamic invocation, you do not specify the endpoints that you use in the import bindings. If you use a mediation flow component, you can specify a target import and dynamic endpoint address using some mediation primitives. For example, the Message Element Setter mediation primitive to manipulate the Target section of the SMO.

<!-- image -->