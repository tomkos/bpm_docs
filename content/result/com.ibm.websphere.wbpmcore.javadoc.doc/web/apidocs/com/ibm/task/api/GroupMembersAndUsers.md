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

## Interface GroupMembersAndUsers

- All Superinterfaces:
PeopleAssignment, java.io.Serializable

public interface GroupMembersAndUsers
extends PeopleAssignment
Describes a people assignment containing groups members and individual users.
 
 The GroupMemberAndUsers interface supports any number of groups and individual users.
 Each user has associated a personal work item.
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
Returns the groups that are used to determine the users that make up this object.

java.util.List
getUsers()
Returns the user IDs of the users that make up this object.

boolean
includeSubGroups()
Indicates if the members of subgroups should be included.

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
Returns the user IDs of the users that make up this object.
Returns:The userIDs of the users contained in this object.
    Returns an empty list when there are no users.
    - getGroups
java.util.List getGroups()
Returns the groups that are used to determine the users that make up this object.
Returns:The names of the groups contained in this object.
    Returns an empty list when there are no groups.
    - includeSubGroups
boolean includeSubGroups()
Indicates if the members of subgroups should be included.