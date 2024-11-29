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

## Interface Reference

- public interface Reference
Interface that represent the reference information from a SCA component.
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

Interface
getInterface()
Method returns the Interface of the specified reference.

java.lang.String
getName()
Method returns the name of the specified reference.

java.lang.String
getWireTarget()
Method returns the name of the target the reference is wired to.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getName
java.lang.String getName()
Method returns the name of the specified reference.
Returns:String
     Name of the specified reference.
    - getWireTarget
java.lang.String getWireTarget()
Method returns the name of the target the reference is wired to. If the 
 reference is not wired null will be returned.
Returns:String
     Name of the target the reference is wired to.
    - getInterface
Interface getInterface()
Method returns the Interface of the specified reference.
Returns:Interface
     Interface of the specified reference.