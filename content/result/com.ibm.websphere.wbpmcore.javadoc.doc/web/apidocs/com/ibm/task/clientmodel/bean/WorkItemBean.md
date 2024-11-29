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

## Class WorkItemBean

- java.lang.Object
    - com.ibm.task.clientmodel.bean.WorkItemBean

- public class WorkItemBean extends java.lang.Object Stores the properties of a work item retrieved from a QueryResultSet and adds metadata for national language support and converters. A work item represents a relationship between a person or group of persons and an object, typically an activity or task instance. The relationship is described by attributes such as the type of the associated object and the reason why the object is assigned. A WorkItemBean object can be instantiated from a QueryResultSet object. Only the following properties are loaded from the query result set: If the property is not found in the query result set, the property remains empty. Accessing an empty property requires the bean to load the missing information from the server. Use the static method getLabel(String, Locale) to retrieve the localized label for a property. Use the static method getConverter(String) to retrieve a converter for a property. The return value may be null because converters are optional. See Also: WorkItem , QueryResultSet

```
public class WorkItemBean
extends java.lang.Object
```

Stores the properties of a work item retrieved from a QueryResultSet 
 and adds metadata for national language support and converters.

A work item represents a relationship between a person or group of persons
 and an object, typically an activity or task instance. The relationship is
 described by attributes such as the type of the associated object and the
 reason why the object is assigned.
 A WorkItemBean object can be instantiated from
 a QueryResultSet object.
 

 Only the following properties are loaded from the query result set:
 
owner 
objectType 
objectID 
creationTime 
ID 
reason 
taskName 
assignedToEverybody 
groupName 

 If the property is not found in the query result set, the property remains empty.
 Accessing an empty property requires the bean to load the missing information
 from the server. 
 

 Use the static method getLabel(String, Locale) to
 retrieve the localized label for a property. 
 Use the static method getConverter(String) to
 retrieve a converter for a property. The return value may be null because converters 
 are optional.

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
ASSIGNEDTOEVERYBODY\_PROPERTY
Use the property name to determine labels and converters for the 
 assignedToEverybody property.

static java.lang.String
COPYRIGHT
(C) Copyright IBM Corporation 2005, 2007.

static java.lang.String
CREATIONIME\_PROPERTY
Deprecated. 
use CREATIONTIME\_PROPERTY

static java.lang.String
CREATIONTIME\_PROPERTY
Use the property name to determine labels and converters for the 
 creationTime property.

static java.lang.String
GROUPNAME\_PROPERTY
Use the property name to determine labels and converters for the 
 groupName property.

static java.lang.String
ID\_PROPERTY
Use the property name to determine labels and converters for the 
 ID property.

static java.lang.String
OBJECTID\_PROPERTY
Use the property name to determine labels and converters for the 
 objectID property.

static java.lang.String
OBJECTTYPE\_PROPERTY
Use the property name to determine labels and converters for the 
 objectType property.

static java.lang.String
OWNER\_PROPERTY
Use the property name to determine labels and converters for the 
 owner property.

static java.lang.String
REASON\_PROPERTY
Use the property name to determine labels and converters for the 
 reason property.

static java.lang.String
TASKDISPLAYNAME\_PROPERTY
Use the property name to determine labels and converters for the 
 taskDisplayName property.

static java.lang.String
TASKNAME\_PROPERTY
Use the property name to determine labels and converters for the 
 taskName property.
    - Constructor Summary

Constructors 

Constructor and Description

WorkItemBean(QueryResultSet resultSet,
            HTMConnection htmConnection)
Constructs a new WorkItemBean from a QueryResultSet.

WorkItemBean(QueryResultSet resultSet,
            HTMConnection htmConnection,
            java.util.Locale locale)
Constructs a new WorkItemBean from a QueryResultSet.
    - Method Summary Methods Modifier and Type Method and Description static SimpleConverter getConverter (java.lang.String propertyName) Returns the default converter for a given property. java.util.Calendar getCreationTime () Returns the creationTime property. java.lang.String getGroupName () Returns the groupName property. com.ibm.bpe.api.WIID getID () Returns the ID property. static java.lang.String getLabel (java.lang.String propertyName) Returns the resource bundle key for a property static java.lang.String getLabel (java.lang.String propertyName, java.util.Locale locale) Returns the label for a property from the resource bundle. OID getObjectID () Returns the objectID property. int getObjectType () Returns the objectType property. java.lang.String getOwner () Returns the owner property. int getReason () Returns the reason property. com.ibm.bpc.clientcore.util.LocalisedString getTaskDisplayName () Returns the taskDisplayName property. java.lang.String getTaskDisplayName (java.util.Locale locale) Returns the taskDisplayName property. java.lang.String getTaskName () Returns the taskName property. TKTID getTaskTemplateID () Returns the property tktid . boolean isAssignedToEverybody () Returns the assignedToEverybody property. static boolean isValid (java.lang.String propertyName) Checks wehther the property is valid. void setAssignedToEverybody (boolean newAssignedToEverybody) Sets the assignedToEverybody property. void setCreationTime (java.util.Calendar newCreationTime) Sets the creationTime property. void setGroupName (java.lang.String newGroupName) Sets the groupName property. void setID (com.ibm.bpe.api.WIID newWorkitemID) Sets the ID property. void setLocalisedDisplayName (java.lang.String displayName, java.util.Locale locale) Sets the taskDisplayName property. void setObjectID (OID newObjectID) Sets the objectID property. void setObjectType (int newObjectType) Sets the objectType property. void setOwner (java.lang.String newOwner) Sets the owner property. void setReason (int newReason) Sets the reason property. java.lang.String toString () Returns all properties in a printable format

### Method Summary

| Modifier and Type                           | Method and Description                                                                                                                   |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| static SimpleConverter                      | getConverter(java.lang.String propertyName) Returns the default converter for a given property.                                          |
| java.util.Calendar                          | getCreationTime() Returns the creationTime property.                                                                                     |
| java.lang.String                            | getGroupName() Returns the groupName property.                                                                                           |
| com.ibm.bpe.api.WIID                        | getID() Returns the ID property.                                                                                                         |
| static java.lang.String                     | getLabel(java.lang.String propertyName) Returns the resource bundle key for a property                                                   |
| static java.lang.String                     | getLabel(java.lang.String propertyName,         java.util.Locale locale) Returns the label for a property from the resource bundle.      |
| OID                                         | getObjectID() Returns the objectID property.                                                                                             |
| int                                         | getObjectType() Returns the objectType property.                                                                                         |
| java.lang.String                            | getOwner() Returns the owner property.                                                                                                   |
| int                                         | getReason() Returns the reason property.                                                                                                 |
| com.ibm.bpc.clientcore.util.LocalisedString | getTaskDisplayName() Returns the taskDisplayName property.                                                                               |
| java.lang.String                            | getTaskDisplayName(java.util.Locale locale) Returns the taskDisplayName property.                                                        |
| java.lang.String                            | getTaskName() Returns the taskName property.                                                                                             |
| TKTID                                       | getTaskTemplateID() Returns the property tktid.                                                                                          |
| boolean                                     | isAssignedToEverybody() Returns the assignedToEverybody property.                                                                        |
| static boolean                              | isValid(java.lang.String propertyName) Checks wehther the property is valid.                                                             |
| void                                        | setAssignedToEverybody(boolean newAssignedToEverybody) Sets the assignedToEverybody property.                                            |
| void                                        | setCreationTime(java.util.Calendar newCreationTime) Sets the creationTime property.                                                      |
| void                                        | setGroupName(java.lang.String newGroupName) Sets the groupName property.                                                                 |
| void                                        | setID(com.ibm.bpe.api.WIID newWorkitemID) Sets the ID property.                                                                          |
| void                                        | setLocalisedDisplayName(java.lang.String displayName,                        java.util.Locale locale) Sets the taskDisplayName property. |
| void                                        | setObjectID(OID newObjectID) Sets the objectID property.                                                                                 |
| void                                        | setObjectType(int newObjectType) Sets the objectType property.                                                                           |
| void                                        | setOwner(java.lang.String newOwner) Sets the owner property.                                                                             |
| void                                        | setReason(int newReason) Sets the reason property.                                                                                       |
| java.lang.String                            | toString() Returns all properties in a printable format                                                                                  |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait