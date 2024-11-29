<!-- image -->

# Considerations when using the business object editor

- You can rename business objects and fields in the business object
editor when you initially create them. Once you have built the business
objects into an application, you should always use refactoring to
ensure that you do not break any dependencies.
- IBM® IntegrationDesigner 's best practices when authoring XML Schema files to create ones own type library: Also, the business object editor can use either the first orsecond definitions, that is complex type definitions or root-levelelements with anonymous complex type definitions.
    - Avoid the use of private business objects (nested anonymous complex
types) to promote the reuse of business objects.
    - Do not use elements and complex type definitions with the same
name in the same XML Schema or WSDL file.
    - Define complex types in XML Schema files, not WSDL definitions,
to create a type library concept.