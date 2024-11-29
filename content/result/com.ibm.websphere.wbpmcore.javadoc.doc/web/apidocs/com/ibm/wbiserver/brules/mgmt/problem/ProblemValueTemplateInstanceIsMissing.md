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

## Class ProblemValueTemplateInstanceIsMissing

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemValueTemplateInstanceIsMissing

- All Implemented Interfaces:
java.io.Serializable

public class ProblemValueTemplateInstanceIsMissing
extends Problem
implements java.io.Serializable
This problem occurs when a tree action should have a value template instance,
 but doesn't.
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

ProblemValueTemplateInstanceIsMissing(TreeAction treeAction)
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getErrorMessage () TreeAction getTreeAction () java.lang.String toString ()

### Method Summary

| Modifier and Type   | Method and Description   |
|---------------------|--------------------------|
| java.lang.String    | getErrorMessage()        |
| TreeAction          | getTreeAction()          |
| java.lang.String    | toString()               |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait