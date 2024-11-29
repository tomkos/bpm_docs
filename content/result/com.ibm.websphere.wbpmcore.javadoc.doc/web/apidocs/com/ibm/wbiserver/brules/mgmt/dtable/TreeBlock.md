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

## Interface TreeBlock

- All Superinterfaces:
BusinessRuleChangeDetector, BusinessRuleValidateable, java.io.Serializable

public interface TreeBlock
extends BusinessRuleValidateable, BusinessRuleChangeDetector, java.io.Serializable
This interface represents a tree block within a decision table.  The tree block defines the main
 decision table.  The decision table is represented internally as a decision tree.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description TreeNode getRootNode () Get the root tree node for this tree block. java.util.List<TreeActionTermDefinition > getTreeActionTermDefinitions () Get the shared action term definitions for this tree block. java.util.List<TreeConditionDefinition > getTreeConditionDefinitions () Get the shared condition definitions for this tree block.

### Method Summary

| Modifier and Type                        | Method and Description                                                                     |
|------------------------------------------|--------------------------------------------------------------------------------------------|
| TreeNode                                 | getRootNode() Get the root tree node for this tree block.                                  |
| java.util.List<TreeActionTermDefinition> | getTreeActionTermDefinitions() Get the shared action term definitions for this tree block. |
| java.util.List<TreeConditionDefinition>  | getTreeConditionDefinitions() Get the shared condition definitions for this tree block.    |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges