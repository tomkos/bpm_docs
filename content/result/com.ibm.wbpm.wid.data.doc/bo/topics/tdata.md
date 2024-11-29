<!-- image -->

# Defining data objects

## About this task

The following topics provide key concepts and step-by-step instructions for creating and editing data in IBM Integration
Designer.

- Business objects

A business object (BO) is a container for application data, such as a customer or an invoice. Data is exchanged between components by business objects. The underlying structure of a business object is an XML schema definition (XSD).
- Business objects and XML Schema definitions (XSDs)

Business objects are logical constructs of XSDs (XML Schema definitions). When you create or import an XSD file, a business object is created for each typed or anonymous complexType in the XSD.
- Service message objects

Service message objects are enhanced business objects that include the application data and header information related to the transport protocol used to invoke a service such as SOAP or JMS. A service message object is composed of a body that contains the application data (also known as the payload or operation message) in a business object, and headers containing additional context information.
- Business object editor

You can use the business object editor inIBM Integration Designer to build and edit business objects.
- Creating business objects in Integration Designer

Data is defined by business objects. You can create business objects using the New Business Object wizard, or by creating or importing XSD files.
- Editing business objects

You can edit existing business objects using the business object editor in IBM Integration Designer.
- Support for schemas from industry standard organizations

IBM Integration Designer supports the use of schemas provided by industrial standard organizations, such as HL7, ACORD and OAGIS. xsd:anySimpleType can now be used to refer to any XSD simple type, xsd:anyType can be used to refer to any complexType or simpleType, while xsd:any can be used to refer to any elements.  xsd:anyAttribute can be used to refer to any XSD global attribute definition.
- Artifact evolution for business objects

Artifact evolution is used to introduce new versions of existing artifacts to IBM Integration Designer and is supported for business objects.
- Considerations when creating or using business objects

There are a number of considerations and limitations for creating and programming with business objects.
- Business graphs

Business graphs are wrappers that are added around a business object, or around a hierarchy of business objects, to provide additional capabilities. For example, you could carry Change Summary and Event Summary information related to the business object in the business graph.