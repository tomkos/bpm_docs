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

## Interface TApplyTo

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TApplyTo
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TApply To'.
 

 
         If the attribute 'role' of an 'applyTo' element has the value 'all', 
         further 'applyTo' elements of the same JSP are ignored.
Since:
6.0.1
See Also:TaskPackage.getTApplyTo()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description TJspApplicableRole getRole () Returns the value of the 'Role ' attribute. boolean isSetRole () Returns whether the value of the 'Role ' attribute is set void setRole (TJspApplicableRole value) Sets the value of the 'Role ' attribute void unsetRole () Unsets the value of the 'Role ' attribute

### Method Summary

| Modifier and Type   | Method and Description                                                   |
|---------------------|--------------------------------------------------------------------------|
| TJspApplicableRole  | getRole() Returns the value of the 'Role' attribute.                     |
| boolean             | isSetRole() Returns whether the value of the 'Role' attribute is set     |
| void                | setRole(TJspApplicableRole value) Sets the value of the 'Role' attribute |
| void                | unsetRole() Unsets the value of the 'Role' attribute                     |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver