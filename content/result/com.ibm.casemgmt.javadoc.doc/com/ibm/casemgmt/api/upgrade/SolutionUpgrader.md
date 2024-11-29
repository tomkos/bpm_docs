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

## Class SolutionUpgrader

- java.lang.Object
    - com.ibm.casemgmt.api.upgrade.SolutionUpgrader

- public class SolutionUpgrader
extends java.lang.Object

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

SolutionUpgrader(boolean upgradeCalledFromCB) 

SolutionUpgrader(java.lang.String CeURI,
                java.lang.String designOSName)
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description com.filenet.api.property.PropertyFilter getDocPropertyFilter () boolean isUpgradeRequired () void upgradeSdf (com.filenet.api.core.UpdatingBatch ub, com.filenet.api.property.PropertyFilter pf, com.ibm.acm.icmbuilder.api.persistence.common.CEDocumentHandler cedoc) java.lang.String upgradeSolution () java.lang.String upgradeSolutionFromCB (java.lang.String solutionName) java.lang.String validateParams (org.apache.commons.json.JSONObject paramJson)

### Method Summary

| Modifier and Type                       | Method and Description                                                                                                                                                                   |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| com.filenet.api.property.PropertyFilter | getDocPropertyFilter()                                                                                                                                                                   |
| boolean                                 | isUpgradeRequired()                                                                                                                                                                      |
| void                                    | upgradeSdf(com.filenet.api.core.UpdatingBatch ub,           com.filenet.api.property.PropertyFilter pf,           com.ibm.acm.icmbuilder.api.persistence.common.CEDocumentHandler cedoc) |
| java.lang.String                        | upgradeSolution()                                                                                                                                                                        |
| java.lang.String                        | upgradeSolutionFromCB(java.lang.String solutionName)                                                                                                                                     |
| java.lang.String                        | validateParams(org.apache.commons.json.JSONObject paramJson)                                                                                                                             |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait