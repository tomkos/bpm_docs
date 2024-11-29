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

## Interface InitiateAndClaimFirstResult

- All Superinterfaces:
java.io.Serializable

public interface InitiateAndClaimFirstResult
extends java.io.Serializable
Returns the result of an initiateAndClaimFirst() call.
 Returns the object ID of the process instance created and
 information about the claimed activity instance.
 
Since:
6.2

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
getActivityName()
Returns the name of the activity that has been claimed.

AIID
getAIID()
Returns the object identifier of the activity that has been claimed.

ATID
getATID()
Returns the object identifier of the activity template that is associated to the claimed activity.

ClientObjectWrapper
getInputMessage()
Returns the input message of the claimed activity.

PIID
getPIID()
Returns the object identifier of the process instance that has been created.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getPIID
PIID getPIID()
Returns the object identifier of the process instance that has been created.
    - getAIID
AIID getAIID()
Returns the object identifier of the activity that has been claimed.
 If no activity has been claimed, null is returned.
    - getATID
ATID getATID()
Returns the object identifier of the activity template that is associated to the claimed activity.
 This object identifier may be used for correlating information in the client.
 If no activity has been claimed, null is returned.
    - getActivityName
java.lang.String getActivityName()
Returns the name of the activity that has been claimed.
 Returns null if no activity has been claimed or if there is no name.
    - getInputMessage
ClientObjectWrapper getInputMessage()
Returns the input message of the claimed activity. Returns null if no activity
 has been claimed or if there is no input message.