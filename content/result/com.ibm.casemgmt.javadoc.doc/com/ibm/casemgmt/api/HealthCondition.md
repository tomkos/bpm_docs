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

## Class HealthCondition

- java.lang.Object
    - com.ibm.casemgmt.api.HealthCondition

- public class HealthCondition
extends java.lang.Object
Represents a HealthCondition instance that is associated with a case. Instances of HealthCondition
 are obtained by calling the fetchCaseHealthConditions method on a Case instance, 
 which returns a list of HealthCondition instances in the case.
 
 HealthCondition objects are stored in the Content Engine repository as objects of CmAcmHealthCondition class.

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description void clear () Clears the memory, if any, that was allocated for the list of HealthAlert objects. Case getCaseFolder () Returns the case that this Health Condition object belongs to. java.util.List<HealthAlert > getHealthDetails () Returns a list of HealthAlert objects. java.lang.Integer getHealthIndicator () Returns the health indicator, which is stored in the CmAcmHealthIndicator property of the Health Condition object. com.filenet.api.util.Id getId () Returns the ID, which is stored in the Id property of the Health Condition object. java.lang.Boolean getIsDataFinalized () Returns the CmAcmIsDataFinalized property value of the Health Condition object. java.lang.String getProviderName () Returns the provider name, which is stored in the CmAcmHealthProviderSymbolicName property of the Health Condition object. void setCaseFolder (Case caseFolder) Sets the case that this Health Condition object belongs to. void setHealthDetails (java.lang.String healthDetails) Sets the health details for this Health Condition object. void setHealthIndicator (java.lang.Integer healthIndicator) Sets the health indicator for this Health Condition object. void setIsDataFinalized (java.lang.Boolean isDataFinalized) Sets the isDateFinalized property for this Health Condition object. void setProviderName (java.lang.String providerName) Sets a provider name for this Health Condition object.

### Method Summary

| Modifier and Type           | Method and Description                                                                                                                       |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| void                        | clear() Clears the memory, if any, that was allocated for the list of HealthAlert objects.                                                   |
| Case                        | getCaseFolder() Returns the case that this Health Condition object belongs to.                                                               |
| java.util.List<HealthAlert> | getHealthDetails() Returns a list of HealthAlert objects.                                                                                    |
| java.lang.Integer           | getHealthIndicator() Returns the health indicator, which is stored in the CmAcmHealthIndicator property of the Health Condition object.      |
| com.filenet.api.util.Id     | getId() Returns the ID, which is stored in the Id property of the Health Condition object.                                                   |
| java.lang.Boolean           | getIsDataFinalized() Returns the CmAcmIsDataFinalized property value of the Health Condition object.                                         |
| java.lang.String            | getProviderName() Returns the provider name, which is stored in the CmAcmHealthProviderSymbolicName property of the Health Condition object. |
| void                        | setCaseFolder(Case caseFolder) Sets the case that this Health Condition object belongs to.                                                   |
| void                        | setHealthDetails(java.lang.String healthDetails) Sets the health details for this Health Condition object.                                   |
| void                        | setHealthIndicator(java.lang.Integer healthIndicator) Sets the health indicator for this Health Condition object.                            |
| void                        | setIsDataFinalized(java.lang.Boolean isDataFinalized) Sets the isDateFinalized property for this Health Condition object.                    |
| void                        | setProviderName(java.lang.String providerName) Sets a provider name for this Health Condition object.                                        |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait