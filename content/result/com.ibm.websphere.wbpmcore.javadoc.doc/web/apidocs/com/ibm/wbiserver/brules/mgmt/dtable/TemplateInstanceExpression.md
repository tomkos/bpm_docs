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

## Interface TemplateInstanceExpression

- All Superinterfaces:
BusinessRuleChangeDetector, BusinessRuleValidateable, java.io.Serializable

public interface TemplateInstanceExpression
extends BusinessRuleValidateable, BusinessRuleChangeDetector, java.io.Serializable
This interface represents an instance of a template used in an expression.  It contains a list
 of values for each parameter defined in the corresponding template.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getExpandedUserPresentation () Get the user presentation for this template instance express with the placeholders for the template parameters filled in with the actual value of the parameter. java.util.List<ParameterValue > getParameterValues () Get the values of all template parameters for this template instance rule. Template getTemplate () Get the template from which this template instance was derived. java.lang.String getUserPresentation () Get the user presentation for this template instance expression.

### Method Summary

| Modifier and Type              | Method and Description                                                                                                                                                                           |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String               | getExpandedUserPresentation() Get the user presentation for this template instance express with the placeholders for   the template parameters filled in with the actual value of the parameter. |
| java.util.List<ParameterValue> | getParameterValues() Get the values of all template parameters for this template instance rule.                                                                                                  |
| Template                       | getTemplate() Get the template from which this template instance was derived.                                                                                                                    |
| java.lang.String               | getUserPresentation() Get the user presentation for this template instance expression.                                                                                                           |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges