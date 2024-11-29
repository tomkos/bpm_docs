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

## Interface ImportMethodBinding

- public interface ImportMethodBinding
Interface that represent the method binding information on a resource adapter binding.
Since:
7.5.1.0

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

java.util.Map<java.lang.String,java.lang.String>
getInteractionProperties()
Method returns the properties of the method interaction.

java.lang.String
getMethod()
Method returns the method of the method binding.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getMethod
java.lang.String getMethod()
Method returns the method of the method binding.
Returns:String
     Method of the method binding.
    - getInteractionProperties
java.util.Map<java.lang.String,java.lang.String> getInteractionProperties()
Method returns the properties of the method interaction.
Returns:Map
     Properties of the method interaction.