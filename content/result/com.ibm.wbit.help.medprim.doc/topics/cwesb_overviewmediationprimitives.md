<!-- image -->

# Mediation primitives

## Introduction

Mediation primitives are the building blocks of mediation flows. You create mediation flows in
mediation flow components, and mediation flow components can exist in either business modules or
mediation modules.

Mediation flows operate on messages that are in-flight between service requesters (service
consumers) and service providers, and each mediation primitive lets you do different things with a
message. For example, you can route a message or change its content. Mediation primitives process
messages as service message objects (SMOs) because SMOs allow different types of
messages to be processed in a common way.

Mediation primitives are connected together through terminals, which provide points
of input to, and output from, the mediation primitive. All mediation primitives have an input
terminal (called in) that can be wired to accept a message. Most mediation
primitives have one fail terminal (called fail) and one or more output
terminals. However, the Stop and Fail mediation primitives have no fail
terminal and no output terminals.

If an output terminal of a mediation primitive is left unwired, WebSphere® Integration Designer generates a warning. At run time, the unwired
output terminal stops this path in the flow without generating an exception, and the message is
discarded.

If an exception occurs during the processing of the input message, the
fail terminal propagates the original message, together with any exception
information. If an exception occurs before mediating the input message, when setting the properties
of a mediation primitive, an IllegalArgumentException is thrown and the original
message is not propagated.

## Mediation flows

A service requester uses a specific interface to invoke a mediation and, in its role as an
intermediary, the mediation uses another interface to invoke the service provider. The interface
used by the service requester is referred to as the source interface, and the interface provided by
the service provider is referred to as the target interface. Depending on the service requester and
the service provider, the source and target interfaces might be the same or different.

For each source operation, the mediation can contain a request flow. For each operation that can
have a response, the mediation can also have a response flow. Each operation can also have an
error flow.

A request flow processes a request message from a service client. The flow begins with a single
input node for the source operation, followed by one or more mediation primitives wired together, in
sequence. Each target operation has a callout node, and the request flow can be wired to the callout
node to call a particular operation. If a message is to be returned to the source directly after
processing, the request flow can be wired to an input response node in the request flow. If fault
messages are defined in the source operation, an input fault node is also created. Wiring the
request flow to an input fault node allows a fault message to be returned directly to the service
requester.

A response flow processes responses returned from the service provider. The flow begins with a
callout response node for each target operation, followed by one or more mediation primitives wired
together, in sequence. The response flow contains a single input response node representing the
source operation. Wiring the response flow to the input response node causes a response to be sent
to the service invoker. If fault messages are defined in the target operation, a callout fault node
is also created in the response flow. The callout fault node allows fault messages that are returned
by the target operation, to be processed. Errors that are returned by the operation but are not
defined as fault messages, are propagated to the fail terminal of the callout
response node.

An error flow processes messages that are propagated to the fail terminal
of a mediation primitive in the request or response flow, or the fail
terminal of a callout response node, that is not wired to another primitive or node. The flow begins
with a single input node, followed by one or more mediation primitives wired together, in sequence.
The error flow for a request-response operation contains a single input response node and, if fault
messages are defined in the operation, the error flow contains an input fault node. An error flow
can be used to complete actions when an unexpected error occurs in the mediation flow; for example,
logging the message using the Message Logger mediation primitive. An error flow can also be used to
return a response message or modeled fault, rather than the unmodeled fault that would be returned
if the error flow were not implemented. For more information on error handling, see the .

## Promoted properties

Promoted properties are given an alias name, and you can set the alias name so that it is
meaningful in the context of a particular mediation. The alias name is the property name that is
displayed on the runtime administrative console; multiple promoted properties can be given the same
alias name if they are of the same type. Therefore, what appears as a single property, in the
administrative console, can set the same value in multiple mediation primitives. You can set the
value of a promoted property, from IBM Integration
Designer and from the runtime administrative console.

## Property groups

A promoted property belongs to a group. By default, the group name is the mediation flow
component name, but you can override the default group name. At integration time, you can use
property groups to create collections of properties. There is a relationship between property groups
and mediation policy namespaces.

At run time, properties are displayed and administered in their groups.

## Dynamic properties

Any mediation primitive that promotes a property is allowing the property value to be dynamically
set, and the mediation primitive is said to be dynamically configurable.

## Mediation policies

If you want to use mediation policies to control your mediation flows, you must include the
Policy Resolution mediation primitive in your mediation flow component. If you want to associate
mediation policies with a target service, rather than a module, you should add an Endpoint Lookup
primitive before the Policy Resolution primitive.

After exporting the EAR file containing your Policy Resolution primitive, you must import it into
WebSphere Service Registry and Repository (WSRR). This
adds your module, and default mediation policies, to the registry. If you want to associate
mediation policies with a target service, you must also load the WSDL for the target service, into
WSRR. After loading your documents into WSRR, you must attach a suitable mediation policy to either
your module or to your target service, or both.

At run time, the Policy Resolution mediation primitive queries your registry, and uses any
suitable mediation policy information to override dynamic properties that come later in the
flow.

## XPath

Many mediation primitives have a property called Root that contains an XPath 1.0
expression. You can use this XPath expression to specify a subset of the message for the mediation
primitive to operate on. Depending on the mediation primitive, you must specify:
/, /body, /headers, or your own
XPath expression. / refers to the complete SMO, /body
refers to the body section of the SMO, /headers refers to the headers of the
SMO. If you specify your own XPath expression, the part of the SMO you specify is processed.

IBM Integration Designer displays the structure of a
message and allows you to select locations within the message. In this way you can navigate the
structure of a message and create XPath expressions.

## Dynamic routing

You can route messages to an endpoint that is decided at run time. The endpoint that the runtime
environment uses is located in the SMO header at /headers/SMOHeader/Target/address.
You can set this part of the SMO manually, using various mediation primitives, but the Endpoint
Lookup mediation primitive can set this location automatically.

In order for the runtime environment to implement dynamic routing on a request, you must set the
Use dynamic endpoint if set in the message header property in the callout
node or Service Invoke mediation primitive.

You can specify a default endpoint that the runtime environment uses if it cannot find a dynamic
endpoint. You specify a default endpoint by wiring an import to a reference.

Dynamic endpoint support does not require you to wire a reference to an import. However, if you
want to provide default configuration settings for the dynamic endpoint, you can use a wired import.
After a reference is wired to an import, the configuration settings of the import apply to all
dynamic endpoints using that reference.

For example, if you are dynamically routing to a JMS or MQ endpoint, you can use a wired import
to define the data format and other connection and interaction properties. The endpoint address to
be used is then supplied dynamically from the mediation flow. Similarly, you can configure the
security settings for a web service dynamic endpoint, by using a wired import with web service
binding.

The Endpoint Lookup mediation primitives can also set a list of alternative target endpoints in
the SMO header at /headers/SMOHeader/AlternateTarget. When the callout or
Service Invoke mediation primitive property Retry on  is set to
failure, you can set the Try alternate endpoints
property to use these alternative endpoints when a callout to the primary dynamic endpoint address (
/headers/SMOHeader/Target/address) has failed.

## Attachments

You can receive and send SOAP messages that have attachments of various sorts, such as images.
You might want to receive SOAP messages with attachments and let the attachments pass through
unchanged, or you might want to create new attachments, perhaps from information in the message.

## Exceptions

A mediation primitive throws a MediationConfigurationException if it detects
either a configuration problem or a transient external resource failure. For example, if a database
cannot be found. In addition, a mediation primitive throws a
MediationConfigurationException if a dynamic property has a problem with the
override value supplied in the relevant policy. For example, if a dynamic property is an integer and
the string value defined in the policy cannot be successfully converted into an integer, the
mediation primitive throws a MediationConfigurationException.

A mediation primitive throws a MediationBusinessException if there is a business
error. For example, if a key that should be in a message, is not found.

The runtime environment throws a MediationRuntimeException if there are problems
setting up a mediation flow.

- Service message objects

Service message objects (SMOs) provide an abstraction layer for processing and manipulating messages exchanged between services.
- Promoted and dynamic properties

Mediation primitives have properties, and some of these properties can be made visible to the runtime administrator by promoting them. Any property that you promote from a primitive in the top level request, response, or fault flow can also be overridden, at run time, using a mediation policy.
- Mediation subflows

A mediation subflow is a preconfigured set of mediation primitives, run in the context of a parent flow, that are wired together to realize a common pattern or use case. Mediation subflows can be shared among mediation flows.
- List of mediation primitives

Mediation primitives let you change the format, content or target of service requests.