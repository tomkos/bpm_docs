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

## Interface TCustomClientSettings

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

All Known Subinterfaces:
TPortalClientSettings, TWebClientSettings

public interface TCustomClientSettings
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TCustom Client Settings'.
 

 
         Abstract base type representing the map of custom client settings.
Since:
6.0.1
See Also:TaskPackage.getTCustomClientSettings()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getClientType () Returns the value of the 'Client Type ' attribute org.eclipse.emf.common.util.EList getCustomSetting () Returns the value of the 'Custom Setting ' containment reference list. void setClientType (java.lang.String value) Sets the value of the 'Client Type ' attribute

### Method Summary

| Modifier and Type                 | Method and Description                                                                   |
|-----------------------------------|------------------------------------------------------------------------------------------|
| java.lang.String                  | getClientType() Returns the value of the 'Client Type' attribute                         |
| org.eclipse.emf.common.util.EList | getCustomSetting() Returns the value of the 'Custom Setting' containment reference list. |
| void                              | setClientType(java.lang.String value) Sets the value of the 'Client Type' attribute      |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver