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

## Class ProblemInvalidConditionValueTemplate

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemInvalidConditionValueTemplate

- All Implemented Interfaces: java.io.Serializable public class ProblemInvalidConditionValueTemplate extends Problem implements java.io.Serializable Problem class representing one of the following errors: See Also: Serialized Form

```
public class ProblemInvalidConditionValueTemplate
extends Problem
implements java.io.Serializable
```

    1. The condition value template for a new condition value is not associated with the 
 condition term definition for the condition node to which the condition value is being 
 added.
 The condition value template for the template instance expression being set on a
 case edge is not an available template for that case edge.

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

ProblemInvalidConditionValueTemplate(TemplateInstanceExpression templateInstanceExpression,
                                    CaseEdge caseEdgeBeingChanged,
                                    ConditionNode conditionNode)
Constructor for the ProblemInvalidConditionValueTemplate class.
    - Method Summary Methods Modifier and Type Method and Description CaseEdge getCaseEdgeBeingChanged () Get the case edge that was being changed when this error occurred. ConditionNode getConditionNode () Get the condition node to which the new condition value was being added. java.lang.String getErrorMessage () TemplateInstanceExpression getTemplateInstanceExpression () The template instance expression that was being set into the existing case edge or that was being used to add a new condition value to a condition node.

### Method Summary

| Modifier and Type          | Method and Description                                                                                                                                                                     |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CaseEdge                   | getCaseEdgeBeingChanged() Get the case edge that was being changed when this error occurred.                                                                                               |
| ConditionNode              | getConditionNode() Get the condition node to which the new condition value was being  added.                                                                                               |
| java.lang.String           | getErrorMessage()                                                                                                                                                                          |
| TemplateInstanceExpression | getTemplateInstanceExpression() The template instance expression that was being set into the existing case edge or   that was being used to add a new condition value to a condition node. |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait