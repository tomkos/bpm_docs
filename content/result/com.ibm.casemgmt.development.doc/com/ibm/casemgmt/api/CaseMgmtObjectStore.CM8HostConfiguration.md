- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class CaseMgmtObjectStore.CM8HostConfiguration

- java.lang.Object
    - com.ibm.casemgmt.api.CaseMgmtObjectStore.CM8HostConfiguration

- Enclosing class:
CaseMgmtObjectStore

public static final class CaseMgmtObjectStore.CM8HostConfiguration
extends java.lang.Object
Represents information about the CM8 host configured for this
 object store. This data is applicable only if the integration type
 (getIntegrationType()) for this object store is CM8.

ID status:
ID review by David Newhall

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description java.lang.String getHostName () Returns the name of the CM8 host. int getHostPort () Returns the port number of the CM8 host. java.lang.String getLibraryConnectionName () Returns the library connection name of the CM8 host. java.lang.String getLibraryName () Returns the library name of the CM8 host. java.lang.String getSchemaName () Returns the schema name of the CM8 host.

### Method Summary

| Modifier and Type   | Method and Description                                                          |
|---------------------|---------------------------------------------------------------------------------|
| java.lang.String    | getHostName() Returns the name of the CM8 host.                                 |
| int                 | getHostPort() Returns the port number of the CM8 host.                          |
| java.lang.String    | getLibraryConnectionName() Returns the library connection name of the CM8 host. |
| java.lang.String    | getLibraryName() Returns the library name of the CM8 host.                      |
| java.lang.String    | getSchemaName() Returns the schema name of the CM8 host.                        |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait