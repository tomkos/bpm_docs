<!-- image -->

# Programming using business object services

This is a brief description of the business object services.

| Service                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BOChangeSummary               | Provides enhancements to the SDO change summary interface to manage the business graph's change summary header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| BOCopy                        | Facilitates copying a graph of business objects or a business graph that contains a graph of business objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| BODataObject                  | Provides enhancements to the SDO Data Object interface.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| BOEquality                    | Provides the ability to determine if two business graphs or business objects are equivalent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| BOEventSummary                | Provides the interface for managing the content of the business graph's event summary header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| BOFactory                     | Provides the capability to create a business graph or a business object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| BOMode                        | Provides access to the business object parsing mode configuration while the application is running. Use this API in the design for applications with logic that provides specific behavior for lazy or eager parsing mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| BOPrinter                     | Prints the business object content or type information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| BOType                        | Provides a mechanism to obtain the SDO type of a business graph or business object that mirrors what Class.forName() provides for Java class names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| BOTypeMetadata                | Provides the capability of taking an annotation binary large object (BLOB) that conforms to the BO Type Metadata pattern and transforms it into a set of SDO DataObjects (and performs the reserve transform).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| BOXMLDocument/BOXMLSerializer | Provides the mechanisms for creating and representing an XML Document in memory, and for serializing and de-serializing an XML document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| BOInstanceValidator           | Provides a facility to validate a business object instance against its XSD definition. Business objects can be present with various forms. They can be simple business objects or wrapped by the enriched business graph model. In certain business integration scenarios, the business objects are in the deleted section of change summary. These business objects drive the downstream business logics. The accuracy of the business objects need to be ensured in all cases. There are two supported styles for BOInstanceValidator: Explicit Programmatic Validation: A system service is provided to validate business objects via a set of programming APIs. Implicit Interface Validation: This validation is enabled/disabled via IBM® Integration Designer on the target interfaces via a SCA interface qualifier. |

- XML document validation

XML documents and business objects can be validated using the validation service.

<!-- image -->