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

## Class SearchableCasePropertyImplForUpgrade

- java.lang.Object
    - com.ibm.casemgmt.api.upgrade.SearchableCasePropertyImplForUpgrade

- All Implemented Interfaces:
com.ibm.bpm.caseapi.searchablecaseproperties.SearchableCasePropertiesAPI.SearchableCaseProperty

public class SearchableCasePropertyImplForUpgrade
extends java.lang.Object
implements com.ibm.bpm.caseapi.searchablecaseproperties.SearchableCasePropertiesAPI.SearchableCaseProperty

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

SearchableCasePropertyImplForUpgrade(java.lang.String name,
                                    java.lang.String type,
                                    java.lang.String propId,
                                    java.lang.String aliasName,
                                    boolean isCase,
                                    boolean isActivity)
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description java.lang.String getAlias () java.lang.String getId () java.lang.String getSimpleType () java.lang.String getSymbolicName () boolean isSearchableForActivities () boolean isSearchableForCases () void setAlias (java.lang.String alias) void setId (java.lang.String id) void setSearchableForActivities (boolean isSearchableForActivities) void setSearchableForCases (boolean isSearchableForCases) void setSimpleType (java.lang.String simpleType) void setSymbolicName (java.lang.String symbolicName)

### Method Summary

| Modifier and Type   | Method and Description                                        |
|---------------------|---------------------------------------------------------------|
| java.lang.String    | getAlias()                                                    |
| java.lang.String    | getId()                                                       |
| java.lang.String    | getSimpleType()                                               |
| java.lang.String    | getSymbolicName()                                             |
| boolean             | isSearchableForActivities()                                   |
| boolean             | isSearchableForCases()                                        |
| void                | setAlias(java.lang.String alias)                              |
| void                | setId(java.lang.String id)                                    |
| void                | setSearchableForActivities(boolean isSearchableForActivities) |
| void                | setSearchableForCases(boolean isSearchableForCases)           |
| void                | setSimpleType(java.lang.String simpleType)                    |
| void                | setSymbolicName(java.lang.String symbolicName)                |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait