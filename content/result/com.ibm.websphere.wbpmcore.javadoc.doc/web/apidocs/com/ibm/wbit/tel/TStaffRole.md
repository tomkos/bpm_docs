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

## Interface TStaffRole

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

All Known Subinterfaces:
TAdministrator, TContactQuery, TEditor, TEMailReceiver, TEscalationReceiver, TPotentialInstanceCreator, TPotentialOwner, TPotentialStarter, TReader

public interface TStaffRole
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TStaff Role'.
 

 Super-type for all staff roles, contains staff query 
         of specific type, via staff support service verbs.
Since:
6.0.1
See Also:TaskPackage.getTStaffRole()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description TVerb getVerb () Returns the value of the 'Verb ' containment reference void setVerb (TVerb value) Sets the value of the 'Verb ' containment reference

### Method Summary

| Modifier and Type   | Method and Description                                                  |
|---------------------|-------------------------------------------------------------------------|
| TVerb               | getVerb() Returns the value of the 'Verb' containment reference         |
| void                | setVerb(TVerb value) Sets the value of the 'Verb' containment reference |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver