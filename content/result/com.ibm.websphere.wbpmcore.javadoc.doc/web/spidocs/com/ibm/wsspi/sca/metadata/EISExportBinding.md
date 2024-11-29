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

## Interface EISExportBinding

- All Superinterfaces:
ExportBinding

public interface EISExportBinding
extends ExportBinding
Interface that represent the EIS binding information on a SCA export.
Since:
7.5.1.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description Connection getConnection () Method returns the Connection of the EIS export binding. java.lang.String getDataBindingType () Method returns the data binding type of the EIS export binding. java.util.List<ExportMethodBinding > getMethodBinding () Method returns the list of ExportMethodBinding objects of the EIS export binding. ResourceAdapter getResourceAdapter () Method returns the ResourceAdapter of the EIS export binding.

### Method Summary

| Modifier and Type                   | Method and Description                                                                                 |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Connection                          | getConnection() Method returns the Connection of the EIS export binding.                               |
| java.lang.String                    | getDataBindingType() Method returns the data binding type of the EIS export binding.                   |
| java.util.List<ExportMethodBinding> | getMethodBinding() Method returns the list of ExportMethodBinding objects of the   EIS export binding. |
| ResourceAdapter                     | getResourceAdapter() Method returns the ResourceAdapter of the EIS export binding.                     |

- Methods inherited from interface com.ibm.wsspi.sca.metadata.ExportBinding
getBindingType