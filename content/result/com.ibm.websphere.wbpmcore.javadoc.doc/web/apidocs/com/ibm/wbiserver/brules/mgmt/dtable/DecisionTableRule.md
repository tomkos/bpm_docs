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

## Interface DecisionTableRule

- All Superinterfaces:
BusinessRuleChangeDetector, BusinessRuleValidateable, Rule, java.io.Serializable

All Known Subinterfaces:
DecisionTableTemplateInstanceRule

public interface DecisionTableRule
extends Rule, java.io.Serializable
This interface represents a rule contained within a decision table.  There is another 
 interface,
 RuleSetRule, that
 represents a rule contained within a ruleset.  Two different interfaces are used
 because a rule within a ruleset has a different kind of parent from a rule within a
 decision table.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description TreeBlock getParentTreeBlock () Get the tree block that contains this rule.

### Method Summary

| Modifier and Type   | Method and Description                                           |
|---------------------|------------------------------------------------------------------|
| TreeBlock           | getParentTreeBlock() Get the tree block that contains this rule. |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.Rule
getDescription, getDisplayName, getExpandedUserPresentation, getName, getUserPresentation, isDisplayNameSynchronizedToName, setDescription, setDisplayName, setDisplayNameIsSynchronizedToName

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges