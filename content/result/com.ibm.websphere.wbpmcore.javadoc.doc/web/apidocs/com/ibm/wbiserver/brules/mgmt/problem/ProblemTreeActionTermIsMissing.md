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

## Class ProblemTreeActionTermIsMissing

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemTreeActionTermIsMissing

- All Implemented Interfaces:
java.io.Serializable

public class ProblemTreeActionTermIsMissing
extends Problem
Problem class representing the error that the tree block is missing a tree
 action term.
See Also:Serialized Form

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

### Field Summary

    - Fields inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
COPYRIGHT

- Constructor Summary

Constructors 

Constructor and Description

ProblemTreeActionTermIsMissing(TreeBlock treeBlock)

- Method Summary Methods Modifier and Type Method and Description java.lang.String getErrorMessage () TreeBlock getTreeBlock ()

### Method Summary

| Modifier and Type   | Method and Description   |
|---------------------|--------------------------|
| java.lang.String    | getErrorMessage()        |
| TreeBlock           | getTreeBlock()           |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait