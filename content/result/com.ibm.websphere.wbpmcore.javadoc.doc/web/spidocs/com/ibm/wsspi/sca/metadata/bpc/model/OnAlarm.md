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

## Interface OnAlarm

- All Superinterfaces: org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier public interface OnAlarm extends org.eclipse.emf.ecore.EObject begin-user-doc A representation of the model object 'On Alarm '. end-user-doc The following features are supported: See Also: com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getOnAlarm()

```
public interface OnAlarm
extends org.eclipse.emf.ecore.EObject
```

The following features are supported:
 
Activity
Wpc Id

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description Activity getActivity () Returns the value of the 'Activity ' containment reference java.lang.String getWpcId () Returns the value of the 'Wpc Id ' attribute void setActivity (Activity value) Sets the value of the 'Activity ' containment reference void setWpcId (java.lang.String value) Sets the value of the 'Wpc Id ' attribute

### Method Summary

| Modifier and Type   | Method and Description                                                             |
|---------------------|------------------------------------------------------------------------------------|
| Activity            | getActivity() Returns the value of the 'Activity' containment reference            |
| java.lang.String    | getWpcId() Returns the value of the 'Wpc Id' attribute                             |
| void                | setActivity(Activity value) Sets the value of the 'Activity' containment reference |
| void                | setWpcId(java.lang.String value) Sets the value of the 'Wpc Id' attribute          |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver