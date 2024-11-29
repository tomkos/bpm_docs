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
The Reference interface represents an SCDL service reference.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static java.lang.String
MULTIPLICITY\_0\_N
Used to indicate a multiplicity of 0..n

static java.lang.String
MULTIPLICITY\_1\_1
Used to indicate a multiplicity of 1..1
    - Method Summary

Methods 

Modifier and Type
Method and Description

InterfaceType
getInterfaceType(java.lang.String uri,
                java.lang.String name)
Returns an InterfaceType object representing the named interface.

java.util.List
getInterfaceTypes()
Returns a list of InterfaceType objects representing the interfaces declared on the reference.

java.lang.String
getMultiplicity()
Returns the value of the multiplicity attribute.

java.lang.String
getName()
Returns the reference name.

OperationType
getOperationType(java.lang.String name)
Returns an OperationType object representing the named operation.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- MULTIPLICITY\_1\_1
static final java.lang.String MULTIPLICITY\_1\_1
Used to indicate a multiplicity of 1..1
See Also:Constant Field Values

- MULTIPLICITY\_0\_N
static final java.lang.String MULTIPLICITY\_0\_N
Used to indicate a multiplicity of 0..n
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getName
java.lang.String getName()
Returns the reference name.
Returns:The reference name.
    - getInterfaceTypes
java.util.List getInterfaceTypes()
Returns a list of InterfaceType objects representing the interfaces declared on the reference.
Returns:The SCA metadata object describing an interface.
    - getInterfaceType
InterfaceType getInterfaceType(java.lang.String uri,
                             java.lang.String name)
Returns an InterfaceType object representing the named interface.
Returns:The SCA metadata object describing the interface.
    - getOperationType
OperationType getOperationType(java.lang.String name)
Returns an OperationType object representing the named operation.
Parameters:name - The operation name.
Returns:The OperationType object.
    - getMultiplicity
java.lang.String getMultiplicity()
Returns the value of the multiplicity attribute.
Returns:The multiplicity attribute.