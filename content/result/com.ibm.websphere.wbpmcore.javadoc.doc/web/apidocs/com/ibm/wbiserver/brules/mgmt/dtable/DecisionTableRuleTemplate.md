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

## Interface DecisionTableRuleTemplate

- All Superinterfaces:
RuleTemplate, java.io.Serializable, Template

public interface DecisionTableRuleTemplate
extends RuleTemplate, java.io.Serializable
This interface represents a rule template contained within a decision table.  There is another
 interface, 
 RuleSetRuleTemplate,
 that represents a rule template contained within a ruleset.
 
 The DecisionTableRuleTemplate interface does not allow new instances of the 
 template to be created since it is not allowed to add new template instance rules to a 
 decision table.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description DecisionTable getParentDecisionTable () Get the decision table that contains this rule template.

### Method Summary

| Modifier and Type   | Method and Description                                                            |
|---------------------|-----------------------------------------------------------------------------------|
| DecisionTable       | getParentDecisionTable() Get the decision table that contains this rule template. |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.Template
getDescription, getDisplayName, getId, getName, getParameter, getParameters, getUserPresentation