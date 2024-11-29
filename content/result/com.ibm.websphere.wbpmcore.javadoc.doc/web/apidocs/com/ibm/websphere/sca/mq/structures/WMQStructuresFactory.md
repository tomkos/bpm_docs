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

## Interface WMQStructuresFactory

- All Superinterfaces:
org.eclipse.emf.ecore.EFactory, org.eclipse.emf.ecore.EModelElement, org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface WMQStructuresFactory
extends org.eclipse.emf.ecore.EFactory

 The Factory for the model.
 It provides a create method for each non-abstract class of the model.
 
See Also:WMQStructuresPackage

- =========== PROPERTY SUMMARY =========== =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Property Summary

Properties 

Type
Property and Description

MQRFH2Property
createMQRFH2
Returns a new object of class 'MQRFH2 Property'

MQRFHProperty
createMQRFH
Returns a new object of class 'MQRFH Property'
    - Field Summary

Fields 

Modifier and Type
Field and Description

static WMQStructuresFactory
eINSTANCE 

static WMQStructuresFactory
INSTANCE
The singleton instance of the factory
    - Method Summary Methods Modifier and Type Method and Description DocumentRoot createDocumentRoot () Returns a new object of class 'Document Root ' MQCIH createMQCIH () Returns a new object of class 'MQCIH ' MQControl createMQControl () Returns a new object of class 'MQ Control ' MQHeader createMQHeader () Returns a new object of class 'MQ Header ' MQHeaders createMQHeaders () Returns a new object of class 'MQ Headers ' MQIIH createMQIIH () Returns a new object of class 'MQIIH ' MQMD createMQMD () Returns a new object of class 'MQMD ' MQOpaqueHeader createMQOpaqueHeader () Returns a new object of class 'MQ Opaque Header ' MQRFH createMQRFH () Returns a new object of class 'MQRFH ' MQRFH2 createMQRFH2 () Returns a new object of class 'MQRFH2 ' MQRFH2Group createMQRFH2Group () Returns a new object of class 'MQRFH2 Group ' MQRFH2Property createMQRFH2Property () Returns a new object of class 'MQRFH2 Property ' MQRFHProperty createMQRFHProperty () Returns a new object of class 'MQRFH Property ' WMQStructuresPackage getWMQStructuresPackage () Returns the package supported by this factory

### Method Summary

| Modifier and Type    | Method and Description                                                  |
|----------------------|-------------------------------------------------------------------------|
| DocumentRoot         | createDocumentRoot() Returns a new object of class 'Document Root'      |
| MQCIH                | createMQCIH() Returns a new object of class 'MQCIH'                     |
| MQControl            | createMQControl() Returns a new object of class 'MQ Control'            |
| MQHeader             | createMQHeader() Returns a new object of class 'MQ Header'              |
| MQHeaders            | createMQHeaders() Returns a new object of class 'MQ Headers'            |
| MQIIH                | createMQIIH() Returns a new object of class 'MQIIH'                     |
| MQMD                 | createMQMD() Returns a new object of class 'MQMD'                       |
| MQOpaqueHeader       | createMQOpaqueHeader() Returns a new object of class 'MQ Opaque Header' |
| MQRFH                | createMQRFH() Returns a new object of class 'MQRFH'                     |
| MQRFH2               | createMQRFH2() Returns a new object of class 'MQRFH2'                   |
| MQRFH2Group          | createMQRFH2Group() Returns a new object of class 'MQRFH2 Group'        |
| MQRFH2Property       | createMQRFH2Property() Returns a new object of class 'MQRFH2 Property'  |
| MQRFHProperty        | createMQRFHProperty() Returns a new object of class 'MQRFH Property'    |
| WMQStructuresPackage | getWMQStructuresPackage() Returns the package supported by this factory |

- Methods inherited from interface org.eclipse.emf.ecore.EFactory
convertToString, create, createFromString, getEPackage, setEPackage

- Methods inherited from interface org.eclipse.emf.ecore.EModelElement
getEAnnotation, getEAnnotations

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver