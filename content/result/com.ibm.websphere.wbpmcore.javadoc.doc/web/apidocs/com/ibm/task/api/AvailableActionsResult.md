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

## Interface AvailableActionsResult

- All Superinterfaces:
java.io.Serializable

public interface AvailableActionsResult
extends java.io.Serializable
Returns the result of a request for available actions.
Since:
7.5

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

int[]
getAvailableActions(TKIID tkiid)
Returns the actions the logged-on user may perform on the specified task instance.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT\_
static final java.lang.String COPYRIGHT\_
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getAvailableActions
int[] getAvailableActions(TKIID tkiid)
Returns the actions the logged-on user may perform on the specified task instance.
Parameters:tkiid - The object ID of the task instance whose actions are to be determined.
Returns:int[] -
    The set of possible actions for the specified task instance.
    Returns null if there are no available actions.