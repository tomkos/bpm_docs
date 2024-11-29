<!-- image -->

# Mapping a message to an SCA interface

## Before you begin

Make sure that a module
that contains your service component architecture application exists
and that the message format used by the JMS, MQ, or MQ JMS client
is known.

- Business object
- Interface
- Imports, exports, and bindings

## Business object

In order
for your SCA application to communicate with an existing messaging
client, you will need to have a business object that would represent
the message that is used by the messaging client.

If the message
that is used by the client is in XML format, the XML schema that defines
it is used as your business object. If you have this schema, you must
import it into your module.  The imported XML schema then appears
under Data in your module. If you do not have
this schema, you can create a business object and add the appropriate
attributes to it that will mirror the XML format used by the client.

If
the message that is used by the client is not in XML format and there
is no XML schema that defines it, you must create a business object
and add the appropriate attributes to it so that it reflects logically
the message format used by the JMS client. For example, if the message
conforms to the Enterprise JavaBean (EJB) model, you create a business
object and add appropriate attributes to the business object to represent
the attributes of the EJB model.

JMS provides
a message class that can have one of five body types containing the
message in a different format. IBM® Integration
Designer supports
this message class. To reduce your development time, IBM Integration
Designer provides
a feature in its dependency editor to generate appropriate business
objects for each of these JMS body types.

1. Right-click Data in your module, and select New
> Business Object from the menu.
2. Specify an appropriate name for your business object and click Finish.
3. Add the appropriate attributes to your business object to fully
describe it, and save the object.

Data bindings, which are discussed later, handle the transformation
of data passed in native format from a messaging system or EIS system
to a Service Data Object (SDO) in a Service Component Architecture-based
(SCA) application.

## Interface

In order for your
SCA application to communicate to an existing messaging client, you
must have an interface that represents the input and output of the
messaging client application; that is, the interface represents the
interaction with the client.

The interface has business operations
to describe the messaging client application operations. The operation
style, such as document literal wrapped, document literal, or RPC,
to be implemented must be decided. An operation can be one-way, sending
a message and not expecting a response, or request-response, sending
a message and expecting a returning message.

The type of the
operation is the type of the business object that represents the message
used by the messaging client. For example, in the case of employee
information, an employeeRecord business object should be used or created.
Based on the content of the employee information, it might cause an
employee record to be created or an existing employee record to be
updated or deleted. So on the interface, you could have three operations:
createEmployeeRecord, updateEmployeeRecord, and deleteEmployeeRecord.

1. Right-click Interfaces in the navigation
of your module, and select New > Interface from
the menu.
2. Specify an appropriate name for the interface and click Finish.
3. Add the appropriate operations to your interface to fully describe
the interaction with the messaging client, and save the interface.

## Imports, exports, and bindings

A
business object represents the message received and sent from the
JMS, MQ, or MQ JMS messaging client, and an interface represents the
interaction of the input and output of the messaging client. But how
is the data transferred between the client and these SCA artifacts?
Business objects and interfaces are found in a module, which is similar
to a project container. Imports and exports define the external interfaces
or access points of the module. In other words, the messaging client
interacts with an SCA application's business objects and interfaces
through imports and exports.

Imports identify services outside
of a module that can be called from within the module. Exports allow
components to listen to requests from external clients. An export
allows an external event to be processed. When a message is put on
a destination, the associated SCA export processes the event invoking
the targeted SCA component. With respect to messaging, imports and
exports work as a pair to send and receive messages. An import allows
an internal event in the SCA application to be processed. When such
a message is put on a destination queue, the associated messaging
client processes the event. When a message is put on a destination
queue, the associated SCA export processes the event invoking the
targeted SCA component.

Binding information, which specifies
the means of transporting the data from the modules, is required for
an import or an export. Several messaging bindings, including JMS,
MQ, and MQ JMS, are available.

The relationship of bindings,
messages in the context of imports and exports, and types of operations
in interfaces is shown in the following table.

| JMS, MQ, or MQ JMS bindings   | One-way operation in an interface   | Request-response operation in an interface   |
|-------------------------------|-------------------------------------|----------------------------------------------|
| Import binding                | Client receives message             | Client receives and sends message            |
| Export binding                | Client sends message                | Client sends and receives message            |

1. Open the assembly editor.
2. From the import group on the palette, select an import and drag
it on to the canvas. An import with no implementation and no interface
is created.
3. Right-click the import and select Add Interface from
the menu.
4. Add an interface with at least one operation.
5. Generate the binding by right-clicking the import and, from the
menu, select Generate Binding > Messaging Binding > <type\_of\_binding>.

1. Open the assembly editor.
2. From the component group on the palette, select an export and
drag it on to the canvas. An export with no implementation and no
interface is created.
3. Right-click the import and select Add Interface from
the menu.
4. Add an interface with at least one operation.
5. Generate the binding by right-clicking the export and, from the
menu, select Generate Binding > Messaging Binding > <type\_of\_binding>.

## Related concepts

- Java Message Service (JMS)
- WebSphere MQ Java Message Service (MQ JMS)
- Generic JMS
- WebSphere MQ (WMQ)

## Related reference

- Recommendations when using messaging bindings
- Language support in non-EIS bindings