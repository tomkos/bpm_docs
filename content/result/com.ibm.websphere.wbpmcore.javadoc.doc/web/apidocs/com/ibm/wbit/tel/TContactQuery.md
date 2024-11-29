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

## Interface TContactQuery

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier, TStaffRole

public interface TContactQuery
extends TStaffRole

 A representation of the model object 'TContact Query'.
 

 contact query staff role
Since:
6.0.1
See Also:TaskPackage.getTContactQuery()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getCategory () Returns the value of the 'Category ' attribute void setCategory (java.lang.String value) Sets the value of the 'Category ' attribute

### Method Summary

| Modifier and Type   | Method and Description                                                         |
|---------------------|--------------------------------------------------------------------------------|
| java.lang.String    | getCategory() Returns the value of the 'Category' attribute                    |
| void                | setCategory(java.lang.String value) Sets the value of the 'Category' attribute |

- Methods inherited from interface com.ibm.wbit.tel.TStaffRole
getVerb, setVerb

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver