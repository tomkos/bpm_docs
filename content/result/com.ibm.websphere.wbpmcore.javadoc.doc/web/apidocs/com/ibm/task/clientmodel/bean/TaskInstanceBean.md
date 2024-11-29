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

## Class TaskInstanceBean

- java.lang.Object
    - com.ibm.task.clientmodel.bean.TaskInstanceBean

- All Implemented Interfaces: Task , java.io.Serializable public class TaskInstanceBean extends java.lang.Objectimplements Task Accesses the properties of the original Task object and adds metadata for national language support and converters. A task instance represents a piece of work. It contains all data necessary to perform the task. For example, a task that is associated with a group of potential owners allows a person that belongs to the group to claim the task, work on the task, and to complete the task. A TaskInstanceBean object can be instantiated from a QueryResultSet object or from a Task object. If the bean was instantiated from an original object returned by the Human Task Manager API, all properties are loaded. If the bean is instantiated from a query, the following properties are loaded from the query result set: If the property is not found in the query result set, the property remains empty. Accessing an empty property requires the bean to load the missing information from the server. Use the static method getLabel(String, Locale) to retrieve the localized label for a property. Use the static method getConverter(String) to retrieve a converter for a property. The return value might be null, as converters are optional. See Also: Task , QueryResultSet , Serialized Form

```
public class TaskInstanceBean
extends java.lang.Object
implements Task
```

Accesses the properties of the original Task object and adds metadata
 for national language support and converters.

A task instance represents a piece of work. It contains all data necessary to
 perform the task. For example, a task that is associated with a group of
 potential owners allows a person that belongs to the group to claim the task,
 work on the task, and to complete the task.

A TaskInstanceBean object can be instantiated from a
 QueryResultSet object or from a Task object. 

 If the bean was instantiated from an original object returned by the Human
 Task Manager API, all properties are loaded. If the bean is instantiated from
 a query, the following properties are loaded from the query result set:
 
ID
activationTime
applicationDefaultsID
applicationName
workBasketName
assignmentType
invokedInstanceType
autoDeletionMode
businessRelevant
completionTime
containmentContextID
contextAuthorizationOfOwner
dueTime
deletionTime
escalatedUpdateable
expirationTime
firstActivationTime
followOnTaskID
positionInHierarchy
adHoc
escalated
child
read
inheritedAuthorization
inline
waitingForSubTask
kind
lastModificationTime
lastStateChangeTime
name
namespace
definitionName
definitionNamespace
originator
owner
parentContextID
invokedInstanceID
priority
startTime
starter
state
substitutionPolicy
supportsAutomaticClaim
supportsClaimIfSuspended
supportsDelegation
supportsSubTasks
supportsFollowOnTasks
suspended
taskTemplateID
topLevelTaskID
type
taskTemplateName

 If the property is not found in the query result set, the property remains
 empty. Accessing an empty property requires the bean to load the missing
 information from the server.

Use the static method getLabel(String, Locale) to
 retrieve the localized label for a property. Use the static method
 getConverter(String) to retrieve a converter for a
 property. The return value might be null, as converters are optional.

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String ACTIVATIONTIME\_PROPERTY Use the property name to determine labels and converters for the activationTime property. static java.lang.String ADHOC\_PROPERTY Use the property name to determine labels and converters for the property adHoc. static java.lang.String APPLICATIONNAME\_PROPERTY Use the property name to determine labels and converters for the applicationName property. static java.lang.String ASSIGNMENTTYPE\_PROPERTY Use the property name to determine labels and converters for the assignmentType property. static java.lang.String AUTODELETIONMODE\_PROPERTY Use the property name to determine labels and converters for the autoDeletionMode property. static java.lang.String BUSINESSRELEVANT\_PROPERTY Use the property name to determine labels and converters for the businessRelevant property. static java.lang.String CHILD\_PROPERTY Use the property name to determine labels and converters for the child property. static java.lang.String COMPLETIONTIME\_PROPERTY Use the property name to determine labels and converters for the completionTime property. static java.lang.String CONTAINMENTCONTEXTID\_PROPERTY Use the property name to determine labels and converters for the containmentContextID property. static java.lang.String COPYRIGHT (C) Copyright IBM Corporation 2004, 2012. static java.lang.String CUSTOMPROPERTY\_PROPERTY Use the property name to determine labels and converters for the customProperty property. static java.lang.String CUSTOMTEXT1\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT2\_PROPERTY Use the property name to determine labels and converters for the customText2 property. static java.lang.String CUSTOMTEXT3\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT4\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT5\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT6\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT7\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT8\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String DELETIONTIME\_PROPERTY Use the property name to determine labels and converters for the deletionTime property. static java.lang.String DESCRIPTION\_PROPERTY Use the property name to determine labels and converters for the description property. static java.lang.String DISPLAYNAME\_PROPERTY Use the property name to determine labels and converters for the displayName property. static java.lang.String DUETIME\_PROPERTY Use the property name to determine labels and converters for the property dueTime. static java.lang.String DURATIONUNTILDUE\_PROPERTY Use the property name to determine converter for the durationUntilDue property. static java.lang.String DURATIONUNTILEXPIRES\_PROPERTY Use the property name to determine converter for the durationUntilExpires property. static java.lang.String ESCALATED\_PROPERTY Use the property name to determine labels and converters for the escalated property. static java.lang.String ESCALATEDUPDATEABLE\_PROPERTY Use the property name to determine labels and converters for the escalatedUpdateable property. static java.lang.String EXPIRATIONTIME\_PROPERTY Use the property name to determine labels and converters for the expirationTime property. static java.lang.String FIRSTACTIVATIONTIME\_PROPERTY Use the property name to determine labels and converters for the firstActivationTime property. static java.lang.String ID\_PROPERTY Use the property name to determine labels and converters for the ID property. static java.lang.String INHERITEDAUTHORIZATION\_PROPERTY Use the property name to determine labels and converters for the inheritedAuthorization property. static java.lang.String INLINE\_PROPERTY Use the property name to determine labels and converters for the property inline. static java.lang.String INPUTMESSAGETYPENAME\_PROPERTY Use the property name to determine labels and converters for the inputMessageTypeName property. static java.lang.String INVOKEDINSTANCEID\_PROPERTY Use the property name to determine labels and converters for the invokedInstanceID property. static java.lang.String INVOKEDINSTANCETYPE\_PROPERTY Use the property name to determine labels and converters for the invokedInstanceType property. static java.lang.String KIND\_PROPERTY Use the property name to determine labels and converters for the kind property. static java.lang.String LASTMODIFICATIONTIME\_PROPERTY Use the property name to determine labels and converters for the lastModificationTime property. static java.lang.String LASTSTATECHANGETIME\_PROPERTY Use the property name to determine labels and converters for the lastStateChangeTime property. static java.lang.String NAME\_PROPERTY Use the property name to determine labels and converters for the name property. static java.lang.String NAMESPACE\_PROPERTY Use the property name to determine labels and converters for the property namespace. static java.lang.String ORIGINATOR\_PROPERTY Use the property name to determine labels and converters for the originator property. static java.lang.String OUTPUTMESSAGETYPENAME\_PROPERTY Use the property name to determine labels and converters for the outputMessageTypeName property. static java.lang.String OWNER\_PROPERTY Use the property name to determine labels and converters for the owner property. static java.lang.String PARENTCONTEXTID\_PROPERTY Use the property name to determine labels and converters for the parentContextID property. static java.lang.String POSITIONINHIERARCHY\_PROPERTY Use the property name to determine labels and converters for the property positionInHierarchy. static java.lang.String PRIORITY\_PROPERTY Use the property name to determine labels and converters for the priority property. static java.lang.String PROCESSAPPACRONYM\_PROPERTY Use the property name to determine labels and converters for the processAppAcronym property. static java.lang.String PROCESSAPPNAME\_PROPERTY Use the property name to determine labels and converters for the processAppName property. static java.lang.String READ\_PROPERTY Use the property name to determine labels and converters for the read property. static java.lang.String RESUMPTIONTIME\_PROPERTY Use the property name to determine labels and converters for the property resumptionTime. static java.lang.String SNAPSHOTID\_PROPERTY Use the property name to determine labels and converters for the snapshotID property. static java.lang.String SNAPSHOTNAME\_PROPERTY Use the property name to determine labels and converters for the snapshotName property. static java.lang.String STARTER\_PROPERTY Use the property name to determine labels and converters for the property starter. static java.lang.String STARTTIME\_PROPERTY Use the property name to determine labels and converters for the startTime property. static java.lang.String STATE\_PROPERTY Use the property name to determine labels and converters for the state property. static java.lang.String SUBSTITUTIONPOLICY\_PROPERTY Use the property name to determine labels and converters for the substitutionPolicy property. static java.lang.String SUPPORTSAUTOMATICCLAIM\_PROPERTY Use the property name to determine labels and converters for the property automaticClaim. static java.lang.String SUPPORTSCLAIMIFSUSPENDED\_PROPERTY Use the property name to determine labels and converters for the property supportsClaimIfSuspended. static java.lang.String SUPPORTSDELEGATION\_PROPERTY Use the property name to determine labels and converters for the property supportsDelegation. static java.lang.String SUPPORTSFOLLOWONTASKS\_PROPERTY Use the property name to determine labels and converters for the property supportsFollowOnTasks. static java.lang.String SUPPORTSSUBTASKS\_PROPERTY Use the property name to determine labels and converters for the property supportsSubTasks. static java.lang.String SUSPENDED\_PROPERTY Use the property name to determine labels and converters for the property suspended. static java.lang.String TASKTEMPLATEDISPLAYNAME\_PROPERTY Use the property name to determine labels and converters for the property task template display name. static java.lang.String TASKTEMPLATEID\_PROPERTY Use the property name to determine labels and converters for thetaskTemplateID property static java.lang.String TASKTEMPLATENAME\_PROPERTY Use the property name to determine labels and converters for the property task template name. static java.lang.String TIP\_PROPERTY Use the property name to determine labels and converters for the tip property. static java.lang.String TOOLKITACRONYM\_PROPERTY Use the property name to determine labels and converters for the toolkitAcronym property. static java.lang.String TOOLKITNAME\_PROPERTY Use the property name to determine labels and converters for the toolkitName property. static java.lang.String TOOLKITSNAPSHOTID\_PROPERTY Use the property name to determine labels and converters for the toolkitSnapshotID property. static java.lang.String TOOLKITSNAPSHOTNAME\_PROPERTY Use the property name to determine labels and converters for the toolkitSnapshotName property. static java.lang.String TOPLEVELTOOLKITACRONYM\_PROPERTY Use the property name to determine labels and converters for the topLevelToolkitAcronym property. static java.lang.String TOPLEVELTOOLKITNAME\_PROPERTY Use the property name to determine labels and converters for the topLevelToolkitName property. static java.lang.String TRACKNAME\_PROPERTY Use the property name to determine labels and converters for the trackName property. static java.lang.String TYPE\_PROPERTY Use the property name to determine labels and converters for type. static java.lang.String VALIDFROMTIME\_PROPERTY Use the property name to determine labels and converters for thevalidFromTime property static java.lang.String WAITINGFORSUBTASK\_PROPERTY Use the property name to determine labels and converters for the property waitingForSubTask. static java.lang.String WORKBASKETNAME\_PROPERTY Use the property name to determine labels and converters for the workBasketName property.

### Field Summary

| Modifier and Type       | Field and Description                                                                                                                   |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| static java.lang.String | ACTIVATIONTIME\_PROPERTY Use the property name to determine labels and converters for the  activationTime property.                      |
| static java.lang.String | ADHOC\_PROPERTY Use the property name to determine labels and converters for the property  adHoc.                                        |
| static java.lang.String | APPLICATIONNAME\_PROPERTY Use the property name to determine labels and converters for the  applicationName property.                    |
| static java.lang.String | ASSIGNMENTTYPE\_PROPERTY Use the property name to determine labels and converters for the  assignmentType property.                      |
| static java.lang.String | AUTODELETIONMODE\_PROPERTY Use the property name to determine labels and converters for the  autoDeletionMode property.                  |
| static java.lang.String | BUSINESSRELEVANT\_PROPERTY Use the property name to determine labels and converters for the  businessRelevant property.                  |
| static java.lang.String | CHILD\_PROPERTY Use the property name to determine labels and converters for the  child property.                                        |
| static java.lang.String | COMPLETIONTIME\_PROPERTY Use the property name to determine labels and converters for the  completionTime property.                      |
| static java.lang.String | CONTAINMENTCONTEXTID\_PROPERTY Use the property name to determine labels and converters for the  containmentContextID property.          |
| static java.lang.String | COPYRIGHT (C) Copyright IBM Corporation 2004, 2012.                                                                                     |
| static java.lang.String | CUSTOMPROPERTY\_PROPERTY Use the property name to determine labels and converters for the  customProperty property.                      |
| static java.lang.String | CUSTOMTEXT1\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                             |
| static java.lang.String | CUSTOMTEXT2\_PROPERTY Use the property name to determine labels and converters for the customText2 property.                             |
| static java.lang.String | CUSTOMTEXT3\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                             |
| static java.lang.String | CUSTOMTEXT4\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                             |
| static java.lang.String | CUSTOMTEXT5\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                             |
| static java.lang.String | CUSTOMTEXT6\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                             |
| static java.lang.String | CUSTOMTEXT7\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                             |
| static java.lang.String | CUSTOMTEXT8\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                             |
| static java.lang.String | DELETIONTIME\_PROPERTY Use the property name to determine labels and converters for the  deletionTime property.                          |
| static java.lang.String | DESCRIPTION\_PROPERTY Use the property name to determine labels and converters for the  description property.                            |
| static java.lang.String | DISPLAYNAME\_PROPERTY Use the property name to determine labels and converters for the  displayName property.                            |
| static java.lang.String | DUETIME\_PROPERTY Use the property name to determine labels and converters for the property  dueTime.                                    |
| static java.lang.String | DURATIONUNTILDUE\_PROPERTY Use the property name to determine converter for the durationUntilDue  property.                              |
| static java.lang.String | DURATIONUNTILEXPIRES\_PROPERTY Use the property name to determine converter for the durationUntilExpires  property.                      |
| static java.lang.String | ESCALATED\_PROPERTY Use the property name to determine labels and converters for the  escalated property.                                |
| static java.lang.String | ESCALATEDUPDATEABLE\_PROPERTY Use the property name to determine labels and converters for the  escalatedUpdateable property.            |
| static java.lang.String | EXPIRATIONTIME\_PROPERTY Use the property name to determine labels and converters for the  expirationTime property.                      |
| static java.lang.String | FIRSTACTIVATIONTIME\_PROPERTY Use the property name to determine labels and converters for the  firstActivationTime property.            |
| static java.lang.String | ID\_PROPERTY Use the property name to determine labels and converters for the  ID property.                                              |
| static java.lang.String | INHERITEDAUTHORIZATION\_PROPERTY Use the property name to determine labels and converters for the  inheritedAuthorization property.      |
| static java.lang.String | INLINE\_PROPERTY Use the property name to determine labels and converters for the property  inline.                                      |
| static java.lang.String | INPUTMESSAGETYPENAME\_PROPERTY Use the property name to determine labels and converters for the  inputMessageTypeName property.          |
| static java.lang.String | INVOKEDINSTANCEID\_PROPERTY Use the property name to determine labels and converters for the  invokedInstanceID property.                |
| static java.lang.String | INVOKEDINSTANCETYPE\_PROPERTY Use the property name to determine labels and converters for the  invokedInstanceType property.            |
| static java.lang.String | KIND\_PROPERTY Use the property name to determine labels and converters for the  kind property.                                          |
| static java.lang.String | LASTMODIFICATIONTIME\_PROPERTY Use the property name to determine labels and converters for the  lastModificationTime property.          |
| static java.lang.String | LASTSTATECHANGETIME\_PROPERTY Use the property name to determine labels and converters for the  lastStateChangeTime property.            |
| static java.lang.String | NAME\_PROPERTY Use the property name to determine labels and converters for the  name property.                                          |
| static java.lang.String | NAMESPACE\_PROPERTY Use the property name to determine labels and converters for the property  namespace.                                |
| static java.lang.String | ORIGINATOR\_PROPERTY Use the property name to determine labels and converters for the  originator property.                              |
| static java.lang.String | OUTPUTMESSAGETYPENAME\_PROPERTY Use the property name to determine labels and converters for the  outputMessageTypeName property.        |
| static java.lang.String | OWNER\_PROPERTY Use the property name to determine labels and converters for the  owner property.                                        |
| static java.lang.String | PARENTCONTEXTID\_PROPERTY Use the property name to determine labels and converters for the  parentContextID property.                    |
| static java.lang.String | POSITIONINHIERARCHY\_PROPERTY Use the property name to determine labels and converters for the property  positionInHierarchy.            |
| static java.lang.String | PRIORITY\_PROPERTY Use the property name to determine labels and converters for the  priority property.                                  |
| static java.lang.String | PROCESSAPPACRONYM\_PROPERTY Use the property name to determine labels and converters for the processAppAcronym property.                 |
| static java.lang.String | PROCESSAPPNAME\_PROPERTY Use the property name to determine labels and converters for the processAppName property.                       |
| static java.lang.String | READ\_PROPERTY Use the property name to determine labels and converters for the  read property.                                          |
| static java.lang.String | RESUMPTIONTIME\_PROPERTY Use the property name to determine labels and converters for the property  resumptionTime.                      |
| static java.lang.String | SNAPSHOTID\_PROPERTY Use the property name to determine labels and converters for the snapshotID property.                               |
| static java.lang.String | SNAPSHOTNAME\_PROPERTY Use the property name to determine labels and converters for the snapshotName property.                           |
| static java.lang.String | STARTER\_PROPERTY Use the property name to determine labels and converters for the property  starter.                                    |
| static java.lang.String | STARTTIME\_PROPERTY Use the property name to determine labels and converters for the  startTime property.                                |
| static java.lang.String | STATE\_PROPERTY Use the property name to determine labels and converters for the  state property.                                        |
| static java.lang.String | SUBSTITUTIONPOLICY\_PROPERTY Use the property name to determine labels and converters for the  substitutionPolicy property.              |
| static java.lang.String | SUPPORTSAUTOMATICCLAIM\_PROPERTY Use the property name to determine labels and converters for the property  automaticClaim.              |
| static java.lang.String | SUPPORTSCLAIMIFSUSPENDED\_PROPERTY Use the property name to determine labels and converters for the property  supportsClaimIfSuspended.  |
| static java.lang.String | SUPPORTSDELEGATION\_PROPERTY Use the property name to determine labels and converters for the property  supportsDelegation.              |
| static java.lang.String | SUPPORTSFOLLOWONTASKS\_PROPERTY Use the property name to determine labels and converters for the property  supportsFollowOnTasks.        |
| static java.lang.String | SUPPORTSSUBTASKS\_PROPERTY Use the property name to determine labels and converters for the property  supportsSubTasks.                  |
| static java.lang.String | SUSPENDED\_PROPERTY Use the property name to determine labels and converters for the property  suspended.                                |
| static java.lang.String | TASKTEMPLATEDISPLAYNAME\_PROPERTY Use the property name to determine labels and converters for the property  task template display name. |
| static java.lang.String | TASKTEMPLATEID\_PROPERTY Use the property name to determine labels and converters for thetaskTemplateID property                         |
| static java.lang.String | TASKTEMPLATENAME\_PROPERTY Use the property name to determine labels and converters for the property  task template name.                |
| static java.lang.String | TIP\_PROPERTY Use the property name to determine labels and converters for the tip property.                                             |
| static java.lang.String | TOOLKITACRONYM\_PROPERTY Use the property name to determine labels and converters for the toolkitAcronym property.                       |
| static java.lang.String | TOOLKITNAME\_PROPERTY Use the property name to determine labels and converters for the toolkitName property.                             |
| static java.lang.String | TOOLKITSNAPSHOTID\_PROPERTY Use the property name to determine labels and converters for the toolkitSnapshotID property.                 |
| static java.lang.String | TOOLKITSNAPSHOTNAME\_PROPERTY Use the property name to determine labels and converters for the toolkitSnapshotName property.             |
| static java.lang.String | TOPLEVELTOOLKITACRONYM\_PROPERTY Use the property name to determine labels and converters for the topLevelToolkitAcronym property.       |
| static java.lang.String | TOPLEVELTOOLKITNAME\_PROPERTY Use the property name to determine labels and converters for the topLevelToolkitName property.             |
| static java.lang.String | TRACKNAME\_PROPERTY Use the property name to determine labels and converters for the trackName property.                                 |
| static java.lang.String | TYPE\_PROPERTY Use the property name to determine labels and converters for type.                                                        |
| static java.lang.String | VALIDFROMTIME\_PROPERTY Use the property name to determine labels and converters for thevalidFromTime property                           |
| static java.lang.String | WAITINGFORSUBTASK\_PROPERTY Use the property name to determine labels and converters for the property  waitingForSubTask.                |
| static java.lang.String | WORKBASKETNAME\_PROPERTY Use the property name to determine labels and converters for the  workBasketName property.                      |

- Fields inherited from interface com.ibm.task.api.Task
ASSIGNMENT\_TYPE\_PARALLEL, ASSIGNMENT\_TYPE\_SINGLE, AUTH\_NONE, AUTH\_READER, AUTO\_DELETE\_ON\_COMPLETION, AUTO\_DELETE\_ON\_SUCCESSFUL\_COMPLETION, HIERARCHY\_POSITION\_FOLLOW\_ON\_TASK, HIERARCHY\_POSITION\_SUB\_TASK, HIERARCHY\_POSITION\_TOP\_TASK, INHERITED\_AUTH\_ADMINISTRATOR, INHERITED\_AUTH\_ALL, INHERITED\_AUTH\_NONE, INVOKED\_INSTANCE\_TYPE\_ACTIVITY, INVOKED\_INSTANCE\_TYPE\_CHILD\_PROCESS, INVOKED\_INSTANCE\_TYPE\_CHILD\_TASK, INVOKED\_INSTANCE\_TYPE\_EVENT, INVOKED\_INSTANCE\_TYPE\_INLINE\_TASK, INVOKED\_INSTANCE\_TYPE\_NOT\_SET, INVOKED\_INSTANCE\_TYPE\_PROCESS, INVOKED\_INSTANCE\_TYPE\_TASK, KIND\_ADMINISTRATIVE, KIND\_HUMAN, KIND\_ORIGINATING, KIND\_PARTICIPATING, KIND\_WPC\_STAFF\_ACTIVITY, STATE\_CLAIMED, STATE\_EXPIRED, STATE\_FAILED, STATE\_FAILING, STATE\_FINISHED, STATE\_FORWARDED, STATE\_INACTIVE, STATE\_PROCESSING\_UNDO, STATE\_READY, STATE\_RUNNING, STATE\_SKIPPED, STATE\_STOPPED, STATE\_TERMINATED, STATE\_TERMINATING, STATE\_WAITING, SUBSTITUTION\_POLICY\_NO\_SUBSTITUTION, SUBSTITUTION\_POLICY\_SELECT\_USER\_IF\_PRESENT, SUBSTITUTION\_POLICY\_SUBSTITUTE\_IF\_ABSENT

- Constructor Summary

Constructors 

Modifier
Constructor and Description

 
TaskInstanceBean(QueryResultSet resultSet,
                HTMConnection htmConnection)
Constructs a new TaskInstanceBean from a
 QueryResultSet.

 
TaskInstanceBean(QueryResultSet resultSet,
                HTMConnection htmConnection,
                java.util.Locale locale)
Constructs a new TaskInstanceBean from a
 QueryResultSet.

 
TaskInstanceBean(QueryResultSet resultSet,
                java.lang.String taskDataViewName,
                HTMConnection htmConnection)
Constructs a new TaskInstanceBean from a
 QueryResultSet.

 
TaskInstanceBean(QueryResultSet resultSet,
                java.lang.String taskDataViewName,
                HTMConnection htmConnection,
                java.util.Locale locale)
Constructs a new TaskInstanceBean from a
 QueryResultSet.

 
TaskInstanceBean(Task task,
                HTMConnection htmConnection)
Constructs a TaskInstanceBean from an original Task
 object.

protected 
TaskInstanceBean(TKIID id,
                HTMConnection htmConnection,
                java.util.Locale locale)
Constructs a TaskInstanceBean from a task instance id.

- Method Summary Methods Modifier and Type Method and Description MessageWrapper createOutputMessageWrapper () Creates an initial empty output message. java.util.Calendar getActivationTime () Returns the property activationTime . ACOID getApplicationDefaultsID () Returns the property applicationDefaultsID . java.lang.String getApplicationName () Returns the name of the application the task is part of. int getAssignmentType () Returns the property assignmentType . int getAutoDeletionMode () Returns the property autoDeletionMode . java.lang.String getCalendarName () Returns the property calendarName . java.util.Calendar getCompletionTime () Returns the property completionTime . OID getContainmentContextID () Returns the property containmentContextID . int getContextAuthorizationOfOwner () Returns the property contextAuthorizationOfOwner . static SimpleConverter getConverter (java.lang.String propertyName) Returns the default converter for a given property. java.lang.String getCustomText1 () Returns the property customText1 . java.lang.String getCustomText2 () Returns the property customText2 . java.lang.String getCustomText3 () Returns the property customText3 . java.lang.String getCustomText4 () Returns the property customText4 . java.lang.String getCustomText5 () Returns the property customText5 . java.lang.String getCustomText6 () Returns the property customText6 . java.lang.String getCustomText7 () Returns the property customText7 . java.lang.String getCustomText8 () Returns the property customText8 . java.lang.String getDefinitionName () Returns the property definition name . java.lang.String getDefinitionNamespace () Returns the property definition namespace . java.util.Calendar getDeletionTime () Returns the property deletionTime . com.ibm.bpc.clientcore.util.LocalisedString getDescription () Returns the localised description. java.lang.String getDescription (java.util.Locale locale) Returns the property description . com.ibm.bpc.clientcore.util.LocalisedString getDisplayName () Returns the localised display name. java.lang.String getDisplayName (java.util.Locale locale) Returns the property displayName . java.util.Calendar getDueTime () Returns the property dueTime . java.lang.String getDurationUntilDeleted () Returns the property durationUntilDeleted . java.lang.String getDurationUntilDue () Returns the property durationUntilDue . java.lang.String getDurationUntilExpires () Returns the property durationUntilExpires . java.lang.String getEventHandlerName () Returns the property eventHandlerName . java.util.Calendar getExpirationTime () Returns the property expirationTime . MessageWrapper getFaultMessageWrapper () Retrieves the fault message. java.util.Calendar getFirstActivationTime () Returns the property firstActivationTime . TKIID getFollowOnTaskID () Returns the property followOnTaskID . protected HTMConnection getHTMConnection () TKIID getID () Returns the property ID . int getInheritedAuthorization () Returns the property inheritedAuthorization . java.lang.String getInputMessageTypeName () Returns the property inputMessageTypeName . MessageWrapper getInputMessageWrapper () Retrieves the input message. OID getInvokedInstanceID () Returns the property invokedInstanceID . int getInvokedInstanceType () Returns the property invokedInstanceType . java.lang.String getJNDINameOfCalendar () Returns the property JNDINameOfCalendar . java.lang.String getJNDINameOfStaffPluginProvider () Returns the property JNDINameOfStaffPluginProvider . int getKind () Returns the property kind . static java.lang.String getLabel (java.lang.String propertyName) Returns the resource bundle key for a property static java.lang.String getLabel (java.lang.String propertyName, java.util.Locale locale) Returns the label for a property from the resource bundle. java.util.Calendar getLastModificationTime () Returns the property lastModificationTime . java.util.Calendar getLastStateChangeTime () Returns the property lastStateChangeTime . java.util.List getLocalesOfDescriptions () Returns the property localesOfDescriptions . java.util.List getLocalesOfDisplayNames () Returns the property localesOfDisplayNames . java.lang.String getName () Returns the property name . java.lang.String getNamespace () Returns the property namespace . protected Task getOriginal () java.lang.String getOriginator () Returns the property originator . java.lang.String getOutputMessageTypeName () Returns the property outputMessageTypeName . MessageWrapper getOutputMessageWrapper () Retrieves the output message. java.lang.String getOwner () Returns the property owner . OID getParentContextID () Returns the property parentContextID . int getPositionInHierarchy () Returns the property positionInHierarchy . java.lang.Integer getPriority () Returns the property priority . java.lang.String getProcessAppAcronym () Returns the processAppAcronym property. java.lang.String getProcessAppName () Returns the processAppName property. java.util.Calendar getResumptionTime () Returns the property resumptionTime . java.lang.String getSnapshotID () Returns the snapshotID property. java.lang.String getSnapshotName () Returns the snapshotName property. java.lang.String getStarter () Returns the property starter . java.util.Calendar getStartTime () Returns the property startTime . int getState () Returns the property state . int getSubstitutionPolicy () Returns the property substitutionPolicy . TKTID getTaskTemplateID () Returns the property taskTemplateID . java.lang.String getTaskTemplateName () Returns the property taskTemplateName . java.lang.String getToolkitAcronym () Returns the toolkitAcronym property. java.lang.String getToolkitName () Returns the toolkitName property. java.lang.String getToolkitSnapshotID () Returns the toolkitSnapshotID property. java.lang.String getToolkitSnapshotName () Returns the toolkitSnapshotName property. TKIID getTopLevelTaskID () Returns the property topLevelTaskID . java.lang.String getTopLevelToolkitAcronym () Returns the topLevelToolkitAcronym property. java.lang.String getTopLevelToolkitName () Returns the topLevelToolkitName property. java.lang.String getTrackName () Returns the trackName property. java.lang.String getType () Returns the property type . java.util.Calendar getValidFromTime () Returns the validFromTime property. java.lang.String getWorkBasketName () Returns the property workBasketName . boolean isAdHoc () Returns the property adHoc . boolean isBusinessRelevanceUpdateable () Signals whether the business relevance property can be changed for the kind and current state of the object. boolean isBusinessRelevant () Returns the property businessRelevant . boolean isChild () Returns the property isChild . boolean isContextAuthorizationOfOwnerUpdateable () Signals whether the context authorization property can be changed for the kind and current state of the object. boolean isDeletionTimeUpdateable () Signals whether the deletion time property can be changed for the kind and current state of the object. boolean isDescriptionUpdateable () Signals whether the description property can be changed for the kind and current state of the object. boolean isDisplayNameUpdateable () Signals whether the display name property can be changed for the kind and current state of the object. boolean isDueTimeUpdateable () Signals whether the due time property can be changed for the kind and current state of the object. boolean isDurationUntilDeletedUpdateable () Signals whether the duration until deleted property can be changed for the kind and current state of the object. boolean isDurationUntilDueUpdateable () Signals whether the duration until due property can be changed for the kind and current state of the object. boolean isDurationUntilExpiresUpdateable () Signals whether the duration until expires property can be changed for the kind and current state of the object. boolean isEscalated () Returns the property escalated . boolean isEscalatedUpdateable () Returns the property escalatedUpdateable() . boolean isEventHandlerNameUpdateable () Signals whether the event handler name property can be changed for the kind and current state of the object. boolean isExpirationTimeUpdateable () Signals whether the expiration time property can be changed for the kind and current state of the object. boolean isInline () Returns the property inline . boolean isNamespaceUpdateable () Signals whether the namespace property can be changed for the kind and current state of the object. boolean isNameUpdateable () Signals whether the name property can be changed for the kind and current state of the object. boolean isParentContextIDUpdateable () Signals whether the parent context i d property can be changed for the kind and current state of the object. boolean isPriorityUpdateable () Signals whether the priority property can be changed for the kind and current state of the object. boolean isRead () Returns the property isRead . boolean isReadUpdateable () Returns the property readUpdateable() . boolean isSupportsAutomaticClaim () Returns the property supportsAutomaticClaim . boolean isSupportsClaimIfSuspended () Returns the property supportsClaimIfSuspended . boolean isSupportsClaimIfSuspendedUpdateable () Signals whether the supports claim suspended property can be changed for the kind and current state of the object. boolean isSupportsDelegation () Returns the property supportsDelegation . boolean isSupportsDelegationUpdateable () Signals whether the supports delegation property can be changed for the kind and current state of the object. boolean isSupportsFollowOnTasks () Returns the property supportsFollowOnTasks . boolean isSupportsFollowOnTasksUpdateable () Signals whether the supports follow on task property can be changed for the kind and current state of the object. boolean isSupportsSubTasks () Returns the property supportsSubTasks . boolean isSupportsSubTasksUpdateable () Signals whether the supports sub task property can be changed for the kind and current state of the object. boolean isSuspended () Returns the property suspended . boolean isTip () Returns the tip property. boolean isTransferredToWorkBasket () Returns the property isTransferrredToWorkBasket . boolean isTypeUpdateable () Signals whether the type property can be changed for the kind and current state of the object. static boolean isValid (java.lang.String propertyName) Checks if the property is valid. boolean isWaitingForSubTask () Returns the property waitingForSubTask . boolean isWorkBasketNameUpdateable () Signals whether the work basket name property can be changed for the kind and current state of the object. void setApplicationName (java.lang.String newApplicationName) void setBusinessRelevance (boolean arg0) Sets the property businessRelevance . void setChild (boolean childState) Sets the property child . void setContextAuthorizationOfOwner (int arg0) Sets the property contextAuthorizationOfOwner . void setDeletionTime (java.util.Calendar arg0) Sets the property deletionTime . void setDescription (java.lang.String arg0, java.util.Locale arg1) Sets the property description . void setDisplayName (java.lang.String arg0, java.util.Locale arg1) Sets the property displayName . void setDueTime (java.util.Calendar arg0) Sets the property dueTime . void setDurationUntilDeleted (java.lang.String arg0) Sets the property durationUntilDeleted . void setDurationUntilDue (java.lang.String arg0) Sets the property durationUntilDue . void setDurationUntilExpires (java.lang.String arg0) Sets the property durationUntilExpires . void setEscalated (boolean escalatedState) Sets the property escalated . void setEventHandlerName (java.lang.String arg0) Sets the property eventHandlerName . void setExpirationTime (java.util.Calendar arg0) Sets the property expirationTime . protected void setHTMConnection (HTMConnection connection) void setLocalisedDescription (java.lang.String description, java.util.Locale locale) Sets the property description . void setLocalisedDisplayName (java.lang.String displayName, java.util.Locale locale) Sets the property displayName . void setName (java.lang.String arg0) Sets the property name . void setNamespace (java.lang.String arg0) Sets the property namespace . protected void setOriginal (Task task) void setParentContextID (OID arg0) Sets the property parentContextID . void setPriority (java.lang.Integer arg0) Sets the property priority . void setRead (boolean readState) Sets the property read . void setState (java.lang.Integer newState) Sets the property state . void setSupportsClaimIfSuspended (boolean arg0) Sets the property supportsClaimIfSuspended . void setSupportsDelegation (boolean arg0) Sets the property supportsDelegation . void setSupportsFollowOnTasks (boolean arg0) Sets the property supportsFollowOnTasks . void setSupportsSubTasks (boolean arg0) Sets the property supportsSubTasks . void setSuspended (boolean suspendedState) Sets the property suspended . void setType (java.lang.String arg0) Sets the property type . void setWorkBasketName (java.lang.String arg0) Sets the property workBasketName . boolean supportsAutomaticClaim () Returns the property supportsAutomaticClaim . boolean supportsClaimIfSuspended () Returns the property supportsClaimIfSuspended . boolean supportsDelegation () Returns the property supportsDelegation . boolean supportsFollowOnTasks () Returns the property supportsFollowOnTasks . boolean supportsSubTasks () Returns the property supportsSubTasks .

### Method Summary

| Modifier and Type                           | Method and Description                                                                                                                                     |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MessageWrapper                              | createOutputMessageWrapper() Creates an initial empty output message.                                                                                      |
| java.util.Calendar                          | getActivationTime() Returns the property activationTime.                                                                                                   |
| ACOID                                       | getApplicationDefaultsID() Returns the property applicationDefaultsID.                                                                                     |
| java.lang.String                            | getApplicationName() Returns the name of the application the task is part of.                                                                              |
| int                                         | getAssignmentType() Returns the property assignmentType.                                                                                                   |
| int                                         | getAutoDeletionMode() Returns the property autoDeletionMode.                                                                                               |
| java.lang.String                            | getCalendarName() Returns the property calendarName.                                                                                                       |
| java.util.Calendar                          | getCompletionTime() Returns the property completionTime.                                                                                                   |
| OID                                         | getContainmentContextID() Returns the property containmentContextID.                                                                                       |
| int                                         | getContextAuthorizationOfOwner() Returns the property contextAuthorizationOfOwner.                                                                         |
| static SimpleConverter                      | getConverter(java.lang.String propertyName) Returns the default converter for a given property.                                                            |
| java.lang.String                            | getCustomText1() Returns the property customText1.                                                                                                         |
| java.lang.String                            | getCustomText2() Returns the property customText2.                                                                                                         |
| java.lang.String                            | getCustomText3() Returns the property customText3.                                                                                                         |
| java.lang.String                            | getCustomText4() Returns the property customText4.                                                                                                         |
| java.lang.String                            | getCustomText5() Returns the property customText5.                                                                                                         |
| java.lang.String                            | getCustomText6() Returns the property customText6.                                                                                                         |
| java.lang.String                            | getCustomText7() Returns the property customText7.                                                                                                         |
| java.lang.String                            | getCustomText8() Returns the property customText8.                                                                                                         |
| java.lang.String                            | getDefinitionName() Returns the property definition name.                                                                                                  |
| java.lang.String                            | getDefinitionNamespace() Returns the property definition namespace.                                                                                        |
| java.util.Calendar                          | getDeletionTime() Returns the property deletionTime.                                                                                                       |
| com.ibm.bpc.clientcore.util.LocalisedString | getDescription() Returns the localised description.                                                                                                        |
| java.lang.String                            | getDescription(java.util.Locale locale) Returns the property description.                                                                                  |
| com.ibm.bpc.clientcore.util.LocalisedString | getDisplayName() Returns the localised display name.                                                                                                       |
| java.lang.String                            | getDisplayName(java.util.Locale locale) Returns the property displayName.                                                                                  |
| java.util.Calendar                          | getDueTime() Returns the property dueTime.                                                                                                                 |
| java.lang.String                            | getDurationUntilDeleted() Returns the property durationUntilDeleted.                                                                                       |
| java.lang.String                            | getDurationUntilDue() Returns the property durationUntilDue.                                                                                               |
| java.lang.String                            | getDurationUntilExpires() Returns the property durationUntilExpires.                                                                                       |
| java.lang.String                            | getEventHandlerName() Returns the property eventHandlerName.                                                                                               |
| java.util.Calendar                          | getExpirationTime() Returns the property expirationTime.                                                                                                   |
| MessageWrapper                              | getFaultMessageWrapper() Retrieves the fault message.                                                                                                      |
| java.util.Calendar                          | getFirstActivationTime() Returns the property firstActivationTime.                                                                                         |
| TKIID                                       | getFollowOnTaskID() Returns the property followOnTaskID.                                                                                                   |
| protected HTMConnection                     | getHTMConnection()                                                                                                                                         |
| TKIID                                       | getID() Returns the property ID.                                                                                                                           |
| int                                         | getInheritedAuthorization() Returns the property inheritedAuthorization.                                                                                   |
| java.lang.String                            | getInputMessageTypeName() Returns the property inputMessageTypeName.                                                                                       |
| MessageWrapper                              | getInputMessageWrapper() Retrieves the input message.                                                                                                      |
| OID                                         | getInvokedInstanceID() Returns the property invokedInstanceID.                                                                                             |
| int                                         | getInvokedInstanceType() Returns the property invokedInstanceType.                                                                                         |
| java.lang.String                            | getJNDINameOfCalendar() Returns the property JNDINameOfCalendar.                                                                                           |
| java.lang.String                            | getJNDINameOfStaffPluginProvider() Returns the property JNDINameOfStaffPluginProvider.                                                                     |
| int                                         | getKind() Returns the property kind.                                                                                                                       |
| static java.lang.String                     | getLabel(java.lang.String propertyName) Returns the resource bundle key for a property                                                                     |
| static java.lang.String                     | getLabel(java.lang.String propertyName,         java.util.Locale locale) Returns the label for a property from the resource bundle.                        |
| java.util.Calendar                          | getLastModificationTime() Returns the property lastModificationTime.                                                                                       |
| java.util.Calendar                          | getLastStateChangeTime() Returns the property lastStateChangeTime.                                                                                         |
| java.util.List                              | getLocalesOfDescriptions() Returns the property localesOfDescriptions.                                                                                     |
| java.util.List                              | getLocalesOfDisplayNames() Returns the property localesOfDisplayNames.                                                                                     |
| java.lang.String                            | getName() Returns the property name.                                                                                                                       |
| java.lang.String                            | getNamespace() Returns the property namespace.                                                                                                             |
| protected Task                              | getOriginal()                                                                                                                                              |
| java.lang.String                            | getOriginator() Returns the property originator.                                                                                                           |
| java.lang.String                            | getOutputMessageTypeName() Returns the property outputMessageTypeName.                                                                                     |
| MessageWrapper                              | getOutputMessageWrapper() Retrieves the output message.                                                                                                    |
| java.lang.String                            | getOwner() Returns the property owner.                                                                                                                     |
| OID                                         | getParentContextID() Returns the property parentContextID.                                                                                                 |
| int                                         | getPositionInHierarchy() Returns the property positionInHierarchy.                                                                                         |
| java.lang.Integer                           | getPriority() Returns the property priority.                                                                                                               |
| java.lang.String                            | getProcessAppAcronym() Returns the processAppAcronym property.                                                                                             |
| java.lang.String                            | getProcessAppName() Returns the processAppName property.                                                                                                   |
| java.util.Calendar                          | getResumptionTime() Returns the property resumptionTime.                                                                                                   |
| java.lang.String                            | getSnapshotID() Returns the snapshotID property.                                                                                                           |
| java.lang.String                            | getSnapshotName() Returns the snapshotName property.                                                                                                       |
| java.lang.String                            | getStarter() Returns the property starter.                                                                                                                 |
| java.util.Calendar                          | getStartTime() Returns the property startTime.                                                                                                             |
| int                                         | getState() Returns the property state.                                                                                                                     |
| int                                         | getSubstitutionPolicy() Returns the property substitutionPolicy.                                                                                           |
| TKTID                                       | getTaskTemplateID() Returns the property taskTemplateID.                                                                                                   |
| java.lang.String                            | getTaskTemplateName() Returns the property taskTemplateName.                                                                                               |
| java.lang.String                            | getToolkitAcronym() Returns the toolkitAcronym property.                                                                                                   |
| java.lang.String                            | getToolkitName() Returns the toolkitName property.                                                                                                         |
| java.lang.String                            | getToolkitSnapshotID() Returns the toolkitSnapshotID property.                                                                                             |
| java.lang.String                            | getToolkitSnapshotName() Returns the toolkitSnapshotName property.                                                                                         |
| TKIID                                       | getTopLevelTaskID() Returns the property topLevelTaskID.                                                                                                   |
| java.lang.String                            | getTopLevelToolkitAcronym() Returns the topLevelToolkitAcronym property.                                                                                   |
| java.lang.String                            | getTopLevelToolkitName() Returns the topLevelToolkitName property.                                                                                         |
| java.lang.String                            | getTrackName() Returns the trackName property.                                                                                                             |
| java.lang.String                            | getType() Returns the property type.                                                                                                                       |
| java.util.Calendar                          | getValidFromTime() Returns the validFromTime property.                                                                                                     |
| java.lang.String                            | getWorkBasketName() Returns the property workBasketName.                                                                                                   |
| boolean                                     | isAdHoc() Returns the property adHoc.                                                                                                                      |
| boolean                                     | isBusinessRelevanceUpdateable() Signals whether the business relevance property can be changed for the  kind and current state of the object.              |
| boolean                                     | isBusinessRelevant() Returns the property businessRelevant.                                                                                                |
| boolean                                     | isChild() Returns the property isChild.                                                                                                                    |
| boolean                                     | isContextAuthorizationOfOwnerUpdateable() Signals whether the context authorization property can be changed for the  kind and current state of the object. |
| boolean                                     | isDeletionTimeUpdateable() Signals whether the deletion time property can be changed for the kind  and current state of the object.                        |
| boolean                                     | isDescriptionUpdateable() Signals whether the description property can be changed for the kind and  current state of the object.                           |
| boolean                                     | isDisplayNameUpdateable() Signals whether the display name property can be changed for the kind and  current state of the object.                          |
| boolean                                     | isDueTimeUpdateable() Signals whether the due time property can be changed for the kind and  current state of the object.                                  |
| boolean                                     | isDurationUntilDeletedUpdateable() Signals whether the duration until deleted property can be changed for  the kind and current state of the object.       |
| boolean                                     | isDurationUntilDueUpdateable() Signals whether the duration until due property can be changed for the  kind and current state of the object.               |
| boolean                                     | isDurationUntilExpiresUpdateable() Signals whether the duration until expires property can be changed for  the kind and current state of the object.       |
| boolean                                     | isEscalated() Returns the property escalated.                                                                                                              |
| boolean                                     | isEscalatedUpdateable() Returns the property escalatedUpdateable().                                                                                        |
| boolean                                     | isEventHandlerNameUpdateable() Signals whether the event handler name property can be changed for the  kind and current state of the object.               |
| boolean                                     | isExpirationTimeUpdateable() Signals whether the expiration time property can be changed for the kind  and current state of the object.                    |
| boolean                                     | isInline() Returns the property inline.                                                                                                                    |
| boolean                                     | isNamespaceUpdateable() Signals whether the namespace property can be changed for the kind and  current state of the object.                               |
| boolean                                     | isNameUpdateable() Signals whether the name property can be changed for the kind and current  state of the object.                                         |
| boolean                                     | isParentContextIDUpdateable() Signals whether the parent context i d property can be changed for the  kind and current state of the object.                |
| boolean                                     | isPriorityUpdateable() Signals whether the priority property can be changed for the kind and  current state of the object.                                 |
| boolean                                     | isRead() Returns the property isRead.                                                                                                                      |
| boolean                                     | isReadUpdateable() Returns the property readUpdateable().                                                                                                  |
| boolean                                     | isSupportsAutomaticClaim() Returns the property supportsAutomaticClaim.                                                                                    |
| boolean                                     | isSupportsClaimIfSuspended() Returns the property supportsClaimIfSuspended.                                                                                |
| boolean                                     | isSupportsClaimIfSuspendedUpdateable() Signals whether the supports claim suspended property can be changed for  the kind and current state of the object. |
| boolean                                     | isSupportsDelegation() Returns the property supportsDelegation.                                                                                            |
| boolean                                     | isSupportsDelegationUpdateable() Signals whether the supports delegation property can be changed for the  kind and current state of the object.            |
| boolean                                     | isSupportsFollowOnTasks() Returns the property supportsFollowOnTasks.                                                                                      |
| boolean                                     | isSupportsFollowOnTasksUpdateable() Signals whether the supports follow on task property can be changed for  the kind and current state of the object.     |
| boolean                                     | isSupportsSubTasks() Returns the property supportsSubTasks.                                                                                                |
| boolean                                     | isSupportsSubTasksUpdateable() Signals whether the supports sub task property can be changed for the  kind and current state of the object.                |
| boolean                                     | isSuspended() Returns the property suspended.                                                                                                              |
| boolean                                     | isTip() Returns the tip property.                                                                                                                          |
| boolean                                     | isTransferredToWorkBasket() Returns the property isTransferrredToWorkBasket.                                                                               |
| boolean                                     | isTypeUpdateable() Signals whether the type property can be changed for the kind and current  state of the object.                                         |
| static boolean                              | isValid(java.lang.String propertyName) Checks if the property is valid.                                                                                    |
| boolean                                     | isWaitingForSubTask() Returns the property waitingForSubTask.                                                                                              |
| boolean                                     | isWorkBasketNameUpdateable() Signals whether the work basket name property can be changed for the kind  and current state of the object.                   |
| void                                        | setApplicationName(java.lang.String newApplicationName)                                                                                                    |
| void                                        | setBusinessRelevance(boolean arg0) Sets the property businessRelevance.                                                                                    |
| void                                        | setChild(boolean childState) Sets the property child.                                                                                                      |
| void                                        | setContextAuthorizationOfOwner(int arg0) Sets the property contextAuthorizationOfOwner.                                                                    |
| void                                        | setDeletionTime(java.util.Calendar arg0) Sets the property deletionTime.                                                                                   |
| void                                        | setDescription(java.lang.String arg0,               java.util.Locale arg1) Sets the property description.                                                  |
| void                                        | setDisplayName(java.lang.String arg0,               java.util.Locale arg1) Sets the property displayName.                                                  |
| void                                        | setDueTime(java.util.Calendar arg0) Sets the property dueTime.                                                                                             |
| void                                        | setDurationUntilDeleted(java.lang.String arg0) Sets the property durationUntilDeleted.                                                                     |
| void                                        | setDurationUntilDue(java.lang.String arg0) Sets the property durationUntilDue.                                                                             |
| void                                        | setDurationUntilExpires(java.lang.String arg0) Sets the property durationUntilExpires.                                                                     |
| void                                        | setEscalated(boolean escalatedState) Sets the property escalated.                                                                                          |
| void                                        | setEventHandlerName(java.lang.String arg0) Sets the property eventHandlerName.                                                                             |
| void                                        | setExpirationTime(java.util.Calendar arg0) Sets the property expirationTime.                                                                               |
| protected void                              | setHTMConnection(HTMConnection connection)                                                                                                                 |
| void                                        | setLocalisedDescription(java.lang.String description,                        java.util.Locale locale) Sets the property description.                       |
| void                                        | setLocalisedDisplayName(java.lang.String displayName,                        java.util.Locale locale) Sets the property displayName.                       |
| void                                        | setName(java.lang.String arg0) Sets the property name.                                                                                                     |
| void                                        | setNamespace(java.lang.String arg0) Sets the property namespace.                                                                                           |
| protected void                              | setOriginal(Task task)                                                                                                                                     |
| void                                        | setParentContextID(OID arg0) Sets the property parentContextID.                                                                                            |
| void                                        | setPriority(java.lang.Integer arg0) Sets the property priority.                                                                                            |
| void                                        | setRead(boolean readState) Sets the property read.                                                                                                         |
| void                                        | setState(java.lang.Integer newState) Sets the property state.                                                                                              |
| void                                        | setSupportsClaimIfSuspended(boolean arg0) Sets the property supportsClaimIfSuspended.                                                                      |
| void                                        | setSupportsDelegation(boolean arg0) Sets the property supportsDelegation.                                                                                  |
| void                                        | setSupportsFollowOnTasks(boolean arg0) Sets the property supportsFollowOnTasks.                                                                            |
| void                                        | setSupportsSubTasks(boolean arg0) Sets the property supportsSubTasks.                                                                                      |
| void                                        | setSuspended(boolean suspendedState) Sets the property suspended.                                                                                          |
| void                                        | setType(java.lang.String arg0) Sets the property type.                                                                                                     |
| void                                        | setWorkBasketName(java.lang.String arg0) Sets the property workBasketName.                                                                                 |
| boolean                                     | supportsAutomaticClaim() Returns the property supportsAutomaticClaim.                                                                                      |
| boolean                                     | supportsClaimIfSuspended() Returns the property supportsClaimIfSuspended.                                                                                  |
| boolean                                     | supportsDelegation() Returns the property supportsDelegation.                                                                                              |
| boolean                                     | supportsFollowOnTasks() Returns the property supportsFollowOnTasks.                                                                                        |
| boolean                                     | supportsSubTasks() Returns the property supportsSubTasks.                                                                                                  |

    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait