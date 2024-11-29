<!-- image -->

# Business objects

Service Component Architecture (SCA) provides the framework for
defining an application module, the services it provides, the services
it consumes, and the composition of components that provide the business
logic of the application module. Business objects play an important
role in the application, defining the business data that is used to
describe the service and component contracts and the business data
that the components manipulate.

Figure 1. Business
objects represent the data that flows between services in an application

<!-- image -->

A business object contains fields that have a name, a type (scalar
type or another business object), a default value (for scalar types)
and cardinality.  Business objects can extend (define a superset of
fields) other business objects through parent/child relationships;
however, a business object can only inherit from a single parent.
These objects can also be used in conjunction with each other to perform
a task.

## Business object fields

Essentially, business
object fields are the mechanisms through which you define what information
a business object can hold, and how that information should be accessible.
Business object fields are used to define the content of a business
object. Each field has a name, type, cardinality, and other optional
properties. After you create a business object, you can use the business
object editor to create or change its fields. A business object is
simply a container for the data specified in its fields. An empty
business object without fields is not useful as it does not have the
means to actually hold any data.

If you were to create a business
object and add a field called "customerName" with
type "string", you can now actually do something
with the business object. With the addition of each new field, the
usefulness of the business object increases. For example, if you were
to add, "customerID" of type "int", customerAddress of
type "string", you now have a business object with
useful information in it to use however you would like. You can pass
it to a web service for example, to run a credit check on a customer.
You may even choose to have your business object contain "salesContact"
that has a type "Employee" - another business object.
A business object can contain other business objects as data too,
meaning that if needed, business objects can be very complex containers
of data.

## Business object programming model

- The business object definition and instance data
- A set of services that support the operations on the business
objects

Business object type definitions are represented by the commonj.sdo.Type
and commonj.sdo.Property interfaces. The business object programming
model provides a set of rules for mapping the XML schema complex type
information to the Type interface and each of the elements in the
complex type definition to the Property interface.

Business
object instances are represented by the commonj.sdo.DataObject interface.
The business object programming model is untyped, which means that
the same commonj.sdo.DataObject interface can be used to represent
different business object definitions, such as Customer and Order.
The definition of which properties can be set and retrieved from each
business object is determined by type information defined in the XML
schema associated with each business object.

The business object
programming model behavior is based on the Service Data Object 2.1
specification. For additional information, see the SDO 2.1 for Java
specification, tutorials and javadocs on the web: http://www.oasis-opencsa.org/.

Business
object services support various lifecycle operations (such as creation,
equality, parsing, and serialization) on business objects.

For
specifics on the business object programming model, see the  Generated API and SPI documentation on business objects.

## Bindings, data bindings, and data handlers

In some cases,
such as the web service binding, the binding used to export and import
services automatically transforms the data into the appropriate format.
In other cases, such as the JMS binding, developers can provide a
data binding or data handler that converts non-native formats into
business objects represented by the DataObject interface.

For
more information on developing data bindings and data handlers, refer
to Data handlers and Data bindings.