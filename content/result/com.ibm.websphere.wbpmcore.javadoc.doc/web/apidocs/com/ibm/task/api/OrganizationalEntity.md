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

## Interface OrganizationalEntity

- All Superinterfaces:
PeopleAssignment, java.io.Serializable

public interface OrganizationalEntity
extends PeopleAssignment
Describes an organizational entity.
 
 An organizational entity specifies user or group information when
 assigning people to a human task or a work basket.
 
 The OrganizationalEntity interface is modelled after the data type in WS-HumanTask.
Since:
6.2.0.3

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
getGroups()
Returns the groups that are used to determine the users that make up this organizational entity.

java.util.List
getUsers()
Returns the user IDs of the users that make up this organizational entity.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getUsers
java.util.List getUsers()
Returns the user IDs of the users that make up this organizational entity.
Returns:The userIDs of the users contained in this organizational entity.
    Returns an empty list when there are no users in this organizational entity.
    - getGroups
java.util.List getGroups()
Returns the groups that are used to determine the users that make up this organizational entity.
Returns:The names of the groups contained in this organizational entity.
    Returns an empty list when there are no groups in this organizational entity.