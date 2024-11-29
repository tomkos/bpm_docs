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

## Interface DocumentRoot

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface DocumentRoot
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'Document Root'.
Since:
6.0.1
See Also:TaskPackage.getDocumentRoot()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description org.eclipse.emf.ecore.util.FeatureMap getMixed () Returns the value of the 'Mixed ' attribute list. TTask getTask () Returns the value of the 'Task ' containment reference org.eclipse.emf.common.util.EMap getXMLNSPrefixMap () Returns the value of the 'XMLNS Prefix Map ' map. org.eclipse.emf.common.util.EMap getXSISchemaLocation () Returns the value of the 'XSI Schema Location ' map. void setTask (TTask value) Sets the value of the 'Task ' containment reference

### Method Summary

| Modifier and Type                     | Method and Description                                                     |
|---------------------------------------|----------------------------------------------------------------------------|
| org.eclipse.emf.ecore.util.FeatureMap | getMixed() Returns the value of the 'Mixed' attribute list.                |
| TTask                                 | getTask() Returns the value of the 'Task' containment reference            |
| org.eclipse.emf.common.util.EMap      | getXMLNSPrefixMap() Returns the value of the 'XMLNS Prefix Map' map.       |
| org.eclipse.emf.common.util.EMap      | getXSISchemaLocation() Returns the value of the 'XSI Schema Location' map. |
| void                                  | setTask(TTask value) Sets the value of the 'Task' containment reference    |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver