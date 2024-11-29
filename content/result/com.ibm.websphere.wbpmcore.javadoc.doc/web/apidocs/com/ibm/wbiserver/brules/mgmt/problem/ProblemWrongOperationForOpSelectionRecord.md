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

## Class ProblemWrongOperationForOpSelectionRecord

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemWrongOperationForOpSelectionRecord

- All Implemented Interfaces:
java.io.Serializable

public class ProblemWrongOperationForOpSelectionRecord
extends Problem
implements java.io.Serializable
This class represents a validation error where an attempt was made to add an operation 
 selection record to an operation selection record list but the operation associated with 
 the selection record is not the same as the operation containing the operation selection 
 record list.
See Also:Serialized Form

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Constructor Summary

Constructors 

Constructor and Description

ProblemWrongOperationForOpSelectionRecord(OperationSelectionRecord operationSelectionRecord,
                                         OperationSelectionRecordList operationSelectionRecordList)
Constructor for the ProblemWrongOperationForOpSelectionRecord object.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getErrorMessage () OperationSelectionRecord getOperationSelectionRecord () Get the operation selection record that was being added. OperationSelectionRecordList getOperationSelectionRecordList () Get the operation selection record list to which the operation selection record was being added.

### Method Summary

| Modifier and Type            | Method and Description                                                                                                              |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String             | getErrorMessage()                                                                                                                   |
| OperationSelectionRecord     | getOperationSelectionRecord() Get the operation selection record that was being added.                                              |
| OperationSelectionRecordList | getOperationSelectionRecordList() Get the operation selection record list to which the operation selection record  was being added. |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait