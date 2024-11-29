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

## Interface FailedEventExceptionReport

- public interface FailedEventExceptionReport
The  FailedEventExceptionReport  interface defines the structured information
 of exception when performing a batch operation to delete and resubmit failed events.

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
getExceptionDetail()
Get exception detail.

java.util.Date
getExceptionTime()
Get the time when exception happens.

java.lang.String
getMsgId()
Get failed event message id.

boolean
isWarning()

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getMsgId
java.lang.String getMsgId()
Get failed event message id.
Returns:message id
    - getExceptionTime
java.util.Date getExceptionTime()
Get the time when exception happens.
Returns:exception time
    - getExceptionDetail
java.lang.String getExceptionDetail()
Get exception detail.
Returns:exception detail
    - isWarning
boolean isWarning()
Returns:boolean