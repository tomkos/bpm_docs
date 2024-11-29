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

## Interface Activity

- All Superinterfaces: org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier All Known Subinterfaces: InlineHumanTask , Invoke , PartnerActivity , Pick , Receive , Scope , StructuredActivity , Switch public interface Activity extends org.eclipse.emf.ecore.EObject begin-user-doc A representation of the model object 'Activity '. end-user-doc The following features are supported: See Also: com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getActivity()

```
public interface Activity
extends org.eclipse.emf.ecore.EObject
```

The following features are supported:
 
ATID
Display Name
Generated
Incoming Gateway
Kind
Name
Outgoing Gateway
Wpc Id

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getATID () Returns the value of the 'ATID ' attribute java.lang.String getDisplayName () Returns the value of the 'Display Name ' attribute GatewayKind getIncomingGateway () Returns the value of the 'Incoming Gateway ' attribute. ActivityKind getKind () Returns the value of the 'Kind ' attribute. java.lang.String getName () Returns the value of the 'Name ' attribute GatewayKind getOutgoingGateway () Returns the value of the 'Outgoing Gateway ' attribute. java.lang.String getWpcId () Returns the value of the 'Wpc Id ' attribute boolean isGenerated () Returns the value of the 'Generated ' attribute boolean isSetGenerated () Returns whether the value of the 'Generated ' attribute is set boolean isSetIncomingGateway () Returns whether the value of the 'Incoming Gateway ' attribute is set boolean isSetKind () Returns whether the value of the 'Kind ' attribute is set boolean isSetOutgoingGateway () Returns whether the value of the 'Outgoing Gateway ' attribute is set void setATID (java.lang.String value) Sets the value of the 'ATID ' attribute void setDisplayName (java.lang.String value) Sets the value of the 'Display Name ' attribute void setGenerated (boolean value) Sets the value of the 'Generated ' attribute void setIncomingGateway (GatewayKind value) Sets the value of the 'Incoming Gateway ' attribute void setKind (ActivityKind value) Sets the value of the 'Kind ' attribute void setName (java.lang.String value) Sets the value of the 'Name ' attribute void setOutgoingGateway (GatewayKind value) Sets the value of the 'Outgoing Gateway ' attribute void setWpcId (java.lang.String value) Sets the value of the 'Wpc Id ' attribute void unsetGenerated () Unsets the value of the 'Generated ' attribute void unsetIncomingGateway () Unsets the value of the 'Incoming Gateway ' attribute void unsetKind () Unsets the value of the 'Kind ' attribute void unsetOutgoingGateway () Unsets the value of the 'Outgoing Gateway ' attribute

### Method Summary

| Modifier and Type   | Method and Description                                                                      |
|---------------------|---------------------------------------------------------------------------------------------|
| java.lang.String    | getATID() Returns the value of the 'ATID' attribute                                         |
| java.lang.String    | getDisplayName() Returns the value of the 'Display Name' attribute                          |
| GatewayKind         | getIncomingGateway() Returns the value of the 'Incoming Gateway' attribute.                 |
| ActivityKind        | getKind() Returns the value of the 'Kind' attribute.                                        |
| java.lang.String    | getName() Returns the value of the 'Name' attribute                                         |
| GatewayKind         | getOutgoingGateway() Returns the value of the 'Outgoing Gateway' attribute.                 |
| java.lang.String    | getWpcId() Returns the value of the 'Wpc Id' attribute                                      |
| boolean             | isGenerated() Returns the value of the 'Generated' attribute                                |
| boolean             | isSetGenerated() Returns whether the value of the 'Generated' attribute is set              |
| boolean             | isSetIncomingGateway() Returns whether the value of the 'Incoming Gateway' attribute is set |
| boolean             | isSetKind() Returns whether the value of the 'Kind' attribute is set                        |
| boolean             | isSetOutgoingGateway() Returns whether the value of the 'Outgoing Gateway' attribute is set |
| void                | setATID(java.lang.String value) Sets the value of the 'ATID' attribute                      |
| void                | setDisplayName(java.lang.String value) Sets the value of the 'Display Name' attribute       |
| void                | setGenerated(boolean value) Sets the value of the 'Generated' attribute                     |
| void                | setIncomingGateway(GatewayKind value) Sets the value of the 'Incoming Gateway' attribute    |
| void                | setKind(ActivityKind value) Sets the value of the 'Kind' attribute                          |
| void                | setName(java.lang.String value) Sets the value of the 'Name' attribute                      |
| void                | setOutgoingGateway(GatewayKind value) Sets the value of the 'Outgoing Gateway' attribute    |
| void                | setWpcId(java.lang.String value) Sets the value of the 'Wpc Id' attribute                   |
| void                | unsetGenerated() Unsets the value of the 'Generated' attribute                              |
| void                | unsetIncomingGateway() Unsets the value of the 'Incoming Gateway' attribute                 |
| void                | unsetKind() Unsets the value of the 'Kind' attribute                                        |
| void                | unsetOutgoingGateway() Unsets the value of the 'Outgoing Gateway' attribute                 |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver