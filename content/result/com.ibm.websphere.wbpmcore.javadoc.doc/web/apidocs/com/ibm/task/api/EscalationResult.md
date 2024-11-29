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

## Interface EscalationResult

- All Superinterfaces:
java.io.Serializable

public interface EscalationResult
extends java.io.Serializable
Returns the result of an API call that processes multiple escalation instances,
 for example, the result of a bulkTransferWorkItem(ESIID[], ...), call.
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

ESIID
getESIID()
Returns the object identifier of the escalation instance that has been processed.

TaskException
getTaskException()
Returns the TaskException object that describes any error that occurred during processing.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getESIID
ESIID getESIID()
Returns the object identifier of the escalation instance that has been processed.
    - getTaskException
TaskException getTaskException()
Returns the TaskException object that describes any error that occurred during processing.
 Returns null if processing completed successfully.