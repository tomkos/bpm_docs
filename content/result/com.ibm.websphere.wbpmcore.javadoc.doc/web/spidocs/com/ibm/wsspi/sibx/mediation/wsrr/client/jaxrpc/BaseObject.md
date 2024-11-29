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

## Class BaseObject

- java.lang.Object
    - com.ibm.wsspi.sibx.mediation.wsrr.client.jaxrpc.BaseObject

- Direct Known Subclasses:
LogicalObject, OriginalObject

public abstract class BaseObject
extends java.lang.Object
The base WSRR object. All concrete WSRR objects inherit from this object.

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

BaseObject()
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getBsrURI () java.lang.String[] getClassificationURIs () java.lang.String getClassificationURIs (int i) java.lang.String getCreationTimestamp () java.lang.String getDescription () java.lang.String getLastModified () java.lang.String getLastModifiedBy () java.lang.String getName () java.lang.String getNamespace () java.lang.String getOwner () UserDefinedProperty [] getUserDefinedProperties () UserDefinedProperty getUserDefinedProperties (int i) UserDefinedRelationship [] getUserDefinedRelationships () UserDefinedRelationship getUserDefinedRelationships (int i) java.lang.String getVersion () void setBsrURI (java.lang.String bsrURI) void setClassificationURIs (int i, java.lang.String value) void setClassificationURIs (java.lang.String[] classificationURIs) void setCreationTimestamp (java.lang.String creationTimestamp) void setDescription (java.lang.String description) void setLastModified (java.lang.String lastModified) void setLastModifiedBy (java.lang.String lastModifiedBy) void setName (java.lang.String name) void setNamespace (java.lang.String namespace) void setOwner (java.lang.String owner) void setUserDefinedProperties (int i, UserDefinedProperty value) void setUserDefinedProperties (UserDefinedProperty [] userDefinedProperties) void setUserDefinedRelationships (int i, UserDefinedRelationship value) void setUserDefinedRelationships (UserDefinedRelationship [] userDefinedRelationships) void setVersion (java.lang.String version)

### Method Summary

| Modifier and Type         | Method and Description                                                                       |
|---------------------------|----------------------------------------------------------------------------------------------|
| java.lang.String          | getBsrURI()                                                                                  |
| java.lang.String[]        | getClassificationURIs()                                                                      |
| java.lang.String          | getClassificationURIs(int i)                                                                 |
| java.lang.String          | getCreationTimestamp()                                                                       |
| java.lang.String          | getDescription()                                                                             |
| java.lang.String          | getLastModified()                                                                            |
| java.lang.String          | getLastModifiedBy()                                                                          |
| java.lang.String          | getName()                                                                                    |
| java.lang.String          | getNamespace()                                                                               |
| java.lang.String          | getOwner()                                                                                   |
| UserDefinedProperty[]     | getUserDefinedProperties()                                                                   |
| UserDefinedProperty       | getUserDefinedProperties(int i)                                                              |
| UserDefinedRelationship[] | getUserDefinedRelationships()                                                                |
| UserDefinedRelationship   | getUserDefinedRelationships(int i)                                                           |
| java.lang.String          | getVersion()                                                                                 |
| void                      | setBsrURI(java.lang.String bsrURI)                                                           |
| void                      | setClassificationURIs(int i,                      java.lang.String value)                    |
| void                      | setClassificationURIs(java.lang.String[] classificationURIs)                                 |
| void                      | setCreationTimestamp(java.lang.String creationTimestamp)                                     |
| void                      | setDescription(java.lang.String description)                                                 |
| void                      | setLastModified(java.lang.String lastModified)                                               |
| void                      | setLastModifiedBy(java.lang.String lastModifiedBy)                                           |
| void                      | setName(java.lang.String name)                                                               |
| void                      | setNamespace(java.lang.String namespace)                                                     |
| void                      | setOwner(java.lang.String owner)                                                             |
| void                      | setUserDefinedProperties(int i,                         UserDefinedProperty value)           |
| void                      | setUserDefinedProperties(UserDefinedProperty[] userDefinedProperties)                        |
| void                      | setUserDefinedRelationships(int i,                            UserDefinedRelationship value) |
| void                      | setUserDefinedRelationships(UserDefinedRelationship[] userDefinedRelationships)              |
| void                      | setVersion(java.lang.String version)                                                         |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait