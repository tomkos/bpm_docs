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

## Interface SCAImportBinding

- All Superinterfaces:
ImportBinding

public interface SCAImportBinding
extends ImportBinding
Interface that represent the SCA binding information on a SCA import.
Since:
7.5.1.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getExportName () Method returns the export name that belongs to the SCA binding of the import. java.lang.String getModuleName () Method returns the module name that belongs to the SCA binding of the import. java.lang.String getModuleShortName () Method returns the module short name that belongs to the SCA binding of the import. java.lang.String getRootContainerNameAcronym () Method returns the root container name acronym that belongs to the SCA binding of the import. java.lang.String getRootContainerSnapshotAcronym () Method returns the root container snapshot acronym that belongs to the SCA binding of the import. java.lang.String getVersion () Method returns the version value that belongs to the SCA binding of the import. java.lang.String getVersionProvider () Method returns the version provider that belongs to the SCA binding of the import.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String    | getExportName() Method returns the export name that belongs to the SCA binding of   the import.                                       |
| java.lang.String    | getModuleName() Method returns the module name that belongs to the SCA binding of   the import.                                       |
| java.lang.String    | getModuleShortName() Method returns the module short name that belongs to the SCA binding of   the import.                            |
| java.lang.String    | getRootContainerNameAcronym() Method returns the root container name acronym that belongs to the SCA   binding of the import.         |
| java.lang.String    | getRootContainerSnapshotAcronym() Method returns the root container snapshot acronym that belongs to the SCA   binding of the import. |
| java.lang.String    | getVersion() Method returns the version value that belongs to the SCA binding of   the import.                                        |
| java.lang.String    | getVersionProvider() Method returns the version provider that belongs to the SCA binding of   the import.                             |

- Methods inherited from interface com.ibm.wsspi.sca.metadata.ImportBinding
getBindingType