<!-- image -->

# Mapping weakly typed elements

## Before you begin

When you map weakly typed elements where an element produced in one map might be used as input to
another map, be aware of the limitation described in XML map: Troubleshooting and limitations.

The payload of messages processed by mediation flows is defined as business objects, and is
carried in the body of the service message object (SMO). The business object definitions describe
the message structure in terms of the fields they contain, the type of each field, and the number of
occurrences of each field. A field in a business object can be a strong type, which means its type
and internal structure are known, or it can be a weak type, in which case the business object
definition allows more than one type of data to occur in the field.

The Set Message Type primitive allows you to 'overlay' message fields in the SMO with type
information that is different from the type described in the original business object definition.
This is useful when the business object definition contains weakly-typed field definitions, but you
know that content of a particular data type will be present in the instance message at run time.

You can manipulate strong-type fields more easily than weak-type because their structure and type
is known. Using the Set Message Type you can cast a weakly-typed field to a strongly typed field.
Primitives that are connected to the output terminal of Set Message Type can then access the
elements to which the any type element was cast. For example, you can use the XML map editor or the
business object map editor to view the fields with the type that was cast instead of xsd:any,
xsd:anyType, or xsd:anySimpleType. You can then manipulate the content of these fields.