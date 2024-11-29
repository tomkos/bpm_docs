# Custom Mediation primitive

## Introduction

You can use the Custom Mediation
primitive to implement your own mediation logic in Java™ code.

The Custom Mediation primitive
combines the flexibility of a user-defined mediation primitive, with
the simplicity of a predefined mediation primitive. You can add new
terminals and create your own properties, and this allows you to create
complex transformations and routing patterns.

By default, a
Custom Mediation primitive has one input terminal (in),
one output terminal (out), and one fail terminal
(fail). However, you can add more input and
output terminals. The input terminals are wired to accept a message;
the output and fail terminals are wired to propagate the message.
The input message is passed as the input parameter to the Java code. If the operation returns successfully,
the response from the Java code
is propagated to an output terminal. If the operation returns unsuccessfully,
the fail terminal propagates the original message, together with any
exception information.

## Details

You can add an extra terminal to
a Custom Mediation primitive by right-clicking the Custom Mediation
primitive and selecting either Add Input Terminal or Add
Output Terminal. The name you give to a terminal is used
in code generation and, therefore, must be a valid Java identifier.

You can define your own
properties in a Custom Mediation primitive by going to the User
Properties tab of the Properties view.
You can add, edit and remove user properties.

You create your Java code by going to the Details tab
of the Properties view, and adding either Java snippets or visual snippets.
Because mediation primitives process messages as service message objects
(SMOs), the visual snippets for processing messages are in the SMO
services folder, in the Visual Snippet view.

You
specify the Java imports your
code needs on the Java Imports tab of the Properties view.

For
most mediation primitives, the mediation flow editor detects the message
types and only allows you to wire primitives that have compatible
message types. However, for Custom Mediation primitives, the editor
does not know the message types. Therefore, before you wire your Custom
Mediation primitive, specify its message types in the Terminal tab
of the Properties view.

## Migration

Any deployed version 6.0.x Custom
Mediation flows continue to work without migration or redeployment.

- Continue to work without migration.
- Are marked as deprecated, in WebSphere® Integration
Developer.
- Have read-only properties, in WebSphere Integration
Developer.
- Need manual migration to take advantage of the version 6.1.x Service
Invoke mediation primitive.

- Continue to work without migration.
- Are marked as deprecated, in WebSphere Integration
Developer.
- Cannot have more than one input terminal and one output terminal.
- The Root property is now read-only and is no
longer available in WebSphere Integration
Developer.
- Keep the method signature of the implementation as commonj.sdo.DataObject
execute(commonj.sdo.DataObject input1). The implementation
is modifiable using the embedded Java or
visual editors.
- Can be migrated to version 6.1.x using the fix in the Problems view.

## Usage

You can use the Custom Mediation primitive
to do processing that is not covered by other mediation primitives.

```
out1.fire(smo);
out2.fire(smo);
out.fire(smo);
```

You can create complex transformations.
For example, you could extract different parts of the input message
to send to the different output terminals.

In the same way as
you can make use of multiple output terminals, you can also make use
of multiple input terminals. For example, you could create a fault-handling
node by creating multiple input terminals each for a different terminal
type, and in your Java code
create a new output message that contains the /context/failInfo/failureString information.

- Custom mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)
- Example: Creating a ServiceMessageObject object

This example shows you how to create a new ServiceMessageObject object inside a Custom Mediation primitive.
- Example: Creating a new JMS header

This example shows you how to create a new JMS header for the ServiceMessageObject object inside a Custom Mediation primitive.
- Example: Creating a new SOAP header

This example shows you how to create a new SOAP header for the ServiceMessageObject object inside a Custom Mediation primitive.
- Example: Creating a new MQ header

This example shows you how to create a new MQ header for the ServiceMessageObject object inside a Custom Mediation primitive.
- Example: Accessing MQCIH header data

This example shows you how to access MQCIH header data in a message.
- Example: Querying WSRR

This example shows you how to query WSRR inside a Custom Mediation primitive.
- Example: Accessing WebSphere eXtreme Scale

This example shows you how to access WebSphere eXtreme Scale (eXtreme Scale) inside a Custom Mediation primitive.