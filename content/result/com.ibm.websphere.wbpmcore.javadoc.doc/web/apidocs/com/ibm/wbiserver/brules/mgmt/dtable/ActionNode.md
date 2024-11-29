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

## Interface ActionNode

- All Superinterfaces:
BusinessRuleChangeDetector, BusinessRuleValidateable, java.io.Serializable, TreeNode

public interface ActionNode
extends java.io.Serializable, TreeNode
This interface represents an action node within a decision tree. Actions are
 the result of executing the decision tree. They assign values to the output
 variables. Action nodes are always the leaf nodes of the tree since the
 represent the end state after having traversed the condition nodes of the
 tree to get to the final action to be performed. An action node can have one
 or more individual actions that are performed. Each action assigns a value to
 some output variable, referred to as the term.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.util.List<TreeAction > getTreeActions () Get the list of tree actions associated with this action node.

### Method Summary

| Modifier and Type          | Method and Description                                                          |
|----------------------------|---------------------------------------------------------------------------------|
| java.util.List<TreeAction> | getTreeActions() Get the list of tree actions associated with this action node. |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.dtable.TreeNode
getContainingTreeBlock, getParentNode, getRootNode, isOtherwiseCase

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges