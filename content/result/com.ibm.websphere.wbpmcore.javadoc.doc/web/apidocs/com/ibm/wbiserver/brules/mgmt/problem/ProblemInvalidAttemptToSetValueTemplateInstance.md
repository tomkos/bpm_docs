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

## Class ProblemInvalidAttemptToSetValueTemplateInstance

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemInvalidAttemptToSetValueTemplateInstance

- All Implemented Interfaces:
java.io.Serializable

public class ProblemInvalidAttemptToSetValueTemplateInstance
extends Problem
implements java.io.Serializable
Problem class representing the error that an attempt was made to set the value template
 instance of a part of a decision table when that part currently does not contains a value
 template instance.  It is not allowed to set a value template instance into a part of a
 decision table that currently does not have a value template instance.
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

ProblemInvalidAttemptToSetValueTemplateInstance(TemplateInstanceExpression templateInstanceExpressionBeingAdded,
                                               java.lang.Object objectBeingAddedTo)
Constructor for the ProblemInvalidAttemptToSetValueTemplateInstance class.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getErrorMessage () java.lang.Object getObjectBeingAddedTo () Get the part of the decision table to which the template instance expression was being added. TemplateInstanceExpression getTemplateInstanceExpressionBeingAdded () Get the template instance expression that was being added to a part of a decision table.

### Method Summary

| Modifier and Type          | Method and Description                                                                                                             |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String           | getErrorMessage()                                                                                                                  |
| java.lang.Object           | getObjectBeingAddedTo() Get the part of the decision table to which the template instance expression was being  added.             |
| TemplateInstanceExpression | getTemplateInstanceExpressionBeingAdded() Get the template instance expression that was being added to a part of a decision table. |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait