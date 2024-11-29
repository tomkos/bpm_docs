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

## Class InbasketSynchronizer

- java.lang.Object
    - com.ibm.casemgmt.api.upgrade.InbasketSynchronizer

- public class InbasketSynchronizer
extends java.lang.Object

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

InbasketSynchronizer(com.ibm.xmlns.prod.ecm.acm.sdf.SolutionType soltype,
                    filenet.vw.api.VWSystemConfiguration vwSystemConfiguration)
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description java.lang.String generateBPMAliasUsingP8Id (java.util.Map<java.lang.String,java.lang.String> propGuids, java.lang.Object obj, java.util.Map<java.lang.String,java.lang.String> map) java.lang.String generateBPMAliasUsingSymbolicName (java.lang.Object obj) java.util.Map<java.lang.String,java.lang.String> getInbasketColumnAliases () java.util.Map<java.lang.String,com.ibm.bpm.caseapi.searchablecaseproperties.SearchableCasePropertiesAPI.SearchableCaseProperty> getInbasketsForSychronization () java.util.Map<java.lang.String,java.lang.String> getPropertyGuids () boolean hasAnyLocalBPMActivity () void syncBPMAlias4Inbaskets (java.lang.String BranchId)

### Method Summary

| Modifier and Type                                                                                                               | Method and Description                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String                                                                                                                | generateBPMAliasUsingP8Id(java.util.Map<java.lang.String,java.lang.String> propGuids,                          java.lang.Object obj,                          java.util.Map<java.lang.String,java.lang.String> map) |
| java.lang.String                                                                                                                | generateBPMAliasUsingSymbolicName(java.lang.Object obj)                                                                                                                                                             |
| java.util.Map<java.lang.String,java.lang.String>                                                                                | getInbasketColumnAliases()                                                                                                                                                                                          |
| java.util.Map<java.lang.String,com.ibm.bpm.caseapi.searchablecaseproperties.SearchableCasePropertiesAPI.SearchableCaseProperty> | getInbasketsForSychronization()                                                                                                                                                                                     |
| java.util.Map<java.lang.String,java.lang.String>                                                                                | getPropertyGuids()                                                                                                                                                                                                  |
| boolean                                                                                                                         | hasAnyLocalBPMActivity()                                                                                                                                                                                            |
| void                                                                                                                            | syncBPMAlias4Inbaskets(java.lang.String BranchId)                                                                                                                                                                   |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait