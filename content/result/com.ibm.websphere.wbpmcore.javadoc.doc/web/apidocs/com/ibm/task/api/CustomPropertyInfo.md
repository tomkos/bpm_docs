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

## Interface CustomPropertyInfo

- All Superinterfaces:
java.io.Serializable

public interface CustomPropertyInfo
extends java.io.Serializable
Provides information about a custom property.
 
 Custom properties allow a user to add additional properties to an object beyond
 those provided and managed by the Human Task Manager.
Since:
6.1.2

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

int
getAssociatedObjectType()
Returns the object type of the object the custom property is set for.

java.lang.String
getName()
Returns the name of the custom property.

boolean
isBinary()
Indicates whether the custom property is a binary custom property or not.

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
Returns the name of the custom property.
Returns:The name of the custom property.
    - getAssociatedObjectType
int getAssociatedObjectType()
Returns the object type of the object the custom property is set for.
Returns:The associated object type - refer to ObjectType.
    - isBinary
boolean isBinary()
Indicates whether the custom property is a binary custom property or not.
Returns:True when the custom property is a binary custom property else false.