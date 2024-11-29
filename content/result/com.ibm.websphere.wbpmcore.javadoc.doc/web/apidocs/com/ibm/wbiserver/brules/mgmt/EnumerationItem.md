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

## Interface EnumerationItem

- All Superinterfaces:
java.io.Serializable

public interface EnumerationItem
extends java.io.Serializable
This interface represents a single valid value in an enumeration constraint.

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
getUserPresentation()
Get the user presentation for this enumeration item.

java.lang.String
getValue()
Get the value of this enumeration item as a string.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getUserPresentation
java.lang.String getUserPresentation()
Get the user presentation for this enumeration item.  If not null, this is the string that 
 should be used to display this enumeration item to the user.
Returns:The user presentation string for this enumeration item or null if no user
 presentation string is set.
    - getValue
java.lang.String getValue()
Get the value of this enumeration item as a string.  If the type of the associated parameter
 is not string, then the returned string value can be parsed into the type expected by the 
 parameter using standard Java conversion methods.  For example, if the type of the 
 associated parameter is boolean, then the string value can be converted to a boolean type 
 using the Boolean.valueOf() method.
Returns:The value of this enumeration item as a string.