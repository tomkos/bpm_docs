# Data Handler mediation primitive

## Introduction

You can use the Data Handler
mediation primitive to transform a targeted section of a message.
The starting point of a transformation is indicated by an XPath expression.

The
Data Handler mediation primitive can be used when you are trying to
integrate services, and parts of the message are in a format that
is not easy to manipulate with existing mediation primitives. The
Data Handler primitive can also be used to transform the data in a
message into a business object (BO) that can be manipulated by other
mediation primitives. The part of the message not referenced by the
XPath expression is not modified.

The Data Handler primitive
has one input terminal (in), one output terminal
(out), and a fail terminal (fail).
The in terminal is wired to accept a message
and the other terminals are wired to propagate a message. The input
message triggers a transformation and if the transformation is successful,
the out terminal propagates the modified message.
If an exception occurs during the transformation, the fail terminal
propagates the input message, together with any exception information
contained in the failInfo element.

## Details

The Data Handler primitive gives
you a simple mechanism for manipulating messages, using the data handler
framework in the runtime environment. You can change any section of
the service message objects (SMO) using the Data Handler primitive.

You need to configure a data handler for this primitive.
You can generate a configuration file using the Binding
Resource Configuration panel. You must ensure that the
data handler is compatible with the source and target elements identified
by the XPath expressions.

## Usage

You can use the Data Handler primitive
to convert a physical format, such as a Text string inside a JMS Text
Message object, into a logical BO structure and back again. This allows
the transformation of the physical format into the specific BO to
be completed in the mediation flow component, instead of the export
and import.

- Transform a section of the input message from one defined structure
to another defined structure. For example, if the SMO includes a string
value that is comma delimited and you want to parse this into a specific
BO.
- Alter the message type. For example, when a JMS export has been
configured to use a JMS basic-typed data binding and within the mediation
module the integration developer decides that the content should be
inflated to a specific BO structure.

## Example: Using Data Handler mediation primitive with
service gateway for web service binding

```
Source XPATH: /body/message/value
Target XPATH: /body
Data handler configuration: Point to a configuration of the XML DataHandler without any values specified for the root name 
   or namespace 
Action: Convert from native data format to a business object
```

```
Source XPATH: /body
Target XPATH: /body/message/value
Binding resources configuration: Point to a configuration of the XML DataHandler without any values specified for the root name or namespace
Action: Convert from a business object to native data format
Weakly typed field /body/message 
Actual field type: textBody
```

- Data Handler mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)