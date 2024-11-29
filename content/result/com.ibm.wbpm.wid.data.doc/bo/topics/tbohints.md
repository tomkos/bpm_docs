<!-- image -->

# Considerations when creating or using business objects

- Considerations when using the business object editor

There are a number of considerations when using the business object editor.
- Hints and tips for the Business Object editor

There are a number of hints and tips that help when using the Business Object editor.
- Considerations when choosing the business object parsing mode

The business object parsing mode determines how XML data is parsed at run time. A business object parsing mode is defined on a module or library when it is created. You can change the parsing mode of the module or library, however you should be aware of the implications.
- Duplicate business objects

Duplicate business objects are caused when more than one complexType elements with the same namespace are present in multiple XML Schema Definition (XSD) or Web Services Description Language (WSDL) files in the same module or library. As a result, the business object that is created at run time might have the wrong definition.
- Concurrent access for business objects

IBM Workflow Server does not support concurrent access of business object instances for read or write operations. Processing the same business object instance in multiple threads for read and write operations can lead to data corruption.
- ElementFormDefault definition

The elementFormDefault is a schema property that defines how the types would be qualified for a given schema definition.  For any schema created in IBM Integration Designer, by default this property is not specified, and the property is treated as unqualified.
- Limitations of business objects

There are limitations that you should be aware of when using the business object editor, or when working with business objects.