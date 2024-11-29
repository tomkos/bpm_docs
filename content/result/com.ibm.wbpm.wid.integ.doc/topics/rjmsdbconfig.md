<!-- image -->

# Working with the simple JMS data bindings

A
standard schema is defined for messaging types as a data handler that
uses a data binding. The data handler, Native Body Schema
for Native Body DataHandler, is the standard JMS data
handler for all message types. To add this predefined resource, expand
your project and then double-click Dependencies.
The Dependencies editor opens. Expand Predefined Resources to
select the data handler. Save your work.

- BytesMessage - The message body is a byte array.
- MapMessage - The message body is set of name/value pairs which
can be addressed by name and where the value is a simple Java™ type.
- ObjectMessage - The message body is a serialized Java Object.
- StreamMessage - The message body is a stream (sequence) of simple Java types.
- TextMessage - The message body is a Java String.

- BytesBody - Extracts the bytes from the incoming bytes message
and wraps them into the business object. Conversely, it can also or
extract the bytes from the business object and wrap them into the
outgoing bytes message.
- MapBody - Extracts the name, value and type information for every
entry in the incoming map message and creates a list of MapEntry business
objects. It then wraps the list into the business object. Conversely,
it can also extract the name, value and type information from the
MapEntry list in the map body business object and create the corresponding
entries in the outgoing map message.
- NativeBody - Converts raw data into one of the base native data
structures during an inbound message. Conversely, it converts a business
object to raw data during an outbound message.
- ObjectBody - Extracts the object from an incoming object message
and wraps it into the business object. Conversely, it can also extract
the object from the business object and wrap it into the outgoing
object message.
- simpleJavaType - Transforms the incoming Java serialized object in the object message
into a business object. Conversely, it can also serialize the business
object to the outgoing Java serialized
object in the object message.
- StreamBody - Extracts the name and type information for every
entry in the incoming stream message, creates a list of the StreamEntry
business objects, then wraps them into the stream body business object.
Conversely, it can also extract the name and type information from
the StreamEntry list in the stream body business object and create
corresponding entries in the outgoing stream message.
- TextBody - Extracts the text from the incoming text message and
wraps it into the text body business object. Conversely, it can also
extract the text from the text body business object and wrap it into
the outgoing text message.

The data bindings display in the Data area
of your project after you have selected the Native Body
Schema for Native Body DataHandler. When you use the data
bindings for standard JMS message body types, you must add the service
gateway interface and schema files if you are building a static service
gateway.  In your module, open the dependencies editor. Under Predefined
Resources, select Service gateway interface.
Save your work and close the dependencies editor.

Two specialized
JMS data bindings also exist, one for Text and one for Object messages.
The Text binding requires the message body to be an XML description
of a message. The Object binding requires the message body to be a
serialized data object. These bindings are general purpose and support
any message body.

For Text and Bytes messages, the bindings
treat the message payload as unstructured data and transfer it as
a whole into the corresponding business object. In certain cases,
the data and map elements (of the message payload) need to be parsed
into a structure within a business object. This happens when the data
is structured. In those cases, you must provide your own data bindings
and business object definitions.

A
delimited data binding is available for cases where the message body
is in a format delimited by a comma (,). A fixed width data binding
is available for cases where the message body is in a fixed width
format.

A JMS adapter language data binding generator binding
treats the message body as a language supported by the JMS adapter
such as COBOL.

The nine standard JMS data bindings can be used
when you have a simple message or you want to perform routing without
looking at message content. You would choose the Text or Object data
bindings if you have business objects you want to work with. Use the
delimited or fixed width data bindings when the message body contains
a message in those formats. Use the JMS adapter language data binding
when the message body is in a language like COBOL.

When you
create an interface with request or request-response operations for
interacting with the destinations of messaging providers, the input
and output data types must match your use case. For example, if you
are performing message routing with a flow component, use the appropriate
JMS type. If you are processing the data then use a type that matches
the message body.

You can also use a WTX data handler. The transformation extender data
binding is a universal validation and transformation engine that converts
business objects to other data formats.

## Related concepts

- Prepackaged JMS data format transformations
- JMS function selectors

## Related reference

- Overview of JMS, MQ JMS and generic JMS bindings
- Data handlers
- Business object XML using JMS text message serialization
- Prepackaged JMS and MQ fault selectors