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

## Interface TreeConditionDefinition

- All Superinterfaces:
java.io.Serializable

public interface TreeConditionDefinition
extends java.io.Serializable
This interface represents a shared definition of a tree condition term and the possible values
 for the condition.  These definitions are referenced by the actual tree nodes that specify
 the logic of the decision table.

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

TreeConditionTermDefinition
getConditionTermDefinition()
Get the condition term definition for this tree condition.

java.util.List<TreeConditionValueDefinition>
getConditionValueDefinitions()
Get the list of shared condition value definitions for this condition definition.

Orientation
getOrientation()
Get the orientation for this condition.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getConditionTermDefinition
TreeConditionTermDefinition getConditionTermDefinition()
Get the condition term definition for this tree condition.  The condition term 
 definition defines the "left-hand side" of a condition.  For example, if the condition
 is "intVar + 1 > 50", the condition term definition would define the "intVar + 1" part.
Returns:The condition term definition for this tree condition.
    - getConditionValueDefinitions
java.util.List<TreeConditionValueDefinition> getConditionValueDefinitions()
Get the list of shared condition value definitions for this condition definition.
 This list contains the list of possible values for this condition.  This includes
 template instance expressions, which allow certain parameters to be changed at runtime.
Returns:The list of shared condition value definitions for this condition.  The returned
 list is unmodifiable.
    - getOrientation
Orientation getOrientation()
Get the orientation for this condition.
Returns:The orientation for this condition.