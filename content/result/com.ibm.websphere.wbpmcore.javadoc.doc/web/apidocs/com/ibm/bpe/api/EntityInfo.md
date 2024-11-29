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

## Interface EntityInfo

- All Superinterfaces:
java.io.Serializable

public interface EntityInfo
extends java.io.Serializable
Provides information about an entity that is returned as a result of a query
 against a query table.
Since:
6.2.0.1 - introduced in 6.2

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

java.util.List
getAttributeInfo()
Returns information about the selected attributes of the entity.

java.lang.String
getEntityTypeName()
Returns the type of entity.

java.util.List
getKeyAttributeInfo()
Returns information about the key attributes of the entity

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getEntityTypeName
java.lang.String getEntityTypeName()
Returns the type of entity.
Returns:The type of the entity.
    - getAttributeInfo
java.util.List getAttributeInfo()
Returns information about the selected attributes of the entity.
 
Returns:A list of AttributeInfo objects that describe the attributes that are selected for the entity.
    - getKeyAttributeInfo
java.util.List getKeyAttributeInfo()
Returns information about the key attributes of the entity
 
Returns:A list of AttributeInfo objects that describe the key attributes of the entity.