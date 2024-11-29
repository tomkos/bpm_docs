# Set Message Type mediation primitive

## Introduction

You can use the Set Message
Type mediation primitive to treat weakly-typed message fields as though
they are strongly-typed. A field is weakly-typed if it can contain
more than one type of data. A field is strongly-typed if its type
and internal structure are known. The Set Message Type mediation primitive
lets you do the equivalent of casting a generic data type to a more
specific data type.

Typically, a weakly-typed field is declared
as having an XML schema type of anyType or anySimpleType,
or is an XML wildcard element (any). Less commonly
used weak-typing constructs are abstract types and substitution groups.

The
Set Message Type mediation primitive lets you overlay message fields
with more detailed structures, and then use the more detailed structures
in other mediation primitives. For example, if a message field is
defined to contain any type of content but you know it will contain
customer details, you might overlay the generic structure with a customer
details structure.

After you define how weakly-typed fields
are to be interpreted, the IBM Integration Designer tools show the
more detailed structures. The more detailed structures make it easier
for you to manipulate the message content. For example, you could
create mappings that operate on the contents of the weakly-typed fields.

The Set Message Type mediation primitive has one input
terminal (in), one output terminal (out),
and a fail terminal (fail). The in terminal
is wired to accept a message and the other terminals are wired to
propagate a message. At run time, if no exception occurs during the
processing of the input message, the out terminal
propagates the unmodified message. However, if an exception occurs
during the processing of the input message, the fail terminal
propagates the original message, and stores the exception information
in the failInfo element of the service message object
(SMO). The fail terminal is used if you enable
validation, and the input message fields do not conform to the strong
data types you specify.

## Details

After you wire together all parts
of your mediation flow, and configure your mediation primitives, every
terminal has a terminal type with an associated message type. When
you specify strongly-typed data, using the Set Message Type mediation
primitive, this information is associated with the out terminal.

Using
the Set Message Type mediation primitive you define how fields in
the input message are to be interpreted and this information is accessible
to mediation primitives that come later in the mediation flow. The
information specified by the Set Message Type persists through the
rest of the mediation flow, unless another mediation primitive changes
the message type. For example, a Mapping mediation primitive might
change the message type, or another Set Message Type might reset the
strong-typing.

## Usage

An ESB is often used to make routing
decisions based on message content, and to transform messages to a
format understood by the service provider. In order to make routing
decisions, or specify transformations, it is useful to have a complete
representation of the message. If the mapping editor, or XPath wizard,
shows that your message contains weakly-typed fields, you can overlay
these with a detailed representation using the Set Message Type mediation
primitive. Without the Set Message Type capabilities, you must write Java™ code for a Custom Mediation
primitive, or create a hand-written XSL stylesheet for a Mapping mediation
primitive.

XML schema definitions sometimes use weakly-typed
fields to represent message content that can vary. For example, an
XML schema might define a generic message type that can hold different
payload types. However, if you know what the exact message format
is, you can use the Set Message Type mediation primitive to make the
format known to the tools, and the other mediation primitives in the
flow.

You can use the Set Message Type mediation primitive to
treat a weakly-typed message field as though it is a strongly-typed
field. You can also use the Set Message Type mediation primitive to
treat a strongly-typed field as though it is contains data of a different
strong type. However, the new strong type must be derived from the
strong type declared in the input message.

At run time, the
Set Message Type mediation primitive lets you check that the message
content matches the specific data types you expect.

- Set Message Type mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)