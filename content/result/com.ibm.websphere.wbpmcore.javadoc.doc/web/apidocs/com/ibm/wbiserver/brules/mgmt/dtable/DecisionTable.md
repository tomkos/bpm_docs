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

## Interface DecisionTable

- All Superinterfaces:
BusinessRule, BusinessRuleChangeDetector, BusinessRuleValidateable, java.io.Serializable

public interface DecisionTable
extends BusinessRule
This interface represents a decision table.  A decision table is represented as a tree with nodes
 that represent conditions and actions.  These nodes are contained within the decision table's
 tree block.  A decision table can also have an initialization rule.  This is a rule that is
 run before the decision table itself is evaluated.  The initialization rule can be either
 a hard-coded rule or a rule created from a template.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description DecisionTableRule getInitRule () Get the initialization rule for this decision table, if one exists. DecisionTableRuleTemplate getInitTemplate () Get the rule template for the initialization rule, if one exists. TreeBlock getTreeBlock () Get the tree block for this decision table.

### Method Summary

| Modifier and Type         | Method and Description                                                              |
|---------------------------|-------------------------------------------------------------------------------------|
| DecisionTableRule         | getInitRule() Get the initialization rule for this decision table, if one exists.   |
| DecisionTableRuleTemplate | getInitTemplate() Get the rule template for the initialization rule, if one exists. |
| TreeBlock                 | getTreeBlock() Get the tree block for this decision table.                          |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRule
createCopy, getAssociatedOperation, getDescription, getDisplayName, getName, getProperties, getProperty, getPropertyValue, getRuntimeID, getSaveDate, getTargetNameSpace, getType, isDisplayNameSynchronizedToName, setDescription, setDisplayName, setDisplayNameIsSynchronizedToName, setPropertyValue

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges