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

## Interface TEscalation

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TEscalation
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TEscalation'.
 

Since:
6.0.1
See Also:TaskPackage.getTEscalation()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description TAtLeastExpectedStates getAtLeastExpectedState () Returns the value of the 'At Least Expected State ' attribute. java.lang.String getAutoRepeatDuration () Returns the value of the 'Auto Repeat Duration ' attribute org.eclipse.emf.common.util.EList getCustomProperty () Returns the value of the 'Custom Property ' containment reference list. org.eclipse.emf.common.util.EList getDescription () Returns the value of the 'Description ' containment reference list. org.eclipse.emf.common.util.EList getDisplayName () Returns the value of the 'Display Name ' containment reference list. org.eclipse.emf.common.util.EList getDocumentation () Returns the value of the 'Documentation ' containment reference list. java.lang.String getDurationUntilEscalation () Returns the value of the 'Duration Until Escalation ' attribute java.lang.String getEmail () Returns the value of the 'Email ' attribute TEMailReceiver getEMailReceiver () Returns the value of the 'EMail Receiver ' containment reference TEscalationActions getEscalationAction () Returns the value of the 'Escalation Action ' attribute. TEscalationReceiver getEscalationReceiver () Returns the value of the 'Escalation Receiver ' containment reference TIncreasePriority getIncreasePriority () Returns the value of the 'Increase Priority ' attribute. java.lang.String getName () Returns the value of the 'Name ' attribute boolean isSetAtLeastExpectedState () Returns whether the value of the 'At Least Expected State ' attribute is set boolean isSetEscalationAction () Returns whether the value of the 'Escalation Action ' attribute is set boolean isSetIncreasePriority () Returns whether the value of the 'Increase Priority ' attribute is set void setAtLeastExpectedState (TAtLeastExpectedStates value) Sets the value of the 'At Least Expected State ' attribute void setAutoRepeatDuration (java.lang.String value) Sets the value of the 'Auto Repeat Duration ' attribute void setDurationUntilEscalation (java.lang.String value) Sets the value of the 'Duration Until Escalation ' attribute void setEmail (java.lang.String value) Sets the value of the 'Email ' attribute void setEMailReceiver (TEMailReceiver value) Sets the value of the 'EMail Receiver ' containment reference void setEscalationAction (TEscalationActions value) Sets the value of the 'Escalation Action ' attribute void setEscalationReceiver (TEscalationReceiver value) Sets the value of the 'Escalation Receiver ' containment reference void setIncreasePriority (TIncreasePriority value) Sets the value of the 'Increase Priority ' attribute void setName (java.lang.String value) Sets the value of the 'Name ' attribute void unsetAtLeastExpectedState () Unsets the value of the 'At Least Expected State ' attribute void unsetEscalationAction () Unsets the value of the 'Escalation Action ' attribute void unsetIncreasePriority () Unsets the value of the 'Increase Priority ' attribute

### Method Summary

| Modifier and Type                 | Method and Description                                                                                             |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------|
| TAtLeastExpectedStates            | getAtLeastExpectedState() Returns the value of the 'At Least Expected State' attribute.                            |
| java.lang.String                  | getAutoRepeatDuration() Returns the value of the 'Auto Repeat Duration' attribute                                  |
| org.eclipse.emf.common.util.EList | getCustomProperty() Returns the value of the 'Custom Property' containment reference list.                         |
| org.eclipse.emf.common.util.EList | getDescription() Returns the value of the 'Description' containment reference list.                                |
| org.eclipse.emf.common.util.EList | getDisplayName() Returns the value of the 'Display Name' containment reference list.                               |
| org.eclipse.emf.common.util.EList | getDocumentation() Returns the value of the 'Documentation' containment reference list.                            |
| java.lang.String                  | getDurationUntilEscalation() Returns the value of the 'Duration Until Escalation' attribute                        |
| java.lang.String                  | getEmail() Returns the value of the 'Email' attribute                                                              |
| TEMailReceiver                    | getEMailReceiver() Returns the value of the 'EMail Receiver' containment reference                                 |
| TEscalationActions                | getEscalationAction() Returns the value of the 'Escalation Action' attribute.                                      |
| TEscalationReceiver               | getEscalationReceiver() Returns the value of the 'Escalation Receiver' containment reference                       |
| TIncreasePriority                 | getIncreasePriority() Returns the value of the 'Increase Priority' attribute.                                      |
| java.lang.String                  | getName() Returns the value of the 'Name' attribute                                                                |
| boolean                           | isSetAtLeastExpectedState() Returns whether the value of the 'At Least Expected State' attribute is set            |
| boolean                           | isSetEscalationAction() Returns whether the value of the 'Escalation Action' attribute is set                      |
| boolean                           | isSetIncreasePriority() Returns whether the value of the 'Increase Priority' attribute is set                      |
| void                              | setAtLeastExpectedState(TAtLeastExpectedStates value) Sets the value of the 'At Least Expected State' attribute    |
| void                              | setAutoRepeatDuration(java.lang.String value) Sets the value of the 'Auto Repeat Duration' attribute               |
| void                              | setDurationUntilEscalation(java.lang.String value) Sets the value of the 'Duration Until Escalation' attribute     |
| void                              | setEmail(java.lang.String value) Sets the value of the 'Email' attribute                                           |
| void                              | setEMailReceiver(TEMailReceiver value) Sets the value of the 'EMail Receiver' containment reference                |
| void                              | setEscalationAction(TEscalationActions value) Sets the value of the 'Escalation Action' attribute                  |
| void                              | setEscalationReceiver(TEscalationReceiver value) Sets the value of the 'Escalation Receiver' containment reference |
| void                              | setIncreasePriority(TIncreasePriority value) Sets the value of the 'Increase Priority' attribute                   |
| void                              | setName(java.lang.String value) Sets the value of the 'Name' attribute                                             |
| void                              | unsetAtLeastExpectedState() Unsets the value of the 'At Least Expected State' attribute                            |
| void                              | unsetEscalationAction() Unsets the value of the 'Escalation Action' attribute                                      |
| void                              | unsetIncreasePriority() Unsets the value of the 'Increase Priority' attribute                                      |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver