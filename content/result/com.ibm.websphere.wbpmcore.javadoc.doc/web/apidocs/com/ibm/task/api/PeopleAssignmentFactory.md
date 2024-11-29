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

## Class PeopleAssignmentFactory

- java.lang.Object
    - com.ibm.task.api.PeopleAssignmentFactory

- public class PeopleAssignmentFactory
extends java.lang.Object
Factory to create people assignments, for example, an organizational entity.
Since:
6.2.0.3

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description GroupMembersAndUsers createByGroupMembersAndUsers (java.util.List users, java.util.List groups, boolean includeSubGroups) Creates an organizational entity from a list of groups and users. OrganizationalEntity createByLiteralGroup (java.lang.String group) Creates an organizational entity from a group of users. OrganizationalEntity createByLiteralGroups (java.util.List groups) Creates an organizational entity from groups of users. OrganizationalEntity createByLiteralUsers (java.util.List userIDs) Creates an organizational entity from a list of users. OrganizationalEntity createByLiteralUsersAndGroups (java.util.List userIDs, java.util.List groups) Creates an organizational entity from a list of users and a list of group of users. Everybody createEverybody () Creates an everybody people assignment. static PeopleAssignmentFactory newInstance () Returns the single instance of a PeopleAssignmentFactory.

### Method Summary

| Modifier and Type              | Method and Description                                                                                                                                                                                                        |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GroupMembersAndUsers           | createByGroupMembersAndUsers(java.util.List users,                             java.util.List groups,                             boolean includeSubGroups) Creates an organizational entity from a list of groups and users. |
| OrganizationalEntity           | createByLiteralGroup(java.lang.String group) Creates an organizational entity from a group of users.                                                                                                                          |
| OrganizationalEntity           | createByLiteralGroups(java.util.List groups) Creates an organizational entity from groups of users.                                                                                                                           |
| OrganizationalEntity           | createByLiteralUsers(java.util.List userIDs) Creates an organizational entity from a list of users.                                                                                                                           |
| OrganizationalEntity           | createByLiteralUsersAndGroups(java.util.List userIDs,                              java.util.List groups) Creates an organizational entity from a list of users and a list of group of users.                                 |
| Everybody                      | createEverybody() Creates an everybody people assignment.                                                                                                                                                                     |
| static PeopleAssignmentFactory | newInstance() Returns the single instance of a PeopleAssignmentFactory.                                                                                                                                                       |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait