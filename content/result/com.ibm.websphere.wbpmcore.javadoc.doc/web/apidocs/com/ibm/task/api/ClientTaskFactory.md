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

## Class ClientTaskFactory

- java.lang.Object
    - com.ibm.task.api.ClientTaskFactory

- public abstract class ClientTaskFactory
extends java.lang.Object
Factory to create a ClientTaskFactory object.
Since:
6.0.1

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Constructor Summary

Constructors 

Constructor and Description

ClientTaskFactory()
    - Method Summary Methods Modifier and Type Method and Description abstract javax.wsdl.Operation createOperation (javax.wsdl.Definition definition, javax.wsdl.PortType portType, java.lang.String name, javax.xml.namespace.QName inputType, javax.xml.namespace.QName outputType, java.util.Map faultTypes) Creates an operation with the specified name for the specified port type and WSDL definition. abstract javax.wsdl.PortType createPortType (javax.wsdl.Definition definition, java.lang.String name) Creates a port type with the specified name in the specified WSDL definition. abstract org.eclipse.emf.ecore.resource.ResourceSet createResourceSet () Creates a resource set. abstract org.eclipse.emf.ecore.resource.ResourceSet createResourceSet (java.lang.ClassLoader cl) Creates a resource set that uses the specified class loader to locate resources. static TaskModel createTaskModel (org.eclipse.emf.ecore.resource.ResourceSet resourceSet) Creates a task model. abstract TTask createTTask (org.eclipse.emf.ecore.resource.ResourceSet resourceSet, TTaskKinds taskKind, java.lang.String taskName, com.ibm.bpe.api.UTCDate validFrom, java.lang.String targetNamespace, javax.wsdl.PortType portType, javax.wsdl.Operation operation) Creates a collaboration or to-do task with the specified name in the specified resource set. abstract javax.wsdl.Definition createWSDLDefinition (org.eclipse.emf.ecore.resource.ResourceSet resourceSet, javax.xml.namespace.QName name) Creates a WSDL definition with the specified name in the specified resource set. abstract TaskFactory getTaskFactory () Returns the TaskFactory so that TTask objects can be modified. abstract org.eclipse.wst.wsdl.WSDLFactory getWSDLFactory () Returns the WSDLFactory so that WSDL objects can be created. abstract org.eclipse.xsd.XSDFactory getXSDFactory () Returns the XSDFactory so that XSD objects can be created. abstract javax.wsdl.Definition loadWSDLDefinition (org.eclipse.emf.ecore.resource.ResourceSet resourceSet, java.lang.String wsdlLocation) Retrieves the specified WSDL definition and puts it into the specified resource set. abstract org.eclipse.xsd.XSDSchema loadXSDSchema (org.eclipse.emf.ecore.resource.ResourceSet resourceSet, java.lang.String xsdLocation) Retrieves the XSD schema of the specified complex message type and puts it into the specified resource set. static ClientTaskFactory newInstance () Returns the single instance of a ClientTaskFactory.

### Method Summary

| Modifier and Type                                   | Method and Description                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract javax.wsdl.Operation                       | createOperation(javax.wsdl.Definition definition,                javax.wsdl.PortType portType,                java.lang.String name,                javax.xml.namespace.QName inputType,                javax.xml.namespace.QName outputType,                java.util.Map faultTypes) Creates an operation with the specified name for the specified port type  and WSDL definition.                                 |
| abstract javax.wsdl.PortType                        | createPortType(javax.wsdl.Definition definition,               java.lang.String name) Creates a port type with the specified name in the specified WSDL definition.                                                                                                                                                                                                                                                   |
| abstract org.eclipse.emf.ecore.resource.ResourceSet | createResourceSet() Creates a resource set.                                                                                                                                                                                                                                                                                                                                                                           |
| abstract org.eclipse.emf.ecore.resource.ResourceSet | createResourceSet(java.lang.ClassLoader cl) Creates a resource set that uses the specified class loader to locate resources.                                                                                                                                                                                                                                                                                          |
| static TaskModel                                    | createTaskModel(org.eclipse.emf.ecore.resource.ResourceSet resourceSet) Creates a task model.                                                                                                                                                                                                                                                                                                                         |
| abstract TTask                                      | createTTask(org.eclipse.emf.ecore.resource.ResourceSet resourceSet,            TTaskKinds taskKind,            java.lang.String taskName,            com.ibm.bpe.api.UTCDate validFrom,            java.lang.String targetNamespace,            javax.wsdl.PortType portType,            javax.wsdl.Operation operation) Creates a collaboration or to-do task with the specified name in the specified resource set. |
| abstract javax.wsdl.Definition                      | createWSDLDefinition(org.eclipse.emf.ecore.resource.ResourceSet resourceSet,                     javax.xml.namespace.QName name) Creates a WSDL definition with the specified name in the specified resource set.                                                                                                                                                                                                     |
| abstract TaskFactory                                | getTaskFactory() Returns the TaskFactory so that TTask objects can be modified.                                                                                                                                                                                                                                                                                                                                       |
| abstract org.eclipse.wst.wsdl.WSDLFactory           | getWSDLFactory() Returns the WSDLFactory so that WSDL objects can be created.                                                                                                                                                                                                                                                                                                                                         |
| abstract org.eclipse.xsd.XSDFactory                 | getXSDFactory() Returns the XSDFactory so that XSD objects can be created.                                                                                                                                                                                                                                                                                                                                            |
| abstract javax.wsdl.Definition                      | loadWSDLDefinition(org.eclipse.emf.ecore.resource.ResourceSet resourceSet,                   java.lang.String wsdlLocation) Retrieves the specified WSDL definition and puts it into the specified resource set.                                                                                                                                                                                                      |
| abstract org.eclipse.xsd.XSDSchema                  | loadXSDSchema(org.eclipse.emf.ecore.resource.ResourceSet resourceSet,              java.lang.String xsdLocation) Retrieves the XSD schema of the specified complex message type and puts it into the  specified resource set.                                                                                                                                                                                         |
| static ClientTaskFactory                            | newInstance() Returns the single instance of a ClientTaskFactory.                                                                                                                                                                                                                                                                                                                                                     |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait