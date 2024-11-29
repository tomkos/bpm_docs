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

## Interface FailedEventParameter

- public interface FailedEventParameter
The  FailedEventParameter  interface defines the parameter structure
 of a failed event.

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

java.lang.String
getName()
Get parameter name.

int
getPosition()
Get parameter position.

java.lang.String
getType()
Get parameter type.

java.lang.Object
getValue()
Get parameter value.

void
setValue(java.lang.Object value)
Set parameter value.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getValue
java.lang.Object getValue()
Get parameter value.
Returns:parameter value
    - getType
java.lang.String getType()
Get parameter type.
Returns:parameter type
    - getPosition
int getPosition()
Get parameter position.
Returns:parameter position
    - getName
java.lang.String getName()
Get parameter name.
Returns:parameter name
    - setValue
void setValue(java.lang.Object value)
Set parameter value. This is used for modified resubmission.
Parameters:value - new value of failed event parameter