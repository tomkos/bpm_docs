<!-- image -->

# Working with the IBM business object framework

Table 1 summarizes how the basic types of data
are implemented in the business object framework.

| Data Abstraction   | Implementation                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Instance data      | Business object                                  | Business objects are the primary mechanism for representing business entities, or document literal message definitions, enabling everything from a simple basic object with scalar properties to a large complex hierarchy or graph of objects. A business object is a direct corollary to the SDO DataObject concept.                                                                                                |
| Instance metadata  | Business graph                                   | Business graphs are wrappers that are added around a simple business object or a hierarchy of business objects to provide additional capabilities, such as carrying change summary and event summary information related to the business objects in the business graph. A business graph is a direct corollary of the SDO DataGraph concept, except that it provides more than just the single change summary header. |
| Type metadata      | Enterprise metadataBusiness object type metadata | Business object type metadata is the metadata that can be added to business object definitions to enhance their value in the runtime. These metadata items are added to the business object's XML schema definition as well known xs:annotation and xs:appinfo elements.                                                                                                                                              |
| Services           | Business object services (APIs)                  | Business object services are a set of capabilities provided in addition to the basic capabilities provided by Service Data Objects. Examples are services such as create, copy, equality, and serialization. These APIs are found in the com.ibm.websphere.bo package.                                                                                                                                                |

The IBM® Business Automation Workflow business object framework is
an extension of the SDO standard. Therefore, business objects exchanged between IBM Business Automation Workflow components are instances of the
commonj.sdo.DataObject class. However, the IBM Business Automation Workflow business object framework adds several
services and functions that simplify and enrich the basic DataObject functionality.

To facilitate the creation and manipulation of business objects, the WebSphere® business object framework extends SDO specifications by
providing a set of Java™ services. These services are part of
the package named com.ibm.websphere.bo.

- BOFactory: The key service that provides various ways to create instances of business
objects.
- BOXMLSerializer: Provides ways to "inflate" a business object from a stream or to write
the content of a business object, in XML format, to a stream.
- BOCopy: Provides methods that make copies of business objects ("deep" and "shallow"
semantics).
- BODataObject: Gives you access to the data object aspects of a business object, such as
the change summary, the business graph, and the event summary.
- BOXMLDocument: The front end to the service that lets you manipulate the business object
as an XML document.
- BOChangeSummary and BOEventSummary: Simplifies access to and manipulation of the
change summary and event summary portion of a business object.
- BOEquality: A service that enables you to determine whether two business objects contain
the same information. It supports both deep and shallow equality.
- BOType and BOTypeMetaData: These services materialize instances of the
commonj.sdo Type and let you manipulate the associated metadata. Instances of Type
can then be used to create business objects "by type".
- BOInstanceValidator: Validates the data in a business object to see if it conforms to the
XSD.