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

## Interface BOTypeMetadata

- public interface BOTypeMetadata
The BOTypeMetadata interface represents the client programming model
 interface for the BOTypeMetadata service.  The BOTypeMetadata service
 provides the ability to transform an annotation String into a Business
 Object and a Business Object back to an annotation String.

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
transformAnnotationToDataObject(java.lang.String annotationString)
Returns the Business Object deserialized from the value of the
 annotation.

java.lang.String
transformDataObjectToAnnotation(commonj.sdo.DataObject dataObject)
Serializes the DataObject into an XML Schema annotation value and retuns
 the annotation as a string.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - transformAnnotationToDataObject
commonj.sdo.DataObject transformAnnotationToDataObject(java.lang.String annotationString)
                                                       throws java.io.IOException
Returns the Business Object deserialized from the value of the
 annotation.
Parameters:annotationString - The annotation String
Returns:The Business Object
Throws:
java.io.IOException
    - transformDataObjectToAnnotation
java.lang.String transformDataObjectToAnnotation(commonj.sdo.DataObject dataObject)
                                                 throws java.io.IOException
Serializes the DataObject into an XML Schema annotation value and retuns
 the annotation as a string.
Parameters:dataObject - The Business Object
Returns:The annotation string
Throws:
java.io.IOException