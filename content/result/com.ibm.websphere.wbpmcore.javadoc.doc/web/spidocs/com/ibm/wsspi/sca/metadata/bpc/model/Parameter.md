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

## Interface Parameter

- All Superinterfaces: org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier public interface Parameter extends org.eclipse.emf.ecore.EObject begin-user-doc A representation of the model object 'Parameter '. end-user-doc The following features are supported: See Also: com.ibm.ws.sca.metadata.bpc.model.ItcamPackage#getParameter()

```
public interface Parameter
extends org.eclipse.emf.ecore.EObject
```

The following features are supported:
 
Id
Value

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getId () Returns the value of the 'Id ' attribute java.lang.String getValue () Returns the value of the 'Value ' attribute void setId (java.lang.String value) Sets the value of the 'Id ' attribute void setValue (java.lang.String value) Sets the value of the 'Value ' attribute

### Method Summary

| Modifier and Type   | Method and Description                                                   |
|---------------------|--------------------------------------------------------------------------|
| java.lang.String    | getId() Returns the value of the 'Id' attribute                          |
| java.lang.String    | getValue() Returns the value of the 'Value' attribute                    |
| void                | setId(java.lang.String value) Sets the value of the 'Id' attribute       |
| void                | setValue(java.lang.String value) Sets the value of the 'Value' attribute |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver