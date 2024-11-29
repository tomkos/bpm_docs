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

## Interface ItemInfo

- All Known Subinterfaces:
BFMComponentInfo, ComponentInfo, ExportInfo, HTMComponentInfo, ImportInfo

public interface ItemInfo
Super interface for components, imports and exports that provide common 
 information of components, imports and exports.
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

java.lang.String
getDescription()
Method returns the description of the item.

java.lang.String
getDisplayName()
Method returns the display name of the item.

Interface
getInterface()
Method returns the interface of the item.

java.util.Collection<Interface>
getInterfaces()
Method returns the interfaces of the item.

java.lang.String
getName()
Method returns the name of the item.

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
Method returns the name of the item.
Returns:String  
     Name of the item.
    - getDisplayName
java.lang.String getDisplayName()
Method returns the display name of the item.
Returns:String  
     Display name of the item.
    - getDescription
java.lang.String getDescription()
Method returns the description of the item.
Returns:String  
     Description of the item.
    - getInterface
Interface getInterface()
Method returns the interface of the item.
Returns:Interface
     Interface of the item.
    - getInterfaces
java.util.Collection<Interface> getInterfaces()
Method returns the interfaces of the item.
Returns:Collection
     Collection of interfaces of the item.