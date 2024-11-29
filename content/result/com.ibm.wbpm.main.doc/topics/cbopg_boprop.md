<!-- image -->

# Business object property definition

Complex type definitions, anonymous complex type definitions, and elements referencing complex
type definitions are used to define the outer business objects. The term property is used to define
the data inside a business object. The term is derived from the Service Data Object term property,
and is defined by the commonj.sdo.Property interface. It is synonymous with the
concept of an attribute.

A property can either be simple or complex. A simple property can be defined either as an XML
schema attribute, or as an XML schema element with a type that is an XML schema simple type. A
complex property can either reference another business object, or it can define a complex structure
within the current business object.

Figure 1. XML schema simple types

<!-- image -->