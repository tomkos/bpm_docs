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

## Interface BOXSDHelper

- public interface BOXSDHelper
Provides access to additional information when the Type or Property is
 defined by an XML Schema (XSD). Methods return null/false otherwise or if the
 information is unavailable. Defines Types from an XSD.

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

commonj.sdo.Property
getGlobalProperty(java.lang.String uri,
                 java.lang.String propertyName,
                 boolean isElement)
Returns the Property defined by the named global element or attribute in
 the targetNamespace uri, or null if not found.

boolean
hasAnyAttribute(commonj.sdo.Type type)
Returns true if the Type contains an anyAttribute tag,
 or returns false if the Type does not.

boolean
isAttribute(commonj.sdo.Property property)
Returns true if the Property is derived from an attribute,
 or returns false otherwise

boolean
isElement(commonj.sdo.Property property)
Returns true if the Property is derived from an element,
 or returns false otherwise

boolean
isMixed(commonj.sdo.Type type)
Returns true if the Type is declared to contain mixed content.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - isMixed
boolean isMixed(commonj.sdo.Type type)
Returns true if the Type is declared to contain mixed content. A
 DataObject's mixed content values are typically accessed via a Sequence.
Parameters:type - to identify if mixed content.
Returns:true if the Type is declared to contain mixed content.
    - getGlobalProperty
commonj.sdo.Property getGlobalProperty(java.lang.String uri,
                                     java.lang.String propertyName,
                                     boolean isElement)
Returns the Property defined by the named global element or attribute in
 the targetNamespace uri, or null if not found.
Parameters:uri - The uri of the targetNamespace.propertyName - The name of the global property.isElement - is true for global elements, false for global attributes.
Returns:the Property defined by the named global element or attribute in
         the targetNamespace uri, or null if not found.
    - hasAnyAttribute
boolean hasAnyAttribute(commonj.sdo.Type type)
Returns true if the Type contains an anyAttribute tag,
 or returns false if the Type does not.
Parameters:type - to identify if the anyAttribute tag is present.
Returns:true if the Type contains an anyAttribute tag
    - isElement
boolean isElement(commonj.sdo.Property property)
Returns true if the Property is derived from an element,
 or returns false otherwise
Parameters:property - to identify if the Property is derived from an element
Returns:true if the Property is derived from an element
    - isAttribute
boolean isAttribute(commonj.sdo.Property property)
Returns true if the Property is derived from an attribute,
 or returns false otherwise
Parameters:property - to identify if the Property is derived from an attribute
Returns:true if the Property is derived from an attribute