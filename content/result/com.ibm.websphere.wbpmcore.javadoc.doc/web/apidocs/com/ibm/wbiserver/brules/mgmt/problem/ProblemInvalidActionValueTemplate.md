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

## Class ProblemInvalidActionValueTemplate

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemInvalidActionValueTemplate

- All Implemented Interfaces:
java.io.Serializable

public class ProblemInvalidActionValueTemplate
extends Problem
implements java.io.Serializable
Problem class representing the error that the action value template being used to define
 the value for an action is not available to that action, i.e. it is not associated with
 the TreeActionTermDefinition for the action.
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

ProblemInvalidActionValueTemplate(TemplateInstanceExpression templateInstanceBeingUsed,
                                 TreeAction treeAction)
Constructor for the ProblemInvalidActionValueTemplate class.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getErrorMessage () TemplateInstanceExpression getTemplateInstanceBeingUsed () Get the template instance that is in error. TreeAction getTreeAction () The tree action for which the template instance is being used.

### Method Summary

| Modifier and Type          | Method and Description                                                         |
|----------------------------|--------------------------------------------------------------------------------|
| java.lang.String           | getErrorMessage()                                                              |
| TemplateInstanceExpression | getTemplateInstanceBeingUsed() Get the template instance that is in error.     |
| TreeAction                 | getTreeAction() The tree action for which the template instance is being used. |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait