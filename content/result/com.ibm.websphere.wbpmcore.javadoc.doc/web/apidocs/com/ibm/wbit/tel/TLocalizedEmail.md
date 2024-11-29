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

## Interface TLocalizedEmail

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TLocalizedEmail
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TLocalized Email'.
 

 
         User-definable email template for a single locale
Since:
6.0.1
See Also:TaskPackage.getTLocalizedEmail()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
copyright
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getBody () Returns the value of the 'Body ' attribute java.lang.String getLocale () Returns the value of the 'Locale ' attribute java.lang.String getSubject () Returns the value of the 'Subject ' attribute void setBody (java.lang.String value) Sets the value of the 'Body ' attribute void setLocale (java.lang.String value) Sets the value of the 'Locale ' attribute void setSubject (java.lang.String value) Sets the value of the 'Subject ' attribute

### Method Summary

| Modifier and Type   | Method and Description                                                       |
|---------------------|------------------------------------------------------------------------------|
| java.lang.String    | getBody() Returns the value of the 'Body' attribute                          |
| java.lang.String    | getLocale() Returns the value of the 'Locale' attribute                      |
| java.lang.String    | getSubject() Returns the value of the 'Subject' attribute                    |
| void                | setBody(java.lang.String value) Sets the value of the 'Body' attribute       |
| void                | setLocale(java.lang.String value) Sets the value of the 'Locale' attribute   |
| void                | setSubject(java.lang.String value) Sets the value of the 'Subject' attribute |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver