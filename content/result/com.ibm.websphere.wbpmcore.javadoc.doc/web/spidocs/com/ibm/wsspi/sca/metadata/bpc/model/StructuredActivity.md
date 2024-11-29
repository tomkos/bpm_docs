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

## Interface StructuredActivity

- All Superinterfaces: Activity , org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier All Known Subinterfaces: Scope public interface StructuredActivity extends Activity begin-user-doc A representation of the model object 'Structured Activity '. end-user-doc The following features are supported: See Also: com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getStructuredActivity()

```
public interface StructuredActivity
extends Activity
```

The following features are supported:
 
Activities
Complex End ATID

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description org.eclipse.emf.common.util.EList getActivities () Returns the value of the 'Activities ' containment reference list. java.lang.String getComplexEndATID () Returns the value of the 'Complex End ATID ' attribute void setComplexEndATID (java.lang.String value) Sets the value of the 'Complex End ATID ' attribute

### Method Summary

| Modifier and Type                 | Method and Description                                                                       |
|-----------------------------------|----------------------------------------------------------------------------------------------|
| org.eclipse.emf.common.util.EList | getActivities() Returns the value of the 'Activities' containment reference list.            |
| java.lang.String                  | getComplexEndATID() Returns the value of the 'Complex End ATID' attribute                    |
| void                              | setComplexEndATID(java.lang.String value) Sets the value of the 'Complex End ATID' attribute |

- Methods inherited from interface com.ibm.wsspi.sca.metadata.bpc.model.Activity
getATID, getDisplayName, getIncomingGateway, getKind, getName, getOutgoingGateway, getWpcId, isGenerated, isSetGenerated, isSetIncomingGateway, isSetKind, isSetOutgoingGateway, setATID, setDisplayName, setGenerated, setIncomingGateway, setKind, setName, setOutgoingGateway, setWpcId, unsetGenerated, unsetIncomingGateway, unsetKind, unsetOutgoingGateway

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver