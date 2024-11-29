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

## Interface ParameterValue

- All Superinterfaces:
BusinessRuleChangeDetector, BusinessRuleValidateable, java.io.Serializable

public interface ParameterValue
extends java.io.Serializable, BusinessRuleValidateable, BusinessRuleChangeDetector
This interface represents the value for one template parameter.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description Parameter getParameter () Get the parameter for this value. java.lang.String getValue () Get the parameter value. void setValue (java.lang.String newValue) Set the parameter value.

### Method Summary

| Modifier and Type   | Method and Description                                       |
|---------------------|--------------------------------------------------------------|
| Parameter           | getParameter() Get the parameter for this value.             |
| java.lang.String    | getValue() Get the parameter value.                          |
| void                | setValue(java.lang.String newValue) Set the parameter value. |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges