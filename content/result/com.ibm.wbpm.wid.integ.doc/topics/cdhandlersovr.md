<!-- image -->

# Overview of data handlers

In your service-oriented architecture (SOA) implementation, business
data can flow between service providers and service consumers over
a variety of protocols (HTTP, JMS, MQ, EIS and so on) in a variety
of data formats such as comma separated value, delimited, fixed width,
COBOL and so on. Different protocols have different mechanisms for
carrying the business data in their protocol envelope. For example,
in the case of JMS, as a message body of JMS message; in the case
of HTTP, as payload of HTTP message. While the business protocol envelope
is different, the business data may or may not be in same format across
these protocols. The format in which business data flows on the wire
between service provider and service consumer is referred to as the native
format.

Business process components running on IBM® Workflow
Server understand
business data as business objects but they do not understand the native
format in which the data is flowing. Therefore, an export of an IBM Workflow
Server module
needs to de-serialize business data in native format obtained from
a protocol message which was received itself in a request from a service
consumer, into a business object. The export then invokes the business
process component with the business object. For two-way operations
(as shown in the diagram) the business object response from business
process needs to be serialized into native data format, which then
can be packed into the transport protocol message to be returned as
a response to service requester. 1 indicates the message protocol
carrying business data in native format.

<!-- image -->

Likewise, to invoke a service, the business process components
running on IBM Workflow
Server need
to serialize a business object into native data format. Therefore,
an import of an IBM Workflow
Server module
needs to serialize a business object to business data in a native
format, which then is packaged into the transport protocol message
used to invoke the target service. For a two-way operation, a business
response in native data format obtained from the protocol response
message needs to be de-serialized into a business object. 1 indicates
the message protocol carrying business data in native format.

<!-- image -->

IBM Workflow
Server data
bindings can be developed to serialize and de-serialize business data.
However for scenarios where the same native data format can flow over
multiple transport protocols (HTTP, JMS, MQ, EIS), the data transformation
logic needs to be repeated for each of the data bindings. For these
scenarios IBM Workflow
Server introduces
the concept of data handlers.

Data handlers are reusable transformation logic in IBM Workflow
Server which
can be invoked from data bindings, flow components and Java™ components. Data handlers can be configured
on some bindings and can be used in flow components. Unlike data binding
interfaces, the data handler interface is protocol neutral, which
enables data handlers to be usable across the bindings. Additionally,
if your scenario requires a business object to native data format
transformation beyond the normal types of data transformation, you
can call a data handler that can support that format from your Java components.

Data handler implementation can call other data handlers. This
is referred to as data handler chaining. Data handler chaining
is very useful for complex native data formats. For such formats if
transformation logic is complex the data handler implementation can
call other data handlers. For example if the native protocol message
has multiple parts, data handlers can be developed for each part.
The complex data handler for this multi-part message can call the
data handlers for each of the parts.

This section illustrates how to author data handlers, how to configure
them, how to call them and use them with your data bindings or in
your Java components.