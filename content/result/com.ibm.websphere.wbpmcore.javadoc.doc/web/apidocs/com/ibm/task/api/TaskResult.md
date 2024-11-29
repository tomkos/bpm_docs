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

## Interface TaskResult

- All Superinterfaces:
java.io.Serializable

public interface TaskResult
extends java.io.Serializable
Returns the result of an API call that processes multiple task instances,
 for example, the result of a complete(TKIID[]) call.
Since:
6.1

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

TaskException
getTaskException()
Returns the TaskException object that describes any error that occurred during processing.

TKIID
getTKIID()
Returns the object identifier of the task instance that has been processed.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getTKIID
TKIID getTKIID()
Returns the object identifier of the task instance that has been processed.
    - getTaskException
TaskException getTaskException()
Returns the TaskException object that describes any error that occurred during processing.
 Returns null if processing completed successfully.