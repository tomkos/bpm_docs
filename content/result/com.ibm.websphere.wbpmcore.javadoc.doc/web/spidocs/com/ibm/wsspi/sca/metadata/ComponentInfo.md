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

## Interface ComponentInfo

- All Superinterfaces:
ItemInfo

All Known Subinterfaces:
BFMComponentInfo, HTMComponentInfo

public interface ComponentInfo
extends ItemInfo
Interface that represent the information from a SCA component. This interface
 provide access to the generic information available in the SCA component and
 will be extended by specific implementation that extend the generic 
 information with implementation specific information.
Since:
7.5.1.0
See Also:ItemInfo

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getImplementationType () Method returns the type of implementation of the component. java.util.List<Reference > getReferences () Method returns the list of references of the component.

### Method Summary

| Modifier and Type         | Method and Description                                                              |
|---------------------------|-------------------------------------------------------------------------------------|
| java.lang.String          | getImplementationType() Method returns the type of implementation of the component. |
| java.util.List<Reference> | getReferences() Method returns the list of references of the component.             |

- Methods inherited from interface com.ibm.wsspi.sca.metadata.ItemInfo
getDescription, getDisplayName, getInterface, getInterfaces, getName