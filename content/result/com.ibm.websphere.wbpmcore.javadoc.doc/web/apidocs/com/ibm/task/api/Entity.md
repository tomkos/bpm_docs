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

## Interface Entity

- All Superinterfaces:
java.io.Serializable

public interface Entity
extends java.io.Serializable
Describes an entity that is returned as the result of an entity-based query request
 against a query table.
Since:
7.0

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

java.io.Serializable
getAttributeValue(java.lang.String attributeName)
Returns the value of the specified attribute.

java.io.Serializable[]
getAttributeValuesOfArray(java.lang.String attributeName)
Returns the values of the specified array attribute.

EntityInfo
getEntityInfo()
Returns type information of the entity.

KeyAttributes
getKeyAttributes()
Returns the values and definitions of the key attributes.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getEntityInfo
EntityInfo getEntityInfo()
Returns type information of the entity.
Returns:The information about the entity.
    - getAttributeValue
java.io.Serializable getAttributeValue(java.lang.String attributeName)
Returns the value of the specified attribute.
 
Parameters:attributeName - The name of the attribute whose value is to be retrieved.
 
Returns:The attribute value. If the value is not set for the entity, null is returned.
    If the attribute is no single-valued attribute but an array, a Serializable[] is returned.
 
Throws:
java.lang.IllegalArgumentException - If the attribute name is null or if the attribute does not exist.
    - getAttributeValuesOfArray
java.io.Serializable[] getAttributeValuesOfArray(java.lang.String attributeName)
Returns the values of the specified array attribute.
 
Parameters:attributeName - The name of the attribute whose values are to be retrieved.
 
Returns:The attribute value. If the value is not set for the entity, an empty array is returned.
 
Throws:
java.lang.IllegalArgumentException - If the attribute name is null or if the attribute does not exist or
    if the attribute name specifies a single-valued attribute.
    - getKeyAttributes
KeyAttributes getKeyAttributes()
Returns the values and definitions of the key attributes.
 
Returns:KeyAttributes - The key attribute values and definitions.