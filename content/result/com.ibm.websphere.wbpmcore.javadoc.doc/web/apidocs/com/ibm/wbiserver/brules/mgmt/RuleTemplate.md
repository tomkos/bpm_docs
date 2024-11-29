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

## Interface RuleTemplate

- All Superinterfaces:
java.io.Serializable, Template

All Known Subinterfaces:
DecisionTableRuleTemplate, RuleSetRuleTemplate

public interface RuleTemplate
extends java.io.Serializable, Template
This interface represents a rule template.  If the template is contained within a ruleset,
 then new instances of the template can be created and added to the rule block associated 
 with the containing ruleset.  This is the only way to add a new rule to a ruleset.  Templates
 contained within a ruleset are represented by the
 RuleSetRuleTemplate
 interface.  Refer to that interface for more information about creating a new instance of
 a template.  Templates contained within a decision table are represented by the
 DecisionTableRuleTemplate
 interface.  New instances of a DecisionTableRuleTemplate cannot be created since
 it is not allowed to add new template instance rules to a decision table.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

### Method Summary

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.Template
getDescription, getDisplayName, getId, getName, getParameter, getParameters, getUserPresentation