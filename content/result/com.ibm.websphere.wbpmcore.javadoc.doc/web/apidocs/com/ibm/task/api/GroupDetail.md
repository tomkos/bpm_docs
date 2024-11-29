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

## Interface GroupDetail

- All Superinterfaces:
java.io.Serializable

public interface GroupDetail
extends java.io.Serializable
Interface for accessing group details.
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

java.lang.String
getGroupName()
Returns the name of the group that is described by this object.

java.util.List
getProperty(java.lang.String property)
Returns the named group property.

java.util.List
getPropertyNames()
Returns the names of all group properties that are described by this object.

java.util.List
getSubgroupDetails()
Returns the description of subgroups directly contained in the group.

java.util.List
getUserDetails()
Returns the description of users directly contained in the group.

boolean
isInDirectory()
States whether the group is described in the people directory.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getGroupName
java.lang.String getGroupName()
Returns the name of the group that is described by this object.
Returns:The group name
    - isInDirectory
boolean isInDirectory()
States whether the group is described in the people directory.
Returns:True states that the group is found in the people directory.
    False states that the group is not found in the people directory, that is,
    properties are not returned.
    - getProperty
java.util.List getProperty(java.lang.String property)
Returns the named group property.
Parameters:property - The name of the group property that is to be returned.
Returns:The requested property. More than one string is returned when the property is multi-valued.
    - getPropertyNames
java.util.List getPropertyNames()
Returns the names of all group properties that are described by this object.
Returns:A list of group property names that are contained in this object.
    - getUserDetails
java.util.List getUserDetails()
Returns the description of users directly contained in the group.
Returns:A list of UserDetail objects. Returns an empty list when
    user details are not contained in this object.
    - getSubgroupDetails
java.util.List getSubgroupDetails()
Returns the description of subgroups directly contained in the group.
Returns:A list of GroupDetail objects. Returns an empty list when
    subgroup details are not contained in this object.