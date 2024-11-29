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

## Class LogicalObject

- java.lang.Object
    - com.ibm.wsspi.sibx.mediation.wsrr.client.jaxrpc.BaseObject
        - com.ibm.wsspi.sibx.mediation.wsrr.client.jaxrpc.LogicalObject

- Direct Known Subclasses:
\_import, \_interface, AttributeDeclaration, ElementDeclaration, Export, ExportBinding, ExtensionLogicalObject, ImportBinding, LocalAttribute, Module, PolicyAttachment, PolicyExpression, SOAPAddress, SOAPBinding, WSDLBinding, WSDLFault, WSDLInput, WSDLMessage, WSDLOperation, WSDLOutput, WSDLPart, WSDLPort, WSDLPortType, WSDLService, XSDType

public abstract class LogicalObject
extends BaseObject
Represents the base LogicalObject WSRR object

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

LogicalObject()
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getDocument () ExtensionLogicalObject [] getExtensions () ExtensionLogicalObject getExtensions (int i) void setDocument (java.lang.String document) void setExtensions (ExtensionLogicalObject [] extensions) void setExtensions (int i, ExtensionLogicalObject value)

### Method Summary

| Modifier and Type        | Method and Description                                          |
|--------------------------|-----------------------------------------------------------------|
| java.lang.String         | getDocument()                                                   |
| ExtensionLogicalObject[] | getExtensions()                                                 |
| ExtensionLogicalObject   | getExtensions(int i)                                            |
| void                     | setDocument(java.lang.String document)                          |
| void                     | setExtensions(ExtensionLogicalObject[] extensions)              |
| void                     | setExtensions(int i,              ExtensionLogicalObject value) |

    - Methods inherited from class com.ibm.wsspi.sibx.mediation.wsrr.client.jaxrpc.BaseObject
getBsrURI, getClassificationURIs, getClassificationURIs, getCreationTimestamp, getDescription, getLastModified, getLastModifiedBy, getName, getNamespace, getOwner, getUserDefinedProperties, getUserDefinedProperties, getUserDefinedRelationships, getUserDefinedRelationships, getVersion, setBsrURI, setClassificationURIs, setClassificationURIs, setCreationTimestamp, setDescription, setLastModified, setLastModifiedBy, setName, setNamespace, setOwner, setUserDefinedProperties, setUserDefinedProperties, setUserDefinedRelationships, setUserDefinedRelationships, setVersion
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait