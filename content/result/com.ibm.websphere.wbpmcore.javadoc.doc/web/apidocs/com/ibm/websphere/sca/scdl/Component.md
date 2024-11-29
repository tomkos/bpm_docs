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

## Interface Component

- public interface Component
The Component interface represents an SCDL service component.

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

InterfaceType
getInterfaceType(java.lang.String uri,
                java.lang.String name)
Returns an InterfaceType object representing the named interface.

java.util.List
getInterfaceTypes()
Returns a list of InterfaceType objects representing the interfaces exposed by the service component.

java.lang.String
getName()
Returns the component name.

Reference
getReference(java.lang.String referenceName)
Returns the SCDL Reference object representing the named reference.

java.util.List
getReferences()
Returns the list of SCDL references declared by the component.

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
Returns the component name.
Returns:The component name.
    - getInterfaceTypes
java.util.List getInterfaceTypes()
Returns a list of InterfaceType objects representing the interfaces exposed by the service component.
Returns:The list of InterfaceType objects.
    - getInterfaceType
InterfaceType getInterfaceType(java.lang.String uri,
                             java.lang.String name)
Returns an InterfaceType object representing the named interface.
Returns:The InterfaceType object representing the named interface.
    - getReferences
java.util.List getReferences()
Returns the list of SCDL references declared by the component.
Returns:The list of SCDL references declared by the component.
    - getReference
Reference getReference(java.lang.String referenceName)
Returns the SCDL Reference object representing the named reference.
Parameters:referenceName - The name of the reference.
Returns:The SCDL Reference object representing the reference.