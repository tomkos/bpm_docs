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

## Interface BOXMLDocument

- public interface BOXMLDocument The BOXMLDocument interface provides the client programming model for a Business Document. The Business Document can be created in one of two ways: The BOFactory mechanism enables the creation of a Business Document in memory from an XML Schema global element definition. The BOXMLSerializer mechanism enables the creation of a Business Document in memory by composing together a root element, its target namespace, and an existing Business Object. Business Documents can be serialized and deserialized using the BOXMLSerialization service.

```
public interface BOXMLDocument
```

Using BOFactory.createXMLDocument
 Using BOXMLSerializer.createXMLDocument
 

 The BOFactory mechanism enables the creation of a Business Document
 in memory from an XML Schema global element definition.

 The BOXMLSerializer mechanism enables the creation of a Business Document
 in memory by composing together a root element, its target namespace, and
 an existing Business Object.

 Business Documents can be serialized and deserialized using the
 BOXMLSerialization service.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

commonj.sdo.DataObject
getDataObject()
Returns the Business Object associated with the Business Document.

java.lang.String
getEncoding()
Returns the XML encoding of the Business Document.

java.lang.String
getRootElementName()
Returns the name of the root element of the Business Document.

java.lang.String
getRootElementURI()
Returns the target namespace of the Business Document.

java.lang.String
getXMLVersion()
Returns the XML version of the Business Document, or null if it is
 not specified.

void
setEncoding(java.lang.String encoding)
Sets the XML encoding of the Business Document.

void
setXMLVersion(java.lang.String xmlVersion)
Sets the XML version of the Business Document.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getDataObject
commonj.sdo.DataObject getDataObject()
Returns the Business Object associated with the Business Document.
Returns:The Business Object from the Business Document
    - getRootElementURI
java.lang.String getRootElementURI()
Returns the target namespace of the Business Document.
 If null is returned, it represents the null target namespace.
Returns:The target namespace from the Business Document
    - getRootElementName
java.lang.String getRootElementName()
Returns the name of the root element of the Business Document.
Returns:The root element name from the Business Document
    - getXMLVersion
java.lang.String getXMLVersion()
Returns the XML version of the Business Document, or null if it is
 not specified.
Returns:The XML version of the Business Document
    - setXMLVersion
void setXMLVersion(java.lang.String xmlVersion)
Sets the XML version of the Business Document.
Parameters:The - XML version of the Business Document
    - getEncoding
java.lang.String getEncoding()
Returns the XML encoding of the Business Document.
 The default encoding is UTF-8.
Returns:The encoding of the Business Document
    - setEncoding
void setEncoding(java.lang.String encoding)
Sets the XML encoding of the Business Document.
Parameters:encoding - The XML encoding of the Business Document