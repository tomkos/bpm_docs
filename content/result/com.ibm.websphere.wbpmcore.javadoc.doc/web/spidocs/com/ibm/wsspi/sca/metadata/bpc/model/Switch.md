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

## Interface Switch

- All Superinterfaces: Activity , org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier public interface Switch extends Activity begin-user-doc A representation of the model object 'Switch '. end-user-doc The following features are supported: See Also: com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getSwitch()

```
public interface Switch
extends Activity
```

The following features are supported:
 
Case
Otherwise
Complex End ATID

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description org.eclipse.emf.common.util.EList getCase () Returns the value of the 'Case ' containment reference list. java.lang.String getComplexEndATID () Returns the value of the 'Complex End ATID ' attribute Case getOtherwise () Returns the value of the 'Otherwise ' containment reference void setComplexEndATID (java.lang.String value) Sets the value of the 'Complex End ATID ' attribute void setOtherwise (Case value) Sets the value of the 'Otherwise ' containment reference

### Method Summary

| Modifier and Type                 | Method and Description                                                                       |
|-----------------------------------|----------------------------------------------------------------------------------------------|
| org.eclipse.emf.common.util.EList | getCase() Returns the value of the 'Case' containment reference list.                        |
| java.lang.String                  | getComplexEndATID() Returns the value of the 'Complex End ATID' attribute                    |
| Case                              | getOtherwise() Returns the value of the 'Otherwise' containment reference                    |
| void                              | setComplexEndATID(java.lang.String value) Sets the value of the 'Complex End ATID' attribute |
| void                              | setOtherwise(Case value) Sets the value of the 'Otherwise' containment reference             |

- Methods inherited from interface com.ibm.wsspi.sca.metadata.bpc.model.Activity
getATID, getDisplayName, getIncomingGateway, getKind, getName, getOutgoingGateway, getWpcId, isGenerated, isSetGenerated, isSetIncomingGateway, isSetKind, isSetOutgoingGateway, setATID, setDisplayName, setGenerated, setIncomingGateway, setKind, setName, setOutgoingGateway, setWpcId, unsetGenerated, unsetIncomingGateway, unsetKind, unsetOutgoingGateway

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver