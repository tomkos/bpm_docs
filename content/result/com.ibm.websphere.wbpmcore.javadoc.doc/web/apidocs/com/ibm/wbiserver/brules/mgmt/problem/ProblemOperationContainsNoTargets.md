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

## Class ProblemOperationContainsNoTargets

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemOperationContainsNoTargets

- All Implemented Interfaces:
java.io.Serializable

public class ProblemOperationContainsNoTargets
extends Problem
implements java.io.Serializable
This class represents a validation error where an operation has no default business rule 
 target and also has no business rule targets qualified by date ranges.  An operation must 
 have at least one target.
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

ProblemOperationContainsNoTargets(Operation operation)
Constructor for the ProblemOperationContainsNoTargets object.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getErrorMessage () Operation getOperation () Get the operation which has the error.

### Method Summary

| Modifier and Type   | Method and Description                                |
|---------------------|-------------------------------------------------------|
| java.lang.String    | getErrorMessage()                                     |
| Operation           | getOperation() Get the operation which has the error. |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait