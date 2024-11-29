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

## Interface StaffRole

- All Superinterfaces: org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier public interface StaffRole extends org.eclipse.emf.ecore.EObject begin-user-doc A representation of the model object 'Staff Role '. end-user-doc The following features are supported: See Also: com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getStaffRole()

```
public interface StaffRole
extends org.eclipse.emf.ecore.EObject
```

The following features are supported:
 
Verb
Role

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description Role getRole () Returns the value of the 'Role ' attribute. Verb getVerb () Returns the value of the 'Verb ' containment reference boolean isSetRole () Returns whether the value of the 'Role ' attribute is set void setRole (Role value) Sets the value of the 'Role ' attribute void setVerb (Verb value) Sets the value of the 'Verb ' containment reference void unsetRole () Unsets the value of the 'Role ' attribute

### Method Summary

| Modifier and Type   | Method and Description                                                 |
|---------------------|------------------------------------------------------------------------|
| Role                | getRole() Returns the value of the 'Role' attribute.                   |
| Verb                | getVerb() Returns the value of the 'Verb' containment reference        |
| boolean             | isSetRole() Returns whether the value of the 'Role' attribute is set   |
| void                | setRole(Role value) Sets the value of the 'Role' attribute             |
| void                | setVerb(Verb value) Sets the value of the 'Verb' containment reference |
| void                | unsetRole() Unsets the value of the 'Role' attribute                   |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver