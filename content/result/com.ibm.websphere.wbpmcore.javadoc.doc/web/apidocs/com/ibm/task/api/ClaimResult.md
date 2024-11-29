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

## Interface ClaimResult

- All Superinterfaces:
java.io.Serializable

public interface ClaimResult
extends java.io.Serializable
Returns the result of a special claim request. The claim request either asks to process
 multiple task instances at a time or uses a query table to determine the task to be claimed.
Since:
6.1

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT\_
    - Method Summary

Methods 

Modifier and Type
Method and Description

ClientObjectWrapper
getInputMessage()
Returns the input message of the claimed task.

TaskException
getTaskException()
Returns the TaskException object that describes any error that occurred during processing.

TKIID
getTKIID()
Returns the object identifier of the task instance that has been processed.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT\_
static final java.lang.String COPYRIGHT\_
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getTKIID
TKIID getTKIID()
Returns the object identifier of the task instance that has been processed.
    - getInputMessage
ClientObjectWrapper getInputMessage()
Returns the input message of the claimed task. Returns null if the task has not
 been claimed or if there is no input message.
    - getTaskException
TaskException getTaskException()
Returns the TaskException object that describes any error that occurred during processing.
 Returns null if processing completed successfully.
 
 If the claim request refers to a query table, a ClaimResult is only returned
 when a task instance is successfully claimed.
 This means that getTaskException() always returns null.