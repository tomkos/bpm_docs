<!-- image -->

# Mediation Flow Component

## Mediation flows

A mediation exposes an interface to the service requester. The mediation might use another
interface to call the service provider. The interface used by the service requester is referred to
as the source interface, and the interface provided by the service provider is referred to as the
target interface. Depending on the service requester and the service provider, the source and target
interfaces might be different.

For each source operation, the mediation can contain a request flow. For each operation that has
a response, the mediation has a response flow.

A request flow processes a request message from a service requester. The flow begins with a
single input node for the source operation, followed by one or more mediation primitives wired
together. Each target operation has a callout node, and the request flow can be wired to the callout
node to call a particular operation. If a message is to be returned to the source directly after
processing, the request flow can be wired to an input response node in the request flow. If fault
messages are defined in the source operation, an input fault node is also created. Wiring the
request flow to an input fault node allows a fault message to be returned directly to the service
requester.

A response flow processes responses returned from the service provider. The flow begins with a
callout response node for each target operation, followed by one or more mediation primitives wired
together. The response flow contains a single input response node representing the source operation.
Wiring the response flow to the input response node causes a response to be sent to the service
requester. If fault messages are defined in the target operation, a callout fault node is also
created in the response flow. The callout fault node allows fault messages that are returned by the
target operation, to be processed. Errors that are returned by the operation but are not defined as
fault messages, are propagated to the fail terminal of the callout response node.

Figure 1. Mediation flows

<!-- image -->

## Mediation primitives

Each mediation primitive allows you to manipulate messages. For example, you can route a message
or change its content. Mediation primitives process messages as Service Message Objects (SMOs).

You can use mediation primitives to change the format, content, or target of service request
messages.

All mediation primitives have an input terminal (called in) that can be wired to accept a
message. Most mediation primitives have one fail terminal (called fail) and one or more output
terminals. However, the Stop and Fail mediation primitives have no fail terminal and no output
terminals.

If a failure occurs during the processing of the input message, the fail terminal propagates the
original message, together with any failure information. If the fail terminal is not wired, the error flow runs. If the error flow has not been implemented,  the running
of the flow stops and a failure is reported to the system log.

If an output terminal of a mediation primitive is left unwired at run time, the unwired output
terminal stops this path in the flow without generating a failure, and the message is consumed.

The behavior of a mediation primitive is controlled by properties. Each mediation primitive type
has its own properties that configure the mediation primitives' capability.

## Administrative control of mediations

Mediation primitives and nodes have properties that can be used to customize their behavior. Some
of these properties can be made visible to the IBM® Workflow
Server administrator by promoting them. Certain properties lend themselves to
being administratively configured. Integration Designer lists
the properties that you can choose to promote under the promoted properties of a mediation
primitive.

Promoted properties are given an alias name, and you can set the alias name so that it is
meaningful in the context of a particular mediation. The alias name is the property name that is
displayed on the administrative console; multiple promoted properties can be given the same alias
name if they are of the same type. Therefore, what appears as a single property, in the
administrative console, can set the same value in multiple mediation primitives. You can set the
value of a promoted property, from Integration Designer,
during installation of the module and once the application has been installed using the
administrative console.

- Service Message Objects

The Service Message Object (SMO) provides an abstraction layer for processing and manipulating messages exchanged between services.

<!-- image -->