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

## Interface TTask

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TTask
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TTask'.
 

 
         Task type for all kinds of tasks (oTask, pTask, hTask, aTask).
Since:
6.0.1
See Also:TaskPackage.getTTask()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description TBoolean getAllowClaimWhenSuspended () Returns the value of the 'Allow Claim When Suspended ' attribute. java.lang.String getApplicationDefaultsComponentName () Returns the value of the 'Application Defaults Component Name ' attribute TBoolean getAutoClaim () Returns the value of the 'Auto Claim ' attribute. TAutoDeletionMode getAutoDeletionMode () Returns the value of the 'Auto Deletion Mode ' attribute. TAutonomy getAutonomy () Returns the value of the 'Autonomy ' attribute. TBoolean getBusinessRelevance () Returns the value of the 'Business Relevance ' attribute. java.lang.String getCalendarJNDIName () Returns the value of the 'Calendar JNDI Name ' attribute java.lang.String getCalendarName () Returns the value of the 'Calendar Name ' attribute java.lang.String getContainmentContextComponentName () Returns the value of the 'Containment Context Component Name ' attribute TContextAuthorizationForOwner getContextAuthorizationForOwner () Returns the value of the 'Context Authorization For Owner ' attribute. org.eclipse.emf.common.util.EList getCustomProperty () Returns the value of the 'Custom Property ' containment reference list. java.lang.String getDefaultLocale () Returns the value of the 'Default Locale ' attribute org.eclipse.emf.common.util.EList getDescription () Returns the value of the 'Description ' containment reference list. org.eclipse.emf.common.util.EList getDisplayName () Returns the value of the 'Display Name ' containment reference list. org.eclipse.emf.common.util.EList getDocumentation () Returns the value of the 'Documentation ' containment reference list. java.lang.String getDurationUntilDeleted () Returns the value of the 'Duration Until Deleted ' attribute java.lang.String getDurationUntilDue () Returns the value of the 'Duration Until Due ' attribute java.lang.String getDurationUntilExpires () Returns the value of the 'Duration Until Expires ' attribute org.eclipse.emf.common.util.EList getEmail () Returns the value of the 'Email ' containment reference list. TEscalationSettings getEscalationSettings () Returns the value of the 'Escalation Settings ' containment reference java.lang.String getEventHandlerName () Returns the value of the 'Event Handler Name ' attribute TImport getImport () Returns the value of the 'Import ' containment reference TInterface getInterface () Returns the value of the 'Interface ' containment reference java.lang.String getJndiNameStaffPluginProvider () Returns the value of the 'Jndi Name Staff Plugin Provider ' attribute. TTaskKinds getKind () Returns the value of the 'Kind ' attribute. java.lang.String getName () Returns the value of the 'Name ' attribute int getPriority () Returns the value of the 'Priority ' attribute. java.lang.String getPriorityDefinition () Returns the value of the 'Priority Definition ' attribute TStaffSettings getStaffSettings () Returns the value of the 'Staff Settings ' containment reference TSubstitutionKinds getSubstitutionPolicy () Returns the value of the 'Substitution Policy ' attribute. TBoolean getSupportsDelegation () Returns the value of the 'Supports Delegation ' attribute. TBoolean getSupportsFollowOnTask () Returns the value of the 'Supports Follow On Task ' attribute. TBoolean getSupportsSubTask () Returns the value of the 'Supports Sub Task ' attribute. org.eclipse.emf.common.util.URI getTargetNamespace () Returns the value of the 'Target Namespace ' attribute java.lang.String getType () Returns the value of the 'Type ' attribute TUISettings getUiSettings () Returns the value of the 'Ui Settings ' containment reference java.lang.String getValidFrom () Returns the value of the 'Valid From ' attribute java.lang.String getWorkBasket () Returns the value of the 'Work Basket ' attribute boolean isInline () boolean isSetAllowClaimWhenSuspended () Returns whether the value of the 'Allow Claim When Suspended ' attribute is set boolean isSetAutoClaim () Returns whether the value of the 'Auto Claim ' attribute is set boolean isSetAutoDeletionMode () Returns whether the value of the 'Auto Deletion Mode ' attribute is set boolean isSetAutonomy () Returns whether the value of the 'Autonomy ' attribute is set boolean isSetBusinessRelevance () Returns whether the value of the 'Business Relevance ' attribute is set boolean isSetContextAuthorizationForOwner () Returns whether the value of the 'Context Authorization For Owner ' attribute is set boolean isSetJndiNameStaffPluginProvider () Returns whether the value of the 'Jndi Name Staff Plugin Provider ' attribute is set boolean isSetKind () Returns whether the value of the 'Kind ' attribute is set boolean isSetPriority () Returns whether the value of the 'Priority ' attribute is set boolean isSetSubstitutionPolicy () Returns whether the value of the 'Substitution Policy ' attribute is set boolean isSetSupportsDelegation () Returns whether the value of the 'Supports Delegation ' attribute is set boolean isSetSupportsFollowOnTask () Returns whether the value of the 'Supports Follow On Task ' attribute is set boolean isSetSupportsSubTask () Returns whether the value of the 'Supports Sub Task ' attribute is set void setAllowClaimWhenSuspended (TBoolean value) Sets the value of the 'Allow Claim When Suspended ' attribute void setApplicationDefaultsComponentName (java.lang.String value) Sets the value of the 'Application Defaults Component Name ' attribute void setAutoClaim (TBoolean value) Sets the value of the 'Auto Claim ' attribute void setAutoDeletionMode (TAutoDeletionMode value) Sets the value of the 'Auto Deletion Mode ' attribute void setAutonomy (TAutonomy value) Sets the value of the 'Autonomy ' attribute void setBusinessRelevance (TBoolean value) Sets the value of the 'Business Relevance ' attribute void setCalendarJNDIName (java.lang.String value) Sets the value of the 'Calendar JNDI Name ' attribute void setCalendarName (java.lang.String value) Sets the value of the 'Calendar Name ' attribute void setContainmentContextComponentName (java.lang.String value) Sets the value of the 'Containment Context Component Name ' attribute void setContextAuthorizationForOwner (TContextAuthorizationForOwner value) Sets the value of the 'Context Authorization For Owner ' attribute void setDefaultLocale (java.lang.String value) Sets the value of the 'Default Locale ' attribute void setDurationUntilDeleted (java.lang.String value) Sets the value of the 'Duration Until Deleted ' attribute void setDurationUntilDue (java.lang.String value) Sets the value of the 'Duration Until Due ' attribute void setDurationUntilExpires (java.lang.String value) Sets the value of the 'Duration Until Expires ' attribute void setEscalationSettings (TEscalationSettings value) Sets the value of the 'Escalation Settings ' containment reference void setEventHandlerName (java.lang.String value) Sets the value of the 'Event Handler Name ' attribute void setImport (TImport value) Sets the value of the 'Import ' containment reference void setInterface (TInterface value) Sets the value of the 'Interface ' containment reference void setJndiNameStaffPluginProvider (java.lang.String value) Sets the value of the 'Jndi Name Staff Plugin Provider ' attribute void setKind (TTaskKinds value) Sets the value of the 'Kind ' attribute void setName (java.lang.String value) Sets the value of the 'Name ' attribute void setPriority (int value) Sets the value of the 'Priority ' attribute void setPriorityDefinition (java.lang.String value) Sets the value of the 'Priority Definition ' attribute void setStaffSettings (TStaffSettings value) Sets the value of the 'Staff Settings ' containment reference void setSubstitutionPolicy (TSubstitutionKinds value) Sets the value of the 'Substitution Policy ' attribute void setSupportsDelegation (TBoolean value) Sets the value of the 'Supports Delegation ' attribute void setSupportsFollowOnTask (TBoolean value) Sets the value of the 'Supports Follow On Task ' attribute void setSupportsSubTask (TBoolean value) Sets the value of the 'Supports Sub Task ' attribute void setTargetNamespace (org.eclipse.emf.common.util.URI value) Sets the value of the 'Target Namespace ' attribute void setType (java.lang.String value) Sets the value of the 'Type ' attribute void setUiSettings (TUISettings value) Sets the value of the 'Ui Settings ' containment reference void setValidFrom (java.lang.String value) Sets the value of the 'Valid From ' attribute void setWorkBasket (java.lang.String value) Sets the value of the 'Work Basket ' attribute void unsetAllowClaimWhenSuspended () Unsets the value of the 'Allow Claim When Suspended ' attribute void unsetAutoClaim () Unsets the value of the 'Auto Claim ' attribute void unsetAutoDeletionMode () Unsets the value of the 'Auto Deletion Mode ' attribute void unsetAutonomy () Unsets the value of the 'Autonomy ' attribute void unsetBusinessRelevance () Unsets the value of the 'Business Relevance ' attribute void unsetContextAuthorizationForOwner () Unsets the value of the 'Context Authorization For Owner ' attribute void unsetJndiNameStaffPluginProvider () Unsets the value of the 'Jndi Name Staff Plugin Provider ' attribute void unsetKind () Unsets the value of the 'Kind ' attribute void unsetPriority () Unsets the value of the 'Priority ' attribute void unsetSubstitutionPolicy () Unsets the value of the 'Substitution Policy ' attribute void unsetSupportsDelegation () Unsets the value of the 'Supports Delegation ' attribute void unsetSupportsFollowOnTask () Unsets the value of the 'Supports Follow On Task ' attribute void unsetSupportsSubTask () Unsets the value of the 'Supports Sub Task ' attribute

### Method Summary

| Modifier and Type                 | Method and Description                                                                                                                 |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| TBoolean                          | getAllowClaimWhenSuspended() Returns the value of the 'Allow Claim When Suspended' attribute.                                          |
| java.lang.String                  | getApplicationDefaultsComponentName() Returns the value of the 'Application Defaults Component Name' attribute                         |
| TBoolean                          | getAutoClaim() Returns the value of the 'Auto Claim' attribute.                                                                        |
| TAutoDeletionMode                 | getAutoDeletionMode() Returns the value of the 'Auto Deletion Mode' attribute.                                                         |
| TAutonomy                         | getAutonomy() Returns the value of the 'Autonomy' attribute.                                                                           |
| TBoolean                          | getBusinessRelevance() Returns the value of the 'Business Relevance' attribute.                                                        |
| java.lang.String                  | getCalendarJNDIName() Returns the value of the 'Calendar JNDI Name' attribute                                                          |
| java.lang.String                  | getCalendarName() Returns the value of the 'Calendar Name' attribute                                                                   |
| java.lang.String                  | getContainmentContextComponentName() Returns the value of the 'Containment Context Component Name' attribute                           |
| TContextAuthorizationForOwner     | getContextAuthorizationForOwner() Returns the value of the 'Context Authorization For Owner' attribute.                                |
| org.eclipse.emf.common.util.EList | getCustomProperty() Returns the value of the 'Custom Property' containment reference list.                                             |
| java.lang.String                  | getDefaultLocale() Returns the value of the 'Default Locale' attribute                                                                 |
| org.eclipse.emf.common.util.EList | getDescription() Returns the value of the 'Description' containment reference list.                                                    |
| org.eclipse.emf.common.util.EList | getDisplayName() Returns the value of the 'Display Name' containment reference list.                                                   |
| org.eclipse.emf.common.util.EList | getDocumentation() Returns the value of the 'Documentation' containment reference list.                                                |
| java.lang.String                  | getDurationUntilDeleted() Returns the value of the 'Duration Until Deleted' attribute                                                  |
| java.lang.String                  | getDurationUntilDue() Returns the value of the 'Duration Until Due' attribute                                                          |
| java.lang.String                  | getDurationUntilExpires() Returns the value of the 'Duration Until Expires' attribute                                                  |
| org.eclipse.emf.common.util.EList | getEmail() Returns the value of the 'Email' containment reference list.                                                                |
| TEscalationSettings               | getEscalationSettings() Returns the value of the 'Escalation Settings' containment reference                                           |
| java.lang.String                  | getEventHandlerName() Returns the value of the 'Event Handler Name' attribute                                                          |
| TImport                           | getImport() Returns the value of the 'Import' containment reference                                                                    |
| TInterface                        | getInterface() Returns the value of the 'Interface' containment reference                                                              |
| java.lang.String                  | getJndiNameStaffPluginProvider() Returns the value of the 'Jndi Name Staff Plugin Provider' attribute.                                 |
| TTaskKinds                        | getKind() Returns the value of the 'Kind' attribute.                                                                                   |
| java.lang.String                  | getName() Returns the value of the 'Name' attribute                                                                                    |
| int                               | getPriority() Returns the value of the 'Priority' attribute.                                                                           |
| java.lang.String                  | getPriorityDefinition() Returns the value of the 'Priority Definition' attribute                                                       |
| TStaffSettings                    | getStaffSettings() Returns the value of the 'Staff Settings' containment reference                                                     |
| TSubstitutionKinds                | getSubstitutionPolicy() Returns the value of the 'Substitution Policy' attribute.                                                      |
| TBoolean                          | getSupportsDelegation() Returns the value of the 'Supports Delegation' attribute.                                                      |
| TBoolean                          | getSupportsFollowOnTask() Returns the value of the 'Supports Follow On Task' attribute.                                                |
| TBoolean                          | getSupportsSubTask() Returns the value of the 'Supports Sub Task' attribute.                                                           |
| org.eclipse.emf.common.util.URI   | getTargetNamespace() Returns the value of the 'Target Namespace' attribute                                                             |
| java.lang.String                  | getType() Returns the value of the 'Type' attribute                                                                                    |
| TUISettings                       | getUiSettings() Returns the value of the 'Ui Settings' containment reference                                                           |
| java.lang.String                  | getValidFrom() Returns the value of the 'Valid From' attribute                                                                         |
| java.lang.String                  | getWorkBasket() Returns the value of the 'Work Basket' attribute                                                                       |
| boolean                           | isInline()                                                                                                                             |
| boolean                           | isSetAllowClaimWhenSuspended() Returns whether the value of the 'Allow Claim When Suspended' attribute is set                          |
| boolean                           | isSetAutoClaim() Returns whether the value of the 'Auto Claim' attribute is set                                                        |
| boolean                           | isSetAutoDeletionMode() Returns whether the value of the 'Auto Deletion Mode' attribute is set                                         |
| boolean                           | isSetAutonomy() Returns whether the value of the 'Autonomy' attribute is set                                                           |
| boolean                           | isSetBusinessRelevance() Returns whether the value of the 'Business Relevance' attribute is set                                        |
| boolean                           | isSetContextAuthorizationForOwner() Returns whether the value of the 'Context Authorization For Owner' attribute is set                |
| boolean                           | isSetJndiNameStaffPluginProvider() Returns whether the value of the 'Jndi Name Staff Plugin Provider' attribute is set                 |
| boolean                           | isSetKind() Returns whether the value of the 'Kind' attribute is set                                                                   |
| boolean                           | isSetPriority() Returns whether the value of the 'Priority' attribute is set                                                           |
| boolean                           | isSetSubstitutionPolicy() Returns whether the value of the 'Substitution Policy' attribute is set                                      |
| boolean                           | isSetSupportsDelegation() Returns whether the value of the 'Supports Delegation' attribute is set                                      |
| boolean                           | isSetSupportsFollowOnTask() Returns whether the value of the 'Supports Follow On Task' attribute is set                                |
| boolean                           | isSetSupportsSubTask() Returns whether the value of the 'Supports Sub Task' attribute is set                                           |
| void                              | setAllowClaimWhenSuspended(TBoolean value) Sets the value of the 'Allow Claim When Suspended' attribute                                |
| void                              | setApplicationDefaultsComponentName(java.lang.String value) Sets the value of the 'Application Defaults Component Name' attribute      |
| void                              | setAutoClaim(TBoolean value) Sets the value of the 'Auto Claim' attribute                                                              |
| void                              | setAutoDeletionMode(TAutoDeletionMode value) Sets the value of the 'Auto Deletion Mode' attribute                                      |
| void                              | setAutonomy(TAutonomy value) Sets the value of the 'Autonomy' attribute                                                                |
| void                              | setBusinessRelevance(TBoolean value) Sets the value of the 'Business Relevance' attribute                                              |
| void                              | setCalendarJNDIName(java.lang.String value) Sets the value of the 'Calendar JNDI Name' attribute                                       |
| void                              | setCalendarName(java.lang.String value) Sets the value of the 'Calendar Name' attribute                                                |
| void                              | setContainmentContextComponentName(java.lang.String value) Sets the value of the 'Containment Context Component Name' attribute        |
| void                              | setContextAuthorizationForOwner(TContextAuthorizationForOwner value) Sets the value of the 'Context Authorization For Owner' attribute |
| void                              | setDefaultLocale(java.lang.String value) Sets the value of the 'Default Locale' attribute                                              |
| void                              | setDurationUntilDeleted(java.lang.String value) Sets the value of the 'Duration Until Deleted' attribute                               |
| void                              | setDurationUntilDue(java.lang.String value) Sets the value of the 'Duration Until Due' attribute                                       |
| void                              | setDurationUntilExpires(java.lang.String value) Sets the value of the 'Duration Until Expires' attribute                               |
| void                              | setEscalationSettings(TEscalationSettings value) Sets the value of the 'Escalation Settings' containment reference                     |
| void                              | setEventHandlerName(java.lang.String value) Sets the value of the 'Event Handler Name' attribute                                       |
| void                              | setImport(TImport value) Sets the value of the 'Import' containment reference                                                          |
| void                              | setInterface(TInterface value) Sets the value of the 'Interface' containment reference                                                 |
| void                              | setJndiNameStaffPluginProvider(java.lang.String value) Sets the value of the 'Jndi Name Staff Plugin Provider' attribute               |
| void                              | setKind(TTaskKinds value) Sets the value of the 'Kind' attribute                                                                       |
| void                              | setName(java.lang.String value) Sets the value of the 'Name' attribute                                                                 |
| void                              | setPriority(int value) Sets the value of the 'Priority' attribute                                                                      |
| void                              | setPriorityDefinition(java.lang.String value) Sets the value of the 'Priority Definition' attribute                                    |
| void                              | setStaffSettings(TStaffSettings value) Sets the value of the 'Staff Settings' containment reference                                    |
| void                              | setSubstitutionPolicy(TSubstitutionKinds value) Sets the value of the 'Substitution Policy' attribute                                  |
| void                              | setSupportsDelegation(TBoolean value) Sets the value of the 'Supports Delegation' attribute                                            |
| void                              | setSupportsFollowOnTask(TBoolean value) Sets the value of the 'Supports Follow On Task' attribute                                      |
| void                              | setSupportsSubTask(TBoolean value) Sets the value of the 'Supports Sub Task' attribute                                                 |
| void                              | setTargetNamespace(org.eclipse.emf.common.util.URI value) Sets the value of the 'Target Namespace' attribute                           |
| void                              | setType(java.lang.String value) Sets the value of the 'Type' attribute                                                                 |
| void                              | setUiSettings(TUISettings value) Sets the value of the 'Ui Settings' containment reference                                             |
| void                              | setValidFrom(java.lang.String value) Sets the value of the 'Valid From' attribute                                                      |
| void                              | setWorkBasket(java.lang.String value) Sets the value of the 'Work Basket' attribute                                                    |
| void                              | unsetAllowClaimWhenSuspended() Unsets the value of the 'Allow Claim When Suspended' attribute                                          |
| void                              | unsetAutoClaim() Unsets the value of the 'Auto Claim' attribute                                                                        |
| void                              | unsetAutoDeletionMode() Unsets the value of the 'Auto Deletion Mode' attribute                                                         |
| void                              | unsetAutonomy() Unsets the value of the 'Autonomy' attribute                                                                           |
| void                              | unsetBusinessRelevance() Unsets the value of the 'Business Relevance' attribute                                                        |
| void                              | unsetContextAuthorizationForOwner() Unsets the value of the 'Context Authorization For Owner' attribute                                |
| void                              | unsetJndiNameStaffPluginProvider() Unsets the value of the 'Jndi Name Staff Plugin Provider' attribute                                 |
| void                              | unsetKind() Unsets the value of the 'Kind' attribute                                                                                   |
| void                              | unsetPriority() Unsets the value of the 'Priority' attribute                                                                           |
| void                              | unsetSubstitutionPolicy() Unsets the value of the 'Substitution Policy' attribute                                                      |
| void                              | unsetSupportsDelegation() Unsets the value of the 'Supports Delegation' attribute                                                      |
| void                              | unsetSupportsFollowOnTask() Unsets the value of the 'Supports Follow On Task' attribute                                                |
| void                              | unsetSupportsSubTask() Unsets the value of the 'Supports Sub Task' attribute                                                           |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver