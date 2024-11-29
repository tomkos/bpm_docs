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

## Interface TImport

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TImport
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TImport'.
 

 Same behavior than defined in WS-BPEL:
         The presence of an import element should be interpreted as a hint to 
         the WS-BPEL processor. In particular, processors are not required to 
         retrieve the imported document from the location specified on the 
         import element.
Since:
6.0.1
See Also:TaskPackage.getTImport()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description org.eclipse.emf.common.util.URI getImportType () Returns the value of the 'Import Type ' attribute org.eclipse.emf.common.util.URI getLocation () Returns the value of the 'Location ' attribute org.eclipse.emf.common.util.URI getNamespace () Returns the value of the 'Namespace ' attribute void setImportType (org.eclipse.emf.common.util.URI value) Sets the value of the 'Import Type ' attribute void setLocation (org.eclipse.emf.common.util.URI value) Sets the value of the 'Location ' attribute void setNamespace (org.eclipse.emf.common.util.URI value) Sets the value of the 'Namespace ' attribute

### Method Summary

| Modifier and Type               | Method and Description                                                                             |
|---------------------------------|----------------------------------------------------------------------------------------------------|
| org.eclipse.emf.common.util.URI | getImportType() Returns the value of the 'Import Type' attribute                                   |
| org.eclipse.emf.common.util.URI | getLocation() Returns the value of the 'Location' attribute                                        |
| org.eclipse.emf.common.util.URI | getNamespace() Returns the value of the 'Namespace' attribute                                      |
| void                            | setImportType(org.eclipse.emf.common.util.URI value) Sets the value of the 'Import Type' attribute |
| void                            | setLocation(org.eclipse.emf.common.util.URI value) Sets the value of the 'Location' attribute      |
| void                            | setNamespace(org.eclipse.emf.common.util.URI value) Sets the value of the 'Namespace' attribute    |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver