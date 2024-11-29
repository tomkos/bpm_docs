<!-- image -->

# Modeling business objects

- Target namespace definition

Most business and communications problems that XML can solve require a combination of several XML vocabularies. XML has a mechanism for qualifying names to be allocated into different namespaces, such as namespaces that apply to different industries. In XML, a uniform resource identifier (URI) provides a unique name to associate with the element, attribute, and type definitions in an XML schema.
- Business object definition

IBM Business Automation Workflow provides a flexible mechanism for defining or importing business objects.
- Business object property definition

XML schema provides complex types, simple types, and attributes, which are used to build business objects.
- Supported XSD and WSDL artifacts

When a WSDL or a schema is imported into a project in IBM Integration Designer, the business objects rendered from the WSDL or schema can then be used to develop a module. It is important to note however, that only certain artifacts from a schema are rendered as business objects (for example, root/top level elements and named complex types). Certain artifacts, such as nested anonymous complex types, are not rendered as business objects. These restrictions are a result of which artifacts are accessible in the XML schema. For example, if you import a schema which resulted in only one business object, it is most likely that the rest of the elements were anonymous complex types. The following information details which XSD and WSDL artifacts result in business objects.
- Flat and hierarchical business objects

Business objects can be modeled as flat or as hierarchical.
- Business object characteristics

Business objects have inherent characteristics that enhance their use within the business object framework.