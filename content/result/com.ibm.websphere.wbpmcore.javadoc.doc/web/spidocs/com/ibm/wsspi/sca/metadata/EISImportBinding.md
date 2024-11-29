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

## Interface EISImportBinding

- All Superinterfaces:
ImportBinding

public interface EISImportBinding
extends ImportBinding
Interface that represent the EIS binding information on a SCA import.
Since:
7.5.1.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description Connection getConnection () Method returns the Connection of the EIS import binding. java.lang.String getDataBindingType () Method returns the data binding type of the EIS import binding. java.util.List<ImportMethodBinding > getMethodBinding () Method returns the list ImportMethodBinding objects of the EIS import binding. ResourceAdapter getResourceAdapter () Method returns the ResourceAdapter of the EIS import binding.

### Method Summary

| Modifier and Type                   | Method and Description                                                                              |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Connection                          | getConnection() Method returns the Connection of the EIS import binding.                            |
| java.lang.String                    | getDataBindingType() Method returns the data binding type of the EIS import binding.                |
| java.util.List<ImportMethodBinding> | getMethodBinding() Method returns the list ImportMethodBinding objects of the   EIS import binding. |
| ResourceAdapter                     | getResourceAdapter() Method returns the ResourceAdapter of the EIS import binding.                  |

- Methods inherited from interface com.ibm.wsspi.sca.metadata.ImportBinding
getBindingType