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

## Interface TEscalationChain

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TEscalationChain
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TEscalation Chain'.
 

Since:
6.0.1
See Also:TaskPackage.getTEscalationChain()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description TActivationStates getActivationState () Returns the value of the 'Activation State ' attribute. org.eclipse.emf.common.util.EList getEscalation () Returns the value of the 'Escalation ' containment reference list. boolean isSetActivationState () Returns whether the value of the 'Activation State ' attribute is set void setActivationState (TActivationStates value) Sets the value of the 'Activation State ' attribute void unsetActivationState () Unsets the value of the 'Activation State ' attribute

### Method Summary

| Modifier and Type                 | Method and Description                                                                         |
|-----------------------------------|------------------------------------------------------------------------------------------------|
| TActivationStates                 | getActivationState() Returns the value of the 'Activation State' attribute.                    |
| org.eclipse.emf.common.util.EList | getEscalation() Returns the value of the 'Escalation' containment reference list.              |
| boolean                           | isSetActivationState() Returns whether the value of the 'Activation State' attribute is set    |
| void                              | setActivationState(TActivationStates value) Sets the value of the 'Activation State' attribute |
| void                              | unsetActivationState() Unsets the value of the 'Activation State' attribute                    |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver