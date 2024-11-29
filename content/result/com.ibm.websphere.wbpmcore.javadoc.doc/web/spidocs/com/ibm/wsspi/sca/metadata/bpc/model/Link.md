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

## Interface Link

- All Superinterfaces: org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier public interface Link extends org.eclipse.emf.ecore.EObject begin-user-doc A representation of the model object 'Link '. end-user-doc The following features are supported: See Also: com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getLink()

```
public interface Link
extends org.eclipse.emf.ecore.EObject
```

The following features are supported:
 
Fault Name
From Activity Id
From ATID
Generated
Kind
To Activity Id
To ATID
Wpc Id

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description javax.xml.namespace.QName getFaultName () Returns the value of the 'Fault Name ' attribute java.lang.String getFromActivityId () Returns the value of the 'From Activity Id ' attribute java.lang.String getFromATID () Returns the value of the 'From ATID ' attribute LinkKind getKind () Returns the value of the 'Kind ' attribute. java.lang.String getToActivityId () Returns the value of the 'To Activity Id ' attribute java.lang.String getToATID () Returns the value of the 'To ATID ' attribute java.lang.String getWpcId () Returns the value of the 'Wpc Id ' attribute boolean isGenerated () Returns the value of the 'Generated ' attribute boolean isSetGenerated () Returns whether the value of the 'Generated ' attribute is set boolean isSetKind () Returns whether the value of the 'Kind ' attribute is set void setFaultName (javax.xml.namespace.QName value) Sets the value of the 'Fault Name ' attribute void setFromActivityId (java.lang.String value) Sets the value of the 'From Activity Id ' attribute void setFromATID (java.lang.String value) Sets the value of the 'From ATID ' attribute void setGenerated (boolean value) Sets the value of the 'Generated ' attribute void setKind (LinkKind value) Sets the value of the 'Kind ' attribute void setToActivityId (java.lang.String value) Sets the value of the 'To Activity Id ' attribute void setToATID (java.lang.String value) Sets the value of the 'To ATID ' attribute void setWpcId (java.lang.String value) Sets the value of the 'Wpc Id ' attribute void unsetGenerated () Unsets the value of the 'Generated ' attribute void unsetKind () Unsets the value of the 'Kind ' attribute

### Method Summary

| Modifier and Type         | Method and Description                                                                       |
|---------------------------|----------------------------------------------------------------------------------------------|
| javax.xml.namespace.QName | getFaultName() Returns the value of the 'Fault Name' attribute                               |
| java.lang.String          | getFromActivityId() Returns the value of the 'From Activity Id' attribute                    |
| java.lang.String          | getFromATID() Returns the value of the 'From ATID' attribute                                 |
| LinkKind                  | getKind() Returns the value of the 'Kind' attribute.                                         |
| java.lang.String          | getToActivityId() Returns the value of the 'To Activity Id' attribute                        |
| java.lang.String          | getToATID() Returns the value of the 'To ATID' attribute                                     |
| java.lang.String          | getWpcId() Returns the value of the 'Wpc Id' attribute                                       |
| boolean                   | isGenerated() Returns the value of the 'Generated' attribute                                 |
| boolean                   | isSetGenerated() Returns whether the value of the 'Generated' attribute is set               |
| boolean                   | isSetKind() Returns whether the value of the 'Kind' attribute is set                         |
| void                      | setFaultName(javax.xml.namespace.QName value) Sets the value of the 'Fault Name' attribute   |
| void                      | setFromActivityId(java.lang.String value) Sets the value of the 'From Activity Id' attribute |
| void                      | setFromATID(java.lang.String value) Sets the value of the 'From ATID' attribute              |
| void                      | setGenerated(boolean value) Sets the value of the 'Generated' attribute                      |
| void                      | setKind(LinkKind value) Sets the value of the 'Kind' attribute                               |
| void                      | setToActivityId(java.lang.String value) Sets the value of the 'To Activity Id' attribute     |
| void                      | setToATID(java.lang.String value) Sets the value of the 'To ATID' attribute                  |
| void                      | setWpcId(java.lang.String value) Sets the value of the 'Wpc Id' attribute                    |
| void                      | unsetGenerated() Unsets the value of the 'Generated' attribute                               |
| void                      | unsetKind() Unsets the value of the 'Kind' attribute                                         |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver