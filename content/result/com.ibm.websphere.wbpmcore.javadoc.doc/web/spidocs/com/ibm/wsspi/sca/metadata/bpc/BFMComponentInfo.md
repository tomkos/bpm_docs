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

## Interface BFMComponentInfo

- All Superinterfaces:
ComponentInfo, ItemInfo

public interface BFMComponentInfo
extends ComponentInfo
Interface that represent the information from a SCA process component.
Since:
7.5.1.0
See Also:ComponentInfo

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getModeledDisplayId (java.lang.String displayId) Helper method to return the modeled display id for any display id passed as parameter. Process getProcess () Method that returns the detailed information about a process component.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                   |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String    | getModeledDisplayId(java.lang.String displayId) Helper method to return the modeled display id for any display id passed   as parameter. |
| Process             | getProcess() Method that returns the detailed information about a process component.                                                     |

- Methods inherited from interface com.ibm.wsspi.sca.metadata.ComponentInfo
getImplementationType, getReferences

- Methods inherited from interface com.ibm.wsspi.sca.metadata.ItemInfo
getDescription, getDisplayName, getInterface, getInterfaces, getName