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

## Interface OperationSelectionRecord

- All Superinterfaces:
BusinessRuleChangeDetector, BusinessRuleValidateable, java.io.Serializable

public interface OperationSelectionRecord
extends BusinessRuleValidateable, BusinessRuleChangeDetector, java.io.Serializable
This interface represents one selection record associated with an operation.  A selection record
 specifies a target business rule for the operation along with the start and end dates for
 that target.  The business rule should be invoked when the date falls within the specified 
 range.  The user can create new instances of this interface in order to add new selection records 
 (new date ranges) to an Operation.  This is done using one of the 
 newOperationSelectionRecord methods on the 
 OperationSelectionRecordList
 interface.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description Operation getAssociatedOperation () Get the operation with which this operation selection record is associated. BusinessRule getBusinessRuleTarget () Get the business rule target for this selection record. java.util.Date getEndDate () Get the end date for this operation selection record. java.util.Date getStartDate () Get the start date for this operation selection record. void setBusinessRuleTarget (BusinessRule newBusinessRuleTarget) Set the business rule target for this selection record. void setEndDate (java.util.Date newEndDate) Set the end date for this operation selection record. void setStartDate (java.util.Date newStartDate) Set the start date for this operation selection record.

### Method Summary

| Modifier and Type   | Method and Description                                                                                            |
|---------------------|-------------------------------------------------------------------------------------------------------------------|
| Operation           | getAssociatedOperation() Get the operation with which this operation selection record is associated.              |
| BusinessRule        | getBusinessRuleTarget() Get the business rule target for this selection record.                                   |
| java.util.Date      | getEndDate() Get the end date for this operation selection record.                                                |
| java.util.Date      | getStartDate() Get the start date for this operation selection record.                                            |
| void                | setBusinessRuleTarget(BusinessRule newBusinessRuleTarget) Set the business rule target for this selection record. |
| void                | setEndDate(java.util.Date newEndDate) Set the end date for this operation selection record.                       |
| void                | setStartDate(java.util.Date newStartDate) Set the start date for this operation selection record.                 |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges