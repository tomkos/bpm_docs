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

## Interface TreeConditionTermDefinition

- All Superinterfaces:
java.io.Serializable

public interface TreeConditionTermDefinition
extends java.io.Serializable
This interface represents the definition of a condition term.  A condition term is the "left-hand
 side" of a condition.  For example, if the condition is "intVar + 1 > 50", the condition term 
 definition would define the "intVar + 1" part.

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

java.util.List<TreeConditionValueTemplate>
getConditionValueTemplates()
Get the list of condition value templates associated with this condition term.

java.lang.String
getUserPresentation()
Get the user presentation string for this condition term definition.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getConditionValueTemplates
java.util.List<TreeConditionValueTemplate> getConditionValueTemplates()
Get the list of condition value templates associated with this condition term.  A 
 condition value is the "right-hand side" of a condition.  For example, if the condition 
 is "intVar + 1 > intVar2 + 10", the condition value is the "intVar2 + 10" part.  The
 templates in this list can be used to define condition values.
Returns:The list of condition value templates associated with this condition term.  
 The list may be empty if there are no condition value templates.  The returned list
 is unmodifiable.
    - getUserPresentation
java.lang.String getUserPresentation()
Get the user presentation string for this condition term definition.
Returns:The user presentation string for this condition term definition.  May be null
 if the condition term is defined by a template.