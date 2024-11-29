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

## Class ActivityInstanceBean

- java.lang.Object
    - com.ibm.bpe.clientmodel.bean.ActivityInstanceBean

- All Implemented Interfaces: ActivityInstanceData , java.io.Serializable public class ActivityInstanceBean extends java.lang.Objectimplements ActivityInstanceData Accesses the properties of the original ActivityInstanceData object and adds metadata for national language support and converters. An ActivityInstanceBean object can be instantiated from either a QueryResultSet object or an ActivityInstanceData object. If the bean was instantiated from an original object returned by the Business Process Choreographer API, all properties are loaded. If, however, the bean is instantiated from a query only the following properties are loaded from the query result set: If a property is not found in the query result set, the property remains empty. Ig the bean accesses an empty property, it must load the missing information from the server. Use the static method getLabel(String, Locale) to retrieve the localized label for a property. Use the static method getConverter(String) to retrieve a converter for a property. As converters are optional, the return value might be null. See Also: ActivityInstanceData , QueryResultSet , Serialized Form

```
public class ActivityInstanceBean
extends java.lang.Object
implements ActivityInstanceData
```

Accesses the properties of the original ActivityInstanceData object
 and adds metadata for national language support and converters.

An ActivityInstanceBean object can be instantiated from either a
 QueryResultSet object or an ActivityInstanceData object. 

 If the bean was instantiated from an original object returned by the Business
 Process Choreographer API, all properties are loaded. If, however, the bean
 is instantiated from a query only the following properties are loaded from
 the query result set:
 
ID
activationTime
completionTime
description
expirationTime
kind
owner
startTime
executionState
activityName
processInstanceName
processTemplateName
processTemplateDisplayName
stopReason
subState

 If a property is not found in the query result set, the property remains
 empty. Ig the bean accesses an empty property, it must load the missing
 information from the server.

Use the static method getLabel(String, Locale)
 to retrieve the localized label for a property. Use the static method
 getConverter(String) to retrieve a converter for
 a property. As converters are optional, the return value might be null.

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String ACTIVATIONTIME\_PROPERTY Uses the property name to determine labels and converters for the "activation time" property. static java.lang.String APPLICATIONNAME\_PROPERTY Uses the property name to determine labels and converters for the "application name" property. static java.lang.String AVAILABLEACTIONS\_PROPERTY Uses the property name to determine labels and converters for the "available actions" property. static java.lang.String COMPLETIONTIME\_PROPERTY Uses the property name to determine labels and converters for the "completion time" property. static java.lang.String CONTINUEONERROR\_PROPERTY Use the property name to determine labels and converters for the continueOnError property. static java.lang.String COPYRIGHT (C) Copyright IBM Corporation 2004, 2010. static java.lang.String CUSTOMPROPERTY\_PROPERTY Uses the property name to determine labels and converters for the "custom properties" property. static java.lang.String DESCRIPTION\_PROPERTY Uses the property name to determine labels and converters for the "description" property. static java.lang.String DISPLAYNAME\_PROPERTY Uses the property name to determine labels and converters for the "display name" property. static java.lang.String EXECUTIONSTATE\_PROPERTY Uses the property name to determine labels and converters for the "execution state" property. static java.lang.String EXPIRATIONTIME\_PROPERTY Uses the property name to determine labels and converters for the "expiration time" property. static java.lang.String FAULTNAMES\_PROPERTY Uses the property name to determine labels and converters for the "fault name" property. static java.lang.String ID\_PROPERTY Uses the property name to determine labels and converters for the "ID" property. static java.lang.String INPUTMESSAGETYPENAME\_PROPERTY Uses the property name to determine labels and converters for the "input message type name" property. static java.lang.String INPUTMESSAGETYPETYPESYSTEMNAME\_PROPERTY Deprecated. static java.lang.String KIND\_PROPERTY Uses the property name to determine labels and converters for the "kind" property. static java.lang.String LASTMODIFICATIONTIME\_PROPERTY Uses the property name to determine labels and converters for the "last modification time" property. static java.lang.String LASTSTATECHANGETIME\_PROPERTY Uses the property name to determine labels and converters for the "last state change time" property. static java.lang.String NAME\_PROPERTY Uses the property name to determine labels and converters for the "name" property. static java.lang.String OUTPUTMESSAGETYPENAME\_PROPERTY Uses the property name to determine labels and converters for the "output message type name" property. static java.lang.String OUTPUTMESSAGETYPETYPESYSTEMNAME\_PROPERTY Deprecated. static java.lang.String OWNER\_PROPERTY Uses the property name to determine labels and converters for the "owner" property. static java.lang.String PREVIOUSEXPIRATIONTIME\_PROPERTY Uses the property name to determine labels and converters for the "expiration time" property. static java.lang.String PROCESSADMINISTRATORS\_PROPERTY Uses the property name to determine labels and converters for the "process administrators" property. static java.lang.String PROCESSINSTANCEID\_PROPERTY Uses the property name to determine labels and converters for the "process instance ID" property. static java.lang.String PROCESSINSTANCENAME\_PROPERTY Uses the property name to determine labels and converters for the "process instance name" property. static java.lang.String PROCESSTEMPLATEDISPLAYNAME\_PROPERTY Use the property name to determine labels and converters for the processTemplateDisplayName property. static java.lang.String PROCESSTEMPLATEID\_PROPERTY Uses the property name to determine labels and converters for the "process template ID" property. static java.lang.String PROCESSTEMPLATENAME\_PROPERTY Uses the property name to determine labels and converters for the "process template name" property. static java.lang.String SKIPREQUESTED\_PROPERTY Uses the property name to determine labels and converters for the "skipRequested" property. static java.lang.String STARTTIME\_PROPERTY Uses the property name to determine labels and converters for the "start time" property. static java.lang.String STOPREASON\_PROPERTY Uses the property name to determine labels and converters for the "stopReason" property. static java.lang.String SUBSTATE\_PROPERTY Uses the property name to determine labels and converters for the "subState" property. static java.lang.String UNHANDLEDEXCEPTION\_PROPERTY Uses the property name to determine labels and converters for the "unhandled exception" property.

### Field Summary

| Modifier and Type       | Field and Description                                                                                                                      |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| static java.lang.String | ACTIVATIONTIME\_PROPERTY Uses the property name to determine labels and converters for the  "activation time" property.                     |
| static java.lang.String | APPLICATIONNAME\_PROPERTY Uses the property name to determine labels and converters for the  "application name" property.                   |
| static java.lang.String | AVAILABLEACTIONS\_PROPERTY Uses the property name to determine labels and converters for the  "available actions" property.                 |
| static java.lang.String | COMPLETIONTIME\_PROPERTY Uses the property name to determine labels and converters for the  "completion time" property.                     |
| static java.lang.String | CONTINUEONERROR\_PROPERTY Use the property name to determine labels and converters for the  continueOnError property.                       |
| static java.lang.String | COPYRIGHT (C) Copyright IBM Corporation 2004, 2010.                                                                                        |
| static java.lang.String | CUSTOMPROPERTY\_PROPERTY Uses the property name to determine labels and converters for the  "custom properties" property.                   |
| static java.lang.String | DESCRIPTION\_PROPERTY Uses the property name to determine labels and converters for the  "description" property.                            |
| static java.lang.String | DISPLAYNAME\_PROPERTY Uses the property name to determine labels and converters for the  "display name" property.                           |
| static java.lang.String | EXECUTIONSTATE\_PROPERTY Uses the property name to determine labels and converters for the  "execution state" property.                     |
| static java.lang.String | EXPIRATIONTIME\_PROPERTY Uses the property name to determine labels and converters for the  "expiration time" property.                     |
| static java.lang.String | FAULTNAMES\_PROPERTY Uses the property name to determine labels and converters for the  "fault name" property.                              |
| static java.lang.String | ID\_PROPERTY Uses the property name to determine labels and converters for the "ID"  property.                                              |
| static java.lang.String | INPUTMESSAGETYPENAME\_PROPERTY Uses the property name to determine labels and converters for the  "input message type name" property.       |
| static java.lang.String | INPUTMESSAGETYPETYPESYSTEMNAME\_PROPERTY Deprecated.                                                                                        |
| static java.lang.String | KIND\_PROPERTY Uses the property name to determine labels and converters for the "kind"  property.                                          |
| static java.lang.String | LASTMODIFICATIONTIME\_PROPERTY Uses the property name to determine labels and converters for the  "last modification time" property.        |
| static java.lang.String | LASTSTATECHANGETIME\_PROPERTY Uses the property name to determine labels and converters for the  "last state change time" property.         |
| static java.lang.String | NAME\_PROPERTY Uses the property name to determine labels and converters for the "name"  property.                                          |
| static java.lang.String | OUTPUTMESSAGETYPENAME\_PROPERTY Uses the property name to determine labels and converters for the  "output message type name" property.     |
| static java.lang.String | OUTPUTMESSAGETYPETYPESYSTEMNAME\_PROPERTY Deprecated.                                                                                       |
| static java.lang.String | OWNER\_PROPERTY Uses the property name to determine labels and converters for the "owner"  property.                                        |
| static java.lang.String | PREVIOUSEXPIRATIONTIME\_PROPERTY Uses the property name to determine labels and converters for the  "expiration time" property.             |
| static java.lang.String | PROCESSADMINISTRATORS\_PROPERTY Uses the property name to determine labels and converters for the  "process administrators" property.       |
| static java.lang.String | PROCESSINSTANCEID\_PROPERTY Uses the property name to determine labels and converters for the  "process instance ID" property.              |
| static java.lang.String | PROCESSINSTANCENAME\_PROPERTY Uses the property name to determine labels and converters for the  "process instance name" property.          |
| static java.lang.String | PROCESSTEMPLATEDISPLAYNAME\_PROPERTY Use the property name to determine labels and converters for the  processTemplateDisplayName property. |
| static java.lang.String | PROCESSTEMPLATEID\_PROPERTY Uses the property name to determine labels and converters for the  "process template ID" property.              |
| static java.lang.String | PROCESSTEMPLATENAME\_PROPERTY Uses the property name to determine labels and converters for the  "process template name" property.          |
| static java.lang.String | SKIPREQUESTED\_PROPERTY Uses the property name to determine labels and converters for the  "skipRequested" property.                        |
| static java.lang.String | STARTTIME\_PROPERTY Uses the property name to determine labels and converters for the  "start time" property.                               |
| static java.lang.String | STOPREASON\_PROPERTY Uses the property name to determine labels and converters for the  "stopReason" property.                              |
| static java.lang.String | SUBSTATE\_PROPERTY Uses the property name to determine labels and converters for the  "subState" property.                                  |
| static java.lang.String | UNHANDLEDEXCEPTION\_PROPERTY Uses the property name to determine labels and converters for the  "unhandled exception" property.             |

- Fields inherited from interface com.ibm.bpe.api.ActivityInstanceData
INVOKED\_INSTANCE\_TYPE\_CHILD\_PROCESS, INVOKED\_INSTANCE\_TYPE\_CHILD\_TASK, INVOKED\_INSTANCE\_TYPE\_INLINE\_TASK, INVOKED\_INSTANCE\_TYPE\_NOT\_SET, KIND\_ABSTRACT\_TASK, KIND\_ASSIGN, KIND\_CALL\_ACTIVITY, KIND\_COMPENSATE, KIND\_COMPENSATE\_SCOPE, KIND\_COMPENSATION\_END\_EVENT, KIND\_COMPENSATION\_INTERRUPTING\_SUBPROCESS\_START\_EVENT, KIND\_COMPENSATION\_THROW\_EVENT, KIND\_CUSTOM, KIND\_EMPTY, KIND\_ERROR\_END\_EVENT, KIND\_ERROR\_EVENT\_SUBPROCESS\_ACTIVITY, KIND\_ERROR\_INTERRUPTING\_BOUNDARY\_EVENT, KIND\_ERROR\_INTERRUPTING\_SUBPROCESS\_START\_EVENT, KIND\_EVENT\_BASED\_GATEWAY, KIND\_FLOW, KIND\_FLOW\_END, KIND\_FOR\_EACH\_PARALLEL, KIND\_FOR\_EACH\_PARALLEL\_END, KIND\_FOR\_EACH\_SERIAL, KIND\_FOR\_EACH\_SERIAL\_END, KIND\_INVOKE, KIND\_INVOKE\_END, KIND\_IOR\_GATEWAY, KIND\_IOR\_IN\_GATEWAY, KIND\_MESSAGE\_CATCH\_EVENT, KIND\_MESSAGE\_END\_EVENT, KIND\_MESSAGE\_EVENT\_SUBPROCESS\_ACTIVITY, KIND\_MESSAGE\_NONINTERRUPTING\_SUBPROCESS\_START\_EVENT, KIND\_MESSAGE\_START\_EVENT, KIND\_MESSAGE\_THROW\_EVENT, KIND\_NONE\_END\_EVENT, KIND\_NONE\_START\_EVENT, KIND\_PARALLEL\_GATEWAY, KIND\_PICK, KIND\_PICK\_END, KIND\_RECEIVE, KIND\_RECEIVE\_TASK, KIND\_REPEAT\_UNTIL, KIND\_REPEAT\_UNTIL\_END, KIND\_REPLY, KIND\_RETHROW, KIND\_SCOPE, KIND\_SCOPE\_END, KIND\_SCRIPT, KIND\_SCRIPT\_TASK, KIND\_SEND\_TASK, KIND\_SEQUENCE, KIND\_SEQUENCE\_END, KIND\_SERVICE\_TASK, KIND\_STAFF, KIND\_SUBPROCESS\_ACTIVITY, KIND\_SWITCH, KIND\_SWITCH\_END, KIND\_TERMINATE, KIND\_TERMINATE\_END\_EVENT, KIND\_THROW, KIND\_TIMER\_CATCH\_EVENT, KIND\_TIMER\_EVENT\_SUBPROCESS\_ACTIVITY, KIND\_TIMER\_INTERRUPTING\_BOUNDARY\_EVENT, KIND\_TIMER\_NONINTERRUPTING\_SUBPROCESS\_START\_EVENT, KIND\_USER\_TASK, KIND\_WAIT, KIND\_WHILE, KIND\_WHILE\_END, KIND\_XOR\_GATEWAY, STATE\_CLAIMED, STATE\_EXPIRED, STATE\_FAILED, STATE\_FAILING, STATE\_FINISHED, STATE\_INACTIVE, STATE\_PROCESSING\_UNDO, STATE\_READY, STATE\_RUNNING, STATE\_SKIPPED, STATE\_STOPPED, STATE\_TERMINATED, STATE\_TERMINATING, STATE\_WAITING, STOP\_REASON\_ACTIVATION\_FAILED, STOP\_REASON\_EXIT\_CONDITION\_FALSE, STOP\_REASON\_FOLLOW\_ON\_NAVIGATION\_FAILED, STOP\_REASON\_IMPLEMENTATION\_FAILED, STOP\_REASON\_UNSPECIFIED, SUB\_STATE\_EXPIRING, SUB\_STATE\_FAILING, SUB\_STATE\_FINISHING, SUB\_STATE\_NONE, SUB\_STATE\_RESTARTING, SUB\_STATE\_SKIPPING

- Constructor Summary

Constructors 

Modifier
Constructor and Description

 
ActivityInstanceBean(ActivityInstanceData activity,
                    BFMConnection bfmConnection)
Constructs a new ActivityInstanceBean from an original
 ActivityInstanceData object.

protected 
ActivityInstanceBean(AIID id,
                    BFMConnection bfmConnection)
Constructs a new ActivityInstanceBean from an activity
 instance id.

 
ActivityInstanceBean(QueryResultSet resultSet,
                    BFMConnection bfmConnection)
Constructs a new ActivityInstanceBean from a
 QueryResultSet.

- Method Summary Methods Modifier and Type Method and Description java.util.Calendar getActivationTime () Returns the activationTime property. boolean getActivityClaimed () Returns true if executionState is of state CLAIMED, returns false otherwise ATID getActivityTemplateID () Returns the activityTemplateID property. TKIID getAdminTaskID () Returns the adminTaskID property. java.lang.String getApplicationName () Returns the applicationName property. int[] getAvailableActions () Returns the availableActions property. java.util.Calendar getCompletionTime () Returns the completionTime property. static SimpleConverter getConverter (java.lang.String propertyName) Returns the default converter for a given property. java.lang.String getCustomProperty (java.lang.String arg) Returns the customProperty property. java.lang.String getDescription () Returns the description property. java.lang.String getDisplayName () Returns the displayName property. com.ibm.bpe.api.FEIID getEnclosingForEachID () Returns the enclosingForEachID property. com.ibm.bpe.api.EHIID getEventHandlerInstanceID () Returns the eventHandlerInstanceID property. int getExecutionState () Returns the executionState property. java.util.Calendar getExpirationTime () Returns the expirationTime property. MessageWrapper getFaultMessageWrapper () Retrieves the fault message. java.util.List getFaultNames () Returns the faultNames property. AIID getID () Returns the ID property. java.lang.String getInputMessageTypeName () Returns the inputMessageTypeName property. java.lang.String getInputMessageTypeTypeSystemName () Deprecated. MessageWrapper getInputMessageWrapper () Retrieves the input message. OID getInvokedInstanceID () Returns the invokedInstanceID property. int getInvokedInstanceType () Returns the invokedInstanceType property. int getKind () Returns the kind property. static java.lang.String getLabel (java.lang.String propertyName) Returns the resource bundle key for a property. static java.lang.String getLabel (java.lang.String propertyName, java.util.Locale locale) Returns the label of a property from the resource bundle. java.util.Calendar getLastModificationTime () Returns the lastModificationTime property. java.util.Calendar getLastStateChangeTime () Returns the lastStateChangeTime property. java.lang.String getName () Returns the name property. java.util.List getNamesOfCustomProperties () Returns the namesOfCustomProperties() property. java.lang.String getOutputMessageTypeName () Returns the outputMessageTypeName property. java.lang.String getOutputMessageTypeTypeSystemName () Deprecated. MessageWrapper getOutputMessageWrapper () Retrieves the output message. java.lang.String getOwner () Returns the owner property. java.util.Calendar getPreviousExpirationTime () Returns the time the activity instance expired for the first time. StaffResultSet getProcessAdministrators () Returns the processAdministrators property. TKIID getProcessAdminTaskID () Returns the processAdminTaskID property. PIID getProcessInstanceID () Returns the processInstanceID property. java.lang.String getProcessInstanceName () Returns the processInstanceName property. java.lang.String getProcessTemplateDisplayName () Returns the processTemplateDisplayName property. PTID getProcessTemplateID () Returns the processTemplateID property. java.lang.String getProcessTemplateName () Returns the processTemplateName property. com.ibm.bpe.api.SIID getScopeID () Returns the scopeID property. com.ibm.bpe.api.STID getScopeTemplateID () Returns the scopeTemplateID property. java.util.Calendar getStartTime () Returns the startTime property. int getStopReason () Returns the stopReason property. int getSubState () Returns the subState property. TKIID getTaskID () Returns the taskID property. ProcessException getUnhandledException () Returns the unhandledException property. boolean isBusinessRelevant () Returns the businessRelevant property. boolean isContinueOnError () Returns the continueOnError property. boolean isSkipRequested () Returns the skipRequested property. static boolean isValid (java.lang.String propertyName) Checks that the property is valid. void setExecutionState (int state) Changes the activity's executionState property.

### Method Summary

| Modifier and Type       | Method and Description                                                                                                             |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| java.util.Calendar      | getActivationTime() Returns the activationTime property.                                                                           |
| boolean                 | getActivityClaimed() Returns true if executionState is of state CLAIMED, returns  false otherwise                                  |
| ATID                    | getActivityTemplateID() Returns the activityTemplateID property.                                                                   |
| TKIID                   | getAdminTaskID() Returns the adminTaskID property.                                                                                 |
| java.lang.String        | getApplicationName() Returns the applicationName property.                                                                         |
| int[]                   | getAvailableActions() Returns the availableActions property.                                                                       |
| java.util.Calendar      | getCompletionTime() Returns the completionTime property.                                                                           |
| static SimpleConverter  | getConverter(java.lang.String propertyName) Returns the default converter for a given property.                                    |
| java.lang.String        | getCustomProperty(java.lang.String arg) Returns the customProperty property.                                                       |
| java.lang.String        | getDescription() Returns the description property.                                                                                 |
| java.lang.String        | getDisplayName() Returns the displayName property.                                                                                 |
| com.ibm.bpe.api.FEIID   | getEnclosingForEachID() Returns the enclosingForEachID property.                                                                   |
| com.ibm.bpe.api.EHIID   | getEventHandlerInstanceID() Returns the eventHandlerInstanceID property.                                                           |
| int                     | getExecutionState() Returns the executionState property.                                                                           |
| java.util.Calendar      | getExpirationTime() Returns the expirationTime property.                                                                           |
| MessageWrapper          | getFaultMessageWrapper() Retrieves the fault message.                                                                              |
| java.util.List          | getFaultNames() Returns the faultNames property.                                                                                   |
| AIID                    | getID() Returns the ID property.                                                                                                   |
| java.lang.String        | getInputMessageTypeName() Returns the inputMessageTypeName property.                                                               |
| java.lang.String        | getInputMessageTypeTypeSystemName() Deprecated.                                                                                    |
| MessageWrapper          | getInputMessageWrapper() Retrieves the input message.                                                                              |
| OID                     | getInvokedInstanceID() Returns the invokedInstanceID property.                                                                     |
| int                     | getInvokedInstanceType() Returns the invokedInstanceType property.                                                                 |
| int                     | getKind() Returns the kind property.                                                                                               |
| static java.lang.String | getLabel(java.lang.String propertyName) Returns the resource bundle key for a property.                                            |
| static java.lang.String | getLabel(java.lang.String propertyName,         java.util.Locale locale) Returns the label of a property from the resource bundle. |
| java.util.Calendar      | getLastModificationTime() Returns the lastModificationTime property.                                                               |
| java.util.Calendar      | getLastStateChangeTime() Returns the lastStateChangeTime property.                                                                 |
| java.lang.String        | getName() Returns the name property.                                                                                               |
| java.util.List          | getNamesOfCustomProperties() Returns the namesOfCustomProperties() property.                                                       |
| java.lang.String        | getOutputMessageTypeName() Returns the outputMessageTypeName property.                                                             |
| java.lang.String        | getOutputMessageTypeTypeSystemName() Deprecated.                                                                                   |
| MessageWrapper          | getOutputMessageWrapper() Retrieves the output message.                                                                            |
| java.lang.String        | getOwner() Returns the owner property.                                                                                             |
| java.util.Calendar      | getPreviousExpirationTime() Returns the time the activity instance expired for the first time.                                     |
| StaffResultSet          | getProcessAdministrators() Returns the processAdministrators property.                                                             |
| TKIID                   | getProcessAdminTaskID() Returns the processAdminTaskID property.                                                                   |
| PIID                    | getProcessInstanceID() Returns the processInstanceID property.                                                                     |
| java.lang.String        | getProcessInstanceName() Returns the processInstanceName property.                                                                 |
| java.lang.String        | getProcessTemplateDisplayName() Returns the processTemplateDisplayName property.                                                   |
| PTID                    | getProcessTemplateID() Returns the processTemplateID property.                                                                     |
| java.lang.String        | getProcessTemplateName() Returns the processTemplateName property.                                                                 |
| com.ibm.bpe.api.SIID    | getScopeID() Returns the scopeID property.                                                                                         |
| com.ibm.bpe.api.STID    | getScopeTemplateID() Returns the scopeTemplateID property.                                                                         |
| java.util.Calendar      | getStartTime() Returns the startTime property.                                                                                     |
| int                     | getStopReason() Returns the stopReason property.                                                                                   |
| int                     | getSubState() Returns the subState property.                                                                                       |
| TKIID                   | getTaskID() Returns the taskID property.                                                                                           |
| ProcessException        | getUnhandledException() Returns the unhandledException property.                                                                   |
| boolean                 | isBusinessRelevant() Returns the businessRelevant property.                                                                        |
| boolean                 | isContinueOnError() Returns the continueOnError property.                                                                          |
| boolean                 | isSkipRequested() Returns the skipRequested property.                                                                              |
| static boolean          | isValid(java.lang.String propertyName) Checks that the property is valid.                                                          |
| void                    | setExecutionState(int state) Changes the activity's executionState property.                                                       |

    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait