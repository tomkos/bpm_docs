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

## Interface StaffQueryResult

- public interface StaffQueryResult
This interface provides methods to handle the result of a staff query.
 The staff query result is returned by a staff plugin.
Since:
6.0.2

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
States that a set of qualifying group IDs is returned.

static int
RESULT\_TYPE\_NOBODY
States that no one is qualifying.

static int
RESULT\_TYPE\_USERIDS
States that a set of qualifying user IDs is returned.

static int
RESULT\_TYPE\_USERIDS\_AND\_GROUPIDS
States that user and group IDs are returned.
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String[]
getGroupIDs()
This method returns the set of group IDs when the result type indicates
 that group IDs are returned.

int
getResultType()
This method returns an indicator that describes the content of the staff
 result set.

java.util.Collection
getUserData()
This method returns a collection of UserData objects.

java.util.Map
getUserDataMap()
This method returns a Map containing key-value pairs with user name as 
 key and a UserData object as values.

com.ibm.bpe.api.UTCDate
getValidUntilDate()
This method returns the time when the cached user collection expires and when
 it will be newly retrieved using the staff plugin.

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
States that a set of qualifying user IDs is returned. Note that the set can be empty.
See Also:Constant Field Values

- RESULT\_TYPE\_GROUPIDS
static final int RESULT\_TYPE\_GROUPIDS
States that a set of qualifying group IDs is returned.
See Also:Constant Field Values

- RESULT\_TYPE\_USERIDS\_AND\_GROUPIDS
static final int RESULT\_TYPE\_USERIDS\_AND\_GROUPIDS
States that user and group IDs are returned.
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getResultType int getResultType() This method returns an indicator that describes the content of the staff result set. Possible values are: Returns: The staff result set indicator.

#### getResultType

```
int getResultType()
```

Possible values are:
 
RESULT\_TYPE\_NOBODY
RESULT\_TYPE\_EVERYBODY
RESULT\_TYPE\_USERIDS
RESULT\_TYPE\_GROUPIDS
RESULT\_TYPE\_USERIDS\_AND\_GROUPIDS

- getGroupIDs
java.lang.String[] getGroupIDs()
This method returns the set of group IDs when the result type indicates
 that group IDs are returned. Otherwise, it returns null.
 
Note: Currrently, the maximum array size is 1.
Returns:The group IDs or null.

- getValidUntilDate
com.ibm.bpe.api.UTCDate getValidUntilDate()
This method returns the time when the cached user collection expires and when
 it will be newly retrieved using the staff plugin. The time is assumed
 to be in UTC.
Returns:The expiration time.

- getUserData
java.util.Collection getUserData()
This method returns a collection of UserData objects.
 
 A UserData objects contains attributes like userid, e-mail address and 
 preferred locale.
 
Note: If the result type is not RESULT\_TYPE\_USERIDS, 'null' 
 is returned.
 
Important: 
 If this method is used once, the getUserDataMap() method will return 'null'
 to prevent the modification of the map normally returned with 
 the getUserDataMap() method.
Returns:A collection of UserData objects.

- getUserDataMap
java.util.Map getUserDataMap()
This method returns a Map containing key-value pairs with user name as 
 key and a UserData object as values.
 
 A UserData objects contains attributes like userid, e-mail address and 
 preferred locale.
 
Note: If the result type is not RESULT\_TYPE\_USERIDS, 'null' 
 is returned.
 
Important: 
 If this method is used once, the getUserData() method will return 'null'
 to prevent the modification of the collection normally returned with 
 the getUserData() method.
Returns:Map of UserData objects or null