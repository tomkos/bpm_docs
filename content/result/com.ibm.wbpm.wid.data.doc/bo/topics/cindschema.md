<!-- image -->

# Support for schemas from industry standard organizations

- xsd:any
- xsd:anyType
- xsd:anySimpleType

- Supported XSD and WSDL artifacts

When a WSDL or a schema is imported into a project in IBM Integration Designer, the business objects rendered from the WSDL or schema can then be used to develop a module. It is important to note however, that only certain artifacts from a schema are rendered as business objects (for example, root/top level elements and named complex types). Certain artifacts, such as nested anonymous complex types, are not rendered as business objects. These restrictions are a result of which artifacts are accessible in the XML schema. For example, if you import a schema which resulted in only one business object, it is most likely that the rest of the elements were anonymous complex types. The following information details which XSD and WSDL artifacts will result in business objects.
- SimpleType support in the business object editor

Enabling support for simpleTypes allows business objects to inherit from a string type (instead of only from another business object).