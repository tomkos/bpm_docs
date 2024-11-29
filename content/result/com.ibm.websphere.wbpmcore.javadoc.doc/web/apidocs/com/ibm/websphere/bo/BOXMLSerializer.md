- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Interface BOXMLSerializer

- public interface BOXMLSerializer The BOXMLSerializer interface represents the client programming model interface for the BOXMLSerializer service. The BOXMLSerializer service provides the following capabilities: The key elements of a Business Document consist of the name and target namespace of the root element housing the business document and the DataObject contained in the business object. These three elements which represent the Business Document are required for serialization. It is for this reason that the creation operation is provided, to aggregate these elements into a BOXMLDocument that can then be serialized. In addition, BOXMLSerializer also provides a helper operation that enables the three elements to be provided directly to the serialization operation. The deserialization of the Business Document results in a BOXMLDocuemnt. From that document, the DataObject can be retrieved and utilized. Note: Some of the operations take options, however, in the initial release of the product there are currently no supported options.

```
public interface BOXMLSerializer
```

creation of a Business Document from a DataObject,
 serialization/deserialization of a Business Document, and
 serialization/deserialization of a DataObject.
 

 The key elements of a Business Document consist of the name and target
 namespace of the root element housing the business document and the
 DataObject contained in the business object.  These three elements which
 represent the Business Document are required for serialization.  It is
 for this reason that the creation operation is provided, to aggregate
 these elements into a BOXMLDocument that can then be serialized.  In
 addition, BOXMLSerializer also provides a helper operation that enables
 the three elements to be provided directly to the serialization
 operation.

 The deserialization of the Business Document results in a BOXMLDocuemnt.
 From that document, the DataObject can be retrieved and utilized.

 Note: Some of the operations take options, however, in the initial release
 of the product there are currently no supported options.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static java.lang.String
SCHEMALOCATION
    - Method Summary

Methods 

Modifier and Type
Method and Description

BOXMLDocument
createXMLDocument(commonj.sdo.DataObject businessObject,
                 java.lang.String targetNamespace,
                 java.lang.String rootElementName)
Creates a BOXMLDocument representing a Business Document consisting of
 a root element name and its target namespace, and the contained
 DataObject.

BOXMLDocument
readXMLDocument(java.io.InputStream inputStream)
Deserializes the Business Document from an input stream.

BOXMLDocument
readXMLDocumentWithOptions(java.io.InputStream inputStream,
                          java.lang.Object options)
Deserializes the Business Document from an input stream with options.

void
writeDataObject(commonj.sdo.DataObject businessObject,
               java.lang.String targetNamespace,
               java.lang.String rootElementName,
               java.io.OutputStream outputStream)
Serializes the Business Document consisting of a root element name
 and target namespace and the containing DataObject to the specified
 output stream.

void
writeDataObjectWithOptions(commonj.sdo.DataObject businessObject,
                          java.lang.String targetNamespace,
                          java.lang.String rootElementName,
                          java.io.OutputStream outputStream,
                          java.lang.Object options)
Serializes the Business Document consisting of a root element name
 and target namespace and the containing DataObject to the specified
 output stream with options.

void
writeXMLDocument(BOXMLDocument businessDocument,
                java.io.OutputStream outputStream)
Serializes the Business Document as a XML v1.0 stream to the
 specified output stream.

void
writeXMLDocumentWithOptions(BOXMLDocument businessDocument,
                           java.io.OutputStream outputStream,
                           java.lang.Object options)
Serializes the Business Document as a XML v1.0 stream to the
 specified output stream with options.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- SCHEMALOCATION
static final java.lang.String SCHEMALOCATION
See Also:Constant Field Values

- Method Detail

### Method Detail

    - createXMLDocument
BOXMLDocument createXMLDocument(commonj.sdo.DataObject businessObject,
                              java.lang.String targetNamespace,
                              java.lang.String rootElementName)
Creates a BOXMLDocument representing a Business Document consisting of
 a root element name and its target namespace, and the contained
 DataObject.
Parameters:businessObject - The DataObject portion of the Business DocumenttargetNamespace - The target namespace of the Business DocumentrootElementName - The root element name of the Business Document
Returns:The created Business Document
    - writeXMLDocument
void writeXMLDocument(BOXMLDocument businessDocument,
                    java.io.OutputStream outputStream)
                      throws java.io.IOException
Serializes the Business Document as a XML v1.0 stream to the
 specified output stream.
Parameters:businessDocument - The Business Document to serializeoutputStream - The target output stream for the XML v1.0 stream
Throws:
java.io.IOException
    - writeXMLDocumentWithOptions
void writeXMLDocumentWithOptions(BOXMLDocument businessDocument,
                               java.io.OutputStream outputStream,
                               java.lang.Object options)
                                 throws java.io.IOException
Serializes the Business Document as a XML v1.0 stream to the
 specified output stream with options.
 "options" is a placeholder for passing in any serialization options in future.
 There are no options that are currently supported.
Parameters:businessDocument - The Business Document to serializeoutputStream - The target output stream for the XML v1.0 streamoptions - Serialization options
Throws:
java.io.IOException
    - writeDataObject
void writeDataObject(commonj.sdo.DataObject businessObject,
                   java.lang.String targetNamespace,
                   java.lang.String rootElementName,
                   java.io.OutputStream outputStream)
                     throws java.io.IOException
Serializes the Business Document consisting of a root element name
 and target namespace and the containing DataObject to the specified
 output stream.
Parameters:businessObject - The Business ObjecttargetNamespace - The target namespace of the Business DocumentrootElementName - The root element name of the Business DocumentoutputStream - The target output stream
Throws:
java.io.IOException
    - writeDataObjectWithOptions
void writeDataObjectWithOptions(commonj.sdo.DataObject businessObject,
                              java.lang.String targetNamespace,
                              java.lang.String rootElementName,
                              java.io.OutputStream outputStream,
                              java.lang.Object options)
                                throws java.io.IOException
Serializes the Business Document consisting of a root element name
 and target namespace and the containing DataObject to the specified
 output stream with options.
 "options" is a placeholder for passing in any serialization options in future.
 There are no options that are currently supported.
Parameters:businessObject - The Business ObjecttargetNamespace - The target namespace of the Business DocumentrootElementName - The root element name of the Business DocumentoutputStream - The target output streamoptions - Serialization options
Throws:
java.io.IOException
    - readXMLDocument
BOXMLDocument readXMLDocument(java.io.InputStream inputStream)
                              throws java.io.IOException
Deserializes the Business Document from an input stream.
Parameters:inputStream - The source input stream
Returns:The deserialized Business Document
Throws:
java.io.IOException
    - readXMLDocumentWithOptions
BOXMLDocument readXMLDocumentWithOptions(java.io.InputStream inputStream,
                                       java.lang.Object options)
                                         throws java.io.IOException
Deserializes the Business Document from an input stream with options.
 "options" is a placeholder for passing in any deserialization options in future.
 There are no options that are currently supported.
Parameters:inputStream - The source input streamoptions - Deserialization options
Returns:The deserialized Business Document
Throws:
java.io.IOException