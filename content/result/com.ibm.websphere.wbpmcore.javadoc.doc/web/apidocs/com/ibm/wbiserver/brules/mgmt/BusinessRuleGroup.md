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

## Interface BusinessRuleGroup

- All Superinterfaces:
BusinessRuleChangeDetector, BusinessRuleValidateable, java.io.Serializable

public interface BusinessRuleGroup
extends BusinessRuleValidateable, BusinessRuleChangeDetector, java.io.Serializable
An object implementing this interface represents one business rule group component in the 
 server.  It is used as the starting point for accessing information related to all operations, 
 rule sets, and decision tables that are associated with the business rule group.
 
 A business rule group has a set of operations associated with it.  These operations can
 be retrieved using the 
 getOperations 
 method.  The Operation objects returned can be used to navigate to down to
 the rulesets and decision tables that implement the operations.
 
 A business rule group also has a set of properties associated with it.  A property is a 
 name-value pair that is intended to give additional information about the business rule
 group.  There are two types of properties: user-defined and system-defined.  User-defined
 properties are completely defined and under the control of the user.  They can be defined,
 their values can be changed, and they can be removed.  System-defined properties are defined
 by the system and cannot be changed by the user.  Properties can be used in queries to find
 business rule groups whose properties match certain criteria.  Refer to the classes in
 the com.ibm.wbiserver.brules.mgmt.query package for more information about
 queries.
   
 Methods are provided on the 
 BusinessRuleManager class to
 query for business rule groups based on the values assigned to the properties.  Once you
 have a business rule group you can get a list of its properties.  This list includes both
 system-defined and user-defined properties.  System-defined properties are read-only.  For
 user-defined properties, you are also allowed to change the values of existing 
 properties, remove existing properties, and add new properties.  No validation is performed
 on the changes for user-defined properties since the properties and their values are 
 completely defined by the user.
 
 Some data on the business rule group and its sub-objects is allowed to be changed.  Many 
 changes are validated at the time the set method is called, however some changes cannot be
 validated at that time.  Therefore a validate method is provided that can be 
 called to perform a complete validation after all changes are made.  The validate
 method will validate the object on which it is called and also all of its sub-objects.  
 Changes will also be validated at the time that they are published.
 
 The user should use one of the methods on the
 BusinessRuleManager class to
 get instances of the BusinessRuleGroup interface.  BusinessRuleManager
 provides various method to either get all BusinessRuleGroup objects accessible
 to the server or to query on various properties of the business rule groups.  
 
 For situations where a business rule group or sub-objects are of a newer version than what
 the runtime supports, a shell business rule group is instantiated. This situation occurs
 when the runtime configuration involves multiple servers in a single cell where the servers
 are of different runtime versions.  Because a server can only support a certain amount of
 features or level of the business rule language, those business rule groups or sub-objects 
 that use newer versions, will not be recognized by a management client and changes to these 
 artifacts may remove or corrupt the new items in the objects.  The shell business rule group limits what
 can be seen and changed in the newer business rule group version.  The shell business rule group
 will be limited to only the name and target namespace of the business rule group as well as two
 properties, IBMSystemVersion and IBMSystemShell.  The IBMSystemVersion property will list the
 version of the model that was used to create the business rule group.  If it is a sub-object 
 that is of a newer version, the version will be x.x.x signifing that it is a newer version that
 can not be determined as only the business rule group has a version recorded with the model.
 This property will not be part of the normal list of properties if the business rule group 
 is not a shell.  The existance of the IBMSystemShell property indicates the business rule group 
 is a shel and not a regular business rule group. 
 The isShell method can also be 
 used to check if the business rule group is a shell.  A shell business rule group is limited in 
 function and basically read only.  The getName, 
 getTargetNameSpace,  
 getProperties, 
 getProperty, and 
 getPropertyValue 
 methods are the only methods which are supported.  All other get and set methods will result in 
 a UnsupportedOperationException exception thrown.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getDescription () Get the description of the business rule group. java.lang.String getDisplayName () Get the display name for this business rule group. java.lang.String getName () Get the name of the business rule group. Operation getOperation (java.lang.String operationName) Get the operation with the specified name from the list of operations for this business rule group. java.util.List<Operation > getOperations () Get a list of all operations associated with this business rule group. PresentationTimezone getPresentationTimezone () Get the presentation time zone for the business rule group. PropertyList getProperties () Get the list of properties associated with this business rule group. Property getProperty (java.lang.String name) Get the property on this business rule group that has the specified name. java.lang.String getPropertyValue (java.lang.String name) Get the value of the property on this business rule group that has the specified name. java.lang.String getRuntimeID () Returns a globally unique ID for the business rule group. java.util.Date getSaveDate () Get the date and time that the information in this copy of the business rule group was saved to persistent storage. java.lang.String getTargetNameSpace () Get the target name space of the business rule group. boolean isDisplayNameSynchronizedToName () Check to see if the display name is synchronized to the name for this business rule group. boolean isGoverned () Returns a boolean that indicates whether the business rule group is under governance. boolean isShell () Retrieve flag indicating if a business rule group is a shell which is an indication that it is of a newer version than what is supported on the server on which it was retrieved. BusinessRuleGroup refresh () Retrieve this business rule group and its associated objects from persistent storage again. void setDescription (java.lang.String newDescription) Set the description associated with this business rule group. void setDisplayName (java.lang.String newDisplayName) Set the display name for this business rule group. void setDisplayNameIsSynchronizedToName (boolean newDisplayNameIsSynchronizedToName) Change the value of the flag that determines whether or not the display name is synchronized to the name for this business rule group. void setGovernance (boolean governanceEnabled) Set the governance value for the business rule group. void setPropertyValue (java.lang.String name, java.lang.String value) Set the value of the property with the specified name to the specified value.

### Method Summary

| Modifier and Type         | Method and Description                                                                                                                                                                                                 |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String          | getDescription() Get the description of the business rule group.                                                                                                                                                       |
| java.lang.String          | getDisplayName() Get the display name for this business rule group.                                                                                                                                                    |
| java.lang.String          | getName() Get the name of the business rule group.                                                                                                                                                                     |
| Operation                 | getOperation(java.lang.String operationName) Get the operation with the specified name from the list of operations for this  business rule group.                                                                      |
| java.util.List<Operation> | getOperations() Get a list of all operations associated with this business rule group.                                                                                                                                 |
| PresentationTimezone      | getPresentationTimezone() Get the presentation time zone for the business rule group.                                                                                                                                  |
| PropertyList              | getProperties() Get the list of properties associated with this business rule group.                                                                                                                                   |
| Property                  | getProperty(java.lang.String name) Get the property on this business rule group that has the specified name.                                                                                                           |
| java.lang.String          | getPropertyValue(java.lang.String name) Get the value of the property on this business rule group that has the specified name.                                                                                         |
| java.lang.String          | getRuntimeID() Returns a globally unique ID for the business rule group.                                                                                                                                               |
| java.util.Date            | getSaveDate() Get the date and time that the information in this copy of the business rule group  was saved to persistent storage.                                                                                     |
| java.lang.String          | getTargetNameSpace() Get the target name space of the business rule group.                                                                                                                                             |
| boolean                   | isDisplayNameSynchronizedToName() Check to see if the display name is synchronized to the name for this business rule  group.                                                                                          |
| boolean                   | isGoverned() Returns a boolean that indicates whether the business rule group is under  governance.                                                                                                                    |
| boolean                   | isShell() Retrieve flag indicating if a business rule group is a shell which is an indication that   it is of a newer version than what is supported on the server on which it was retrieved.                          |
| BusinessRuleGroup         | refresh() Retrieve this business rule group and its associated objects from persistent storage   again.                                                                                                                |
| void                      | setDescription(java.lang.String newDescription) Set the description associated with this business rule group.                                                                                                          |
| void                      | setDisplayName(java.lang.String newDisplayName) Set the display name for this business rule group.                                                                                                                     |
| void                      | setDisplayNameIsSynchronizedToName(boolean newDisplayNameIsSynchronizedToName) Change the value of the flag that determines whether or not the display name is  synchronized to the name for this business rule group. |
| void                      | setGovernance(boolean governanceEnabled) Set the governance value for the business rule group.                                                                                                                         |
| void                      | setPropertyValue(java.lang.String name,                 java.lang.String value) Set the value of the property with the specified name to the specified value.                                                          |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges