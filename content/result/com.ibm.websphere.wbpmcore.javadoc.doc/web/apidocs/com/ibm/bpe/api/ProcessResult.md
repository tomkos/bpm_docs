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

## Interface ProcessResult

- All Superinterfaces:
java.io.Serializable

public interface ProcessResult
extends java.io.Serializable
Returns the result of an API call that processes multiple process instances,
 for example, the result of a
 BusinessFlowManagerService.setInlineCustomProperty(PIID[],InlineCustomProperty) call.
Since:
7.5.1

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

PIID
getPIID()
Returns the object identifier of the process instance that has been processed.

ProcessException
getProcessException()
Returns the ProcessException object that describes any error that occurred during processing.

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
Returns the object identifier of the process instance that has been processed.
    - getProcessException
ProcessException getProcessException()
Returns the ProcessException object that describes any error that occurred during processing.
 Returns null if processing completed successfully.