<!-- image -->

# Programming techniques

- Arrays in business objects

You can define arrays for an element in a business object so that the element can contain more than one instance of data.
- Creating nested business objects

You can use the setWithCreate function to create nested business objects within a parent business object.
- Differentiating identically named elements

You must provide unique names for business object elements and attributes.
- Differentiating identically named properties

When multiple XSDs with the same namespace define the same named types, an incorrect type can be accidentally referenced.
- Resolving property names that contain periods

Property names in an XSD may contain a period (".") as one of many valid characters, while in a SDO they are also used to show indexing in a property of multiple cardinality. This may cause resolution problems in certain situations.
- Support for null business objects

This scenario involves an outside system communicating with IBM® Business Automation Workflow through XML wrapped inside of a SOAP message. When the enclosed element is nillible and has xsi:nil="true", then the resulting DataObject which is created in IBM Business Automation Workflow is null.
- Using the Sequence object to set data order

Some XSDs are defined in a way that makes the order that the data occurs in the XML have special significance.
- Using Any data types

This section provides programming techniques for using Any data types.

<!-- image -->