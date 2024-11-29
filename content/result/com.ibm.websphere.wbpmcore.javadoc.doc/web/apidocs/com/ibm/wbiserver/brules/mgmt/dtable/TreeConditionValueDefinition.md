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

## Interface TreeConditionValueDefinition

- All Superinterfaces:
java.io.Serializable

public interface TreeConditionValueDefinition
extends java.io.Serializable
This interface represents the definition of a condition value.  A condition value is the "right-hand
 side" of a condition.  For example, if the condition is "intVar + 1 > intVar2 + 10", the condition 
 value definition would define the "intVar2 + 10" part.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

TemplateInstanceExpression
getConditionValueTemplateInstance()
Get the template instance with parameter values for this condition value.

java.lang.String
getUserPresentation()
Get the user presentation string for this condition value definition.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getConditionValueTemplateInstance
TemplateInstanceExpression getConditionValueTemplateInstance()
Get the template instance with parameter values for this condition value.  Each value
 definition will contain either a template instance or a user presentation.  It will 
 not have both.  If it contains a template instance, then the user presentation can be
 obtained from the template associated with the template instance.
Returns:The template instance for this condition value.  null if there is no 
 template instance.
    - getUserPresentation
java.lang.String getUserPresentation()
Get the user presentation string for this condition value definition.  Each value
 definition will contain either a template instance or a user presentation.  It will 
 not have both.  If it contains a template instance, then the user presentation can be
 obtained from the template associated with the template instance.
Returns:The user presentation string for this condition value definition.  null if
 there is no user presentation.