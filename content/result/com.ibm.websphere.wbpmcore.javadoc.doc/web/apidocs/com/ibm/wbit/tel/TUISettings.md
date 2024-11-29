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

## Interface TUISettings

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TUISettings
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TUI Settings'.
 

Since:
6.0.1
See Also:TaskPackage.getTUISettings()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description org.eclipse.emf.common.util.EList getCustomClientSettings () Returns the value of the 'Custom Client Settings ' containment reference list. org.eclipse.emf.common.util.EList getPortalClientSettings () Returns the value of the 'Portal Client Settings ' containment reference list. org.eclipse.emf.common.util.EList getWebClientSettings () Returns the value of the 'Web Client Settings ' containment reference list.

### Method Summary

| Modifier and Type                 | Method and Description                                                                                  |
|-----------------------------------|---------------------------------------------------------------------------------------------------------|
| org.eclipse.emf.common.util.EList | getCustomClientSettings() Returns the value of the 'Custom Client Settings' containment reference list. |
| org.eclipse.emf.common.util.EList | getPortalClientSettings() Returns the value of the 'Portal Client Settings' containment reference list. |
| org.eclipse.emf.common.util.EList | getWebClientSettings() Returns the value of the 'Web Client Settings' containment reference list.       |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver