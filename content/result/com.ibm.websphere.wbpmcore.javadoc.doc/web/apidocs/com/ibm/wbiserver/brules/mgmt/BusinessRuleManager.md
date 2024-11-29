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

## Class BusinessRuleManager

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.BusinessRuleManager

- public class BusinessRuleManager
extends java.lang.Object
This class is the starting point for accessing information about business rules that are installed
 and available on the WPS server.  Methods are provided to either get all business rule groups
 available to this server (getBusinessRuleGroups) or to query for specific
 business rule groups by property values (methods starting with getBRGsBy).
 Each logical business rule group is represented by a BusinessRuleGroup object 
 in the returned List.  Each BusinessRuleGroup object can then be 
 used to navigate to the desired information.
 
 After a set of BusinessRuleGroup objects has been obtained, the client can
 use the methods on these objects and on any sub-objects accessible from the 
 BusinessRuleGroup objects to read and/or update data.  Many changes are
 validated at the time the relevant set method is called.  Some changes are not validated at
 that time.  These are cases where there are dependencies among
 multiple pieces of data that can't necessarily be validated until all changes are complete.
 An example of such a dependency is the default target and the set of date-specific targets on
 an operation.  An operation must have at least one target defined.  The target could be 
 either the default target or a date-specific target.  Now consider an operation that currently
 has a default target specified and no date-specified targets.  The user wants to change this
 so that there is no default target and there is one or more date-specfic targets.  If the
 default target is set to null first, a validation error should not be given because we
 don't know if a date-specific target is going to be added later.  A validate
 method is provided on the BusinessRuleGroup class to validate these kind of
 dependencies.
 
 For situations where a business rule group or sub-objects are of a newer version than what
 the runtime supports, a shell business rule group will be returned. This situation occurs
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
  
 As set methods are called the Java objects are updated but no changes are made to the 
 underlying persistent data that is actually used when an operation is invoked on a business 
 rule group.  To change the persistent data the publish method should be called 
 to publish the changes to persistent storage.  The publish method validates
 the specified business rules groups.  If no errors are detected, the business rule groups
 are published to persistent storage.  After the changes are published the changed data will 
 be used the next time an operation on a business rule group is called.  Any in-flight 
 operations will continue to use the old data.
 
 The business rule management API uses an optimistic locking scheme when retrieving data
 from persistent storage.  This means that two clients could be making changes to Java objects
 representing the same set of persistent data at the same time.  Neither client has any sort of
 lock on the persistent data.  In this case the first one to call publish wins.  
 The second call to publish will detect that the persistent data has been updated
 since the transient copies were obtained and the publish will fail.  In this case the second
 client must start over by retrieving the data again using getBusinessRuleGroups
 and making any changes to the newly-retrieved objects.
 
 Because of the read-only nature of a shell business rule group, if a shell business rule group
 is part of a list of business rule groups to published will be ignored as the other business 
 rule groups are validated and published.  
 
 All methods on this class are static.  There is no need to ever create an instance of
 this class.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static com.ibm.wbiservers.customization.audit.AuditRecorder
auditRecorder 

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description static java.util.List<BusinessRuleGroup > getBRGsByName (java.lang.String name, QueryOperator op, int numberToSkip, int maxToReturn) Get business rule groups using the name as a key. static java.util.List<BusinessRuleGroup > getBRGsByProperties (QueryNode queryTree, int numberToSkip, int maxToReturn) Get business rule groups that have property values that match the query specified in the given query tree. static java.util.List<BusinessRuleGroup > getBRGsBySingleProperty (java.lang.String propertyName, QueryOperator op, java.lang.String propertyValue, int numberToSkip, int maxToReturn) Get business rule groups that have a property matching the specified parameters. static java.util.List<BusinessRuleGroup > getBRGsByTNS (java.lang.String tns, QueryOperator op, int numberToSkip, int maxToReturn) Get business rule groups using the target name space as a key. static java.util.List<BusinessRuleGroup > getBRGsByTNSAndName (java.lang.String tns, QueryOperator tnsOp, java.lang.String name, QueryOperator nameOp, int numberToSkip, int maxToReturn) Get business rule groups using the target name space and name as a key. static java.util.List<BusinessRuleGroup > getBusinessRuleGroups (int numberToSkip, int maxToReturn) Get all business rule groups that are installed and available to the WPS server in which this code is being run. protected static com.ibm.wsspi.uow.UOWManager getUOWManager () static void publish (java.util.List<BusinessRuleGroup > updatedBusinessRuleGroups, boolean publishOnlyChangedArtifacts) Publish the changes in the specified BusinessRuleGroup objects to persistent storage.

### Method Summary

| Modifier and Type                             | Method and Description                                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static java.util.List<BusinessRuleGroup>      | getBRGsByName(java.lang.String name,              QueryOperator op,              int numberToSkip,              int maxToReturn) Get business rule groups using the name as a key.                                                                                                                                       |
| static java.util.List<BusinessRuleGroup>      | getBRGsByProperties(QueryNode queryTree,                    int numberToSkip,                    int maxToReturn) Get business rule groups that have property values that match the query specified  in the given query tree.                                                                                            |
| static java.util.List<BusinessRuleGroup>      | getBRGsBySingleProperty(java.lang.String propertyName,                        QueryOperator op,                        java.lang.String propertyValue,                        int numberToSkip,                        int maxToReturn) Get business rule groups that have a property matching the specified parameters. |
| static java.util.List<BusinessRuleGroup>      | getBRGsByTNS(java.lang.String tns,             QueryOperator op,             int numberToSkip,             int maxToReturn) Get business rule groups using the target name space as a key.                                                                                                                               |
| static java.util.List<BusinessRuleGroup>      | getBRGsByTNSAndName(java.lang.String tns,                    QueryOperator tnsOp,                    java.lang.String name,                    QueryOperator nameOp,                    int numberToSkip,                    int maxToReturn) Get business rule groups using the target name space and name as a key.    |
| static java.util.List<BusinessRuleGroup>      | getBusinessRuleGroups(int numberToSkip,                      int maxToReturn) Get all business rule groups that are installed and available to the WPS  server in which this code is being run.                                                                                                                          |
| protected static com.ibm.wsspi.uow.UOWManager | getUOWManager()                                                                                                                                                                                                                                                                                                          |
| static void                                   | publish(java.util.List<BusinessRuleGroup> updatedBusinessRuleGroups,        boolean publishOnlyChangedArtifacts) Publish the changes in the specified BusinessRuleGroup objects to persistent  storage.                                                                                                                  |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait