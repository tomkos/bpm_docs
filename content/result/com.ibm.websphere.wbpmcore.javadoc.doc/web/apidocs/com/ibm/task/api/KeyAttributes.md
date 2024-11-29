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

## Interface KeyAttributes

- All Superinterfaces:
java.io.Serializable

public interface KeyAttributes
extends java.io.Serializable
Provides information about key attributes.
 
 A key attribute is part of an entity which is returned as a result of a query
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

java.util.List
getKeyAttributeInfo()
Returns information about the key attributes.

java.io.Serializable[]
getValues()
Returns the values of the key attributes.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getValues
java.io.Serializable[] getValues()
Returns the values of the key attributes.
Returns:Serializable[] - the values of the key attributes.
    - getKeyAttributeInfo
java.util.List getKeyAttributeInfo()
Returns information about the key attributes.
Returns:List - a list of AttributeInfo objects describing the key attributes.