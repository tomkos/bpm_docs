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

## Interface Pick

- All Superinterfaces: Activity , org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier public interface Pick extends Activity begin-user-doc A representation of the model object 'Pick '. end-user-doc The following features are supported: See Also: com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getPick()

```
public interface Pick
extends Activity
```

The following features are supported:
 
On Message
On Alarm
Complex End ATID
Initializing

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getComplexEndATID () Returns the value of the 'Complex End ATID ' attribute org.eclipse.emf.common.util.EList getOnAlarm () Returns the value of the 'On Alarm ' containment reference list. org.eclipse.emf.common.util.EList getOnMessage () Returns the value of the 'On Message ' containment reference list. boolean isInitializing () Returns the value of the 'Initializing ' attribute boolean isSetInitializing () Returns whether the value of the 'Initializing ' attribute is set void setComplexEndATID (java.lang.String value) Sets the value of the 'Complex End ATID ' attribute void setInitializing (boolean value) Sets the value of the 'Initializing ' attribute void unsetInitializing () Unsets the value of the 'Initializing ' attribute

### Method Summary

| Modifier and Type                 | Method and Description                                                                       |
|-----------------------------------|----------------------------------------------------------------------------------------------|
| java.lang.String                  | getComplexEndATID() Returns the value of the 'Complex End ATID' attribute                    |
| org.eclipse.emf.common.util.EList | getOnAlarm() Returns the value of the 'On Alarm' containment reference list.                 |
| org.eclipse.emf.common.util.EList | getOnMessage() Returns the value of the 'On Message' containment reference list.             |
| boolean                           | isInitializing() Returns the value of the 'Initializing' attribute                           |
| boolean                           | isSetInitializing() Returns whether the value of the 'Initializing' attribute is set         |
| void                              | setComplexEndATID(java.lang.String value) Sets the value of the 'Complex End ATID' attribute |
| void                              | setInitializing(boolean value) Sets the value of the 'Initializing' attribute                |
| void                              | unsetInitializing() Unsets the value of the 'Initializing' attribute                         |

- Methods inherited from interface com.ibm.wsspi.sca.metadata.bpc.model.Activity
getATID, getDisplayName, getIncomingGateway, getKind, getName, getOutgoingGateway, getWpcId, isGenerated, isSetGenerated, isSetIncomingGateway, isSetKind, isSetOutgoingGateway, setATID, setDisplayName, setGenerated, setIncomingGateway, setKind, setName, setOutgoingGateway, setWpcId, unsetGenerated, unsetIncomingGateway, unsetKind, unsetOutgoingGateway

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver