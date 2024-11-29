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

## Interface UserDetail

- All Superinterfaces:
java.io.Serializable

public interface UserDetail
extends java.io.Serializable
Interface for accessing user details.
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

java.util.List
getProperty(java.lang.String property)
Returns the named user property.

java.util.List
getPropertyNames()
Returns the names of all user properties that are described.

java.lang.String
getUserID()
Returns the user ID of the user that is described by this object.

boolean
isInDirectory()
States whether the user is described in the people directory.

boolean
isVirtualUser()
States whether the user is a virtual user.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getUserID
java.lang.String getUserID()
Returns the user ID of the user that is described by this object.
Returns:The user ID.
    - isInDirectory
boolean isInDirectory()
States whether the user is described in the people directory.
Returns:True states that the user is found in the people directory.
    False states that the user is not found in the people directory, that is,
    user properties are not returned.
    - isVirtualUser
boolean isVirtualUser()
States whether the user is a virtual user.
Returns:True states that the user is a virtual user.
    False states that the user is no virtual user.
    - getProperty
java.util.List getProperty(java.lang.String property)
Returns the named user property.
Parameters:property - The name of the user property that is to be returned.
Returns:The requested property. More than one string is returned when the property is multi-valued.
    - getPropertyNames
java.util.List getPropertyNames()
Returns the names of all user properties that are described.
Returns:A list of user property names that are contained in this object.