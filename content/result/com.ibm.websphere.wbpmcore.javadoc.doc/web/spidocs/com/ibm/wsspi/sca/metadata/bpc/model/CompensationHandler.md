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

## Interface CompensationHandler

- All Superinterfaces: org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier public interface CompensationHandler extends org.eclipse.emf.ecore.EObject begin-user-doc A representation of the model object 'Compensation Handler '. end-user-doc The following features are supported: See Also: com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getCompensationHandler()

```
public interface CompensationHandler
extends org.eclipse.emf.ecore.EObject
```

The following features are supported:
 
Activity

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description Activity getActivity () Returns the value of the 'Activity ' containment reference void setActivity (Activity value) Sets the value of the 'Activity ' containment reference

### Method Summary

| Modifier and Type   | Method and Description                                                             |
|---------------------|------------------------------------------------------------------------------------|
| Activity            | getActivity() Returns the value of the 'Activity' containment reference            |
| void                | setActivity(Activity value) Sets the value of the 'Activity' containment reference |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver