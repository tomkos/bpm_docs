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

## Class QueryHelper

- java.lang.Object
    - com.ibm.task.api.QueryHelper

- public class QueryHelper
extends java.lang.Object
Helper class to support native SQL requests against the ProcessChoreographer database.
 This class provides methods that help to build native SQL select statements and
 to understand the results of the query.
Since:
6.1.2

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description static java.lang.String convertGroupIfNeeded (java.lang.String group, int direction, java.util.Locale locale) Converts the specified group name to lower or upper case or leaves it unchanged depending on the direction and locale values. static java.util.List convertGroupsIfNeeded (java.util.List groups, int direction, java.util.Locale locale) Converts the specified group names to lower or upper case or leaves them unchanged depending on the direction and locale values. static java.lang.String convertUserIfNeeded (java.lang.String user, int direction, java.util.Locale locale) Converts the specified user ID to lower or upper case or leaves it unchanged depending on the direction and locale values. static java.util.List convertUsersIfNeeded (java.util.List users, int direction, java.util.Locale locale) Converts the specified user IDs to lower or upper case or leaves them unchanged depending on the direction and locale values. static OID toOID (byte[] id) Creates an OID object from its byte array representation. static OID toOID (java.lang.String id) Creates an OID object from its string representation.

### Method Summary

| Modifier and Type       | Method and Description                                                                                                                                                                                                                                            |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static java.lang.String | convertGroupIfNeeded(java.lang.String group,                     int direction,                     java.util.Locale locale) Converts the specified group name to lower or upper case or leaves it unchanged   depending on the direction and locale values.      |
| static java.util.List   | convertGroupsIfNeeded(java.util.List groups,                      int direction,                      java.util.Locale locale) Converts the specified group names to lower or upper case or leaves them unchanged   depending on the direction and locale values. |
| static java.lang.String | convertUserIfNeeded(java.lang.String user,                    int direction,                    java.util.Locale locale) Converts the specified user ID to lower or upper case or leaves it unchanged   depending on the direction and locale values.             |
| static java.util.List   | convertUsersIfNeeded(java.util.List users,                     int direction,                     java.util.Locale locale) Converts the specified user IDs to lower or upper case or leaves them unchanged   depending on the direction and locale values.        |
| static OID              | toOID(byte[] id) Creates an OID object from its byte array representation.                                                                                                                                                                                        |
| static OID              | toOID(java.lang.String id) Creates an OID object from its string representation.                                                                                                                                                                                  |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait