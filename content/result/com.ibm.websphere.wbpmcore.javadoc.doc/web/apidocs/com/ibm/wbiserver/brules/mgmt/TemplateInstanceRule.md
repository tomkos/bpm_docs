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

## Interface TemplateInstanceRule

- All Superinterfaces:
BusinessRuleChangeDetector, BusinessRuleValidateable, Rule, java.io.Serializable

All Known Subinterfaces:
DecisionTableTemplateInstanceRule, RuleSetTemplateInstanceRule

public interface TemplateInstanceRule
extends Rule, BusinessRuleValidateable, BusinessRuleChangeDetector, java.io.Serializable
This interface represents a rule within either a ruleset or a decision table that is based on 
 a rule template.  
 
 An existing template instance rule can be modified by changing its associated 
 parameter values.  This can be done by using the getParameterValues method
 to get the list of parameter values and then changing the values on the appropriate
 ParameterValue object using its setValue method.
See Also:RuleTemplate

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description ParameterValue getParameterValue (java.lang.String parameterName) Get the value of the template parameter with the specified name. java.util.List<ParameterValue > getParameterValues () Get the values of all template parameters for this template instance rule. RuleTemplate getRuleTemplate () Get the template from which this rule was defined.

### Method Summary

| Modifier and Type              | Method and Description                                                                                             |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------|
| ParameterValue                 | getParameterValue(java.lang.String parameterName) Get the value of the template parameter with the specified name. |
| java.util.List<ParameterValue> | getParameterValues() Get the values of all template parameters for this template instance rule.                    |
| RuleTemplate                   | getRuleTemplate() Get the template from which this rule was defined.                                               |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.Rule
getDescription, getDisplayName, getExpandedUserPresentation, getName, getUserPresentation, isDisplayNameSynchronizedToName, setDescription, setDisplayName, setDisplayNameIsSynchronizedToName

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges