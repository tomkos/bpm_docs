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

## Interface TreeAction

- All Superinterfaces: BusinessRuleChangeDetector , BusinessRuleValidateable , java.io.Serializable public interface TreeAction extends BusinessRuleValidateable , BusinessRuleChangeDetector , java.io.Serializable This interface represents one action within a decision tree action node. Each of these actions assigns a value to a variable (referred to as the "term"). Each TreeAction contains the following: The value for each tree action is either a hard-coded expression or is defined by a template instance. The hard-coded expression cannot be obtained using the API. If the value is a hard-coded expression, then the value user presentation string should be used to determine how to present the value to the user. If the value is defined by a template instance, then the associated template, along with the parameter values from the template instance, should be used to determine how to present the value to the user.

```
public interface TreeAction
extends BusinessRuleValidateable, BusinessRuleChangeDetector, java.io.Serializable
```

    1. The definition of the term for this action.  This defines the variable that a value will
 be assigned to by this action.
 The user presentation string for the value for this action.  This defines how the value
 should be presented to the end user.  This may be null if there is no user presentation or
 if the value is defined by a template, i.e. there is a value template instance.  In this case
 the user presentation is defined by the template used to define the value.
 A template instance that defines the value for this action.  This may be null if the value
 is not defined by a template.
 An indication of whether or not the value is "not applicable".  A "not applicable" value
 means that the action is an invocation of another SCA component.

The value for each tree action is either a hard-coded expression or is defined by a 
 template instance.  The hard-coded expression cannot be obtained using the API.  If the value
 is a hard-coded expression, then the value user presentation string should be used to 
 determine how to present the value to the user.  If the value is defined by a template
 instance, then the associated template, along with the parameter values from the template
 instance, should be used to determine how to present the value to the user.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.util.List<TreeActionValueTemplate > getAvailableValueTemplates () Get the value templates available for use by this action. TreeActionTermDefinition getTermDefinition () Get the definition of the term of this tree action. TemplateInstanceExpression getValueTemplateInstance () Get the template instance defining the value for this action. java.lang.String getValueUserPresentation () Get the user presentation string for the value for this tree action. boolean isValueNotApplicable () Determine whether or not the value is "not applicable". void setValueTemplateInstance (TemplateInstanceExpression valueTemplateInstance) Set the template instance defining the value for this action.

### Method Summary

| Modifier and Type                       | Method and Description                                                                                                                   |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| java.util.List<TreeActionValueTemplate> | getAvailableValueTemplates() Get the value templates available for use by this action.                                                   |
| TreeActionTermDefinition                | getTermDefinition() Get the definition of the term of this tree action.                                                                  |
| TemplateInstanceExpression              | getValueTemplateInstance() Get the template instance defining the value for this action.                                                 |
| java.lang.String                        | getValueUserPresentation() Get the user presentation string for the value for this tree action.                                          |
| boolean                                 | isValueNotApplicable() Determine whether or not the value is "not applicable".                                                           |
| void                                    | setValueTemplateInstance(TemplateInstanceExpression valueTemplateInstance) Set the template instance defining the value for this action. |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges