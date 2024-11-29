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

## Class ProblemCaseEdgeChildNodeMissing

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemCaseEdgeChildNodeMissing

- All Implemented Interfaces:
java.io.Serializable

public class ProblemCaseEdgeChildNodeMissing
extends Problem
Problem class representing the error that the case edge has no child node.
See Also:Serialized Form

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

### Field Summary

    - Fields inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
COPYRIGHT

- Constructor Summary

Constructors 

Constructor and Description

ProblemCaseEdgeChildNodeMissing(CaseEdge caseEdge)

- Method Summary Methods Modifier and Type Method and Description CaseEdge getCaseEdge () java.lang.String getErrorMessage ()

### Method Summary

| Modifier and Type   | Method and Description   |
|---------------------|--------------------------|
| CaseEdge            | getCaseEdge()            |
| java.lang.String    | getErrorMessage()        |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait