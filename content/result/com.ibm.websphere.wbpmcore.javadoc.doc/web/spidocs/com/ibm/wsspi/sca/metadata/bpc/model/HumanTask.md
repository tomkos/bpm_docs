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

## Interface HumanTask

- All Superinterfaces: org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier public interface HumanTask extends org.eclipse.emf.ecore.EObject begin-user-doc A representation of the model object 'Human Task '. end-user-doc The following features are supported: See Also: com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getHumanTask()

```
public interface HumanTask
extends org.eclipse.emf.ecore.EObject
```

The following features are supported:
 
Staff Settings
Description
Display Name
JNDI Name Staff Plugin Provider
Kind
Name
Namespace
Operation
TKTID
Type
Valid From
Work Basket Name

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getDescription () Returns the value of the 'Description ' attribute java.lang.String getDisplayName () Returns the value of the 'Display Name ' attribute java.lang.String getJNDINameStaffPluginProvider () Returns the value of the 'JNDI Name Staff Plugin Provider ' attribute HumanTaskKind getKind () Returns the value of the 'Kind ' attribute. java.lang.String getName () Returns the value of the 'Name ' attribute java.lang.String getNamespace () Returns the value of the 'Namespace ' attribute java.lang.String getOperation () Returns the value of the 'Operation ' attribute org.eclipse.emf.common.util.EList getStaffSettings () Returns the value of the 'Staff Settings ' containment reference list. java.lang.String getTKTID () Returns the value of the 'TKTID ' attribute HumanTaskType getType () Returns the value of the 'Type ' attribute. java.util.Date getValidFrom () Returns the value of the 'Valid From ' attribute java.lang.String getWorkBasketName () Returns the value of the 'Work Basket Name ' attribute boolean isSetKind () Returns whether the value of the 'Kind ' attribute is set boolean isSetType () Returns whether the value of the 'Type ' attribute is set void setDescription (java.lang.String value) Sets the value of the 'Description ' attribute void setDisplayName (java.lang.String value) Sets the value of the 'Display Name ' attribute void setJNDINameStaffPluginProvider (java.lang.String value) Sets the value of the 'JNDI Name Staff Plugin Provider ' attribute void setKind (HumanTaskKind value) Sets the value of the 'Kind ' attribute void setName (java.lang.String value) Sets the value of the 'Name ' attribute void setNamespace (java.lang.String value) Sets the value of the 'Namespace ' attribute void setOperation (java.lang.String value) Sets the value of the 'Operation ' attribute void setTKTID (java.lang.String value) Sets the value of the 'TKTID ' attribute void setType (HumanTaskType value) Sets the value of the 'Type ' attribute void setValidFrom (java.util.Date value) Sets the value of the 'Valid From ' attribute void setWorkBasketName (java.lang.String value) Sets the value of the 'Work Basket Name ' attribute void unsetKind () Unsets the value of the 'Kind ' attribute void unsetType () Unsets the value of the 'Type ' attribute

### Method Summary

| Modifier and Type                 | Method and Description                                                                                                   |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| java.lang.String                  | getDescription() Returns the value of the 'Description' attribute                                                        |
| java.lang.String                  | getDisplayName() Returns the value of the 'Display Name' attribute                                                       |
| java.lang.String                  | getJNDINameStaffPluginProvider() Returns the value of the 'JNDI Name Staff Plugin Provider' attribute                    |
| HumanTaskKind                     | getKind() Returns the value of the 'Kind' attribute.                                                                     |
| java.lang.String                  | getName() Returns the value of the 'Name' attribute                                                                      |
| java.lang.String                  | getNamespace() Returns the value of the 'Namespace' attribute                                                            |
| java.lang.String                  | getOperation() Returns the value of the 'Operation' attribute                                                            |
| org.eclipse.emf.common.util.EList | getStaffSettings() Returns the value of the 'Staff Settings' containment reference list.                                 |
| java.lang.String                  | getTKTID() Returns the value of the 'TKTID' attribute                                                                    |
| HumanTaskType                     | getType() Returns the value of the 'Type' attribute.                                                                     |
| java.util.Date                    | getValidFrom() Returns the value of the 'Valid From' attribute                                                           |
| java.lang.String                  | getWorkBasketName() Returns the value of the 'Work Basket Name' attribute                                                |
| boolean                           | isSetKind() Returns whether the value of the 'Kind' attribute is set                                                     |
| boolean                           | isSetType() Returns whether the value of the 'Type' attribute is set                                                     |
| void                              | setDescription(java.lang.String value) Sets the value of the 'Description' attribute                                     |
| void                              | setDisplayName(java.lang.String value) Sets the value of the 'Display Name' attribute                                    |
| void                              | setJNDINameStaffPluginProvider(java.lang.String value) Sets the value of the 'JNDI Name Staff Plugin Provider' attribute |
| void                              | setKind(HumanTaskKind value) Sets the value of the 'Kind' attribute                                                      |
| void                              | setName(java.lang.String value) Sets the value of the 'Name' attribute                                                   |
| void                              | setNamespace(java.lang.String value) Sets the value of the 'Namespace' attribute                                         |
| void                              | setOperation(java.lang.String value) Sets the value of the 'Operation' attribute                                         |
| void                              | setTKTID(java.lang.String value) Sets the value of the 'TKTID' attribute                                                 |
| void                              | setType(HumanTaskType value) Sets the value of the 'Type' attribute                                                      |
| void                              | setValidFrom(java.util.Date value) Sets the value of the 'Valid From' attribute                                          |
| void                              | setWorkBasketName(java.lang.String value) Sets the value of the 'Work Basket Name' attribute                             |
| void                              | unsetKind() Unsets the value of the 'Kind' attribute                                                                     |
| void                              | unsetType() Unsets the value of the 'Type' attribute                                                                     |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver