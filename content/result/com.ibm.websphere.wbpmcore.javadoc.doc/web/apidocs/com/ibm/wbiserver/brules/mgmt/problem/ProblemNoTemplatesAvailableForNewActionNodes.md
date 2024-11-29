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

## Class ProblemNoTemplatesAvailableForNewActionNodes

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemNoTemplatesAvailableForNewActionNodes

- All Implemented Interfaces:
java.io.Serializable

public class ProblemNoTemplatesAvailableForNewActionNodes
extends Problem
implements java.io.Serializable
This exception is thrown when calling
 ConditionNode.addConditionValueToThisLevel() if there are no
 available templates that can be used to fill in the newly-created empty
 ActionNodes.
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

ProblemNoTemplatesAvailableForNewActionNodes(ConditionNode conditionNode)
    - Method Summary Methods Modifier and Type Method and Description ConditionNode getConditionNode () java.lang.String getErrorMessage ()

### Method Summary

| Modifier and Type   | Method and Description   |
|---------------------|--------------------------|
| ConditionNode       | getConditionNode()       |
| java.lang.String    | getErrorMessage()        |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait