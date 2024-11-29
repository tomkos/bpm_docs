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

## Class OriginalObject

- java.lang.Object
    - com.ibm.wsspi.sibx.mediation.wsrr.client.jaxrpc.BaseObject
        - com.ibm.wsspi.sibx.mediation.wsrr.client.jaxrpc.OriginalObject

- Direct Known Subclasses:
Document, GenericObject, QueryObject, SCAModule

public abstract class OriginalObject
extends BaseObject
Represents an OriginalObject WSRR object

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

OriginalObject()
    - Method Summary Methods Modifier and Type Method and Description java.lang.String[] getPredecessors () java.lang.String getTemplate () void setPredecessors (java.lang.String[] predecessors) void setTemplate (java.lang.String template)

### Method Summary

| Modifier and Type   | Method and Description                           |
|---------------------|--------------------------------------------------|
| java.lang.String[]  | getPredecessors()                                |
| java.lang.String    | getTemplate()                                    |
| void                | setPredecessors(java.lang.String[] predecessors) |
| void                | setTemplate(java.lang.String template)           |

    - Methods inherited from class com.ibm.wsspi.sibx.mediation.wsrr.client.jaxrpc.BaseObject
getBsrURI, getClassificationURIs, getClassificationURIs, getCreationTimestamp, getDescription, getLastModified, getLastModifiedBy, getName, getNamespace, getOwner, getUserDefinedProperties, getUserDefinedProperties, getUserDefinedRelationships, getUserDefinedRelationships, getVersion, setBsrURI, setClassificationURIs, setClassificationURIs, setCreationTimestamp, setDescription, setLastModified, setLastModifiedBy, setName, setNamespace, setOwner, setUserDefinedProperties, setUserDefinedProperties, setUserDefinedRelationships, setUserDefinedRelationships, setVersion
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait