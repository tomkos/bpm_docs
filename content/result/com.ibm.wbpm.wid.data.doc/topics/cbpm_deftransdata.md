<!-- image -->

# Defining and transforming data

- Defining data objects

There are two types of data objects in IBM® Integration Designer; business objects are containers for application (or payload) data related to business functions, such as a customer or an invoice. Business objects are based on a data-access technology called Service Data Objects.Service message objects contain business objects in addition to contextual data such as SOAP header information. The underlying structure of a business object is an XML schema definition (XSD).
- Transforming data

When you are integrating services, you often need to transform the data into a format that the receiving service can process. Typically, interfaces and operations of disparate services are not identical, and the message from the source needs to be transformed into a format that can be accepted by the target. Or, you may want to manipulate the data that you are moving between the source and target. You can use XML maps or business object maps to transform your data.
- Creating and mapping interfaces

Interfaces are the means of exchanging data between components.
- Creating relationships

When attributes in a source and destination data type contain equivalent data that is represented differently, the transformation step employs a relationship. The relationship editor is used to model and design business integration relationships and roles.