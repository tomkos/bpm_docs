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

## Class ProblemTargetBusRuleNotSet

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemTargetBusRuleNotSet

- All Implemented Interfaces:
java.io.Serializable

public class ProblemTargetBusRuleNotSet
extends Problem
implements java.io.Serializable
Problem class representing the error that the target business rule is not set for the
 specified operation selection record.
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

ProblemTargetBusRuleNotSet(OperationSelectionRecord operationSelectionRecord)
Constructor for the ProblemTargetBusRuleNotSet class.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getErrorMessage () OperationSelectionRecord getOperationSelectionRecord () Get the operation selection record involved in the error.

### Method Summary

| Modifier and Type        | Method and Description                                                                  |
|--------------------------|-----------------------------------------------------------------------------------------|
| java.lang.String         | getErrorMessage()                                                                       |
| OperationSelectionRecord | getOperationSelectionRecord() Get the operation selection record involved in the error. |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait