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

## Interface TEmail

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TEmail
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TEmail'.
 

 
         User-definable multi-language template for an email
Since:
6.0.1
See Also:TaskPackage.getTEmail()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
copyright
    - Method Summary Methods Modifier and Type Method and Description org.eclipse.emf.common.util.EList getLocalizedEmail () Returns the value of the 'Localized Email ' containment reference list. java.lang.String getName () Returns the value of the 'Name ' attribute void setName (java.lang.String value) Sets the value of the 'Name ' attribute

### Method Summary

| Modifier and Type                 | Method and Description                                                                     |
|-----------------------------------|--------------------------------------------------------------------------------------------|
| org.eclipse.emf.common.util.EList | getLocalizedEmail() Returns the value of the 'Localized Email' containment reference list. |
| java.lang.String                  | getName() Returns the value of the 'Name' attribute                                        |
| void                              | setName(java.lang.String value) Sets the value of the 'Name' attribute                     |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver