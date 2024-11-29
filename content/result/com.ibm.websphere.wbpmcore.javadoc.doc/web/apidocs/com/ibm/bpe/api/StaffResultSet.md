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

## Interface StaffResultSet

- All Superinterfaces:
java.io.Serializable

public interface StaffResultSet
extends java.io.Serializable
Returns the persons or groups that are members of a specific role.
 
 The staff result set contains user or group IDs that belong to a specific role, for example,
 the process administrators of a process instance.
 If everybody or nobody is qualifying specifically, then no user or group IDs are provided.
 The result type indicates whether user or group IDs are provided or whether everybody
 or nobody is qualifying.
Since:
5.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
RESULT\_TYPE\_EVERYBODY
States that everybody is qualifying.

static int
RESULT\_TYPE\_GROUPIDS
States that group IDs are returned.

static int
RESULT\_TYPE\_NOBODY
States that no one is qualifying.

static int
RESULT\_TYPE\_USERIDS
States that user IDs are returned.

static int
RESULT\_TYPE\_USERIDS\_AND\_GROUPIDS
States that user and group IDs are returned.
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String[]
getGroupIDs()
Returns group IDs when the result type indicates that group IDs are returned.

int
getResultType()
Returns an indicator that describes the content of the staff result set.

java.lang.String[]
getUserIDs()
Returns user IDs when the result type indicates that user IDs are returned.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- RESULT\_TYPE\_NOBODY
static final int RESULT\_TYPE\_NOBODY
States that no one is qualifying.
See Also:Constant Field Values

- RESULT\_TYPE\_EVERYBODY
static final int RESULT\_TYPE\_EVERYBODY
States that everybody is qualifying.
See Also:Constant Field Values

- RESULT\_TYPE\_USERIDS
static final int RESULT\_TYPE\_USERIDS
States that user IDs are returned. Note that the array can be empty.
See Also:Constant Field Values

- RESULT\_TYPE\_GROUPIDS
static final int RESULT\_TYPE\_GROUPIDS
States that group IDs are returned. Note that the array can be empty.
Since:
6.0.2
See Also:Constant Field Values

- RESULT\_TYPE\_USERIDS\_AND\_GROUPIDS
static final int RESULT\_TYPE\_USERIDS\_AND\_GROUPIDS
States that user and group IDs are returned.
Since:
6.0.2
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getResultType
int getResultType()
Returns an indicator that describes the content of the staff result set.
 
 Possible values are: RESULT\_TYPE\_NOBODY, RESULT\_TYPE\_EVERYBODY, RESULT\_TYPE\_USERIDS,
                      RESULT\_TYPE\_GROUPIDS, RESULT\_TYPE\_USERIDS\_AND\_GROUPIDS
    - getGroupIDs
java.lang.String[] getGroupIDs()
Returns group IDs when the result type indicates that group IDs are returned.
 Otherwise, the array is empty.
Since:
6.0.2
    - getUserIDs
java.lang.String[] getUserIDs()
Returns user IDs when the result type indicates that user IDs are returned.
 Otherwise, the array is empty.
 
 Note that the array is also empty when no staff expression has been defined, for example,
 there is no staff expression for a process template that defines a set of process administrators.