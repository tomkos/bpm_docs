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

## Class ProblemOverlappingRanges

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemOverlappingRanges

- All Implemented Interfaces:
java.io.Serializable

public class ProblemOverlappingRanges
extends Problem
implements java.io.Serializable
This class represents a validation error where two operation selection records have 
 overlapping date ranges.
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

ProblemOverlappingRanges(Operation operation,
                        OperationSelectionRecord selectionRecord1,
                        OperationSelectionRecord selectionRecord2)
Constructor for the ProblemOverlappingRanges class.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getErrorMessage () Operation getOperation () Get the operation that contains the overlapping date ranges. OperationSelectionRecord getSelectionRecord1 () Get one of the operation selection records that has overlapping date ranges. OperationSelectionRecord getSelectionRecord2 () Get one of the operation selection records that has overlapping date ranges.

### Method Summary

| Modifier and Type        | Method and Description                                                                             |
|--------------------------|----------------------------------------------------------------------------------------------------|
| java.lang.String         | getErrorMessage()                                                                                  |
| Operation                | getOperation() Get the operation that contains the overlapping date ranges.                        |
| OperationSelectionRecord | getSelectionRecord1() Get one of the operation selection records that has overlapping date ranges. |
| OperationSelectionRecord | getSelectionRecord2() Get one of the operation selection records that has overlapping date ranges. |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait