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

## Interface Process

- All Superinterfaces: org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier public interface Process extends org.eclipse.emf.ecore.EObject begin-user-doc A representation of the model object 'Process '. end-user-doc The following features are supported: See Also: com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getProcess()

```
public interface Process
extends org.eclipse.emf.ecore.EObject
```

The following features are supported:
 
Activity
Link
Display Name
Mode
Name
Namespace
PTID
Valid From
Wpc Id

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description Activity getActivity () Returns the value of the 'Activity ' containment reference java.lang.String getDisplayName () Returns the value of the 'Display Name ' attribute org.eclipse.emf.common.util.EList getLink () Returns the value of the 'Link ' containment reference list. ProcessMode getMode () Returns the value of the 'Mode ' attribute. java.lang.String getName () Returns the value of the 'Name ' attribute java.lang.String getNamespace () Returns the value of the 'Namespace ' attribute java.lang.String getPTID () Returns the value of the 'PTID ' attribute java.util.Date getValidFrom () Returns the value of the 'Valid From ' attribute java.lang.String getWpcId () Returns the value of the 'Wpc Id ' attribute boolean isSetMode () Returns whether the value of the 'Mode ' attribute is set void setActivity (Activity value) Sets the value of the 'Activity ' containment reference void setDisplayName (java.lang.String value) Sets the value of the 'Display Name ' attribute void setMode (ProcessMode value) Sets the value of the 'Mode ' attribute void setName (java.lang.String value) Sets the value of the 'Name ' attribute void setNamespace (java.lang.String value) Sets the value of the 'Namespace ' attribute void setPTID (java.lang.String value) Sets the value of the 'PTID ' attribute void setValidFrom (java.util.Date value) Sets the value of the 'Valid From ' attribute void setWpcId (java.lang.String value) Sets the value of the 'Wpc Id ' attribute void unsetMode () Unsets the value of the 'Mode ' attribute

### Method Summary

| Modifier and Type                 | Method and Description                                                                |
|-----------------------------------|---------------------------------------------------------------------------------------|
| Activity                          | getActivity() Returns the value of the 'Activity' containment reference               |
| java.lang.String                  | getDisplayName() Returns the value of the 'Display Name' attribute                    |
| org.eclipse.emf.common.util.EList | getLink() Returns the value of the 'Link' containment reference list.                 |
| ProcessMode                       | getMode() Returns the value of the 'Mode' attribute.                                  |
| java.lang.String                  | getName() Returns the value of the 'Name' attribute                                   |
| java.lang.String                  | getNamespace() Returns the value of the 'Namespace' attribute                         |
| java.lang.String                  | getPTID() Returns the value of the 'PTID' attribute                                   |
| java.util.Date                    | getValidFrom() Returns the value of the 'Valid From' attribute                        |
| java.lang.String                  | getWpcId() Returns the value of the 'Wpc Id' attribute                                |
| boolean                           | isSetMode() Returns whether the value of the 'Mode' attribute is set                  |
| void                              | setActivity(Activity value) Sets the value of the 'Activity' containment reference    |
| void                              | setDisplayName(java.lang.String value) Sets the value of the 'Display Name' attribute |
| void                              | setMode(ProcessMode value) Sets the value of the 'Mode' attribute                     |
| void                              | setName(java.lang.String value) Sets the value of the 'Name' attribute                |
| void                              | setNamespace(java.lang.String value) Sets the value of the 'Namespace' attribute      |
| void                              | setPTID(java.lang.String value) Sets the value of the 'PTID' attribute                |
| void                              | setValidFrom(java.util.Date value) Sets the value of the 'Valid From' attribute       |
| void                              | setWpcId(java.lang.String value) Sets the value of the 'Wpc Id' attribute             |
| void                              | unsetMode() Unsets the value of the 'Mode' attribute                                  |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver