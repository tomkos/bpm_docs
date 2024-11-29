<!-- image -->

# Overview of MQ data format transformations

- MQ message to SCA message architecture
- Accessing MQ messages
- MQ data bindings in IBM Integration Designer

## MQ message to SCA message architecture

The
following points define the MQ message to SCA message architecture:

- When either an SCA message needs to be converted to a WebSphere MQ message, or vice-versa,
you must configure one body data binding and may provide any number
of header data bindings.
- A data binding is represented by the name of a Java™ class. The instances of that class can
convert both from an MQ message to an SCA message and vice versa.
The data binding classes are supplied with the product or may be written
by yourself or some third party.
- IBM® Integration
Designer includes
a set of header data bindings. You may add custom header data bindings
to this set on an individual import or export. Your user header data
bindings will take precedence over the IBM provided
header data bindings.
- When reading an MQ message, header bindings are chosen
based on the format identifier in control information associated with
the header. When no header binding can determine the message, the
body binding is called. Body data bindings have access to the remaining
portion of the unparsed message and also the entire chain of parsed
header objects.
- When writing an MQ message, header bindings are again chosen
based on the format identifier in the control information associated
with the header. The body data binding can override the format identifier
written into the MQ message.
- A function selector must
be used with an export which, in conjunction with method bindings,
will determine which body data binding is used.

## Accessing MQ messages

To
read MQ messages, an MQDataInputStream object is
passed. It is based on the DataInputStream class.
To write MQ messages, an MQDataOutputStream object
is passed. It is based on a DataOutputStream class.
These classes contain methods that simplify the reading and writing
of types used in MQ message structures. The MQDataInputStream and MQDataOutputStream objects
also can determine MQ Coded Character Set Identifier (CCSID) and encoding
values. Upon entry to the read() or write() method, the Stream is
initialized with the expected CCSID and encoding values. Data bindings
for more complex structures may need to update these values during
read or write operations. The Streams honor the current CCSID and
encoding settings when writing or reading from the MQ message.

The MQDataInputStream and MQDataOutputStream interfaces
can be found in IBM Integration
Designer.

## MQ data bindings in IBM Integration
Designer

In
addition to support for the MQ Message Descriptor (MQMD), the MQ data
bindings supplied with IBM Integration
Designer provide
complete support for the MQRFH and MQRFH2 headers, which provides
interoperability with JMS, IBM Integration Bus, and the publish-subscribe
distribution method. Partial support is provided for messages with
a format that begins MQH; that is, messages with a format for the
form MQHxxxxx. These headers are exposed as binary data in SCA and
Service Message Objects (SMOs). SMOs are used in mediation flow components.

Five
body data bindings may be used with an MQ import or MQ export. String
and binary data bindings treat the body as unstructured binary or
text data. XSD types are provided describing the DataObjects used
by these bindings. These data bindings require a business object definition
matching that expected of the JMSObjectMessage and JMSTextMessage data
bindings, as discussed in Overview of JMS, MQ JMS and generic JMS bindings.

Note
that to use these body data bindings, which are discussed in Working with the simple JMS data bindings, you need to first add a schema to
your module. To add the schema, open the dependencies editor and under Predefined
Resources, select Native Body schema for Native
Body DataHandler. Then save your selection and close the
editor. In the navigation under Data, the appropriate
business objects to be used with these body data bindings are created.
When you create input and output variables for your operations, select
the appropriate business type. For example, select a JMSTextBody if
using text. When you generate the MQ data format transformation, a
filtering mechanism will choose the appropriate data format transformation.
In this case, wrapped text.

Additional bindings store a serialized
form of the SCA message body in the MQ message. One serialized form
uses Java object serialization
and one serialized form uses an XML form. When either of these body
data bindings are used with an import, the import includes an MQRFH2
header in the outbound MQ message with a property TargetFunctionName in
the folder. This property is set to the name of the invoked operation.
An export using the JMS-type function
selector will look for a user property with that name.

Lastly,
the MQ Service Gateway data binding can be used in conjunction with
the Service Gateway interface. This data binding determines the type
of the inbound MQ message and defers processing to the corresponding
built-in data binding.

When a message is parsed, the header
bindings are executed first, then the function selector and then the
body binding.

## Related concepts

- Prepackaged MQ data format transformations
- Prepackaged MQ function selectors

## Related reference

- Data handlers
- Overview of the MQ function selectors
- Prepackaged JMS and MQ fault selectors