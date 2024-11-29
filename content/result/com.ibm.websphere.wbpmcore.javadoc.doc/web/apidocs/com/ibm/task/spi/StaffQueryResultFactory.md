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

## Class StaffQueryResultFactory

- java.lang.Object
    - com.ibm.task.spi.StaffQueryResultFactory

- public class StaffQueryResultFactory
extends java.lang.Object
This class provides for a factory that creates objects of
 StaffQueryResult and UserData.
Since:
6.0.2
Version:
6.1.0

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Constructor Summary

Constructors 

Constructor and Description

StaffQueryResultFactory()
    - Method Summary Methods Modifier and Type Method and Description static StaffQueryResultFactory newInstance () Creates an instance of the factory. StaffQueryResult newStaffQueryResult (java.util.Collection userData) Creates a new object of StaffQueryResult by specifying a set of users. StaffQueryResult newStaffQueryResult (java.util.Collection userData, java.lang.String[] groupIDs) Creates a new object of StaffQueryResult by specifying a set of users and an array of group IDs. StaffQueryResult newStaffQueryResult (int resultType) Creates a new object of StaffQueryResult by specifying the result type. StaffQueryResult newStaffQueryResult (java.util.Map userDataMap) Creates a new object of StaffQueryResult by specifying a map of users. StaffQueryResult newStaffQueryResult (java.lang.String groupID) Creates a new object of StaffQueryResult by specifying a group ID. StaffQueryResult newStaffQueryResult (java.lang.String[] groupIDs) Creates a new object of StaffQueryResult by specifying an array of group IDs. UserData newUserData (java.lang.String userID, java.util.Locale preferredLocale, java.lang.String eMailAddress) Creates a new object of UserData.

### Method Summary

| Modifier and Type              | Method and Description                                                                                                                                                                               |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static StaffQueryResultFactory | newInstance() Creates an instance of the factory.                                                                                                                                                    |
| StaffQueryResult               | newStaffQueryResult(java.util.Collection userData) Creates a new object of StaffQueryResult by specifying a set of users.                                                                            |
| StaffQueryResult               | newStaffQueryResult(java.util.Collection userData,                    java.lang.String[] groupIDs) Creates a new object of StaffQueryResult by specifying a set of users  and an array of group IDs. |
| StaffQueryResult               | newStaffQueryResult(int resultType) Creates a new object of StaffQueryResult by specifying the result type.                                                                                          |
| StaffQueryResult               | newStaffQueryResult(java.util.Map userDataMap) Creates a new object of StaffQueryResult by specifying a map of users.                                                                                |
| StaffQueryResult               | newStaffQueryResult(java.lang.String groupID) Creates a new object of StaffQueryResult by specifying a group ID.                                                                                     |
| StaffQueryResult               | newStaffQueryResult(java.lang.String[] groupIDs) Creates a new object of StaffQueryResult by specifying an array of group IDs.                                                                       |
| UserData                       | newUserData(java.lang.String userID,            java.util.Locale preferredLocale,            java.lang.String eMailAddress) Creates a new object of UserData.                                        |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait