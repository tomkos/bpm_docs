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

## Interface ActivityData

- Deprecated.

@Deprecated
public interface ActivityData
The interface to set/get activity data for a session activity

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
Deprecated. 
Copyright
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getActivityId()
Deprecated. 
Get Activity Id.

java.io.Serializable
getData(java.lang.Object key)
Deprecated. 
Get value by KEY from ActivityData.

java.util.Enumeration
getKeys()
Deprecated. 
Get keys for data other than session id, activity id, source comp name, target comp name

java.lang.String
getParentActivityId()
Deprecated. 
Get Parent Activity Id, may be null.

java.lang.String
getSessionId()
Deprecated. 
Get Session Id.

java.lang.String
getSourceComponentName()
Deprecated. 
Get the name of the source component.

java.lang.String
getTargetComponentName()
Deprecated. 
Get the name of the target component.

void
removeData(java.lang.Object key)
Deprecated. 
Remove the KEY value from ActivityData

void
setData(java.lang.Object key,
       java.io.Serializable value)
Deprecated. 
Set a property (KEY-VALUE pair) to ActivityData.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
Deprecated. 
Copyright
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getSessionId
java.lang.String getSessionId()
Deprecated. 
Get Session Id.
Returns:String
    - getActivityId
java.lang.String getActivityId()
Deprecated. 
Get Activity Id.
Returns:String
    - getParentActivityId
java.lang.String getParentActivityId()
Deprecated. 
Get Parent Activity Id, may be null.
Returns:String
    - getSourceComponentName
java.lang.String getSourceComponentName()
Deprecated. 
Get the name of the source component.
Returns:String
    - getTargetComponentName
java.lang.String getTargetComponentName()
Deprecated. 
Get the name of the target component.
Returns:String
    - setData
void setData(java.lang.Object key,
           java.io.Serializable value)
Deprecated. 
Set a property (KEY-VALUE pair) to ActivityData.
Parameters:key - value -
    - getData
java.io.Serializable getData(java.lang.Object key)
Deprecated. 
Get value by KEY from ActivityData.
Parameters:key - 
Returns:Serializable
    - getKeys
java.util.Enumeration getKeys()
Deprecated. 
Get keys for data other than session id, activity id, source comp name, target comp name
Returns:Enumeration
    - removeData
void removeData(java.lang.Object key)
Deprecated. 
Remove the KEY value from ActivityData
Parameters:key -