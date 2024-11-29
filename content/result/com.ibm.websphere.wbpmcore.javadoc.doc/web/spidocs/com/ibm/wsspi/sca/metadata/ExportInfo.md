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

## Interface ExportInfo

- All Superinterfaces:
ItemInfo

public interface ExportInfo
extends ItemInfo
Interface that represent the information from a SCA export. This interface
 provide access to the generic information available in the SCA export.
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
    - Method Summary Methods Modifier and Type Method and Description ExportBinding getExportBinding () Method returns the export binding information if the export has a data binding; otherwise null . java.lang.String getTargetName () Method returns the target name if the export is wired to a target.

### Method Summary

| Modifier and Type   | Method and Description                                                                                               |
|---------------------|----------------------------------------------------------------------------------------------------------------------|
| ExportBinding       | getExportBinding() Method returns the export binding information if the export has a data   binding; otherwise null. |
| java.lang.String    | getTargetName() Method returns the target name if the export is wired to a target.                                   |

- Methods inherited from interface com.ibm.wsspi.sca.metadata.ItemInfo
getDescription, getDisplayName, getInterface, getInterfaces, getName