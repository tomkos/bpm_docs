<!-- image -->

# JMS function selector

## Standard JMS message function
selector

A second function selector is available that follows
the JMS standard of defining a message class with five subclasses
of the message class for the body or payload which contains the message
itself. Each subclass has a different body type. This function selector
uses the JMSType property of the message to select
the operation name.

The function selector is com.ibm.websphere.jms.data.bindings.JMSFunctionSelector.

To
simplify working with this function selector, a function has been
added to generate the appropriate business objects for the body types.
In the dependencies editor of a module beneath the Predefined Resources
heading, selecting Native Body schema for Native Body DataHandler and
saving the dependencies generates the business objects for these body
types. You can then use these business objects to represent the message
from the JMS client.

These data bindings could be used for routing
messages. For example, using a mediation module between an export
and two imports, a message filter primitive examines the values in
the message properties and routes high priority messages to one destination
and lower priority messages to another destination. Another possible
use could be to add an mapping transformation or database lookup mediation
primitive between an export and import to modify the message.

The
following table shows the relationship of the predefined resource,
the body type, the business object created for it, and the data type
for standard JMS messages.

| Predefined resource                            | Body type     | Business object   | Data type                                                                |
|------------------------------------------------|---------------|-------------------|--------------------------------------------------------------------------|
| Native Body schema for Native Body DataHandler | BytesMessage  | BytesBody         | Byte array                                                               |
| Same as first row                              | MapMessage    | MapBody           | Set of name/value pairs addressed by name. Value is a simple Java™ type. |
| Same as first row                              | Message       | BaseBody          | None (empty)                                                             |
| Same as first row                              | ObjectMessage | ObjectBody        | Serialized Java object                                                   |
| Same as first row                              | StreamMessage | StreamBody        | Stream of simple Java types                                              |
| Same as first row                              | TextMessage   | TextBody          | Java String                                                              |

Note that if the operation name is not set, it will be
derived from the type of incoming message as determined by this table:

| Message type   | Operation name   |
|----------------|------------------|
| BytesMessage   | handleBytes      |
| MapMessage     | handleMap        |
| ObjectMessage  | handleObject     |
| StreamMessage  | handleStream     |
| TextMessage    | handleText       |
| Message        | handleBase       |

If the operation name returned by the function selector
has not been configured for the export, an exception will be thrown.