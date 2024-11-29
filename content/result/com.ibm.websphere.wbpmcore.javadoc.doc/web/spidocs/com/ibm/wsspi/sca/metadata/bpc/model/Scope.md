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

## Interface Scope

- All Superinterfaces: Activity , org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier, StructuredActivity public interface Scope extends StructuredActivity begin-user-doc A representation of the model object 'Scope '. end-user-doc The following features are supported: See Also: com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getScope()

```
public interface Scope
extends StructuredActivity
```

The following features are supported:
 
Fault Handler
Event Handler
Compensation Handler

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description CompensationHandler getCompensationHandler () Returns the value of the 'Compensation Handler ' containment reference org.eclipse.emf.common.util.EList getEventHandler () Returns the value of the 'Event Handler ' containment reference list. org.eclipse.emf.common.util.EList getFaultHandler () Returns the value of the 'Fault Handler ' containment reference list. void setCompensationHandler (CompensationHandler value) Sets the value of the 'Compensation Handler ' containment reference

### Method Summary

| Modifier and Type                 | Method and Description                                                                                               |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------|
| CompensationHandler               | getCompensationHandler() Returns the value of the 'Compensation Handler' containment reference                       |
| org.eclipse.emf.common.util.EList | getEventHandler() Returns the value of the 'Event Handler' containment reference list.                               |
| org.eclipse.emf.common.util.EList | getFaultHandler() Returns the value of the 'Fault Handler' containment reference list.                               |
| void                              | setCompensationHandler(CompensationHandler value) Sets the value of the 'Compensation Handler' containment reference |

- Methods inherited from interface com.ibm.wsspi.sca.metadata.bpc.model.StructuredActivity
getActivities, getComplexEndATID, setComplexEndATID

- Methods inherited from interface com.ibm.wsspi.sca.metadata.bpc.model.Activity
getATID, getDisplayName, getIncomingGateway, getKind, getName, getOutgoingGateway, getWpcId, isGenerated, isSetGenerated, isSetIncomingGateway, isSetKind, isSetOutgoingGateway, setATID, setDisplayName, setGenerated, setIncomingGateway, setKind, setName, setOutgoingGateway, setWpcId, unsetGenerated, unsetIncomingGateway, unsetKind, unsetOutgoingGateway

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver