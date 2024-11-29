<!-- image -->

# Business object characteristics

## Cardinality

The cardinality of properties is defined by standard XML schema minOccurs and
maxOccurs facets for simple and complex types and the use
attribute for attributes.

## Default property values

The capability to provide default values in XML schema for attributes and simple types in a
business object is supported by the business object framework. This support is visible at creation
time when the simple property types of a business
object reflect their
default values.

## Nillable

An element can be defined in XML schema to be
nillable.
The business object framework enables properties that are nillable to have their
value set to Null at run time.

## Key definition

Business object key information can be used by multiple subsystems, such as relationship,
sequencing, and isolation. However, each of these subsystems can define their own key mechanism
independent of the business
object's
key definition. Since the underlying model language
leveraged
by business objects is XML schema, first class support for key definitions exists within the
modeling language. However, this support within the modeling language is not fully supported in the
SDO run time.

- They can define compound keys.
- They can define unique constraints that are relative to a portion of the document.

Although a business object is not required to have a defined key, it is highly recommended.
Business objects that do not define a key can be used by applications.
This
scenario is a common use model in many Java EE centric applications use models, where JavaBeans are passed back and forth between the servlet and
EJB containers without the specification of a
key.
However, those business objects that do not define a key are unable to interact with the subsystems
that require a key.
This
situation limits their ability to take advantage of IBM® Business Automation Workflow qualities of service.