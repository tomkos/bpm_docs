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

## Interface RuleSetTemplateInstanceRule

- All Superinterfaces:
BusinessRuleChangeDetector, BusinessRuleValidateable, Rule, RuleSetRule, java.io.Serializable, TemplateInstanceRule

public interface RuleSetTemplateInstanceRule
extends TemplateInstanceRule, RuleSetRule, java.io.Serializable
This interface represents a template instance rule contained within a rule block in a 
 ruleset.  There is another interface, 
 DecisionTableTemplateInstanceRule,
 that represents a template instance rule contained within a decision table.
   
 An existing RuleSetTemplateInstanceRule can be changed by getting
 its parameter values and changing them directly.  See
 TemplateInstanceRule for 
 details.
 
 A new RuleSetTemplateInstanceRule can be created by getting the desired
 RuleSetRuleTemplate and calling the 
 createRuleFromTemplate 
 method on it.  The new RuleSetTemplateInstanceRule can then be added to a
 rule block using one of the addRule methods on the RuleBlock class.
See Also:RuleSetRuleTemplate, 
RuleBlock

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description RuleSetRuleTemplate getRuleSetRuleTemplate () Get the RuleSetRuleTemplate for this template instance rule.

### Method Summary

| Modifier and Type   | Method and Description                                                                |
|---------------------|---------------------------------------------------------------------------------------|
| RuleSetRuleTemplate | getRuleSetRuleTemplate() Get the RuleSetRuleTemplate for this template instance rule. |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.TemplateInstanceRule
getParameterValue, getParameterValues, getRuleTemplate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.ruleset.RuleSetRule
getParentRuleBlock

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.Rule
getDescription, getDisplayName, getExpandedUserPresentation, getName, getUserPresentation, isDisplayNameSynchronizedToName, setDescription, setDisplayName, setDisplayNameIsSynchronizedToName