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

## Interface Receive

- All Superinterfaces: Activity , org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier, PartnerActivity public interface Receive extends PartnerActivity begin-user-doc A representation of the model object 'Receive '. end-user-doc The following features are supported: See Also: com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getReceive()

```
public interface Receive
extends PartnerActivity
```

The following features are supported:
 
Initializing

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description boolean isInitializing () Returns the value of the 'Initializing ' attribute boolean isSetInitializing () Returns whether the value of the 'Initializing ' attribute is set void setInitializing (boolean value) Sets the value of the 'Initializing ' attribute void unsetInitializing () Unsets the value of the 'Initializing ' attribute

### Method Summary

| Modifier and Type   | Method and Description                                                               |
|---------------------|--------------------------------------------------------------------------------------|
| boolean             | isInitializing() Returns the value of the 'Initializing' attribute                   |
| boolean             | isSetInitializing() Returns whether the value of the 'Initializing' attribute is set |
| void                | setInitializing(boolean value) Sets the value of the 'Initializing' attribute        |
| void                | unsetInitializing() Unsets the value of the 'Initializing' attribute                 |

- Methods inherited from interface com.ibm.wsspi.sca.metadata.bpc.model.PartnerActivity
getOperation, setOperation

- Methods inherited from interface com.ibm.wsspi.sca.metadata.bpc.model.Activity
getATID, getDisplayName, getIncomingGateway, getKind, getName, getOutgoingGateway, getWpcId, isGenerated, isSetGenerated, isSetIncomingGateway, isSetKind, isSetOutgoingGateway, setATID, setDisplayName, setGenerated, setIncomingGateway, setKind, setName, setOutgoingGateway, setWpcId, unsetGenerated, unsetIncomingGateway, unsetKind, unsetOutgoingGateway

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver