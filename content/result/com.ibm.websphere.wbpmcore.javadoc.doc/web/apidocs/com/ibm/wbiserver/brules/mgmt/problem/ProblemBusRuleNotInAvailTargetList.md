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

## Class ProblemBusRuleNotInAvailTargetList

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemBusRuleNotInAvailTargetList

- All Implemented Interfaces:
java.io.Serializable

public class ProblemBusRuleNotInAvailTargetList
extends Problem
implements java.io.Serializable
Problem class representing the error that the specified business rule is not in the
 available targets list.
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

ProblemBusRuleNotInAvailTargetList(BusinessRule businessRule,
                                  Operation operation)
Constructor for the ProblemBusRuleNotInAvailTargetList class.
    - Method Summary Methods Modifier and Type Method and Description BusinessRule getBusinessRule () Get the business rule involved in the error. java.lang.String getErrorMessage () Operation getOperation () Get the operation involved in the error.

### Method Summary

| Modifier and Type   | Method and Description                                         |
|---------------------|----------------------------------------------------------------|
| BusinessRule        | getBusinessRule() Get the business rule involved in the error. |
| java.lang.String    | getErrorMessage()                                              |
| Operation           | getOperation() Get the operation involved in the error.        |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait