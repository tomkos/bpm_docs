# Mapping mediation primitive

## Introduction

You can use the Mapping mediation
primitive to transform messages using XSL transformations or Business
Object Maps. This mediation primitive was named the XSL Transformation
mediation primitive in WebSphere® Enterprise Service Bus version
7.5.1 and earlier.

When you are integrating services, you often
need to transform data into a format that the receiving service can
process; the Mapping mediation primitive lets you transform one message
type into a different message type.

The Mapping mediation primitive
has one input terminal (in), one output terminal
(out), and a fail terminal (fail).
The in terminal is wired to accept a message
and the other terminals are wired to propagate a message. The input
message triggers a transformation and if the transformation is successful,
the out terminal propagates the modified message.
If an exception occurs during the transformation, the fail terminal
propagates the original message, together with any exception information
contained in the failInfo element.

## Details

The Mapping mediation primitive
gives you a simple mechanism for manipulating messages, using an XSLT
1.0 transformation, an XSLT 2.0 transformation or a Business Object
Map. You can change the headers, context, or body of the SMO by mapping
between the input and output message.

In order to transform
messages, the Mapping mediation primitive needs access to a mapping
file, which you can specify using the Mapping file property.
The mapping file can be either an XML mapping file or an XSL stylesheet.

When
you create an Mapping mediation primitive, IBM Integration
Designer lets you create a new XML map from the Details tab
of the Properties view. Alternatively, you
can browse the existing XML maps, and select a suitable one.

When
you create an XML map you specify the message root, (an XPath 1.0
expression), which for mediation flows can refer to the following
locations in the SMO: /, /headers, /context or /body.
The message root specifies the root of the transformations, and applies
to both input messages and output messages. If the message root is /,
the transformation applies to the whole SMO.

If you use the
XML mapping editor then, after the mapping has been created, an XSL
stylesheet is generated to perform the transformation at run time
depending on the Target engine property defined
in the XML map. If you wire the input and output terminals of the
Mapping mediation primitive before using the XML mapping editor, the
input and output message types are already entered for you.

XSLT2
transformations in the runtime are supported in WebSphere
ESB and IBM® Business Automation
Workflow at
version 7.5 and later.

You do not have to use the XML mapping
editor. Alternatively, you can use an existing XSL stylesheet to perform
your transformation.  The stylesheet must exist in the mediation module
project directory before you can select it.

## Migration

Introduced in WebSphere Integration
Developer version 6.1, the Mapping mediation primitive had a new XML
mapping editor. XML maps that were built in a previous version must
be migrated to the new format before you can edit them.

## Usage

If you need to connect mediation primitives
whose message types are different, you can use the Mapping mediation
primitive to transform the message type.

- Transform an input message type to a different output message
type. For example, if the mediation flow starts with one operation
but ends with another operation, and the second operation has a different
argument type.
- Alter the content of a message, without changing the message type.
- Apply an existing XML map, or stylesheet, to transform a message.

- Manipulate data, before or after the Database Lookup mediation
primitive is invoked.
- Copy the response from the Service Invoke mediation primitive
into the shared context.
- Create a new message body, using data in the shared context, after
the Fan In mediation primitive.

You can transform messages using either the Mapping mediation
primitive or the Business Object Map mediation primitive. The key
difference is that the Business Object Map mediation primitive performs
transformations on business objects, using Service Data Objects (SDO),
whereas the Mapping mediation primitive can perform transformations
in both XML, using a stylesheet; and business objects, using Service
Data Objects

If you have existing XML maps, XSL stylesheets
or business object maps, you might be able to reuse them with the
Mapping mediation primitive; and if you have existing business object
maps you might be able to reuse them with the Business Object Map
mediation primitive. Some kinds of transformation are easier to perform
in XSL, and others using a business object map.

- Mapping mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)