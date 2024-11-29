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

## Interface TreeConditionValueTemplate

- All Superinterfaces:
java.io.Serializable, Template

public interface TreeConditionValueTemplate
extends java.io.Serializable, Template
This interface represents a template for a tree condition value.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description TemplateInstanceExpression createTemplateInstanceExpression (java.util.List<ParameterValue > parameterValues) Create a template instance expression based on this condition value template and having the specified values for its parameters.

### Method Summary

| Modifier and Type          | Method and Description                                                                                                                                                                                             |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TemplateInstanceExpression | createTemplateInstanceExpression(java.util.List<ParameterValue> parameterValues) Create a template instance expression based on this condition value  template and having the specified values for its parameters. |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.Template
getDescription, getDisplayName, getId, getName, getParameter, getParameters, getUserPresentation