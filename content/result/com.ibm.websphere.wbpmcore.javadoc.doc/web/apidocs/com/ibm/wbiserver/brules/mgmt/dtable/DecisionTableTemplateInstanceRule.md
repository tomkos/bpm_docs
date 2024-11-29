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

## Interface DecisionTableTemplateInstanceRule

- All Superinterfaces:
BusinessRuleChangeDetector, BusinessRuleValidateable, DecisionTableRule, Rule, java.io.Serializable, TemplateInstanceRule

public interface DecisionTableTemplateInstanceRule
extends TemplateInstanceRule, DecisionTableRule, java.io.Serializable
This interface represents a template instance rule contained within a tree block in a 
 decision table.  There is another interface, 
 RuleSetTemplateInstanceRule,
 that represents a template instance rule contained within a ruleset.
   
 An existing DecisionTableTemplateInstanceRule can be changed by getting
 its parameter values and changing them directly.  See
 TemplateInstanceRule for 
 details.

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

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.TemplateInstanceRule
getParameterValue, getParameterValues, getRuleTemplate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.Rule
getDescription, getDisplayName, getExpandedUserPresentation, getName, getUserPresentation, isDisplayNameSynchronizedToName, setDescription, setDisplayName, setDisplayNameIsSynchronizedToName