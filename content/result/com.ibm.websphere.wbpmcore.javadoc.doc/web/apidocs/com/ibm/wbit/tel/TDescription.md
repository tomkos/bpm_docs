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

## Interface TDescription

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TDescription
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TDescription'.
 

 
         Description for artifacts, multi-language enabled. 
         May contain %XPath% expression. 
         Size after resolution is within 1 to 254.
Since:
6.0.1
See Also:TaskPackage.getTDescription()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getLocale () Returns the value of the 'Locale ' attribute java.lang.String getValue () Returns the value of the 'Value ' attribute void setLocale (java.lang.String value) Sets the value of the 'Locale ' attribute void setValue (java.lang.String value) Sets the value of the 'Value ' attribute

### Method Summary

| Modifier and Type   | Method and Description                                                     |
|---------------------|----------------------------------------------------------------------------|
| java.lang.String    | getLocale() Returns the value of the 'Locale' attribute                    |
| java.lang.String    | getValue() Returns the value of the 'Value' attribute                      |
| void                | setLocale(java.lang.String value) Sets the value of the 'Locale' attribute |
| void                | setValue(java.lang.String value) Sets the value of the 'Value' attribute   |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver