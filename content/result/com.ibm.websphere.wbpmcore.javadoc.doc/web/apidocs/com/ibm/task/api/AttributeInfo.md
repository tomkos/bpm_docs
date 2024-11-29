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

## Interface AttributeInfo

- All Superinterfaces:
java.io.Serializable

All Known Subinterfaces:
AttributeMetaData

public interface AttributeInfo
extends java.io.Serializable
Provides information about an attribute of a query table.
 
 An attribute is part of an entity or row which is returned as a result of a query
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

java.lang.String
getName()
Returns the name of the attribute.

java.lang.String
getSourceAttributeName()
Returns the name of the source attribute.

java.lang.String
getSourceQueryTableIdentifier()
Returns the identifier of the query table that is the source of the attribute.

java.lang.String
getSourceQueryTableName()
Returns the name of the query table that is the source of the attribute.

AttributeType
getType()
Returns the type of the attribute.

boolean
isArray()
States whether the attribute is an array.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getName
java.lang.String getName()
Returns the name of the attribute.
Returns:The name of the attribute.
    - getType
AttributeType getType()
Returns the type of the attribute.
Returns:The type of the attribute.
    - isArray
boolean isArray()
States whether the attribute is an array.
Returns:boolean - True states that the attribute is an array of values. False states
    that the attribute is no array.
    - getSourceAttributeName
java.lang.String getSourceAttributeName()
Returns the name of the source attribute.
Returns:The name of the source attribute.
    - getSourceQueryTableName
java.lang.String getSourceQueryTableName()
Returns the name of the query table that is the source of the attribute.
Returns:The name of the source query table.
    - getSourceQueryTableIdentifier
java.lang.String getSourceQueryTableIdentifier()
Returns the identifier of the query table that is the source of the attribute.
Returns:The identifier of the source query table.