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

## Interface ConditionNode

- All Superinterfaces:
BusinessRuleChangeDetector, BusinessRuleValidateable, java.io.Serializable, TreeNode

public interface ConditionNode
extends java.io.Serializable, TreeNode
This interface represents on condition in a decision tree.  A condition node has a reference 
 to a condition term definition that defines the term ("left-hand side") for this condition.
 It also contains a list of case edges which represent the cases to be checked for for
 the specified term.  Each case edge defines a particular condition, such as "== 100" or
 ">=1000 and < 10000", that is checked for this term.  Each case edge refers to a
 child node which is the either the next condition node in the tree or is an action node
 that defines the action to take.  The case edge whose condition evaluates to true is 
 followed to get to the next node in the tree.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description void addConditionValueToThisLevel (TemplateInstanceExpression newConditionValue) Add a new condition value to all the condition nodes at the same level as this one in the decision tree. java.util.List<TreeConditionValueTemplate > getAvailableValueTemplates () Get the value templates available for use by this condition node. java.util.List<CaseEdge > getCaseEdges () Get the list of case edges for this condition node. TreeNode getOtherwiseCase () This is a 'condition' that is satisfied if no other condition is satisfied. TreeConditionTermDefinition getTermDefinition () Get the term definition for this condition. boolean removeConditionValue (TemplateInstanceExpression conditionValueToRemove) Remove the specified condition value from this condition node.

### Method Summary

| Modifier and Type                          | Method and Description                                                                                                                                                               |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                                       | addConditionValueToThisLevel(TemplateInstanceExpression newConditionValue) Add a new condition value to all the condition nodes at the same level as this one in  the decision tree. |
| java.util.List<TreeConditionValueTemplate> | getAvailableValueTemplates() Get the value templates available for use by this condition node.                                                                                       |
| java.util.List<CaseEdge>                   | getCaseEdges() Get the list of case edges for this condition node.                                                                                                                   |
| TreeNode                                   | getOtherwiseCase() This is a 'condition' that is satisfied if no other condition is  satisfied.                                                                                      |
| TreeConditionTermDefinition                | getTermDefinition() Get the term definition for this condition.                                                                                                                      |
| boolean                                    | removeConditionValue(TemplateInstanceExpression conditionValueToRemove) Remove the specified condition value from this condition node.                                               |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.dtable.TreeNode
getContainingTreeBlock, getParentNode, getRootNode, isOtherwiseCase

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges