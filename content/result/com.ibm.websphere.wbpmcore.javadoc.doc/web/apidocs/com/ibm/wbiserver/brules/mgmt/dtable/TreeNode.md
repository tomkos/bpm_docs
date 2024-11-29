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

## Interface TreeNode

- All Superinterfaces:
BusinessRuleChangeDetector, BusinessRuleValidateable, java.io.Serializable

All Known Subinterfaces:
ActionNode, ConditionNode

public interface TreeNode
extends BusinessRuleValidateable, BusinessRuleChangeDetector, java.io.Serializable
This interface represents one node within a decision tree. This is the
 abstract base class for a tree node. An actual tree node will be either of
 type ConditionNode or ActionNode. A
 ConditionNode represents a condition in the tree while an
 ActionNode represents an action.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description TreeBlock getContainingTreeBlock () Get the tree block that contains this tree node. TreeNode getParentNode () Get the parent node of this node. TreeNode getRootNode () Get the root node of the tree containing this node. boolean isOtherwiseCase () Determine whether or not this tree node is part of the otherwise case.

### Method Summary

| Modifier and Type   | Method and Description                                                                   |
|---------------------|------------------------------------------------------------------------------------------|
| TreeBlock           | getContainingTreeBlock() Get the tree block that contains this tree node.                |
| TreeNode            | getParentNode() Get the parent node of this node.                                        |
| TreeNode            | getRootNode() Get the root node of the tree containing this node.                        |
| boolean             | isOtherwiseCase() Determine whether or not this tree node is part of the otherwise case. |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges