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

## Interface RuleSetRuleTemplate

- All Superinterfaces:
RuleTemplate, java.io.Serializable, Template

public interface RuleSetRuleTemplate
extends RuleTemplate, java.io.Serializable
This interface represents a rule template contained within a ruleset.  There is another
 interface, 
 DecisionTableRuleTemplate,
 that represents a rule template contained within a decision table.
 
 The RuleSetRuleTemplate interface allows you to create new instances of the
 template.  To do this, you first need to create ParameterValue objects to 
 represent the values for all the parameters on this template.  Use the 
 getParameters
 method on this template to get the defined parameters, then use the 
 createParameterValue 
 method on the individual Parameter objects to create ParameterValue
 objects with the desired values.  Once the list of ParameterValue objects
 is created, create a template instance using the 
 createRuleFromTemplate method on this 
 interface.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description RuleSetTemplateInstanceRule createRuleFromTemplate (java.lang.String ruleName, java.util.List<ParameterValue > parameterValues) Create a new rule based on this rule template with the specified name and the specified values for the template parameters. RuleSet getParentRuleSet () Get the ruleset that contains this rule template.

### Method Summary

| Modifier and Type           | Method and Description                                                                                                                                                                                                                               |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RuleSetTemplateInstanceRule | createRuleFromTemplate(java.lang.String ruleName,                       java.util.List<ParameterValue> parameterValues) Create a new rule based on this rule template with the specified name and  the specified values for the template parameters. |
| RuleSet                     | getParentRuleSet() Get the ruleset that contains this rule template.                                                                                                                                                                                 |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.Template
getDescription, getDisplayName, getId, getName, getParameter, getParameters, getUserPresentation