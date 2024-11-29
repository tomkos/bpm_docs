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

## Interface BusinessCategoryResult

- All Superinterfaces:
java.io.Serializable

public interface BusinessCategoryResult
extends java.io.Serializable
Returns the result of an API call that processes multiple business categories,
 for example, the result of a
 setPriorityOfBusinessCategories call.
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

BCID
getBCID()
Returns the object identifier of the business category that has been processed.

java.lang.String
getBusinessCategoryName()
Returns the name of the business category that has been processed.

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

    - getBCID
BCID getBCID()
Returns the object identifier of the business category that has been processed.
 May be null when the business category name is specified.
    - getBusinessCategoryName
java.lang.String getBusinessCategoryName()
Returns the name of the business category that has been processed.
 May be null when the object identifier of the business category is specified.
    - getTaskException
TaskException getTaskException()
Returns the TaskException object that describes any error that occurred during processing.
 Returns null if processing completed successfully.