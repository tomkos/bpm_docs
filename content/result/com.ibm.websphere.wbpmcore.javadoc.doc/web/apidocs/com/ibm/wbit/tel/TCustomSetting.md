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

## Interface TCustomSetting

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TCustomSetting
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TCustom Setting'.
 

 
         User-definable client property, name/optional value pair
Since:
6.0.1
See Also:TaskPackage.getTCustomSetting()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getName () Returns the value of the 'Name ' attribute java.lang.String getValue () Returns the value of the 'Value ' attribute void setName (java.lang.String value) Sets the value of the 'Name ' attribute void setValue (java.lang.String value) Sets the value of the 'Value ' attribute

### Method Summary

| Modifier and Type   | Method and Description                                                   |
|---------------------|--------------------------------------------------------------------------|
| java.lang.String    | getName() Returns the value of the 'Name' attribute                      |
| java.lang.String    | getValue() Returns the value of the 'Value' attribute                    |
| void                | setName(java.lang.String value) Sets the value of the 'Name' attribute   |
| void                | setValue(java.lang.String value) Sets the value of the 'Value' attribute |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver