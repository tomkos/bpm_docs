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

## Interface ModuleMetaData

- public interface ModuleMetaData
Interface for the SCA meta data that can be retrieved by the SCA meta data 
 registry MetaDataRegistry.
Since:
7.5.1.0
See Also:MetaDataRegistry

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

BOMode
getBOMode()
Method that returns the BO Mode (BO Eager, BO Lazy) of the SCA module.

java.util.Collection<ComponentInfo>
getComponents()
Method returns a list of ComponentInfo objects with information 
 about each component within this SCA module.

java.util.Collection<ExportInfo>
getExports()
Method returns a list of ExportInfo objects with information 
 about each export within this SCA module.

java.util.Collection<ImportInfo>
getImports()
Method returns a list of ImportInfo objects with information 
 about each import within this SCA module.

java.lang.String
getModuleName()
Method that returns the SCA module name.

java.lang.String
getModuleShortName()
Method that returns the SCA module short name.

java.lang.String
getRootContainerAcronym()
Method returns the root container acronym if the application belongs to a 
 process application; otherwise null.

java.lang.String
getRootContainerName()
Method returns the root container name if the application belongs to a 
 process application; otherwise null.

java.lang.String
getRootContainerSnapshotGUID()
Method returns the root container snapshot GUID if the application belongs 
 to a process application; otherwise null.

java.lang.String
getRootContainerSnapshotName()
Method returns the root container snapshot name if the application belongs 
 to a process application; otherwise null.

java.lang.String
getRootContainerTrackName()
Method returns the root container track name if the application belongs 
 to a process application; otherwise null.

java.lang.String
getToolkitAcronym()
Method returns the toolkit acronym if the application belongs to a 
 process application and the process application contains a toolkit; 
 otherwise null.

java.lang.String
getToolkitName()
Method returns the name of the toolkit if the application belongs to a 
 process application and the process application contains a toolkit; 
 otherwise null.

java.lang.String
getToolkitSnapshotID()
Method returns the toolkit snapshot ID if the application belongs to a 
 process application and the process application contains a toolkit; 
 otherwise null.

java.lang.String
getToolkitSnapshotName()
Method returns the toolkit snapshot name if the application belongs to a 
 process application and the process application contains a toolkit; 
 otherwise null.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getModuleName
java.lang.String getModuleName()
Method that returns the SCA module name.
Returns:String
     SCA module name.
    - getModuleShortName
java.lang.String getModuleShortName()
Method that returns the SCA module short name.
Returns:String
     SCA module short name.
    - getBOMode
BOMode getBOMode()
Method that returns the BO Mode (BO Eager, BO Lazy) of the SCA module.
Returns:BOMode
     BO Mode (BO Eager, BO Lazy) of the SCA module.
    - getRootContainerSnapshotGUID
java.lang.String getRootContainerSnapshotGUID()
Method returns the root container snapshot GUID if the application belongs 
 to a process application; otherwise null.
Returns:String
     Root container snapshot GUID if the application belongs to a process 
     application; otherwise null.
    - getRootContainerName
java.lang.String getRootContainerName()
Method returns the root container name if the application belongs to a 
 process application; otherwise null.
Returns:String
     Root container name if the application belongs to a process 
     application; otherwise null.
    - getRootContainerAcronym
java.lang.String getRootContainerAcronym()
Method returns the root container acronym if the application belongs to a 
 process application; otherwise null.
Returns:String
     Root container acronym if the application belongs to a process 
     application; otherwise null.
    - getRootContainerSnapshotName
java.lang.String getRootContainerSnapshotName()
Method returns the root container snapshot name if the application belongs 
 to a process application; otherwise null.
Returns:String
     Root container snapshot name if the application belongs to a process 
     application; otherwise null.
    - getRootContainerTrackName
java.lang.String getRootContainerTrackName()
Method returns the root container track name if the application belongs 
 to a process application; otherwise null.
Returns:String
     Root container track name if the application belongs to a process 
     application; otherwise null.
    - getToolkitName
java.lang.String getToolkitName()
Method returns the name of the toolkit if the application belongs to a 
 process application and the process application contains a toolkit; 
 otherwise null.
Returns:String
     Name of the toolkit if the application belongs to a process 
     application and the process application contains a toolkit; 
     otherwise null.
    - getToolkitAcronym
java.lang.String getToolkitAcronym()
Method returns the toolkit acronym if the application belongs to a 
 process application and the process application contains a toolkit; 
 otherwise null.
Returns:String
     Toolkit acronym if the application belongs to a process 
     application and the process application contains a toolkit; 
     otherwise null.
    - getToolkitSnapshotName
java.lang.String getToolkitSnapshotName()
Method returns the toolkit snapshot name if the application belongs to a 
 process application and the process application contains a toolkit; 
 otherwise null.
Returns:String
     Toolkit snapshot name if the application belongs to a process 
     application and the process application contains a toolkit; 
     otherwise null.
    - getToolkitSnapshotID
java.lang.String getToolkitSnapshotID()
Method returns the toolkit snapshot ID if the application belongs to a 
 process application and the process application contains a toolkit; 
 otherwise null.
Returns:String
     Toolkit snapshot ID if the application belongs to a process 
     application and the process application contains a toolkit; 
     otherwise null.
    - getComponents
java.util.Collection<ComponentInfo> getComponents()
Method returns a list of ComponentInfo objects with information 
 about each component within this SCA module.
Returns:Collection
     List of ComponentInfo objects with information about each 
     component within this SCA module.
    - getImports
java.util.Collection<ImportInfo> getImports()
Method returns a list of ImportInfo objects with information 
 about each import within this SCA module.
Returns:Collection
     List of ImportInfo objects with information about each 
     import within this SCA module.
    - getExports
java.util.Collection<ExportInfo> getExports()
Method returns a list of ExportInfo objects with information 
 about each export within this SCA module.
Returns:Collection
     List of ExportInfo objects with information about each 
     export within this SCA module.