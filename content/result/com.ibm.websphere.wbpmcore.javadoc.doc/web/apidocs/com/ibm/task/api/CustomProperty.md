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

## Interface CustomProperty

- All Superinterfaces:
java.io.Serializable

All Known Subinterfaces:
InlineCustomProperty

public interface CustomProperty
extends java.io.Serializable
Describes a named custom property.
 
 Custom properties allow a user to add additional properties to an object beyond
 those provided and managed by the Human Task Manager.
Since:
6.0

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
Returns the name of the custom property.

java.lang.String
getValue()
Returns the value of the custom property.

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
    - getValue
java.lang.String getValue()
Returns the value of the custom property.
Returns:The value of the custom property.