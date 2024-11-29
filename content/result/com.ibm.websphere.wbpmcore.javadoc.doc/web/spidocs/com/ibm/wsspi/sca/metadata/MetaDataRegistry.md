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

## Class MetaDataRegistry

- java.lang.Object
    - com.ibm.wsspi.sca.metadata.MetaDataRegistry

- public final class MetaDataRegistry
extends java.lang.Object
Meta Data registry that provide a interface to retrieve the SCA meta data 
 for a specific application getModuleMetaData(String). To do so
 it is necessary to get an instance of the registry by calling 
 newInstance().
Since:
7.5.1.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description ModuleMetaData getModuleMetaData (java.lang.String appName) Method returns the module meta data for the specified application name. static MetaDataRegistry newInstance () Static factory method to create a new instance of the meta data registry.

### Method Summary

| Modifier and Type       | Method and Description                                                                                              |
|-------------------------|---------------------------------------------------------------------------------------------------------------------|
| ModuleMetaData          | getModuleMetaData(java.lang.String appName) Method returns the module meta data for the specified application name. |
| static MetaDataRegistry | newInstance() Static factory method to create a new instance of the meta data registry.                             |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait