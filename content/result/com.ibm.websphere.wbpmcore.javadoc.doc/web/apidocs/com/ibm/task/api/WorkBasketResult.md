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

## Interface WorkBasketResult

- All Superinterfaces:
java.io.Serializable

public interface WorkBasketResult
extends java.io.Serializable
Returns the result of an API call that processes multiple work baskets,
 for example, the result of a
 removeAsDistributionTarget call.
Since:
6.2.0.3

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

WBID
getWBID()
Returns the object identifier of the work basket that has been processed.

java.lang.String
getWorkBasketName()
Returns the name of the work basket that has been processed.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getWBID
WBID getWBID()
Returns the object identifier of the work basket that has been processed.
 May be null when the work basket name is specified.
    - getWorkBasketName
java.lang.String getWorkBasketName()
Returns the name of the work basket that has been processed.
 May be null when the object identifier of the work basket is specified.
    - getTaskException
TaskException getTaskException()
Returns the TaskException object that describes any error that occurred during processing.
 Returns null if processing completed successfully.