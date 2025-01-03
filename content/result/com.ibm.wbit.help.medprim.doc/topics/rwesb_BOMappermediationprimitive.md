# Business Object Map mediation primitive

## Introduction

1. Copy data from the first field in the input message, to the second
field in the output message.
2. Copy part of the second field in the input message, to the first
field in the output message.
3. Assign a constant value to the third field in the output message.

The Business Object Map mediation primitive has one input
terminal (in), one output terminal (out)
and a fail terminal (fail). The in terminal
is wired to accept a message and the other terminals are wired to
propagate a message. The input message triggers a transformation and
if the transformation is successful, the out terminal
propagates the modified message. If an exception occurs during the
transformation, the fail terminal propagates
the original message, together with any exception information contained
in the failInfo element.

## Details

When you create a Business Object
Map mediation primitive,IBM® Integration
Designer lets you create
a new business object map from the Details tab
of the Properties view. Alternatively, you
can browse the existing business object maps, and select a suitable
one.

When you create a business object map you specify the message
root, (an XPath 1.0 expression), which for mediation flows can refer
to the following locations in the service message object (SMO): /, /headers, /context or /body.
The message root specifies the root of the transformations, and applies
to both input messages and output messages. If the message root is /,
the transformation applies to the whole SMO.

## Transform types

The business object map
editor supports the following transform types, which are also called
mapping types:

| Transform (mapping) type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Move                       | Copy the value in the source field to the target field. For example, copy a customer name from the input business object to the output business object.                                                                                                                                                                                                                                                                                                                                                               |
| Extract                    | Extract part of the value in the source field, and assign it to the target field. The value of the source field must be a String. For example, copy part of an address from the input business object to the output business object. The extract transform is similar to the String.substring() method in Java™.                                                                                                                                                                                                      |
| Join                       | Combine the values of two or more source fields, and assign the combined value to the target field. The target of a join transform must be a String. For example, combine the first name John and the last name Smith, from the input business object, to make the name John Smith, in the output business object.                                                                                                                                                                                                    |
| Submap                     | You can use a submap to map between complex types, (business objects). The input and output of the business object map must be of the same type as the source and target of the submap transform. Submaps allow you to reuse mapping definitions. A submap transform uses a previously-defined map to perform a transformation between two parts of the message. You can use a submap transform even if the source, or the target, is a weakly-typed element.                                                         |
| Custom                     | Provide Java code to specify the logic for mapping the inputs and outputs.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Assign                     | Assign a constant value to the target field. The assign transform has a target field, but no source field.                                                                                                                                                                                                                                                                                                                                                                                                            |
| Relationship               | Perform relationship management. A relationship creates an association between data from two, or more, business objects. When fields in an input and output business object contain equivalent data, that is represented differently, the transformation step can use a relationship. You can create relationships using the IBM Integration Designer, New relationship wizard; and you can reuse existing relationships. The source and target of a relationship transform must be complex types (business objects). |
| Custom assign              | Provide Java code to decide the value you assign to the target field. The custom assign transform has a target field, but no source field.                                                                                                                                                                                                                                                                                                                                                                            |
| Custom callout             | Provide Java code that takes the value of a source field and uses it with your own logic. The custom callout transform can be useful for initialization, before running other transforms. The custom callout transform has a source field, but no target field.                                                                                                                                                                                                                                                       |

A move transform copies the value of a
primitive-type source field to a primitive-type target field. You
can map one primitive-type field to another primitive-type field.
However, if the data cannot be converted you will get an exception
at run time. For example, if the String 123A is mapped
to an int, at run time you will see an exception in the server log.
You cannot map complex types (business objects) using a move transform.
To map between business objects, you need a submap.

You can
use custom transforms to provide your own transformation logic. Custom
transforms use Java code. If there is a source
field and a target field you use the custom transform.
If there is no source field you can use a custom assign transform,
which is similar to an assign transform, except that
you use Java code to decide what value to
assign. If there is no target field to set, you can use a custom
callout transform to call Java code.
The Java code might initialize values before other
transforms run.

In some cases, you can use the move, submap,
and custom transforms even if the source, or the
target, is weakly-typed. A field is weakly-typed if it can contain
more than one type of data element. For example, you could use a submap
when the source or target element is of type anyType.
However, if the source data is incompatible with the target data you
will get an exception at run time.

## Usage

- Transform an input message type to a different output message
type. For example, if the mediation flow starts with one operation
but ends with another operation, and the second operation has a different
argument type.
- Alter the content of a message, without changing the message type.
- Apply your own logic to message transformations, by using the custom transforms.
- Reuse existing business object maps. You can reuse maps as top-level
maps, or as submaps.
- Apply mappings defined as relationships, to the content of messages.
You can create, and reuse, relationships.

The Business Object Map mediation primitive can be useful
if you need to manipulate data, before or after the Database Lookup
mediation primitive is invoked.

You can transform messages using
either the Mapping primitive or the Business Object Map mediation
primitive. The main difference is that the Business Object Map mediation
primitive performs transformations on business objects, using Service
Data Objects (SDO), whereas the Mapping mediation primitive can perform
transformations in both XML, using a stylesheet; and business objects,
using Service Data Objects.

If you have existing XML maps,
XSL stylesheets or business object maps, you can reuse them with the
Mapping mediation primitive. If you have existing business object
maps you can reuse them with the Business Object Map mediation primitive.
Some types of transformation are easier to perform in XSL, and others
using a business object map.

- Business Object Map mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)