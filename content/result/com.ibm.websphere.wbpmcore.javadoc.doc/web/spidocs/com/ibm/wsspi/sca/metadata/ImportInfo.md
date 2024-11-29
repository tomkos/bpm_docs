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

## Interface ImportInfo

- All Superinterfaces:
ItemInfo

public interface ImportInfo
extends ItemInfo
Interface that represent the information from a SCA import. This interface
 provide access to the generic information available in the SCA import.
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
    - Method Summary Methods Modifier and Type Method and Description ImportBinding getImportBinding () Method returns the import binding information if the import has a data binding; otherwise null .

### Method Summary

| Modifier and Type   | Method and Description                                                                                               |
|---------------------|----------------------------------------------------------------------------------------------------------------------|
| ImportBinding       | getImportBinding() Method returns the import binding information if the import has a data   binding; otherwise null. |

- Methods inherited from interface com.ibm.wsspi.sca.metadata.ItemInfo
getDescription, getDisplayName, getInterface, getInterfaces, getName