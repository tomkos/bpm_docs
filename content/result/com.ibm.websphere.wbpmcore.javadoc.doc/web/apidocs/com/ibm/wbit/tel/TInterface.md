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

## Interface TInterface

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TInterface
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TInterface'.
 

 
         The interface of a task is described by the port type and operation of 
         a web service, incl. the corresponding message definitions.
         For an oTask the interface is defined by the signature of the operation 
         of the service that is invoked.
         For an hTask the interface defines the signature of the operation the 
         hTask exposes.
         For an hTask the interface defines the input and output message of 
         the task.
Since:
6.0.1
See Also:TaskPackage.getTInterface()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description TInterfaceKinds getKind () Returns the value of the 'Kind ' attribute. javax.wsdl.Operation getOperation () Returns the value of the 'Operation ' attribute java.lang.String getOperationName () javax.wsdl.PortType getPortType () Returns the value of the 'Port Type ' attribute javax.xml.namespace.QName getPortTypeName () boolean isSetKind () Returns whether the value of the 'Kind ' attribute is set void setKind (TInterfaceKinds value) Sets the value of the 'Kind ' attribute void setOperation (javax.wsdl.Operation value) Sets the value of the 'Operation ' attribute void setPortType (javax.wsdl.PortType value) Sets the value of the 'Port Type ' attribute void unsetKind () Unsets the value of the 'Kind ' attribute

### Method Summary

| Modifier and Type         | Method and Description                                                               |
|---------------------------|--------------------------------------------------------------------------------------|
| TInterfaceKinds           | getKind() Returns the value of the 'Kind' attribute.                                 |
| javax.wsdl.Operation      | getOperation() Returns the value of the 'Operation' attribute                        |
| java.lang.String          | getOperationName()                                                                   |
| javax.wsdl.PortType       | getPortType() Returns the value of the 'Port Type' attribute                         |
| javax.xml.namespace.QName | getPortTypeName()                                                                    |
| boolean                   | isSetKind() Returns whether the value of the 'Kind' attribute is set                 |
| void                      | setKind(TInterfaceKinds value) Sets the value of the 'Kind' attribute                |
| void                      | setOperation(javax.wsdl.Operation value) Sets the value of the 'Operation' attribute |
| void                      | setPortType(javax.wsdl.PortType value) Sets the value of the 'Port Type' attribute   |
| void                      | unsetKind() Unsets the value of the 'Kind' attribute                                 |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver