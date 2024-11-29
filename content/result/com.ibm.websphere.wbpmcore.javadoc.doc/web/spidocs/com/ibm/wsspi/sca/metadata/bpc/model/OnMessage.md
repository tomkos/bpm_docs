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

## Interface OnMessage

- All Superinterfaces: org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier public interface OnMessage extends org.eclipse.emf.ecore.EObject begin-user-doc A representation of the model object 'On Message '. end-user-doc The following features are supported: See Also: com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getOnMessage()

```
public interface OnMessage
extends org.eclipse.emf.ecore.EObject
```

The following features are supported:
 
Activity
Operation
Wpc Id

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description Activity getActivity () Returns the value of the 'Activity ' containment reference java.lang.String getOperation () Returns the value of the 'Operation ' attribute java.lang.String getWpcId () Returns the value of the 'Wpc Id ' attribute void setActivity (Activity value) Sets the value of the 'Activity ' containment reference void setOperation (java.lang.String value) Sets the value of the 'Operation ' attribute void setWpcId (java.lang.String value) Sets the value of the 'Wpc Id ' attribute

### Method Summary

| Modifier and Type   | Method and Description                                                             |
|---------------------|------------------------------------------------------------------------------------|
| Activity            | getActivity() Returns the value of the 'Activity' containment reference            |
| java.lang.String    | getOperation() Returns the value of the 'Operation' attribute                      |
| java.lang.String    | getWpcId() Returns the value of the 'Wpc Id' attribute                             |
| void                | setActivity(Activity value) Sets the value of the 'Activity' containment reference |
| void                | setOperation(java.lang.String value) Sets the value of the 'Operation' attribute   |
| void                | setWpcId(java.lang.String value) Sets the value of the 'Wpc Id' attribute          |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver