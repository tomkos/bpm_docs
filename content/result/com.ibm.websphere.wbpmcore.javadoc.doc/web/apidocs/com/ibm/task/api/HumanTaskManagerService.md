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

## Interface HumanTaskManagerService

- All Known Subinterfaces:
HumanTaskManager, LocalHumanTaskManager, LocalHumanTaskManagerService

public interface HumanTaskManagerService
HumanTaskManagerService defines the human task methods that can be called by a local or remote client.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.util.List
bulkTransferWorkItem(ESIID[] esiids,
                    int assignmentReason,
                    java.lang.String fromOwner,
                    java.lang.String toOwner)
Transfers the specified work items for the specified escalation instances
 using escalation instance IDs - each transfer operation is executed in a transaction on its own.

java.util.List
bulkTransferWorkItem(java.lang.String[] identifiers,
                    int assignmentReason,
                    java.lang.String fromOwner,
                    java.lang.String toOwner)
Transfers the specified work items for the specified escalation or task instances
 using escalation or task instance IDs - each transfer operation is executed in a transaction on its own.

java.util.List
bulkTransferWorkItem(TKIID[] tkiids,
                    int assignmentReason,
                    java.lang.String fromOwner,
                    java.lang.String toOwner)
Transfers the specified work items for the specified task instances
 using task instance IDs - each transfer operation is executed in a transaction on its own.

ClientObjectWrapper
callTask(java.lang.String tkiid,
        ClientObjectWrapper input)
Synchronously executes a previously created invocation task instance
 using a string representation of the task instance ID.

ClientObjectWrapper
callTask(TKIID tkiid,
        ClientObjectWrapper input)
Synchronously executes a previously created invocation task instance
 using the task instance ID.

void
cancelClaim(java.lang.String tkiid)
Cancels the claim of a task instance using a string representation of the task instance ID.

java.util.List
cancelClaim(java.lang.String[] identifiers)
Cancels the claim of the specified task instances
 using string representations of the task instance IDs.

void
cancelClaim(java.lang.String tkiid,
           boolean keepTaskData)
Cancels the claim of a task instance and keeps any data that has been set
 using a string representation of the task instance ID.

void
cancelClaim(TKIID tkiid)
Cancels the claim of a task instance using the task instance ID.

java.util.List
cancelClaim(TKIID[] tkiids)
Cancels the claim of the specified task instances
 using task instance IDs.

void
cancelClaim(TKIID tkiid,
           boolean keepTaskData)
Cancels the claim of a task instance and keeps any data that has been set
 using the task instance ID.

ClientObjectWrapper
claim(java.lang.String tkiid)
Claims a ready to-do or collaboration task instance for user processing
 using a string representation of the task instance ID.

java.util.List
claim(java.lang.String[] identifiers)
Claims ready to-do or collaboration task instances for user processing
 using string representations of task instance IDs.

ClaimResult
claim(java.lang.String queryTableName,
     FilterOptions filterOptions,
     AuthorizationOptions authorizationOptions,
     java.util.List parameters,
     int maxRetryCount)
Claims a ready to-do or collaboration task instance contained in the specified
 query table.

Task
claim(java.lang.String whereClause,
     java.lang.String orderByClause,
     java.util.TimeZone timeZone)
Claims some ready to-do or collaboration task instance for user processing.

ClientObjectWrapper
claim(TKIID tkiid)
Claims a ready to-do or collaboration task instance for user processing
 using the task instance ID.

java.util.List
claim(TKIID[] tkiids)
Claims ready to-do or collaboration task instances for user processing
 using task instance IDs.

void
complete(java.lang.String tkiid)
Completes a claimed task instance using a string representation
 of the task instance ID.

java.util.List
complete(java.lang.String[] tkiids)
Completes the specified task instances using string representations of the task instance IDs.

void
complete(java.lang.String tkiid,
        ClientObjectWrapper output)
Completes a claimed task instance using a string representation
 of the task instance ID and passes the result of user processing.

void
complete(java.lang.String tkiid,
        java.lang.String faultName,
        ClientObjectWrapper faultMessage)
Completes a claimed task instance using a string representation of
 the task instance ID and states the failing of user processing.

void
complete(TKIID tkiid)
Completes a claimed task instance using
 the task instance ID.

java.util.List
complete(TKIID[] tkiids)
Completes the specified task instances using task instance IDs.

void
complete(TKIID tkiid,
        ClientObjectWrapper output)
Completes a claimed task instance using
 the task instance ID and passes the result of user processing.

void
complete(TKIID tkiid,
        java.lang.String faultName,
        ClientObjectWrapper faultMessage)
Completes a claimed task instance using the
 task instance ID and states the failing of user processing.

void
completeWithFollowOnTask(java.lang.String tkiid,
                        java.lang.String followOnID,
                        ClientObjectWrapper input)
Completes a task instance and starts a follow-on task
 using a string representation of the task instance ID.

void
completeWithFollowOnTask(TKIID tkiid,
                        TKIID followOnID,
                        ClientObjectWrapper input)
Completes a task instance and starts a follow-on task
 using the task instance ID.

void
completeWithNewFollowOnTask(java.lang.String tkiid,
                           java.lang.String name,
                           java.lang.String namespace,
                           ClientObjectWrapper input)
Completes a task instance and creates and starts a follow-on task
 using a string representation of the task instance ID.

void
completeWithNewFollowOnTask(java.lang.String tkiid,
                           TaskModel taskModel,
                           java.lang.String applicationName,
                           ClientObjectWrapper input)
Completes a task instance and creates and starts an ad hoc follow-on task
 using a string representation of the task instance ID.

void
completeWithNewFollowOnTask(TKIID tkiid,
                           java.lang.String name,
                           java.lang.String namespace,
                           ClientObjectWrapper input)
Completes a task instance and creates and starts a follow-on task
 using the task instance ID.

void
completeWithNewFollowOnTask(TKIID tkiid,
                           TaskModel taskModel,
                           java.lang.String applicationName,
                           ClientObjectWrapper input)
Completes a task instance and creates and starts an ad hoc follow-on task
 using the task instance ID.

ClientObjectWrapper
createAndCallTask(java.lang.String tktid,
                 ClientObjectWrapper input)
Creates and synchronously executes an invocation task instance
 using a string representation of the task template ID.

ClientObjectWrapper
createAndCallTask(java.lang.String name,
                 java.lang.String namespace,
                 ClientObjectWrapper input)
Creates and synchronously executes an invocation task instance.

ClientObjectWrapper
createAndCallTask(TKTID tktid,
                 ClientObjectWrapper input)
Creates and synchronously executes an invocation task instance
 using the task template ID.

TKIID
createAndStartTask(java.lang.String tktid,
                  ClientObjectWrapper input,
                  ReplyHandlerWrapper replyHandler)
Creates and starts a task instance
 using a string representation of the task template ID.

TKIID
createAndStartTask(java.lang.String name,
                  java.lang.String namespace,
                  ClientObjectWrapper input,
                  ReplyHandlerWrapper replyHandler)
Creates and starts a task instance from the currently valid task template.

TKIID
createAndStartTask(TaskModel taskModel,
                  java.lang.String applicationName,
                  java.lang.String parentContext,
                  ClientObjectWrapper input,
                  ReplyHandlerWrapper replyHandler)
Creates and starts a task from the specified task model.

TKIID
createAndStartTask(TKTID tktid,
                  ClientObjectWrapper input,
                  ReplyHandlerWrapper replyHandler)
Creates and starts a task instance
 using the task template ID.

TKIID
createAndStartTaskAsSubTask(java.lang.String tktid,
                           java.lang.String parentTaskID,
                           ClientObjectWrapper input)
Creates and starts a task instance as a subtask of the specified parent
 task instance using string representations of the task template and instance IDs.

TKIID
createAndStartTaskAsSubTask(java.lang.String name,
                           java.lang.String namespace,
                           java.lang.String parentTaskID,
                           ClientObjectWrapper input)
Creates and starts a task instance as a subtask of the specified parent
 task instance using a string representation of the parent task instance ID.

TKIID
createAndStartTaskAsSubTask(java.lang.String name,
                           java.lang.String namespace,
                           TKIID parentTaskID,
                           ClientObjectWrapper input)
Creates and starts a task instance as a subtask of the specified parent
 task instance using the parent task instance ID.

TKIID
createAndStartTaskAsSubTask(TaskModel taskModel,
                           java.lang.String applicationName,
                           java.lang.String parentTaskID,
                           ClientObjectWrapper input)
Creates and starts a task from the specified task model as a subtask of the
 specified parent task instance using a string representation of the task instance ID.

TKIID
createAndStartTaskAsSubTask(TaskModel taskModel,
                           java.lang.String applicationName,
                           TKIID parentTaskID,
                           ClientObjectWrapper input)
Creates and starts a task from the specified task model as a subtask of the
 specified parent task instance using the task instance ID.

TKIID
createAndStartTaskAsSubTask(TKTID tktid,
                           TKIID parentTaskID,
                           ClientObjectWrapper input)
Creates and starts a task instance as a subtask of the specified parent
 task instance using task template and parent task instance IDs.

ClientObjectWrapper
createFaultMessage(java.lang.String identifier,
                  java.lang.String faultName)
Creates a fault message for a fault that is defined by the specified task instance
 or template
 using a string representation of the task instance or template ID.

ClientObjectWrapper
createFaultMessage(TKIID tkiid,
                  java.lang.String faultName)
Creates a fault message for a fault that is defined by the specified task instance
 using the task instance ID.

ClientObjectWrapper
createFaultMessage(TKTID tktid,
                  java.lang.String faultName)
Creates a fault message for a fault that is defined by the specified task template
 using the task template ID.

ClientObjectWrapper
createInputMessage(java.lang.String identifier)
Creates an input message for the specified task instance or template
 using a string representation of the task instance or template ID.

ClientObjectWrapper
createInputMessage(TKIID tkiid)
Creates an input message for the specified task instance
 using the task instance ID.

ClientObjectWrapper
createInputMessage(TKTID tktid)
Creates an input message for the specified task template
 using the task template ID.

ClientObjectWrapper
createMessage(java.lang.String tkiid,
             java.lang.String messageTypeName)
Deprecated. 
As of version 6.0, replaced by createInputMessage,
 createOutputMessage, and
 createFaultMessage.

ClientObjectWrapper
createMessage(TKIID tkiid,
             java.lang.String messageTypeName)
Deprecated. 
As of version 6.0, replaced by createInputMessage,
 createOutputMessage, and
 createFaultMessage.

ClientObjectWrapper
createOutputMessage(java.lang.String identifier)
Creates an output message for the specified task instance or template
 using a string representation of the task instance or template ID.

ClientObjectWrapper
createOutputMessage(TKIID tkiid)
Creates an output message for the specified task instance
 using the task instance ID.

ClientObjectWrapper
createOutputMessage(TKTID tktid)
Creates an output message for the specified task template
 using the task template ID.

void
createStoredQuery(java.lang.String storedQueryName,
                 java.lang.String selectClause,
                 java.lang.String whereClause,
                 java.lang.String orderByClause,
                 java.lang.Integer threshold,
                 java.util.TimeZone timeZone)
Creates a query definition and persistently stores it in the database.

void
createStoredQuery(java.lang.String storedQueryName,
                 java.lang.String selectClause,
                 java.lang.String whereClause,
                 java.lang.String orderByClause,
                 java.lang.Integer threshold,
                 java.util.TimeZone timeZone,
                 java.util.List storedQueryProperties,
                 java.lang.String clientType)
Creates a query definition and specifies properties to be stored together with the query.

void
createStoredQuery(java.lang.String userID,
                 java.lang.String storedQueryName,
                 java.lang.String selectClause,
                 java.lang.String whereClause,
                 java.lang.String orderByClause,
                 java.lang.Integer threshold,
                 java.util.TimeZone timeZone,
                 java.util.List storedQueryProperties,
                 java.lang.String clientType)
Creates a query definition for the specified user.

TKIID
createTask(java.lang.String tktid,
          ClientObjectWrapper input)
Creates a task instance using a string representation of the task template ID
 and optionally passes an input message.

TKIID
createTask(java.lang.String name,
          java.lang.String namespace)
Creates a task instance from the currently valid task template.

TKIID
createTask(java.lang.String name,
          java.lang.String namespace,
          ClientObjectWrapper input)
Creates a task instance from the currently valid task template and specifies an input message.

TKIID
createTask(TaskModel taskModel,
          java.lang.String applicationName,
          java.lang.String parentContext)
Creates a task instance from the specified task model.

TKIID
createTask(TaskModel taskModel,
          java.lang.String applicationName,
          java.lang.String parentContext,
          ClientObjectWrapper input)
Creates a task instance from the specified task model and specifies an input message.

TKIID
createTask(TKTID tktid,
          ClientObjectWrapper input)
Creates a task instance using the task template ID
 and optionally passes an input message.

TKTID
createTaskTemplate(TaskModel taskModel,
                  java.lang.String applicationName)
Creates a task template from the specified task model.

void
createWorkItem(ESIID esiid,
              int assignmentReason,
              java.lang.String userID)
Creates a user work item for the specified escalation instance
 using the escalation instance ID.

void
createWorkItem(java.lang.String identifier,
              int assignmentReason,
              java.lang.String userID)
Creates a user work item for the specified task or escalation instance
 using a string representation of the task or escalation instance ID.

void
createWorkItem(TKIID tkiid,
              int assignmentReason,
              java.lang.String userID)
Creates a user work item for the specified task instance
 using the task instance ID.

void
delete(java.lang.String tkiid)
Deletes the specified task instance
  using a string representation of the task instance ID.

void
delete(java.lang.String identifier,
      boolean deleteInstances)
Deletes the specified task template
  using a string representation of the task template ID.

void
delete(TKIID tkiid)
Deletes the specified task instance using the task instance ID.

void
delete(TKTID tktid,
      boolean deleteInstances)
Deletes the specified task template using the task template ID.

void
deleteStoredQuery(java.lang.String storedQueryName)
Deletes the specified stored query.

void
deleteStoredQuery(java.lang.String userID,
                 java.lang.String storedQueryName)
Deletes the specified stored query for the specified user.

void
deleteWorkItem(ESIID esiid,
              int assignmentReason,
              java.lang.String userID)
Deletes the specified user work item using the escalation instance ID.

void
deleteWorkItem(java.lang.String identifier,
              int assignmentReason,
              java.lang.String userID)
Deletes the specified user work item using a string representation of
 the task or escalation instance ID.

void
deleteWorkItem(TKIID tkiid,
              int assignmentReason,
              java.lang.String userID)
Deletes the specified user work item using the task instance ID.

java.util.List
findQueryTableMetaData(MetaDataOptions metaDataOptions)
Queries the meta data of query tables.

boolean
getAbsence()
Deprecated. 
As of version 7.0, replaced by getUserSubstitutionDetail.
 

boolean
getAbsence(java.lang.String userID)
Deprecated. 
As of version 7.0, replaced by getUserSubstitutionDetail.

AIID
getActivityID(java.lang.String tkiid)
Retrieves the object ID of the activity instance associated to the specified task instance
 using a string representation of the task instance ID.

AIID
getActivityID(TKIID tkiid)
Retrieves the object ID of the activity instance associated to the specified task instance
 using the task instance ID.

java.util.List
getAllCustomProperties(java.lang.String identifier)
Retrieves all custom properties of the specified task template or task instance
 using a string representation of the object ID.

java.util.List
getAllCustomProperties(TKIID tkiid)
Retrieves all custom properties of the specified task instance using the task instance ID.

java.util.List
getAllCustomProperties(TKTID tktid)
Retrieves all custom properties of the specified task template using the task template ID.

WorkItem[]
getAllWorkItems(ESIID esiid)
Returns all work item assignments associated to specified escalation
  instance using the escalation instance ID.

WorkItem[]
getAllWorkItems(java.lang.String identifier)
Returns all work item assignments associated to specified task or escalation
  instance using a string representation of the task or escalation instance ID.

WorkItem[]
getAllWorkItems(TKIID tkiid)
Returns all work item assignments associated to specified task
  instance using the task instance ID.

ApplicationComponent
getApplicationComponent(ACOID acoid)
Retrieves the specified application component using the application component ID.

ApplicationComponent
getApplicationComponent(java.lang.String acoid)
Retrieves the specified application component using a string
 representation of the application component ID.

boolean[][]
getAvailableActionFlags(ESIID[] esiids)
Returns the actions that can be called for the specified escalation instances
 in their current state by the logged-on user using escalation instance IDs.

boolean[][]
getAvailableActionFlags(java.lang.String[] identifiers)
Returns the actions that can be called for the specified tasks or escalations
 in their current state by the logged-on user
 using string representations of the task or escalation instance IDs.

boolean[][]
getAvailableActionFlags(TKIID[] tkiids)
Returns the actions that can be called for the specified tasks in their
 current state by the logged-on user using task instance IDs.

int[]
getAvailableActions(ESIID esiid)
Returns the actions that can be called in the current escalation instance state
 by the logged-on user using the escalation instance ID.

int[]
getAvailableActions(ESTID estid)
Returns the actions that can be called in the current escalation template state
 by the logged-on user using the escalation template ID.

int[]
getAvailableActions(java.lang.String identifier)
Returns the actions that can be called by the logged-on user
 for the specified task instance, task template, escalation instance, or escalation template
 using a string representation of the object ID.

int[]
getAvailableActions(TKIID tkiid)
Returns the actions that can be called in the current task instance state
 by the logged-on user using the task instance ID.

int[]
getAvailableActions(TKTID tktid)
Returns the actions that can be called in the current task template state
 by the logged-on user using the task template ID.

BinaryCustomProperty
getBinaryCustomProperty(ESIID esiid,
                       java.lang.String propertyName)
Retrieves the named binary custom property of the specified
 escalation instance using the escalation instance ID.

BinaryCustomProperty
getBinaryCustomProperty(java.lang.String identifier,
                       java.lang.String propertyName)
Retrieves the named binary custom property of the specified
 task or escalation instance using a string representation of the object ID.

BinaryCustomProperty
getBinaryCustomProperty(TKIID tkiid,
                       java.lang.String propertyName)
Retrieves the named binary custom property of the specified
 task instance using the task instance ID.

java.util.List
getBinaryCustomPropertyNames(ESIID esiid)
Retrieves the names of all binary custom properties of the specified
 escalation instance using the escalation instance ID.

java.util.List
getBinaryCustomPropertyNames(java.lang.String identifier)
Retrieves the names of all binary custom properties of the specified
 task or escalation instance using a string representation of the task or escalation instance ID.

java.util.List
getBinaryCustomPropertyNames(TKIID tkiid)
Retrieves the names of all binary custom properties of the specified
 task instance using the task instance ID.

java.util.List
getCustomProperties(ESIID esiid)
Retrieves the custom properties of the specified escalation
 instance using the escalation instance ID.

java.util.List
getCustomProperties(ESTID estid)
Retrieves the custom properties of the specified escalation template
 using the escalation template ID.

java.util.List
getCustomProperties(java.lang.String identifier)
Retrieves the custom properties of the specified
 task instance, task template, escalation instance, or escalation template
 using a string representation of the object ID.

java.util.List
getCustomProperties(TKIID tkiid)
Retrieves all custom properties of the specified task
 instance using the task instance ID.

java.util.List
getCustomProperties(TKTID tktid)
Retrieves the custom properties of the specified task template
 using the task template ID.

java.lang.String
getCustomProperty(ESIID esiid,
                 java.lang.String propertyName)
Retrieves the named custom property of the specified escalation
 instance using the escalation instance ID.

java.lang.String
getCustomProperty(ESTID estid,
                 java.lang.String propertyName)
Retrieves the named custom property of the specified escalation
 template using the escalation template ID.

java.lang.String
getCustomProperty(java.lang.String identifier,
                 java.lang.String propertyName)
Retrieves the named custom property of the specified
 task instance, task template, escalation instance, or escalation template
 using a string representation of the object ID.

java.lang.String
getCustomProperty(TKIID tkiid,
                 java.lang.String propertyName)
Retrieves the named custom property of the specified task
 instance using the task instance ID.

java.lang.String
getCustomProperty(TKTID tktid,
                 java.lang.String propertyName)
Retrieves the named custom property of the specified task
 template using the task template ID.

java.util.List
getCustomPropertyInfo(int objectType,
                     java.lang.String nameFilter,
                     java.lang.Integer threshold)
Retrieves information about custom properties of the specified object types.

java.util.List
getCustomPropertyNames(ESIID esiid)
Retrieves the names of all custom properties of the specified
 escalation instance using the escalation instance ID.

java.util.List
getCustomPropertyNames(ESTID estid)
Retrieves the names of all custom properties of the specified
 escalation template using the escalation template ID.

java.util.List
getCustomPropertyNames(java.lang.String identifier)
Retrieves the names of all custom properties of the specified
 task instance, task template, escalation instance, or escalation template
 using a string representation of the object ID.

java.util.List
getCustomPropertyNames(TKIID tkiid)
Retrieves the names of all custom properties of the specified
 task instance using the task instance ID.

java.util.List
getCustomPropertyNames(TKTID tktid)
Retrieves the names of all custom properties of the specified
 task template using the task template ID.

java.lang.String
getDocumentation(ESIID esiid,
                java.util.Locale locale)
Retrieves the documentation of the specified escalation instance
 using the escalation instance ID.

java.lang.String
getDocumentation(ESTID estid,
                java.util.Locale locale)
Retrieves the documentation of the specified escalation template
 using the escalation template ID.

java.lang.String
getDocumentation(java.lang.String identifier,
                java.util.Locale locale)
Retrieves the documentation of the specified object
 using a string representation of the object ID.

java.lang.String
getDocumentation(TKIID tkiid,
                java.util.Locale locale)
Retrieves the documentation of the specified task instance
 using the task instance ID.

java.lang.String
getDocumentation(TKTID tktid,
                java.util.Locale locale)
Retrieves the documentation of the specified task template
 using the task template ID.

Escalation
getEscalation(ESIID esiid)
Retrieves the specified escalation instance using the escalation instance ID.

Escalation
getEscalation(java.lang.String esiid)
Retrieves the specified escalation instance using a string representation of
 the escalation instance ID.

Escalation
getEscalation(java.lang.String tkiid,
             java.lang.String escalationName)
Retrieves the specified escalation instance using a string representation of
 the associated task instance ID and the escalation name.

Escalation
getEscalation(TKIID tkiid,
             java.lang.String escalationName)
Retrieves the specified escalation instance using
 the associated task instance ID and the escalation name.

EscalationInfo
getEscalationInfo(java.lang.String tkiid)
Retrieves information about all escalations of the specified task instance using
 a string representation of the task instance ID.

EscalationInfo
getEscalationInfo(TKIID tkiid)
Retrieves information about all escalations of the specified task instance using
 the task instance ID.

EscalationTemplate
getEscalationTemplate(ESTID estid)
Retrieves the specified escalation template using the escalation template ID.

EscalationTemplate
getEscalationTemplate(java.lang.String estid)
Retrieves the specified escalation template using
  a string representation of the escalation template ID.

ClientObjectWrapper
getFaultMessage(java.lang.String tkiid)
Retrieves the fault message of the specified task instance using
 a string representation of the task instance ID.

ClientObjectWrapper
getFaultMessage(TKIID tkiid)
Retrieves the fault message of the specified task instance
 using the task instance ID.

java.util.List
getFaultNames(java.lang.String identifier)
Retrieves the fault names defined for the specified task instance or template
 using a string representation of the task instance or template ID.

java.util.List
getFaultNames(TKIID tkiid)
Retrieves the fault names defined for the specified task instance
 using the task instance ID.

java.util.List
getFaultNames(TKTID tktid)
Retrieves the fault names defined for the specified task template
 using the task template ID.

java.util.List
getGroupDetails(java.lang.String[] groupNames,
               java.lang.String[] groupProperties,
               java.lang.String[] userProperties,
               java.lang.String[] subGroupProperties,
               java.lang.Integer threshold)
Returns details about the specified groups.

java.lang.String[]
getGroupNames()
Returns the names of groups the logged-on user is part of.

HtmConfiguration
getHtmConfiguration()
Returns configuration settings of the Human Task Manager.

InlineCustomProperty
getInlineCustomProperty(java.lang.String identifier,
                       java.lang.String propertyName)
Retrieves the named inline custom property of the specified task template
 or task instance using string representations of the object IDs.

InlineCustomProperty
getInlineCustomProperty(TKIID tkiid,
                       java.lang.String propertyName)
Retrieves the named inline custom property of the specified task instance using the task instance ID.

InlineCustomProperty
getInlineCustomProperty(TKTID tktid,
                       java.lang.String propertyName)
Retrieves the named inline custom property of the specified task template using the task template ID.

ClientObjectWrapper
getInputMessage(java.lang.String tkiid)
Retrieves the input message of the specified task instance using a
 string representation of the task instance ID.

ClientObjectWrapper
getInputMessage(TKIID tkiid)
Retrieves the input message of the task instance using the task instance ID.

java.lang.String
getMessageTextOfException(java.util.Locale locale,
                         java.lang.String messageKey,
                         java.lang.Object[] variableValues)
Retrieves the message text associated to the specified message key and locale.

int
getOperationMode()
Indicates whether the Human Task Manager database is used as an archive.

ClientObjectWrapper
getOutputMessage(java.lang.String tkiid)
Retrieves the output message of the specified task instance
 using a string representation of the ID.

ClientObjectWrapper
getOutputMessage(TKIID tkiid)
Retrieves the output message of the specified task instance
 using the task instance ID.

PIID
getProcessID(java.lang.String tkiid)
Retrieves the object ID of the BPEL process instance that contains the specified
 task instance using a string representation of the task instance ID.

PIID
getProcessID(TKIID tkiid)
Retrieves the object ID of the BPEL process instance that contains the specified
 task instance using the task instance ID.

QueryTableMetaData
getQueryTableMetaData(java.lang.String queryTableName,
                     java.util.Locale locale)
Returns the meta data of the specified query table.

StoredQuery
getStoredQuery(int kind,
              java.lang.String storedQueryName)
Retrieves the specified private or public stored query definition.

StoredQuery
getStoredQuery(java.lang.String storedQueryName)
Retrieves the specified stored query definition.

StoredQuery
getStoredQuery(java.lang.String userID,
              java.lang.String storedQueryName)
Retrieves the specified stored query definition for the specified user.

java.lang.String[]
getStoredQueryNames()
Retrieves the names of stored queries that are persistently stored in the database.

java.lang.String[]
getStoredQueryNames(int kind)
Retrieves the names of private or public stored queries that are persistently stored in the database.

java.lang.String[]
getStoredQueryNames(java.lang.String userID)
Retrieves the names of stored queries that are persistently stored in the database
 for the specified user.

java.util.List
getSubstitutes()
Deprecated. 
As of version 7.0, replaced by getUserSubstitutionDetail.
 

java.util.List
getSubstitutes(java.lang.String userID)
Deprecated. 
As of version 7.0, replaced by getUserSubstitutionDetail.

java.util.List
getSubTaskIDs(java.lang.String tkiid)
Retrieves the object IDs of all task instances that are subtasks of the
 specified task instance using a string representation of the task instance ID.

java.util.List
getSubTaskIDs(TKIID tkiid)
Retrieves the object IDs of all task instances that are subtasks of the
 specified task instance using the task instance ID.

Task
getTask(java.lang.String tkiid)
Retrieves the specified task instance using a string
 representation of the task instance ID.

Task
getTask(TKIID tkiid)
Retrieves the specified task instance using the task instance ID.

Task
getTaskAndMarkRead(java.lang.String tkiid)
Retrieves the specified task instance using a string
 representation of the task instance ID and marks the task as read.

Task
getTaskAndMarkRead(TKIID tkiid)
Retrieves the specified task instance using the task instance ID
 and marks the task as read.

java.util.List
getTaskHistory(java.lang.String tkiid)
Retrieves the history events associated to the specified task instance
 using a string representation of the task instance ID.

java.util.List
getTaskHistory(TKIID tkiid)
Retrieves the history events associated to the specified task instance
 using the task instance ID.

boolean
getTaskRead(java.lang.String tkiid)
States whether the specified task instance is marked read using
  a string representation of the task instance ID.

boolean
getTaskRead(TKIID tkiid)
States whether the specified task instance is marked read using
  the task instance ID.

TaskTemplate
getTaskTemplate(java.lang.String tktid)
Retrieves the specified task template using a string representation of
 the task template ID.

TaskTemplate
getTaskTemplate(TKTID tktid)
Retrieves the specified task template using the task template ID.

CustomClientSettings
getUISettings(java.lang.String identifier)
Retrieves client interface settings for the specified task instance or template
 using a string representation of the object ID.

CustomClientSettings
getUISettings(TKIID tkiid)
Retrieves client interface settings for the specified task instance
 using the task instance ID.

CustomClientSettings
getUISettings(TKTID tktid)
Retrieves client interface settings for the specified task template
 using the task template ID.

java.util.List
getUserDetails(java.lang.String[] userIDs,
              java.lang.String[] userProperties)
Retrieves details about the specified users.

StaffResultSet
getUsersInRole(java.lang.String identifier,
              int role)
Retrieves the users that are members of the specified role for the
 specified task instance or template using a string representation of the task instance or template ID.

StaffResultSet
getUsersInRole(TKIID tkiid,
              int role)
Retrieves the users that are members of the specified role for the
 specified task using the task instance ID.

StaffResultSet
getUsersInRole(TKTID tktid,
              int role)
Retrieves the users that are members of the specified role for the
 specified task template using the task template ID.

UserSubstitutionDetail
getUserSubstitutionDetail()
Retrieves absence and substitution details about the logged-on user.

UserSubstitutionDetail
getUserSubstitutionDetail(java.lang.String userID)
Retrieves absence and substitution details about the specified user.

WorkItem[]
getWorkItems(ESIID esiid)
Returns the work item assignments for the logged-on user and the
  specified escalation instance using the escalation instance ID.

WorkItem[]
getWorkItems(java.lang.String identifier)
Returns the work item assignments for the logged-on user and the
  specified task or escalation instance using a string representation of the task or escalation instance ID.

WorkItem[]
getWorkItems(TKIID tkiid)
Returns the work item assignments for the logged-on user and the
  specified task instance using the task instance ID.

boolean
isSystemAdministrator()
States whether the logged-on user is a system administrator
    for the Human Task Manager component.

boolean
isSystemMonitor()
States whether the logged-on user is a task system monitor
    for the Human Task Manager component.

boolean
isUserInRole(java.lang.String identifier,
            java.lang.String userID,
            int role)
States whether the specified user is a member of the specified role for the
   specified task instance or template using a string representation of the task instance or template ID.

boolean
isUserInRole(TKIID tkiid,
            java.lang.String userID,
            int role)
States whether the specified user is a member of the specified role for the
   specified task instance using the task instance ID.

boolean
isUserInRole(TKTID tktid,
            java.lang.String userID,
            int role)
States whether the specified user is a member of the specified role for the
   specified task template using the task template ID.

QueryResultSet
query(int kind,
     java.lang.String storedQueryName,
     java.lang.Integer skipTuples,
     java.lang.Integer threshold,
     java.util.List parameters)
Performs the specified public or private stored query.

QueryResultSet
query(java.lang.String storedQueryName,
     java.lang.Integer skipTuples)
Deprecated. 
As of version 6.0.2, replaced by query(Sting storedQueryName, Integer skipTuples, List parameters),

QueryResultSet
query(java.lang.String storedQueryName,
     java.lang.Integer skipTuples,
     java.lang.Integer threshold)
Deprecated. 
As of version 6.0.2, replaced by query(Sting storedQueryName, Integer skipTuples, Integer threshold, List parameters),

QueryResultSet
query(java.lang.String storedQueryName,
     java.lang.Integer skipTuples,
     java.lang.Integer threshold,
     java.util.List parameters)
Performs the specified stored query and specifies values for parameters in the where-clause.

QueryResultSet
query(java.lang.String storedQueryName,
     java.lang.Integer skipTuples,
     java.util.List parameters)
Performs the specified stored query, specifies values for the parameters in the
 where-clause, and returns the qualifying object properties.

QueryResultSet
query(java.lang.String userID,
     java.lang.String storedQueryName,
     java.lang.Integer skipTuples,
     java.lang.Integer threshold,
     java.util.List parameters)
Performs the specified private stored query of the specified user.

QueryResultSet
query(java.lang.String selectClause,
     java.lang.String whereClause,
     java.lang.String orderByClause,
     java.lang.Integer skipTuples,
     java.lang.Integer threshold,
     java.util.TimeZone timeZone)
Retrieves selected object properties persistently stored in the database
 and allows for retrieving a specified set of data only.

QueryResultSet
query(java.lang.String selectClause,
     java.lang.String whereClause,
     java.lang.String orderByClause,
     java.lang.Integer threshold,
     java.util.TimeZone timeZone)
Retrieves selected object properties persistently stored in the database.

QueryResultSet
queryAll(java.lang.String selectClause,
        java.lang.String whereClause,
        java.lang.String orderByClause,
        java.lang.Integer skipTuples,
        java.lang.Integer threshold,
        java.util.TimeZone timeZone)
Retrieves selected object properties of all objects persistently stored in the database
 and allows for retrieving a specified set of data only.

EntityResultSet
queryEntities(java.lang.String queryTableName,
             FilterOptions filterOptions,
             AuthorizationOptions authorizationOptions,
             java.util.List parameters)
Queries entities using the specified query table.

int
queryEntityCount(java.lang.String queryTableName,
                FilterOptions filterOptions,
                AuthorizationOptions authorizationOptions,
                java.util.List parameters)
Counts qualifying entities of a potential query for entities.

int
queryRowCount(java.lang.String queryTableName,
             FilterOptions filterOptions,
             AuthorizationOptions authorizationOptions,
             java.util.List parameters)
Counts qualifying objects of a potential query table query.

RowResultSet
queryRows(java.lang.String queryTableName,
         FilterOptions filterOptions,
         AuthorizationOptions authorizationOptions,
         java.util.List parameters)
Queries attributes using the specified query table.

TaskTemplate[]
queryTaskTemplates(java.lang.String whereClause,
                  java.lang.String orderByClause,
                  java.lang.Integer threshold,
                  java.util.TimeZone timeZone)
Retrieves task templates that are persistently stored in the database.

StaffResultSet
resolveStaffQuery(java.lang.String parameterizedPeopleAssignmentCriteria,
                 java.lang.String jndiNameOfStaffPluginProvider,
                 int substitutionPolicy,
                 java.util.Map contextVariables)
Tentatively resolves the specified people assignment criteria and returns the qualifying users or groups.

void
restart(java.lang.String tkiid,
       ClientObjectWrapper input,
       boolean keepResultMessages)
Restarts the specified task instance
 using a string representation of the task instance ID.

void
restart(TKIID tkiid,
       ClientObjectWrapper input,
       boolean keepResultMessages)
Restarts the specified task instance
 using the task instance ID.

void
resume(java.lang.String tkiid)
Resumes the execution of the specified suspended collaboration or to-do
 task instance using a string representation of the task instance ID.

void
resume(TKIID tkiid)
Resumes the execution of the specified suspended collaboration or to-do
 task instance using the task instance ID.

java.util.List
searchGroupDetails(java.lang.String searchCondition,
                  java.lang.String[] groupProperties,
                  java.lang.String[] userProperties,
                  java.lang.String[] subGroupProperties,
                  java.lang.Integer threshold)
Returns details about the groups searched for.

java.util.List
searchUserDetails(java.lang.String searchCondition,
                 java.lang.String[] userProperties,
                 java.lang.Integer threshold)
Returns details about the users searched for.

void
setAbsence(boolean absence)
Deprecated. 
As of version 7.0, replaced by setUserSubstitutionDetail.

void
setAbsence(java.lang.String userID,
          boolean absence)
Deprecated. 
As of version 7.0, replaced by setUserSubstitutionDetail.

void
setBinaryCustomProperty(ESIID esiid,
                       BinaryCustomProperty property)
Stores custom-specific binary values for the specified escalation instance using
 the escalation instance ID.

void
setBinaryCustomProperty(java.lang.String identifier,
                       BinaryCustomProperty property)
Stores custom-specific binary values for the specified task or escalation instance
 using a string representation of the task or escalation instance ID.

void
setBinaryCustomProperty(TKIID tkiid,
                       BinaryCustomProperty property)
Stores custom-specific binary values for the specified task instance using
 the task instance ID.

void
setCustomProperties(java.lang.String tkiid,
                   java.util.List customProperties)
Stores custom-specific values for the specified task instance using
 a string representation of the task instance ID.

void
setCustomProperties(TKIID tkiid,
                   java.util.List customProperties)
Stores custom-specific values for the specified task instance using
 the task instance ID.

void
setCustomProperty(ESIID esiid,
                 java.lang.String propertyName,
                 java.lang.String propertyValue)
Stores custom-specific values for the specified escalation instance.

java.util.List
setCustomProperty(java.lang.String[] tkiids,
                 java.lang.String propertyName,
                 java.lang.String propertyValue)
Stores custom-specific values for the specified task instances using
 string representations of the task instance IDs.

void
setCustomProperty(java.lang.String identifier,
                 java.lang.String propertyName,
                 java.lang.String propertyValue)
Stores custom-specific values for the specified task or escalation instance
 using a string representation of the object ID.

java.util.List
setCustomProperty(TKIID[] tkiids,
                 java.lang.String propertyName,
                 java.lang.String propertyValue)
Stores custom-specific values for the specified task instances using
 task instance IDs.

void
setCustomProperty(TKIID tkiid,
                 java.lang.String propertyName,
                 java.lang.String propertyValue)
Stores custom-specific values for the specified task instance.

void
setFaultMessage(java.lang.String tkiid,
               java.lang.String faultName,
               ClientObjectWrapper faultMessage)
Stores the specified fault message for the specified task instance into the
 database using a string representation of the task instance ID.

void
setFaultMessage(TKIID tkiid,
               java.lang.String faultName,
               ClientObjectWrapper faultMessage)
Stores the specified fault message for the specified task instance into the
 database using the task instance ID.

void
setInlineCustomProperties(java.lang.String tkiid,
                         java.util.List customProperties)
Stores custom-specific values for the specified task instance using
 a string representation of the task instance ID.

void
setInlineCustomProperties(TKIID tkiid,
                         java.util.List customProperties)
Stores custom-specific values for the specified task instance using
 the task instance ID.

java.util.List
setInlineCustomProperty(java.lang.String[] tkiids,
                       InlineCustomProperty property)
Stores a custom-specific value for the specified task instances using
 string representations of the task instance IDs.

void
setInlineCustomProperty(java.lang.String tkiid,
                       InlineCustomProperty property)
Stores a custom-specific value for the specified task instance
 using a string representation of the task instance ID.

java.util.List
setInlineCustomProperty(TKIID[] tkiids,
                       InlineCustomProperty property)
Stores a custom-specific value for the specified task instances using
 task instance IDs.

void
setInlineCustomProperty(TKIID tkiid,
                       InlineCustomProperty property)
Stores a custom specific value for the specified task instance using the task instance ID.

void
setInputMessage(java.lang.String tkiid,
               ClientObjectWrapper inputMessage)
Stores the input message of the specified task instance into the database
 using a string representation of the task instance ID.

void
setInputMessage(TKIID tkiid,
               ClientObjectWrapper inputMessage)
Stores the input message of the specified task instance into the database
 using the task instance ID.

void
setOutputMessage(java.lang.String tkiid,
                ClientObjectWrapper outputMessage)
Stores the output message of the specified task instance into the database
 using a string representation of the task instance ID.

void
setOutputMessage(TKIID tkiid,
                ClientObjectWrapper outputMessage)
Stores the output message of the specified task instance into the database
 using the task instance ID.

void
setSubstitutes(java.util.List substitutes)
Deprecated. 
As of version 7.0, replaced by setUserSubstitutionDetail.

void
setSubstitutes(java.lang.String userID,
              java.util.List substitutes)
Deprecated. 
As of version 7.0, replaced by setUserSubstitutionDetail.

void
setTaskRead(java.lang.String tkiid,
           boolean newValue)
Specifies whether the specified task instance is to be marked as read using
  a string representation of the task instance ID.

void
setTaskRead(TKIID tkiid,
           boolean newValue)
Specifies whether the specified task instance is to be marked as read using
  the task instance ID.

void
setUserSubstitutionDetail(java.lang.String userID,
                         UserSubstitutionDetail substitutionDetail)
Sets absence and substitution details for the specified user.

void
setUserSubstitutionDetail(UserSubstitutionDetail substitutionDetail)
Sets absence and substitution details for the logged-on user.

void
startTask(java.lang.String tkiid,
         ClientObjectWrapper input,
         ReplyHandlerWrapper replyHandler)
Asynchronously executes a previously created task
 using a string representation of the task instance ID.

void
startTask(TKIID tkiid,
         ClientObjectWrapper input,
         ReplyHandlerWrapper replyHandler)
Asynchronously executes a previously created task
 using the task instance ID.

void
startTaskAsSubTask(java.lang.String tkiid,
                  java.lang.String parentTaskID,
                  ClientObjectWrapper input)
Executes a previously created task as a subtask of the specified parent task instance
 using a string representation of the task instance ID.

void
startTaskAsSubTask(TKIID tkiid,
                  TKIID parentTaskID,
                  ClientObjectWrapper input)
Executes a previously created task as a subtask of the specified parent
 task instance using the task instance ID.

void
startTaskTemplate(java.lang.String tktid)
This method starts a task template that has been created at Runtime
 using a string representation of the task template ID.

void
startTaskTemplate(TKTID tktid)
This method starts a task template that has been created at Runtime
 using the task template ID.

void
stopTaskTemplate(java.lang.String tktid)
This method stops a task template that has been created at Runtime
 using a string representation of the task template ID.

void
stopTaskTemplate(TKTID tktid)
This method stops a task template that has been created at Runtime
 using the task template ID.

void
suspend(java.lang.String tkiid)
Suspends the specified collaboration or to-do task instance
 using a string representation of the task instance ID.

void
suspend(java.lang.String tkiid,
       java.util.Calendar deadline)
Suspends the specified collaboration or to-do task instance
 until the specified point in time is reached using a string representation of the task instance ID.

void
suspend(java.lang.String tkiid,
       int duration)
Suspends the specified collaboration or to-do task instance for the specified
 number of seconds using a string representation of the task instance ID.

void
suspend(java.lang.String tkiid,
       java.lang.String duration)
Suspends the specified collaboration or to-do task instance for the specified
 duration using a string representation of the task instance ID.

void
suspend(TKIID tkiid)
Suspends the specified collaboration or to-do task instance
 using the task instance ID.

void
suspend(TKIID tkiid,
       java.util.Calendar deadline)
Suspends the specified collaboration or to-do task instance
 until the specified point in time is reached using the task instance ID.

void
suspend(TKIID tkiid,
       int duration)
Suspends the specified collaboration or to-do task instance for the specified
 number of seconds using the task instance ID.

void
suspend(TKIID tkiid,
       java.lang.String duration)
Suspends the specified collaboration or to-do task instance for the specified
 duration using the task instance ID.

void
suspendAndCancelClaim(java.lang.String tkiid,
                     java.util.Calendar deadline,
                     boolean keepTaskData)
Suspends the specified collaboration or to-do task instance
 until the specified point in time is reached,
 and cancels the claim of the task instance when execution is resumed
 using a string representation of the task instance ID.

void
suspendAndCancelClaim(java.lang.String tkiid,
                     int duration,
                     boolean keepTaskData)
Suspends the specified collaboration or to-do task instance for the specified
 number of seconds and cancels the claim of the task instance when execution is resumed
 using a string representation of the task instance ID.

void
suspendAndCancelClaim(java.lang.String tkiid,
                     java.lang.String duration,
                     boolean keepTaskData)
Suspends the specified collaboration or to-do task instance for the specified
 duration and cancels the claim of the task instance when execution is resumed
 using a string representation of the task instance ID.

void
suspendAndCancelClaim(TKIID tkiid,
                     java.util.Calendar deadline,
                     boolean keepTaskData)
Suspends the specified collaboration or to-do task instance
 until the specified point in time is reached,
 and cancels the claim of the task instance when execution is resumed
 using the task instance ID.

void
suspendAndCancelClaim(TKIID tkiid,
                     int duration,
                     boolean keepTaskData)
Suspends the specified collaboration or to-do task instance for the specified
 number of seconds and cancels the claim of the task instance when execution is resumed
 using the task instance ID.

void
suspendAndCancelClaim(TKIID tkiid,
                     java.lang.String duration,
                     boolean keepTaskData)
Suspends the specified collaboration or to-do task instance for the specified
 duration and cancels the claim of the task instance when execution is resumed
 using the task instance ID.

void
terminate(java.lang.String tkiid)
Terminates the specified task instance using
 a string representation of the task instance ID.

void
terminate(TKIID tkiid)
Terminates the specified task instance using the task instance ID.

java.util.List
transferToWorkBasket(java.lang.String[] tkiids,
                    java.lang.String workBasketName)
Transfers the specified task instances to the specified work basket using
 string representations of the task instance IDs.

java.util.List
transferToWorkBasket(TKIID[] tkiids,
                    java.lang.String workBasketName)
Transfers the specified task instances to the specified work basket using
 task instance IDs.

java.util.List
transferWorkItem(ESIID[] esiids,
                int assignmentReason,
                java.lang.String fromOwner,
                java.lang.String toOwner)
Transfers the specified work items for the specified escalation instances
 using escalation instance IDs.

void
transferWorkItem(ESIID esiid,
                int assignmentReason,
                java.lang.String fromOwner,
                java.lang.String toOwner)
Transfers the specified work item for the specified escalation instance
 using the escalation instance ID.

java.util.List
transferWorkItem(java.lang.String[] identifiers,
                int assignmentReason,
                java.lang.String fromOwner,
                java.lang.String toOwner)
Transfers the specified work items for the specified escalation or task instances
 using string representations of escalation or task instance IDs.

void
transferWorkItem(java.lang.String identifier,
                int assignmentReason,
                java.lang.String fromOwner,
                java.lang.String toOwner)
Transfers the specified work item using a string representation
 of the task or escalation instance ID.

java.util.List
transferWorkItem(TKIID[] tkiids,
                int assignmentReason,
                java.lang.String fromOwner,
                java.lang.String toOwner)
Transfers the specified work items for the specified task instances using
 task instance IDs.

void
transferWorkItem(TKIID tkiid,
                int assignmentReason,
                java.lang.String fromOwner,
                java.lang.String toOwner)
Transfers the specified work item for the specified task instance
 using the task instance ID.

void
triggerEscalation(ESIID esiid)
Manually triggers the specified escalation instance
 using the escalation instance ID.

void
triggerEscalation(java.lang.String esiid)
Manually triggers the specified escalation instance
 using a string representation of the escalation instance ID.

void
update(Escalation escalation)
Updates a persistently stored escalation instance.

void
update(java.lang.String tkiid,
      TaskModel taskModel,
      java.lang.String applicationName,
      java.lang.String parentContext,
      ClientObjectWrapper input)
Updates a task instance that has been created at Runtime
 using a string representation of the task instance ID.

void
update(Task task)
Updates a persistently stored task instance.

void
update(TKIID tkiid,
      TaskModel taskModel,
      java.lang.String applicationName,
      java.lang.String parentContext,
      ClientObjectWrapper input)
Updates a task instance that has been created at Runtime
 using the task instance ID.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - bulkTransferWorkItem java.util.List bulkTransferWorkItem(java.lang.String[] identifiers, int assignmentReason, java.lang.String fromOwner, java.lang.String toOwner) throws ArchiveUnsupportedOperationException , IdWrongFormatException , IdWrongTypeException , InvalidAssignmentReasonException , ParameterNullException , UserDoesNotExistException , WorkItemManagerException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Transfers the specified work items for the specified escalation or task instances using escalation or task instance IDs - each transfer operation is executed in a transaction on its own. This method is particularly suitable in cases where processing large numbers of tasks or escalations is required, and where the application is not concerned that the transfer happens as part of an enclosing global transaction. When work items of a task instance are transferred, then the caller must be an owner, starter, originator, or administrator of the task instances. The task can be escalated. suspended, or waiting for subtasks. When work items of an escalation instance are transferred, then the caller must be an administrator of the associated task instances. Escalation-receiver work items can be transferred when the task is escalated, that is, the escalation is in the escalated state. The following specific rules apply for the transfer of work items: This method is not supported in archive mode. Parameters: identifiers - An array of escalation instance or task instance IDs that are used to identify the work items to be transferred. assignmentReason - The reason why the work item is assigned - refer to the work item assignment reasons . fromOwner - The user ID or the name of the group the work item currently belongs to. toOwner - The user ID or the name of the group the work item is to be transferred to. Work items can be transferred from a user to a user or from a group of users to a group of users. If a user work item is transferred, it is checked whether the user transferred to exists but the check may be executed case insensitively. The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments' custom property of the Human Task Manager configuration to 'true'. Returns: List - A list of TaskResult objects, one for every transfer operation that failed. Refer to TaskResult to view the TaskResult properties. Returns an empty list when all transfers executed successfully. Throws: ArchiveUnsupportedOperationException IdWrongFormatException IdWrongTypeException InvalidAssignmentReasonException ParameterNullException UserDoesNotExistException WorkItemManagerException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.1 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### bulkTransferWorkItem

```
java.util.List bulkTransferWorkItem(java.lang.String[] identifiers,
                                  int assignmentReason,
                                  java.lang.String fromOwner,
                                  java.lang.String toOwner)
                                    throws ArchiveUnsupportedOperationException,
                                           IdWrongFormatException,
                                           IdWrongTypeException,
                                           InvalidAssignmentReasonException,
                                           ParameterNullException,
                                           UserDoesNotExistException,
                                           WorkItemManagerException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
```

This method is particularly suitable in cases where processing large numbers of tasks or escalations
 is required, and where the application is not concerned that the transfer happens
 as part of an enclosing global transaction.
 
 When work items of a task instance are transferred, then
 the caller must be an owner, starter, originator, or administrator of the task instances.
 The task can be escalated. suspended, or waiting for subtasks.
 
 When work items of an escalation instance are transferred, then
 the caller must be an administrator of the associated task instances.
 Escalation-receiver work items can be transferred
 when the task is escalated, that is, the escalation is in the escalated state.
 
 The following specific rules apply for the transfer of work items:
 
Work items assigned to "everybody" cannot be transferred.
 The owner of a task instance can transfer the "owner" work item to a potential owner
 or an administrator of the task instance.
 The starter of a task instance can transfer the "starter" work item to a potential starter
 or an administrator of the task instance.
 A "starter" work item can be transferred in the expired, terminated, finished, failed, and running state.
 The originator of a task instance can transfer the "originator" work item to a potential instance creator
 or an administrator of the task instance.
 The originator of a task instance can transfer a "potential starter" work item to any person.
 A "potential starter" work item can be transferred in the inactive state.
 The administrator of a task instance can transfer all work items to any person.
 A "starter" work item can be transferred in the expired, terminated, finished, failed, and running state.
 A "potential starter" work item can be transferred in the inactive state.
 A "reader" or "administrator" work item can be transferred in all but the inactive state.
 A "potential owner" or "editor" work item can be transferred in the ready or claimed state.
 An "escalation receiver" work item can be transferred in the ready, running, or claimed state.
 

 This method is not supported in archive mode.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- bulkTransferWorkItem
java.util.List bulkTransferWorkItem(ESIID[] esiids,
                                  int assignmentReason,
                                  java.lang.String fromOwner,
                                  java.lang.String toOwner)
                                    throws ArchiveUnsupportedOperationException,
                                           IdWrongFormatException,
                                           InvalidAssignmentReasonException,
                                           ParameterNullException,
                                           UserDoesNotExistException,
                                           WorkItemManagerException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Transfers the specified work items for the specified escalation instances
 using escalation instance IDs - each transfer operation is executed in a transaction on its own.
 
 This method is particularly suitable in cases where processing large numbers of escalations
 is required, and where the application is not concerned that the transfer happens
 as part of an enclosing global transaction.
 
 The caller must be an administrator of the associated task instances.
 Escalation-receiver work items can be transferred
 when the task is escalated, that is, the escalation is in the escalated state.
 An e-mail is not sent to the user or group that receives the transferred work item.
 
 This method is not supported in archive mode.
Parameters:esiids - Array of escalation instance IDs that are used to identify
 the work items to be transferred.assignmentReason - The reason why the work item is assigned - refer to
     the work item assignment reasons.fromOwner - The user ID or the name of the group the work item currently belongs to.toOwner - The user ID or the name of the group the work item is to be transferred to.
    Work items can be transferred from a user to a user or from a group of users to a group of users.
    If a user work item is transferred, it is checked whether the user transferred to
    exists but the check may be executed case insensitively.
    The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments'
    custom property of the Human Task Manager configuration to 'true'.
 
Returns:List -
    A list of EscalationResult objects, one for every transfer operation that failed.
 Refer to
 EscalationResult  to view the EscalationResult properties.
 Returns an empty list when all transfers executed successfully.
 
Throws:
ArchiveUnsupportedOperationException
IdWrongFormatException
InvalidAssignmentReasonException
ParameterNullException
UserDoesNotExistException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- bulkTransferWorkItem java.util.List bulkTransferWorkItem(TKIID [] tkiids, int assignmentReason, java.lang.String fromOwner, java.lang.String toOwner) throws ArchiveUnsupportedOperationException , IdWrongFormatException , InvalidAssignmentReasonException , ParameterNullException , UserDoesNotExistException , WorkItemManagerException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Transfers the specified work items for the specified task instances using task instance IDs - each transfer operation is executed in a transaction on its own. This method is particularly suitable in cases where processing large numbers of tasks is required, and where the application is not concerned that the transfer happens as part of an enclosing global transaction. The caller must be an owner, starter, originator, or administrator of the task instances. The task can be escalated. suspended, or waiting for subtasks. The following specific rules apply for the transfer of work items: This method is not supported in archive mode. Parameters: tkiids - An array of task instance IDs that are used to identify the work items to be transferred. assignmentReason - The reason why the work item is assigned - refer to the work item assignment reasons . fromOwner - The user ID or the name of the group the work item currently belongs to. toOwner - The user ID or the name of the group the work item is to be transferred to. Work items can be transferred from a user to a user or from a group of users to a group of users. If a user work item is transferred, it is checked whether the user transferred to exists but the check may be executed case insensitively. The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments' custom property of the Human Task Manager configuration to 'true'. Returns: List - A list of TaskResult objects, one for every transfer operation that failed. Refer to TaskResult to view the TaskResult properties. Returns an empty list when all transfers executed successfully. Throws: ArchiveUnsupportedOperationException IdWrongFormatException InvalidAssignmentReasonException ParameterNullException UserDoesNotExistException WorkItemManagerException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.1 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### bulkTransferWorkItem

```
java.util.List bulkTransferWorkItem(TKIID[] tkiids,
                                  int assignmentReason,
                                  java.lang.String fromOwner,
                                  java.lang.String toOwner)
                                    throws ArchiveUnsupportedOperationException,
                                           IdWrongFormatException,
                                           InvalidAssignmentReasonException,
                                           ParameterNullException,
                                           UserDoesNotExistException,
                                           WorkItemManagerException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
```

This method is particularly suitable in cases where processing large numbers of tasks
 is required, and where the application is not concerned that the transfer happens
 as part of an enclosing global transaction.
 
 The caller must be an owner, starter, originator, or administrator of the task instances.
 The task can be escalated. suspended, or waiting for subtasks.
 
 The following specific rules apply for the transfer of work items:
 
Work items assigned to "everybody" cannot be transferred.
 The owner of a task instance can transfer the "owner" work item to a potential owner
 or an administrator of the task instance.
 The starter of a task instance can transfer the "starter" work item to a potential starter
 or an administrator of the task instance.
 A "starter" work item can be transferred in the expired, terminated, finished, failed, and running state.
 The originator of a task instance can transfer the "originator" work item to a potential instance creator
 or an administrator of the task instance.
 The originator of a task instance can transfer a "potential starter" work item to any person.
 A "potential starter" work item can be transferred in the inactive state.
 The administrator of a task instance can transfer all work items to any person.
 A "starter" work item can be transferred in the expired, terminated, finished, failed, and running state.
 A "potential starter" work item can be transferred in the inactive state.
 A "reader" or "administrator" work item can be transferred in all but the inactive state.
 A "potential owner" or "editor" work item can be transferred in the ready or claimed state.
 

 This method is not supported in archive mode.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- callTask
ClientObjectWrapper callTask(java.lang.String tkiid,
                           ClientObjectWrapper input)
                             throws ArchiveUnsupportedOperationException,
                                    AdministratorCannotBeResolvedException,
                                    ApplicationVetoException,
                                    CannotCreateWorkItemException,
                                    FaultReplyException,
                                    IdWrongFormatException,
                                    IdWrongTypeException,
                                    InvalidLengthException,
                                    NotAuthorizedException,
                                    ObjectDoesNotExistException,
                                    SCAServiceAccessFailureException,
                                    SCAServiceResultErrorException,
                                    SchedulingFailedException,
                                    WrongKindException,
                                    WrongMessageTypeException,
                                    WrongStateException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Synchronously executes a previously created invocation task instance
 using a string representation of the task instance ID. An input message
 can be passed to specify initial values for the task.
 
 An invocation task instance is also known as originating task instance.
 
 This method returns only when the execution of the task finishes with the result of
 execution. If a fault occurs, an exception is thrown. The service that is called must be
 a two-way operation. Otherwise, SCAServiceAccessFailureException is thrown.
 
 The task instance must be a stand-alone task in the inactive state.
 The caller must be a potential starter, the originator, or an administrator of the task instance.
 
 The action associated to this method is TaskActions.CALLTASK.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID that is used
    to identify the task instance.input - The input message.
    The object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:ClientObjectWrapper -
    The output message that denotes the result of execution.
 
Throws:
ArchiveUnsupportedOperationException
AdministratorCannotBeResolvedException
ApplicationVetoException
CannotCreateWorkItemException
FaultReplyException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- callTask
ClientObjectWrapper callTask(TKIID tkiid,
                           ClientObjectWrapper input)
                             throws ArchiveUnsupportedOperationException,
                                    AdministratorCannotBeResolvedException,
                                    ApplicationVetoException,
                                    CannotCreateWorkItemException,
                                    FaultReplyException,
                                    IdWrongFormatException,
                                    InvalidLengthException,
                                    NotAuthorizedException,
                                    ObjectDoesNotExistException,
                                    SCAServiceAccessFailureException,
                                    SCAServiceResultErrorException,
                                    SchedulingFailedException,
                                    WrongKindException,
                                    WrongMessageTypeException,
                                    WrongStateException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Synchronously executes a previously created invocation task instance
 using the task instance ID. An input message
 can be passed to specify initial values for the task.
 
 An invocation task instance is also known as originating task instance.
 
 This method returns only when the execution of the task finishes with the result of
 execution. If a fault occurs, an exception is thrown. The service that is called must be
 a two-way operation. Otherwise, SCAServiceAccessFailureException is thrown.
 
 The task instance must be a stand-alone task in the inactive state.
 The caller must be a potential starter, the originator, or an administrator of the task instance.
 
 The action associated to this method is TaskActions.CALLTASK.
 
 This method is not supported in archive mode.
Parameters:tkiid - The task instance ID that is used to identify the task instance.input - The input message.
    The object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:ClientObjectWrapper -
    The output message that denotes the result of execution.
 
Throws:
ArchiveUnsupportedOperationException
AdministratorCannotBeResolvedException
ApplicationVetoException
CannotCreateWorkItemException
FaultReplyException
IdWrongFormatException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- cancelClaim
void cancelClaim(java.lang.String tkiid)
                 throws ApplicationVetoException,
                        ArchiveUnsupportedOperationException,
                        IdWrongFormatException,
                        IdWrongTypeException,
                        NotAuthorizedException,
                        ObjectDoesNotExistException,
                        WrongKindException,
                        WrongStateException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Cancels the claim of a task instance using a string representation of the task instance ID.
 
 The task instance must have been claimed. It can be escalated.
 
 The task instance is returned to the ready state.
 Any previously stored output or fault message is deleted.
 
 The caller must be the owner or an administrator of the task instance.
 
 The action associated to this method is TaskActions.CANCELCLAIM.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID that is used
    to identify the task instance.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.0
 
 Throws an ApplicationFailedException when the application refuses to execute the method.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- cancelClaim
void cancelClaim(TKIID tkiid)
                 throws ApplicationVetoException,
                        ArchiveUnsupportedOperationException,
                        IdWrongFormatException,
                        NotAuthorizedException,
                        ObjectDoesNotExistException,
                        WrongKindException,
                        WrongStateException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Cancels the claim of a task instance using the task instance ID.
 
 The task instance must have been claimed. It can be escalated.
 
 The task instance is returned to the ready state.
 Any previously stored output or fault message is deleted.
 
 The caller must be the owner or an administrator of the task instance.
 
 The action associated to this method is TaskActions.CANCELCLAIM.
 
 This method is not supported in archive mode.
Parameters:tkiid - The task instance ID that is used to identify the task instance.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.0
 
 Throws an ApplicationFailedException when the application refuses to execute the method.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- cancelClaim
void cancelClaim(java.lang.String tkiid,
               boolean keepTaskData)
                 throws ApplicationVetoException,
                        ArchiveUnsupportedOperationException,
                        IdWrongFormatException,
                        IdWrongTypeException,
                        NotAuthorizedException,
                        ObjectDoesNotExistException,
                        WrongKindException,
                        WrongStateException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Cancels the claim of a task instance and keeps any data that has been set
 using a string representation of the task instance ID.
 
 The task instance must have been claimed. It can be escalated.
 
 The task instance is returned to the ready state.
 If specified, any previously stored output or fault message is kept.
 
 The caller must be the owner or an administrator of the task instance.
 
 The action associated to this method is TaskActions.CANCELCLAIM.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID that is used
    to identify the task instance.keepTaskData - Specifies whether data saved for the claimed task instance is to be kept.
    True states that any output or fault message set is to be kept.
    False states that any output or fault message set is to be deleted.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- cancelClaim
void cancelClaim(TKIID tkiid,
               boolean keepTaskData)
                 throws ApplicationVetoException,
                        ArchiveUnsupportedOperationException,
                        IdWrongFormatException,
                        NotAuthorizedException,
                        ObjectDoesNotExistException,
                        WrongKindException,
                        WrongStateException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Cancels the claim of a task instance and keeps any data that has been set
 using the task instance ID.
 
 The task instance must have been claimed. It can be escalated.
 
 The task instance is returned to the ready state.
 If specified, any previously stored output or fault message is kept.
 
 The caller must be the owner or an administrator of the task instance.
 
 The action associated to this method is TaskActions.CANCELCLAIM.
 
 This method is not supported in archive mode.
Parameters:tkiid - The task instance ID that is used to identify the task instance.keepTaskData - Specifies whether data saved for the claimed task instance is to be kept.
    True states that any output or fault message set is to be kept.
    False states that any output or fault message set is to be deleted.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- cancelClaim java.util.List cancelClaim(java.lang.String[] identifiers) throws ArchiveUnsupportedOperationException , IdWrongFormatException , IdWrongTypeException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Cancels the claim of the specified task instances using string representations of the task instance IDs. The task instances must have been claimed. They can be escalated. The task instances are returned to the ready state. Any previously stored output or fault message is deleted. The caller must be the owner or an administrator of the task instances. The action associated to this method is TaskActions.CANCELCLAIM . This method is not supported in archive mode. Parameters: identifiers - An array of task instance IDs that are used to identify the task instances to be released. Returns: List - A list of TaskResult objects, one for every task instance specified. Refer to TaskResult . If a single cancelClaim operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all cancelClaim operations are undone. Throws: ArchiveUnsupportedOperationException IdWrongFormatException IdWrongTypeException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.1 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### cancelClaim

```
java.util.List cancelClaim(java.lang.String[] identifiers)
                           throws ArchiveUnsupportedOperationException,
                                  IdWrongFormatException,
                                  IdWrongTypeException,
                                  UnexpectedFailureException,
                                  java.rmi.RemoteException,
                                  javax.ejb.EJBException
```

The task instances must have been claimed. They can be escalated.
 
 The task instances are returned to the ready state.
 Any previously stored output or fault message is deleted.
 
 The caller must be the owner or an administrator of the task instances.
 
 The action associated to this method is TaskActions.CANCELCLAIM.
 
 This method is not supported in archive mode.

If a single cancelClaim operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.ObjectDoesNotExistException
 com.ibm.task.api.WrongKindException
 com.ibm.task.api.WrongStateException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all cancelClaim operations are undone.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- cancelClaim java.util.List cancelClaim(TKIID [] tkiids) throws ArchiveUnsupportedOperationException , IdWrongFormatException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Cancels the claim of the specified task instances using task instance IDs. The task instances must have been claimed. They can be escalated. The task instances are returned to the ready state. Any previously stored output or fault message is deleted. The caller must be the owner or an administrator of the task instances. The action associated to this method is TaskActions.CANCELCLAIM . This method is not supported in archive mode. Parameters: tkiids - An array of task instance IDs that are used to identify the task instances to be released. Returns: List - A list of TaskResult objects, one for every task instance specified. Refer to TaskResult . If a single cancelClaim operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all cancelClaim operations are undone. Throws: ArchiveUnsupportedOperationException IdWrongFormatException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.1 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### cancelClaim

```
java.util.List cancelClaim(TKIID[] tkiids)
                           throws ArchiveUnsupportedOperationException,
                                  IdWrongFormatException,
                                  UnexpectedFailureException,
                                  java.rmi.RemoteException,
                                  javax.ejb.EJBException
```

The task instances must have been claimed. They can be escalated.
 
 The task instances are returned to the ready state.
 Any previously stored output or fault message is deleted.
 
 The caller must be the owner or an administrator of the task instances.
 
 The action associated to this method is TaskActions.CANCELCLAIM.
 
 This method is not supported in archive mode.

If a single cancelClaim operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.ObjectDoesNotExistException
 com.ibm.task.api.WrongKindException
 com.ibm.task.api.WrongStateException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all cancelClaim operations are undone.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- claim
ClientObjectWrapper claim(java.lang.String tkiid)
                          throws ApplicationVetoException,
                                 ArchiveUnsupportedOperationException,
                                 CannotCreateWorkItemException,
                                 IdWrongFormatException,
                                 IdWrongTypeException,
                                 NotAuthorizedException,
                                 ObjectDoesNotExistException,
                                 SchedulingFailedException,
                                 WrongKindException,
                                 WrongStateException,
                                 UnexpectedFailureException,
                                 java.rmi.RemoteException,
                                 javax.ejb.EJBException
Claims a ready to-do or collaboration task instance for user processing
 using a string representation of the task instance ID. The task instance can be escalated
 but only suspended when the 'supportsClaimIfSuspended' property is set.
 The collaboration task instance must be stand-alone.
 
 Collaboration and to-do task instances are also known as
 human and participating task instances.
 
 The caller must be a potential owner or an administrator of the task instance.
 
 The state of the task instance is changed to claimed.
 Refer to complete for information on how
 to complete a task instance.
 
 The action associated to this method is TaskActions.CLAIM.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID that is used
    to identify the task instance to be claimed.
 
Returns:ClientObjectWrapper -
    The input message of the claimed task instance.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
SchedulingFailedException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.0
 
 Throws an ApplicationFailedException when the application refuses to execute the method.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- claim
ClientObjectWrapper claim(TKIID tkiid)
                          throws ApplicationVetoException,
                                 ArchiveUnsupportedOperationException,
                                 CannotCreateWorkItemException,
                                 IdWrongFormatException,
                                 NotAuthorizedException,
                                 ObjectDoesNotExistException,
                                 SchedulingFailedException,
                                 WrongKindException,
                                 WrongStateException,
                                 UnexpectedFailureException,
                                 java.rmi.RemoteException,
                                 javax.ejb.EJBException
Claims a ready to-do or collaboration task instance for user processing
 using the task instance ID. The task instance can be escalated
 but only suspended when the 'supportsClaimIfSuspended' property is set.
 The collaboration task instance must be stand-alone.
 
 Collaboration and to-do task instances are also known as
 human and participating task instances.
 
 The caller must be a potential owner or an administrator of the task instance.
 
 The state of the task instance is changed to claimed.
 Refer to complete for information
 on how to complete a task instance.
 
 The action associated to this method is TaskActions.CLAIM.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID of the task instance to be claimed.
 
Returns:ClientObjectWrapper -
    The input message of the claimed task instance.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
SchedulingFailedException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.0
 
 Throws an ApplicationFailedException when the application refuses to execute the method.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- claim Task claim(java.lang.String whereClause, java.lang.String orderByClause, java.util.TimeZone timeZone) throws ArchiveUnsupportedOperationException , CannotCreateWorkItemException , SchedulingFailedException , WorkItemManagerException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Claims some ready to-do or collaboration task instance for user processing. The task instance can be escalated. Collaboration and to-do task instances are also known as human and participating task instances. The task instance that is claimed is identified by the specified where- and order-by-clauses. The first task instance is claimed that qualifies under these conditions, that is not suspended, and for which the caller is a potential owner or administrator. Refer to complete for information on how to complete a task instance. The action associated to this method is TaskActions.CLAIM . This method is not supported in archive mode. Parameters: whereClause - The search condition to be applied to the query domain. The search condition is used to filter the set of ready and not suspended task instances that can be claimed by the logged-on user. Its syntax is an SQL where-clause. The following rules apply: If a filter is not to be applied, null must be specified. orderByClause - Sorts the query result set by the values of the columns you identify. The orderby-clause sorts the set of qualifying ready and not suspended tasks. Its syntax is an SQL order-by-clause. Each comma separated part of the order-by-clause must specify a property from the published views - see the InfoCenter for details. If you identify more that one property, the query result set is ordered by the values of the first property you identify, then by the values of the second property, and so on. If sort criteria are not to be applied, null must be specified. Note that sort criteria are applied on the server, that is, the locale of the server is used for sorting. timeZone - Specifies the time zone of the timestamp constants in the whereClause respectively the time zone for the timestamp values returned. If a timezone is not specified, UTC is assumed. Returns: Task - The task instance that is claimed. If there is no ready and not suspended task instance for the logged-on user, null is returned. Refer to Task to view the task instance properties. Throws: ArchiveUnsupportedOperationException CannotCreateWorkItemException SchedulingFailedException WorkItemManagerException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.0 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode. 7.0 Throws a SchedulingFailedException when scheduling the task failed.

#### claim

```
Task claim(java.lang.String whereClause,
         java.lang.String orderByClause,
         java.util.TimeZone timeZone)
           throws ArchiveUnsupportedOperationException,
                  CannotCreateWorkItemException,
                  SchedulingFailedException,
                  WorkItemManagerException,
                  UnexpectedFailureException,
                  java.rmi.RemoteException,
                  javax.ejb.EJBException
```

Collaboration and to-do task instances are also known as
 human and participating task instances.
 
 The task instance that is claimed is identified by the specified where- and order-by-clauses.
 The first task instance is claimed that qualifies under these conditions, that is not suspended,
 and for which the caller is a potential owner or administrator.
 
 Refer to complete for information on how
 to complete a task instance.
 
 The action associated to this method is TaskActions.CLAIM.
 
 This method is not supported in archive mode.

    - Specify object ID constants as ID('string-rep-of-oid').
    Specify timestamp constants as TS('yyyy-mm-ddThh:mm:ss') or as CURRENT\_DATE
    for comparisons with the current date.
    

    The date and time parts of a TS definition are optional; either the date or the time must
    be specified. If no date part of a TS definition is specified, the current date is taken.
    Optional time values that are not specified are set to zero.
    The timestamp is 24 hours based.
    For example, TS('16:04') is the same as TS('2002-12-24T16:04:00') provided that the
    current date is December 24th, 2002.
    

    If a date part of a TS definition is specified, the year must consist of 4 letters;
    the month and day specifications are optional.
    Missing month and day specifications are set to 01. For example, specifying
    TS('2003') is the same as specifying TS('2003-01-01T00:00:00').
    Specify binary constants as BIN('UTF-8 string').
    Use constants
    instead of integer enumerations. For example, instead of specifying a task state expression
    "TASK.STATE=2" , specify "TASK.STATE=TASK.STATE.STATE\_READY".

If a filter is not to be applied, null must be specified.

If you identify more that one property, the query result set is ordered by the
    values of the first property you identify, then by the values of the second property,
    and so on.
    
    If sort criteria are not to be applied, null must be specified.
    
    Note that sort criteria are applied on the server, that is, the locale of the
    server is used for sorting.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- claim
ClaimResult claim(java.lang.String queryTableName,
                FilterOptions filterOptions,
                AuthorizationOptions authorizationOptions,
                java.util.List parameters,
                int maxRetryCount)
                  throws ApplicationVetoException,
                         ArchiveUnsupportedOperationException,
                         CannotCreateWorkItemException,
                         InvalidParameterException,
                         NotAuthorizedException,
                         ObjectDoesNotExistException,
                         ParameterNullException,
                         SchedulingFailedException,
                         WrongKindException,
                         UnexpectedFailureException,
                         TaskException,
                         java.rmi.RemoteException,
                         javax.ejb.EJBException
Claims a ready to-do or collaboration task instance contained in the specified
 query table. The primary query table must be TASK.
 
 Collaboration and to-do task instances are also known as
 human and participating task instances.
 
 The task instance that is claimed is identified by the options defined for the query table
 and the authorization and filter options specified for this request.
 The first task instance is claimed that qualifies under these conditions.
 The caller must be a potential owner or an administrator of the claimed task instance.
 
 Note that, for best performance reasons, you should specify at least the conditions
 "KIND IN (KIND\_PARTICIPATING, KIND\_HUMAN) AND STATE=STATE\_READY" on the primary query table TASK
 when modeling the query table.
 
 Refer to complete for information on how
 to complete a task instance.
 
 The action associated to this method is TaskActions.CLAIM.
 
 This method is not supported in archive mode.
Parameters:queryTableName - The name of the query table.filterOptions - The filter options to be applied in addition to any filters defined
    for the query table.
    Refer to FilterOptions.authorizationOptions - The authorization options to be applied in addition to any authorization
    specifications defined for the query table.
    
    Authorization options can be specified for predefined query tables that contain
    instance data or for composite query tables that define a primary query table which
    contains instance data and that use instance-based authorization.
    If authorization options are specified for query tables that do not contain instance
    but template data, a NotAuthorizedException is thrown.
    They are ignored for supplemental query tables.
    
    System administrators and monitors can use the AdminAuthorizationOptions to
    run queries that need special authorization, for example, to run a query on behalf
    of another user. These options must be specified when the query is run on
    predefined query tables. When the query is run on composite query tables and
    the primary view contains template data, administrative options must be specified
    if role-based authorization is required.
    When specified for a predefined query table that contains instance data or for
    a composite query table with a primary view that contains instance data, then
    all data contained in the query table is returned.
    
    Refer to AuthorizationOptions or
    AdminAuthorizationOptions.parameters - A list of Parameter objects to set values for parameters used
    in query table filters and selection criteria.
    Refer to Parameter.maxRetryCount - In case of concurrency conflicts, specifies how often claiming a task should be retried.
    For example, if the first task instance that qualifies cannot be claimed because it is
    just claimed by another user, then a retry count of 1 specifies that
    the next qualifying task instance should be claimed.
    If also unsuccessful, the claiming process ends.
    
    If claiming should not be retried, 0 must be specified.
    If there are less qualifying task instances than the mayRetryCount, all
    qualifying task instances are tried to be claimed if necessary.
 
Returns:ClaimResult -
    The result of the claim.
 Refer to ClaimResult for details.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
InvalidParameterException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
SchedulingFailedException
WrongKindException
UnexpectedFailureException
TaskException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- claim java.util.List claim(java.lang.String[] identifiers) throws ArchiveUnsupportedOperationException , CannotCreateWorkItemException , IdWrongFormatException , IdWrongTypeException , SchedulingFailedException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Claims ready to-do or collaboration task instances for user processing using string representations of task instance IDs. The task instances can be escalated but only suspended when the 'supportsClaimIfSuspended' property is set. The collaboration task instance must be stand-alone. Collaboration and to-do task instances are also known as human and participating task instances. The caller must be a potential owner or an administrator of the task instances. The states of the task instances are changed to claimed. Refer to complete for information on how to complete a task instance. The action associated to this method is TaskActions.CLAIM . This method is not supported in archive mode. Parameters: identifiers - An array of task instance IDs that are used to identify the task instances to be claimed. Returns: List - A list of ClaimResult objects, one for every task instance specified. Refer to ClaimResult . If a single claim operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all claim operations are undone. Throws: ArchiveUnsupportedOperationException CannotCreateWorkItemException IdWrongFormatException IdWrongTypeException SchedulingFailedException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.1 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode. 7.0 Throws a SchedulingFailedException when scheduling a task failed.

#### claim

```
java.util.List claim(java.lang.String[] identifiers)
                     throws ArchiveUnsupportedOperationException,
                            CannotCreateWorkItemException,
                            IdWrongFormatException,
                            IdWrongTypeException,
                            SchedulingFailedException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
```

Collaboration and to-do task instances are also known as
 human and participating task instances.
 
 The caller must be a potential owner or an administrator of the task instances.
 
 The states of the task instances are changed to claimed.
 Refer to complete for information on how
 to complete a task instance.
 
 The action associated to this method is TaskActions.CLAIM.
 
 This method is not supported in archive mode.

If a single claim operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.ObjectDoesNotExistException
 com.ibm.task.api.WrongKindException
 com.ibm.task.api.WrongStateException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all claim operations are undone.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a SchedulingFailedException when scheduling a task failed.

- claim java.util.List claim(TKIID [] tkiids) throws ArchiveUnsupportedOperationException , CannotCreateWorkItemException , IdWrongFormatException , SchedulingFailedException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Claims ready to-do or collaboration task instances for user processing using task instance IDs. The task instances can be escalated but only suspended when the 'supportsClaimIfSuspended' property is set. The collaboration task instance must be stand-alone. Collaboration and to-do task instances are also known as human and participating task instances. The caller must be a potential owner or an administrator of the task instances. The states of the task instances are changed to claimed. Refer to complete for information on how to complete a task instance. The action associated to this method is TaskActions.CLAIM . This method is not supported in archive mode. Parameters: tkiids - An array of task instance IDs that are used to identify the task instances to be claimed. Returns: List - A list of ClaimResult objects, one for every task instance specified. Refer to ClaimResult . If a single claim operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all claim operations are undone. Throws: ArchiveUnsupportedOperationException CannotCreateWorkItemException IdWrongFormatException SchedulingFailedException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.1 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode. 7.0 Throws a SchedulingFailedException when scheduling a task failed.

#### claim

```
java.util.List claim(TKIID[] tkiids)
                     throws ArchiveUnsupportedOperationException,
                            CannotCreateWorkItemException,
                            IdWrongFormatException,
                            SchedulingFailedException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
```

Collaboration and to-do task instances are also known as
 human and participating task instances.
 
 The caller must be a potential owner or an administrator of the task instances.
 
 The states of the task instances are changed to claimed.
 Refer to complete for information on how
 to complete a task instance.
 
 The action associated to this method is TaskActions.CLAIM.
 
 This method is not supported in archive mode.

If a single claim operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.ObjectDoesNotExistException
 com.ibm.task.api.WrongKindException
 com.ibm.task.api.WrongStateException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all claim operations are undone.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a SchedulingFailedException when scheduling a task failed.

- complete
void complete(java.lang.String tkiid)
              throws ApplicationVetoException,
                     ArchiveUnsupportedOperationException,
                     IdWrongFormatException,
                     IdWrongTypeException,
                     NotAuthorizedException,
                     ObjectDoesNotExistException,
                     ParallelRoutingTaskException,
                     SchedulingFailedException,
                     WrongKindException,
                     WrongStateException,
                     UnexpectedFailureException,
                     java.rmi.RemoteException,
                     javax.ejb.EJBException
Completes a claimed task instance using a string representation
 of the task instance ID.
 
 The task instance must be in the claimed state. It can be escalated.
 The caller must be the owner or an administrator of the task instance.
 
 Completion of a task instance means that user processing has finished.
 If user processing completed successfully,
 the task instance is put into the finished state.
 
 If user processing did not complete successfully, that is,
 if a fault message is set, the task instance is put into the failed state.
 
 The action associated to this method is TaskActions.COMPLETE.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID that is used
    to identify the task instance to be completed.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
ParallelRoutingTaskException
SchedulingFailedException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.0
 
 Throws an ApplicationFailedException when the application refuses to execute the method.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when completion of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- complete
void complete(TKIID tkiid)
              throws ApplicationVetoException,
                     ArchiveUnsupportedOperationException,
                     IdWrongFormatException,
                     NotAuthorizedException,
                     ObjectDoesNotExistException,
                     ParallelRoutingTaskException,
                     SchedulingFailedException,
                     WrongKindException,
                     WrongStateException,
                     UnexpectedFailureException,
                     java.rmi.RemoteException,
                     javax.ejb.EJBException
Completes a claimed task instance using
 the task instance ID.
 
 The task instance must be in the claimed state. It can be escalated.
 The caller must be the owner or an administrator of the task instance.
 
 Completion of a task instance means that user processing has finished.
 If user processing completed successfully,
 the task instance is put into the finished state.
 
 If user processing did not complete successfully, that is,
 if a fault message is set, the task instance is put into the failed state.
 
 The action associated to this method is TaskActions.COMPLETE.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID to identify the task instance to be completed.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParallelRoutingTaskException
SchedulingFailedException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.0
 
 Throws an ApplicationFailedException when the application refuses to execute the method.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when completion of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- complete
void complete(java.lang.String tkiid,
            ClientObjectWrapper output)
              throws ApplicationVetoException,
                     ArchiveUnsupportedOperationException,
                     IdWrongFormatException,
                     IdWrongTypeException,
                     NotAuthorizedException,
                     ObjectDoesNotExistException,
                     ParallelRoutingTaskException,
                     ParameterNullException,
                     SchedulingFailedException,
                     WrongKindException,
                     WrongMessageTypeException,
                     WrongStateException,
                     UnexpectedFailureException,
                     java.rmi.RemoteException,
                     javax.ejb.EJBException
Completes a claimed task instance using a string representation
 of the task instance ID and passes the result of user processing.
 
 The task instance must be in the claimed state. It can be escalated.
 The caller must be the owner or an administrator of the task instance.
 
 The action associated to this method is TaskActions.COMPLETE.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID that is used
    to identify the task instance to be completed.output - The output message that denotes the successful result of processing.
    Note that an object wrapped by the ClientObjectWrapper must be serializable.
 
    Any previously set output or fault message is ignored.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
ParallelRoutingTaskException
ParameterNullException
SchedulingFailedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.0
 
 Throws an ApplicationFailedException when the application refuses to execute the method.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when completion of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- complete
void complete(TKIID tkiid,
            ClientObjectWrapper output)
              throws ApplicationVetoException,
                     ArchiveUnsupportedOperationException,
                     IdWrongFormatException,
                     NotAuthorizedException,
                     ObjectDoesNotExistException,
                     ParallelRoutingTaskException,
                     ParameterNullException,
                     SchedulingFailedException,
                     WrongKindException,
                     WrongMessageTypeException,
                     WrongStateException,
                     UnexpectedFailureException,
                     java.rmi.RemoteException,
                     javax.ejb.EJBException
Completes a claimed task instance using
 the task instance ID and passes the result of user processing.
 
 The task instance must be in the claimed state. It can be escalated.
 The caller must be the owner or an administrator of the task instance.
 
 The action associated to this method is TaskActions.COMPLETE.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID to identify the task instance to be completed.output - The output message that denotes the successful result of processing.
    Note that an object wrapped by the ClientObjectWrapper must be serializable.
 
    Any previously set output or fault message is ignored.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParallelRoutingTaskException
ParameterNullException
SchedulingFailedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.0
 
 Throws an ApplicationFailedException when the application refuses to execute the method.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when completion of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- complete
void complete(java.lang.String tkiid,
            java.lang.String faultName,
            ClientObjectWrapper faultMessage)
              throws ApplicationVetoException,
                     ArchiveUnsupportedOperationException,
                     IdWrongFormatException,
                     IdWrongTypeException,
                     InvalidQNameException,
                     NotAuthorizedException,
                     ObjectDoesNotExistException,
                     ParallelRoutingTaskException,
                     ParameterNullException,
                     SchedulingFailedException,
                     WrongKindException,
                     WrongMessageTypeException,
                     WrongStateException,
                     UnexpectedFailureException,
                     java.rmi.RemoteException,
                     javax.ejb.EJBException
Completes a claimed task instance using a string representation of
 the task instance ID and states the failing of user processing.
 
 The task instance must be in the claimed state. It can be escalated.
 The caller must be the owner or an administrator of the task instance.
 
 Completion of a task instance means that user processing finished.
 A fault message is passed to state the unsuccessful execution of user processing.
 The task instance is put into the failed state.
 
 The action associated to this method is TaskActions.COMPLETE.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID that is used
    to identify the task instance to be completed.faultName - A fault name to state unsuccessful processing. The fault name must point to
    a fault that is defined for the task.
    Refer to getFaultNames.faultMessage - The fault message. Not that the object
    wrapped by the ClientObjectWrapper must be serializable.
 
    Any previously set output or fault message is ignored.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
InvalidQNameException
NotAuthorizedException
ObjectDoesNotExistException
ParallelRoutingTaskException
ParameterNullException
SchedulingFailedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.0
 
 Throws an ApplicationFailedException when the application refuses to execute the method.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when completion of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- complete
void complete(TKIID tkiid,
            java.lang.String faultName,
            ClientObjectWrapper faultMessage)
              throws ApplicationVetoException,
                     ArchiveUnsupportedOperationException,
                     IdWrongFormatException,
                     InvalidQNameException,
                     NotAuthorizedException,
                     ObjectDoesNotExistException,
                     ParallelRoutingTaskException,
                     ParameterNullException,
                     SchedulingFailedException,
                     WrongKindException,
                     WrongMessageTypeException,
                     WrongStateException,
                     UnexpectedFailureException,
                     java.rmi.RemoteException,
                     javax.ejb.EJBException
Completes a claimed task instance using the
 task instance ID and states the failing of user processing.
 
 The task instance must be in the claimed state. It can be escalated.
 The caller must be the owner or an administrator of the task instance.
 
 Completion of a task instance means that user processing finished.
 A fault message is passed to state the unsuccessful execution of user processing.
 The task instance is put into the failed state.
 
 The action associated to this method is TaskActions.COMPLETE.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID to identify the task instance to be completed.faultName - A fault name to state unsuccessful processing. The fault name must point to
    a fault that is defined for the task.
    Refer to getFaultNames.faultMessage - The fault message. Note that the object
    wrapped by the ClientObjectWrapper must be serializable.
 
    Any previously set output or fault message is ignored.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
InvalidQNameException
NotAuthorizedException
ObjectDoesNotExistException
ParallelRoutingTaskException
ParameterNullException
SchedulingFailedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.0
 
 Throws an ApplicationFailedException when the application refuses to execute the method.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when completion of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- complete java.util.List complete(java.lang.String[] tkiids) throws ArchiveUnsupportedOperationException , IdWrongFormatException , IdWrongTypeException , ParallelRoutingTaskException , SchedulingFailedException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Completes the specified task instances using string representations of the task instance IDs. The task instances must be in the claimed state. They can be escalated. The caller must be the owner or an administrator of the task instances. Completion of a task instance means that user processing has finished. If user processing completed successfully, the task instance is put into the finished state. If user processing did not complete successfully, that is, if a fault message has been set, the task instance is put into the failed state. The action associated to this method is TaskActions.COMPLETE . This method is not supported in archive mode. Parameters: tkiids - An array of task instance IDs that identify the task instances to be completed Returns: List - A list of TaskResult objects, one for every task instance specified. Refer to TaskResult . If a single complete operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all complete operations are undone. Throws: ArchiveUnsupportedOperationException IdWrongFormatException IdWrongTypeException ParallelRoutingTaskException SchedulingFailedException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.1 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode. 7.0 Throws a ParallelRoutingTaskException when completion of a parallel routing task failed. 7.0 Throws a SchedulingFailedException when scheduling the task failed.

#### complete

```
java.util.List complete(java.lang.String[] tkiids)
                        throws ArchiveUnsupportedOperationException,
                               IdWrongFormatException,
                               IdWrongTypeException,
                               ParallelRoutingTaskException,
                               SchedulingFailedException,
                               UnexpectedFailureException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
```

The task instances must be in the claimed state. They can be escalated.
 The caller must be the owner or an administrator of the task instances.
 
 Completion of a task instance means that user processing has finished.
 If user processing completed successfully, the task instance is put
 into the finished state.
 
 If user processing did not complete successfully, that is,
 if a fault message has been set, the task instance is put into the failed state.
 
 The action associated to this method is TaskActions.COMPLETE.
 
 This method is not supported in archive mode.

If a single complete operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.ObjectDoesNotExistException
 com.ibm.task.api.WrongKindException
 com.ibm.task.api.WrongStateException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all complete operations are undone.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when completion of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- complete java.util.List complete(TKIID [] tkiids) throws ArchiveUnsupportedOperationException , IdWrongFormatException , ParallelRoutingTaskException , SchedulingFailedException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Completes the specified task instances using task instance IDs. The task instances must be in the claimed state. They can be escalated. The caller must be the owner or an administrator of the task instances. Completion of a task instance means that user processing has finished. If user processing completed successfully, the task instance is put into the finished state. If user processing did not complete successfully, that is, if a fault message has been set, the task instance is put into the failed state. The action associated to this method is TaskActions.COMPLETE . This method is not supported in archive mode. Parameters: tkiids - An array of task instance IDs that identify the task instances to be completed Returns: List - A list of TaskResult objects, one for every task instance specified. Refer to TaskResult . If a single complete operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all complete operations are undone. Throws: ArchiveUnsupportedOperationException IdWrongFormatException ParallelRoutingTaskException SchedulingFailedException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.1 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode. 7.0 Throws a ParallelRoutingTaskException when completion of a parallel routing task failed. 7.0 Throws a SchedulingFailedException when scheduling the task failed.

#### complete

```
java.util.List complete(TKIID[] tkiids)
                        throws ArchiveUnsupportedOperationException,
                               IdWrongFormatException,
                               ParallelRoutingTaskException,
                               SchedulingFailedException,
                               UnexpectedFailureException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
```

The task instances must be in the claimed state. They can be escalated.
 The caller must be the owner or an administrator of the task instances.
 
 Completion of a task instance means that user processing has finished.
 If user processing completed successfully, the task instance is put
 into the finished state.
 
 If user processing did not complete successfully, that is,
 if a fault message has been set, the task instance is put into the failed state.
 
 The action associated to this method is TaskActions.COMPLETE.
 
 This method is not supported in archive mode.

If a single complete operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.ObjectDoesNotExistException
 com.ibm.task.api.ParameterNullException
 com.ibm.task.api.WrongKindException
 com.ibm.task.api.WrongStateException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all complete operations are undone.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when completion of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- completeWithFollowOnTask
void completeWithFollowOnTask(java.lang.String tkiid,
                            java.lang.String followOnID,
                            ClientObjectWrapper input)
                              throws AdministratorCannotBeResolvedException,
                                     ApplicationVetoException,
                                     ArchiveUnsupportedOperationException,
                                     CannotCreateWorkItemException,
                                     FaultMessageDefinitionDoesNotMatchException,
                                     FollowOnTasksNotSupportedException,
                                     IdWrongFormatException,
                                     IdWrongTypeException,
                                     InvalidLengthException,
                                     NotAuthorizedException,
                                     UserDoesNotExistException,
                                     ObjectDoesNotExistException,
                                     OutputMessageDefinitionDoesNotMatchException,
                                     ParallelRoutingTaskException,
                                     SCAServiceAccessFailureException,
                                     SCAServiceResultErrorException,
                                     SchedulingFailedException,
                                     WrongKindException,
                                     WrongMessageTypeException,
                                     WrongStateException,
                                     UnexpectedFailureException,
                                     java.rmi.RemoteException,
                                     javax.ejb.EJBException
Completes a task instance and starts a follow-on task
 using a string representation of the task instance ID.
 
 The task instance that is completed must be in the claimed state. It can be escalated.
 As a result of this call, it is set into the forwarded state. If a reply handler is
 specified, it is called when the last follow-on task in a possible chain is finished.
 
 The task instance that is started as follow-on task must be in the inactive state. It
 can be a collaboration or stand-alone invocation task. Escalation or deletion timer settings
 of the completed task become active.
 
 Collaboration and invocation task instances are also known as
 human and originating task instances.
 
 The output and fault message definitions of the completed and the follow-on task
 must be of the same type. The types of the input messages may differ.
 Any output or fault message stored persistently is automatically passed
 to the follow-on task. The input message is passed if it is of the same type and if not
 specified otherwise - see the input parameter below.
 
 The caller must be the owner or an administrator of the task instance that is to
 be completed and must be allowed to at least read the follow-on task.
 
 The action associated to this method is TaskActions.COMPLETEWITHFOLLOWONTASK.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID that is used
    to identify the task instance to be completed.followOnID - A string representation of the task instance ID that is used
    to identify the task instance that is to follow.input - An optional input message for the follow-on task. If not specified,
    the input message of the completed task is passed to the follow-on task provided
    that they are of the same type.
    
    Note that an object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
FaultMessageDefinitionDoesNotMatchException
FollowOnTasksNotSupportedException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
OutputMessageDefinitionDoesNotMatchException
ParallelRoutingTaskException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when completion of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- completeWithFollowOnTask
void completeWithFollowOnTask(TKIID tkiid,
                            TKIID followOnID,
                            ClientObjectWrapper input)
                              throws AdministratorCannotBeResolvedException,
                                     ApplicationVetoException,
                                     ArchiveUnsupportedOperationException,
                                     CannotCreateWorkItemException,
                                     FaultMessageDefinitionDoesNotMatchException,
                                     FollowOnTasksNotSupportedException,
                                     IdWrongFormatException,
                                     InvalidLengthException,
                                     NotAuthorizedException,
                                     UserDoesNotExistException,
                                     ObjectDoesNotExistException,
                                     OutputMessageDefinitionDoesNotMatchException,
                                     ParallelRoutingTaskException,
                                     SCAServiceAccessFailureException,
                                     SCAServiceResultErrorException,
                                     SchedulingFailedException,
                                     WrongKindException,
                                     WrongMessageTypeException,
                                     WrongStateException,
                                     UnexpectedFailureException,
                                     java.rmi.RemoteException,
                                     javax.ejb.EJBException
Completes a task instance and starts a follow-on task
 using the task instance ID.
 
 The task instance that is completed must be in the claimed state. It can be escalated.
 As a result of this call, it is set into the forwarded state. If a reply handler is
 specified, it is called when the last follow-on task in a possible chain is finished.
 
 The task instance that is started as follow-on task must be in the inactive state. It
 can be a collaboration or stand-alone invocation task. Escalation or deletion timer settings
 of the completed task become active.
 
 Collaboration and invocation task instances are also known as
 human and originating task instances.
 
 The output and fault message definitions of the completed and the follow-on task
 must be of the same type. The types of the input messages may differ.
 Any output or fault message stored persistently is automatically passed
 to the follow-on task. The input message is passed if it is of the same type and if not
 specified otherwise - see the input parameter below.
 
 The caller must be the owner or an administrator of the task instance that is to
 be completed and must be allowed to at least read the follow-on task.
 
 The action associated to this method is TaskActions.COMPLETEWITHFOLLOWONTASK.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID to identify the task instance to be completed.followOnID - The object ID
    to identify the task instance that is to follow.input - An optional input message for the follow-on task. If not specified,
    the input message of the completed task is passed to the follow-on task provided
    that they are of the same type.
    
    Note that an object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
FaultMessageDefinitionDoesNotMatchException
FollowOnTasksNotSupportedException
IdWrongFormatException
InvalidLengthException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
OutputMessageDefinitionDoesNotMatchException
ParallelRoutingTaskException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when completion of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- completeWithNewFollowOnTask
void completeWithNewFollowOnTask(java.lang.String tkiid,
                               java.lang.String name,
                               java.lang.String namespace,
                               ClientObjectWrapper input)
                                 throws AdministratorCannotBeResolvedException,
                                        ApplicationVetoException,
                                        ArchiveUnsupportedOperationException,
                                        CannotCreateWorkItemException,
                                        FaultMessageDefinitionDoesNotMatchException,
                                        FollowOnTasksNotSupportedException,
                                        IdWrongFormatException,
                                        IdWrongTypeException,
                                        InvalidApplicationStateException,
                                        InvalidLengthException,
                                        NotAuthorizedException,
                                        UserDoesNotExistException,
                                        ObjectDoesNotExistException,
                                        OutputMessageDefinitionDoesNotMatchException,
                                        ParallelRoutingTaskException,
                                        ParameterNullException,
                                        SCAServiceAccessFailureException,
                                        SCAServiceResultErrorException,
                                        SchedulingFailedException,
                                        WrongKindException,
                                        WrongMessageTypeException,
                                        WrongStateException,
                                        UnexpectedFailureException,
                                        java.rmi.RemoteException,
                                        javax.ejb.EJBException
Completes a task instance and creates and starts a follow-on task
 using a string representation of the task instance ID.
 
 The task instance that is completed must be in the claimed state. It can be escalated.
 As a result of this call, it is set into the forwarded state. If a reply handler is
 specified, it is called when the last follow-on task in a possible chain is finished.
 
 The task instance that is created and started as follow-on task must
 be a collaboration or stand-alone invocation task. Escalation or deletion timer settings
 of the completed task become active.
 
 Collaboration and invocation task instances are also known as
 human and originating task instances.
 
 The output and fault message definitions of the completed and the follow-on task
 must be of the same type. The types of the input messages may differ.
 Any output or fault message stored persistently is automatically passed
 to the follow-on task. The input message is passed if it is of the same type and if not
 specified otherwise - see the input parameter below.
 
 The caller must be the owner or an administrator of the completed task instance.
 The caller must be a potential instance creator or an administrator of the task template.
 
 The action associated to this method is TaskTemplateActions.COMPLETEWITHNEWFOLLOWONTASK.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID that is used
    to identify the task instance to be completed.name - The name of the task template from which an instance is to be created
    as follow-on task. The currently valid template is then instantiated.namespace - The namespace of the task template.input - An optional input message for the follow-on task. If not specified,
    the input message of the completed task is passed to the follow-on task provided
    that they are of the same type.
    
    Note that an object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
FaultMessageDefinitionDoesNotMatchException
FollowOnTasksNotSupportedException
IdWrongFormatException
IdWrongTypeException
InvalidApplicationStateException
InvalidLengthException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
OutputMessageDefinitionDoesNotMatchException
ParallelRoutingTaskException
ParameterNullException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when completion of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- completeWithNewFollowOnTask
void completeWithNewFollowOnTask(TKIID tkiid,
                               java.lang.String name,
                               java.lang.String namespace,
                               ClientObjectWrapper input)
                                 throws AdministratorCannotBeResolvedException,
                                        ApplicationVetoException,
                                        ArchiveUnsupportedOperationException,
                                        CannotCreateWorkItemException,
                                        FaultMessageDefinitionDoesNotMatchException,
                                        FollowOnTasksNotSupportedException,
                                        IdWrongFormatException,
                                        InvalidApplicationStateException,
                                        InvalidLengthException,
                                        NotAuthorizedException,
                                        UserDoesNotExistException,
                                        ObjectDoesNotExistException,
                                        OutputMessageDefinitionDoesNotMatchException,
                                        ParallelRoutingTaskException,
                                        ParameterNullException,
                                        SCAServiceAccessFailureException,
                                        SCAServiceResultErrorException,
                                        SchedulingFailedException,
                                        WrongKindException,
                                        WrongMessageTypeException,
                                        WrongStateException,
                                        UnexpectedFailureException,
                                        java.rmi.RemoteException,
                                        javax.ejb.EJBException
Completes a task instance and creates and starts a follow-on task
 using the task instance ID.
 
 The task instance that is completed must be in the claimed state. It can be escalated.
 As a result of this call, it is set into the forwarded state. If a reply handler is
 specified, it is called when the last follow-on task in a possible chain is finished.
 
 The task instance that is created and started as follow-on task must
 be a collaboration or stand-alone invocation task. Escalation or deletion timer settings
 of the completed task become active.
 
 Collaboration and invocation task instances are also known as
 human and originating task instances.
 
 The output and fault message definitions of the completed and the follow-on task
 must be of the same type. The types of the input messages may differ.
 Any output or fault message stored persistently is automatically passed
 to the follow-on task. The input message is passed if it is of the same type and if not
 specified otherwise - see the input parameter below.
 
 The caller must be the owner or an administrator of the completed task instance.
 The caller must be a potential instance creator or an administrator of the task template.
 
 The action associated to this method is TaskTemplateActions.COMPLETEWITHNEWFOLLOWONTASK.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID to identify the task instance to be completed.name - The name of the task template from which an instance is to be created
    as follow-on task. The currently valid template is then instantiated.namespace - The namespace of the task template.input - An optional input message for the follow-on task. If not specified,
    the input message of the completed task is passed to the follow-on task provided
    that they are of the same type.
    
    Note that an object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
FaultMessageDefinitionDoesNotMatchException
FollowOnTasksNotSupportedException
IdWrongFormatException
InvalidApplicationStateException
InvalidLengthException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
OutputMessageDefinitionDoesNotMatchException
ParallelRoutingTaskException
ParameterNullException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when completion of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- completeWithNewFollowOnTask
void completeWithNewFollowOnTask(java.lang.String tkiid,
                               TaskModel taskModel,
                               java.lang.String applicationName,
                               ClientObjectWrapper input)
                                 throws AdministratorCannotBeResolvedException,
                                        ApplicationVetoException,
                                        ArchiveUnsupportedOperationException,
                                        CannotCreateWorkItemException,
                                        FaultMessageDefinitionDoesNotMatchException,
                                        FollowOnTasksNotSupportedException,
                                        IdWrongFormatException,
                                        IdWrongTypeException,
                                        InvalidLengthException,
                                        NotAuthorizedException,
                                        UserDoesNotExistException,
                                        ObjectDoesNotExistException,
                                        OutputMessageDefinitionDoesNotMatchException,
                                        ParallelRoutingTaskException,
                                        ParameterNullException,
                                        SchedulingFailedException,
                                        TaskDeploymentException,
                                        TELValidationException,
                                        WrongKindException,
                                        WrongMessageTypeException,
                                        WrongStateException,
                                        UnexpectedFailureException,
                                        java.rmi.RemoteException,
                                        javax.ejb.EJBException
Completes a task instance and creates and starts an ad hoc follow-on task
 using a string representation of the task instance ID.
 
 The task instance that is completed must be in the claimed state. It can be escalated.
 As a result of this call, it is set into the forwarded state. If a reply handler is
 specified, it is called when the last follow-on task in a possible chain is finished.
 
 The task instance that is created and started as follow-on task must
 be a collaboration or stand-alone invocation task. Escalation or deletion timer settings
 of the completed task become active.
 
 Collaboration and invocation task instances are also known as
 human and originating task instances.
 
 The output and fault message definitions of the completed and the follow-on task
 must be of the same type. The types of the input messages may differ.
 Any output or fault message stored persistently is automatically passed
 to the follow-on task. The input message is passed if it is of the same type and if not
 specified otherwise - see the input parameter below.
 
 The caller must be the owner or an administrator of the completed task instance.
 The caller must have potential-instance-creator rights on the associated
 application component which is inherited from the completed task instance.
 
 The action associated to this method is TaskTemplateActions.COMPLETEWITHNEWFOLLOWONTASK.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID that is used
    to identify the task instance to be completed.taskModel - The model that describes the task template from which a follow-on task is
    to be created at Runtime.applicationName - The name of the enterprise application that contains the message
    or business calendar definitions used in the TaskModel.
    If the message definitions are simple types only or if you do not use a business
    calendar, null may be specified.input - An optional input message for the follow-on task. If not specified,
    the input message of the completed task is passed to the follow-on task provided
    that they are of the same type.
    
    Note that an object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
FaultMessageDefinitionDoesNotMatchException
FollowOnTasksNotSupportedException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
OutputMessageDefinitionDoesNotMatchException
ParallelRoutingTaskException
ParameterNullException
SchedulingFailedException
TaskDeploymentException
TELValidationException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when completion of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- completeWithNewFollowOnTask
void completeWithNewFollowOnTask(TKIID tkiid,
                               TaskModel taskModel,
                               java.lang.String applicationName,
                               ClientObjectWrapper input)
                                 throws AdministratorCannotBeResolvedException,
                                        ApplicationVetoException,
                                        ArchiveUnsupportedOperationException,
                                        CannotCreateWorkItemException,
                                        FaultMessageDefinitionDoesNotMatchException,
                                        FollowOnTasksNotSupportedException,
                                        IdWrongFormatException,
                                        InvalidLengthException,
                                        NotAuthorizedException,
                                        UserDoesNotExistException,
                                        ObjectDoesNotExistException,
                                        OutputMessageDefinitionDoesNotMatchException,
                                        ParallelRoutingTaskException,
                                        ParameterNullException,
                                        SchedulingFailedException,
                                        TaskDeploymentException,
                                        TELValidationException,
                                        WrongKindException,
                                        WrongMessageTypeException,
                                        WrongStateException,
                                        UnexpectedFailureException,
                                        java.rmi.RemoteException,
                                        javax.ejb.EJBException
Completes a task instance and creates and starts an ad hoc follow-on task
 using the task instance ID.
 
 The task instance that is completed must be in the claimed state. It can be escalated.
 As a result of this call, it is set into the forwarded state. If a reply handler is
 specified, it is called when the last follow-on task in a possible chain is finished.
 
 The task instance that is created and started as follow-on task must
 be a collaboration or stand-alone invocation task. Escalation or deletion timer settings
 of the completed task become active.
 
 Collaboration and invocation task instances are also known as
 human and originating task instances.
 
 The output and fault message definitions of the completed and the follow-on task
 must be of the same type. The types of the input messages may differ.
 Any output or fault message stored persistently is automatically passed
 to the follow-on task. The input message is passed if it is of the same type and if not
 specified otherwise - see the input parameter below.
 
 The caller must be the owner or an administrator of the completed task instance.
 The caller must have potential-instance-creator rights on the associated
 application component which is inherited from the completed task instance.
 
 The action associated to this method is TaskTemplateActions.COMPLETEWITHNEWFOLLOWONTASK.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID to identify the task instance to be completed.taskModel - The model that describes the task template from which a follow-on task is
    to be created at Runtime.applicationName - The name of the enterprise application that contains the message
    or business calendar definitions used in the TaskModel.
    If the message definitions are simple types only or if you do not use a business
    calendar, null may be specified.input - An optional input message for the follow-on task. If not specified,
    the input message of the completed task is passed to the follow-on task provided
    that they are of the same type.
    
    Note that an object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
FaultMessageDefinitionDoesNotMatchException
FollowOnTasksNotSupportedException
IdWrongFormatException
InvalidLengthException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
OutputMessageDefinitionDoesNotMatchException
ParallelRoutingTaskException
ParameterNullException
SchedulingFailedException
TaskDeploymentException
TELValidationException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when completion of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- createAndCallTask
ClientObjectWrapper createAndCallTask(java.lang.String tktid,
                                    ClientObjectWrapper input)
                                      throws AdministratorCannotBeResolvedException,
                                             ApplicationVetoException,
                                             ArchiveUnsupportedOperationException,
                                             CannotCreateWorkItemException,
                                             FaultReplyException,
                                             IdWrongFormatException,
                                             IdWrongTypeException,
                                             InvalidApplicationStateException,
                                             InvalidLengthException,
                                             NotAuthorizedException,
                                             ObjectDoesNotExistException,
                                             SCAServiceAccessFailureException,
                                             SCAServiceResultErrorException,
                                             SchedulingFailedException,
                                             WrongKindException,
                                             WrongMessageTypeException,
                                             WrongStateException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Creates and synchronously executes an invocation task instance
 using a string representation of the task template ID.
 An input message can be passed to specify initial values for the task.
 
 Note that an invocation task instance is also known as originating task instance.
 
 This method returns only when the execution of the task finishes with the result of
 execution. If a fault occurs, an exception is thrown. The service that is called must be
 a two-way operation. Otherwise, SCAServiceAccessFailureException is thrown.
 
 The caller must be a potential instance creator or an administrator of the task template.
 
 The action associated to this method is TaskTemplateActions.CREATEANDCALLTASK.
 
 This method is not supported in archive mode.
Parameters:tktid - The string representation of a task template ID from which an instance is to be created
    and executed. A WrongStateException is thrown when the specified task template
    is stopped.input - The input message.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:ClientObjectWrapper -
    The output message to state the result of execution.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
FaultReplyException
IdWrongFormatException
IdWrongTypeException
InvalidApplicationStateException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5

- createAndCallTask
ClientObjectWrapper createAndCallTask(TKTID tktid,
                                    ClientObjectWrapper input)
                                      throws AdministratorCannotBeResolvedException,
                                             ApplicationVetoException,
                                             ArchiveUnsupportedOperationException,
                                             CannotCreateWorkItemException,
                                             FaultReplyException,
                                             IdWrongFormatException,
                                             InvalidApplicationStateException,
                                             InvalidLengthException,
                                             NotAuthorizedException,
                                             ObjectDoesNotExistException,
                                             SCAServiceAccessFailureException,
                                             SCAServiceResultErrorException,
                                             SchedulingFailedException,
                                             WrongKindException,
                                             WrongMessageTypeException,
                                             WrongStateException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Creates and synchronously executes an invocation task instance
 using the task template ID.
 An input message can be passed to specify initial values for the task.
 
 Note that an invocation task instance is also known as originating task instance.
 
 This method returns only when the execution of the task finishes with the result of
 execution. If a fault occurs, an exception is thrown. The service that is called must be
 a two-way operation. Otherwise, SCAServiceAccessFailureException is thrown.
 
 The caller must be a potential instance creator or an administrator of the task template.
 
 The action associated to this method is TaskTemplateActions.CREATEANDCALLTASK.
 
 This method is not supported in archive mode.
Parameters:tktid - The task template ID of the task template from which an instance is to be created
    and executed. A WrongStateException is thrown when the specified task template
    is stopped.input - The input message.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:ClientObjectWrapper -
    The output message to state the result of execution.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
FaultReplyException
IdWrongFormatException
InvalidApplicationStateException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5

- createAndCallTask
ClientObjectWrapper createAndCallTask(java.lang.String name,
                                    java.lang.String namespace,
                                    ClientObjectWrapper input)
                                      throws AdministratorCannotBeResolvedException,
                                             ApplicationVetoException,
                                             ArchiveUnsupportedOperationException,
                                             CannotCreateWorkItemException,
                                             FaultReplyException,
                                             InvalidApplicationStateException,
                                             InvalidLengthException,
                                             NotAuthorizedException,
                                             ObjectDoesNotExistException,
                                             ParameterNullException,
                                             SCAServiceAccessFailureException,
                                             SCAServiceResultErrorException,
                                             SchedulingFailedException,
                                             WrongKindException,
                                             WrongMessageTypeException,
                                             WrongStateException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Creates and synchronously executes an invocation task instance. An input message
 can be passed to specify initial values for the task.
 
 An invocation task instance is also known as originating task instance.
 
 This method returns only when the execution of the task finishes with the result of
 execution. If a fault occurs, an exception is thrown. The service that is called must be
 a two-way operation. Otherwise, SCAServiceAccessFailureException is thrown.
 
 The caller must be a potential instance creator or an administrator of the task template.
 
 The action associated to this method is TaskTemplateActions.CREATEANDCALLTASK.
 
 This method is not supported in archive mode.
Parameters:name - The name of the task template from which an instance is to be created
    and executed. The currently valid template is then instantiated. A WrongStateException
    is thrown when the currently valid template is stopped.namespace - The namespace of the task template.input - The input message.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:ClientObjectWrapper -
    The output message to state the result of execution.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
FaultReplyException
InvalidApplicationStateException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- createAndStartTask
TKIID createAndStartTask(java.lang.String tktid,
                       ClientObjectWrapper input,
                       ReplyHandlerWrapper replyHandler)
                         throws AdministratorCannotBeResolvedException,
                                ApplicationVetoException,
                                ArchiveUnsupportedOperationException,
                                CannotCreateWorkItemException,
                                IdWrongFormatException,
                                IdWrongTypeException,
                                InvalidApplicationStateException,
                                InvalidLengthException,
                                NotAuthorizedException,
                                ObjectDoesNotExistException,
                                ParallelRoutingTaskException,
                                SCAServiceAccessFailureException,
                                SCAServiceResultErrorException,
                                SchedulingFailedException,
                                WrongKindException,
                                WrongMessageTypeException,
                                WrongStateException,
                                UnexpectedFailureException,
                                java.rmi.RemoteException,
                                javax.ejb.EJBException
Creates and starts a task instance
 using a string representation of the task template ID.
 
 The caller must be a potential instance creator or an administrator of the task template.
 The caller becomes the originator of the task. When the task is an invocation aka originating task,
 then the caller also becomes the starter of the task.
 
 The action associated to this method is TaskTemplateActions.CREATEANDSTARTTASK.
 
 This method is not supported in archive mode.
Parameters:tktid - The string representation of the task template ID from which an instance
    is to be created and started. A WrongStateException
    is thrown when the specified task template is stopped.input - The input message.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.replyHandler - The reply handler to be used in order to send the result of execution
   automatically back to the
   caller. "null" must be specified if no reply handler is to be used.
 
Returns:TKIID -
    The task instance ID of the task created.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongFormatException
IdWrongTypeException
InvalidApplicationStateException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParallelRoutingTaskException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5

- createAndStartTask
TKIID createAndStartTask(TKTID tktid,
                       ClientObjectWrapper input,
                       ReplyHandlerWrapper replyHandler)
                         throws AdministratorCannotBeResolvedException,
                                ApplicationVetoException,
                                ArchiveUnsupportedOperationException,
                                CannotCreateWorkItemException,
                                IdWrongFormatException,
                                InvalidApplicationStateException,
                                InvalidLengthException,
                                NotAuthorizedException,
                                ObjectDoesNotExistException,
                                ParallelRoutingTaskException,
                                SCAServiceAccessFailureException,
                                SCAServiceResultErrorException,
                                SchedulingFailedException,
                                WrongKindException,
                                WrongMessageTypeException,
                                WrongStateException,
                                UnexpectedFailureException,
                                java.rmi.RemoteException,
                                javax.ejb.EJBException
Creates and starts a task instance
 using the task template ID.
 
 The caller must be a potential instance creator or an administrator of the task template.
 The caller becomes the originator of the task. When the task is an invocation aka originating task,
 then the caller also becomes the starter of the task.
 
 The action associated to this method is TaskTemplateActions.CREATEANDSTARTTASK.
 
 This method is not supported in archive mode.
Parameters:tktid - The  task template ID from which an instance
    is to be created and started. A WrongStateException
    is thrown when the specified task template is stopped.input - The input message.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.replyHandler - The reply handler to be used in order to send the result of execution
   automatically back to the
   caller. "null" must be specified if no reply handler is to be used.
 
Returns:TKIID -
    The task instance ID of the task created.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongFormatException
InvalidApplicationStateException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParallelRoutingTaskException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5

- createAndStartTask
TKIID createAndStartTask(java.lang.String name,
                       java.lang.String namespace,
                       ClientObjectWrapper input,
                       ReplyHandlerWrapper replyHandler)
                         throws AdministratorCannotBeResolvedException,
                                ApplicationVetoException,
                                ArchiveUnsupportedOperationException,
                                CannotCreateWorkItemException,
                                InvalidApplicationStateException,
                                InvalidLengthException,
                                NotAuthorizedException,
                                UserDoesNotExistException,
                                ObjectDoesNotExistException,
                                ParallelRoutingTaskException,
                                ParameterNullException,
                                SCAServiceAccessFailureException,
                                SCAServiceResultErrorException,
                                SchedulingFailedException,
                                WrongKindException,
                                WrongMessageTypeException,
                                WrongStateException,
                                UnexpectedFailureException,
                                java.rmi.RemoteException,
                                javax.ejb.EJBException
Creates and starts a task instance from the currently valid task template.
 
 The caller must be a potential instance creator or an administrator of the task template.
 The caller becomes the originator of the task. When the task is an invocation aka originating task,
 then the caller also becomes the starter of the task.
 
 The action associated to this method is TaskTemplateActions.CREATEANDSTARTTASK.
 
 This method is not supported in archive mode.
Parameters:name - The name of the task template from which an instance is to be created
    and started. The currently valid template is then instantiated. A WrongStateException
    is thrown when the currently valid template is stopped.namespace - The namespace of the task template.input - The input message.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.replyHandler - The reply handler to be used in order to send the result of execution
   automatically back to the
   caller. "null" must be specified if no reply handler is to be used.
 
Returns:TKIID -
    The task instance ID of the task created.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
InvalidApplicationStateException
InvalidLengthException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
ParallelRoutingTaskException
ParameterNullException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when starting of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- createAndStartTask
TKIID createAndStartTask(TaskModel taskModel,
                       java.lang.String applicationName,
                       java.lang.String parentContext,
                       ClientObjectWrapper input,
                       ReplyHandlerWrapper replyHandler)
                         throws AdministratorCannotBeResolvedException,
                                ApplicationVetoException,
                                ArchiveUnsupportedOperationException,
                                CannotCreateWorkItemException,
                                IdWrongTypeException,
                                InvalidLengthException,
                                NotAuthorizedException,
                                UserDoesNotExistException,
                                ObjectDoesNotExistException,
                                ParallelRoutingTaskException,
                                ParameterNullException,
                                SchedulingFailedException,
                                WrongMessageTypeException,
                                UnexpectedFailureException,
                                TaskDeploymentException,
                                TELValidationException,
                                java.rmi.RemoteException,
                                javax.ejb.EJBException
Creates and starts a task from the specified task model.
 
 The caller must have potential-instance-creator rights on the associated application component.
 The caller becomes the originator of the new task.
 
 The action associated to this method is TaskTemplateActions.CREATEANDSTARTTASK.
 
 This method is not supported in archive mode.
Parameters:taskModel - The model that describes the task instance to be created at Runtime.applicationName - The name of the enterprise application that contains the message
    or business calendar definitions used in the TaskModel.
    If the message definitions are simple types only or if you do not use a business
    calendar, null may be specified.parentContext - The object ID (ACOID) or the name of the application component
    to be associated with the newly created task instance.input - The input message.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.replyHandler - The reply handler to be used in order to send the result of execution
   automatically back to the
   caller. "null" must be specified if no reply handler is to be used.
 
Returns:TKIID -
    The task instance ID of the task created and run.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongTypeException
InvalidLengthException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
ParallelRoutingTaskException
ParameterNullException
SchedulingFailedException
WrongMessageTypeException
UnexpectedFailureException
TaskDeploymentException
TELValidationException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when starting of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- createAndStartTaskAsSubTask
TKIID createAndStartTaskAsSubTask(java.lang.String tktid,
                                java.lang.String parentTaskID,
                                ClientObjectWrapper input)
                                  throws AdministratorCannotBeResolvedException,
                                         ApplicationVetoException,
                                         ArchiveUnsupportedOperationException,
                                         CannotCreateWorkItemException,
                                         IdWrongFormatException,
                                         IdWrongTypeException,
                                         InvalidApplicationStateException,
                                         InvalidLengthException,
                                         NotAuthorizedException,
                                         ObjectDoesNotExistException,
                                         ParallelRoutingTaskException,
                                         SCAServiceAccessFailureException,
                                         SCAServiceResultErrorException,
                                         SchedulingFailedException,
                                         SubTasksNotSupportedException,
                                         WrongKindException,
                                         WrongMessageTypeException,
                                         WrongStateException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Creates and starts a task instance as a subtask of the specified parent
 task instance using string representations of the task template and instance IDs.
 The parent task instance is then waiting for the completion of the subtask. It can only
 be completed when all subtasks came to an end.
 
 The subtask created must be a collaboration or stand-alone invocation task. An invocation task
 must be derived from a task template that has not been created at Runtime. The parent task
 instance must be a collaboration or to-do task in the claimed state.
 It can be escalated or already waiting for a subtask. It can, however, not be suspended.
 
 Note that collaboration, invocation, and to-do task instances are also known as
 human, originating, and participating task instances.
 
 A subtask can only
 be created when the parent task supports subtask creation - refer to Task to
 view the task instance properties.
 
 The caller must be a potential instance creator or an administrator of the subtask template
 and an owner or administrator of the parent task instance.
 The caller becomes the originator of the subtask. When the subtask is an invocation aka originating task,
 then the caller also becomes the starter of the task.
 
 The action associated to this method is TaskTemplateActions.CREATEANDSTARTTASKASSUBTASK.
 
 This method is not supported in archive mode.
Parameters:tktid - The string representation of the task template ID from which the subtask
    is to be created and started. A WrongStateException
    is thrown when the specified task template is stopped.parentTaskID - The string representation of the task instance ID that identifies
    the parent task instance.input - The input message.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:TKIID -
    The task instance ID of the subtask created.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongFormatException
IdWrongTypeException
InvalidApplicationStateException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParallelRoutingTaskException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
SubTasksNotSupportedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5

- createAndStartTaskAsSubTask
TKIID createAndStartTaskAsSubTask(TKTID tktid,
                                TKIID parentTaskID,
                                ClientObjectWrapper input)
                                  throws AdministratorCannotBeResolvedException,
                                         ApplicationVetoException,
                                         ArchiveUnsupportedOperationException,
                                         CannotCreateWorkItemException,
                                         IdWrongFormatException,
                                         InvalidApplicationStateException,
                                         InvalidLengthException,
                                         NotAuthorizedException,
                                         ObjectDoesNotExistException,
                                         ParallelRoutingTaskException,
                                         SCAServiceAccessFailureException,
                                         SCAServiceResultErrorException,
                                         SchedulingFailedException,
                                         SubTasksNotSupportedException,
                                         WrongKindException,
                                         WrongMessageTypeException,
                                         WrongStateException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Creates and starts a task instance as a subtask of the specified parent
 task instance using task template and parent task instance IDs.
 The parent task instance is then waiting for the completion of the subtask. It can only
 be completed when all subtasks came to an end.
 
 The subtask created must be a collaboration or stand-alone invocation task. An invocation task
 must be derived from a task template that has not been created at Runtime. The parent task
 instance must be a collaboration or to-do task in the claimed state.
 It can be escalated or already waiting for a subtask. It can, however, not be suspended.
 
 Note that collaboration, invocation, and to-do task instances are also known as
 human, originating, and participating task instances.
 
 A subtask can only
 be created when the parent task supports subtask creation - refer to Task to
 view the task instance properties.
 
 The caller must be a potential instance creator or an administrator of the subtask template
 and an owner or administrator of the parent task instance.
 The caller becomes the originator of the subtask. When the subtask is an invocation aka originating task,
 then the caller also becomes the starter of the task.
 
 The action associated to this method is TaskTemplateActions.CREATEANDSTARTTASKASSUBTASK.
 
 This method is not supported in archive mode.
Parameters:tktid - The task template ID from which the subtask
    is to be created and started. A WrongStateException
    is thrown when the specified task template is stopped.parentTaskID - The task instance ID that identifies the parent task instance.input - The input message.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:TKIID -
    The task instance ID of the subtask created.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongFormatException
InvalidApplicationStateException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParallelRoutingTaskException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
SubTasksNotSupportedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5

- createAndStartTaskAsSubTask
TKIID createAndStartTaskAsSubTask(java.lang.String name,
                                java.lang.String namespace,
                                java.lang.String parentTaskID,
                                ClientObjectWrapper input)
                                  throws AdministratorCannotBeResolvedException,
                                         ApplicationVetoException,
                                         ArchiveUnsupportedOperationException,
                                         CannotCreateWorkItemException,
                                         IdWrongFormatException,
                                         IdWrongTypeException,
                                         InvalidApplicationStateException,
                                         InvalidLengthException,
                                         NotAuthorizedException,
                                         UserDoesNotExistException,
                                         ObjectDoesNotExistException,
                                         ParallelRoutingTaskException,
                                         ParameterNullException,
                                         SCAServiceAccessFailureException,
                                         SCAServiceResultErrorException,
                                         SchedulingFailedException,
                                         SubTasksNotSupportedException,
                                         WrongKindException,
                                         WrongMessageTypeException,
                                         WrongStateException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Creates and starts a task instance as a subtask of the specified parent
 task instance using a string representation of the parent task instance ID.
 The parent task instance is then waiting for the completion of the subtask. It can only
 be completed when all subtasks came to an end.
 
 The subtask created must be a collaboration or stand-alone invocation task. An invocation task
 must be derived from a task template that has not been created at Runtime. The parent task
 instance must be a collaboration or to-do task in the claimed state.
 It can be escalated or already waiting for a subtask. It can, however, not be suspended.
 
 Note that collaboration, invocation, and to-do task instances are also known as
 human, originating, and participating task instances.
 
 A subtask can only
 be created when the parent task supports subtask creation - refer to Task to
 view the task instance properties.
 
 The caller must be a potential instance creator or an administrator of the subtask template
 and an owner or administrator of the parent task instance.
 The caller becomes the originator of the subtask. When the subtask is an invocation aka originating task,
 then the caller also becomes the starter of the task.
 
 The action associated to this method is TaskTemplateActions.CREATEANDSTARTTASKASSUBTASK.
 
 This method is not supported in archive mode.
Parameters:name - The name of the task template from which the subtask is to be created
    and started. The currently valid template is then instantiated. A WrongStateException
    is thrown when the currently valid template is stopped.namespace - The namespace of the task template.parentTaskID - A string representation of the task instance ID that identifies
    the parent task instance.input - The input message.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:TKIID -
    The task instance ID of the subtask created.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongFormatException
IdWrongTypeException
InvalidApplicationStateException
InvalidLengthException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
ParallelRoutingTaskException
ParameterNullException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
SubTasksNotSupportedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when starting of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- createAndStartTaskAsSubTask
TKIID createAndStartTaskAsSubTask(java.lang.String name,
                                java.lang.String namespace,
                                TKIID parentTaskID,
                                ClientObjectWrapper input)
                                  throws AdministratorCannotBeResolvedException,
                                         ApplicationVetoException,
                                         ArchiveUnsupportedOperationException,
                                         CannotCreateWorkItemException,
                                         IdWrongFormatException,
                                         InvalidApplicationStateException,
                                         InvalidLengthException,
                                         NotAuthorizedException,
                                         UserDoesNotExistException,
                                         ObjectDoesNotExistException,
                                         ParallelRoutingTaskException,
                                         ParameterNullException,
                                         SCAServiceAccessFailureException,
                                         SCAServiceResultErrorException,
                                         SchedulingFailedException,
                                         SubTasksNotSupportedException,
                                         WrongKindException,
                                         WrongMessageTypeException,
                                         WrongStateException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Creates and starts a task instance as a subtask of the specified parent
 task instance using the parent task instance ID.
 The parent task instance is then waiting for the completion of the subtask. It can only
 be completed when all subtasks came to an end.
 
 The subtask created must be a collaboration or stand-alone invocation task. An invocation task
 must be derived from a task template that has not been created at Runtime. The parent task
 instance must be a collaboration or to-do task in the claimed state.
 It can be escalated or already waiting for a subtask. It can, however, not be suspended.
 
 Note that collaboration, invocation, and to-do task instances are also known as
 human, originating, and participating task instances.
 
 A subtask can only
 be created when the parent task supports subtask creation - refer to Task to
 view the task instance properties.
 
 The caller must be a potential instance creator or an administrator of the subtask template
 and an owner or administrator of the parent task instance.
 The caller becomes the originator of the subtask. When the subtask is an invocation aka originating task,
 then the caller also becomes the starter of the task.
 
 The action associated to this method is TaskTemplateActions.CREATEANDSTARTTASKASSUBTASK.
 
 This method is not supported in archive mode.
Parameters:name - The name of the task template from which the subtask is to be created
    and started. The currently valid template is then instantiated. A WrongStateException
    is thrown when the currently valid template is stopped.namespace - The namespace of the task template.parentTaskID - The task instance ID that identifies the parent task instance.input - The input message.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:TKIID -
    The task instance ID of the subtask created.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongFormatException
InvalidApplicationStateException
InvalidLengthException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
ParallelRoutingTaskException
ParameterNullException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
SubTasksNotSupportedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when starting of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- createAndStartTaskAsSubTask
TKIID createAndStartTaskAsSubTask(TaskModel taskModel,
                                java.lang.String applicationName,
                                java.lang.String parentTaskID,
                                ClientObjectWrapper input)
                                  throws AdministratorCannotBeResolvedException,
                                         ApplicationVetoException,
                                         ArchiveUnsupportedOperationException,
                                         CannotCreateWorkItemException,
                                         IdWrongFormatException,
                                         IdWrongTypeException,
                                         InvalidLengthException,
                                         NotAuthorizedException,
                                         UserDoesNotExistException,
                                         ObjectDoesNotExistException,
                                         ParallelRoutingTaskException,
                                         ParameterNullException,
                                         SCAServiceAccessFailureException,
                                         SCAServiceResultErrorException,
                                         SchedulingFailedException,
                                         SubTasksNotSupportedException,
                                         TaskDeploymentException,
                                         TELValidationException,
                                         WrongMessageTypeException,
                                         WrongKindException,
                                         WrongStateException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Creates and starts a task from the specified task model as a subtask of the
 specified parent task instance using a string representation of the task instance ID.
 The parent task instance is then waiting for the completion of the subtask. It can only
 be completed when all subtasks came to an end.
 
 The subtask created must be a collaboration or stand-alone invocation task.
 The parent task instance must be a collaboration or to-do task in the claimed state.
 
 Collaboration, invocation, and to-do task instances are also known as
 human, originating, and participating task instances.
 
 A subtask can only
 be created when the parent task supports subtask creation - refer to Task to
 view the task instance properties.
 
 The caller must have potential-instance-creator rights on the associated application component
 and be an owner or administrator of the parent task instance.
 The caller becomes the originator of the subtask. When the subtask is an invocation aka originating task,
 then the caller also becomes the starter of the task.
 The subtask inherits the context of the parent.
 
 The action associated to this method is TaskTemplateActions.CREATEANDSTARTTASKASSUBTASK.
 
 This method is not supported in archive mode.
Parameters:taskModel - The model that describes the subtask to be created at Runtime.applicationName - The name of the enterprise application that contains the message
    or business calendar definitions used in the TaskModel.
    If the message definitions are simple types only or if you do not use a business
    calendar, null may be specified.parentTaskID - Astring representation of the task instance ID that identifies the parent
    task instance.input - The input message.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:TKIID -
    The task instance ID of the subtask created and run.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
ParallelRoutingTaskException
ParameterNullException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
SubTasksNotSupportedException
TaskDeploymentException
TELValidationException
WrongMessageTypeException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when starting of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- createAndStartTaskAsSubTask
TKIID createAndStartTaskAsSubTask(TaskModel taskModel,
                                java.lang.String applicationName,
                                TKIID parentTaskID,
                                ClientObjectWrapper input)
                                  throws AdministratorCannotBeResolvedException,
                                         ApplicationVetoException,
                                         ArchiveUnsupportedOperationException,
                                         CannotCreateWorkItemException,
                                         IdWrongFormatException,
                                         InvalidLengthException,
                                         NotAuthorizedException,
                                         UserDoesNotExistException,
                                         ObjectDoesNotExistException,
                                         ParallelRoutingTaskException,
                                         ParameterNullException,
                                         SCAServiceAccessFailureException,
                                         SCAServiceResultErrorException,
                                         SchedulingFailedException,
                                         SubTasksNotSupportedException,
                                         TaskDeploymentException,
                                         TELValidationException,
                                         WrongMessageTypeException,
                                         WrongKindException,
                                         WrongStateException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Creates and starts a task from the specified task model as a subtask of the
 specified parent task instance using the task instance ID.
 The parent task instance is then waiting for the completion of the subtask. It can only
 be completed when all subtasks came to an end.
 
 The subtask created must be a collaboration or stand-alone invocation task.
 The parent task instance must be a collaboration or to-do task
 in the claimed state.
 
 Collaboration, invocation, and to-do task instances are also known as
 human, originating, and participating task instances.
 
 A subtask can only
 be created when the parent task supports subtask creation - refer to Task to
 view the task instance properties.
 
 The caller must have potential-instance-creator rights on the associated application component
 and be an owner or administrator of the parent task instance.
 The caller becomes the originator of the subtask. When the subtask is an invocation aka originating task,
 then the caller also becomes the starter of the task.
 The subtask inherits the context of the parent.
 
 The action associated to this method is TaskTemplateActions.CREATEANDSTARTTASKASSUBTASK.
 
 This method is not supported in archive mode.
Parameters:taskModel - The model that describes the subtask to be created at Runtime.applicationName - The name of the enterprise application that contains the message
    or business calendar definitions used in the TaskModel.
    If the message definitions are simple types only or if you do not use a business
    calendar, null may be specified.parentTaskID - The task instance ID that identifies the parent task instance.input - The input message.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:TKIID -
    The task instance ID of the subtask created and run.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongFormatException
InvalidLengthException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
ParallelRoutingTaskException
ParameterNullException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
SubTasksNotSupportedException
TaskDeploymentException
TELValidationException
WrongMessageTypeException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when starting of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- createFaultMessage
ClientObjectWrapper createFaultMessage(java.lang.String identifier,
                                     java.lang.String faultName)
                                       throws ArchiveUnsupportedOperationException,
                                              IdWrongFormatException,
                                              IdWrongTypeException,
                                              InvalidQNameException,
                                              NotAuthorizedException,
                                              ObjectDoesNotExistException,
                                              ParameterNullException,
                                              WrongKindException,
                                              WrongStateException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
Creates a fault message for a fault that is defined by the specified task instance
 or template
 using a string representation of the task instance or template ID.
 This method creates a message that can be used when unsuccessfully completing a task instance -
 refer to complete.
 
 The task instance or template must be a to-do, collaboration, or invocation task.
 Collaboration, to-do, and invocation tasks are also known as
 human, participating, and originating tasks.
 
 The task instance can be in any state. The task template must be started.
 
 The action associated to this method is TaskTemplateActions.CREATEFAULTMESSAGE or
 TaskActions.CREATEFAULTMESSAGE.
 
 This method is not supported in archive mode.
Parameters:identifier - A string representation of the task instance or template ID that
    is used to identify the task instance or template.faultName - The name of the fault for which a message is to be created. The fault name
    must identify a fault that is defined for the task instance or template. Refer
    to getFaultNames(TKIID) or
    to getFaultNames(TKTID).
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when the specified
    fault cannot be found for the task instance.
 
Throws:
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
InvalidQNameException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Supports task templates.

- createFaultMessage
ClientObjectWrapper createFaultMessage(TKTID tktid,
                                     java.lang.String faultName)
                                       throws ArchiveUnsupportedOperationException,
                                              IdWrongFormatException,
                                              ObjectDoesNotExistException,
                                              ParameterNullException,
                                              WrongKindException,
                                              WrongStateException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
Creates a fault message for a fault that is defined by the specified task template
 using the task template ID.
 This method creates a message that can be used when unsuccessfully completing a task instance
 derived from the specified template -
 refer to complete.
 
 The task template must be a to-do, collaboration, or invocation task.
 Collaboration, to-do, and invocation tasks are also known as
 human, participating, and originating tasks.
 
 The task template must be started.
 
 The action associated to this method is TaskTemplateActions.CREATEFAULTMESSAGE.
 
 This method is not supported in archive mode.
Parameters:tktid - The task template ID that is used to identify the task template.faultName - The name of the fault for which a message is to be created. The fault name
    must identify a fault that is defined for the task template. Refer
    to getFaultNames.
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when the specified
    fault cannot be found for the task instance.
 
Throws:
ArchiveUnsupportedOperationException
IdWrongFormatException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createFaultMessage
ClientObjectWrapper createFaultMessage(TKIID tkiid,
                                     java.lang.String faultName)
                                       throws ArchiveUnsupportedOperationException,
                                              IdWrongFormatException,
                                              InvalidQNameException,
                                              NotAuthorizedException,
                                              ObjectDoesNotExistException,
                                              ParameterNullException,
                                              WrongKindException,
                                              WrongStateException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
Creates a fault message for a fault that is defined by the specified task instance
 using the task instance ID.
 This method creates a message that can be used when unsuccessfully completing a task -
 refer to complete.
 
 The task instance must be a to-do, collaboration, or invocation task.
 Collaboration, to-do, and invocation task instances are also known as
 human, participating, and originating task instances.
 
 The task instance can be in any state.
 
 The action associated to this method is TaskActions.CREATEFAULTMESSAGE.
 
 This method is not supported in archive mode.
Parameters:tkiid - The task instance ID that is used to identify the task instance.faultName - The name of the fault for which a message is to be created. The fault name
    must identify a fault that is defined for the task instance. Refer
    to getFaultNames.
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when the specified
    fault cannot be found for the task instance.
 
Throws:
ArchiveUnsupportedOperationException
IdWrongFormatException
InvalidQNameException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 The task instance can be in any state.

- createInputMessage
ClientObjectWrapper createInputMessage(java.lang.String identifier)
                                       throws ArchiveUnsupportedOperationException,
                                              IdWrongFormatException,
                                              IdWrongTypeException,
                                              NotAuthorizedException,
                                              ObjectDoesNotExistException,
                                              WrongKindException,
                                              WrongStateException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
Creates an input message for the specified task instance or template
 using a string representation of the task instance or template ID.
 For example, create a message that can be used when starting a task.
 
 The task template must be started.
 
 The action associated to this method is TaskTemplateActions.CREATEINPUTMESSAGE or
 TaskActions.CREATEINPUTMESSAGE.
 
 This method is not supported in archive mode.
Parameters:identifier - A string representation of the task instance or template ID
    that is used to identify the task instance or template.
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when
  the task does not expect an input message.
 
Throws:
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 The task template must be started. The task instance can be in any state.

- createInputMessage
ClientObjectWrapper createInputMessage(TKIID tkiid)
                                       throws ArchiveUnsupportedOperationException,
                                              IdWrongFormatException,
                                              NotAuthorizedException,
                                              ObjectDoesNotExistException,
                                              WrongKindException,
                                              WrongStateException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
Creates an input message for the specified task instance
 using the task instance ID.
 For example, create a message that can be used when starting a task.
 
 The action associated to this method is TaskActions.CREATEINPUTMESSAGE.
 
 This method is not supported in archive mode.
Parameters:tkiid - The task instance ID that is used to identify the task instance.
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when
  the task does not expect an input message.
 
Throws:
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 The task instance can be in any state.

- createInputMessage
ClientObjectWrapper createInputMessage(TKTID tktid)
                                       throws ArchiveUnsupportedOperationException,
                                              IdWrongFormatException,
                                              NotAuthorizedException,
                                              ObjectDoesNotExistException,
                                              WrongKindException,
                                              WrongStateException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
Creates an input message for the specified task template
 using the task template ID.
 For example, create a message that can be used when starting a task.
 
 The task template must be started.
 
 The action associated to this method is TaskTemplateActions.CREATEINPUTMESSAGE.
 
 This method is not supported in archive mode.
Parameters:tktid - The task template ID that is used to identify the task template.
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when
  an input message is not expected.
 
Throws:
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 The task template must be started.

- createMessage
ClientObjectWrapper createMessage(java.lang.String tkiid,
                                java.lang.String messageTypeName)
                                  throws ArchiveUnsupportedOperationException,
                                         IdWrongFormatException,
                                         IdWrongTypeException,
                                         NotAuthorizedException,
                                         ObjectDoesNotExistException,
                                         ParameterNullException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Deprecated. As of version 6.0, replaced by createInputMessage,
 createOutputMessage, and
 createFaultMessage.
Creates a message defined by the specified task instance
 using a string representation of the task instance ID.
 For example, create a message that can be used when completing a task.
 
 The caller must have at least reader authority for the task instance.
 
 This method is not supported in archive mode.
Parameters:tkiid - A String representation of the task instance ID that is used
    to identify the task instance for which a message is to be created.messageTypeName - The name of the message type for which a message is to be created.
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when the specified
    message type cannot be found.
 
Throws:
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createMessage
ClientObjectWrapper createMessage(TKIID tkiid,
                                java.lang.String messageTypeName)
                                  throws ArchiveUnsupportedOperationException,
                                         IdWrongFormatException,
                                         NotAuthorizedException,
                                         ObjectDoesNotExistException,
                                         ParameterNullException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Deprecated. As of version 6.0, replaced by createInputMessage,
 createOutputMessage, and
 createFaultMessage.
Creates a message defined by the specified task instance
 using the task instance ID.
 For example, create a message that can be used to complete a task instance.
 
 The caller must have at least reader authority for the task instance.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID of the task instance for which a message is to be created.messageTypeName - The name of the message type for which a message is to be created.
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when the specified
    message type cannot be found.
 
Throws:
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createOutputMessage
ClientObjectWrapper createOutputMessage(java.lang.String identifier)
                                        throws ArchiveUnsupportedOperationException,
                                               IdWrongFormatException,
                                               IdWrongTypeException,
                                               NotAuthorizedException,
                                               ObjectDoesNotExistException,
                                               WrongKindException,
                                               WrongStateException,
                                               UnexpectedFailureException,
                                               java.rmi.RemoteException,
                                               javax.ejb.EJBException
Creates an output message for the specified task instance or template
 using a string representation of the task instance or template ID.
 For example, creates a message that can be used when completing a task instance.
 
 The task instance or template must be a to-do, collaboration, or invocation task.
 Collaboration, to-do, and invocation tasks are also known as
 human, participating, and originating tasks.
 
 The task instance can be in any state. The task template must be started.
 
 The action associated to this method is TaskTemplateActions.CREATEOUTPUTMESSAGE or
 TaskActions.CREATEOUTNPUTMESSAGE.
 
 This method is not supported in archive mode.
Parameters:identifier - A string representation of the task instance or template ID
    that is used to identify the task instance or template.
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when
    the task does not return an output message.
 
Throws:
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Supports task templates.

- createOutputMessage
ClientObjectWrapper createOutputMessage(TKTID tktid)
                                        throws ArchiveUnsupportedOperationException,
                                               IdWrongFormatException,
                                               ObjectDoesNotExistException,
                                               WrongKindException,
                                               WrongStateException,
                                               UnexpectedFailureException,
                                               java.rmi.RemoteException,
                                               javax.ejb.EJBException
Creates an output message for the specified task template
 using the task template ID.
 For example, creates a message that can be used when completing a task derived from the task template.
 
 The task template must be a to-do, collaboration, or invocation task.
 Collaboration, to-do, and invocation tasks are also known as
 human, participating, and originating tasks.
 
 The task template must be started.
 
 The action associated to this method is TaskTemplateActions.CREATEOUTPUTMESSAGE.
 
 This method is not supported in archive mode.
Parameters:tktid - The task template ID that is used to identify the task template.
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when
    the task does not return an output message.
 
Throws:
ArchiveUnsupportedOperationException
IdWrongFormatException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createOutputMessage
ClientObjectWrapper createOutputMessage(TKIID tkiid)
                                        throws ArchiveUnsupportedOperationException,
                                               IdWrongFormatException,
                                               NotAuthorizedException,
                                               ObjectDoesNotExistException,
                                               WrongKindException,
                                               WrongStateException,
                                               UnexpectedFailureException,
                                               java.rmi.RemoteException,
                                               javax.ejb.EJBException
Creates an output message for the specified task instance
 using the task instance ID.
 For example, creates a message that can be used when completing a task instance.
 
 The task instance must be a to-do, collaboration, or invocation task.
 Collaboration, to-do, and invocation task instances are also known as
 human, participating, and originating task instances.
 
 The task instance can be in any state.
 
 The action associated to this method is TaskActions.CREATEOUTPUTMESSAGE.
 
 This method is not supported in archive mode.
Parameters:tkiid - The task instance ID that is used to identify the task instance.
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when
    the task does not return an output message.
 
Throws:
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 The task instance can be in any state.

- createStoredQuery void createStoredQuery(java.lang.String storedQueryName, java.lang.String selectClause, java.lang.String whereClause, java.lang.String orderByClause, java.lang.Integer threshold, java.util.TimeZone timeZone) throws InvalidLengthException , NotAuthorizedException , ParameterNullException , StoredQueryNameNotUniqueException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Creates a query definition and persistently stores it in the database. If this method is called by a task system administrator, then a stored query is created that is available for public usage. If this method is called by a regular user, then a stored query is created that is privately available for the logged-on user. A stored query represents a set of selected object properties. The number of tuples in the set can be restricted by a filter or threshold. When executing the stored query, that set can additionally be restricted by specifying a starting tuple parameter. To allow for the re-use of stored queries, parameters can be specified in the where-clause so that, for example, the owner of tasks can be specified when the stored query is executed. Besides defining filtering criteria, sort criteria can be defined that are applied on the server. Sorting on the server means that the locale of the server is used. Specify the parameters of the query definition, the select-, where-, and order-by-clause, using SQL based on the published views. Execution of the query can thus be shifted to SQL and becomes portable and optimizable. Note, however, when you use a combination of the order-by-clause, threshold, or skipTuples parameters, the tuples returned depend on your database system. For example, some database systems order all records and then return the requested number of tuples. Other database systems first take the requested number of tuples and then apply the order criteria. The domain of the query, that is, the SQL from-clause, is determined automatically. In principle, all properties of objects are selectable for which you own a work item or which can be transitively reached via your work item. As a rule of thumb, all objects except task templates can be reached via work items. This means that you cannot use task template properties only but that you must specify a non task template property in the select- or where-clause. Note that a task system administrator has special rights and can retrieve information on objects associated to other users. When the stored query is executed by a task system administrator, the selected properties of all objects for which there are work items are returned, no matter whether there is a personally owned work item or another user's work item. Although stored query definitions are stored persistently, object properties contained in the result set are assembled dynamically when they are queried. Refer to query for the execution of stored queries. When a stored query definition needs to be updated, it must be deleted and recreated - refer to deleteStoredQuery for the deletion of stored queries. Parameters: storedQueryName - The name of the stored query to be created; must not be greater than 64 bytes in UTF-8 format. The name must be unique. selectClause - Describes the query result that is returned when the stored query is executed. Its syntax is an SQL select-clause. It either declares a list of names that identify the object properties (columns of the result) to be returned or it specifies the COUNT keyword. Aggregation functions like AVG, SUM, MIN, and MAX are not supported. Each part of the select-clause separated by a comma must specify a property from the published views - see the InfoCenter for details. To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the view name. For example, "TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE". To count the number of potentially qualifying tuples, use the COUNT keyword. For example, to count the number of task instance IDs that satisfy the where-clause, specify a select-clause such as "COUNT(DISTINCT TASK.TKIID)". If you use the more generic "COUNT(*)", then you must specify a where-clause so that the tuples to be counted can be determined. For example, to count all tasks, specify a where-clause such as "TASK.TKIID=TASK.TKIID" that always evaluates to true. A selectClause must not be greater than 512 bytes in UTF-8 format. The QueryResultSet contains columns in the same order as specified in the selectClause. If tuples are to be counted, an int value is returned (row 1, column 1). whereClause - Specifies the search condition that is applied when the stored query is executed. Its syntax is an SQL where-clause. The following rules apply: If a filter is not to be applied, null must be specified. A whereClause must not be greater than 2047 bytes in UTF-8 format. orderByClause - Orders the result of the stored query execution by the values of the columns you identify. Its syntax is an SQL order-by-clause. Each part of the order-by-clause separated by a comma must specify a property from the published views. If you identify more that one property, the stored query execution result is ordered by the values of the first property you identify, then by the values of the second property, and so on. If sort criteria are not to be applied, null must be specified. An orderByClause must not be greater than 254 bytes in UTF-8 format. Note that sort criteria are applied on the server, that is, the locale of the server is used for sorting. threshold - The maximum number of stored query execution result tuples to be returned from the server to the client. If a threshold is not to be applied, null must be specified. timeZone - Specifies the time zone of the timestamp constants in the whereClause respectively the time zone for the timestamp values returned. If a timezone is not specified, UTC is assumed. Throws: InvalidLengthException NotAuthorizedException ParameterNullException StoredQueryNameNotUniqueException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.0 Change History Release Modification 6.0.2 Can create a private stored query.

#### createStoredQuery

```
void createStoredQuery(java.lang.String storedQueryName,
                     java.lang.String selectClause,
                     java.lang.String whereClause,
                     java.lang.String orderByClause,
                     java.lang.Integer threshold,
                     java.util.TimeZone timeZone)
                       throws InvalidLengthException,
                              NotAuthorizedException,
                              ParameterNullException,
                              StoredQueryNameNotUniqueException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
```

A stored query represents a set of selected object properties. The number of tuples in the set
 can be restricted by a filter or threshold. When executing the stored query, that set
 can additionally be restricted by specifying a starting tuple parameter.
 
 To allow for the re-use of stored queries, parameters can be specified in the where-clause
 so that, for example, the owner of tasks can be specified when the stored query is executed.
 
 Besides defining filtering criteria, sort criteria can be defined that are applied on the server.
 Sorting on the server means that the locale of the server is used.
 
 Specify the parameters of the query definition, the select-, where-, and order-by-clause,
 using SQL based on the published views.
 Execution of the query can thus be shifted to SQL and becomes portable and optimizable.
 
 Note, however, when you use a combination of the order-by-clause, threshold, or skipTuples
 parameters, the tuples returned depend on your database system.
 For example, some database systems order all records and then return the requested number of tuples.
 Other database systems first take the requested number of tuples and then apply the order criteria.
 
 The domain of the query, that is, the SQL from-clause, is determined automatically.
 In principle, all properties of objects are selectable for which you own a work item
 or which can be transitively reached via your work item.
 As a rule of thumb, all objects except task templates can be reached via work items.
 This means that you cannot use task template properties only but that you
 must specify a non task template property in the select- or where-clause.
 
 Note that a task system administrator has special rights and can retrieve
 information on objects associated to other users. When the stored query is executed by
 a task system administrator, the selected properties of all objects for which there are
 work items are returned, no matter whether there is a personally
 owned work item or another user's work item.
 
 Although stored query definitions are stored persistently, object properties contained in
 the result set are assembled dynamically when they are queried.
 Refer to query for the execution of stored queries.
 
 When a stored query definition needs to be updated, it must be deleted and recreated -
 refer to deleteStoredQuery for the deletion of
 stored queries.

It either declares a list of names that identify the object properties (columns of the result)
    to be returned or it specifies the COUNT keyword. Aggregation functions like AVG, SUM,
    MIN, and MAX are not supported.
    
    Each part of the select-clause separated by a comma must specify a property from the
    published views - see the InfoCenter for details.
    
    To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the
    view name. For example, "TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE".
    
    To count the number of potentially qualifying tuples, use the COUNT keyword.
    For example, to count the number of task instance IDs that satisfy the
    where-clause, specify a select-clause such as "COUNT(DISTINCT TASK.TKIID)".
    If you use the more generic "COUNT(*)", then you must specify a where-clause
    so that the tuples to be counted can be determined.
    For example, to count all tasks,
    specify a where-clause such as "TASK.TKIID=TASK.TKIID" that always evaluates to true.
    
    A selectClause must not be greater than 512 bytes in UTF-8 format.
    
    The QueryResultSet contains columns in the same order
    as specified in the selectClause. If tuples are to be counted, an int value is returned
    (row 1, column 1).

    - Specify object ID constants as ID('string-rep-of-oid').
    Specify timestamp constants as TS('yyyy-mm-ddThh:mm:ss') or as CURRENT\_DATE
    for comparisons with the current date.
    

    The date and time parts of a TS definition are optional; either the date or the time must
    be specified. If no date part of a TS definition is specified, the current date is taken.
    Optional time values that are not specified are set to zero.
    The timestamp is 24 hours based.
    For example, TS('16:04') is the same as TS('2002-12-24T16:04:00') provided that the
    current date is December 24th, 2002.
    

    If a date part of a TS definition is specified, the year must consist of 4 letters;
    the month and day specifications are optional.
    Missing month and day specifications are set to 01. For example, specifying
    TS('2003') is the same as specifying TS('2003-01-01T00:00:00').
    Specify binary constants as BIN('UTF-8 string').
    Use constants
    instead of integer enumerations. For example, instead of specifying a task instance state expression
    "TASK.STATE=2" , specify "TASK.STATE=TASK.STATE.STATE\_READY".
    Duplicate apostrophes (') in comparising values. For example,
    "TASK\_CPROP.STRING\_VALUE='d''automatisation'".
    To specify a where clause that refers to properties of name-value pairs, like
    custom properties, add a one-digit suffix (0-9) to the view name.
    

    For example, to have only tuples returned where a task custom property "prop1" has
    the value "v1" or where a task custom property "prop2" has the value v2", the where clause
    can look like
    "TASK\_CPROP1.NAME='prop1' AND TASK\_CPROP1.STRING\_VALUE='v1' OR
    TASK\_CPROP2.NAME='prop2' AND TASK\_CPROP2.STRING\_VALUE = 'v2'".
    For performance reasons, you should not use more than one "OR" construct; use "IN" instead.
    

    For example, to retrieve the values of custom properties "prop1" and "prop2" of all task instances,
    the select clause can look like
    "DISTINCT TASK.TKIID, TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE" and the where-clause
    "TASK\_CPROP1.NAME = 'prop1' AND TASK\_CPROP2.NAME = 'prop2'".
    Specify parameters as @param followed by a number suffix. The number of the
    first parameter must be 1, of the second 2, and so on.
    For example, "TASK\_CPROP.NAME = '@param1'".
    

    The same parameter can be used multiple times.
    Parameters are replaced by strings when the stored query is executed -
    see query.

If a filter is not to be applied, null must be specified.
    
    A whereClause must not be greater than 2047 bytes in UTF-8 format.

If you identify more that one property, the stored query execution result is ordered by the
    values of the first property you identify, then by the values of the second property,
    and so on.
    
    If sort criteria are not to be applied, null must be specified.
    An orderByClause must not be greater than 254 bytes in UTF-8 format.
    
    Note that sort criteria are applied on the server, that is, the locale of the
    server is used for sorting.

Change History

Release
 Modification
 
6.0.2
 
 Can create a private stored query.

- createStoredQuery void createStoredQuery(java.lang.String storedQueryName, java.lang.String selectClause, java.lang.String whereClause, java.lang.String orderByClause, java.lang.Integer threshold, java.util.TimeZone timeZone, java.util.List storedQueryProperties, java.lang.String clientType) throws InvalidLengthException , InvalidParameterException , ParameterNullException , StoredQueryNameNotUniqueException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Creates a query definition and specifies properties to be stored together with the query. If this method is called by a task system administrator, then a stored query is created that is available for public usage. If this method is called by a regular user, then a stored query is created that is privately available for the calling logged-on user. A stored query represents a set of selected object properties. The number of tuples in the set can be restricted by a filter or threshold. When executing the stored query, that set can additionally be restricted by specifying a starting tuple parameter. To allow for the re-use of stored queries, parameters can be specified in the where-clause so that, for example, the owner of tasks can be specified when the stored query is executed. Besides defining filtering criteria, sort criteria can be defined that are applied on the server. This means that the locale of the server is used for sorting. Specify the parameters of the query definition, the select-, where-, and order-by-clause, using SQL based on the published views. Execution of the query can thus be shifted to SQL and becomes portable and optimizable. Note, however, when you use a combination of the order-by-clause, threshold, or skipTuples parameters, the tuples returned depend on your database system. For example, some database systems order all records and then return the requested number of tuples. Other database systems first take the requested number of tuples and then apply the order criteria. The domain of the query, that is, the SQL from-clause, is determined automatically. In principle, all properties of objects are selectable for which you own a work item or which can be transitively reached via your work item. As a rule of thumb, all objects except task templates can be reached via work items. This means that you cannot use task template properties only but that you must specify a non task template property in the select- or where-clause. Note that a task system administrator has special rights and can retrieve information on objects associated to other users. When the stored query is executed by a task system administrator, the selected properties of all objects for which there are work items are returned, no matter whether there is a personally owned work item or another user's work item. Although stored query definitions are stored persistently, object properties contained in the result set are assembled dynamically when they are queried. Refer to query for the execution of stored queries. When a stored query definition needs to be updated, it must be deleted and recreated - refer to deleteStoredQuery for the deletion of stored queries. Parameters: storedQueryName - The name of the stored query to be created; must not be greater than 64 bytes in UTF-8 format. The name must be unique. selectClause - Describes the query result that is returned when the stored query is executed. Its syntax is an SQL select-clause. It either declares a list of names that identify the object properties (columns of the result) to be returned or it specifies the COUNT keyword. Aggregation functions like AVG, SUM, MIN, and MAX are not supported. Each part of the select-clause separated by a comma must specify a property from the published views - see the InfoCenter for details. To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the view name. For example, "TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE". To count the number of potentially qualifying tuples, use the COUNT keyword. For example, to count the number of task instance IDs that satisfy the where-clause, specify a select-clause such as "COUNT(DISTINCT TASK.TKIID)". If you use the more generic "COUNT(*)", then you must specify a where-clause so that the tuples to be counted can be determined. For example, to count all tasks, specify a where-clause such as "TASK.TKIID=TASK.TKIID" that always evaluates to true. A selectClause must not be greater than 512 bytes in UTF-8 format. The QueryResultSet contains columns in the same order as specified in the selectClause. If tuples are to be counted, an int value is returned (row 1, column 1). whereClause - Specifies the search condition that is applied when the stored query is executed. Its syntax is an SQL where-clause. The following rules apply: If a filter is not to be applied, null must be specified. A whereClause must not be greater than 2047 bytes in UTF-8 format. orderByClause - Orders the result of the stored query execution by the values of the columns you identify. Its syntax is an SQL order-by-clause. Each part of the order-by-clause separated by a comma must specify a property from the published views. If you identify more that one property, the stored query execution result is ordered by the values of the first property you identify, then by the values of the second property, and so on. If sort criteria are not to be applied, null must be specified. An orderByClause must not be greater than 254 bytes in UTF-8 format. Note that sort criteria are applied on the server, that is, the locale of the server is used for sorting. threshold - The maximum number of stored query execution result tuples to be returned from the server to the client. If a threshold is not to be applied, null must be specified. timeZone - Specifies the time zone of the timestamp constants in the whereClause respectively the time zone for the timestamp values returned. If a timezone is not specified, UTC is assumed. storedQueryProperties - Specifies user-defined properties to be attached to the stored query. Must be a list of StoredQueryProperty objects - see StoredQueryProperty . If no properties are to be attached, null must be passed. clientType - A user-defined client type to specify the creator of the stored query, for example, Web, Portal, or Custom. The client type must not be greater than 128 bytes in UTF-8 format. Throws: InvalidLengthException InvalidParameterException ParameterNullException StoredQueryNameNotUniqueException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.0.2

#### createStoredQuery

```
void createStoredQuery(java.lang.String storedQueryName,
                     java.lang.String selectClause,
                     java.lang.String whereClause,
                     java.lang.String orderByClause,
                     java.lang.Integer threshold,
                     java.util.TimeZone timeZone,
                     java.util.List storedQueryProperties,
                     java.lang.String clientType)
                       throws InvalidLengthException,
                              InvalidParameterException,
                              ParameterNullException,
                              StoredQueryNameNotUniqueException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
```

A stored query represents a set of selected object properties. The number of tuples in the set
 can be restricted by a filter or threshold. When executing the stored query, that set
 can additionally be restricted by specifying a starting tuple parameter.
 
 To allow for the re-use of stored queries, parameters can be specified in the where-clause
 so that, for example, the owner of tasks can be specified when the stored query is executed.
 
 Besides defining filtering criteria, sort criteria can be defined that are applied on the server.
 This means that the locale of the server is used for sorting.
 
 Specify the parameters of the query definition, the select-, where-, and order-by-clause,
 using SQL based on the published views.
 Execution of the query can thus be shifted to SQL and becomes portable and optimizable.
 
 Note, however, when you use a combination of the order-by-clause, threshold, or skipTuples
 parameters, the tuples returned depend on your database system.
 For example, some database systems order all records and then return the requested number of tuples.
 Other database systems first take the requested number of tuples and then apply the order criteria.
 
 The domain of the query, that is, the SQL from-clause, is determined automatically.
 In principle, all properties of objects are selectable for which you own a work item
 or which can be transitively reached via your work item.
 As a rule of thumb, all objects except task templates can be reached via work items.
 This means that you cannot use task template properties only but that you
 must specify a non task template property in the select- or where-clause.
 
 Note that a task system administrator has special rights and can retrieve
 information on objects associated to other users. When the stored query is executed by
 a task system administrator, the selected properties of all objects for which there are
 work items are returned, no matter whether there is a personally
 owned work item or another user's work item.
 
 Although stored query definitions are stored persistently, object properties contained in
 the result set are assembled dynamically when they are queried.
 Refer to query for the execution of stored queries.
 
 When a stored query definition needs to be updated, it must be deleted and recreated -
 refer to deleteStoredQuery for the deletion of
 stored queries.

It either declares a list of names that identify the object properties (columns of the result)
    to be returned or it specifies the COUNT keyword. Aggregation functions like AVG, SUM,
    MIN, and MAX are not supported.
    
    Each part of the select-clause separated by a comma must specify a property from the
    published views - see the InfoCenter for details.
    
    To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the
    view name. For example, "TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE".
    
    To count the number of potentially qualifying tuples, use the COUNT keyword.
    For example, to count the number of task instance IDs that satisfy the
    where-clause, specify a select-clause such as "COUNT(DISTINCT TASK.TKIID)".
    If you use the more generic "COUNT(*)", then you must specify a where-clause
    so that the tuples to be counted can be determined.
    For example, to count all tasks,
    specify a where-clause such as "TASK.TKIID=TASK.TKIID" that always evaluates to true.
    
    A selectClause must not be greater than 512 bytes in UTF-8 format.
    
    The QueryResultSet contains columns in the same order
    as specified in the selectClause. If tuples are to be counted, an int value is returned
    (row 1, column 1).

    - Specify object ID constants as ID('string-rep-of-oid').
    Specify timestamp constants as TS('yyyy-mm-ddThh:mm:ss') or as CURRENT\_DATE
    for comparisons with the current date.
    

    The date and time parts of a TS definition are optional; either the date or the time must
    be specified. If no date part of a TS definition is specified, the current date is taken.
    Optional time values that are not specified are set to zero.
    The timestamp is 24 hours based.
    For example, TS('16:04') is the same as TS('2002-12-24T16:04:00') provided that the
    current date is December 24th, 2002.
    

    If a date part of a TS definition is specified, the year must consist of 4 letters;
    the month and day specifications are optional.
    Missing month and day specifications are set to 01. For example, specifying
    TS('2003') is the same as specifying TS('2003-01-01T00:00:00').
    Specify binary constants as BIN('UTF-8 string').
    Use constants
    instead of integer enumerations. For example, instead of specifying a task instance state expression
    "TASK.STATE=2" , specify "TASK.STATE=TASK.STATE.STATE\_READY".
    Duplicate apostrophes (') in comparising values. For example,
    "TASK\_CPROP.STRING\_VALUE='d''automatisation'".
    To specify a where clause that refers to properties of name-value pairs, like
    custom properties, add a one-digit suffix (0-9) to the view name.
    

    For example, to have only tuples returned where a task custom property "prop1" has
    the value "v1" or where a task custom property "prop2" has the value v2", the where clause
    can look like
    "TASK\_CPROP1.NAME='prop1' AND TASK\_CPROP1.STRING\_VALUE='v1' OR
    TASK\_CPROP2.NAME='prop2' AND TASK\_CPROP2.STRING\_VALUE = 'v2'".
    For performance reasons, you should not use more than one "OR" construct; use "IN" instead.
    

    For example, to retrieve the values of custom properties "prop1" and "prop2" of all task instances,
    the select clause can look like
    "DISTINCT TASK.TKIID, TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE" and the where-clause
    "TASK\_CPROP1.NAME = 'prop1' AND TASK\_CPROP2.NAME = 'prop2'".
    Specify parameters as @param followed by a number suffix. The number of the
    first parameter must be 1, of the second 2, and so on.
    For example, "TASK\_CPROP.NAME = '@param1'".
    

    The same parameter can be used multiple times.
    Parameters are replaced by strings when the stored query is executed -
    see query.

If a filter is not to be applied, null must be specified.
    
    A whereClause must not be greater than 2047 bytes in UTF-8 format.

If you identify more that one property, the stored query execution result is ordered by the
    values of the first property you identify, then by the values of the second property,
    and so on.
    
    If sort criteria are not to be applied, null must be specified.
    An orderByClause must not be greater than 254 bytes in UTF-8 format.
    
    Note that sort criteria are applied on the server, that is, the locale of the
    server is used for sorting.

- createStoredQuery void createStoredQuery(java.lang.String userID, java.lang.String storedQueryName, java.lang.String selectClause, java.lang.String whereClause, java.lang.String orderByClause, java.lang.Integer threshold, java.util.TimeZone timeZone, java.util.List storedQueryProperties, java.lang.String clientType) throws InvalidLengthException , InvalidParameterException , NotAuthorizedException , ParameterNullException , StoredQueryNameNotUniqueException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Creates a query definition for the specified user. A regular user can only create stored queries that are available for his personal usage. A task system administrator can create stored queries that are available for public usage or for the usage of the specified person. A stored query represents a set of selected object properties. The number of tuples in the set can be restricted by a filter or threshold. When executing the stored query, that set can additionally be restricted by specifying a starting tuple parameter. To allow for the re-use of stored queries, parameters can be specified in the where-clause so that, for example, the owner of tasks can be specified when the stored query is executed. Besides defining filtering criteria, sort criteria can be defined that are applied on the server. This means that the locale of the server is used for sorting. Specify the parameters of the query definition, the select-, where-, and order-by-clause, using SQL based on the published views. Execution of the query can thus be shifted to SQL and becomes portable and optimizable. Note, however, when you use a combination of the order-by-clause, threshold, or skipTuples parameters, the tuples returned depend on your database system. For example, some database systems order all records and then return the requested number of tuples. Other database systems first take the requested number of tuples and then apply the order criteria. The domain of the query, that is, the SQL from-clause, is determined automatically. In principle, all properties of objects are selectable for which you own a work item, or which can be transitively reached via your work item. As a rule of thumb, all objects except task templates can be reached via work items. This means that you cannot use task template properties only but that you must specify a non task template property in the select- or where-clause. Note that a task system administrator has special rights and can retrieve information on objects associated to other users. When the stored query is executed by a task system administrator, the selected properties of all objects for which there are work items are returned, no matter whether there is a personally owned work item or another user's work item. Although stored query definitions are stored persistently, object properties contained in the result set are assembled dynamically when they are queried. Refer to query for the execution of stored queries. When a stored query definition needs to be updated, it must be deleted and recreated - refer to deleteStoredQuery for the deletion of stored queries. Parameters: userID - The name of a user who is to become the owner of the stored query. Null means that a public stored query is created. storedQueryName - The name of the stored query to be created; must not be greater than 64 bytes in UTF-8 format. The name must be unique. selectClause - Describes the query result that is returned when the stored query is executed. Its syntax is an SQL select-clause. It either declares a list of names that identify the object properties (columns of the result) to be returned or it specifies the COUNT keyword. Aggregation functions like AVG, SUM, MIN, and MAX are not supported. Each part of the select-clause separated by a comma must specify a property from the published views - see the InfoCenter for details. To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the view name. For example, "TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE". To count the number of potentially qualifying tuples, use the COUNT keyword. For example, to count the number of task instance IDs that satisfy the where-clause, specify a select-clause such as "COUNT(DISTINCT TASK.TKIID)". If you use the more generic "COUNT(*)", then you must specify a where-clause so that the tuples to be counted can be determined. For example, to count all tasks, specify a where-clause such as "TASK.TKIID=TASK.TKIID" that always evaluates to true. A selectClause must not be greater than 512 bytes in UTF-8 format. The QueryResultSet contains columns in the same order as specified in the selectClause. If tuples are to be counted, an int value is returned (row 1, column 1). whereClause - Specifies the search condition that is applied when the stored query is executed. Its syntax is an SQL where-clause. The following rules apply: If a filter is not to be applied, null must be specified. A whereClause must not be greater than 2047 bytes in UTF-8 format. orderByClause - Orders the result of the stored query execution by the values of the columns you identify. Its syntax is an SQL order-by-clause. Each part of the order-by-clause separated by a comma must specify a property from the published views. If you identify more that one property, the stored query execution result is ordered by the values of the first property you identify, then by the values of the second property, and so on. If sort criteria are not to be applied, null must be specified. An orderByClause must not be greater than 254 bytes in UTF-8 format. Note that sort criteria are applied on the server, that is, the locale of the server is used for sorting. threshold - The maximum number of stored query execution result tuples to be returned from the server to the client. If a threshold is not to be applied, null must be specified. timeZone - Specifies the time zone of the timestamp constants in the whereClause respectively the time zone for the timestamp values returned. If a timezone is not specified, UTC is assumed. storedQueryProperties - Specifies user-defined properties to be attached to the stored query. Must be a list of StoredQueryProperty objects - see StoredQueryProperty . If no properties are to be attached, null must be passed. clientType - A user-defined client type to specify the creator of the stored query, for example, Web, Portal, or Custom. The client type must not be greater than 128 bytes in UTF-8 format. Throws: InvalidLengthException InvalidParameterException NotAuthorizedException ParameterNullException StoredQueryNameNotUniqueException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.0.2

#### createStoredQuery

```
void createStoredQuery(java.lang.String userID,
                     java.lang.String storedQueryName,
                     java.lang.String selectClause,
                     java.lang.String whereClause,
                     java.lang.String orderByClause,
                     java.lang.Integer threshold,
                     java.util.TimeZone timeZone,
                     java.util.List storedQueryProperties,
                     java.lang.String clientType)
                       throws InvalidLengthException,
                              InvalidParameterException,
                              NotAuthorizedException,
                              ParameterNullException,
                              StoredQueryNameNotUniqueException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
```

A regular user can only create stored queries that are available for his personal usage.
 A task system administrator can create stored queries that are available for public usage
 or for the usage of the specified person.
 
 A stored query represents a set of selected object properties. The number of tuples in the set
 can be restricted by a filter or threshold. When executing the stored query, that set
 can additionally be restricted by specifying a starting tuple parameter.
 
 To allow for the re-use of stored queries, parameters can be specified in the where-clause
 so that, for example, the owner of tasks can be specified when the stored query is executed.
 
 Besides defining filtering criteria, sort criteria can be defined that are applied on the server.
 This means that the locale of the server is used for sorting.
 
 Specify the parameters of the query definition, the select-, where-, and order-by-clause,
 using SQL based on the published views.
 Execution of the query can thus be shifted to SQL and becomes portable and optimizable.
 
 Note, however, when you use a combination of the order-by-clause, threshold, or skipTuples
 parameters, the tuples returned depend on your database system.
 For example, some database systems order all records and then return the requested number of tuples.
 Other database systems first take the requested number of tuples and then apply the order criteria.
 
 The domain of the query, that is, the SQL from-clause, is determined automatically.
 In principle, all properties of objects are selectable for which you own a work item,
 or which can be transitively reached via your work item.
 As a rule of thumb, all objects except task templates can be reached via work items.
 This means that you cannot use task template properties only but that you
 must specify a non task template property in the select- or where-clause.
 
 Note that a task system administrator has special rights and can retrieve
 information on objects associated to other users. When the stored query is executed by
 a task system administrator, the selected properties of all objects for which there are
 work items are returned, no matter whether there is a personally
 owned work item or another user's work item.
 
 Although stored query definitions are stored persistently, object properties contained in
 the result set are assembled dynamically when they are queried.
 Refer to query for the execution of stored queries.
 
 When a stored query definition needs to be updated, it must be deleted and recreated -
 refer to deleteStoredQuery for the deletion of
 stored queries.

It either declares a list of names that identify the object properties (columns of the result)
    to be returned or it specifies the COUNT keyword. Aggregation functions like AVG, SUM,
    MIN, and MAX are not supported.
    
    Each part of the select-clause separated by a comma must specify a property from the
    published views - see the InfoCenter for details.
    
    To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the
    view name. For example, "TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE".
    
    To count the number of potentially qualifying tuples, use the COUNT keyword.
    For example, to count the number of task instance IDs that satisfy the
    where-clause, specify a select-clause such as "COUNT(DISTINCT TASK.TKIID)".
    If you use the more generic "COUNT(*)", then you must specify a where-clause
    so that the tuples to be counted can be determined.
    For example, to count all tasks,
    specify a where-clause such as "TASK.TKIID=TASK.TKIID" that always evaluates to true.
    
    A selectClause must not be greater than 512 bytes in UTF-8 format.
    
    The QueryResultSet contains columns in the same order
    as specified in the selectClause. If tuples are to be counted, an int value is returned
    (row 1, column 1).

    - Specify object ID constants as ID('string-rep-of-oid').
    Specify timestamp constants as TS('yyyy-mm-ddThh:mm:ss') or as CURRENT\_DATE
    for comparisons with the current date.
    

    The date and time parts of a TS definition are optional; either the date or the time must
    be specified. If no date part of a TS definition is specified, the current date is taken.
    Optional time values that are not specified are set to zero.
    The timestamp is 24 hours based.
    For example, TS('16:04') is the same as TS('2002-12-24T16:04:00') provided that the
    current date is December 24th, 2002.
    

    If a date part of a TS definition is specified, the year must consist of 4 letters;
    the month and day specifications are optional.
    Missing month and day specifications are set to 01. For example, specifying
    TS('2003') is the same as specifying TS('2003-01-01T00:00:00').
    Specify binary constants as BIN('UTF-8 string').
    Use constants
    instead of integer enumerations. For example, instead of specifying a task instance state expression
    "TASK.STATE=2" , specify "TASK.STATE=TASK.STATE.STATE\_READY".
    Duplicate apostrophes (') in comparising values. For example,
    "TASK\_CPROP.STRING\_VALUE='d''automatisation'".
    To specify a where clause that refers to properties of name-value pairs, like
    custom properties, add a one-digit suffix (0-9) to the view name.
    

    For example, to have only tuples returned where a task custom property "prop1" has
    the value "v1" or where a task custom property "prop2" has the value v2", the where clause
    can look like
    "TASK\_CPROP1.NAME='prop1' AND TASK\_CPROP1.STRING\_VALUE='v1' OR
    TASK\_CPROP2.NAME='prop2' AND TASK\_CPROP2.STRING\_VALUE = 'v2'".
    For performance reasons, you should not use more than one "OR" construct; use "IN" instead.
    

    For example, to retrieve the values of custom properties "prop1" and "prop2" of all task instances,
    the select clause can look like
    "DISTINCT TASK.TKIID, TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE" and the where-clause
    "TASK\_CPROP1.NAME = 'prop1' AND TASK\_CPROP2.NAME = 'prop2'".
    Specify parameters as @param followed by a number suffix. The number of the
    first parameter must be 1, of the second 2, and so on.
    For example, "TASK\_CPROP.NAME = '@param1'".
    

    The same parameter can be used multiple times.
    Parameters are replaced by strings when the stored query is executed -
    see query.

If a filter is not to be applied, null must be specified.
    
    A whereClause must not be greater than 2047 bytes in UTF-8 format.

If you identify more that one property, the stored query execution result is ordered by the
    values of the first property you identify, then by the values of the second property,
    and so on.
    
    If sort criteria are not to be applied, null must be specified.
    An orderByClause must not be greater than 254 bytes in UTF-8 format.
    
    Note that sort criteria are applied on the server, that is, the locale of the
    server is used for sorting.

- createTask
TKIID createTask(java.lang.String tktid,
               ClientObjectWrapper input)
                 throws ApplicationVetoException,
                        ArchiveUnsupportedOperationException,
                        CannotCreateWorkItemException,
                        IdWrongFormatException,
                        IdWrongTypeException,
                        InvalidApplicationStateException,
                        InvalidLengthException,
                        NotAuthorizedException,
                        ObjectDoesNotExistException,
                        WrongKindException,
                        WrongMessageTypeException,
                        WrongStateException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Creates a task instance using a string representation of the task template ID
 and optionally passes an input message.
 
 The caller must be a potential instance creator or an administrator of the task template.
 The task must not be inline.
 
 The action associated to this method is TaskTemplateActions.CREATETASK.
 
 This method is not supported in archive mode.
Parameters:tktid - The string representation of the task template ID from which an instance is to be created.input - The input message to be used when the task is run.
    The object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:TKIID -
    The object ID of the task instance created.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongFormatException
IdWrongTypeException
InvalidApplicationStateException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5

- createTask
TKIID createTask(TKTID tktid,
               ClientObjectWrapper input)
                 throws ApplicationVetoException,
                        ArchiveUnsupportedOperationException,
                        CannotCreateWorkItemException,
                        IdWrongFormatException,
                        InvalidApplicationStateException,
                        InvalidLengthException,
                        NotAuthorizedException,
                        ObjectDoesNotExistException,
                        WrongKindException,
                        WrongMessageTypeException,
                        WrongStateException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Creates a task instance using the task template ID
 and optionally passes an input message.
 
 The caller must be a potential instance creator or an administrator of the task template.
 The task must not be inline.
 
 The action associated to this method is TaskTemplateActions.CREATETASK.
 
 This method is not supported in archive mode.
Parameters:tktid - The task template ID from which an instance is to be created.input - The input message to be used when the task is run.
    The object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:TKIID -
    The object ID of the task instance created.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongFormatException
InvalidApplicationStateException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5

- createTask
TKIID createTask(java.lang.String name,
               java.lang.String namespace)
                 throws ApplicationVetoException,
                        ArchiveUnsupportedOperationException,
                        CannotCreateWorkItemException,
                        InvalidApplicationStateException,
                        InvalidLengthException,
                        NotAuthorizedException,
                        ObjectDoesNotExistException,
                        ParameterNullException,
                        WrongKindException,
                        WrongStateException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Creates a task instance from the currently valid task template.
 
 The caller must be a potential instance creator or an administrator of the task template.
 The task must not be inline.
 
 The action associated to this method is TaskTemplateActions.CREATETASK.
 
 This method is not supported in archive mode.
Parameters:name - The name of the task template from which an instance is to be created.namespace - The namespace of the task template.
 
Returns:TKIID -
    The object ID of the task instance created.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
InvalidApplicationStateException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createTask
TKIID createTask(java.lang.String name,
               java.lang.String namespace,
               ClientObjectWrapper input)
                 throws ApplicationVetoException,
                        ArchiveUnsupportedOperationException,
                        CannotCreateWorkItemException,
                        InvalidApplicationStateException,
                        InvalidLengthException,
                        NotAuthorizedException,
                        ObjectDoesNotExistException,
                        ParameterNullException,
                        WrongKindException,
                        WrongStateException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Creates a task instance from the currently valid task template and specifies an input message.
 
 The caller must be a potential instance creator or an administrator of the task template.
 The task must not be inline.
 
 The action associated to this method is TaskTemplateActions.CREATETASK.
 
 This method is not supported in archive mode.
Parameters:name - The name of the task template from which an instance is to be created.namespace - The namespace of the task template.input - The input message to be used when the task is run.
    The object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:TKIID -
    The object ID of the task instance created.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
InvalidApplicationStateException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createTask
TKIID createTask(TaskModel taskModel,
               java.lang.String applicationName,
               java.lang.String parentContext)
                 throws ApplicationVetoException,
                        ArchiveUnsupportedOperationException,
                        CannotCreateWorkItemException,
                        IdWrongTypeException,
                        InvalidLengthException,
                        NotAuthorizedException,
                        ObjectDoesNotExistException,
                        ParameterNullException,
                        UnexpectedFailureException,
                        TaskDeploymentException,
                        TELValidationException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Creates a task instance from the specified task model.
 
 The caller must have potential-instance-creator rights on the associated application component.
 
 The action associated to this method is TaskTemplateActions.CREATETASK.
 
 This method is not supported in archive mode.
Parameters:taskModel - The model that describes the task instance to be created at Runtime.applicationName - The name of the enterprise application that contains the message
    or business calendar definitions used in the TaskModel.
    If the message definitions are simple types only or if you do not use a business
    calendar, null may be specified.parentContext - The object ID (ACOID) or the name of the application component
    to be associated with the task instance.
 
Returns:TKIID -
    The object ID of the task instance created.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongTypeException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
TaskDeploymentException
TELValidationException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createTask
TKIID createTask(TaskModel taskModel,
               java.lang.String applicationName,
               java.lang.String parentContext,
               ClientObjectWrapper input)
                 throws ApplicationVetoException,
                        ArchiveUnsupportedOperationException,
                        CannotCreateWorkItemException,
                        IdWrongTypeException,
                        InvalidLengthException,
                        NotAuthorizedException,
                        ObjectDoesNotExistException,
                        ParameterNullException,
                        WrongMessageTypeException,
                        UnexpectedFailureException,
                        TaskDeploymentException,
                        TELValidationException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Creates a task instance from the specified task model and specifies an input message.
 
 The caller must have potential-instance-creator rights on the associated application component.
 
 The action associated to this method is TaskTemplateActions.CREATETASK.
 
 This method is not supported in archive mode.
Parameters:taskModel - The model that describes the task instance to be created Runtime.applicationName - The name of the enterprise application that contains the message
    or business calendar definitions used in the TaskModel.
    If the message definitions are simple types only or if you do not use a business
    calendar, null may be specified.parentContext - The object ID (ACOID) or the name of the application component
    to be associated with the task instance.input - The input message to be used when the task is run.
    The object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:TKIID -
    The object ID of the task instance created.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongTypeException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongMessageTypeException
UnexpectedFailureException
TaskDeploymentException
TELValidationException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createTaskTemplate
TKTID createTaskTemplate(TaskModel taskModel,
                       java.lang.String applicationName)
                         throws ApplicationVetoException,
                                ArchiveUnsupportedOperationException,
                                InvalidLengthException,
                                NotAuthorizedException,
                                ObjectDoesNotExistException,
                                ParameterNullException,
                                UnexpectedFailureException,
                                TaskDeploymentException,
                                TELValidationException,
                                java.rmi.RemoteException,
                                javax.ejb.EJBException
Creates a task template from the specified task model.
 
 The caller must have potential-instance-creator rights on the associated application component.
 
 This method is not supported in archive mode.
Parameters:taskModel - The model that describes the task template to be created Runtime.applicationName - The name of the enterprise application that contains the message
    or business calendar definitions used in the TaskModel.
    If the message definitions are simple types only or if you do not use a business
    calendar, null may be specified.
 
Returns:TKTID -
    The task template ID of the task template created.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
TaskDeploymentException
TELValidationException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createWorkItem void createWorkItem(java.lang.String identifier, int assignmentReason, java.lang.String userID) throws ApplicationVetoException , ArchiveUnsupportedOperationException , EverybodyWorkItemException , GroupWorkItemException , IdWrongFormatException , IdWrongTypeException , InvalidAssignmentReasonException , InvalidLengthException , NotAuthorizedException , UserDoesNotExistException , ObjectDoesNotExistException , ParameterNullException , TaskDelegationNotSupportedException , WorkItemManagerException , WrongKindException , WrongStateException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Creates a user work item for the specified task or escalation instance using a string representation of the task or escalation instance ID. The work item is created with the specified assignment reason for the specified user. The caller must be an administrator. As long as the task is inactive, the originator of the task can also create new work items. The following rules apply for the creation work items: The action associated to this method is TaskActions.CREATEWORKITEM or EscalationActions.CREATEWORKITEM . This method is not supported in archive mode. Parameters: identifier - A string representation of the task or escalation instance ID that is used to identify the object for which a new work item is to be created. assignmentReason - The reason why the work item is assigned - refer to the work item assignment reasons . userID - The user for which a work item is to be created. It is checked whether the user exists but the check may be executed case insensitively. The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments' custom property of the Human Task Manager configuration to 'true'. Throws: ApplicationVetoException ArchiveUnsupportedOperationException EverybodyWorkItemException GroupWorkItemException IdWrongFormatException IdWrongTypeException InvalidAssignmentReasonException InvalidLengthException NotAuthorizedException UserDoesNotExistException ObjectDoesNotExistException ParameterNullException TaskDelegationNotSupportedException WorkItemManagerException WrongKindException WrongStateException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 5.1.1 Change History Release Modification 6.1 Throws a TaskDelegationNotSupportedException when the task cannot be delegated to the specified user. 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### createWorkItem

```
void createWorkItem(java.lang.String identifier,
                  int assignmentReason,
                  java.lang.String userID)
                    throws ApplicationVetoException,
                           ArchiveUnsupportedOperationException,
                           EverybodyWorkItemException,
                           GroupWorkItemException,
                           IdWrongFormatException,
                           IdWrongTypeException,
                           InvalidAssignmentReasonException,
                           InvalidLengthException,
                           NotAuthorizedException,
                           UserDoesNotExistException,
                           ObjectDoesNotExistException,
                           ParameterNullException,
                           TaskDelegationNotSupportedException,
                           WorkItemManagerException,
                           WrongKindException,
                           WrongStateException,
                           UnexpectedFailureException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
```

The caller must be an administrator. As long as the task
 is inactive, the originator of the task can also create new work items.
 
 The following rules apply for the creation work items:
 
Work items assigned to "everybody" cannot be created.
 Work items with assignment reasons "owner", "starter", and "originator" cannot be created.
 "potential starter" work items can be created as long as the task is inactive.
 The task must be a stand-alone, non-inline task.
 "potential owner" or "editor" work items can be created when the task is ready or claimed.
 "escalation receiver" work items can be created when the task is escalated.
 "administrator" or "reader" work items can be created in any task state but inactive.
 When the task is in the terminated or expired state, the task must be a stand-alone,
 non-inline task.
 

 The action associated to this method is TaskActions.CREATEWORKITEM or
 EscalationActions.CREATEWORKITEM.
 
 This method is not supported in archive mode.

Change History

Release
 Modification
 
6.1
 
 Throws a TaskDelegationNotSupportedException when the task cannot be delegated to the specified user.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createWorkItem void createWorkItem(TKIID tkiid, int assignmentReason, java.lang.String userID) throws ApplicationVetoException , ArchiveUnsupportedOperationException , EverybodyWorkItemException , GroupWorkItemException , IdWrongFormatException , InvalidAssignmentReasonException , InvalidLengthException , NotAuthorizedException , UserDoesNotExistException , ObjectDoesNotExistException , ParameterNullException , TaskDelegationNotSupportedException , WorkItemManagerException , WrongKindException , WrongStateException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Creates a user work item for the specified task instance using the task instance ID. The work item is created with the specified assignment reason for the specified user. The caller must be an administrator when the task is active. As long as the task is inactive, the originator of the task can also create new work items. The following rules apply for the creation of additional work items: The action associated to this method is TaskActions.CREATEWORKITEM . This method is not supported in archive mode. Parameters: tkiid - The object ID of the task instance the new work item should belong to. assignmentReason - The reason why the work item is assigned - refer to the work item assignment reasons . userID - The user the work item should belong to. It is checked whether the user exists but the check may be executed case insensitively. The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments' custom property of the Human Task Manager configuration to 'true'. Throws: ApplicationVetoException ArchiveUnsupportedOperationException EverybodyWorkItemException GroupWorkItemException IdWrongFormatException InvalidAssignmentReasonException InvalidLengthException NotAuthorizedException UserDoesNotExistException ObjectDoesNotExistException ParameterNullException TaskDelegationNotSupportedException WorkItemManagerException WrongKindException WrongStateException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 5.1.1 Change History Release Modification 6.1 Throws a TaskDelegationNotSupportedException when the task cannot be delegated to the specified user. 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### createWorkItem

```
void createWorkItem(TKIID tkiid,
                  int assignmentReason,
                  java.lang.String userID)
                    throws ApplicationVetoException,
                           ArchiveUnsupportedOperationException,
                           EverybodyWorkItemException,
                           GroupWorkItemException,
                           IdWrongFormatException,
                           InvalidAssignmentReasonException,
                           InvalidLengthException,
                           NotAuthorizedException,
                           UserDoesNotExistException,
                           ObjectDoesNotExistException,
                           ParameterNullException,
                           TaskDelegationNotSupportedException,
                           WorkItemManagerException,
                           WrongKindException,
                           WrongStateException,
                           UnexpectedFailureException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
```

The caller must be an administrator when the task is active. As long as the task
 is inactive, the originator of the task can also create new work items.
 
 The following rules apply for the creation of additional work items:
 
Work items assigned to "everybody" cannot be created.
 Work items with assignment reasons "owner", "starter", and "originator" cannot be created.
 "potential starter" work items can be created as long as the task is inactive.
 The task must be a stand-alone, non-inline task.
 "potential owner" or "editor" work items can be created when the task is ready or claimed.
 "administrator" or "reader" work items can be created in any task state but inactive.
 When the task is in the terminated or expired state, the task must be a stand-alone,
 non-inline task.
 

 The action associated to this method is TaskActions.CREATEWORKITEM.
 
 This method is not supported in archive mode.

Change History

Release
 Modification
 
6.1
 
 Throws a TaskDelegationNotSupportedException when the task cannot be delegated to the specified user.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createWorkItem
void createWorkItem(ESIID esiid,
                  int assignmentReason,
                  java.lang.String userID)
                    throws ApplicationVetoException,
                           ArchiveUnsupportedOperationException,
                           EverybodyWorkItemException,
                           GroupWorkItemException,
                           IdWrongFormatException,
                           InvalidAssignmentReasonException,
                           InvalidLengthException,
                           NotAuthorizedException,
                           UserDoesNotExistException,
                           ObjectDoesNotExistException,
                           ParameterNullException,
                           TaskDelegationNotSupportedException,
                           WorkItemManagerException,
                           WrongKindException,
                           WrongStateException,
                           UnexpectedFailureException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
Creates a user work item for the specified escalation instance
 using the escalation instance ID.
 The work item is created with the specified assignment reason
 for the specified user.
 
 The caller must be an administrator. Additional "escalation receiver" work items can only be created
 when the task is escalated.
 
 The action associated to this method is
 EscalationActions.CREATEWORKITEM.
 
 This method is not supported in archive mode.
Parameters:esiid - The object ID of the escalation instance for which a new work item is to be created.assignmentReason - The reason why the work item is assigned - refer to
    the work item assignment reasons.
    Valid values are
    WorkItem.REASON\_ESCALATION\_RECEIVER, WorkItem.REASON\_READER, and WorkItem.REASON\_ADMINISTRATOR.userID - The user for which a new work item is to be created.
    It is checked whether the user exists but the check may be executed case insensitively.
    The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments'
    custom property of the Human Task Manager configuration to 'true'.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EverybodyWorkItemException
GroupWorkItemException
IdWrongFormatException
InvalidAssignmentReasonException
InvalidLengthException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
ParameterNullException
TaskDelegationNotSupportedException
WorkItemManagerException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1
 
 Throws a GroupWorkItemException when a group is specified as user ID.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- delete
void delete(java.lang.String tkiid)
            throws ApplicationVetoException,
                   ChildTaskInstanceActiveException,
                   IdWrongFormatException,
                   IdWrongTypeException,
                   IsNotTopLevelTaskException,
                   NotAuthorizedException,
                   WrongKindException,
                   WrongStateException,
                   UnexpectedFailureException,
                   java.rmi.RemoteException,
                   javax.ejb.EJBException
Deletes the specified task instance
  using a string representation of the task instance ID.
  A to-do, collaboration, or administration task must not be inline or stand-alone with "child" autonomy.
  The task cannot be a subtask or follow-on task.
  Note that collaboration and to-do task instances are also known as
  human and participating task instances.
  
  The task must be in the inactive, terminated, expired, finished, or failed state.
  It can be escalated or suspended.
 
 The caller must have administrative rights or be the originator of the task. An originator
 can only delete an inactive task.
 
 The action associated to this method is TaskActions.DELETE.
Parameters:tkiid - A string representation of the task instance ID
    that is used to identify the task instance.
 
Throws:
ApplicationVetoException
ChildTaskInstanceActiveException
IdWrongFormatException
IdWrongTypeException
IsNotTopLevelTaskException
NotAuthorizedException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- delete
void delete(TKIID tkiid)
            throws ApplicationVetoException,
                   IdWrongFormatException,
                   IsNotTopLevelTaskException,
                   NotAuthorizedException,
                   WrongKindException,
                   WrongStateException,
                   UnexpectedFailureException,
                   java.rmi.RemoteException,
                   javax.ejb.EJBException
Deletes the specified task instance using the task instance ID.
  A to-do, collaboration, or administration task must not be inline or stand-alone with "child" autonomy.
  The task cannot be a subtask or follow-on task.
  Note that collaboration and to-do task instances are also known as
  human and participating task instances.
  
  The task must be in the inactive, terminated, expired, finished, or failed state.
  It can be escalated or suspended.
 
 The caller must have administrative rights or be the originator of the task. An originator
 can only delete an inactive task.
 
 The action associated to this method is TaskActions.DELETE.
Parameters:tkiid - The task instance ID that is used to identify the task instance.
 
Throws:
ApplicationVetoException
IdWrongFormatException
IsNotTopLevelTaskException
NotAuthorizedException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- delete
void delete(java.lang.String identifier,
          boolean deleteInstances)
            throws ApplicationVetoException,
                   ChildTaskInstanceActiveException,
                   IdWrongFormatException,
                   IdWrongTypeException,
                   IsNotAdHocException,
                   NotAuthorizedException,
                   ObjectDoesNotExistException,
                   RunningInstancesException,
                   WrongKindException,
                   WrongStateException,
                   UnexpectedFailureException,
                   java.rmi.RemoteException,
                   javax.ejb.EJBException
Deletes the specified task template
  using a string representation of the task template ID.
  The task template must have been created at Runtime. Templates that have been installed
  as part of an enterprise application are deleted (uninstalled) together with the enterprise application.
 
  The task template must be in the stopped state to prevent new instances from being created.
  No task instances may exist that are derived from this template unless deletion of
  the instances is requested.
 
 The caller must have administrative rights.
 
 The action associated to this method is TaskTemplateActions.DELETETEMPLATE.
Parameters:identifier - A string representation of the task template ID
    that is used to identify the task template to be deleted.deleteInstances - Specifies whether all instances that are derived from this template are to be deleted
    together with the template.
    True states that all derived instances are to be deleted.
    False states that derived instances are not to be deleted; if instances exist, a
    RunningInstancesException is thrown.
 
Throws:
ApplicationVetoException
ChildTaskInstanceActiveException
IdWrongFormatException
IdWrongTypeException
IsNotAdHocException
NotAuthorizedException
ObjectDoesNotExistException
RunningInstancesException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.1

- delete
void delete(TKTID tktid,
          boolean deleteInstances)
            throws ApplicationVetoException,
                   ChildTaskInstanceActiveException,
                   IdWrongFormatException,
                   IsNotAdHocException,
                   NotAuthorizedException,
                   ObjectDoesNotExistException,
                   RunningInstancesException,
                   WrongKindException,
                   WrongStateException,
                   UnexpectedFailureException,
                   java.rmi.RemoteException,
                   javax.ejb.EJBException
Deletes the specified task template using the task template ID.
  The task template must have been created Runtime. Templates that have been installed
  as part of an enterprise application are deleted (uninstalled) together with the enterprise application.
 
  The task template must be in the stopped state to prevent new instances from being created.
  No task instances may exist that are derived from this template unless deletion of
  the instances is requested.
 
 The caller must have administrative rights.
 
 The action associated to this method is TaskTemplateActions.DELETETEMPLATE.
Parameters:tktid - The task template ID that is used to identify the task template to be deleted.deleteInstances - Specifies whether all instances that are derived from this template are to be deleted
    together with the template.
    True states that all derived instances are to be deleted.
    False states that derived instances are not to be deleted; if instances exist, a
    RunningInstancesException is thrown.
 
Throws:
ApplicationVetoException
ChildTaskInstanceActiveException
IdWrongFormatException
IsNotAdHocException
NotAuthorizedException
ObjectDoesNotExistException
RunningInstancesException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.1

- deleteStoredQuery
void deleteStoredQuery(java.lang.String storedQueryName)
                       throws NotAuthorizedException,
                              ParameterNullException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Deletes the specified stored query.
 If this method is called by a task system administrator, then a stored query is deleted
 that is available for public usage.
 If this method is called by a regular user, then a stored query is deleted
 that is privately available for the calling logged-on user.
 
 No error is signalled when the specified stored query does no longer exist.
 
 Refer to createStoredQuery for
 the creation of stored queries.
Parameters:storedQueryName - The name of the stored query to be deleted -
    refer to getStoredQueryNames
    for the retrieval of existing stored query names.
 
Throws:
NotAuthorizedException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.0.2
 
 Can delete a private stored query.

- deleteStoredQuery
void deleteStoredQuery(java.lang.String userID,
                     java.lang.String storedQueryName)
                       throws NotAuthorizedException,
                              ParameterNullException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Deletes the specified stored query for the specified user.
 
 A regular user can only delete stored queries that are available for his personal usage.
 A task system administrator can also delete stored queries that are available
 for the usage of the specified person.
 
 No error is signalled when the specified stored query does no longer exist.
 
 Refer to createStoredQuery for
 the creation of stored queries.
Parameters:userID - The name of the user who is the owner of the stored query.storedQueryName - The name of the stored query to be deleted -
    refer to getStoredQueryNames
    for the retrieval of existing stored query names.
 
Throws:
NotAuthorizedException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- deleteWorkItem void deleteWorkItem(java.lang.String identifier, int assignmentReason, java.lang.String userID) throws ApplicationVetoException , ArchiveUnsupportedOperationException , EverybodyWorkItemException , GroupWorkItemException , IdWrongFormatException , IdWrongTypeException , InvalidAssignmentReasonException , InvalidLengthException , LastAdminWorkItemException , NotAuthorizedException , WorkItemDoesNotExistException , ObjectDoesNotExistException , ParameterNullException , TaskDelegationNotSupportedException , WorkItemManagerException , WrongKindException , WrongStateException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Deletes the specified user work item using a string representation of the task or escalation instance ID. The caller must be an administrator for the deletion of work items for escalation instances or when the task is active. As long as the task is inactive, the originator of the task can also delete a work item. The following rules apply for the deletion of work items: The action associated to this method is TaskActions.DELETEWORKITEM or EscalationActions.DELETEWORKITEM . This method is not supported in archive mode. Parameters: identifier - A string representation of the task or escalation instance ID that is used to identify the work item to be deleted. assignmentReason - The reason why the work item is assigned - refer to the work item assignment reasons . userID - The user the work item belongs to. Throws: ApplicationVetoException ArchiveUnsupportedOperationException EverybodyWorkItemException GroupWorkItemException IdWrongFormatException IdWrongTypeException InvalidAssignmentReasonException InvalidLengthException LastAdminWorkItemException NotAuthorizedException WorkItemDoesNotExistException ObjectDoesNotExistException ParameterNullException TaskDelegationNotSupportedException WorkItemManagerException WrongKindException WrongStateException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 5.1.1 Change History Release Modification 6.1 Throws a GroupWorkItemException when a group work item is asked to be deleted. 6.1 Throws a TaskDelegationNotSupportedException when the last work item is deleted and the task cannot be delegated to the fallback user. 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### deleteWorkItem

```
void deleteWorkItem(java.lang.String identifier,
                  int assignmentReason,
                  java.lang.String userID)
                    throws ApplicationVetoException,
                           ArchiveUnsupportedOperationException,
                           EverybodyWorkItemException,
                           GroupWorkItemException,
                           IdWrongFormatException,
                           IdWrongTypeException,
                           InvalidAssignmentReasonException,
                           InvalidLengthException,
                           LastAdminWorkItemException,
                           NotAuthorizedException,
                           WorkItemDoesNotExistException,
                           ObjectDoesNotExistException,
                           ParameterNullException,
                           TaskDelegationNotSupportedException,
                           WorkItemManagerException,
                           WrongKindException,
                           WrongStateException,
                           UnexpectedFailureException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
```

The caller must be an administrator for the deletion of work items for escalation instances
 or when the task is active.
 As long as the task is inactive, the originator of the task can also delete a work item.
 
 The following rules apply for the deletion of work items:
 
Work items assigned to "everybody" cannot be deleted.
 Work items with assignment reasons "owner", "starter", and "originator" cannot be deleted.
 The last "administrator" work item cannot be deleted.
 "potential starter" work items can only be deleted as long as the task is inactive.
 The task must be a stand-alone, non-inline task.
 "potential owner" or "editor" work items can only be deleted when the task is ready or claimed.
 "escalation receiver" work items can only be deleted when the task is escalated.
 "administrator" or "reader" work items can be deleted in any task state but inactive.
 When the task is in the terminated or expired state, the task must be a stand-alone,
 non-inline task.
 

 The action associated to this method is TaskActions.DELETEWORKITEM or
 EscalationActions.DELETEWORKITEM.
 
 This method is not supported in archive mode.

Change History

Release
 Modification
 
6.1
 
 Throws a GroupWorkItemException when a group work item is asked to be deleted.
 
6.1
 
 Throws a TaskDelegationNotSupportedException when the last work item is deleted and the task cannot be delegated to the fallback user.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- deleteWorkItem void deleteWorkItem(TKIID tkiid, int assignmentReason, java.lang.String userID) throws ApplicationVetoException , ArchiveUnsupportedOperationException , EverybodyWorkItemException , GroupWorkItemException , IdWrongFormatException , InvalidAssignmentReasonException , InvalidLengthException , LastAdminWorkItemException , NotAuthorizedException , WorkItemDoesNotExistException , ObjectDoesNotExistException , ParameterNullException , TaskDelegationNotSupportedException , WorkItemManagerException , WrongKindException , WrongStateException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Deletes the specified user work item using the task instance ID. The caller must be an administrator when the task is active. As long as the task is inactive, the originator of the task can also delete a work item. The following rules apply for the deletion of work items: The action associated to this method is TaskActions.DELETEWORKITEM . This method is not supported in archive mode. Parameters: tkiid - The ID of task instance that is used to identify the work item to be deleted. assignmentReason - The reason why the work item is assigned - refer to the work item assignment reasons . userID - The user the work item belongs to. Throws: ApplicationVetoException ArchiveUnsupportedOperationException EverybodyWorkItemException GroupWorkItemException IdWrongFormatException InvalidAssignmentReasonException InvalidLengthException LastAdminWorkItemException NotAuthorizedException WorkItemDoesNotExistException ObjectDoesNotExistException ParameterNullException TaskDelegationNotSupportedException WorkItemManagerException WrongKindException WrongStateException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 5.1.1 Change History Release Modification 6.1 Throws a GroupWorkItemException when a group work item is asked to be deleted. 6.1 Throws a TaskDelegationNotSupportedException when the last work item is deleted and the task cannot be delegated to the fallback user. 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### deleteWorkItem

```
void deleteWorkItem(TKIID tkiid,
                  int assignmentReason,
                  java.lang.String userID)
                    throws ApplicationVetoException,
                           ArchiveUnsupportedOperationException,
                           EverybodyWorkItemException,
                           GroupWorkItemException,
                           IdWrongFormatException,
                           InvalidAssignmentReasonException,
                           InvalidLengthException,
                           LastAdminWorkItemException,
                           NotAuthorizedException,
                           WorkItemDoesNotExistException,
                           ObjectDoesNotExistException,
                           ParameterNullException,
                           TaskDelegationNotSupportedException,
                           WorkItemManagerException,
                           WrongKindException,
                           WrongStateException,
                           UnexpectedFailureException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
```

The caller must be an administrator when the task is active. As long as the task
 is inactive, the originator of the task can also delete a work item.
 
 The following rules apply for the deletion of work items:
 
Work items assigned to "everybody" cannot be deleted.
 Work items with assignment reasons "owner", "starter", and "originator" cannot be deleted.
 The last "administrator" work item cannot be deleted.
 "potential starter" work items can only be deleted as long as the task is inactive.
 The task must be a stand-alone, non-inline task.
 "potential owner" or "editor" work items can only be deleted when the task is ready or claimed.
 "administrator" or "reader" work items can be deleted in any task state but inactive.
 When the task is in the terminated or expired state, the task must be a stand-alone,
 non-inline task.
 

 The action associated to this method is TaskActions.DELETEWORKITEM.
 
 This method is not supported in archive mode.

Change History

Release
 Modification
 
6.1
 
 Throws a GroupWorkItemException when a group work item is asked to be deleted.
 
6.1
 
 Throws a TaskDelegationNotSupportedException when the last work item is deleted and the task cannot be delegated to the fallback user.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- deleteWorkItem
void deleteWorkItem(ESIID esiid,
                  int assignmentReason,
                  java.lang.String userID)
                    throws ApplicationVetoException,
                           ArchiveUnsupportedOperationException,
                           EverybodyWorkItemException,
                           GroupWorkItemException,
                           IdWrongFormatException,
                           InvalidAssignmentReasonException,
                           InvalidLengthException,
                           LastAdminWorkItemException,
                           NotAuthorizedException,
                           WorkItemDoesNotExistException,
                           ObjectDoesNotExistException,
                           ParameterNullException,
                           TaskDelegationNotSupportedException,
                           WorkItemManagerException,
                           WrongKindException,
                           WrongStateException,
                           UnexpectedFailureException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
Deletes the specified user work item using the escalation instance ID.
 
 The caller must be an administrator.
 "Escalation receiver" work items can only be deleted when the task is escalated.
 
 The action associated to this method is
 EscalationActions.DELETEWORKITEM.
 
 This method is not supported in archive mode.
Parameters:esiid - The ID of escalation instance that is used to identify the work item to be deleted.assignmentReason - The reason why the work item is assigned - refer to
     the work item assignment reasons.userID - The user the work item belongs to.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EverybodyWorkItemException
GroupWorkItemException
IdWrongFormatException
InvalidAssignmentReasonException
InvalidLengthException
LastAdminWorkItemException
NotAuthorizedException
WorkItemDoesNotExistException
ObjectDoesNotExistException
ParameterNullException
TaskDelegationNotSupportedException
WorkItemManagerException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1
 
 Throws a GroupWorkItemException when a group is specified as user ID.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- getAbsence
boolean getAbsence()
                   throws StaffServiceCannotAccessVMMException,
                          StaffServiceSubstitutionNotEnabledException,
                          StaffServiceRuntimeException,
                          UserDoesNotExistException,
                          UnexpectedFailureException,
                          java.rmi.RemoteException,
                          javax.ejb.EJBException
Deprecated. As of version 7.0, replaced by getUserSubstitutionDetail.
 
Returns the absence setting of the logged-on user. Absent users
  do not receive any work items but a substitute receives the work item instead.
Returns:boolean -
    
    The absence setting of the specified user.
    True states that the specified user is absent.
    False states that the specified user is not absent.
 
Throws:
StaffServiceCannotAccessVMMException
StaffServiceSubstitutionNotEnabledException
StaffServiceRuntimeException
UserDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getAbsence
boolean getAbsence(java.lang.String userID)
                   throws NotAuthorizedException,
                          ParameterNullException,
                          StaffServiceCannotAccessVMMException,
                          StaffServiceSubstitutionNotEnabledException,
                          StaffServiceRuntimeException,
                          UserDoesNotExistException,
                          UnexpectedFailureException,
                          java.rmi.RemoteException,
                          javax.ejb.EJBException
Deprecated. As of version 7.0, replaced by getUserSubstitutionDetail.
Returns the absence setting of the specified user. Absent users
  do not receive any work items but a substitute receives the work item instead.
  
  If retrieving the absence setting is not restricted to administrators, then everybody can
  retrieve the absence setting of any user.
  
  If retrieving the absence setting is restricted to administrators, then only
  task system monitors or task system administrators can retrieve the absence setting
  of arbitrary users. A user may, however, always read his/her personal setting.
Parameters:userID - The name of the user whose absence setting is to be retrieved.
 
Returns:boolean -
    
    The absence setting of the specified user.
    True states that the specified user is absent.
    False states that the specified user is not absent.
 
Throws:
NotAuthorizedException
ParameterNullException
StaffServiceCannotAccessVMMException
StaffServiceSubstitutionNotEnabledException
StaffServiceRuntimeException
UserDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getAllCustomProperties
java.util.List getAllCustomProperties(java.lang.String identifier)
                                      throws IdWrongFormatException,
                                             IdWrongTypeException,
                                             NotAuthorizedException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves all custom properties of the specified task template or task instance
 using a string representation of the object ID.
 
 Custom properties allow a user to add additional properties to a task
 beyond those provided and managed by the Human Task Manager.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the object. Thus, using inline custom properties
 can increase performance.
 
 This method returns the custom properties that are attached to the object as well as
 the inline custom properties.
 
 Custom properties can be retrieved in any state of the task instance.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETCUSTOMPROPERTY.
Parameters:identifier - A string representation of the task template or task instance object ID. This
    string is used to identify the object for which the custom properties are to be retrieved.
 
Returns:List -
    A list of CustomProperty and
    InlineCustomProperty objects.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- getAllCustomProperties
java.util.List getAllCustomProperties(TKTID tktid)
                                      throws IdWrongFormatException,
                                             NotAuthorizedException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves all custom properties of the specified task template using the task template ID.
 
 Custom properties allow a user to add additional properties to a task
 beyond those provided and managed by the Human Task Manager.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the object. Thus, using inline custom properties
 can increase performance.
 
 This method returns the custom properties that are attached to the process template as well as
 the inline custom properties.
 
 The caller must have at least reader authority for the task template.
 
 The action associated to this method is TaskTemplateActions.GETCUSTOMPROPERTY.
Parameters:tktid - The task template object ID whose custom properties are to be retrieved.
 
Returns:List -
    A list of CustomProperty and
    InlineCustomProperty objects.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- getAllCustomProperties
java.util.List getAllCustomProperties(TKIID tkiid)
                                      throws IdWrongFormatException,
                                             NotAuthorizedException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves all custom properties of the specified task instance using the task instance ID.
 
 Custom properties allow a user to add additional properties to a task
 beyond those provided and managed by the Human Task Manager.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the object. Thus, using inline custom properties
 can increase performance.
 
 This method returns the custom properties that are attached to the task instance as well as
 the inline custom properties.
 
 Custom properties can be retrieved in any state of the task instance.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETCUSTOMPROPERTY.
Parameters:tkiid - The task instance object ID whose custom properties are to be retrieved.
 
Returns:List -
    A list of CustomProperty and
    InlineCustomProperty objects.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- getAllWorkItems
WorkItem[] getAllWorkItems(java.lang.String identifier)
                           throws IdWrongFormatException,
                                  IdWrongTypeException,
                                  NotAuthorizedException,
                                  ObjectDoesNotExistException,
                                  WorkItemManagerException,
                                  UnexpectedFailureException,
                                  java.rmi.RemoteException,
                                  javax.ejb.EJBException
Returns all work item assignments associated to specified task or escalation
  instance using a string representation of the task or escalation instance ID.
  
  The task or escalation instance can be in any execution state.
  
  The caller must have a work item for the task or escalation instance or be a
  task system administrator or task system monitor.
Parameters:identifier - The string representation of a task or escalation instance ID. The string is
    used to identify the object whose work item assignments are to be retrieved.
 
Returns:WorkItem[] -
    An array of work items. If there are no work items,
    an empty array is returned. Refer to WorkItem
    to view the work item properties.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2.1

- getAllWorkItems
WorkItem[] getAllWorkItems(ESIID esiid)
                           throws IdWrongFormatException,
                                  NotAuthorizedException,
                                  ObjectDoesNotExistException,
                                  WorkItemManagerException,
                                  UnexpectedFailureException,
                                  java.rmi.RemoteException,
                                  javax.ejb.EJBException
Returns all work item assignments associated to specified escalation
  instance using the escalation instance ID.
  
  The escalation instance can be in any state.
  
  The caller must have a work item for the escalation instance or be a
  task system administrator or task system monitor.
Parameters:esiid - The object ID of the escalation instance. This ID is used to identify
    the escalation whose work item assignments are to be retrieved.
 
Returns:WorkItem[] -
    An array of work items. If there are no work items,
    an empty array is returned. Refer to WorkItem
    to view the work item properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2.1

- getAllWorkItems
WorkItem[] getAllWorkItems(TKIID tkiid)
                           throws IdWrongFormatException,
                                  NotAuthorizedException,
                                  ObjectDoesNotExistException,
                                  WorkItemManagerException,
                                  UnexpectedFailureException,
                                  java.rmi.RemoteException,
                                  javax.ejb.EJBException
Returns all work item assignments associated to specified task
  instance using the task instance ID.
  
  The task instance can be in any execution state.
  
  The caller must have a work item for the task instance or be a
  task system administrator or task system monitor.
Parameters:tkiid - The object ID of the task instance. This ID is used to identify
    the task whose work item assignments are to be retrieved.
 
Returns:WorkItem[] -
    An array of work items. If there are no work items,
    an empty array is returned. Refer to WorkItem
    to view the work item properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2.1

- getAvailableActionFlags
boolean[][] getAvailableActionFlags(java.lang.String[] identifiers)
                                    throws IdWrongFormatException,
                                           IdWrongTypeException,
                                           NotAuthorizedException,
                                           ObjectDoesNotExistException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Returns the actions that can be called for the specified tasks or escalations
 in their current state by the logged-on user
 using string representations of the task or escalation instance IDs.
 Refer to TaskActions or
 EscalationActions for possible actions.
Parameters:identifiers - An array of string representations of task or escalation instance IDs.
 
Returns:boolean[][] -
    An array of actions that can be called for each specified task or escalation instance.
 The array contains a row per task or escalation instance and a column per possible action.
 An array entry thus indicates whether a possible action can be called for the task or escalation instance
 by the logged-on user in the current task or escalation instance state.
 True states that the action can be called. False states that the action cannot be called.
 
 The task or escalation instances appear in the same order as specified.
 Refer to TaskActionIndex or
 EscalationActionIndex for index constants that can
 be used to access the columns of the two-dimensional array.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.1
 
 Supports escalation instances.

- getAvailableActionFlags
boolean[][] getAvailableActionFlags(ESIID[] esiids)
                                    throws IdWrongFormatException,
                                           NotAuthorizedException,
                                           ObjectDoesNotExistException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Returns the actions that can be called for the specified escalation instances
 in their current state by the logged-on user using escalation instance IDs.
 Refer to EscalationActions for possible actions.
Parameters:esiids - An array of escalation instance IDs.
 
Returns:boolean[][] -
    An array of actions that can be called for each specified escalation instance.
 The array contains a row per escalation instance and a column per possible action.
 An array entry thus indicates whether a possible action can be called for the escalation
 instance by the logged-on user in the current escalation instance state.
 True states that the action can be called. False states that the action cannot be called.
 
 The escalation instances appear in the same order as specified.
 Refer to EscalationActionIndex for index constants that can
 be used to access the columns of the two-dimensional array.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getAvailableActionFlags
boolean[][] getAvailableActionFlags(TKIID[] tkiids)
                                    throws IdWrongFormatException,
                                           NotAuthorizedException,
                                           ObjectDoesNotExistException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Returns the actions that can be called for the specified tasks in their
 current state by the logged-on user using task instance IDs.
 Refer to TaskActions for possible actions.
Parameters:tkiids - An array of task instance IDs.
 
Returns:boolean[][] -
    An array of actions that can be called for each specified task instance.
 The array contains a row per task instance and a column per possible action.
 An array entry thus indicates whether a possible action can be called for the task instance
 by the logged-on user in the current task instance state.
 True states that the action can be called. False states that the action cannot be called.
 
 The task instances appear in the same order as specified.
 Refer to TaskActionIndex for index constants that can
 be used to access the columns of the two-dimensional array.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getAvailableActions
int[] getAvailableActions(java.lang.String identifier)
                          throws IdWrongFormatException,
                                 IdWrongTypeException,
                                 NotAuthorizedException,
                                 ObjectDoesNotExistException,
                                 UnexpectedFailureException,
                                 java.rmi.RemoteException,
                                 javax.ejb.EJBException
Returns the actions that can be called by the logged-on user
 for the specified task instance, task template, escalation instance, or escalation template
 using a string representation of the object ID.
 Refer to TaskActions, TaskTemplateActions,
 EscalationActions, or
 EscalationTemplateActions for possible actions.
Parameters:identifier - The string representation of the object ID.
 
Returns:int[] -
    The set of possible actions.
    Returns null if there are no available actions.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.1
 
 Supports task templates, escalation templates, and escalation instances.

- getAvailableActions
int[] getAvailableActions(ESTID estid)
                          throws IdWrongFormatException,
                                 NotAuthorizedException,
                                 ObjectDoesNotExistException,
                                 UnexpectedFailureException,
                                 java.rmi.RemoteException,
                                 javax.ejb.EJBException
Returns the actions that can be called in the current escalation template state
 by the logged-on user using the escalation template ID.
 Refer to EscalationTemplateActions for possible actions.
Parameters:estid - The object ID of the escalation template.
 
Returns:int[] -
    The set of possible actions.
    Returns null if there are no available actions.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getAvailableActions
int[] getAvailableActions(ESIID esiid)
                          throws IdWrongFormatException,
                                 NotAuthorizedException,
                                 ObjectDoesNotExistException,
                                 UnexpectedFailureException,
                                 java.rmi.RemoteException,
                                 javax.ejb.EJBException
Returns the actions that can be called in the current escalation instance state
 by the logged-on user using the escalation instance ID.
 Refer to EscalationActions for possible actions.
Parameters:esiid - The object ID of the escalation instance.
 
Returns:int[] -
    The set of possible actions.
    Returns null if there are no available actions.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getAvailableActions
int[] getAvailableActions(TKIID tkiid)
                          throws IdWrongFormatException,
                                 NotAuthorizedException,
                                 ObjectDoesNotExistException,
                                 UnexpectedFailureException,
                                 java.rmi.RemoteException,
                                 javax.ejb.EJBException
Returns the actions that can be called in the current task instance state
 by the logged-on user using the task instance ID.
 Refer to TaskActions for possible actions.
Parameters:tkiid - The object ID of the task instance.
 
Returns:int[] -
    The set of possible actions.
    Returns null if there are no available actions.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1

- getAvailableActions
int[] getAvailableActions(TKTID tktid)
                          throws IdWrongFormatException,
                                 NotAuthorizedException,
                                 ObjectDoesNotExistException,
                                 UnexpectedFailureException,
                                 java.rmi.RemoteException,
                                 javax.ejb.EJBException
Returns the actions that can be called in the current task template state
 by the logged-on user using the task template ID.
 Refer to TaskTemplateActions for possible actions.
Parameters:tktid - The object ID of the task template.
 
Returns:int[] -
    The set of possible actions.
    Returns null if there are no available actions.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getApplicationComponent
ApplicationComponent getApplicationComponent(java.lang.String acoid)
                                             throws IdWrongFormatException,
                                                    IdWrongTypeException,
                                                    NotAuthorizedException,
                                                    ObjectDoesNotExistException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Retrieves the specified application component using a string
 representation of the application component ID.
 
 The caller must be the task system administrator or the task system monitor.
 
 The action associated to this method is
 ApplicationComponentActions.GETAPPLICATIONCOMPONENT.
Parameters:acoid - A string representation of the application component ID. This is used
    to identify the application component to be retrieved.
 
Returns:ApplicationComponent -
    The application component.
    Refer to ApplicationComponent to view the
    application component properties.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getApplicationComponent
ApplicationComponent getApplicationComponent(ACOID acoid)
                                             throws IdWrongFormatException,
                                                    NotAuthorizedException,
                                                    ObjectDoesNotExistException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Retrieves the specified application component using the application component ID.
 
 The caller must be the task system administrator or the task system monitor.
 
 The action associated to this method is
 ApplicationComponentActions.GETAPPLICATIONCOMPONENT.
Parameters:acoid - The object ID of the application component to be retrieved.
 
Returns:ApplicationComponent -
    The application component.
    Refer to ApplicationComponent to view the
    application component properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getCustomProperty
java.lang.String getCustomProperty(java.lang.String identifier,
                                 java.lang.String propertyName)
                                   throws IdWrongFormatException,
                                          IdWrongTypeException,
                                          NotAuthorizedException,
                                          ObjectDoesNotExistException,
                                          ParameterNullException,
                                          WrongKindException,
                                          WrongStateException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the named custom property of the specified
 task instance, task template, escalation instance, or escalation template
 using a string representation of the object ID.
 
 Custom properties allow a user to add additional properties to tasks or escalations
 beyond those provided and managed by the task manager.
 
 A custom property can be retrieved in any state of a task or escalation instance.
 The caller must have at least reader authority for the object.
 
 The action associated to this method is TaskActions.GETCUSTOMPROPERTY or
 EscalationActions.GETCUSTOMPROPERTY or
 TaskTemplateActions.GETCUSTOMPROPERTY or
 EscalationTemplateActions.GETCUSTOMPROPERTY.
Parameters:identifier - A string representation of the task instance, task template, escalation instance,
    or escalation template ID. This
    string is used to identify the object for which the
    custom property is to be retrieved.propertyName - The name of the custom property for which
    the value is to be retrieved.
 
Returns:String -
    The value of the specified custom property.
    Returns null when the specified property cannot be found.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.1
 
 Supports task templates, escalation templates, and escalation instances.

- getCustomProperty
java.lang.String getCustomProperty(ESTID estid,
                                 java.lang.String propertyName)
                                   throws IdWrongFormatException,
                                          NotAuthorizedException,
                                          ObjectDoesNotExistException,
                                          ParameterNullException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the named custom property of the specified escalation
 template using the escalation template ID.
 
 Custom properties allow a user to add additional properties to escalations
 beyond those provided and managed by the task manager.
 
 The caller must have at least reader authority for the escalation template.
 
 The action associated to this method is
 EscalationTemplateActions.GETCUSTOMPROPERTY.
Parameters:estid - The escalation template ID whose named
    custom property is to be retrieved.propertyName - The name of the custom property for which
    the value is to be retrieved.
 
Returns:String -
    The value of the specified custom property.
    Returns null when the specified property cannot be found.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getCustomProperty
java.lang.String getCustomProperty(ESIID esiid,
                                 java.lang.String propertyName)
                                   throws IdWrongFormatException,
                                          NotAuthorizedException,
                                          ObjectDoesNotExistException,
                                          ParameterNullException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the named custom property of the specified escalation
 instance using the escalation instance ID.
 
 Custom properties allow a user to add additional properties to an escalation
 beyond those provided and managed by the task manager.
 
 A custom property can be retrieved in any state of the escalation instance.
 The caller must have at least reader authority for the escalation instance.
 
 The action associated to this method is
 EscalationActions.GETCUSTOMPROPERTY.
Parameters:esiid - The escalation instance ID whose named
    custom property is to be retrieved.propertyName - The name of the custom property for which
    the value is to be retrieved.
 
Returns:String -
    The value of the specified custom property.
    Returns null when the specified property cannot be found.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getCustomProperty
java.lang.String getCustomProperty(TKTID tktid,
                                 java.lang.String propertyName)
                                   throws IdWrongFormatException,
                                          NotAuthorizedException,
                                          ObjectDoesNotExistException,
                                          ParameterNullException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the named custom property of the specified task
 template using the task template ID.
 
 Custom properties allow a user to add additional properties to tasks
 beyond those provided and managed by the task manager.
 
 The caller must have at least reader authority for the task template.
 
 The action associated to this method is
 TaskTemplateActions.GETCUSTOMPROPERTY.
Parameters:tktid - The task template ID whose named
    custom property is to be retrieved.propertyName - The name of the custom property for which
    the value is to be retrieved.
 
Returns:String -
    The value of the specified custom property.
    Returns null when the specified property cannot be found.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getCustomProperty
java.lang.String getCustomProperty(TKIID tkiid,
                                 java.lang.String propertyName)
                                   throws IdWrongFormatException,
                                          NotAuthorizedException,
                                          ObjectDoesNotExistException,
                                          ParameterNullException,
                                          WrongKindException,
                                          WrongStateException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the named custom property of the specified task
 instance using the task instance ID.
 
 Custom properties allow a user to add additional properties to a task
 beyond those provided and managed by the task manager.
 
 A custom properties can be retrieved in any state of the task instance.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETCUSTOMPROPERTY.
Parameters:tkiid - The task instance ID whose named
    custom property is to be retrieved.propertyName - The name of the custom property for which
    the value is to be retrieved.
 
Returns:String -
    The value of the specified custom property.
    Returns null when the specified property cannot be found.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1

- getCustomPropertyInfo
java.util.List getCustomPropertyInfo(int objectType,
                                   java.lang.String nameFilter,
                                   java.lang.Integer threshold)
                                     throws InvalidParameterException,
                                            WorkItemManagerException,
                                            UnexpectedFailureException,
                                            java.rmi.RemoteException,
                                            javax.ejb.EJBException
Retrieves information about custom properties of the specified object types.
 
 Custom properties allow a user to add additional properties to objects
 beyond those provided and managed by the Human Task Manager.
 
 Besides specifying an object type, you can specify a threshold or a filter to reduce
 the number of custom property information returned.
Parameters:objectType - An indicator that specifies for which object type custom property information
    is to be retrieved. If there are multiple custom properties with the same name for the
    same object type, a single information entry is returned.nameFilter - A filter on the names of custom properties.
    A SQL LIKE predicate is applied to the custom property names.threshold - Specifies the maximum number of custom property information entries to be returned from the
    server to the client. If a threshold is not to be applied, null must be specified.
 
Returns:List -
    A list of CustomPropertyInfo objects.
    For instances, information is only returned for custom properties the logged-on
    user is authorized to read.
    
    The list is empty if there are no custom properties for the specified object type
    the user is authorized to read.
 
Throws:
InvalidParameterException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2

- getCustomPropertyNames
java.util.List getCustomPropertyNames(java.lang.String identifier)
                                      throws IdWrongFormatException,
                                             IdWrongTypeException,
                                             NotAuthorizedException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves the names of all custom properties of the specified
 task instance, task template, escalation instance, or escalation template
 using a string representation of the object ID.
 
 Custom properties allow a user to add additional properties to tasks or escalations
 beyond those provided and managed by the task manager.
 
 Custom properties names can be retrieved in any state of a task or escalation instance.
 The caller must have at least reader authority for the task or escalation instance.
 
 The action associated to this method is TaskActions.GETCUSTOMPROPERTY or
 EscalationActions.GETCUSTOMPROPERTY or
 TaskTemplateActions.GETCUSTOMPROPERTY or
 EscalationTemplateActions.GETCUSTOMPROPERTY.
Parameters:identifier - A string representation of the task instance, task template, escalation
    instance, or escalation template ID. This
    string is used to identify the object for which the
    custom property names are to be retrieved.
 
Returns:List -
    A list of custom property names.
    Returns an empty list when there are no custom properties.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.1
 
 Supports escalation instances and templates.

- getCustomPropertyNames
java.util.List getCustomPropertyNames(ESTID estid)
                                      throws NotAuthorizedException,
                                             IdWrongFormatException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves the names of all custom properties of the specified
 escalation template using the escalation template ID.
 
 Custom properties allow a user to add additional properties to escalations
 beyond those provided and managed by the task manager.
 
 The caller must have at least reader authority for the escalation template.
 
 The action associated to this method is
 EscalationTemplateActions.GETCUSTOMPROPERTY.
Parameters:estid - The escalation template ID whose
    custom property names are to be retrieved.
 
Returns:List -
    A list of custom property names.
    Returns an empty list when there are no custom properties.
 
Throws:
NotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getCustomPropertyNames
java.util.List getCustomPropertyNames(ESIID esiid)
                                      throws NotAuthorizedException,
                                             IdWrongFormatException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves the names of all custom properties of the specified
 escalation instance using the escalation instance ID.
 
 Custom properties allow a user to add additional properties to escalations
 beyond those provided and managed by the task manager.
 
 Custom properties names can be retrieved in any state of the escalation instance.
 The caller must have at least reader authority for the escalation instance.
 
 The action associated to this method is
 EscalationActions.GETCUSTOMPROPERTY.
Parameters:esiid - The escalation instance ID whose
    custom property names are to be retrieved.
 
Returns:List -
    A list of custom property names.
    Returns an empty list when there are no custom properties.
 
Throws:
NotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getCustomPropertyNames
java.util.List getCustomPropertyNames(TKTID tktid)
                                      throws NotAuthorizedException,
                                             IdWrongFormatException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves the names of all custom properties of the specified
 task template using the task template ID.
 
 Custom properties allow a user to add additional properties to tasks
 beyond those provided and managed by the task manager.
 
 The caller must have at least reader authority for the task template.
 
 The action associated to this method is
 TaskTemplateActions.GETCUSTOMPROPERTY.
Parameters:tktid - The task template ID whose
    custom property names are to be retrieved.
 
Returns:List -
    A list of custom property names.
    Returns an empty list when there are no custom properties.
 
Throws:
NotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getCustomPropertyNames
java.util.List getCustomPropertyNames(TKIID tkiid)
                                      throws NotAuthorizedException,
                                             IdWrongFormatException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves the names of all custom properties of the specified
 task instance using the task instance ID.
 
 Custom properties allow a user to add additional properties to tasks
 beyond those provided and managed by the task manager.
 
 Custom properties names can be retrieved in any state of the task instance.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETCUSTOMPROPERTY.
Parameters:tkiid - The task instance ID whose
    custom property names are to be retrieved.
 
Returns:List -
    A list of custom property names.
    Returns an empty list when there are no custom properties.
 
Throws:
NotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getCustomProperties
java.util.List getCustomProperties(java.lang.String identifier)
                                   throws IdWrongFormatException,
                                          IdWrongTypeException,
                                          NotAuthorizedException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the custom properties of the specified
 task instance, task template, escalation instance, or escalation template
 using a string representation of the object ID.
 
 Custom properties allow a user to add additional properties to tasks or escalations
 beyond those provided and managed by the task manager.
 
 Custom properties can be retrieved in any state of a task or escalation instance.
 The caller must have at least reader authority for the task or escalation.
 
 The action associated to this method is TaskActions.GETCUSTOMPROPERTY or
 EscalationActions.GETCUSTOMPROPERTY or
 TaskTemplateActions.GETCUSTOMPROPERTY or
 EscalationTemplateActions.GETCUSTOMPROPERTY.
Parameters:identifier - A string representation of the task instance, task template, escalation
    instance, or escalation template ID. This
    string is used to identify the object for which the
    custom properties are to be retrieved.
 
Returns:List -
    A list of CustomProperty objects.
    Returns an empty list when there are no custom properties.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.1
 
 Supports escalation instances and templastes.

- getCustomProperties
java.util.List getCustomProperties(ESTID estid)
                                   throws IdWrongFormatException,
                                          NotAuthorizedException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the custom properties of the specified escalation template
 using the escalation template ID.
 
 Custom properties allow a user to add additional properties to an escalation
 beyond those provided and managed by the task manager.
 
 The caller must have at least reader authority for the escalation template.
 
 The action associated to this method is
 EscalationTemplateActions.GETCUSTOMPROPERTY.
Parameters:estid - The escalation template ID whose
    custom properties are to be retrieved.
 
Returns:List -
    A list of CustomProperty objects.
    Returns an empty list when there are no custom properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getCustomProperties
java.util.List getCustomProperties(ESIID esiid)
                                   throws IdWrongFormatException,
                                          NotAuthorizedException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the custom properties of the specified escalation
 instance using the escalation instance ID.
 
 Custom properties allow a user to add additional properties to an escalation
 beyond those provided and managed by the task manager.
 
 Custom properties can be retrieved in any state of the escalation instance.
 The caller must have at least reader authority for the escalation instance.
 
 The action associated to this method is
 EscalationActions.GETCUSTOMPROPERTY.
Parameters:esiid - The escalation instance ID whose
    custom properties are to be retrieved.
 
Returns:List -
    A list of CustomProperty objects.
    Returns an empty list when there are no custom properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getCustomProperties
java.util.List getCustomProperties(TKTID tktid)
                                   throws IdWrongFormatException,
                                          NotAuthorizedException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the custom properties of the specified task template
 using the task template ID.
 
 Custom properties allow a user to add additional properties to a tasks
 beyond those provided and managed by the task manager.
 
 The caller must have at least reader authority for the task template.
 
 The action associated to this method is TaskTemplateActions.GETCUSTOMPROPERTY.
Parameters:tktid - The task template ID whose
    custom properties are to be retrieved.
 
Returns:List -
    A list of CustomProperty objects.
    Returns an empty list when there are no custom properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getCustomProperties
java.util.List getCustomProperties(TKIID tkiid)
                                   throws IdWrongFormatException,
                                          NotAuthorizedException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves all custom properties of the specified task
 instance using the task instance ID.
 
 Custom properties allow a user to add additional properties to a task
 beyond those provided and managed by the task manager.
 
 Custom properties can be retrieved in any state of the task instance.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETCUSTOMPROPERTY.
Parameters:tkiid - The task instance ID whose
    custom properties are to be retrieved.
 
Returns:List -
    A list of CustomProperty objects.
    Returns an empty list when there are no custom properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getBinaryCustomProperty
BinaryCustomProperty getBinaryCustomProperty(java.lang.String identifier,
                                           java.lang.String propertyName)
                                             throws IdWrongFormatException,
                                                    IdWrongTypeException,
                                                    NotAuthorizedException,
                                                    ObjectDoesNotExistException,
                                                    ParameterNullException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Retrieves the named binary custom property of the specified
 task or escalation instance using a string representation of the object ID.
 
 Custom properties allow a user to add additional properties to tasks or escalations
 beyond those provided and managed by the task manager. Binary custom properties allow,
 for example, to attach a Java object to a task instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 A binary custom property can be retrieved in any state of a the task or escalation instance.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETCUSTOMPROPERTY or
 EscalationActions.GETCUSTOMPROPERTY.
Parameters:identifier - A string representation of the task or escalation instance ID. This
    string is used to identify the task or escalation instance for which the binary
    custom property is to be retrieved.propertyName - The name of the binary custom property to be retrieved.
 
Returns:BinaryCustomProperty -
    The BinaryCustomProperty object.
    Returns null when the named binary custom property cannot be found.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1
 
 Supports escalation instances.

- getBinaryCustomProperty
BinaryCustomProperty getBinaryCustomProperty(ESIID esiid,
                                           java.lang.String propertyName)
                                             throws IdWrongFormatException,
                                                    NotAuthorizedException,
                                                    ObjectDoesNotExistException,
                                                    ParameterNullException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Retrieves the named binary custom property of the specified
 escalation instance using the escalation instance ID.
 
 Custom properties allow a user to add additional properties to escalations
 beyond those provided and managed by the task manager. Binary custom properties allow,
 for example, to attach a Java object to an escalation instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 A binary custom property can be retrieved in any state of a the escalation instance.
 The caller must have at least reader authority for the escalation instance.
 
 The action associated to this method is
 EscalationActions.GETCUSTOMPROPERTY.
Parameters:esiid - The escalation instance ID. This ID
    is used to identify the escalation instance for which the binary
    custom property is to be retrieved.propertyName - The name of the binary custom property to be retrieved.
 
Returns:BinaryCustomProperty -
    The BinaryCustomProperty object.
    Returns null when the named binary custom property cannot be found.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getBinaryCustomProperty
BinaryCustomProperty getBinaryCustomProperty(TKIID tkiid,
                                           java.lang.String propertyName)
                                             throws IdWrongFormatException,
                                                    NotAuthorizedException,
                                                    ObjectDoesNotExistException,
                                                    ParameterNullException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Retrieves the named binary custom property of the specified
 task instance using the task instance ID.
 
 Custom properties allow a user to add additional properties to tasks
 beyond those provided and managed by the task manager. Binary custom properties allow,
 for example, to attach a Java object to a task instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 A binary custom property can be retrieved in any state of a the task instance.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETCUSTOMPROPERTY.
Parameters:tkiid - The task instance ID. This ID
    is used to identify the task instance for which the binary
    custom property is to be retrieved.propertyName - The name of the binary custom property to be retrieved.
 
Returns:BinaryCustomProperty -
    The BinaryCustomProperty object.
    Returns null when the named binary custom property cannot be found.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getBinaryCustomPropertyNames
java.util.List getBinaryCustomPropertyNames(java.lang.String identifier)
                                            throws IdWrongFormatException,
                                                   IdWrongTypeException,
                                                   NotAuthorizedException,
                                                   ObjectDoesNotExistException,
                                                   UnexpectedFailureException,
                                                   java.rmi.RemoteException,
                                                   javax.ejb.EJBException
Retrieves the names of all binary custom properties of the specified
 task or escalation instance using a string representation of the task or escalation instance ID.
 
 Custom properties allow a user to add additional properties to tasks or escalations
 beyond those provided and managed by the task manager. Binary custom properties allow,
 for example, to attach a Java object to a task instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 Binary custom properties names can be retrieved in any state of the task or escalation instance.
 The caller must have at least reader authority for the task instance.
Parameters:identifier - A string representation of the task or escalation instance ID. This
    string is used to identify the task or escalation instance for which the binary
    custom property names are to be retrieved.
 
Returns:List -
    A list of binary custom property names.
    Returns an empty list when there are no binary custom properties.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getBinaryCustomPropertyNames
java.util.List getBinaryCustomPropertyNames(ESIID esiid)
                                            throws IdWrongFormatException,
                                                   NotAuthorizedException,
                                                   ObjectDoesNotExistException,
                                                   UnexpectedFailureException,
                                                   java.rmi.RemoteException,
                                                   javax.ejb.EJBException
Retrieves the names of all binary custom properties of the specified
 escalation instance using the escalation instance ID.
 
 Custom properties allow a user to add additional properties to escalations
 beyond those provided and managed by the task manager. Binary custom properties allow,
 for example, to attach a Java object to an escalation instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 Binary custom properties names can be retrieved in any state of the escalation instance.
 The caller must have at least reader authority for the escalation instance.
Parameters:esiid - The escalation instance ID. This ID
    is used to identify the escalation instance for which the binary
    custom property names are to be retrieved.
 
Returns:List -
    A list of binary custom property names.
    Returns an empty list when there are no binary custom properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getBinaryCustomPropertyNames
java.util.List getBinaryCustomPropertyNames(TKIID tkiid)
                                            throws IdWrongFormatException,
                                                   NotAuthorizedException,
                                                   ObjectDoesNotExistException,
                                                   UnexpectedFailureException,
                                                   java.rmi.RemoteException,
                                                   javax.ejb.EJBException
Retrieves the names of all binary custom properties of the specified
 task instance using the task instance ID.
 
 Custom properties allow a user to add additional properties to tasks
 beyond those provided and managed by the task manager. Binary custom properties allow,
 for example, to attach a Java object to a task instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 Binary custom properties names can be retrieved in any state of the task instance.
 The caller must have at least reader authority for the task instance.
Parameters:tkiid - The task instance ID. This ID
    is used to identify the task instance for which the binary
    custom property names are to be retrieved.
 
Returns:List -
    A list of binary custom property names.
    Returns an empty list when there are no binary custom properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getDocumentation
java.lang.String getDocumentation(java.lang.String identifier,
                                java.util.Locale locale)
                                  throws IdWrongFormatException,
                                         IdWrongTypeException,
                                         NotAuthorizedException,
                                         ObjectDoesNotExistException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Retrieves the documentation of the specified object
 using a string representation of the object ID.
 
 Documentations can be retrieved in any state of the object.
 The caller must have at least reader authority for the object.
 
 The action associated to this method is TaskActions.GETDOCUMENTATION or
 EscalationActions.GETDOCUMENTATION or
 TaskTemplateActions.GETDOCUMENTATION or
 EscalationTemplateActions.GETDOCUMENTATION.
Parameters:identifier - A string representation of the object ID that is used
    to identify the object.locale - The locale for which the documentation is to be provided.
    If no locale is provided, then the documentation is searched for in the default language.
 
Returns:String -
    The documentation. Returns null when there is no documentation
    in the specified locale.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getDocumentation
java.lang.String getDocumentation(ESIID esiid,
                                java.util.Locale locale)
                                  throws IdWrongFormatException,
                                         NotAuthorizedException,
                                         ObjectDoesNotExistException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Retrieves the documentation of the specified escalation instance
 using the escalation instance ID.
 
 Documentations can be retrieved in any state of the escalation.
 The caller must have at least reader authority for the escalation.
 
 The action associated to this method is
 EscalationActions.GETDOCUMENTATION.
Parameters:esiid - The escalation instance ID that is used
    to identify the escalation instance.locale - The locale for which the documentation is to be provided.
    If no locale is provided, then the documentation is searched for in the default language.
 
Returns:String -
    The documentation. Returns null when there is no documentation
    in the specified locale.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getDocumentation
java.lang.String getDocumentation(ESTID estid,
                                java.util.Locale locale)
                                  throws IdWrongFormatException,
                                         NotAuthorizedException,
                                         ObjectDoesNotExistException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Retrieves the documentation of the specified escalation template
 using the escalation template ID.
 
 The caller must have at least reader authority for the escalation template.
 
 The action associated to this method is
 EscalationTemplateActions.GETDOCUMENTATION.
Parameters:estid - The escalation template ID that is used
    to identify the escalation template.locale - The locale for which the documentation is to be provided.
    If no locale is provided, then the documentation is searched for in the default language.
 
Returns:String -
    The documentation. Returns null when there is no documentation
    in the specified locale.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getDocumentation
java.lang.String getDocumentation(TKIID tkiid,
                                java.util.Locale locale)
                                  throws IdWrongFormatException,
                                         NotAuthorizedException,
                                         ObjectDoesNotExistException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Retrieves the documentation of the specified task instance
 using the task instance ID.
 
 Documentations can be retrieved in any state of the task instance.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETDOCUMENTATION.
Parameters:tkiid - The task instance ID that is used to identify the task instance.locale - The locale for which the documentation is to be provided.
    If no locale is provided, then the documentation is searched for in the default language.
 
Returns:String -
    The documentation. Returns null when there is no documentation
    in the specified locale.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getDocumentation
java.lang.String getDocumentation(TKTID tktid,
                                java.util.Locale locale)
                                  throws IdWrongFormatException,
                                         NotAuthorizedException,
                                         ObjectDoesNotExistException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Retrieves the documentation of the specified task template
 using the task template ID.
 
 The caller must have at least reader authority for the task template.
 
 The action associated to this method is
 TaskTemplateActions.GETDOCUMENTATION.
Parameters:tktid - The task template ID that is used to identify the task template.locale - The locale for which the documentation is to be provided.
    If no locale is provided, then the documentation is searched for in the default language.
 
Returns:String -
    The documentation. Returns null when there is no documentation
    in the specified locale.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getEscalation
Escalation getEscalation(java.lang.String tkiid,
                       java.lang.String escalationName)
                         throws EscalationDoesNotExistException,
                                IdWrongFormatException,
                                IdWrongTypeException,
                                NotAuthorizedException,
                                ObjectDoesNotExistException,
                                ParameterNullException,
                                UnexpectedFailureException,
                                java.rmi.RemoteException,
                                javax.ejb.EJBException
Retrieves the specified escalation instance using a string representation of
 the associated task instance ID and the escalation name.
 
 Escalations can be retrieved in any escalation state and any task state. The caller must have at least
 reader authority.
 
 The action associated to this method is
 EscalationActions.GETESCALATION.
Parameters:tkiid - A string representation of the task instance ID that is used
    to identify the associated task instance.escalationName - The name of the escalation.
 
Returns:Escalation -
    The escalation instance. Refer to Escalation
    to view the escalation properties.
 
Throws:
EscalationDoesNotExistException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0

- getEscalation
Escalation getEscalation(java.lang.String esiid)
                         throws IdWrongFormatException,
                                IdWrongTypeException,
                                NotAuthorizedException,
                                ObjectDoesNotExistException,
                                UnexpectedFailureException,
                                java.rmi.RemoteException,
                                javax.ejb.EJBException
Retrieves the specified escalation instance using a string representation of
 the escalation instance ID.
 
 Escalations can be retrieved in any escalation state. The caller must have at least
 reader authority.
 
 The action associated to this method is
 EscalationActions.GETESCALATION.
Parameters:esiid - A string representation of the escalation instance ID that is used
    to identify the escalation to be retrieved.
 
Returns:Escalation -
    The escalation instance. Refer to Escalation
    to view the escalation properties.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getEscalation
Escalation getEscalation(ESIID esiid)
                         throws IdWrongFormatException,
                                NotAuthorizedException,
                                ObjectDoesNotExistException,
                                UnexpectedFailureException,
                                java.rmi.RemoteException,
                                javax.ejb.EJBException
Retrieves the specified escalation instance using the escalation instance ID.
 
 Escalations can be retrieved in any escalation state. The caller must have at least
 reader authority.
 
 The action associated to this method is
 EscalationActions.GETESCALATION.
Parameters:esiid - The escalation instance ID that is used
    to identify the escalation to be retrieved.
 
Returns:Escalation -
    The escalation instance. Refer to Escalation
    to view the escalation properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getEscalation
Escalation getEscalation(TKIID tkiid,
                       java.lang.String escalationName)
                         throws EscalationDoesNotExistException,
                                IdWrongFormatException,
                                NotAuthorizedException,
                                ObjectDoesNotExistException,
                                ParameterNullException,
                                UnexpectedFailureException,
                                java.rmi.RemoteException,
                                javax.ejb.EJBException
Retrieves the specified escalation instance using
 the associated task instance ID and the escalation name.
 
 Escalations can be retrieved in any escalation state and any task state. The caller must have at least
 reader authority.
 
 The action associated to this method is
 EscalationActions.GETESCALATION.
Parameters:tkiid - The task instance ID that is used
    to identify the associated task instance.escalationName - The name of the escalation.
 
Returns:Escalation -
    The escalation instance. Refer to Escalation
    to view the escalation properties.
 
Throws:
EscalationDoesNotExistException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0

- getEscalationInfo
EscalationInfo getEscalationInfo(java.lang.String tkiid)
                                 throws IdWrongFormatException,
                                        IdWrongTypeException,
                                        NotAuthorizedException,
                                        ObjectDoesNotExistException,
                                        UnexpectedFailureException,
                                        java.rmi.RemoteException,
                                        javax.ejb.EJBException
Retrieves information about all escalations of the specified task instance using
 a string representation of the task instance ID.
 
 Escalation information can be retrieved in any task state. The caller must have at least
 reader authority.
Parameters:tkiid - A string representation of the task instance ID that is used
    to identify the task instance.
 
Returns:EscalationInfo -
    The escalation information. Refer to EscalationInfo
    to view the information returned.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0

- getEscalationInfo
EscalationInfo getEscalationInfo(TKIID tkiid)
                                 throws IdWrongFormatException,
                                        NotAuthorizedException,
                                        ObjectDoesNotExistException,
                                        UnexpectedFailureException,
                                        java.rmi.RemoteException,
                                        javax.ejb.EJBException
Retrieves information about all escalations of the specified task instance using
 the task instance ID.
 
 Escalation information can be retrieved in any task state. The caller must have at least
 reader authority.
Parameters:tkiid - The task instance ID that is used
    to identify the task instance.
 
Returns:EscalationInfo -
    The escalation information. Refer to EscalationInfo
    to view the information returned.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0

- getEscalationTemplate
EscalationTemplate getEscalationTemplate(java.lang.String estid)
                                         throws IdWrongFormatException,
                                                IdWrongTypeException,
                                                NotAuthorizedException,
                                                ObjectDoesNotExistException,
                                                UnexpectedFailureException,
                                                java.rmi.RemoteException,
                                                javax.ejb.EJBException
Retrieves the specified escalation template using
  a string representation of the escalation template ID.
 
 The caller must have at least reader authority.
 
 The action associated to this method is
 EscalationTemplateActions.GETESCALATIONTEMPLATE.
Parameters:estid - A string representation of the escalation template ID that is used
    to identify the escalation template to be retrieved.
 
Returns:EscalationTemplate -
    The escalation template. Refer to EscalationTemplate
    to view the escalation template properties.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getEscalationTemplate
EscalationTemplate getEscalationTemplate(ESTID estid)
                                         throws IdWrongFormatException,
                                                NotAuthorizedException,
                                                ObjectDoesNotExistException,
                                                UnexpectedFailureException,
                                                java.rmi.RemoteException,
                                                javax.ejb.EJBException
Retrieves the specified escalation template using the escalation template ID.
 
 The caller must have at least reader authority.
 
 The action associated to this method is
 EscalationTemplateActions.GETESCALATIONTEMPLATE.
Parameters:estid - The escalation template ID that is used
    to identify the escalation template to be retrieved.
 
Returns:EscalationTemplate -
    The escalation template. Refer to EscalationTemplate
    to view the escalation template properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getFaultMessage
ClientObjectWrapper getFaultMessage(java.lang.String tkiid)
                                    throws DataHandlingException,
                                           IdWrongFormatException,
                                           IdWrongTypeException,
                                           NotAuthorizedException,
                                           ObjectDoesNotExistException,
                                           WrongKindException,
                                           WrongStateException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Retrieves the fault message of the specified task instance using
 a string representation of the task instance ID.
 
 The task instance must be a to-do, collaboration, or invocation task.
 Collaboration, to-do, and invocation task instances are also known as
 human, participating, and originating task instances.
 
 The task instance can be in any state but inactive.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is
 TaskActions.GETFAULTMESSAGE.
Parameters:tkiid - A string representation of the task instance ID. This string is used to
    identify the task instance for which the fault message is to be retrieved.
 
Returns:ClientObjectWrapper -
    The fault message. If there is no fault message,
    an empty client object wrapper is returned.
 
Throws:
DataHandlingException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1

- getFaultMessage
ClientObjectWrapper getFaultMessage(TKIID tkiid)
                                    throws DataHandlingException,
                                           IdWrongFormatException,
                                           NotAuthorizedException,
                                           ObjectDoesNotExistException,
                                           WrongKindException,
                                           WrongStateException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Retrieves the fault message of the specified task instance
 using the task instance ID.
 
 The task instance must be a to-do, collaboration, or invocation task.
 Collaboration, to-do, and invocation task instances are also known as
 human, participating, and originating task instances.
 
 The task instance can be in any state but inactive.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is
 TaskActions.GETFAULTMESSAGE.
Parameters:tkiid - The object ID of the task instance for which the fault message is to be retrieved.
 
Returns:ClientObjectWrapper -
    The fault message. If there is no fault message,
    an empty client object wrapper is returned.
 
Throws:
DataHandlingException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1

- getFaultNames
java.util.List getFaultNames(java.lang.String identifier)
                             throws IdWrongFormatException,
                                    IdWrongTypeException,
                                    NotAuthorizedException,
                                    ObjectDoesNotExistException,
                                    WrongKindException,
                                    WrongStateException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Retrieves the fault names defined for the specified task instance or template
 using a string representation of the task instance or template ID.
 
 The task instance or template must be a to-do, collaboration, or invocation task.
 Collaboration, to-do, and invocation tasks are also known as
 human, participating, and originating tasks.
 
 The task instance or template can be in any state.
 
 The caller must have at least reader authority for the task instance or template.
 
 The action associated to this method is TaskActions.GETFAULTNAMES or
 TaskTemplateActions.GETFAULTNAMES.
Parameters:identifier - A string representation of the task instance or template ID that
    is used to identify the task instance or template for which fault names are to be retrieved.
 
Returns:List -
    A list of fault names. If there are no faults, an empty list is returned.
    Fault names are to be specified when a fault message is set or created.
    Refer to complete,
    setFaultMessage,
    or to createFaultMessage(TKIID),
    or to createFaultMessage(TKTID).
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
7.0
 
 Supports task templates.

- getFaultNames
java.util.List getFaultNames(TKTID tktid)
                             throws IdWrongFormatException,
                                    NotAuthorizedException,
                                    ObjectDoesNotExistException,
                                    WrongKindException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Retrieves the fault names defined for the specified task template
 using the task template ID.
 
 The task template must describe a to-do, collaboration, or invocation task.
 Collaboration, to-do, and invocation tasks are also known as
 human, participating, and originating tasks.
 
 The task template can be in any state.
 The caller must have at least reader authority for the task template.
 
 The action associated to this method is
 TaskTemplateActions.GETFAULTNAMES.
Parameters:tktid - The object ID of the task template for which the fault names are to be retrieved.
 
Returns:List -
    A list of fault names. If there are no faults, an empty list is returned.
    Fault names are to be specified when a fault message is set or created.
    Refer to complete,
    setFaultMessage,
    or to createFaultMessage.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0

- getFaultNames
java.util.List getFaultNames(TKIID tkiid)
                             throws IdWrongFormatException,
                                    NotAuthorizedException,
                                    ObjectDoesNotExistException,
                                    WrongKindException,
                                    WrongStateException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Retrieves the fault names defined for the specified task instance
 using the task instance ID.
 
 The task instance must be a to-do, collaboration, or invocation task.
 Collaboration, to-do, and invocation task instances are also known as
 human, participating, and originating task instances.
 
 The task instance can be in any state.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETFAULTNAMES.
Parameters:tkiid - The object ID of the task instance for which the fault names are to be retrieved.
 
Returns:List -
    A list of fault names. If there are no faults, an empty list is returned.
    Fault names are to be specified when a fault message is set.
    Refer to complete,
    setFaultMessage,
    or to createFaultMessage.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1

- getGroupDetails
java.util.List getGroupDetails(java.lang.String[] groupNames,
                             java.lang.String[] groupProperties,
                             java.lang.String[] userProperties,
                             java.lang.String[] subGroupProperties,
                             java.lang.Integer threshold)
                               throws ParameterNullException,
                                      StaffServiceCannotAccessVMMException,
                                      StaffServiceRuntimeException,
                                      UnexpectedFailureException,
                                      java.rmi.RemoteException,
                                      javax.ejb.EJBException
Returns details about the specified groups.
 All properties of type String from the VMM Group object
 can be requested, for example, displayName or description.
 
 Note that this request does not participate in any global transaction, that is, exceptions do
 not cause a global transaction rollback.
Parameters:groupNames - The groups that are to be queried. The names are unique names as defined in VMM.groupProperties - The Group VMM properties that are to be returned
    for the specified groups. The "members" property is ignored, if specified.userProperties - The PersonAccount VMM properties that are to be returned for the users
    directly contained in the group. If not specified, an empty list of user details is returned.subGroupProperties - The Group VMM properties that are to be returned for the subgroups
    directly contained in the group. If not specified, an empty list of group details is returned.
    Note that the "members" property is ignored, if specified.threshold - The maximum number of group, user, or subgroup details to be returned from the
    server to the client. If a threshold is not to be applied, null must be specified.
 
    Group details are determined depth-first. This means that the last group returned
    may not be complete if a threshold is applied.
 
Returns:List -
    A list of GroupDetail objects.
    An object is returned for each group specified even when the group does not exist.
    In that case, the group is marked as not found in the peopele directory.
 
Throws:
ParameterNullException
StaffServiceCannotAccessVMMException
StaffServiceRuntimeException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2

- getGroupNames
java.lang.String[] getGroupNames()
                                 throws UserDoesNotExistException,
                                        UserRegistryException,
                                        UnexpectedFailureException,
                                        java.rmi.RemoteException,
                                        javax.ejb.EJBException
Returns the names of groups the logged-on user is part of.
 The names returned may be names of groups that are defined in the user registry
 as well as names of dynamically allocated groups.
 
Returns:String[] -
    An array of group names. When the user is not part of a group or
    when group work items are not enabled, an empty array is returned.
 
Throws:
UserDoesNotExistException
UserRegistryException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2

- getHtmConfiguration
HtmConfiguration getHtmConfiguration()
                                     throws java.rmi.RemoteException,
                                            javax.ejb.EJBException
Returns configuration settings of the Human Task Manager.
 
 This interface returns configuration settings that influence the functionality of
 specific API methods. For example, whether substitution or group work items are enabled.
 
Returns:HtmConfiguration -
    Human Task Manager configuration settings.
    Refer to HtmConfiguration to view the Human Task Manager
    configuration settings returned.
 
Throws:
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getInlineCustomProperty
InlineCustomProperty getInlineCustomProperty(java.lang.String identifier,
                                           java.lang.String propertyName)
                                             throws IdWrongFormatException,
                                                    IdWrongTypeException,
                                                    NotAuthorizedException,
                                                    ObjectDoesNotExistException,
                                                    ParameterNullException,
                                                    UnsupportedParameterValueException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Retrieves the named inline custom property of the specified task template
 or task instance using string representations of the object IDs.
 
 Custom properties allow a user to add additional properties to a task
 beyond those provided and managed by the Human Task Manager.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the task template or instance. Thus, using inline custom properties
 can increase performance.
 
 Custom properties can be retrieved in any state of the task instance.
 The caller must have at least reader authority for the task instance or task template.
 
 The action associated to this method is TaskActions.GETCUSTOMPROPERTY
 respectively TaskTemplateActions.GETCUSTOMPROPERTY.
Parameters:identifier - A string representation of the task template or task instance object ID. This
    string is used to identify the object for which the inline custom property is to be retrieved.propertyName - The name of the inline custom property for which the value is to be retrieved.
    The name can be one of the predefined names
    InlineCustomProperty.CUSTOM\_TEXT\_1 etc.
 
Returns:InlineCustomProperty -
    The InlineCustomProperty.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnsupportedParameterValueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- getInlineCustomProperty
InlineCustomProperty getInlineCustomProperty(TKTID tktid,
                                           java.lang.String propertyName)
                                             throws IdWrongFormatException,
                                                    NotAuthorizedException,
                                                    ObjectDoesNotExistException,
                                                    ParameterNullException,
                                                    UnsupportedParameterValueException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Retrieves the named inline custom property of the specified task template using the task template ID.
 
 Custom properties allow a user to add additional properties to a task template
 beyond those provided and managed by the Human Task Manager.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the task template. Thus, using inline custom properties
 can increase performance.
 
 The caller must have at least reader authority for the task template.
 
 The action associated to this method is TaskTemplateActions.GETCUSTOMPROPERTY.
Parameters:tktid - The task template object ID whose named custom property is to be retrieved.propertyName - The name of the inline custom property for which the value is to be read.
    The name can be one of the predefined names
    InlineCustomProperty.CUSTOM\_TEXT\_1 etc.
 
Returns:InlineCustomProperty -
    The InlineCustomProperty.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnsupportedParameterValueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- getInlineCustomProperty
InlineCustomProperty getInlineCustomProperty(TKIID tkiid,
                                           java.lang.String propertyName)
                                             throws IdWrongFormatException,
                                                    NotAuthorizedException,
                                                    ObjectDoesNotExistException,
                                                    ParameterNullException,
                                                    UnsupportedParameterValueException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Retrieves the named inline custom property of the specified task instance using the task instance ID.
 
 Custom properties allow a user to add additional properties to a task instance
 beyond those provided and managed by the Human Task Manager.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the task instance. Thus, using inline custom properties
 can increase performance.
 
 Custom properties can be retrieved in any state of the task instance.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETCUSTOMPROPERTY.
Parameters:tkiid - The task instance object ID whose custom property is to be retrieved.propertyName - The name of the custom property for which the value is to be retrieved.
    The name can be one of the predefined names
    InlineCustomProperty.CUSTOM\_TEXT\_1 etc.
 
Returns:InlineCustomProperty -
    The InlineCustomProperty.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnsupportedParameterValueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- getInputMessage
ClientObjectWrapper getInputMessage(java.lang.String tkiid)
                                    throws DataHandlingException,
                                           IdWrongFormatException,
                                           IdWrongTypeException,
                                           NotAuthorizedException,
                                           ObjectDoesNotExistException,
                                           WrongKindException,
                                           WrongStateException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Retrieves the input message of the specified task instance using a
 string representation of the task instance ID.
 
 The input message can be retrieved in any state of the task instance.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETINPUTMESSAGE.
Parameters:tkiid - A string representation of the task instance ID. The string is used
    to identify the task instance for which the input message
    is to be retrieved.
 
Returns:ClientObjectWrapper -
    The input message. Returns an empty client object wrapper
    when there is no input message.
 
Throws:
DataHandlingException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1

- getInputMessage
ClientObjectWrapper getInputMessage(TKIID tkiid)
                                    throws DataHandlingException,
                                           IdWrongFormatException,
                                           NotAuthorizedException,
                                           ObjectDoesNotExistException,
                                           WrongKindException,
                                           WrongStateException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Retrieves the input message of the task instance using the task instance ID.
 
 The input message can be retrieved in any state of the task instance.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETINPUTMESSAGE.
Parameters:tkiid - The object ID of the task instance whose input message is to be retrieved.
 
Returns:ClientObjectWrapper -
    The input message. Returns an empty client object wrapper
    when there is no input message.
 
Throws:
DataHandlingException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1

- getMessageTextOfException
java.lang.String getMessageTextOfException(java.util.Locale locale,
                                         java.lang.String messageKey,
                                         java.lang.Object[] variableValues)
                                           throws ParameterNullException,
                                                  ObjectDoesNotExistException,
                                                  UnexpectedFailureException,
                                                  java.rmi.RemoteException,
                                                  javax.ejb.EJBException
Retrieves the message text associated to the specified message key and locale.
Parameters:locale - The locale to specify the language in which the message text is to be retrieved.
    If no locale is specified, the default language of the server is used.messageKey - The message key of the exception.variableValues - The values of variables to be pasted into the message text, if any.
 
Returns:String -
    The message text.
 
Throws:
ParameterNullException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getOperationMode
int getOperationMode()
                     throws java.rmi.RemoteException,
                            javax.ejb.EJBException
Indicates whether the Human Task Manager database is used as an archive.
 
 If the Human Task Manager database is used as an archive, then
 only reading methods can be called. All method calls that try to change the archive throw
 an ArchiveUnsupportedOperationException.
 
Returns:int -
    States whether the Human Task Manager database is used as an archive or not.
    Refer to OperationMode for more details.
 
Throws:
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2.0.3

- getOutputMessage
ClientObjectWrapper getOutputMessage(java.lang.String tkiid)
                                     throws DataHandlingException,
                                            IdWrongFormatException,
                                            IdWrongTypeException,
                                            NotAuthorizedException,
                                            ObjectDoesNotExistException,
                                            WrongKindException,
                                            WrongStateException,
                                            UnexpectedFailureException,
                                            java.rmi.RemoteException,
                                            javax.ejb.EJBException
Retrieves the output message of the specified task instance
 using a string representation of the ID.
 
 The output message can be retrieved in any state of the task instance.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETOUTPUTMESSAGE.
Parameters:tkiid - A string representation of the task instance ID that is used
    to identify the task instance for which the output message is to be retrieved.
 
Returns:ClientObjectWrapper -
    The output message. If the output message has not yet been set,
    an empty client object wrapper is returned.
 
Throws:
DataHandlingException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1

- getOutputMessage
ClientObjectWrapper getOutputMessage(TKIID tkiid)
                                     throws DataHandlingException,
                                            IdWrongFormatException,
                                            NotAuthorizedException,
                                            ObjectDoesNotExistException,
                                            WrongKindException,
                                            WrongStateException,
                                            UnexpectedFailureException,
                                            java.rmi.RemoteException,
                                            javax.ejb.EJBException
Retrieves the output message of the specified task instance
 using the task instance ID.
 
 The output message can be retrieved in any state of the task instance.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETOUTPUTMESSAGE.
Parameters:tkiid - The object ID of the task instance whose output message is to be retrieved.
 
Returns:ClientObjectWrapper -
    The output message. If the output message has not yet been set,
    an empty client object wrapper is returned.
 
Throws:
DataHandlingException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1

- getStoredQuery
StoredQuery getStoredQuery(java.lang.String storedQueryName)
                           throws ObjectDoesNotExistException,
                                  ParameterNullException,
                                  UnexpectedFailureException,
                                  java.rmi.RemoteException,
                                  javax.ejb.EJBException
Retrieves the specified stored query definition. If a private stored query
 exists for the calling user, then the private stored query is returned; otherwise
 the public stored query with the specified name.
Parameters:storedQueryName - The name of the stored query to be retrieved -
    refer to getStoredQueryNames
    for the retrieval of existing stored query names.
 
Returns:StoredQuery -
    StoredQuery -
    The definition of the stored query retrieved - refer to StoredQuery
    to view the stored query definition.
 
Throws:
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.0.2
 
 Supports private stored queries.

- getStoredQuery
StoredQuery getStoredQuery(java.lang.String userID,
                         java.lang.String storedQueryName)
                           throws NotAuthorizedException,
                                  ObjectDoesNotExistException,
                                  ParameterNullException,
                                  UnexpectedFailureException,
                                  java.rmi.RemoteException,
                                  javax.ejb.EJBException
Retrieves the specified stored query definition for the specified user.
    You must be a task system administrator to retrieve the private stored query of a different user.
Parameters:userID - The name of the user who is the owner of the stored query. If no user is
    specified, a public stored query with the specified name is retrieved.storedQueryName - The name of the stored query to be retrieved -
    refer to getStoredQueryNames
    for the retrieval of existing stored query names.
 
Returns:StoredQuery -
    StoredQuery -
    The definition of the stored query retrieved - refer to StoredQuery
    to view the stored query definition.
 
Throws:
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getStoredQuery
StoredQuery getStoredQuery(int kind,
                         java.lang.String storedQueryName)
                           throws InvalidParameterException,
                                  ObjectDoesNotExistException,
                                  ParameterNullException,
                                  UnexpectedFailureException,
                                  java.rmi.RemoteException,
                                  javax.ejb.EJBException
Retrieves the specified private or public stored query definition.
Parameters:kind - An indicator to specify whether a private or public stored query is to be
    retrieved.
 
    KIND\_PUBLIC states that a public stored query is to be retrieved.
    KIND\_PRIVATE states that a private stored query for the logged-on user is to be retrieved.storedQueryName - The name of the stored query to be retrieved -
    refer to getStoredQueryNames
    for the retrieval of existing stored query names.
 
Returns:StoredQuery -
    StoredQuery -
    The definition of the stored query retrieved - refer to StoredQuery
    to view the stored query definition.
 
Throws:
InvalidParameterException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getStoredQueryNames
java.lang.String[] getStoredQueryNames()
                                       throws WorkItemManagerException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
Retrieves the names of stored queries that are persistently stored in the database.
 Both the names of public and private stored queries are returned.
 
 Refer to createStoredQuery for the
 creation of stored queries.
 
Returns:String[] -
    String[] -
    An array of stored query names. If there are no stored queries, an empty
    array is returned.
 
Throws:
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.0.2
 
 Supports private stored queries.

- getStoredQueryNames
java.lang.String[] getStoredQueryNames(java.lang.String userID)
                                       throws NotAuthorizedException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
Retrieves the names of stored queries that are persistently stored in the database
 for the specified user. Both the names of public and private stored queries are returned.
 You must be a task system administrator to retrieve informations of a different user.
 
 Refer to createStoredQuery for the
 creation of stored queries.
Parameters:userID - The name of the user who is the owner of the private stored queries whose names are to
    be retrieved together with any public names. A regular user can only specify his
    own name; a task system administrator can also specify the name of a different user.
 
Returns:String[] -
    String[] -
    An array of stored query names. If there are no stored queries, an empty
    array is returned.
 
Throws:
NotAuthorizedException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getStoredQueryNames
java.lang.String[] getStoredQueryNames(int kind)
                                       throws InvalidParameterException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
Retrieves the names of private or public stored queries that are persistently stored in the database.
 
 Refer to createStoredQuery for the
 creation of stored queries.
Parameters:kind - An indicator to specify whether a private or public stored query names are to be
    retrieved.
 
    KIND\_PUBLIC states that names of public stored queries are to be retrieved.
    KIND\_PRIVATE states that names of private stored queries for the logged-on user are to be retrieved.
 
Returns:String[] -
    String[] -
    An array of stored query names. If there are no stored queries, an empty
    array is returned.
 
Throws:
InvalidParameterException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getSubTaskIDs
java.util.List getSubTaskIDs(java.lang.String tkiid)
                             throws IdWrongFormatException,
                                    IdWrongTypeException,
                                    NotAuthorizedException,
                                    ObjectDoesNotExistException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Retrieves the object IDs of all task instances that are subtasks of the
 specified task instance using a string representation of the task instance ID.
 
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETTASK.
Parameters:tkiid - A string representation of the task instance ID that is used to identify
    the task instance for which the subtask IDs are to be retrieved.
 
Returns:List -
    A list of task instance IDs (TKIID).
    Returns an empty list when there are no subtasks.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getSubTaskIDs
java.util.List getSubTaskIDs(TKIID tkiid)
                             throws IdWrongFormatException,
                                    NotAuthorizedException,
                                    ObjectDoesNotExistException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Retrieves the object IDs of all task instances that are subtasks of the
 specified task instance using the task instance ID.
 
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETTASK.
Parameters:tkiid - The task instance ID that is used to identify the task instance
    for which the subtask IDs are to be retrieved.
 
Returns:List -
    A list of task instance IDs (TKIID).
    Returns an empty list when there are no subtasks.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getSubstitutes
java.util.List getSubstitutes()
                              throws StaffServiceCannotAccessVMMException,
                                     StaffServiceSubstitutionNotEnabledException,
                                     StaffServiceRuntimeException,
                                     UserDoesNotExistException,
                                     UnexpectedFailureException,
                                     java.rmi.RemoteException,
                                     javax.ejb.EJBException
Deprecated. As of version 7.0, replaced by getUserSubstitutionDetail.
 
Retrieves the substitutes of the logged-on user.
Returns:List -
    A list of users that substitute the logged-on user.
    Returns an empty list when there are no substitutes.
 
Throws:
StaffServiceCannotAccessVMMException
StaffServiceSubstitutionNotEnabledException
StaffServiceRuntimeException
UserDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getSubstitutes
java.util.List getSubstitutes(java.lang.String userID)
                              throws NotAuthorizedException,
                                     ParameterNullException,
                                     StaffServiceCannotAccessVMMException,
                                     StaffServiceSubstitutionNotEnabledException,
                                     StaffServiceRuntimeException,
                                     UserDoesNotExistException,
                                     UnexpectedFailureException,
                                     java.rmi.RemoteException,
                                     javax.ejb.EJBException
Deprecated. As of version 7.0, replaced by getUserSubstitutionDetail.
Retrieves the substitutes of the specified user.
  
  If retrieving the substitutes is not restricted to administrators, then everybody can
  retrieve the substitutes of any user.
  
  If retrieving the substitutes is restricted to administrators, then only
  task system monitors or task system administrators can retrieve the substitutes
  of arbitrary users. A user may, however, always read his/her personal settings.
Parameters:userID - The name of the user whose substitutes are to be retrieved.
 
Returns:List -
    A list of users that substitute the specified user.
    Returns an empty list when there are no substitutes.
 
Throws:
NotAuthorizedException
ParameterNullException
StaffServiceCannotAccessVMMException
StaffServiceSubstitutionNotEnabledException
StaffServiceRuntimeException
UserDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getTask
Task getTask(java.lang.String tkiid)
             throws IdWrongFormatException,
                    IdWrongTypeException,
                    NotAuthorizedException,
                    ObjectDoesNotExistException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Retrieves the specified task instance using a string
 representation of the task instance ID.
 
 The task instance can be in any state.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETTASK.
Parameters:tkiid - A string representation of the task instance ID. This is used
    to identify the task instance to be retrieved.
 
Returns:Task -
    The task instance.
    Refer to Task to view the task instance properties.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1

- getTask
Task getTask(TKIID tkiid)
             throws IdWrongFormatException,
                    NotAuthorizedException,
                    ObjectDoesNotExistException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Retrieves the specified task instance using the task instance ID.
 
 The task instance can be in any state.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETTASK.
Parameters:tkiid - The object ID of the task instance to be retrieved.
 
Returns:Task -
    The task instance.
    Refer to Task to view the task instance properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1

- getTaskAndMarkRead
Task getTaskAndMarkRead(java.lang.String tkiid)
                        throws ApplicationVetoException,
                               ArchiveUnsupportedOperationException,
                               IdWrongFormatException,
                               IdWrongTypeException,
                               NotAuthorizedException,
                               ObjectDoesNotExistException,
                               UnexpectedFailureException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
Retrieves the specified task instance using a string
 representation of the task instance ID and marks the task as read.
 
 The task instance can be in any state.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETTASK.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID. This is used
    to identify the task instance to be retrieved.
 
Returns:Task -
    The task instance.
    Refer to Task to view the task instance properties.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- getTaskAndMarkRead
Task getTaskAndMarkRead(TKIID tkiid)
                        throws ApplicationVetoException,
                               ArchiveUnsupportedOperationException,
                               IdWrongFormatException,
                               NotAuthorizedException,
                               ObjectDoesNotExistException,
                               UnexpectedFailureException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
Retrieves the specified task instance using the task instance ID
 and marks the task as read.
 
 The task instance can be in any state.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETTASK.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID of the task instance to be retrieved.
 
Returns:Task -
    The task instance.
    Refer to Task to view the task instance properties.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- getTaskHistory
java.util.List getTaskHistory(java.lang.String tkiid)
                              throws IdWrongFormatException,
                                     IdWrongTypeException,
                                     NotAuthorizedException,
                                     ObjectDoesNotExistException,
                                     WorkItemManagerException,
                                     UnexpectedFailureException,
                                     java.rmi.RemoteException,
                                     javax.ejb.EJBException
Retrieves the history events associated to the specified task instance
 using a string representation of the task instance ID.
 
 The task instance can be in any state.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETTASK.
Parameters:tkiid - A string representation of the task instance ID. This is used
    to identify the task instance whose history events are to be retrieved.
 
Returns:List -
    A list of TaskHistoryEvent objects.
    Returns an empty list when there are no history events.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5

- getTaskHistory
java.util.List getTaskHistory(TKIID tkiid)
                              throws IdWrongFormatException,
                                     NotAuthorizedException,
                                     ObjectDoesNotExistException,
                                     WorkItemManagerException,
                                     UnexpectedFailureException,
                                     java.rmi.RemoteException,
                                     javax.ejb.EJBException
Retrieves the history events associated to the specified task instance
 using the task instance ID.
 
 The task instance can be in any state.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETTASK.
Parameters:tkiid - The object ID of the task instance. This is used
    to identify the task instance whose history events are to be retrieved.
 
Returns:List -
    A list of TaskHistoryEvent objects.
    Returns an empty list when there are no history events.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5

- getTaskRead
boolean getTaskRead(java.lang.String tkiid)
                    throws IdWrongFormatException,
                           IdWrongTypeException,
                           NotAuthorizedException,
                           ObjectDoesNotExistException,
                           UnexpectedFailureException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
States whether the specified task instance is marked read using
  a string representation of the task instance ID.
  
  The task instance can be in any state.
  The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETTASK.
Parameters:tkiid - A string representation of the task instance ID
    that is used to identify the task instance.
 
Returns:boolean -
    States whether the task is marked read.
   True states that the task is marked read.
   False states that the task is not marked read.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0

- getTaskRead
boolean getTaskRead(TKIID tkiid)
                    throws IdWrongFormatException,
                           NotAuthorizedException,
                           ObjectDoesNotExistException,
                           UnexpectedFailureException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
States whether the specified task instance is marked read using
  the task instance ID.
  
  The task instance can be in any state.
  The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETTASK.
Parameters:tkiid - The object ID of the task instance
    that is used to identify the task instance.
 
Returns:boolean -
    States whether the task is marked read.
   True states that the task is marked read.
   False states that the task is not marked read.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0

- getTaskTemplate
TaskTemplate getTaskTemplate(java.lang.String tktid)
                             throws IdWrongFormatException,
                                    IdWrongTypeException,
                                    NotAuthorizedException,
                                    ObjectDoesNotExistException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Retrieves the specified task template using a string representation of
 the task template ID.
 
 The caller must have at least reader authority for the task template.
 
 The action associated to this method is TaskTemplateActions.GETTEMPLATE.
Parameters:tktid - A string representation of the object ID of the task template to be retrieved.
 
Returns:TaskTemplate -
    The task template.
    Refer to TaskTemplate to view the task template properties.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getTaskTemplate
TaskTemplate getTaskTemplate(TKTID tktid)
                             throws IdWrongFormatException,
                                    NotAuthorizedException,
                                    ObjectDoesNotExistException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Retrieves the specified task template using the task template ID.
 
 The caller must have at least reader authority for the task template.
 
 The action associated to this method is TaskTemplateActions.GETTEMPLATE.
Parameters:tktid - The object ID of the task template to be retrieved.
 
Returns:TaskTemplate -
    The task template.
    Refer to TaskTemplate to view the task template properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getActivityID
AIID getActivityID(java.lang.String tkiid)
                   throws IdWrongFormatException,
                          IdWrongTypeException,
                          NotAuthorizedException,
                          ObjectDoesNotExistException,
                          UnexpectedFailureException,
                          java.rmi.RemoteException,
                          javax.ejb.EJBException
Retrieves the object ID of the activity instance associated to the specified task instance
 using a string representation of the task instance ID.
 
 The task instance can be in any state.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETTASK.
Parameters:tkiid - A string representation of the task instance ID. This is used
    to identify the task instance.
 
Returns:AIID -
    The object ID of the associated activity instance in a BPEL process.
    Returns null when there is no associated activity instance, for example,
    when the task is no inline to-do aka participating task in a BPEL process.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getActivityID
AIID getActivityID(TKIID tkiid)
                   throws IdWrongFormatException,
                          NotAuthorizedException,
                          ObjectDoesNotExistException,
                          UnexpectedFailureException,
                          java.rmi.RemoteException,
                          javax.ejb.EJBException
Retrieves the object ID of the activity instance associated to the specified task instance
 using the task instance ID.
 
 The task instance can be in any state.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETTASK.
Parameters:tkiid - The object ID of the task instance.
 
Returns:AIID -
    The object ID of the associated activity instance in a BPEL process.
    Returns null when there is no associated activity instance, for example,
    when the task is no inline to-do aka participating task in a BPEL process.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getProcessID
PIID getProcessID(java.lang.String tkiid)
                  throws IdWrongFormatException,
                         IdWrongTypeException,
                         NotAuthorizedException,
                         ObjectDoesNotExistException,
                         UnexpectedFailureException,
                         java.rmi.RemoteException,
                         javax.ejb.EJBException
Retrieves the object ID of the BPEL process instance that contains the specified
 task instance using a string representation of the task instance ID.
 
 The task instance can be in any state.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETTASK.
Parameters:tkiid - A string representation of the task instance ID. This is used
    to identify the task instance.
 
Returns:PIID -
    The object ID of the associated BPEL process instance.
    Returns null when there is no associated process instance, for example,
    when the task is not an integral part of a process.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getProcessID
PIID getProcessID(TKIID tkiid)
                  throws IdWrongFormatException,
                         NotAuthorizedException,
                         ObjectDoesNotExistException,
                         UnexpectedFailureException,
                         java.rmi.RemoteException,
                         javax.ejb.EJBException
Retrieves the object ID of the BPEL process instance that contains the specified
 task instance using the task instance ID.
 
 The task instance can be in any state.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETTASK.
Parameters:tkiid - The object ID of the task instance.
 
Returns:PIID -
    The object ID of the associated BPEL process instance.
    Returns null when there is no associated process instance, for example,
    when the task is not an integral part of a process.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getUISettings
CustomClientSettings getUISettings(java.lang.String identifier)
                                   throws IdWrongFormatException,
                                          IdWrongTypeException,
                                          NotAuthorizedException,
                                          ObjectDoesNotExistException,
                                          WrongKindException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves client interface settings for the specified task instance or template
 using a string representation of the object ID.
 
 Client interface settings allow for the specification of presentations that can
 be used by the caller to present objects and data to an end user.
 
 Client interface settings can be retrieved in any state of the task instance.
 The caller must have at least reader authority for the task instance or template.
 
 The action associated to this method is TaskActions.GETUISETTINGS or
 TaskTemplateActions.GETUISETTINGS.
Parameters:identifier - A string representation of the task instance or template ID.
 
Returns:CustomClientSettings -
    The customized client interface settings.
    Returns null when there are no client interface settings.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1

- getUISettings
CustomClientSettings getUISettings(TKTID tktid)
                                   throws IdWrongFormatException,
                                          NotAuthorizedException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          WrongKindException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves client interface settings for the specified task template
 using the task template ID.
 
 Client interface settings allow for the specification of presentations that can
 be used by the caller to present objects and data to an end user.
 
 The caller must have at least reader authority for the task template.
 
 The action associated to this method is
 TaskTemplateActions.GETUISETTINGS.
Parameters:tktid - The object ID of the task template.
 
Returns:CustomClientSettings -
    The customized client interface settings.
    Returns null when there are no client interface settings.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
WrongKindException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getUISettings
CustomClientSettings getUISettings(TKIID tkiid)
                                   throws IdWrongFormatException,
                                          NotAuthorizedException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          WrongKindException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves client interface settings for the specified task instance
 using the task instance ID.
 
 Client interface settings allow for the specification of presentations that can
 be used by the caller to present objects and data to an end user.
 
 Client interface settings can be retrieved in any state of the task instance.
 The caller must have at least reader authority for the task instance.
 
 The action associated to this method is TaskActions.GETUISETTINGS.
Parameters:tkiid - The object ID of the task instance.
 
Returns:CustomClientSettings -
    The customized client interface settings.
    Returns null when there are no client interface settings.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
WrongKindException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1

- getUserDetails
java.util.List getUserDetails(java.lang.String[] userIDs,
                            java.lang.String[] userProperties)
                              throws ParameterNullException,
                                     StaffServiceCannotAccessVMMException,
                                     StaffServiceRuntimeException,
                                     UnexpectedFailureException,
                                     java.rmi.RemoteException,
                                     javax.ejb.EJBException
Retrieves details about the specified users.
 All properties of type String or IdentifierType from the VMM PersonAccount object
 can be requested, for example, uid, cn, sn, givenName, or manager. For properties of
 type IdentifierType, the sub-property uniqueName is returned as a string.
 
 Note that this request does not participate in any global transaction, that is, exceptions do
 not cause a global transaction rollback.
Parameters:userIDs - The users that are to be queried.userProperties - The PersonAccount VMM properties that are to be returned for the specified users.
     If no user properties are specified, then no properties are returned. It is, however,
     stated whether the user
     is defined in the people directory or whether the user is a virtual user.
 
Returns:List -
    A list of UserDetail objects.
    An object is returned for each user specified even when the user does not exist.
    In that case, the user is marked as not found in the people directory.
 
Throws:
ParameterNullException
StaffServiceCannotAccessVMMException
StaffServiceRuntimeException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2

- getUsersInRole
StaffResultSet getUsersInRole(java.lang.String identifier,
                            int role)
                              throws IdWrongFormatException,
                                     IdWrongTypeException,
                                     InvalidAssignmentReasonException,
                                     NotAuthorizedException,
                                     ObjectDoesNotExistException,
                                     WorkItemManagerException,
                                     UnexpectedFailureException,
                                     java.rmi.RemoteException,
                                     javax.ejb.EJBException
Retrieves the users that are members of the specified role for the
 specified task instance or template using a string representation of the task instance or template ID.
 
 The action associated to this method is TaskActions.GETROLEINFO or
 TaskTemplateActions.GETROLEINFO.
Parameters:identifier - A string representation of task instance or template ID that is used to identify the
    task instance or template.role - The role whose members are to be queried. Refer to the work item assignment
    reasons.
 
Returns:StaffResultSet -
    The users that are members of the specified role.
    Refer to StaffResultSet for more information.
 
Throws:
IdWrongFormatException
IdWrongTypeException
InvalidAssignmentReasonException
NotAuthorizedException
ObjectDoesNotExistException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.0.2
 
 Supports task templates.

- getUsersInRole
StaffResultSet getUsersInRole(TKTID tktid,
                            int role)
                              throws IdWrongFormatException,
                                     InvalidAssignmentReasonException,
                                     NotAuthorizedException,
                                     ObjectDoesNotExistException,
                                     WorkItemManagerException,
                                     UnexpectedFailureException,
                                     java.rmi.RemoteException,
                                     javax.ejb.EJBException
Retrieves the users that are members of the specified role for the
 specified task template using the task template ID.
 
 The action associated to this method is
 TaskTemplateActions.GETROLEINFO.
Parameters:tktid - The object ID of the task template that is used to identify the
    task template.role - The role whose members are to be queried, either an administrator,
    reader, or  potential instance creator. Refer to the work item assignment
    reasons.
 
Returns:StaffResultSet -
    The users that are members of the specified role.
    Refer to StaffResultSet for more information.
 
Throws:
IdWrongFormatException
InvalidAssignmentReasonException
NotAuthorizedException
ObjectDoesNotExistException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getUsersInRole
StaffResultSet getUsersInRole(TKIID tkiid,
                            int role)
                              throws IdWrongFormatException,
                                     InvalidAssignmentReasonException,
                                     NotAuthorizedException,
                                     ObjectDoesNotExistException,
                                     WorkItemManagerException,
                                     UnexpectedFailureException,
                                     java.rmi.RemoteException,
                                     javax.ejb.EJBException
Retrieves the users that are members of the specified role for the
 specified task using the task instance ID.
 
 The action associated to this method is TaskActions.GETROLEINFO.
Parameters:tkiid - The object ID of the task instance that is used to identify the
    task instance.role - The role whose members are to be queried, either an administrator,
    reader, editor, potential owner, owner, potential starter, starter, originator,
    or escalation receiver. Refer to the work item assignment
    reasons.
 
Returns:StaffResultSet -
    The users that are members of the specified role.
    Refer to StaffResultSet for more information.
 
Throws:
IdWrongFormatException
InvalidAssignmentReasonException
NotAuthorizedException
ObjectDoesNotExistException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getUserSubstitutionDetail
UserSubstitutionDetail getUserSubstitutionDetail()
                                                 throws NotAuthorizedException,
                                                        StaffServiceCannotAccessVMMException,
                                                        StaffServiceSubstitutionNotEnabledException,
                                                        StaffServiceRuntimeException,
                                                        UserDoesNotExistException,
                                                        UnexpectedFailureException,
                                                        java.rmi.RemoteException,
                                                        javax.ejb.EJBException
Retrieves absence and substitution details about the logged-on user.
 
Returns:UserSubstitutionDetail -
    The absence and substitution details of the logged-on user.
  Refer to UserSubstitutionDetail.
 
Throws:
NotAuthorizedException
StaffServiceCannotAccessVMMException
StaffServiceSubstitutionNotEnabledException
StaffServiceRuntimeException
UserDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0

- getUserSubstitutionDetail
UserSubstitutionDetail getUserSubstitutionDetail(java.lang.String userID)
                                                 throws NotAuthorizedException,
                                                        ParameterNullException,
                                                        StaffServiceCannotAccessVMMException,
                                                        StaffServiceSubstitutionNotEnabledException,
                                                        StaffServiceRuntimeException,
                                                        UserDoesNotExistException,
                                                        UnexpectedFailureException,
                                                        java.rmi.RemoteException,
                                                        javax.ejb.EJBException
Retrieves absence and substitution details about the specified user.
  
  The caller must be a task system administrator or task system monitor.
Parameters:userID - The userID that is queried.
 
Returns:UserSubstitutionDetail -
    The absence and substitution details of the specified user.
  Refer to UserSubstitutionDetail.
 
Throws:
NotAuthorizedException
ParameterNullException
StaffServiceCannotAccessVMMException
StaffServiceSubstitutionNotEnabledException
StaffServiceRuntimeException
UserDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0

- getWorkItems
WorkItem[] getWorkItems(java.lang.String identifier)
                        throws IdWrongFormatException,
                               IdWrongTypeException,
                               NotAuthorizedException,
                               ObjectDoesNotExistException,
                               WorkItemManagerException,
                               UnexpectedFailureException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
Returns the work item assignments for the logged-on user and the
  specified task or escalation instance using a string representation of the task or escalation instance ID.
  
  The task or escalation instance can be in any execution state.
  
  Note that a task system administrator is treated like any other user, that is,
  does only see the personally owned work items.
Parameters:identifier - The string representation of a task or escalation instance ID. The string is
    used to identify the object whose work item assignments are to be retrieved.
 
Returns:WorkItem[] -
    An array of work items. If there are no work items,
    an empty array is returned. Refer to WorkItem
    to view the work item properties.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2.1

- getWorkItems
WorkItem[] getWorkItems(ESIID esiid)
                        throws IdWrongFormatException,
                               NotAuthorizedException,
                               ObjectDoesNotExistException,
                               WorkItemManagerException,
                               UnexpectedFailureException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
Returns the work item assignments for the logged-on user and the
  specified escalation instance using the escalation instance ID.
  
  The escalation instance can be in any state.
  
  Note that a task system administrator is treated like any other user, that is,
  does only see the personally owned work items.
Parameters:esiid - The object ID of the escalation instance. This ID is used to identify
    the escalation whose work item assignments are to be retrieved.
 
Returns:WorkItem[] -
    An array of work items. If there are no work items,
    an empty array is returned. Refer to WorkItem
    to view the work item properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2.1

- getWorkItems
WorkItem[] getWorkItems(TKIID tkiid)
                        throws IdWrongFormatException,
                               NotAuthorizedException,
                               ObjectDoesNotExistException,
                               WorkItemManagerException,
                               UnexpectedFailureException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
Returns the work item assignments for the logged-on user and the
  specified task instance using the task instance ID.
  
  The task instance can be in any execution state.
  
  Note that a task system administrator is treated like any other user, that is,
  does only see the personally owned work items.
Parameters:tkiid - The object ID of the task instance. This ID is used to identify
    the task whose work item assignments are to be retrieved.
 
Returns:WorkItem[] -
    An array of work items. If there are no work items,
    an empty array is returned. Refer to WorkItem
    to view the work item properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2.1

- isSystemAdministrator
boolean isSystemAdministrator()
                              throws java.rmi.RemoteException,
                                     javax.ejb.EJBException
States whether the logged-on user is a system administrator
    for the Human Task Manager component.
    
    In general, authorization is granted to persons explicitly when a task template is
    defined or implicitly, for example, when a task is started.
    Above that, special authority is granted to a person playing the role of a task
    system administrator. A system administrator has all priviledges.
 
Returns:boolean -
    boolean -
   True states that the logged-on user is a task system administrator.
   False states that the logged-on user is no task system administrator.
 
Throws:
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- isSystemMonitor
boolean isSystemMonitor()
                        throws java.rmi.RemoteException,
                               javax.ejb.EJBException
States whether the logged-on user is a task system monitor
    for the Human Task Manager component.
    
    In general, authorization is granted to persons explicitly when a task template is
    defined or implicitly, for example, when a task is started.
    Above that, special authority is granted to a person playing the role of a task
    system monitor. A task system monitor has the priviledge to read all objects.
 
Returns:boolean -
    boolean -
   True states that the logged-on user is a task system monitor.
   False states that the logged-on user is no task system monitor.
 
Throws:
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- isUserInRole
boolean isUserInRole(java.lang.String identifier,
                   java.lang.String userID,
                   int role)
                     throws IdWrongFormatException,
                            IdWrongTypeException,
                            InvalidAssignmentReasonException,
                            NotAuthorizedException,
                            UserDoesNotExistException,
                            ObjectDoesNotExistException,
                            ParameterNullException,
                            UserRegistryException,
                            WorkItemManagerException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
States whether the specified user is a member of the specified role for the
   specified task instance or template using a string representation of the task instance or template ID.
 
 The action associated to this method is TaskActions.GETROLEINFO or
 TaskTemplateActions.GETROLEINFO.
Parameters:identifier - A string representation of task instance or template ID that is used to identify the
    task instance or template.userID - The user whose membership in a role is to be queried.
    
    The existence of the user ID is verified but the verification may be executed case insensitively.
    Verification can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments'
    custom property of the Human Task Manager configuration to 'true'.role - The role that the user needs to be a member of. Refer to the work item
    assignment reasons.
 
Returns:boolean -
    boolean -
    True states that the user is a member of the specified role.
    False states that the user is no member of the specified role.
 
Throws:
IdWrongFormatException
IdWrongTypeException
InvalidAssignmentReasonException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
ParameterNullException
UserRegistryException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.1
 
 Throws a UserDoesNotExistException when the specified user cannot be found.

- isUserInRole
boolean isUserInRole(TKTID tktid,
                   java.lang.String userID,
                   int role)
                     throws IdWrongFormatException,
                            InvalidAssignmentReasonException,
                            NotAuthorizedException,
                            UserDoesNotExistException,
                            ObjectDoesNotExistException,
                            ParameterNullException,
                            UserRegistryException,
                            WorkItemManagerException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
States whether the specified user is a member of the specified role for the
   specified task template using the task template ID.
 
 The action associated to this method is
 TaskTemplateActions.GETROLEINFO.
Parameters:tktid - The object ID of the task template that is used to identify the
    task template.userID - The user whose membership in a role is to be queried.
    
    The existence of the user ID is verified but the verification may be executed case insensitively.
    Verification can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments'
    custom property of the Human Task Manager configuration to 'true'.role - The role that the user needs to be a member of, either an administrator,
        reader, or  potential instance creator. Refer to the work item
    assignment reasons.
 
Returns:boolean -
    boolean -
    True states that the user is a member of the specified role.
    False states that the user is no member of the specified role.
 
Throws:
IdWrongFormatException
InvalidAssignmentReasonException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
ParameterNullException
UserRegistryException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1
 
 Throws a UserDoesNotExistException when the specified user cannot be found.

- isUserInRole
boolean isUserInRole(TKIID tkiid,
                   java.lang.String userID,
                   int role)
                     throws IdWrongFormatException,
                            InvalidAssignmentReasonException,
                            NotAuthorizedException,
                            UserDoesNotExistException,
                            ObjectDoesNotExistException,
                            ParameterNullException,
                            UserRegistryException,
                            WorkItemManagerException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
States whether the specified user is a member of the specified role for the
   specified task instance using the task instance ID.
 
 The action associated to this method is TaskActions.GETROLEINFO.
Parameters:tkiid - The object ID of the task instance that is used to identify the
    task instance.userID - The user whose membership in a role is to be queried.
    
    The existence of the user ID is verified but the verification may be executed case insensitively.
    Verification can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments'
    custom property of the Human Task Manager configuration to 'true'.role - The role that the user needs to be a member of, either an administrator,
        reader, editor, potential owner, owner, potential starter, starter, originator,
        or escalation receiver. Refer to the work item
    assignment reasons.
 
Returns:boolean -
    boolean -
    True states that the user is a member of the specified role.
    False states that the user is no member of the specified role.
 
Throws:
IdWrongFormatException
InvalidAssignmentReasonException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
ParameterNullException
UserRegistryException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.1
 
 Throws a UserDoesNotExistException when the specified user cannot be found.

- query QueryResultSet query(java.lang.String selectClause, java.lang.String whereClause, java.lang.String orderByClause, java.lang.Integer threshold, java.util.TimeZone timeZone) throws ParameterNullException , UnexpectedFailureException , WorkItemManagerException , java.rmi.RemoteException, javax.ejb.EJBException Retrieves selected object properties persistently stored in the database. You can specify a filter or a threshold to restrict the number of tuples returned. The tuples are sorted on the server according to the specified sort criteria. Sorting on the server means that the locale of the server is used. Specify the parameters of the query, the select-, where-, and order-by-clause, using SQL based on the published views. Execution of the query can thus be shifted to SQL and becomes portable and optimizable. Note, however, when you use a combination of the order-by-clause and threshold parameters, the tuples returned depend on your database system. For example, some database systems order all records and then return the requested number of tuples. Other database systems first take the requested number of tuples and then apply the order criteria. The domain of the query, that is, the SQL from-clause, is determined automatically. In principle, all properties of objects are selectable for which you own a work item or which can be transitively reached via your work item. As a rule of thumb, all objects except task templates can be reached via work items. This means that you cannot use task template properties only but that you must specify a non task template property in the select- or where-clause. Note that a task system administrator has special rights and can retrieve information on objects associated to other users. query thus returns the selected properties of all objects for which there are work items to the task systems administrator, no matter whether there is a personally owned work item or another user's work item. If the task system administrator wants to view everything that is stored on the database, independently from the existence of a work item, he/she can use queryAll. Parameters: selectClause - Describes the query result, that is, declares a list of names that identify the object properties (columns of the result) to be returned. Its syntax is an SQL select-clause. Aggregation functions like AVG, SUM, MIN, and MAX are not supported. Each comma separated part of the select-clause must specify a property from the published views - see the InfoCenter for details. To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the view name. For example, "TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE". To count the number of potentially qualifying tuples, use the COUNT keyword. For example, to count the number of task instance IDs that satisfy the where-clause, specify a select-clause such as "COUNT(DISTINCT TASK.TKIID)". If you use the more generic "COUNT(*)", then you must specify a where-clause so that the tuples to be counted can be determined. For example, to count all tasks, specify a where-clause such as "TASK.TKIID=TASK.TKIID" that always evaluates to true. The QueryResultSet contains columns in the same order as specified in the selectClause. If tuples are to be counted, an int value is returned (row 1, column 1). whereClause - The search condition to be applied to the query domain. Its syntax is an SQL where-clause. The following rules apply: If a filter is not to be applied, null must be specified. orderByClause - Sorts the query result set by the values of the columns you identify. Its syntax is an SQL order-by-clause. Each comma separated part of the order-by-clause must specify a property from the published views - see the InfoCenter for details. If you identify more that one property, the query result set is ordered by the values of the first property you identify, then by the values of the second property, and so on. If sort criteria are not to be applied, null must be specified. Note that sort criteria are applied on the server, that is, the locale of the server is used for sorting. threshold - The maximum number of query result set tuples to be returned from the server to the client. If a threshold is not to be applied, null must be specified. timeZone - The time zone of the timestamp constants in the whereClause respectively the time zone for the timestamp values returned. If a timezone is not specified, UTC is assumed. Returns: QueryResultSet - An object containing the query result. If qualifying tuples are not found, an empty query result set is returned. Refer to QueryResultSet for information on how to analyze the query result set. Throws: ParameterNullException UnexpectedFailureException WorkItemManagerException java.rmi.RemoteException javax.ejb.EJBException Since: 5.1.1

#### query

```
QueryResultSet query(java.lang.String selectClause,
                   java.lang.String whereClause,
                   java.lang.String orderByClause,
                   java.lang.Integer threshold,
                   java.util.TimeZone timeZone)
                     throws ParameterNullException,
                            UnexpectedFailureException,
                            WorkItemManagerException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
```

You can specify a filter or a threshold to restrict the number of tuples
 returned. The tuples are sorted on the server according to the specified sort criteria.
 Sorting on the server means that the locale of the server is used.
 
 Specify the parameters of the query, the select-, where-, and order-by-clause,
 using SQL based on the published views.
 Execution of the query can thus be shifted to SQL and becomes portable and optimizable.
 
 Note, however, when you use a combination of the order-by-clause and threshold
 parameters, the tuples returned depend on your database system.
 For example, some database systems order all records and then return the requested number of tuples.
 Other database systems first take the requested number of tuples and then apply the order criteria.
 
 The domain of the query, that is, the SQL from-clause, is determined automatically.
 In principle, all properties of objects are selectable for which you own a work item
 or which can be transitively reached via your work item.
 As a rule of thumb, all objects except task templates can be reached via work items.
 This means that you cannot use task template properties only but that you
 must specify a non task template property in the select- or where-clause.
 
 Note that a task system administrator has special rights and can retrieve
 information on objects associated to other users.
 query thus returns the selected properties of all objects for which there are
 work items to the task systems administrator, no matter whether there is a personally
 owned work item or another user's work item.
 If the task system administrator wants to view everything that is stored
 on the database, independently from the existence of a work item, he/she can use queryAll.

To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the
    view name. For example, "TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE".
    
    To count the number of potentially qualifying tuples, use the COUNT keyword.
    For example, to count the number of task instance IDs that satisfy the
    where-clause, specify a select-clause such as "COUNT(DISTINCT TASK.TKIID)".
    If you use the more generic "COUNT(*)", then you must specify a where-clause
    so that the tuples to be counted can be determined.
    For example, to count all tasks,
    specify a where-clause such as "TASK.TKIID=TASK.TKIID" that always evaluates to true.
    
    The QueryResultSet contains columns in the same order
    as specified in the selectClause. If tuples are to be counted, an int value is returned
    (row 1, column 1).

    - Specify object ID constants as ID('string-rep-of-oid').
    Specify timestamp constants as TS('yyyy-mm-ddThh:mm:ss') or as CURRENT\_DATE
    for comparisons with the current date.
    

    The date and time parts of a TS definition are optional; either the date or the time must
    be specified. If no date part of a TS definition is specified, the current date is taken.
    Optional time values that are not specified are set to zero.
    The timestamp is 24 hours based.
    For example, TS('16:04') is the same as TS('2002-12-24T16:04:00') provided that the
    current date is December 24th, 2002.
    

    If a date part of a TS definition is specified, the year must consist of 4 letters;
    the month and day specifications are optional.
    Missing month and day specifications are set to 01. For example, specifying
    TS('2003') is the same as specifying TS('2003-01-01T00:00:00').
    Specify binary constants as BIN('UTF-8 string').
    Use constants
    instead of integer enumerations. For example, instead of specifying a task instance state expression
    "TASK.STATE=2" , specify "TASK.STATE=TASK.STATE.STATE\_READY".
Duplicate apostrophes (') in comparising values. For example,
    "TASK\_CPROP.STRING\_VALUE='d''automatisation'".
    To specify a where clause that refers to properties of name-value pairs, like
    custom properties, add a one-digit suffix (0-9) to the view name.
    

    For example, to have only tuples returned where a task custom property "prop1" has
    the value "v1" or where a task custom property "prop2" has the value v2", the where clause
    can look like
    "TASK\_CPROP1.NAME='prop1' AND TASK\_CPROP1.STRING\_VALUE='v1' OR
    TASK\_CPROP2.NAME='prop2' AND TASK\_CPROP2.STRING\_VALUE = 'v2'".
    For performance reasons, you should not use more than one "OR" construct; use "IN" instead.
    

    For example, to retrieve the values of custom properties "prop1" and "prop2" of all task instances,
    the select clause can look like
    "DISTINCT TASK.TKIID, TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE" and the where-clause
    "TASK\_CPROP1.NAME = 'prop1' AND TASK\_CPROP2.NAME = 'prop2'".

If a filter is not to be applied, null must be specified.

If you identify more that one property, the query result set is ordered by the
    values of the first property you identify, then by the values of the second property,
    and so on.
    
    If sort criteria are not to be applied, null must be specified.
    
    Note that sort criteria are applied on the server, that is, the locale of the
    server is used for sorting.

- query QueryResultSet query(java.lang.String selectClause, java.lang.String whereClause, java.lang.String orderByClause, java.lang.Integer skipTuples, java.lang.Integer threshold, java.util.TimeZone timeZone) throws ParameterNullException , UnexpectedFailureException , WorkItemManagerException , java.rmi.RemoteException, javax.ejb.EJBException Retrieves selected object properties persistently stored in the database and allows for retrieving a specified set of data only. You can specify a filter, a starting tuple, or a threshold to restrict the number of tuples returned. The tuples are sorted on the server according to the specified sort criteria. Sorting on the server means that the locale of the server is used. Specify the parameters of the query, the select-, where-, and order-by-clause, using SQL based on the published views. Execution of the query can thus be shifted to SQL and becomes portable and optimizable. Note, however, when you use a combination of the order-by-clause, threshold, or skipTuples parameters, the tuples returned depend on your database system. For example, some database systems order all records and then return the requested number of tuples. Other database systems first take the requested number of tuples and then apply the order criteria. The domain of the query, that is, the SQL from-clause, is determined automatically. In principle, all properties of objects are selectable for which you own a work item, or which can be transitively reached via your work item. As a rule of thumb, all objects except task templates can be reached via work items. This means that you cannot use task template properties only but that you must specify a non task template property in the select- or where-clause. Note that a task system administrator has special rights and can retrieve information on objects associated to other users. query thus returns the selected properties of all objects for which there are work items to the task systems administrator, no matter whether there is a personally owned work item or another user's work item. If the task system administrator wants to view everything that is stored on the database, independently from the existence of a work item, he/she can use queryAll. Parameters: selectClause - Describes the query result, that is, declares a list of names that identify the object properties (columns of the result) to be returned. Its syntax is an SQL select-clause. Aggregation functions like AVG, SUM, MIN, and MAX are not supported. Each comma separated part of the select-clause must specify a property from the published views - see the InfoCenter for details. To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the view name. For example, "TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE". To count the number of potentially qualifying tuples, use the COUNT keyword. For example, to count the number of task instance IDs that satisfy the where-clause, specify a select-clause such as "COUNT(DISTINCT TASK.TKIID)". If you use the more generic "COUNT(*)", then you must specify a where-clause so that the tuples to be counted can be determined. For example, to count all tasks, specify a where-clause such as "TASK.TKIID=TASK.TKIID" that always evaluates to true. The QueryResultSet contains columns in the same order as specified in the selectClause. If tuples are to be counted, an int value is returned (row 1, column 1). whereClause - The search condition to be applied to the query domain. Its syntax is an SQL where-clause. The following rules apply: If a filter is not to be applied, null must be specified. orderByClause - Sorts the query result set by the values of the columns you identify. Its syntax is an SQL order-by-clause. Each comma separated part of the order-by-clause must specify a property from the published views - see the InfoCenter for details. If you identify more that one property, the query result set is ordered by the values of the first property you identify, then by the values of the second property, and so on. If sort criteria are not to be applied, null must be specified. Note that sort criteria are applied on the server, that is, the locale of the server is used for sorting. skipTuples - The number of query result set tuples to be ignored and not to be returned to the caller. For example, a value of '5' means that the first 5 qualifying tuples are not returned. Use this parameter together with the threshold to implement paging in your client application. If all qualifying tuples are to be returned, null or 0 must be specified. threshold - The maximum number of query result set tuples to be returned from the server to the client. If a threshold is not to be applied, null must be specified. timeZone - The time zone of the timestamp constants in the whereClause respectively the time zone for the timestamp values returned. If a timezone is not specified, UTC is assumed. Returns: QueryResultSet - An object containing the query result. If qualifying tuples are not found, an empty query result set is returned. Refer to QueryResultSet for information on how to analyze the query result set. Throws: ParameterNullException UnexpectedFailureException WorkItemManagerException java.rmi.RemoteException javax.ejb.EJBException Since: 6.0

#### query

```
QueryResultSet query(java.lang.String selectClause,
                   java.lang.String whereClause,
                   java.lang.String orderByClause,
                   java.lang.Integer skipTuples,
                   java.lang.Integer threshold,
                   java.util.TimeZone timeZone)
                     throws ParameterNullException,
                            UnexpectedFailureException,
                            WorkItemManagerException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
```

You can specify a filter, a starting tuple, or a threshold to restrict the number of tuples
 returned. The tuples are sorted on the server according to the specified sort criteria.
 Sorting on the server means that the locale of the server is used.
 
 Specify the parameters of the query, the select-, where-, and order-by-clause,
 using SQL based on the published views.
 Execution of the query can thus be shifted to SQL and becomes portable and optimizable.
 
 Note, however, when you use a combination of the order-by-clause, threshold, or skipTuples
 parameters, the tuples returned depend on your database system.
 For example, some database systems order all records and then return the requested number of tuples.
 Other database systems first take the requested number of tuples and then apply the order criteria.
 
 The domain of the query, that is, the SQL from-clause, is determined automatically.
 In principle, all properties of objects are selectable for which you own a work item,
 or which can be transitively reached via your work item.
 As a rule of thumb, all objects except task templates can be reached via work items.
 This means that you cannot use task template properties only but that you
 must specify a non task template property in the select- or where-clause.
 
 Note that a task system administrator has special rights and can retrieve
 information on objects associated to other users.
 query thus returns the selected properties of all objects for which there are
 work items to the task systems administrator, no matter whether there is a personally
 owned work item or another user's work item.
 If the task system administrator wants to view everything that is stored
 on the database, independently from the existence of a work item, he/she can use queryAll.

To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the
    view name. For example, "TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE".
    
    To count the number of potentially qualifying tuples, use the COUNT keyword.
    For example, to count the number of task instance IDs that satisfy the
    where-clause, specify a select-clause such as "COUNT(DISTINCT TASK.TKIID)".
    If you use the more generic "COUNT(*)", then you must specify a where-clause
    so that the tuples to be counted can be determined.
    For example, to count all tasks,
    specify a where-clause such as "TASK.TKIID=TASK.TKIID" that always evaluates to true.
    
    The QueryResultSet contains columns in the same order
    as specified in the selectClause. If tuples are to be counted, an int value is returned
    (row 1, column 1).

    - Specify object ID constants as ID('string-rep-of-oid').
    Specify timestamp constants as TS('yyyy-mm-ddThh:mm:ss') or as CURRENT\_DATE
    for comparisons with the current date.
    

    The date and time parts of a TS definition are optional; either the date or the time must
    be specified. If no date part of a TS definition is specified, the current date is taken.
    Optional time values that are not specified are set to zero.
    The timestamp is 24 hours based.
    For example, TS('16:04') is the same as TS('2002-12-24T16:04:00') provided that the
    current date is December 24th, 2002.
    

    If a date part of a TS definition is specified, the year must consist of 4 letters;
    the month and day specifications are optional.
    Missing month and day specifications are set to 01. For example, specifying
    TS('2003') is the same as specifying TS('2003-01-01T00:00:00').
    Specify binary constants as BIN('UTF-8 string').
    Use constants
    instead of integer enumerations. For example, instead of specifying a task instance state expression
    "TASK.STATE=2" , specify "TASK.STATE=TASK.STATE.STATE\_READY".
Duplicate apostrophes (') in comparising values. For example,
    "TASK\_CPROP.STRING\_VALUE='d''automatisation'".
    To specify a where clause that refers to properties of name-value pairs, like
    custom properties, add a one-digit suffix (0-9) to the view name.
    

    For example, to have only tuples returned where a task custom property "prop1" has
    the value "v1" or where a task custom property "prop2" has the value v2", the where clause
    can look like
    "TASK\_CPROP1.NAME='prop1' AND TASK\_CPROP1.STRING\_VALUE='v1' OR
    TASK\_CPROP2.NAME='prop2' AND TASK\_CPROP2.STRING\_VALUE = 'v2'".
    For performance reasons, you should not use more than one "OR" construct; use "IN" instead.
    

    For example, to retrieve the values of custom properties "prop1" and "prop2" of all task instances,
    the select clause can look like
    "DISTINCT TASK.TKIID, TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE" and the where-clause
    "TASK\_CPROP1.NAME = 'prop1' AND TASK\_CPROP2.NAME = 'prop2'".

If a filter is not to be applied, null must be specified.

If you identify more that one property, the query result set is ordered by the
    values of the first property you identify, then by the values of the second property,
    and so on.
    
    If sort criteria are not to be applied, null must be specified.
    
    Note that sort criteria are applied on the server, that is, the locale of the
    server is used for sorting.

If all qualifying tuples are to be returned, null or 0 must be specified.

- query
QueryResultSet query(java.lang.String storedQueryName,
                   java.lang.Integer skipTuples)
                     throws IdWrongFormatException,
                            ObjectDoesNotExistException,
                            ParameterNullException,
                            QueryCannotJoinException,
                            QueryInvalidOperandException,
                            QueryInvalidTimestampException,
                            QueryUndefinedParameterException,
                            QueryUnknownColumnException,
                            QueryUnknownOperatorException,
                            QueryUnknownTableException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Deprecated. As of version 6.0.2, replaced by query(Sting storedQueryName, Integer skipTuples, List parameters),
Performs the specified stored query and returns the qualifying object properties.
 If a private stored query with the specified name
 exists for the calling user, then the private stored query is performed; otherwise
 the public stored query with the specified name.
 
 Only properties of objects are returned for which the logged-on user has a work item.
 Note that a task system administrator has special rights and can retrieve
 information on objects associated to other users.
 query thus returns the selected properties of all objects for which there are
 work items to the task systems administrator, no matter whether there is a personally
 owned work item or another user's work item.
 
 Refer to createStoredQuery for
 the creation of stored queries.
Parameters:storedQueryName - The name of the stored query to be executed -
    refer to getStoredQueryNames
    for the retrieval of existing stored query names.skipTuples - The number of query result set tuples to be ignored and not to be
    returned to the caller. For example, a value of '5' means that the first 5
    qualifying tuples are not returned. Use this parameter together with the threshold
    of the stored query definition to implement paging in your client application.
    
    If all qualifying tuples are to be returned, null or 0 must be specified.
 
Returns:QueryResultSet -
    QueryResultSet -
    The qualifying object properties. If
    qualifying objects are not found, an empty query result set is returned. Refer
    to QueryResultSet
    for information on how to analyze the query result set.
 
Throws:
IdWrongFormatException
ObjectDoesNotExistException
ParameterNullException
QueryCannotJoinException
QueryInvalidOperandException
QueryInvalidTimestampException
QueryUndefinedParameterException
QueryUnknownColumnException
QueryUnknownOperatorException
QueryUnknownTableException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.0.2
 
 Supports private stored queries.
 
6.1
 
 Throws a QueryCannotJoinException when views that are used cannot be joined.

- query
QueryResultSet query(java.lang.String storedQueryName,
                   java.lang.Integer skipTuples,
                   java.util.List parameters)
                     throws IdWrongFormatException,
                            InvalidStoredQueryParametersException,
                            ObjectDoesNotExistException,
                            ParameterNullException,
                            QueryCannotJoinException,
                            QueryInvalidOperandException,
                            QueryInvalidTimestampException,
                            QueryUndefinedParameterException,
                            QueryUnknownColumnException,
                            QueryUnknownOperatorException,
                            QueryUnknownTableException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Performs the specified stored query, specifies values for the parameters in the
 where-clause, and returns the qualifying object properties.
 If a private stored query with the specified name
 exists for the calling user, then the private stored query is performed; otherwise
 the public stored query with the specified name.
 
 Only properties of objects are returned for which the logged-on user has a work item.
 Note that a task system administrator has special rights and can retrieve
 information on objects associated to other users.
 query thus returns the selected properties of all objects for which there are
 work items to the task systems administrator, no matter whether there is a personally
 owned work item or another user's work item.
 
 Refer to createStoredQuery for
 the creation of stored queries.
Parameters:storedQueryName - The name of the stored query to be executed -
    refer to getStoredQueryNames
    for the retrieval of existing stored query names.skipTuples - The number of query result set tuples to be ignored and not to be
    returned to the caller. For example, a value of '5' means that the first 5
    qualifying tuples are not returned. Use this parameter together with the threshold
    of the stored query definition to implement paging in your client application.
    
    If all qualifying tuples are to be returned, null or 0 must be specified.parameters - A list of string values to replace parameters in the where-clause. There must
    be a value for each parameter in the where-clause. The first string replaces all occurrences of @param1,
    the second string replaces all occurrences of @param2, and so on.
 
Returns:QueryResultSet -
    QueryResultSet -
    The qualifying object properties. If
    qualifying objects are not found, an empty query result set is returned. Refer
    to QueryResultSet
    for information on how to analyze the query result set.
 
Throws:
IdWrongFormatException
InvalidStoredQueryParametersException
ObjectDoesNotExistException
ParameterNullException
QueryCannotJoinException
QueryInvalidOperandException
QueryInvalidTimestampException
QueryUndefinedParameterException
QueryUnknownColumnException
QueryUnknownOperatorException
QueryUnknownTableException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1
 
 Throws a QueryCannotJoinException when views that are used cannot be joined.

- query
QueryResultSet query(java.lang.String storedQueryName,
                   java.lang.Integer skipTuples,
                   java.lang.Integer threshold)
                     throws IdWrongFormatException,
                            ObjectDoesNotExistException,
                            ParameterNullException,
                            QueryCannotJoinException,
                            QueryInvalidOperandException,
                            QueryInvalidTimestampException,
                            QueryUndefinedParameterException,
                            QueryUnknownColumnException,
                            QueryUnknownOperatorException,
                            QueryUnknownTableException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Deprecated. As of version 6.0.2, replaced by query(Sting storedQueryName, Integer skipTuples, Integer threshold, List parameters),
Performs the specified stored query and returns the properties of objects
 in the specified range.
 If a private stored query with the specified name
 exists for the calling user, then the private stored query is performed; otherwise
 the public stored query with the specified name.
 
 Only properties of objects are returned for which the logged-on user has a work item.
 Note that a task system administrator has special rights and can retrieve
 information on objects associated to other users.
 query thus returns the selected properties of all objects for which there are
 work items to the task systems administrator, no matter whether there is a personally
 owned work item or another user's work item.
 
 Refer to createStoredQuery for
 the creation of stored queries.
Parameters:storedQueryName - The name of the stored query to be executed -
    refer to getStoredQueryNames
    for the retrieval of existing stored query names.skipTuples - The number of query result set tuples to be ignored and not to be
    returned to the caller. For example, a value of '5' means that the first 5
    qualifying tuples are not returned. Use this parameter together with the threshold
    to implement paging in your client application.
    
    If all qualifying tuples are to be returned, null or 0 must be specified.threshold - The maximum number of result set tuples to be returned from the
    server to the client.
    If the threshold is to be taken from the stored query definition, specify null or use the
    query method
    that does not request a threshold parameter.
 
Returns:QueryResultSet -
    QueryResultSet -
    The qualifying object properties. If
    qualifying objects are not found, an empty query result set is returned. Refer
    to QueryResultSet
    for information on how to analyze the query result set.
 
Throws:
IdWrongFormatException
ObjectDoesNotExistException
ParameterNullException
QueryCannotJoinException
QueryInvalidOperandException
QueryInvalidTimestampException
QueryUndefinedParameterException
QueryUnknownColumnException
QueryUnknownOperatorException
QueryUnknownTableException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.1
 
Change History

Release
 Modification
 
6.0.2
 
 Supports private stored queries.
 
6.1
 
 Throws a QueryCannotJoinException when views that are used cannot be joined.

- query
QueryResultSet query(java.lang.String storedQueryName,
                   java.lang.Integer skipTuples,
                   java.lang.Integer threshold,
                   java.util.List parameters)
                     throws IdWrongFormatException,
                            InvalidStoredQueryParametersException,
                            ObjectDoesNotExistException,
                            ParameterNullException,
                            QueryCannotJoinException,
                            QueryInvalidOperandException,
                            QueryInvalidTimestampException,
                            QueryUndefinedParameterException,
                            QueryUnknownColumnException,
                            QueryUnknownOperatorException,
                            QueryUnknownTableException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Performs the specified stored query and specifies values for parameters in the where-clause.
 
 If a private stored query with the specified name
 exists for the calling user, then the private stored query is performed; otherwise
 the public stored query with the specified name.
 
 Only properties of objects are returned for which the logged-on user has a work item.
 Note that a task system administrator has special rights and can retrieve
 information on objects associated to other users.
 query thus returns the selected properties of all objects for which there are
 work items to the task systems administrator, no matter whether there is a personally
 owned work item or another user's work item.
 
 Refer to createStoredQuery for
 the creation of stored queries.
Parameters:storedQueryName - The name of the stored query to be executed -
    refer to getStoredQueryNames
    for the retrieval of existing stored query names.skipTuples - The number of query result set tuples to be ignored and not to be
    returned to the caller. For example, a value of '5' means that the first 5
    qualifying tuples are not returned. Use this parameter together with the threshold
    to implement paging in your client application.
    
    If all qualifying tuples are to be returned, null or 0 must be specified.threshold - The maximum number of result set tuples to be returned from the
    server to the client.
    If the threshold is to be taken from the stored query definition, specify null or use the
    query method
    that does not request a threshold parameter.parameters - A list of string values to replace parameters in the where-clause. There must
    be a value for each parameter in the where-clause. The first string replaces all occurrences of @param1,
    the second string replaces all occurrences of @param2, and so on.
 
Returns:QueryResultSet -
    QueryResultSet -
    The qualifying object properties. If
    qualifying objects are not found, an empty query result set is returned. Refer
    to QueryResultSet
    for information on how to analyze the query result set.
 
Throws:
IdWrongFormatException
InvalidStoredQueryParametersException
ObjectDoesNotExistException
ParameterNullException
QueryCannotJoinException
QueryInvalidOperandException
QueryInvalidTimestampException
QueryUndefinedParameterException
QueryUnknownColumnException
QueryUnknownOperatorException
QueryUnknownTableException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1
 
 Throws a QueryCannotJoinException when views that are used cannot be joined.

- query
QueryResultSet query(java.lang.String userID,
                   java.lang.String storedQueryName,
                   java.lang.Integer skipTuples,
                   java.lang.Integer threshold,
                   java.util.List parameters)
                     throws IdWrongFormatException,
                            InvalidStoredQueryParametersException,
                            NotAuthorizedException,
                            ObjectDoesNotExistException,
                            ParameterNullException,
                            QueryCannotJoinException,
                            QueryInvalidOperandException,
                            QueryInvalidTimestampException,
                            QueryUndefinedParameterException,
                            QueryUnknownColumnException,
                            QueryUnknownOperatorException,
                            QueryUnknownTableException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Performs the specified private stored query of the specified user.
 
 Only properties of objects are returned for which the logged-on user has a work item.
 Note that a task system administrator has special rights and can retrieve
 information on objects associated to other users.
 query thus returns the selected properties of all objects for which there are
 work items to the task systems administrator, no matter whether there is a personally
 owned work item or another user's work item.
 
 Refer to createStoredQuery for
 the creation of stored queries.
Parameters:userID - The name of the user who is the owner of the stored query.storedQueryName - The name of the stored query to be executed -
    refer to getStoredQueryNames
    for the retrieval of existing stored query names.skipTuples - The number of query result set tuples to be ignored and not to be
    returned to the caller. For example, a value of '5' means that the first 5
    qualifying tuples are not returned. Use this parameter together with the threshold
    to implement paging in your client application.
    
    If all qualifying tuples are to be returned, null or 0 must be specified.threshold - The maximum number of result set tuples to be returned from the
    server to the client.
    If the threshold is to be taken from the stored query definition, specify null or use the
    query method
    that does not request a threshold parameter.parameters - A list of string values to replace parameters in the where-clause. There must
    be a value for each parameter in the where-clause. The first string replaces all occurrences of @param1,
    the second string replaces all occurrences of @param2, and so on.
 
Returns:QueryResultSet -
    QueryResultSet -
    The qualifying object properties. If
    qualifying objects are not found, an empty query result set is returned. Refer
    to QueryResultSet
    for information on how to analyze the query result set.
 
Throws:
IdWrongFormatException
InvalidStoredQueryParametersException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
QueryCannotJoinException
QueryInvalidOperandException
QueryInvalidTimestampException
QueryUndefinedParameterException
QueryUnknownColumnException
QueryUnknownOperatorException
QueryUnknownTableException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1
 
 Throws a QueryCannotJoinException when views that are used cannot be joined.

- query
QueryResultSet query(int kind,
                   java.lang.String storedQueryName,
                   java.lang.Integer skipTuples,
                   java.lang.Integer threshold,
                   java.util.List parameters)
                     throws IdWrongFormatException,
                            InvalidParameterException,
                            InvalidStoredQueryParametersException,
                            ObjectDoesNotExistException,
                            ParameterNullException,
                            QueryCannotJoinException,
                            QueryInvalidOperandException,
                            QueryInvalidTimestampException,
                            QueryUndefinedParameterException,
                            QueryUnknownColumnException,
                            QueryUnknownOperatorException,
                            QueryUnknownTableException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Performs the specified public or private stored query.
 
 Only properties of objects are returned for which the logged-on user has a work item.
 Note that a task system administrator has special rights and can retrieve
 information on objects associated to other users.
 query thus returns the selected properties of all objects for which there are
 work items to the task systems administrator, no matter whether there is a personally
 owned work item or another user's work item.
 
 Refer to createStoredQuery for
 the creation of stored queries.
Parameters:kind - An indicator to specify whether a private or public stored query is to be used.
 
    KIND\_PUBLIC states that a public stored query is to be used.
    KIND\_PRIVATE states that a private stored query for the logged-on user is to be used.storedQueryName - The name of the stored query to be executed -
    refer to getStoredQueryNames
    for the retrieval of existing stored query names.skipTuples - The number of query result set tuples to be ignored and not to be
    returned to the caller. For example, a value of '5' means that the first 5
    qualifying tuples are not returned. Use this parameter together with the threshold
    to implement paging in your client application.
    
    If all qualifying tuples are to be returned, null or 0 must be specified.threshold - The maximum number of result set tuples to be returned from the
    server to the client.
    If the threshold is to be taken from the stored query definition, specify null or use the
    query method
    that does not request a threshold parameter.parameters - A list of string values to replace parameters in the where-clause. There must
    be a value for each parameter in the where-clause. The first string replaces all occurrences of @param1,
    the second string replaces all occurrences of @param2, and so on.
 
Returns:QueryResultSet -
    QueryResultSet -
    The qualifying object properties. If
    qualifying objects are not found, an empty query result set is returned. Refer
    to QueryResultSet
    for information on how to analyze the query result set.
 
Throws:
IdWrongFormatException
InvalidParameterException
InvalidStoredQueryParametersException
ObjectDoesNotExistException
ParameterNullException
QueryCannotJoinException
QueryInvalidOperandException
QueryInvalidTimestampException
QueryUndefinedParameterException
QueryUnknownColumnException
QueryUnknownOperatorException
QueryUnknownTableException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1
 
 Throws a QueryCannotJoinException when views that are used cannot be joined.

- queryAll QueryResultSet queryAll(java.lang.String selectClause, java.lang.String whereClause, java.lang.String orderByClause, java.lang.Integer skipTuples, java.lang.Integer threshold, java.util.TimeZone timeZone) throws NotAuthorizedException , ParameterNullException , UnexpectedFailureException , WorkItemManagerException , java.rmi.RemoteException, javax.ejb.EJBException Retrieves selected object properties of all objects persistently stored in the database and allows for retrieving a specified set of data only. You can specify a filter, a starting tuple, or a threshold to restrict the number of tuples returned. The tuples are sorted on the server according to the specified sort criteria. Sorting on the server means that the locale of the server is used. Specify the parameters of the query, the select-, where-, and order-by-clause, using SQL based on the published views. Execution of the query can thus be shifted to SQL and becomes portable and optimizable. Note, however, when you use a combination of the order-by-clause, threshold, or skipTuples parameters, the tuples returned depend on your database system. For example, some database systems order all records and then return the requested number of tuples. Other database systems first take the requested number of tuples and then apply the order criteria. The domain of the query, that is, the SQL from-clause, is determined automatically. The caller must be a task system administrator or monitor. Parameters: selectClause - Describes the query result, that is, represents a list of names that identify the object properties (columns of the result) to be returned. Its syntax is an SQL select-clause. Aggregation functions like AVG, SUM, MIN, and MAX are not supported. Each comma separated part of the select-clause must specify a property from the published views - see the InfoCenter for details. To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the view name. For example, "TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE". To count the number of potentially qualifying tuples, use the COUNT keyword. For example, to count the number of task instance IDs that satisfy the where-clause, specify a select-clause such as "COUNT(DISTINCT TASK.TKIID)". If you use the more generic "COUNT(*)", then you must specify a where-clause so that the tuples to be counted can be determined. For example, to count all tasks, specify a where-clause such as "TASK.TKIID=TASK.TKIID" that always evaluates to true. The QueryResultSet contains columns in the same order as specified in the selectClause. If tuples are to be counted, an int value is returned (row 1, column 1). whereClause - The search condition to be applied to the query domain. Its syntax is an SQL where-clause. The following rules apply: If a filter is not to be applied, null must be specified. orderByClause - Sorts the query result set by the values of the columns you identify. Its syntax is an SQL order-by-clause. Each comma separated part of the order-by-clause must specify a property from the published views - see the InfoCenter for details. If you identify more that one property, the query result set is ordered by the values of the first property you identify, then by the values of the second property, and so on. If sort criteria are not to be applied, null must be specified. Note that sort criteria are applied on the server, that is, the locale of the server is used for sorting. skipTuples - The number of query result set tuples to be ignored and not to be returned to the caller. For example, a value of '5' means that the first 5 qualifying tuples are not returned. Use this parameter together with the threshold to implement paging in your client application. If all qualifying tuples are to be returned, null or 0 must be specified. threshold - The maximum number of query result set tuples to be returned. If a threshold is not to be applied, null must be specified. timeZone - The time zone of the timestamp constants in the whereClause respectively the time zone for the timestamp values returned. If a timezone is not specified, UTC is assumed. Returns: QueryResultSet - An object containing the query result. If qualifying tuples are not found, an empty query result set is returned. Refer to QueryResultSet for information on how to analyze the query result set. Throws: NotAuthorizedException ParameterNullException UnexpectedFailureException WorkItemManagerException java.rmi.RemoteException javax.ejb.EJBException Since: 6.0

#### queryAll

```
QueryResultSet queryAll(java.lang.String selectClause,
                      java.lang.String whereClause,
                      java.lang.String orderByClause,
                      java.lang.Integer skipTuples,
                      java.lang.Integer threshold,
                      java.util.TimeZone timeZone)
                        throws NotAuthorizedException,
                               ParameterNullException,
                               UnexpectedFailureException,
                               WorkItemManagerException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
```

You can specify a filter, a starting tuple, or a threshold to restrict the number of tuples
 returned. The tuples are sorted on the server according to the specified sort criteria.
 Sorting on the server means that the locale of the server is used.
 
 Specify the parameters of the query, the select-, where-, and order-by-clause,
 using SQL based on the published views.
 Execution of the query can thus be shifted to SQL and becomes portable and optimizable.
 
 Note, however, when you use a combination of the order-by-clause, threshold, or skipTuples
 parameters, the tuples returned depend on your database system.
 For example, some database systems order all records and then return the requested number of tuples.
 Other database systems first take the requested number of tuples and then apply the order criteria.
 
 The domain of the query, that is, the SQL from-clause, is determined automatically.
 
 The caller must be a task system administrator or monitor.

To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the
    view name. For example, "TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE".
    
    To count the number of potentially qualifying tuples, use the COUNT keyword.
    For example, to count the number of task instance IDs that satisfy the
    where-clause, specify a select-clause such as "COUNT(DISTINCT TASK.TKIID)".
    If you use the more generic "COUNT(*)", then you must specify a where-clause
    so that the tuples to be counted can be determined.
    For example, to count all tasks,
    specify a where-clause such as "TASK.TKIID=TASK.TKIID" that always evaluates to true.
    
    The QueryResultSet contains columns in the same order
    as specified in the selectClause. If tuples are to be counted, an int value is returned
    (row 1, column 1).

    - Specify object ID constants as ID('string-rep-of-oid').
    Specify timestamp constants as TS('yyyy-mm-ddThh:mm:ss') or as CURRENT\_DATE
    for comparisons with the current date.
    

    The date and time parts of a TS definition are optional; either the date or the time must
    be specified. If no date part of a TS definition is specified, the current date is taken.
    Optional time values that are not specified are set to zero.
    The timestamp is 24 hours based.
    For example, TS('16:04') is the same as TS('2002-12-24T16:04:00') provided that the
    current date is December 24th, 2002.
    

    If a date part of a TS definition is specified, the year must consist of 4 letters;
    the month and day specifications are optional.
    Missing month and day specifications are set to 01. For example, specifying
    TS('2003') is the same as specifying TS('2003-01-01T00:00:00').
    Specify binary constants as BIN('UTF-8 string').
    Use constants
    instead of integer enumerations. For example, instead of specifying a task instance state expression
    "TASK.STATE=2" , specify "TASK.STATE=TASK.STATE.STATE\_READY".
Duplicate apostrophes (') in comparising values. For example,
    "TASK\_CPROP.STRING\_VALUE='d''automatisation'".
    To specify a where clause that refers to properties of name-value pairs, like
    custom properties, add a one-digit suffix (0-9) to the view name.
    

    For example, to have only tuples returned where a task custom property "prop1" has
    the value "v1" or where a task custom property "prop2" has the value v2", the where clause
    can look like
    "TASK\_CPROP1.NAME='prop1' AND TASK\_CPROP1.STRING\_VALUE='v1' OR
    TASK\_CPROP2.NAME='prop2' AND TASK\_CPROP2.STRING\_VALUE = 'v2'".
    For performance reasons, you should not use more than one "OR" construct; use "IN" instead.
    

    For example, to retrieve the values of custom properties "prop1" and "prop2" of all task instances,
    the select clause can look like
    "DISTINCT TASK.TKIID, TASK\_CPROP1.STRING\_VALUE, TASK\_CPROP2.STRING\_VALUE" and the where-clause
    "TASK\_CPROP1.NAME = 'prop1' AND TASK\_CPROP2.NAME = 'prop2'".

If a filter is not to be applied, null must be specified.

If you identify more that one property, the query result set is ordered by the
    values of the first property you identify, then by the values of the second property,
    and so on.
    
    If sort criteria are not to be applied, null must be specified.
    
    Note that sort criteria are applied on the server, that is, the locale of the
    server is used for sorting.

If all qualifying tuples are to be returned, null or 0 must be specified.

- queryTaskTemplates TaskTemplate [] queryTaskTemplates(java.lang.String whereClause, java.lang.String orderByClause, java.lang.Integer threshold, java.util.TimeZone timeZone) throws IdWrongFormatException , QueryCannotJoinException , QueryInvalidOperandException , QueryInvalidTimestampException , QueryUndefinedParameterException , QueryUnknownColumnException , QueryUnknownOperatorException , QueryUnknownTableException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Retrieves task templates that are persistently stored in the database. If the HumanTaskManager is running in archive mode, then all qualifying task templates are returned. If the HumanTaskManager is not running in archive mode, then qualifying task templates that are part of started applications are returned. You can specify a threshold or filter to restrict the number of task templates returned. If the number of task templates is not restricted, all task templates that qualify are returned. Note that all versions of a task template are returned unless you filter for their valid-from times. The task templates are sorted on the server according to the specified sort criteria. Sorting on the server means that the locale of the server is used. The parameters of the query, the where- and order-by-clause, are specified using SQL based on the TASK\_TEMPLATE view. Execution of the query can thus be shifted to SQL and becomes portable and customizable. Note, however, when you use a combination of the order-by-clause and threshold parameters, the tuples returned depend on your database system. For example, some database systems order all records and then return the requested number of tuples. Other database systems first take the requested number of tuples and then apply the order criteria. Parameters: whereClause - The search condition to be applied to the set of available task templates. Its syntax is an SQL where-clause. The following rules apply: If a filter is not to be applied, null must be specified. orderByClause - Sorts the qualifying task templates by the values of the columns you identify. Its syntax is an SQL order-by-clause. Each comma separated part of the order-by-clause must specify a property from the TASK\_TEMPL view - see the InfoCenter for details. If you identify more that one property, the task templates are ordered by the values of the first property you identify, then by the values of the second property, and so on. If sort criteria are not to be applied, null must be specified. Note that sort criteria are applied on the server, that is, the locale of the server is used for sorting. threshold - The maximum number of task templates to be returned. If a threshold is not to be applied, null must be specified. timeZone - The time zone of the timestamp constants in the whereClause respectively the time zone for the timestamp values returned. If a timezone is not specified, UTC is assumed. Returns: TaskTemplate[] - An array of qualifying task templates. If no templates qualify, an empty array is returned. Refer to TaskTemplate to view the task template properties. Throws: IdWrongFormatException QueryCannotJoinException QueryInvalidOperandException QueryInvalidTimestampException QueryUndefinedParameterException QueryUnknownColumnException QueryUnknownOperatorException QueryUnknownTableException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.0 Change History Release Modification 6.1 Throws a QueryCannotJoinException when views that are used cannot be joined.

#### queryTaskTemplates

```
TaskTemplate[] queryTaskTemplates(java.lang.String whereClause,
                                java.lang.String orderByClause,
                                java.lang.Integer threshold,
                                java.util.TimeZone timeZone)
                                  throws IdWrongFormatException,
                                         QueryCannotJoinException,
                                         QueryInvalidOperandException,
                                         QueryInvalidTimestampException,
                                         QueryUndefinedParameterException,
                                         QueryUnknownColumnException,
                                         QueryUnknownOperatorException,
                                         QueryUnknownTableException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
```

You can specify a threshold or filter to restrict the number of task templates returned.
 If the number of task templates is not restricted, all task templates that qualify
 are returned. Note that
 all versions of a task template are returned unless you filter for their valid-from times.
 The task templates are sorted on the server according to the specified sort criteria.
 Sorting on the server means that the locale of the server is used.
 
 The parameters of the query, the where- and order-by-clause, are specified using SQL
 based on the TASK\_TEMPLATE view. Execution of the query can thus be shifted to SQL and
 becomes portable and customizable.
 
 Note, however, when you use a combination of the order-by-clause and threshold
 parameters, the tuples returned depend on your database system.
 For example, some database systems order all records and then return the requested number of tuples.
 Other database systems first take the requested number of tuples and then apply the order criteria.

    - Specify object ID constants as ID('string-rep-of-oid').
    Specify timestamp constants as TS('yyyy-mm-ddThh:mm:ss') or as CURRENT\_DATE
    for comparisons with the current date.
    

    The date and time parts of a TS definition are optional; either the date or the time must
    be specified. If no date part of a TS definition is specified, the current date is taken.
    Optional time values that are not specified are set to zero.
    The timestamp is 24 hours based.
    For example, TS('16:04') is the same as TS('2002-12-24T16:04:00') provided that the
    current date is December 24th, 2002.
    

    If a date part of a TS definition is specified, the year must consist of 4 letters;
    the month and day specifications are optional.
    Missing month and day specifications are set to 01. For example, specifying
    TS('2003') is the same as specifying TS('2003-01-01T00:00:00').
    Specify binary constants as BIN('UTF-8 string').
    Use constants
    instead of integer enumerations. For example, instead of specifying a task tempalte state expression
    "TASK\_TEMPL.STATE=2" , specify "TASK\_TEMPL.STATE=TASK\_TEMPL.STATE.STATE\_STOPPED".
Duplicate apostrophes (') in comparising values. For example,
    "TASK\_CPROP.STRING\_VALUE='d''automatisation'".

If a filter is not to be applied, null must be specified.

If you identify more that one property, the task templates are ordered by the
    values of the first property you identify, then by the values of the second property,
    and so on.
    
    If sort criteria are not to be applied, null must be specified.
    
    Note that sort criteria are applied on the server, that is, the locale of the
    server is used for sorting.

Change History

Release
 Modification
 
6.1
 
 Throws a QueryCannotJoinException when views that are used cannot be joined.

- resolveStaffQuery
StaffResultSet resolveStaffQuery(java.lang.String parameterizedPeopleAssignmentCriteria,
                               java.lang.String jndiNameOfStaffPluginProvider,
                               int substitutionPolicy,
                               java.util.Map contextVariables)
                                 throws InvalidParameterException,
                                        ParameterNullException,
                                        StaffServiceRuntimeException,
                                        UnexpectedFailureException,
                                        java.rmi.RemoteException,
                                        javax.ejb.EJBException
Tentatively resolves the specified people assignment criteria and returns the qualifying users or groups.
 
 Note that any exception thrown does not cause a database rollback because a database update
 is not involved in this call.
Parameters:parameterizedPeopleAssignmentCriteria - The parameterized people assignment criteria to be resolved.
    These are the criteria as specified in the TEL.jndiNameOfStaffPluginProvider - The JNDI name of the people directory configuration to be used.substitutionPolicy - The substitution policy to be applied. Refer to
    SubstitutionPolicy for valid specifications. Note that
    a substitution policy can only be applied if the Virtual Memory Management (VMM)
    people directory configuration is used.contextVariables - An optional map of context variable names and their values.
    Context variables allow for context-sensitive queries so that even static people assignment queries
    show dynamic behavior. Context variable names are, for example,
    wf:process.starter or wf:process.administrators.
    
    The value of a context variable is a string or an array of strings. Note that there
    can only be a single array with more than one value.
 
Returns:StaffResultSet -
    The users that qualify when the specified people assignment criteria are resolved.
    Refer to StaffResultSet for more information.
 
Throws:
InvalidParameterException
ParameterNullException
StaffServiceRuntimeException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- restart void restart(java.lang.String tkiid, ClientObjectWrapper input, boolean keepResultMessages) throws AdministratorCannotBeResolvedException , ApplicationVetoException , ArchiveUnsupportedOperationException , CannotCreateWorkItemException , IdWrongFormatException , IdWrongTypeException , InvalidApplicationStateException , InvalidLengthException , NotAuthorizedException , UserDoesNotExistException , ObjectDoesNotExistException , ParallelRoutingTaskException , SCAServiceAccessFailureException , SCAServiceResultErrorException , SchedulingFailedException , WrongKindException , WrongMessageTypeException , WrongStateException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Restarts the specified task instance using a string representation of the task instance ID. The task instance can be a collaboration, invocation, or to-do task. The task instance can be in any state but inactive. Additionally, The task instance can be escalated, suspended, or waiting for subtasks. The caller must be the originator or an administrator of the task instance. Note that collaboration, invocation, and to-do tasks are also known as human, originating, and participating tasks. Restarting the task instance causes staff resolution to be newly performed and all timers to be reset. If you used the update method to change timer durations, then timers are set up according to these values. If you used the update method to explicitely set a scheduler time, then the corresponding durations are not calculated. Timers are not set up. For inline to-do tasks, expiration is not recalculated. Any subtasks or follow-on tasks are deleted. Any escalations are cancelled and reset into the inactive state. For invocation tasks, the logged-on user becomes the starter of the restarted task instance. The action associated to this method is TaskActions.RESTARTTASK . This method is not supported in archive mode. Parameters: tkiid - A string representation of the task instance ID that is used to identify the task instance. input - The input message. If no input message is provided, the original input message is used. Note that, for inline to-do tasks, the input message is not synchronized with the Business Flow Manager staff activity. The object wrapped by the ClientObjectWrapper must be serializable. keepResultMessages - Specifies whether output or fault messages are to be kept. True states that any output or fault message set is to be kept. False states that any output or fault message set is to be deleted. Throws: AdministratorCannotBeResolvedException ApplicationVetoException ArchiveUnsupportedOperationException CannotCreateWorkItemException IdWrongFormatException IdWrongTypeException InvalidApplicationStateException InvalidLengthException NotAuthorizedException UserDoesNotExistException ObjectDoesNotExistException ParallelRoutingTaskException SCAServiceAccessFailureException SCAServiceResultErrorException SchedulingFailedException WrongKindException WrongMessageTypeException WrongStateException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.2 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode. 7.0 Throws a ParallelRoutingTaskException when starting of a parallel routing task failed. 7.0 Throws a SchedulingFailedException when scheduling the task failed.

#### restart

```
void restart(java.lang.String tkiid,
           ClientObjectWrapper input,
           boolean keepResultMessages)
             throws AdministratorCannotBeResolvedException,
                    ApplicationVetoException,
                    ArchiveUnsupportedOperationException,
                    CannotCreateWorkItemException,
                    IdWrongFormatException,
                    IdWrongTypeException,
                    InvalidApplicationStateException,
                    InvalidLengthException,
                    NotAuthorizedException,
                    UserDoesNotExistException,
                    ObjectDoesNotExistException,
                    ParallelRoutingTaskException,
                    SCAServiceAccessFailureException,
                    SCAServiceResultErrorException,
                    SchedulingFailedException,
                    WrongKindException,
                    WrongMessageTypeException,
                    WrongStateException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
```

The task instance can be a collaboration, invocation, or to-do task.
 The task instance can be in any state but inactive. Additionally,
 
An invocation task cannot be in the running state.
 A to-do task cannot be in an end state, that is, cannot be finished, failed, terminated,
 or expired. If the to-do task is forwarded, then the follow-on task cannot be in an end state.
 An inline to-do task cannot be in the ready or running state.
 

 The task instance can be escalated, suspended, or waiting for subtasks.
 The caller must be the originator or an administrator of the task instance.
 
 Note that collaboration, invocation, and to-do tasks are also known as
 human, originating, and participating tasks.
 
 Restarting the task instance causes staff resolution to be newly performed
 and all timers to be reset. If you used the update method to change timer
 durations, then timers are set up according to these values.
 If you used the update method to explicitely set a scheduler time, then the corresponding
 durations are not calculated. Timers are not set up.
 For inline to-do tasks, expiration is not recalculated.
 
 Any subtasks or follow-on tasks are deleted.
 Any escalations are cancelled and reset into the inactive state.
 
 For invocation tasks, the logged-on user becomes the starter of the restarted task instance.
 
 The action associated to this method is TaskActions.RESTARTTASK.
 
 This method is not supported in archive mode.

The object wrapped by the ClientObjectWrapper must be serializable.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when starting of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- restart void restart(TKIID tkiid, ClientObjectWrapper input, boolean keepResultMessages) throws AdministratorCannotBeResolvedException , ApplicationVetoException , ArchiveUnsupportedOperationException , CannotCreateWorkItemException , IdWrongFormatException , InvalidApplicationStateException , InvalidLengthException , NotAuthorizedException , UserDoesNotExistException , ObjectDoesNotExistException , ParallelRoutingTaskException , SCAServiceAccessFailureException , SCAServiceResultErrorException , SchedulingFailedException , WrongKindException , WrongMessageTypeException , WrongStateException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Restarts the specified task instance using the task instance ID. The task instance can be a collaboration, invocation, or to-do task. The task instance can be in any state but inactive. Additionally, The task instance can be escalated, suspended, or waiting for subtasks. The caller must be the originator or an administrator of the task instance. Note that collaboration, invocation, and to-do tasks are also known as human, originating, and participating tasks. Restarting the task instance causes staff resolution to be newly performed and all timers to be reset. If you used the update method to change timer durations, then timers are set up according to these values. If you used the update method to explicitely set a scheduler time, then the corresponding durations are not calculated. Timers are not set up. For inline to-do tasks, expiration is not recalculated. Any subtasks or follow-on tasks are deleted. Any escalations are cancelled and reset into the inactive state. For invocation tasks, the logged-on user becomes the starter of the restarted task instance. The action associated to this method is TaskActions.RESTARTTASK . This method is not supported in archive mode. Parameters: tkiid - The task instance ID that is used to identify the task instance. input - The input message. If no input message is provided, the original input message is used. Note that, for inline to-do tasks, the input message is not synchronized with the Business Flow Manager staff activity. The object wrapped by the ClientObjectWrapper must be serializable. keepResultMessages - Specifies whether output or fault messages are to be kept. True states that any output or fault message set is to be kept. False states that any output or fault message set is to be deleted. Throws: AdministratorCannotBeResolvedException ApplicationVetoException ArchiveUnsupportedOperationException CannotCreateWorkItemException IdWrongFormatException InvalidApplicationStateException InvalidLengthException NotAuthorizedException UserDoesNotExistException ObjectDoesNotExistException ParallelRoutingTaskException SCAServiceAccessFailureException SCAServiceResultErrorException SchedulingFailedException WrongKindException WrongMessageTypeException WrongStateException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.2 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode. 7.0 Throws a ParallelRoutingTaskException when starting of a parallel routing task failed. 7.0 Throws a SchedulingFailedException when scheduling the task failed.

#### restart

```
void restart(TKIID tkiid,
           ClientObjectWrapper input,
           boolean keepResultMessages)
             throws AdministratorCannotBeResolvedException,
                    ApplicationVetoException,
                    ArchiveUnsupportedOperationException,
                    CannotCreateWorkItemException,
                    IdWrongFormatException,
                    InvalidApplicationStateException,
                    InvalidLengthException,
                    NotAuthorizedException,
                    UserDoesNotExistException,
                    ObjectDoesNotExistException,
                    ParallelRoutingTaskException,
                    SCAServiceAccessFailureException,
                    SCAServiceResultErrorException,
                    SchedulingFailedException,
                    WrongKindException,
                    WrongMessageTypeException,
                    WrongStateException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
```

The task instance can be a collaboration, invocation, or to-do task.
 The task instance can be in any state but inactive. Additionally,
 
An invocation task cannot be in the running state.
 A to-do task cannot be in an end state, that is, cannot be finished, failed, terminated,
 or expired. If the to-do task is forwarded, then the follow-on task cannot be in an end state.
 An inline to-do task cannot be in the ready or running state.
 

 The task instance can be escalated, suspended, or waiting for subtasks.
 The caller must be the originator or an administrator of the task instance.
 
 Note that collaboration, invocation, and to-do tasks are also known as
 human, originating, and participating tasks.
 
 Restarting the task instance causes staff resolution to be newly performed
 and all timers to be reset. If you used the update method to change timer
 durations, then timers are set up according to these values.
 If you used the update method to explicitely set a scheduler time, then the corresponding
 durations are not calculated. Timers are not set up.
 For inline to-do tasks, expiration is not recalculated.
 
 Any subtasks or follow-on tasks are deleted.
 Any escalations are cancelled and reset into the inactive state.
 
 For invocation tasks, the logged-on user becomes the starter of the restarted task instance.
 
 The action associated to this method is TaskActions.RESTARTTASK.
 
 This method is not supported in archive mode.

The object wrapped by the ClientObjectWrapper must be serializable.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when starting of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- resume
void resume(java.lang.String tkiid)
            throws ApplicationVetoException,
                   ArchiveUnsupportedOperationException,
                   IdWrongFormatException,
                   IdWrongTypeException,
                   NotAuthorizedException,
                   ObjectDoesNotExistException,
                   WrongKindException,
                   WrongStateException,
                   UnexpectedFailureException,
                   java.rmi.RemoteException,
                   javax.ejb.EJBException
Resumes the execution of the specified suspended collaboration or to-do
 task instance using a string representation of the task instance ID.
 Collaboration and to-do task instances are also known as human and participating task instances.
 
 The suspended task instance can be in the ready or claimed state. It can be
 escalated or waiting for subtasks.
 The caller can be the owner, originator, or administrator of the task instance.
 
 The action associated to this method is TaskActions.RESUME.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID to be resumed.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- resume
void resume(TKIID tkiid)
            throws ApplicationVetoException,
                   ArchiveUnsupportedOperationException,
                   IdWrongFormatException,
                   NotAuthorizedException,
                   ObjectDoesNotExistException,
                   WrongKindException,
                   WrongStateException,
                   UnexpectedFailureException,
                   java.rmi.RemoteException,
                   javax.ejb.EJBException
Resumes the execution of the specified suspended collaboration or to-do
 task instance using the task instance ID.
 Collaboration and to-do task instances are also
 known as human and participating task instances.
 
 The suspended task instance can be in the ready or claimed state. It can be
 escalated or waiting for subtasks.
 The caller can be the owner, originator, or administrator of the task instance.
 
 The action associated to this method is TaskActions.RESUME.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID of the task instance to be resumed.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- searchGroupDetails
java.util.List searchGroupDetails(java.lang.String searchCondition,
                                java.lang.String[] groupProperties,
                                java.lang.String[] userProperties,
                                java.lang.String[] subGroupProperties,
                                java.lang.Integer threshold)
                                  throws ParameterNullException,
                                         StaffServiceCannotAccessVMMException,
                                         StaffServiceRuntimeException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Returns details about the groups searched for.
 All properties of type String from the VMM Group object
 can be requested, for example, displayName or description.
 
 Note that this request does not participate in any global transaction, that is, exceptions do
 not cause a global transaction rollback.
Parameters:searchCondition - The groups that are to be searched for.
    
    The group names are specified as part of a VMM search expression
    "//entities[@xsi:type='Group' and ( searchCondition )]". For example,
    If you specify a search condition "cn='a*'", the following VMM search expression
    is build and executed: "//entities[@xsi:type='Group' and (cn='a*')]".groupProperties - The Group VMM properties that are to be returned
    for the groups found. The "members" property is ignored, if specified.
    If no group properties are specified, then no properties are returned. The name of the
    group is, however, returned.userProperties - The PersonAccount VMM properties that are to be returned for the users
    directly contained in the group. If not specified, an empty list of user details is returned.subGroupProperties - The Group VMM properties that are to be returned for the subgroups
    directly contained in the group. If not specified, an empty list of group details is returned.
    Note that the "members" property is ignored, if specified.threshold - The maximum number of group, user, and subgroup objects to be returned from the
    server to the client. If a threshold is not to be applied, null must be specified.
    
    Group details are determined depth-first. This means that the last group returned
    may not be complete if a threshold is applied.
 
Returns:List -
    A list of GroupDetail objects.
    Returns an empty list when there are no groups that fulfil the search condition.
 
Throws:
ParameterNullException
StaffServiceCannotAccessVMMException
StaffServiceRuntimeException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2

- searchUserDetails
java.util.List searchUserDetails(java.lang.String searchCondition,
                               java.lang.String[] userProperties,
                               java.lang.Integer threshold)
                                 throws ParameterNullException,
                                        StaffServiceCannotAccessVMMException,
                                        StaffServiceRuntimeException,
                                        UnexpectedFailureException,
                                        java.rmi.RemoteException,
                                        javax.ejb.EJBException
Returns details about the users searched for.
 All properties of type String or IdentifierType from the VMM PersonAccount object
 can be requested, for example, uid, cn, sn, givenName, or manager. For properties of
 type IdentifierType, the sub-property uniqueName is returned as a string.
 
 Note that this request does not participate in any global transaction, that is, exceptions do
 not cause a global transaction rollback.
Parameters:searchCondition - The users that are to be searched for.
    
    The users are specified as part of a VMM search expression
    "//entities[@xsi:type='PersonAccount' and ( searchCondition )]". For example,
    If you specify a search condition "uid='a*'", the following VMM search expression
    is build and executed: "//entities[@xsi:type='PersonAccount' and (uid='a*')]".userProperties - The PersonAccount VMM properties that are to be returned for the users found.
     If no user properties are specified, then no properties are returned. The name of the
     user is, however, returned.threshold - The maximum number of UserDetail objects to be returned from the
    server to the client. If a threshold is not to be applied, null must be specified.
 
Returns:List -
    A list of UserDetail objects.
    Returns an empty list when there are no users that fulfil the search condition.
 
Throws:
ParameterNullException
StaffServiceCannotAccessVMMException
StaffServiceRuntimeException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2

- setAbsence
void setAbsence(boolean absence)
                throws ArchiveUnsupportedOperationException,
                       StaffServiceCannotAccessVMMException,
                       StaffServiceSubstitutionNotEnabledException,
                       StaffServiceRuntimeException,
                       UserDoesNotExistException,
                       UnexpectedFailureException,
                       java.rmi.RemoteException,
                       javax.ejb.EJBException
Deprecated. As of version 7.0, replaced by setUserSubstitutionDetail.
Sets the absence information of the logged-on user to the specified value.
  Absent users do not receive any work items but a substitute receives the work item instead.
 
 This method is not supported in archive mode.
Parameters:absence - Specifies the absence setting of the logged-on user.
    True states that the specified user is absent.
    False states that the specified user is not absent.
 
Throws:
ArchiveUnsupportedOperationException
StaffServiceCannotAccessVMMException
StaffServiceSubstitutionNotEnabledException
StaffServiceRuntimeException
UserDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setAbsence
void setAbsence(java.lang.String userID,
              boolean absence)
                throws ArchiveUnsupportedOperationException,
                       NotAuthorizedException,
                       ParameterNullException,
                       StaffServiceCannotAccessVMMException,
                       StaffServiceSubstitutionNotEnabledException,
                       StaffServiceRuntimeException,
                       UserDoesNotExistException,
                       UnexpectedFailureException,
                       java.rmi.RemoteException,
                       javax.ejb.EJBException
Deprecated. As of version 7.0, replaced by setUserSubstitutionDetail.
Sets the absence information of the specified user to the specified value.
  Absent users do not receive any work items but a substitute receives the work item instead.
  
  If setting the absence is not restricted to administrators, then everybody can
  set the absence flag of any user.
  
  If setting the absence is restricted to administrators, then only the
  task system administrators can set the absence flag
  of arbitrary users. A user may, however, always set his/her absence.
 
 This method is not supported in archive mode.
Parameters:userID - The name of the user whose absence setting is to be set.absence - States the absence setting of the specified user.
    True states that the specified user is absent.
    False states that the specified user is not absent.
 
Throws:
ArchiveUnsupportedOperationException
NotAuthorizedException
ParameterNullException
StaffServiceCannotAccessVMMException
StaffServiceSubstitutionNotEnabledException
StaffServiceRuntimeException
UserDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setCustomProperty
void setCustomProperty(java.lang.String identifier,
                     java.lang.String propertyName,
                     java.lang.String propertyValue)
                       throws ApplicationVetoException,
                              ArchiveUnsupportedOperationException,
                              IdWrongFormatException,
                              IdWrongTypeException,
                              InvalidLengthException,
                              NotAuthorizedException,
                              ObjectDoesNotExistException,
                              ParameterNullException,
                              WrongKindException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Stores custom-specific values for the specified task or escalation instance
 using a string representation of the object ID.
 
 Custom properties allow a user to add additional properties to tasks or escalations beyond those
 provided and managed by the task manager.
 
 A custom property has a name and a value of type string.
 
 Custom properties can be provided in any state of the task or escalation instance.
 The parent application may, however, reject to set a property.
 The caller must be the originator, owner, starter, editor, or administrator of the task instance
 or must be the escalation receiver or administrator of the escalation instance.
 
 The action associated to this method is TaskActions.SETCUSTOMPROPERTY or
 EscalationActions.SETCUSTOMPROPERTY.
 
 This method is not supported in archive mode.
Parameters:identifier - A string representation of the task or escalation instance ID
    that is used to identify the task or escalation instance.propertyName - The name of the custom property to be set. The name must not be greater than 220 bytes in UTF-8 format.propertyValue - The custom value to be set. The value must not be greater than 254 bytes in UTF-8 format.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.1
 
 Supports escalation instances.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setCustomProperty
void setCustomProperty(ESIID esiid,
                     java.lang.String propertyName,
                     java.lang.String propertyValue)
                       throws ApplicationVetoException,
                              ArchiveUnsupportedOperationException,
                              IdWrongFormatException,
                              InvalidLengthException,
                              NotAuthorizedException,
                              ObjectDoesNotExistException,
                              ParameterNullException,
                              WrongKindException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Stores custom-specific values for the specified escalation instance.
 
 Custom properties allow a user to add additional properties to escalations beyond those
 provided and managed by the task manager.
 
 A custom property has a name and a value of type string.
 
 Custom properties can be provided in any state of the escalation instance.
 The parent application may, however, reject to set a property.
 The caller must be the escalation receiver, or administrator of the escalation instance.
 
 The action associated to this method is
 EscalationActions.SETCUSTOMPROPERTY.
 
 This method is not supported in archive mode.
Parameters:esiid - The object ID of the escalation instance.propertyName - The name of the custom property to be set. The name must not be greater than 220 bytes in UTF-8 format.propertyValue - The custom value to be set. The value must not be greater than 254 bytes in UTF-8 format.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setCustomProperty
void setCustomProperty(TKIID tkiid,
                     java.lang.String propertyName,
                     java.lang.String propertyValue)
                       throws ApplicationVetoException,
                              ArchiveUnsupportedOperationException,
                              IdWrongFormatException,
                              InvalidLengthException,
                              NotAuthorizedException,
                              ObjectDoesNotExistException,
                              ParameterNullException,
                              WrongKindException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Stores custom-specific values for the specified task instance.
 
 Custom properties allow a user to add additional properties to tasks beyond those
 provided and managed by the task manager.
 
 A custom property has a name and a value of type string.
 
 Custom properties can be provided in any state of the task instance.
 The parent application may, however, reject to set a property.
 The caller must be the originator, owner, starter, editor, or administrator of the task instance.
 
 The action associated to this method is TaskActions.SETCUSTOMPROPERTY.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID of the task instance.propertyName - The name of the custom property to be set. The name must not be greater than 220 bytes in UTF-8 format.propertyValue - The custom value to be set. The value must not be greater than 254 bytes in UTF-8 format.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setCustomProperty java.util.List setCustomProperty(java.lang.String[] tkiids, java.lang.String propertyName, java.lang.String propertyValue) throws ArchiveUnsupportedOperationException , IdWrongFormatException , IdWrongTypeException , InvalidLengthException , ParameterNullException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Stores custom-specific values for the specified task instances using string representations of the task instance IDs. Custom properties allow a user to add additional properties to tasks beyond those provided and managed by the task manager. A custom property has a name and a value of type string. Custom properties can be provided in any state of the task instance. The parent application may, however, reject to set a property. The caller must be the originator, owner, starter, editor, or administrator of the task instance. All operations are executed within the current transaction. If a transaction timeout occurs, then all already executed operations are rolled back. The action associated to this method is TaskActions.SETCUSTOMPROPERTY . This method is not supported in archive mode. Parameters: tkiids - An array of task instance IDs that are used to identify the tasks, propertyName - The name of the custom property to be set. The name must not be greater than 220 bytes in UTF-8 format. propertyValue - The custom value to be set. The value must not be greater than 254 bytes in UTF-8 format. Returns: List - A list of TaskResult objects, one for every task instance specified. Refer to TaskResult . If a single operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all operations are undone. Throws: ArchiveUnsupportedOperationException IdWrongFormatException IdWrongTypeException InvalidLengthException ParameterNullException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 7.0 Change History Release Modification 7.0.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### setCustomProperty

```
java.util.List setCustomProperty(java.lang.String[] tkiids,
                               java.lang.String propertyName,
                               java.lang.String propertyValue)
                                 throws ArchiveUnsupportedOperationException,
                                        IdWrongFormatException,
                                        IdWrongTypeException,
                                        InvalidLengthException,
                                        ParameterNullException,
                                        UnexpectedFailureException,
                                        java.rmi.RemoteException,
                                        javax.ejb.EJBException
```

Custom properties allow a user to add additional properties to tasks beyond those
 provided and managed by the task manager.
 
 A custom property has a name and a value of type string.
 
 Custom properties can be provided in any state of the task instance.
 The parent application may, however, reject to set a property.
 The caller must be the originator, owner, starter, editor, or administrator of the task instance.
 
 All operations are executed within the current transaction.
 If a transaction timeout occurs, then all already executed operations are rolled back.
 
 The action associated to this method is TaskActions.SETCUSTOMPROPERTY.
 
 This method is not supported in archive mode.

If a single operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.ObjectDoesNotExistException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all operations are undone.

Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setCustomProperty java.util.List setCustomProperty(TKIID [] tkiids, java.lang.String propertyName, java.lang.String propertyValue) throws ArchiveUnsupportedOperationException , IdWrongFormatException , InvalidLengthException , ParameterNullException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Stores custom-specific values for the specified task instances using task instance IDs. Custom properties allow a user to add additional properties to tasks beyond those provided and managed by the task manager. A custom property has a name and a value of type string. Custom properties can be provided in any state of the task instance. The parent application may, however, reject to set a property. The caller must be the originator, owner, starter, editor, or administrator of the task instance. All operations are executed within the current transaction. If a transaction timeout occurs, then all already executed operations are rolled back. The action associated to this method is TaskActions.SETCUSTOMPROPERTY . This method is not supported in archive mode. Parameters: tkiids - An array of task instance IDs that are used to identify the tasks, propertyName - The name of the custom property to be set. The name must not be greater than 220 bytes in UTF-8 format. propertyValue - The custom value to be set. The value must not be greater than 254 bytes in UTF-8 format. Returns: List - A list of TaskResult objects, one for every task instance specified. Refer to TaskResult . If a single transfer operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all operations are undone. Throws: ArchiveUnsupportedOperationException IdWrongFormatException InvalidLengthException ParameterNullException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 7.0 Change History Release Modification 7.0.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### setCustomProperty

```
java.util.List setCustomProperty(TKIID[] tkiids,
                               java.lang.String propertyName,
                               java.lang.String propertyValue)
                                 throws ArchiveUnsupportedOperationException,
                                        IdWrongFormatException,
                                        InvalidLengthException,
                                        ParameterNullException,
                                        UnexpectedFailureException,
                                        java.rmi.RemoteException,
                                        javax.ejb.EJBException
```

Custom properties allow a user to add additional properties to tasks beyond those
 provided and managed by the task manager.
 
 A custom property has a name and a value of type string.
 
 Custom properties can be provided in any state of the task instance.
 The parent application may, however, reject to set a property.
 The caller must be the originator, owner, starter, editor, or administrator of the task instance.
 
 All operations are executed within the current transaction.
 If a transaction timeout occurs, then all already executed operations are rolled back.
 
 The action associated to this method is TaskActions.SETCUSTOMPROPERTY.
 
 This method is not supported in archive mode.

If a single transfer operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.ObjectDoesNotExistException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all operations are undone.

Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setCustomProperties
void setCustomProperties(java.lang.String tkiid,
                       java.util.List customProperties)
                         throws ApplicationVetoException,
                                ArchiveUnsupportedOperationException,
                                IdWrongFormatException,
                                IdWrongTypeException,
                                InvalidLengthException,
                                NotAuthorizedException,
                                ObjectDoesNotExistException,
                                ParameterNullException,
                                WrongKindException,
                                UnexpectedFailureException,
                                java.rmi.RemoteException,
                                javax.ejb.EJBException
Stores custom-specific values for the specified task instance using
 a string representation of the task instance ID.
 
 Custom properties allow a user to add additional properties to tasks beyond those
 provided and managed by the task manager.
 
 A custom property has a name and a value of type string.
 It may be constructed using the CustomPropertyFactory.
 
 Custom properties can be provided in any state of the task instance.
 The parent application may, however, reject to set a property.
 The caller must be the originator, owner, starter, editor, or administrator of the task instance.
 
 The action associated to this method is TaskActions.SETCUSTOMPROPERTY.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID.customProperties - A list of CustomProperty objects.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setCustomProperties
void setCustomProperties(TKIID tkiid,
                       java.util.List customProperties)
                         throws ApplicationVetoException,
                                ArchiveUnsupportedOperationException,
                                IdWrongFormatException,
                                InvalidLengthException,
                                NotAuthorizedException,
                                ObjectDoesNotExistException,
                                ParameterNullException,
                                WrongKindException,
                                UnexpectedFailureException,
                                java.rmi.RemoteException,
                                javax.ejb.EJBException
Stores custom-specific values for the specified task instance using
 the task instance ID.
 
 Custom properties allow a user to add additional properties to tasks beyond those
 provided and managed by the task manager.
 
 A custom property has a name and a value of type string.
 It may be constructed using the CustomPropertyFactory.
 
 Custom properties can be provided in any state of the task instance.
 The parent application may, however, reject to set a property.
 The caller must be the originator, owner, starter, editor, or administrator of the task instance.
 
 The action associated to this method is TaskActions.SETCUSTOMPROPERTY.
 
 This method is not supported in archive mode.
Parameters:tkiid - The task instance ID that is used to identify the task instance.customProperties - A list of CustomProperty objects.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setBinaryCustomProperty
void setBinaryCustomProperty(java.lang.String identifier,
                           BinaryCustomProperty property)
                             throws ApplicationVetoException,
                                    ArchiveUnsupportedOperationException,
                                    IdWrongFormatException,
                                    IdWrongTypeException,
                                    InvalidLengthException,
                                    NotAuthorizedException,
                                    ObjectDoesNotExistException,
                                    ParameterNullException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Stores custom-specific binary values for the specified task or escalation instance
 using a string representation of the task or escalation instance ID.
 
 Custom properties allow a user to add additional properties to tasks or escalations
 beyond those provided and managed by the task manager. Binary custom properties allow,
 for example, to attach a Java object to a task instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 Custom properties can be provided in any state of the task or escalation instance.
 The parent application may, however, reject to set a property.
 The caller must be the originator, owner, starter, editor, or administrator of the task instance
 or must be the escalation receiver or administrator of the escalation instance.
 
 The action associated to this method is TaskActions.SETCUSTOMPROPERTY or
 EscalationActions.SETCUSTOMPROPERTY.
 
 This method is not supported in archive mode.
Parameters:identifier - A string representation of the task or escalation instance ID that is used to identify the object.property - The BinaryCustomProperty object.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1
 
 Supports escalation instances.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setBinaryCustomProperty
void setBinaryCustomProperty(TKIID tkiid,
                           BinaryCustomProperty property)
                             throws ApplicationVetoException,
                                    ArchiveUnsupportedOperationException,
                                    IdWrongFormatException,
                                    InvalidLengthException,
                                    NotAuthorizedException,
                                    ObjectDoesNotExistException,
                                    ParameterNullException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Stores custom-specific binary values for the specified task instance using
 the task instance ID.
 
 Custom properties allow a user to add additional properties to tasks
 beyond those provided and managed by the task manager. Binary custom properties allow,
 for example, to attach a Java object to a task instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 Custom properties can be provided in any state of the task instance.
 The parent application may, however, reject to set a property.
 The caller must be the originator, owner, starter, editor, or administrator of the task instance.
 
 The action associated to this method is TaskActions.SETCUSTOMPROPERTY.
 
 This method is not supported in archive mode.
Parameters:tkiid - The task instance ID that is used to identify the task instance.property - The BinaryCustomProperty object.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setBinaryCustomProperty
void setBinaryCustomProperty(ESIID esiid,
                           BinaryCustomProperty property)
                             throws ApplicationVetoException,
                                    ArchiveUnsupportedOperationException,
                                    IdWrongFormatException,
                                    InvalidLengthException,
                                    NotAuthorizedException,
                                    ObjectDoesNotExistException,
                                    ParameterNullException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Stores custom-specific binary values for the specified escalation instance using
 the escalation instance ID.
 
 Custom properties allow a user to add additional properties to escalations
 beyond those provided and managed by the task manager. Binary custom properties allow,
 for example, to attach a Java object to an escalation instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 Custom properties can be provided in any state of the escalation instance.
 The parent application may, however, reject to set a property.
 The caller must be the escalation receiver or administrator of the escalation instance.
 
 The action associated to this method is
 EscalationActions.SETCUSTOMPROPERTY.
 
 This method is not supported in archive mode.
Parameters:esiid - The escalation instance ID that is used to identify the escalation instance.property - The BinaryCustomProperty object.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setFaultMessage
void setFaultMessage(java.lang.String tkiid,
                   java.lang.String faultName,
                   ClientObjectWrapper faultMessage)
                     throws ApplicationVetoException,
                            ArchiveUnsupportedOperationException,
                            IdWrongFormatException,
                            IdWrongTypeException,
                            InvalidQNameException,
                            NotAuthorizedException,
                            ObjectDoesNotExistException,
                            ParameterNullException,
                            WrongKindException,
                            WrongMessageTypeException,
                            WrongStateException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Stores the specified fault message for the specified task instance into the
 database using a string representation of the task instance ID.
 The fault message is saved only, that is, the state of the task instance is not changed.
 Refer to complete for information on how to
 complete a task instance.
 
 Any previously stored fault or output message is deleted.
 
 The task instance must be a collaboration or to-do task.
 Collaboration and to-do task instances are also known as human and participating task instances.
 
 The task instance must be in the claimed state. It can be escalated.
 The caller must be the owner, an editor, or an administrator of the task instance.
 
 The action associated to this method is
 TaskActions.SETFAULTMESSAGE.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID.
    This string is used
    to identify the task instance whose fault message is to be set.faultName - The name of the fault message to be set.
    Must be a fault defined for the task. Refer
    to getFaultNames.faultMessage - The fault message.
    The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
InvalidQNameException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.1.0.1
 
 Throws an ApplicationFailedException when the application refuses to execute the method.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setFaultMessage
void setFaultMessage(TKIID tkiid,
                   java.lang.String faultName,
                   ClientObjectWrapper faultMessage)
                     throws ApplicationVetoException,
                            ArchiveUnsupportedOperationException,
                            IdWrongFormatException,
                            InvalidQNameException,
                            NotAuthorizedException,
                            ObjectDoesNotExistException,
                            ParameterNullException,
                            WrongKindException,
                            WrongMessageTypeException,
                            WrongStateException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Stores the specified fault message for the specified task instance into the
 database using the task instance ID.
 The fault message is saved only, that is, the state of the task instance is not changed.
 Refer to complete for information on how to
 complete a task instance.
 
 Any previously stored fault or output message is deleted.
 
 The task instance must be in the claimed state. It can be escalated.
 The caller must be the owner, an editor, or an administrator of the task instance.
 
 The action associated to this method is
 TaskActions.SETFAULTMESSAGE.
 
 This method is not supported in archive mode.
Parameters:tkiid - The task instance ID that is used
    to identify the task instance whose fault message is to be set.faultName - The name of the fault message to be set.
    Must be a fault defined for the task. Refer
    to getFaultNames.faultMessage - The fault message.
    The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
InvalidQNameException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.1.0.1
 
 Throws an ApplicationFailedException when the application refuses to execute the method.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setInlineCustomProperties
void setInlineCustomProperties(java.lang.String tkiid,
                             java.util.List customProperties)
                               throws ApplicationVetoException,
                                      ArchiveUnsupportedOperationException,
                                      IdWrongFormatException,
                                      IdWrongTypeException,
                                      InvalidLengthException,
                                      NotAuthorizedException,
                                      ObjectDoesNotExistException,
                                      ParameterNullException,
                                      UnsupportedParameterValueException,
                                      UnexpectedFailureException,
                                      java.rmi.RemoteException,
                                      javax.ejb.EJBException
Stores custom-specific values for the specified task instance using
 a string representation of the task instance ID.
 
 Custom properties allow a user to add additional properties to a task
 beyond those provided and managed by the Human Task Manager.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the task instance. Thus, using inline custom properties
 can increase performance.
 
 An inline custom property has a predefined name and a value of type string.
 It may be constructed using the CustomPropertyFactory.
 
 Custom properties can be provided in any state of the task instance.
 The parent application may, however, reject to set a property.
 The caller must be the originator, owner, starter, editor, or administrator of the task instance.
 
 The action associated to this method is TaskActions.SETCUSTOMPROPERTY.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance object ID that is used
    to identify the task instance.customProperties - A list of InlineCustomProperty objects.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnsupportedParameterValueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- setInlineCustomProperties
void setInlineCustomProperties(TKIID tkiid,
                             java.util.List customProperties)
                               throws ApplicationVetoException,
                                      ArchiveUnsupportedOperationException,
                                      IdWrongFormatException,
                                      InvalidLengthException,
                                      NotAuthorizedException,
                                      ObjectDoesNotExistException,
                                      ParameterNullException,
                                      UnsupportedParameterValueException,
                                      UnexpectedFailureException,
                                      java.rmi.RemoteException,
                                      javax.ejb.EJBException
Stores custom-specific values for the specified task instance using
 the task instance ID.
 
 Custom properties allow a user to add additional properties to a task
 beyond those provided and managed by the Human Task Manager.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the task instance. Thus, using inline custom properties
 can increase performance.
 
 An inline custom property has a predefined name and a value of type string.
 It may be constructed using the CustomPropertyFactory.
 
 Custom properties can be provided in any state of the task instance.
 The parent application may, however, reject to set a property.
 The caller must be the originator, owner, starter, editor, or administrator of the task instance.
 
 The action associated to this method is TaskActions.SETCUSTOMPROPERTY.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID of the task instance for which the inline custom properties
 are to be set.customProperties - A list of InlineCustomProperty objects.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnsupportedParameterValueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- setInlineCustomProperty
void setInlineCustomProperty(java.lang.String tkiid,
                           InlineCustomProperty property)
                             throws ApplicationVetoException,
                                    ArchiveUnsupportedOperationException,
                                    IdWrongFormatException,
                                    IdWrongTypeException,
                                    InvalidLengthException,
                                    NotAuthorizedException,
                                    ObjectDoesNotExistException,
                                    ParameterNullException,
                                    UnsupportedParameterValueException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Stores a custom-specific value for the specified task instance
 using a string representation of the task instance ID.
 
 Custom properties allow a user to add additional properties to a task
 beyond those provided and managed by the Human Task Manager.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the task instance. Thus, using inline custom properties
 can increase performance.
 
 An inline custom property has a predefined name and a value of type string.
 It may be constructed using the CustomPropertyFactory.
 
 Custom properties can be provided in any state of the task instance.
 The parent application may, however, reject to set a property.
 The caller must be the originator, owner, starter, editor, or administrator of the task instance.
 
 The action associated to this method is TaskActions.SETCUSTOMPROPERTY.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance object ID that is used
    to identify the task instance.property - The inline custom property to be set.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnsupportedParameterValueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- setInlineCustomProperty
void setInlineCustomProperty(TKIID tkiid,
                           InlineCustomProperty property)
                             throws ApplicationVetoException,
                                    ArchiveUnsupportedOperationException,
                                    IdWrongFormatException,
                                    InvalidLengthException,
                                    NotAuthorizedException,
                                    ObjectDoesNotExistException,
                                    ParameterNullException,
                                    UnsupportedParameterValueException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Stores a custom specific value for the specified task instance using the task instance ID.
 
 Custom properties allow a user to add additional properties to a task
 beyond those provided and managed by the Human Task Manager.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the task instance. Thus, using inline custom properties
 can increase performance.
 
 An inline custom property has a predefined name and a value of type string.
 It may be constructed using the CustomPropertyFactory.
 
 Custom properties can be provided in any state of the task instance.
 The parent application may, however, reject to set a property.
 The caller must be the originator, owner, starter, editor, or administrator of the task instance.
 
 The action associated to this method is TaskActions.SETCUSTOMPROPERTY.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID of the task instance for which the inline custom property
 is to be set.property - The inline custom property to be set.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnsupportedParameterValueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- setInlineCustomProperty java.util.List setInlineCustomProperty(java.lang.String[] tkiids, InlineCustomProperty property) throws ArchiveUnsupportedOperationException , IdWrongFormatException , IdWrongTypeException , InvalidLengthException , ParameterNullException , UnsupportedParameterValueException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Stores a custom-specific value for the specified task instances using string representations of the task instance IDs. Custom properties allow a user to add additional properties to a task beyond those provided and managed by the Human Task Manager. In contrast to custom properties that are attached to an object, inline custom properties are an integral part of the task instance. Thus, using inline custom properties can increase performance. An inline custom property has a predefined name and a value of type string. It may be constructed using the CustomPropertyFactory . Custom properties can be provided in any state of the task instance. The parent application may, however, reject to set a property. The caller must be the originator, owner, starter, editor, or administrator of the task instance. The action associated to this method is TaskActions.SETCUSTOMPROPERTY . This method is not supported in archive mode. Parameters: tkiids - An array of task instance IDs that are used to identify the task instances, property - The inline custom property to be set. Returns: List - A list of TaskResult objects, one for every task instance specified. Refer to TaskResult . If a single operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all operations are undone. Throws: ArchiveUnsupportedOperationException IdWrongFormatException IdWrongTypeException InvalidLengthException ParameterNullException UnsupportedParameterValueException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 7.5.1

#### setInlineCustomProperty

```
java.util.List setInlineCustomProperty(java.lang.String[] tkiids,
                                     InlineCustomProperty property)
                                       throws ArchiveUnsupportedOperationException,
                                              IdWrongFormatException,
                                              IdWrongTypeException,
                                              InvalidLengthException,
                                              ParameterNullException,
                                              UnsupportedParameterValueException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
```

Custom properties allow a user to add additional properties to a task
 beyond those provided and managed by the Human Task Manager.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the task instance. Thus, using inline custom properties
 can increase performance.
 
 An inline custom property has a predefined name and a value of type string.
 It may be constructed using the CustomPropertyFactory.
 
 Custom properties can be provided in any state of the task instance.
 The parent application may, however, reject to set a property.
 The caller must be the originator, owner, starter, editor, or administrator of the task instance.
 
 The action associated to this method is TaskActions.SETCUSTOMPROPERTY.
 
 This method is not supported in archive mode.

If a single operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.ObjectDoesNotExistException
 

 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all operations are undone.

- setInlineCustomProperty java.util.List setInlineCustomProperty(TKIID [] tkiids, InlineCustomProperty property) throws ArchiveUnsupportedOperationException , IdWrongFormatException , InvalidLengthException , ParameterNullException , UnsupportedParameterValueException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Stores a custom-specific value for the specified task instances using task instance IDs. Custom properties allow a user to add additional properties to a task beyond those provided and managed by the Human Task Manager. In contrast to custom properties that are attached to an object, inline custom properties are an integral part of the task instance. Thus, using inline custom properties can increase performance. An inline custom property has a predefined name and a value of type string. It may be constructed using the CustomPropertyFactory . Custom properties can be provided in any state of the task instance. The parent application may, however, reject to set a property. The caller must be the originator, owner, starter, editor, or administrator of the task instance. The action associated to this method is TaskActions.SETCUSTOMPROPERTY . This method is not supported in archive mode. Parameters: tkiids - An array of task instance IDs that are used to identify the task instances, property - The inline custom property to be set. Returns: List - A list of TaskResult objects, one for every task instance specified. Refer to TaskResult . If a single operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all operations are undone. Throws: ArchiveUnsupportedOperationException IdWrongFormatException InvalidLengthException ParameterNullException UnsupportedParameterValueException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 7.5.1

#### setInlineCustomProperty

```
java.util.List setInlineCustomProperty(TKIID[] tkiids,
                                     InlineCustomProperty property)
                                       throws ArchiveUnsupportedOperationException,
                                              IdWrongFormatException,
                                              InvalidLengthException,
                                              ParameterNullException,
                                              UnsupportedParameterValueException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
```

Custom properties allow a user to add additional properties to a task
 beyond those provided and managed by the Human Task Manager.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the task instance. Thus, using inline custom properties
 can increase performance.
 
 An inline custom property has a predefined name and a value of type string.
 It may be constructed using the CustomPropertyFactory.
 
 Custom properties can be provided in any state of the task instance.
 The parent application may, however, reject to set a property.
 The caller must be the originator, owner, starter, editor, or administrator of the task instance.
 
 The action associated to this method is TaskActions.SETCUSTOMPROPERTY.
 
 This method is not supported in archive mode.

If a single operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.ObjectDoesNotExistException
 

 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all operations are undone.

- setInputMessage
void setInputMessage(java.lang.String tkiid,
                   ClientObjectWrapper inputMessage)
                     throws ApplicationVetoException,
                            ArchiveUnsupportedOperationException,
                            DataHandlingException,
                            IdWrongFormatException,
                            IdWrongTypeException,
                            NotAuthorizedException,
                            ObjectDoesNotExistException,
                            ParameterNullException,
                            WrongKindException,
                            WrongMessageTypeException,
                            WrongStateException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Stores the input message of the specified task instance into the database
 using a string representation of the task instance ID.
 The input message is saved only, that is, the state of the task instance is not changed.
 Refer to startTask or claim
 for information on how to start or claim a task instance.
 
 Any previously stored input message is deleted.
 
 The task instance must be in the inactive state. It can be a collaboration, invocation,
 or to-do task.
 The caller must be the originator, a potential starter, or an administrator of the task instance.
 
 Note that collaboration, invocation, and to-do task instances are also known as
 human, originating, and participating task instances.
 
 The action associated to this method is
 TaskActions.SETINPUTMESSAGE.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID.
    This string is used
    to identify the task instance whose input message is to be set.inputMessage - The input message.
    The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
DataHandlingException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setInputMessage
void setInputMessage(TKIID tkiid,
                   ClientObjectWrapper inputMessage)
                     throws ApplicationVetoException,
                            ArchiveUnsupportedOperationException,
                            DataHandlingException,
                            IdWrongFormatException,
                            NotAuthorizedException,
                            ObjectDoesNotExistException,
                            ParameterNullException,
                            WrongKindException,
                            WrongMessageTypeException,
                            WrongStateException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Stores the input message of the specified task instance into the database
 using the task instance ID.
 The input message is saved only, that is, the state of the task instance is not changed.
 Refer to startTask or claim
 for information on how to start or claim a task instance.
 
 Any previously stored input message is deleted.
 
 The task instance must be in the inactive state. It can be a collaboration, invocation,
 or to-do task.
 The caller must be the originator, a potential starter, or an administrator of the task instance.
 
 Note that collaboration, invocation, and to-do task instances are also known as
 human, originating, and participating task instances.
 
 The action associated to this method is
 TaskActions.SETINPUTMESSAGE.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID of the task instance whose input message is to be set.inputMessage - The input message.
    The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
DataHandlingException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setOutputMessage
void setOutputMessage(java.lang.String tkiid,
                    ClientObjectWrapper outputMessage)
                      throws ApplicationVetoException,
                             ArchiveUnsupportedOperationException,
                             DataHandlingException,
                             IdWrongFormatException,
                             IdWrongTypeException,
                             NotAuthorizedException,
                             ObjectDoesNotExistException,
                             ParameterNullException,
                             WrongKindException,
                             WrongMessageTypeException,
                             WrongStateException,
                             UnexpectedFailureException,
                             java.rmi.RemoteException,
                             javax.ejb.EJBException
Stores the output message of the specified task instance into the database
 using a string representation of the task instance ID.
 The output message is saved only, that is, the state of the task instance is not changed.
 Refer to complete
 for information on how to complete a task instance.
 
 Any previously stored output or fault message is deleted.
 
 The task instance must be in the claimed state. It can be escalated.
 The caller must be the owner, an editor, or an administrator of the task instance.
 
 The action associated to this method is
 TaskActions.SETOUTPUTMESSAGE.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID.
    This string is used
    to identify the task instance whose output message is to be set.outputMessage - The output message.
    The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
DataHandlingException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.1.0.1
 
 Throws an ApplicationFailedException when the application refuses to execute the method.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setOutputMessage
void setOutputMessage(TKIID tkiid,
                    ClientObjectWrapper outputMessage)
                      throws ApplicationVetoException,
                             ArchiveUnsupportedOperationException,
                             DataHandlingException,
                             IdWrongFormatException,
                             NotAuthorizedException,
                             ObjectDoesNotExistException,
                             ParameterNullException,
                             WrongKindException,
                             WrongMessageTypeException,
                             WrongStateException,
                             UnexpectedFailureException,
                             java.rmi.RemoteException,
                             javax.ejb.EJBException
Stores the output message of the specified task instance into the database
 using the task instance ID.
 The output message is saved only, that is, the state of the task instance is not changed.
 Refer to complete
 for information on how to complete a task instance.
 
 Any previously stored output or fault message is deleted.
 
 The task instance must be in the claimed state. It can be escalated.
 The caller must be the owner, an editor, or an administrator of the task instance.
 
 The action associated to this method is
 TaskActions.SETOUTPUTMESSAGE.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID of the task instance whose output message is to be set.outputMessage - The output message.
    The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
DataHandlingException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.1.0.1
 
 Throws an ApplicationFailedException when the application refuses to execute the method.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setSubstitutes
void setSubstitutes(java.util.List substitutes)
                    throws ArchiveUnsupportedOperationException,
                           ParameterNullException,
                           StaffServiceCannotAccessVMMException,
                           StaffServiceSubstitutionNotEnabledException,
                           StaffServiceRuntimeException,
                           SubstituteDoesNotExistException,
                           UserDoesNotExistException,
                           UnexpectedFailureException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
Deprecated. As of version 7.0, replaced by setUserSubstitutionDetail.
Sets the substitutes of the logged-on user.
 
 This method is not supported in archive mode.
Parameters:substitutes - A list of users that are substitutes of the logged-on user.
    The substitutes that are provided replace any substitutes that are already set.
    To remove the substitutes that are set, specify an empty list.
    
    The user IDs of the substitutes are checked but the check may be executed case insensitively.
    The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments'
    custom property of the Human Task Manager configuration to 'true'.
 
Throws:
ArchiveUnsupportedOperationException
ParameterNullException
StaffServiceCannotAccessVMMException
StaffServiceSubstitutionNotEnabledException
StaffServiceRuntimeException
SubstituteDoesNotExistException
UserDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setSubstitutes
void setSubstitutes(java.lang.String userID,
                  java.util.List substitutes)
                    throws ArchiveUnsupportedOperationException,
                           NotAuthorizedException,
                           ParameterNullException,
                           StaffServiceCannotAccessVMMException,
                           StaffServiceSubstitutionNotEnabledException,
                           StaffServiceRuntimeException,
                           SubstituteDoesNotExistException,
                           UserDoesNotExistException,
                           UnexpectedFailureException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
Deprecated. As of version 7.0, replaced by setUserSubstitutionDetail.
Sets the substitutes of the specified user.
  
  If setting substitutes is not restricted to administrators, then everybody can
  set the substitutes of any user.
  
  If setting substitutes is restricted to administrators, then only task the
  task system administrators can set the substitutes
  of arbitrary users. A user may, however, always modify his/her substitutes.
 
 This method is not supported in archive mode.
Parameters:userID - The name of the user whose substitutes are to be set.
    It is checked whether the user exists but the check may be executed case insensitively.substitutes - A list of users that are substitutes of the specified user.
    The substitutes that are provided replace any substitutes that are already set.
    To remove the substitutes that are set, specify an empty list.
    
    The user IDs of the substitutes are checked but the check may be executed case insensitively.
    The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments'
    custom property of the Human Task Manager configuration to 'true'.
 
Throws:
ArchiveUnsupportedOperationException
NotAuthorizedException
ParameterNullException
StaffServiceCannotAccessVMMException
StaffServiceSubstitutionNotEnabledException
StaffServiceRuntimeException
SubstituteDoesNotExistException
UserDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setTaskRead
void setTaskRead(java.lang.String tkiid,
               boolean newValue)
                 throws ApplicationVetoException,
                        ArchiveUnsupportedOperationException,
                        IdWrongFormatException,
                        IdWrongTypeException,
                        NotAuthorizedException,
                        ObjectDoesNotExistException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Specifies whether the specified task instance is to be marked as read using
  a string representation of the task instance ID.
  
  The task instance can be in any state.
  The caller must have at least editor authority for the task instance.
 
 The action associated to this method is
 TaskActions.SETTASKREAD.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID
    that is used to identify the task instance.newValue - Specifies whether the task is to be marked as read.
   True states that the task is to be marked as read.
   False states that the task is not to be marked as read.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setTaskRead
void setTaskRead(TKIID tkiid,
               boolean newValue)
                 throws ApplicationVetoException,
                        ArchiveUnsupportedOperationException,
                        IdWrongFormatException,
                        NotAuthorizedException,
                        ObjectDoesNotExistException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Specifies whether the specified task instance is to be marked as read using
  the task instance ID.
  
  The task instance can be in any state.
  The caller must have at least editor authority for the task instance.
 
 The action associated to this method is
 TaskActions.SETTASKREAD.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID of the task instance.newValue - Specifies whether the task is to be marked as read.
   True states that the task is to be marked as read.
   False states that the task is not to be marked as read.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setUserSubstitutionDetail
void setUserSubstitutionDetail(UserSubstitutionDetail substitutionDetail)
                               throws ArchiveUnsupportedOperationException,
                                      NotAuthorizedException,
                                      StaffServiceCannotAccessVMMException,
                                      StaffServiceSubstitutionNotEnabledException,
                                      StaffServiceRuntimeException,
                                      ParameterNullException,
                                      SubstitutionInvalidParametersException,
                                      UserDoesNotExistException,
                                      UnexpectedFailureException,
                                      java.rmi.RemoteException,
                                      javax.ejb.EJBException
Sets absence and substitution details for the logged-on user.
 
 This method is not supported in archive mode.
Parameters:substitutionDetail - The absence and substitution details.
  Refer to UserSubstitutionDetail.
 
Throws:
ArchiveUnsupportedOperationException
NotAuthorizedException
StaffServiceCannotAccessVMMException
StaffServiceSubstitutionNotEnabledException
StaffServiceRuntimeException
ParameterNullException
SubstitutionInvalidParametersException
UserDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setUserSubstitutionDetail
void setUserSubstitutionDetail(java.lang.String userID,
                             UserSubstitutionDetail substitutionDetail)
                               throws ArchiveUnsupportedOperationException,
                                      NotAuthorizedException,
                                      StaffServiceCannotAccessVMMException,
                                      StaffServiceSubstitutionNotEnabledException,
                                      StaffServiceRuntimeException,
                                      ParameterNullException,
                                      SubstitutionInvalidParametersException,
                                      UserDoesNotExistException,
                                      UnexpectedFailureException,
                                      java.rmi.RemoteException,
                                      javax.ejb.EJBException
Sets absence and substitution details for the specified user.
  
  The caller must be a task system administrator.
 
 This method is not supported in archive mode.
Parameters:userID - The userID of the user whose settings are changed.substitutionDetail - The absence and substitution details.
  Refer to UserSubstitutionDetail.
 
Throws:
ArchiveUnsupportedOperationException
NotAuthorizedException
StaffServiceCannotAccessVMMException
StaffServiceSubstitutionNotEnabledException
StaffServiceRuntimeException
ParameterNullException
SubstitutionInvalidParametersException
UserDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- startTask
void startTask(java.lang.String tkiid,
             ClientObjectWrapper input,
             ReplyHandlerWrapper replyHandler)
               throws AdministratorCannotBeResolvedException,
                      ApplicationVetoException,
                      ArchiveUnsupportedOperationException,
                      CannotCreateWorkItemException,
                      IdWrongFormatException,
                      IdWrongTypeException,
                      InvalidLengthException,
                      NotAuthorizedException,
                      UserDoesNotExistException,
                      ObjectDoesNotExistException,
                      ParallelRoutingTaskException,
                      SCAServiceAccessFailureException,
                      SCAServiceResultErrorException,
                      SchedulingFailedException,
                      WrongKindException,
                      WrongMessageTypeException,
                      WrongStateException,
                      UnexpectedFailureException,
                      java.rmi.RemoteException,
                      javax.ejb.EJBException
Asynchronously executes a previously created task
 using a string representation of the task instance ID.
 
 The task instance must be in the inactive state.
 The caller must be a potential starter, the originator, or an administrator of the task.
 When the task is an invocation aka originating task instance, then the caller becomes the starter of the task.
 
 The action associated to this method is
 TaskActions.STARTTASK.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID that is used
    to identify the task instance.input - The input message.
    The object wrapped by the ClientObjectWrapper must be serializable.replyHandler - The reply handler to be used to send the result of execution back to the
   caller. "null" must be passed if no reply handler is provided.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
ParallelRoutingTaskException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when starting of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- startTask
void startTask(TKIID tkiid,
             ClientObjectWrapper input,
             ReplyHandlerWrapper replyHandler)
               throws AdministratorCannotBeResolvedException,
                      ApplicationVetoException,
                      ArchiveUnsupportedOperationException,
                      CannotCreateWorkItemException,
                      IdWrongFormatException,
                      InvalidLengthException,
                      NotAuthorizedException,
                      UserDoesNotExistException,
                      ObjectDoesNotExistException,
                      ParallelRoutingTaskException,
                      SCAServiceAccessFailureException,
                      SCAServiceResultErrorException,
                      SchedulingFailedException,
                      WrongKindException,
                      WrongMessageTypeException,
                      WrongStateException,
                      UnexpectedFailureException,
                      java.rmi.RemoteException,
                      javax.ejb.EJBException
Asynchronously executes a previously created task
 using the task instance ID.
 
 The task instance must be in the inactive state.
 The caller must be a potential starter, the originator, or an administrator of the task.
 When the task is an invocation aka originating task instance, then the caller becomes the starter of the task.
 
 The action associated to this method is
 TaskActions.STARTTASK.
 
 This method is not supported in archive mode.
Parameters:tkiid - The task instance ID that is used to identify the task instance.input - The input message.
    The object wrapped by the ClientObjectWrapper must be serializable.replyHandler - The reply handler to be used to send the result of execution back to the
   caller. "null" must be passed if no reply handler is provided.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongFormatException
InvalidLengthException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
ParallelRoutingTaskException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when starting of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- startTaskAsSubTask
void startTaskAsSubTask(java.lang.String tkiid,
                      java.lang.String parentTaskID,
                      ClientObjectWrapper input)
                        throws AdministratorCannotBeResolvedException,
                               ApplicationVetoException,
                               ArchiveUnsupportedOperationException,
                               CannotCreateWorkItemException,
                               IdWrongFormatException,
                               IdWrongTypeException,
                               InvalidApplicationStateException,
                               InvalidLengthException,
                               NotAuthorizedException,
                               UserDoesNotExistException,
                               ObjectDoesNotExistException,
                               ParallelRoutingTaskException,
                               SCAServiceAccessFailureException,
                               SCAServiceResultErrorException,
                               SchedulingFailedException,
                               SubTasksNotSupportedException,
                               WrongKindException,
                               WrongMessageTypeException,
                               WrongStateException,
                               UnexpectedFailureException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
Executes a previously created task as a subtask of the specified parent task instance
 using a string representation of the task instance ID.
 The parent task instance is then waiting for the completion of the subtask. It can only
 be completed when all subtasks came to an end.
 
 The subtask must be a collaboration or stand-alone invocation task. An invocation task
 must have been derived from a task template that has not been created at Runtime. The parent task
 instance must be a collaboration or to-do task in the claimed state.
 It can be escalated or already waiting for a subtask. It can, however, not be suspended.
 
 Note that collaboration, invocation, and to-do task instances are also known as
 human, originating, amd participating task instances.
 
 A subtask can only be
 started when the parent task supports subtask creation - refer to Task to view the
 task instance properties.
 
 The subtask instance must be in the inactive state. When started it will be in the ready
 or running state.
 The caller must be a potential starter, the originator, or an administrator of the subtask
 and an owner or administrator of the parent task instance.
 When the task is an invocation aka originating task instance, then the caller becomes the starter of the task.
 
 The action associated to this method is
 TaskActions.STARTTASKASSUBTASK.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID that is used
    to identify the subtask instance.parentTaskID - A string representation of the task instance ID that identifies
    the parent task instance.input - The input message.
    The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongFormatException
IdWrongTypeException
InvalidApplicationStateException
InvalidLengthException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
ParallelRoutingTaskException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
SubTasksNotSupportedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when starting of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- startTaskAsSubTask
void startTaskAsSubTask(TKIID tkiid,
                      TKIID parentTaskID,
                      ClientObjectWrapper input)
                        throws AdministratorCannotBeResolvedException,
                               ApplicationVetoException,
                               ArchiveUnsupportedOperationException,
                               CannotCreateWorkItemException,
                               IdWrongFormatException,
                               InvalidApplicationStateException,
                               InvalidLengthException,
                               NotAuthorizedException,
                               UserDoesNotExistException,
                               ObjectDoesNotExistException,
                               ParallelRoutingTaskException,
                               SCAServiceAccessFailureException,
                               SCAServiceResultErrorException,
                               SchedulingFailedException,
                               SubTasksNotSupportedException,
                               WrongKindException,
                               WrongMessageTypeException,
                               WrongStateException,
                               UnexpectedFailureException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
Executes a previously created task as a subtask of the specified parent
 task instance using the task instance ID.
 The parent task instance is then waiting for the completion of the subtask. It can only
 be completed when all subtasks came to an end.
 
 The subtask must be a collaboration or stand-alone invocation task. An invocation task
 must have been derived from a task template that has not been created at Runtime. The parent task
 instance must be a collaboration or to-do task in the claimed state.
 It can be escalated or already waiting for a subtask. It can, however, not be suspended.
 
 Collaboration, invocation, and to-do task instances are also known as
 human, originating, and participating task instances.
 
 A subtask can only be
 started when the parent task supports subtask creation - refer to Task to view the
 task instance properties.
 
 The subtask instance must be in the inactive state. When started it will be in the ready
 or running state.
 The caller must be a potential starter, the originator, or an administrator of the subtask
 and an owner or administrator of the parent task instance.
 When the task is an invocation aka originating task instance, then the caller becomes the starter of the task.
 
 The action associated to this method is
 TaskActions.STARTTASKASSUBTASK.
 
 This method is not supported in archive mode.
Parameters:tkiid - The task instance ID that is used to identify the subtask instance.parentTaskID - The task instance ID that identifies the parent task instance.input - The input message.
    The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
AdministratorCannotBeResolvedException
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongFormatException
InvalidApplicationStateException
InvalidLengthException
NotAuthorizedException
UserDoesNotExistException
ObjectDoesNotExistException
ParallelRoutingTaskException
SCAServiceAccessFailureException
SCAServiceResultErrorException
SchedulingFailedException
SubTasksNotSupportedException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when starting of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- startTaskTemplate
void startTaskTemplate(java.lang.String tktid)
                       throws ApplicationVetoException,
                              ArchiveUnsupportedOperationException,
                              IdWrongFormatException,
                              IdWrongTypeException,
                              NotAuthorizedException,
                              ObjectDoesNotExistException,
                              WrongKindException,
                              WrongStateException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
This method starts a task template that has been created at Runtime
 using a string representation of the task template ID.
 When a task template is started instances can be created
 using the task template.
 
 The caller must be an administrator of the task template. The task template must be stopped.
 
 The action associated to this method is
 TaskTemplateActions.STARTTEMPLATE.
 
 This method is not supported in archive mode.
Parameters:tktid - A string representation of the object ID of the task template to be started.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- startTaskTemplate
void startTaskTemplate(TKTID tktid)
                       throws ApplicationVetoException,
                              ArchiveUnsupportedOperationException,
                              IdWrongFormatException,
                              NotAuthorizedException,
                              ObjectDoesNotExistException,
                              WrongKindException,
                              WrongStateException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
This method starts a task template that has been created at Runtime
 using the task template ID.
 When a task template is started instances can be created
 using the task template.
 
 The caller must be an administrator of the task template. The task template must be stopped.
 
 The action associated to this method is
 TaskTemplateActions.STARTTEMPLATE.
 
 This method is not supported in archive mode.
Parameters:tktid - The object ID of the task template which is to be stopped.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- stopTaskTemplate
void stopTaskTemplate(java.lang.String tktid)
                      throws ApplicationVetoException,
                             ArchiveUnsupportedOperationException,
                             IdWrongFormatException,
                             IdWrongTypeException,
                             NotAuthorizedException,
                             ObjectDoesNotExistException,
                             WrongKindException,
                             WrongStateException,
                             UnexpectedFailureException,
                             java.rmi.RemoteException,
                             javax.ejb.EJBException
This method stops a task template that has been created at Runtime
 using a string representation of the task template ID.
 When a task template is in the stopped state no more instances can be created
 using the task template.
 
 The caller must be an administrator of the task template. The task template must be started.
 
 The action associated to this method is
 TaskTemplateActions.STOPTEMPLATE.
 
 This method is not supported in archive mode.
Parameters:tktid - A string representation of the object ID of the task template to be stopped.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- stopTaskTemplate
void stopTaskTemplate(TKTID tktid)
                      throws ApplicationVetoException,
                             ArchiveUnsupportedOperationException,
                             IdWrongFormatException,
                             NotAuthorizedException,
                             ObjectDoesNotExistException,
                             WrongKindException,
                             WrongStateException,
                             UnexpectedFailureException,
                             java.rmi.RemoteException,
                             javax.ejb.EJBException
This method stops a task template that has been created at Runtime
 using the task template ID.
 When a task template is in the stopped state no more instances can be created
 using the task template.
 
 The caller must be an administrator of the task template. The task template must be started.
 
 The action associated to this method is
 TaskTemplateActions.STOPTEMPLATE.
 
 This method is not supported in archive mode.
Parameters:tktid - The object ID of the task template which is to be stopped.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- suspend
void suspend(java.lang.String tkiid)
             throws ApplicationVetoException,
                    ArchiveUnsupportedOperationException,
                    IdWrongFormatException,
                    IdWrongTypeException,
                    NotAuthorizedException,
                    ObjectDoesNotExistException,
                    WrongKindException,
                    WrongStateException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Suspends the specified collaboration or to-do task instance
 using a string representation of the task instance ID.
 Collaboration and to-do task instances are also known as
 human and participating task instances.
 
 The task instance can be in the ready, running, or claimed state. It can be
 escalated or be waiting for subtasks to complete.
 The caller can be the owner, originator, or administrator of the task instance.
 
 Note that escalation timers continue to run.
 
 The action associated to this method is
 TaskActions.SUSPEND.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID to be suspended.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 A task with parallel ownership can be in the running state.

- suspend
void suspend(TKIID tkiid)
             throws ApplicationVetoException,
                    ArchiveUnsupportedOperationException,
                    IdWrongFormatException,
                    NotAuthorizedException,
                    ObjectDoesNotExistException,
                    WrongKindException,
                    WrongStateException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Suspends the specified collaboration or to-do task instance
 using the task instance ID.
 Collaboration and to-do task instances are also known as
 human and participating task instances.
 
 The task instance can be in the ready, running, or claimed state. It can be
 escalated or be waiting for subtasks to complete.
 The caller can be the owner, originator, or administrator of the task instance.
 
 Note that escalation timers continue to run.
 
 The action associated to this method is
 TaskActions.SUSPEND.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID of the task instance to be suspended.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 A task with parallel ownership can be in the running state.

- suspend
void suspend(java.lang.String tkiid,
           java.lang.String duration)
             throws ApplicationVetoException,
                    ArchiveUnsupportedOperationException,
                    IdWrongFormatException,
                    IdWrongTypeException,
                    NotAuthorizedException,
                    ObjectDoesNotExistException,
                    ParameterNullException,
                    WrongKindException,
                    WrongStateException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Suspends the specified collaboration or to-do task instance for the specified
 duration using a string representation of the task instance ID.
 Collaboration and to-do task instances are also known as
 human and participating task instances.
 
 The task instance can be in the ready, running, or claimed state. It can be
 escalated or be waiting for subtasks to complete.
 The caller can be the owner, originator, or administrator of the task instance.
 
 The task is then suspended for the specified duration or until an explicit resume request is issued.
 
 Note that escalation timers continue to run.
 
 The action associated to this method is
 TaskActions.SUSPEND.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID to be suspended.duration - The time for which the task instance is to be suspended. Its format
    depends on the calendar that is used and may, for example, be "5days". When the time
    has passed, the task instance is automatically resumed.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 A task with parallel ownership can be in the running state.

- suspend
void suspend(TKIID tkiid,
           java.lang.String duration)
             throws ApplicationVetoException,
                    ArchiveUnsupportedOperationException,
                    IdWrongFormatException,
                    NotAuthorizedException,
                    ObjectDoesNotExistException,
                    ParameterNullException,
                    WrongKindException,
                    WrongStateException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Suspends the specified collaboration or to-do task instance for the specified
 duration using the task instance ID.
 Collaboration and to-do task instances are also known as
 human and participating task instances.
 
 The task instance can be in the ready, running, or claimed state. It can be
 escalated or be waiting for subtasks to complete.
 The caller can be the owner, originator, or administrator of the task instance.
 
 The task is then suspended for the specified duration or until an explicit resume request is issued.
 
 Note that escalation timers continue to run.
 
 The action associated to this method is
 TaskActions.SUSPEND.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID of the task instance to be suspended.duration - The time for which the task instance is to be suspended. Its format
    depends on the calendar that is used and may, for example, be "5days". When the time
    has passed, the task instance is automatically resumed.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 A task with parallel ownership can be in the running state.

- suspend
void suspend(java.lang.String tkiid,
           int duration)
             throws ApplicationVetoException,
                    ArchiveUnsupportedOperationException,
                    IdWrongFormatException,
                    IdWrongTypeException,
                    InvalidParameterException,
                    NotAuthorizedException,
                    ObjectDoesNotExistException,
                    WrongKindException,
                    WrongStateException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Suspends the specified collaboration or to-do task instance for the specified
 number of seconds using a string representation of the task instance ID.
 Collaboration and to-do task instances are also known as
 human and participating task instances.
 
 The task instance can be in the ready, running, or claimed state. It can be
 escalated or be waiting for subtasks to complete.
 The caller can be the owner, originator, or administrator of the task instance.
 
 The task is then suspended for the specified duration or until an explicit resume request is issued.
 
 Note that escalation timers continue to run.
 
 The action associated to this method is
 TaskActions.SUSPEND.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID to be suspended.duration - The seconds for which the task instance is to be suspended. When the time
    has passed, the task instance is automatically resumed.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
InvalidParameterException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 A task with parallel ownership can be in the running state.

- suspend
void suspend(TKIID tkiid,
           int duration)
             throws ApplicationVetoException,
                    ArchiveUnsupportedOperationException,
                    IdWrongFormatException,
                    InvalidParameterException,
                    NotAuthorizedException,
                    ObjectDoesNotExistException,
                    WrongKindException,
                    WrongStateException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Suspends the specified collaboration or to-do task instance for the specified
 number of seconds using the task instance ID.
 Collaboration and to-do task instances are also known as
 human and participating task instances.
 
 The task instance can be in the ready, running, or claimed state. It can be
 escalated or be waiting for subtasks to complete.
 The caller can be the owner, originator, or administrator of the task instance.
 
 The task is then suspended for the specified duration or until an explicit resume request is issued.
 
 Note that escalation timers continue to run.
 
 The action associated to this method is
 TaskActions.SUSPEND.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID of the task instance to be suspended.duration - The seconds for which the task instance is to be suspended. When the time
    has passed, the task instance is automatically resumed.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
InvalidParameterException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 A task with parallel ownership can be in the running state.

- suspend
void suspend(java.lang.String tkiid,
           java.util.Calendar deadline)
             throws ApplicationVetoException,
                    ArchiveUnsupportedOperationException,
                    IdWrongFormatException,
                    IdWrongTypeException,
                    NotAuthorizedException,
                    ObjectDoesNotExistException,
                    ParameterNullException,
                    WrongKindException,
                    WrongStateException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Suspends the specified collaboration or to-do task instance
 until the specified point in time is reached using a string representation of the task instance ID.
 Collaboration and to-do task instances are also known as
 human and participating task instances.
 
 The task instance can be in the ready, running, or claimed state. It can be
 escalated or be waiting for subtasks to complete.
 The caller can be the owner, originator, or administrator of the task instance.
 
 The task is then suspended until the specified point in time or until an explicit resume request is issued.
 
 Note that escalation timers continue to run.
 
 The action associated to this method is
 TaskActions.SUSPEND.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance to be suspended.deadline - The time up to which the task instance is to be suspended. When the specified
    time has been reached, the task instance is automatically resumed.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 A task with parallel ownership can be in the running state.

- suspend
void suspend(TKIID tkiid,
           java.util.Calendar deadline)
             throws ApplicationVetoException,
                    ArchiveUnsupportedOperationException,
                    IdWrongFormatException,
                    NotAuthorizedException,
                    ObjectDoesNotExistException,
                    ParameterNullException,
                    WrongKindException,
                    WrongStateException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Suspends the specified collaboration or to-do task instance
 until the specified point in time is reached using the task instance ID.
 Collaboration and to-do task instances are also known as
 human and participating task instances.
 
 The task instance can be in the ready, running, or claimed state. It can be
 escalated or be waiting for subtasks to complete.
 The caller can be the owner, originator, or administrator of the task instance.
 
 The task is then suspended until the specified point in time or until an explicit resume request is issued.
 
 Note that escalation timers continue to run.
 
 The action associated to this method is
 TaskActions.SUSPEND.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID of the task instance to be suspended.deadline - The time up to which the task instance is to be suspended. When the specified
    time has been reached, the task instance is automatically resumed.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 A task with parallel ownership can be in the running state.

- suspendAndCancelClaim
void suspendAndCancelClaim(java.lang.String tkiid,
                         java.lang.String duration,
                         boolean keepTaskData)
                           throws ApplicationVetoException,
                                  ArchiveUnsupportedOperationException,
                                  IdWrongFormatException,
                                  IdWrongTypeException,
                                  NotAuthorizedException,
                                  ObjectDoesNotExistException,
                                  ParameterNullException,
                                  WrongKindException,
                                  WrongStateException,
                                  UnexpectedFailureException,
                                  java.rmi.RemoteException,
                                  javax.ejb.EJBException
Suspends the specified collaboration or to-do task instance for the specified
 duration and cancels the claim of the task instance when execution is resumed
 using a string representation of the task instance ID.
 Collaboration and to-do task instances are also known as
 human and participating task instances.
 
 The task instance must be in the claimed state.
 It can be escalated but not waiting for subtasks to complete.
 It cannot be a task with parallel ownership. A task with parallel ownership
 is not claimed and does not have an owner,
 
 When the task instance is automatically
 resumed after the duration passed, it is returned to the ready state. When the
 task instance is resumed on request before the duration has passed, then the task
 instance remains claimed.
 
 If specified, any previously stored output or fault message is kept.
 
 The caller can be the owner or administrator of the task instance.
 
 The action associated to this method is
 TaskActions.SUSPENDWITHCANCELCLAIM.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID to be suspended.duration - The time for which the task instance is to be suspended. Its format
    depends on the calendar that is used and may, for example, be "5days". When the time
    has passed, the task instance is automatically resumed.keepTaskData - Specifies whether data saved for the claimed task instance is to be kept.
    True states that any output or fault message set is to be kept.
    False states that any output or fault message set is to be deleted.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- suspendAndCancelClaim
void suspendAndCancelClaim(TKIID tkiid,
                         java.lang.String duration,
                         boolean keepTaskData)
                           throws ApplicationVetoException,
                                  ArchiveUnsupportedOperationException,
                                  IdWrongFormatException,
                                  NotAuthorizedException,
                                  ObjectDoesNotExistException,
                                  ParameterNullException,
                                  WrongKindException,
                                  WrongStateException,
                                  UnexpectedFailureException,
                                  java.rmi.RemoteException,
                                  javax.ejb.EJBException
Suspends the specified collaboration or to-do task instance for the specified
 duration and cancels the claim of the task instance when execution is resumed
 using the task instance ID.
 Collaboration and to-do task instances are also known as
 human and participating task instances.
 
 The task instance must be in the claimed state.
 It can be escalated but not waiting for subtasks to complete.
 It cannot be a task with parallel ownership. A task with parallel ownership
 is not claimed and does not have an owner,
 
 When the task instance is automatically
 resumed after the duration passed, it is returned to the ready state. When the
 task instance is resumed on request before the duration has passed, then the task
 instance remains claimed.
 
 If specified, any previously stored output or fault message is kept.
 
 The caller can be the owner or administrator of the task instance.
 
 The action associated to this method is
 TaskActions.SUSPENDWITHCANCELCLAIM.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID of the task instance to be suspended.duration - The time for which the task instance is to be suspended. Its format
    depends on the calendar that is used and may, for example, be "5days". When the time
    has passed, the task instance is automatically resumed.keepTaskData - Specifies whether data saved for the claimed task instance is to be kept.
    True states that any output or fault message set is to be kept.
    False states that any output or fault message set is to be deleted.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- suspendAndCancelClaim
void suspendAndCancelClaim(java.lang.String tkiid,
                         int duration,
                         boolean keepTaskData)
                           throws ApplicationVetoException,
                                  ArchiveUnsupportedOperationException,
                                  IdWrongFormatException,
                                  IdWrongTypeException,
                                  InvalidParameterException,
                                  NotAuthorizedException,
                                  ObjectDoesNotExistException,
                                  WrongKindException,
                                  WrongStateException,
                                  UnexpectedFailureException,
                                  java.rmi.RemoteException,
                                  javax.ejb.EJBException
Suspends the specified collaboration or to-do task instance for the specified
 number of seconds and cancels the claim of the task instance when execution is resumed
 using a string representation of the task instance ID.
 Collaboration and to-do task instances are also known as
 human and participating task instances.
 
 The task instance must be in the claimed state.
 It can be escalated but not waiting for subtasks to complete.
 It cannot be a task with parallel ownership. A task with parallel ownership
 is not claimed and does not have an owner,
 
 When the task instance is automatically
 resumed after the duration passed, it is returned to the ready state. When the
 task instance is resumed on request before the duration has passed, then the task
 instance remains claimed.
 
 If specified, any previously stored output or fault message is kept.
 
 The caller can be the owner or administrator of the task instance.
 
 The action associated to this method is
 TaskActions.SUSPENDWITHCANCELCLAIM.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID to be suspended.duration - The seconds for which the task instance is to be suspended. When the time
    has passed, the task instance is automatically resumed.keepTaskData - Specifies whether data saved for the claimed task instance is to be kept.
    True states that any output or fault message set is to be kept.
    False states that any output or fault message set is to be deleted.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
InvalidParameterException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- suspendAndCancelClaim
void suspendAndCancelClaim(TKIID tkiid,
                         int duration,
                         boolean keepTaskData)
                           throws ApplicationVetoException,
                                  ArchiveUnsupportedOperationException,
                                  IdWrongFormatException,
                                  InvalidParameterException,
                                  NotAuthorizedException,
                                  ObjectDoesNotExistException,
                                  WrongKindException,
                                  WrongStateException,
                                  UnexpectedFailureException,
                                  java.rmi.RemoteException,
                                  javax.ejb.EJBException
Suspends the specified collaboration or to-do task instance for the specified
 number of seconds and cancels the claim of the task instance when execution is resumed
 using the task instance ID.
 
 The task instance must be in the claimed state. It can be
 escalated or be waiting for subtasks to complete. When the task instance is automatically
 resumed after the duration passed, it is returned to the ready state. When the
 task instance is resumed on request before the duration has passed, then the task
 instance remains claimed.
 
 If specified, any previously stored output or fault message is kept.
 
 The caller can be the owner or administrator of the task instance.
 
 The action associated to this method is
 TaskActions.SUSPENDWITHCANCELCLAIM.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID of the task instance to be suspended.duration - The seconds for which the task instance is to be suspended. When the time
    has passed, the task instance is automatically resumed.keepTaskData - Specifies whether data saved for the claimed task instance is to be kept.
    True states that any output or fault message set is to be kept.
    False states that any output or fault message set is to be deleted.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
InvalidParameterException
NotAuthorizedException
ObjectDoesNotExistException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- suspendAndCancelClaim
void suspendAndCancelClaim(java.lang.String tkiid,
                         java.util.Calendar deadline,
                         boolean keepTaskData)
                           throws ApplicationVetoException,
                                  ArchiveUnsupportedOperationException,
                                  IdWrongFormatException,
                                  IdWrongTypeException,
                                  NotAuthorizedException,
                                  ObjectDoesNotExistException,
                                  ParameterNullException,
                                  WrongKindException,
                                  WrongStateException,
                                  UnexpectedFailureException,
                                  java.rmi.RemoteException,
                                  javax.ejb.EJBException
Suspends the specified collaboration or to-do task instance
 until the specified point in time is reached,
 and cancels the claim of the task instance when execution is resumed
 using a string representation of the task instance ID.
 Collaboration and to-do task instances are also known as
 human and participating task instances.
 
 The task instance must be in the claimed state.
 It can be escalated but not waiting for subtasks to complete.
 It cannot be a task with parallel ownership. A task with parallel ownership
 is not claimed and does not have an owner,
 
 When the task instance is automatically
 resumed after the duration passed, it is returned to the ready state. When the
 task instance is resumed on request before the duration has passed, then the task
 instance remains claimed.
 
 If specified, any previously stored output or fault message is kept.
 
 The caller can be the owner or administrator of the task instance.
 
 The action associated to this method is
 TaskActions.SUSPENDWITHCANCELCLAIM.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID to be suspended.deadline - The time up to which the task instance is to be suspended. When the specified
    time has been reached, the task instance is automatically resumed and returned to
    the ready state.keepTaskData - Specifies whether data saved for the claimed task instance is to be kept.
    True states that any output or fault message set is to be kept.
    False states that any output or fault message set is to be deleted.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- suspendAndCancelClaim
void suspendAndCancelClaim(TKIID tkiid,
                         java.util.Calendar deadline,
                         boolean keepTaskData)
                           throws ApplicationVetoException,
                                  ArchiveUnsupportedOperationException,
                                  IdWrongFormatException,
                                  NotAuthorizedException,
                                  ObjectDoesNotExistException,
                                  ParameterNullException,
                                  WrongKindException,
                                  WrongStateException,
                                  UnexpectedFailureException,
                                  java.rmi.RemoteException,
                                  javax.ejb.EJBException
Suspends the specified collaboration or to-do task instance
 until the specified point in time is reached,
 and cancels the claim of the task instance when execution is resumed
 using the task instance ID.
 
 The task instance must be in the claimed state.
 It can be escalated but not waiting for subtasks to complete.
 It cannot be a task with parallel ownership. A task with parallel ownership
 is not claimed and does not have an owner,
 
 When the task instance is automatically
 resumed after the duration passed, it is returned to the ready state. When the
 task instance is resumed on request before the duration has passed, then the task
 instance remains claimed.
 
 If specified, any previously stored output or fault message is kept.
 
 The caller can be the owner or administrator of the task instance.
 
 The action associated to this method is
 TaskActions.SUSPENDWITHCANCELCLAIM.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID of the task instance to be suspended.deadline - The time up to which the task instance is to be suspended. When the specified
    time has been reached, the task instance is automatically resumed and returned to the
    ready state.keepTaskData - Specifies whether data saved for the claimed task instance is to be kept.
    True states that any output or fault message set is to be kept.
    False states that any output or fault message set is to be deleted.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- terminate
void terminate(java.lang.String tkiid)
               throws ApplicationVetoException,
                      ArchiveUnsupportedOperationException,
                      IdWrongFormatException,
                      IdWrongTypeException,
                      NotAuthorizedException,
                      ObjectDoesNotExistException,
                      ParallelRoutingTaskException,
                      SchedulingFailedException,
                      WrongKindException,
                      WrongStateException,
                      UnexpectedFailureException,
                      java.rmi.RemoteException,
                      javax.ejb.EJBException
Terminates the specified task instance using
 a string representation of the task instance ID.
 Terminating an invocation aka originating task instance has no impact on the invoked service.
 
 The task instance can be in the ready, claimed, or running state. It can be
 escalated, suspended, or waiting for subtasks.
 It cannot be an inline task or a stand-alone task with "child" autonomy.
 The caller can be the owner, starter, originator, or administrator of the task instance.
 
 The action associated to this method is
 TaskActions.TERMINATE.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the object ID of the task instance to be terminated.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
ParallelRoutingTaskException
SchedulingFailedException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when completion of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- terminate
void terminate(TKIID tkiid)
               throws ApplicationVetoException,
                      ArchiveUnsupportedOperationException,
                      IdWrongFormatException,
                      NotAuthorizedException,
                      ObjectDoesNotExistException,
                      ParallelRoutingTaskException,
                      SchedulingFailedException,
                      WrongKindException,
                      WrongStateException,
                      UnexpectedFailureException,
                      java.rmi.RemoteException,
                      javax.ejb.EJBException
Terminates the specified task instance using the task instance ID.
 Terminating an invocation aka originating task instance has no impact on the invoked service.
 
 The task instance can be in the ready, claimed, or running state. It can be
 escalated, suspended, or waiting for subtasks.
 It cannot be an inline task or a stand-alone task with "child" autonomy.
 The caller can be the owner, starter, originator, or administrator of the task instance.
 
 The action associated to this method is
 TaskActions.TERMINATE.
 
 This method is not supported in archive mode.
Parameters:tkiid - The object ID of the task instance to be terminated.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
ParallelRoutingTaskException
SchedulingFailedException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws a ParallelRoutingTaskException when completion of a parallel routing task failed.
 
7.0
 
 Throws a SchedulingFailedException when scheduling the task failed.

- transferToWorkBasket java.util.List transferToWorkBasket(java.lang.String[] tkiids, java.lang.String workBasketName) throws ArchiveUnsupportedOperationException , IdWrongFormatException , IdWrongTypeException , InvalidLengthException , InvalidParameterException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Transfers the specified task instances to the specified work basket using string representations of the task instance IDs. The caller must be an owner, starter, originator, editor, or administrator of the task instance. All tasks are marked unread. The isTransferredToWorkBasket property is set to true. All transfer operations are executed within the current transaction. If a transaction timeout occurs, then all already executed transfer operations are rolled back. The action associated to this method is TaskActions.TRANSFERTOWORKBASKET . This method is not supported in archive mode. Parameters: tkiids - An array of task instance IDs that are used to identify the tasks to be transferred. workBasketName - The name of the work basket the tasks are to be transferred to. The work basket name must not contain any replacement variables. Returns: List - A list of TaskResult objects, one for every task instance specified. Refer to TaskResult . If a single transfer operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all transfer operations are undone. Throws: ArchiveUnsupportedOperationException IdWrongFormatException IdWrongTypeException InvalidLengthException InvalidParameterException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.2.0.2 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode. 7.0 Throws an InvalidParameterException when the work basket name contains replacement variables. 7.0.0.2 May return a TaskNotInWorkBasketException or a WrongTaskStateException in the list of TaskResult's.

#### transferToWorkBasket

```
java.util.List transferToWorkBasket(java.lang.String[] tkiids,
                                  java.lang.String workBasketName)
                                    throws ArchiveUnsupportedOperationException,
                                           IdWrongFormatException,
                                           IdWrongTypeException,
                                           InvalidLengthException,
                                           InvalidParameterException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
```

All tasks are marked unread. The isTransferredToWorkBasket property is set to true.
 
 All transfer operations are executed within the current transaction.
 If a transaction timeout occurs, then all already executed transfer operations are rolled back.
 
 The action associated to this method is
 TaskActions.TRANSFERTOWORKBASKET.
 
 This method is not supported in archive mode.

If a single transfer operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.ObjectDoesNotExistException
 com.ibm.task.api.TaskNotInWorkBasketException
 com.ibm.task.api.WrongTaskStateException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all transfer operations are undone.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws an InvalidParameterException when the work basket name contains replacement variables.
 
7.0.0.2
 
 May return a TaskNotInWorkBasketException or a WrongTaskStateException
 in the list of TaskResult's.

- transferToWorkBasket java.util.List transferToWorkBasket(TKIID [] tkiids, java.lang.String workBasketName) throws ArchiveUnsupportedOperationException , IdWrongFormatException , InvalidLengthException , InvalidParameterException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Transfers the specified task instances to the specified work basket using task instance IDs. The caller must be an owner, starter, originator, editor, or administrator of the task instance. All tasks are marked unread. The isTransferredToWorkBasket property is set to true. All transfer operations are executed within the current transaction. If a transaction timeout occurs, then all already executed transfer operations are rolled back. The action associated to this method is TaskActions.TRANSFERTOWORKBASKET . This method is not supported in archive mode. Parameters: tkiids - An array of task instance IDs that are used to identify the tasks to be transferred. workBasketName - The name of the work basket the tasks are to be transferred to. The work basket name must not contain any replacement variables. Returns: List - A list of TaskResult objects, one for every task instance specified. Refer to TaskResult . If a single transfer operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all transfer operations are undone. Throws: ArchiveUnsupportedOperationException IdWrongFormatException InvalidLengthException InvalidParameterException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.2.0.2 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode. 7.0 Throws an InvalidParameterException when the work basket name contains replacement variables. 7.0.0.2 May return a TaskNotInWorkBasketException or a WrongTaskStateException in the list of TaskResult's.

#### transferToWorkBasket

```
java.util.List transferToWorkBasket(TKIID[] tkiids,
                                  java.lang.String workBasketName)
                                    throws ArchiveUnsupportedOperationException,
                                           IdWrongFormatException,
                                           InvalidLengthException,
                                           InvalidParameterException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
```

All tasks are marked unread. The isTransferredToWorkBasket property is set to true.
 
 All transfer operations are executed within the current transaction.
 If a transaction timeout occurs, then all already executed transfer operations are rolled back.
 
 The action associated to this method is
 TaskActions.TRANSFERTOWORKBASKET.
 
 This method is not supported in archive mode.

If a single transfer operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.ObjectDoesNotExistException
 com.ibm.task.api.TaskNotInWorkBasketException
 com.ibm.task.api.WrongTaskStateException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all transfer operations are undone.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws an InvalidParameterException when the work basket name contains replacement variables.
 
7.0.0.2
 
 May return a TaskNotInWorkBasketException or a WrongTaskStateException
 in the list of TaskResult's.

- transferWorkItem void transferWorkItem(java.lang.String identifier, int assignmentReason, java.lang.String fromOwner, java.lang.String toOwner) throws ApplicationVetoException , ArchiveUnsupportedOperationException , EverybodyWorkItemException , IdWrongFormatException , IdWrongTypeException , InvalidAssignmentReasonException , InvalidLengthException , NotAuthorizedException , UserDoesNotExistException , WorkItemDoesNotExistException , ObjectDoesNotExistException , ParameterNullException , TaskDelegationNotSupportedException , WorkItemManagerException , WrongKindException , WrongStateException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Transfers the specified work item using a string representation of the task or escalation instance ID. When work items of a task instance are transferred, then the caller must be an owner, starter, originator, or administrator of the task instance. The task can be escalated. suspended, or waiting for subtasks. When work items of an escalation instance are transferred, then the caller must be an administrator of the associated task instance. "Escalation receiver" work items can be transferred when the task is escalated, that is, the escalation is in the escalated state. An e-mail is not sent to the user or group that receives the transferred work item. The following specific rules apply for the transfer of work items: The action associated to this method is TaskActions.TRANSFERWORKITEM or EscalationActions.TRANSFERWORKITEM . This method is not supported in archive mode. Parameters: identifier - A string representation of the task or escalation instance ID that is used to identify the work item to be transferred. assignmentReason - The reason why the work item is assigned - refer to the work item assignment reasons . fromOwner - The user ID or the name of the group the work item currently belongs to. toOwner - The user ID or the name of the group the work item is to be transferred to. Work items can be transferred from a user to a user or from a group of users to a group of users. If a user work item is transferred, it is checked whether the user transferred to exists but the check may be executed case insensitively. The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments' custom property of the Human Task Manager configuration to 'true'. Throws: ApplicationVetoException ArchiveUnsupportedOperationException EverybodyWorkItemException IdWrongFormatException IdWrongTypeException InvalidAssignmentReasonException InvalidLengthException NotAuthorizedException UserDoesNotExistException WorkItemDoesNotExistException ObjectDoesNotExistException ParameterNullException TaskDelegationNotSupportedException WorkItemManagerException WrongKindException WrongStateException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 5.1.1 Change History Release Modification 6.0.2 Supports escalation instances. 6.0.2 Throws a TaskDelegationNotSupportedException when task delegation is not supported. 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### transferWorkItem

```
void transferWorkItem(java.lang.String identifier,
                    int assignmentReason,
                    java.lang.String fromOwner,
                    java.lang.String toOwner)
                      throws ApplicationVetoException,
                             ArchiveUnsupportedOperationException,
                             EverybodyWorkItemException,
                             IdWrongFormatException,
                             IdWrongTypeException,
                             InvalidAssignmentReasonException,
                             InvalidLengthException,
                             NotAuthorizedException,
                             UserDoesNotExistException,
                             WorkItemDoesNotExistException,
                             ObjectDoesNotExistException,
                             ParameterNullException,
                             TaskDelegationNotSupportedException,
                             WorkItemManagerException,
                             WrongKindException,
                             WrongStateException,
                             UnexpectedFailureException,
                             java.rmi.RemoteException,
                             javax.ejb.EJBException
```

When work items of a task instance are transferred, then
 the caller must be an owner, starter, originator, or administrator of the task instance.
 The task can be escalated. suspended, or waiting for subtasks.
 
 When work items of an escalation instance are transferred, then
 the caller must be an administrator of the associated task instance.
 "Escalation receiver" work items can be transferred
 when the task is escalated, that is, the escalation is in the escalated state.
 An e-mail is not sent to the user or group that receives the transferred work item.
 
 The following specific rules apply for the transfer of work items:
 
Work items assigned to "everybody" cannot be transferred.
 The owner of a task instance can transfer the "owner" work item to a potential owner
 or an administrator of the task instance.
 The starter of a task instance can transfer the "starter" work item to a potential starter
 or an administrator of the task instance.
 A "starter" work item can be transferred in the expired, terminated, finished, failed, and running state.
 The originator of a task instance can transfer the "originator" work item to a potential instance creator
 or an administrator of the task instance.
 The originator of a task instance can transfer a "potential starter" work item to any person.
 A "potential starter" work item can be transferred in the inactive state.
 The administrator of a task instance can transfer all work items to any person.
 A "starter" work item can be transferred in the expired, terminated, finished, failed, and running state.
 A "potential starter" work item can be transferred in the inactive state.
 A "reader" or "administrator" work items can be transferred in all but the inactive state.
 A "potential owner" or "editor" work item can be transferred in the ready or claimed state.
 An "escalation receiver" work item can be transferred in the ready, running, or claimed state.
 

 The action associated to this method is TaskActions.TRANSFERWORKITEM or
 EscalationActions.TRANSFERWORKITEM.
 
 This method is not supported in archive mode.

Change History

Release
 Modification
 
6.0.2
 
 Supports escalation instances.
 
6.0.2
 
 Throws a TaskDelegationNotSupportedException when task delegation is not supported.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- transferWorkItem
void transferWorkItem(ESIID esiid,
                    int assignmentReason,
                    java.lang.String fromOwner,
                    java.lang.String toOwner)
                      throws ApplicationVetoException,
                             ArchiveUnsupportedOperationException,
                             EverybodyWorkItemException,
                             IdWrongFormatException,
                             InvalidAssignmentReasonException,
                             InvalidLengthException,
                             NotAuthorizedException,
                             UserDoesNotExistException,
                             WorkItemDoesNotExistException,
                             ObjectDoesNotExistException,
                             ParameterNullException,
                             TaskDelegationNotSupportedException,
                             WorkItemManagerException,
                             WrongKindException,
                             WrongStateException,
                             UnexpectedFailureException,
                             java.rmi.RemoteException,
                             javax.ejb.EJBException
Transfers the specified work item for the specified escalation instance
 using the escalation instance ID.
 
 The caller must be an administrator of the associated task instance.
 "Escalation receiver" work items can be transferred when the task is escalated,
 that is, the escalation is in the escalated state.
 An e-mail is not sent to the user or group that receives the transferred work item.
 
 The action associated to this method is
 EscalationActions.TRANSFERWORKITEM.
 
 This method is not supported in archive mode.
Parameters:esiid - The escalation instance ID that is used to identify
    the work item to be transferred.assignmentReason - The reason why the work item is assigned - refer to
     the work item assignment reasons.fromOwner - The user ID or the name of the group the work item currently belongs to.toOwner - The user ID or the name of the group the work item is to be transferred to.
    Work items can be transferred from a user to a user or from a group of users to a group of users.
    If a user work item is transferred, it is checked whether the user transferred to
    exists but the check may be executed case insensitively.
    The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments'
    custom property of the Human Task Manager configuration to 'true'.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EverybodyWorkItemException
IdWrongFormatException
InvalidAssignmentReasonException
InvalidLengthException
NotAuthorizedException
UserDoesNotExistException
WorkItemDoesNotExistException
ObjectDoesNotExistException
ParameterNullException
TaskDelegationNotSupportedException
WorkItemManagerException
WrongKindException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- transferWorkItem void transferWorkItem(TKIID tkiid, int assignmentReason, java.lang.String fromOwner, java.lang.String toOwner) throws ApplicationVetoException , ArchiveUnsupportedOperationException , EverybodyWorkItemException , IdWrongFormatException , InvalidAssignmentReasonException , InvalidLengthException , NotAuthorizedException , UserDoesNotExistException , WorkItemDoesNotExistException , ObjectDoesNotExistException , ParameterNullException , TaskDelegationNotSupportedException , WorkItemManagerException , WrongKindException , WrongStateException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Transfers the specified work item for the specified task instance using the task instance ID. The caller must be an owner, starter, originator, or administrator of the task instance. The task can be escalated. suspended, or waiting for subtasks. The following specific rules apply for the transfer of work items: The action associated to this method is TaskActions.TRANSFERWORKITEM . This method is not supported in archive mode. Parameters: tkiid - The task instance ID that is used to identify the work item to be transferred. assignmentReason - The reason why the work item is assigned - refer to the work item assignment reasons . fromOwner - The user ID or the name of the group the work item currently belongs to. toOwner - The user ID or the name of the group the work item is to be transferred to. Work items can be transferred from a user to a user or from a group of users to a group of users. If a user work item is transferred, it is checked whether the user transferred to exists but the check may be executed case insensitively. The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments' custom property of the Human Task Manager configuration to 'true'. Throws: ApplicationVetoException ArchiveUnsupportedOperationException EverybodyWorkItemException IdWrongFormatException InvalidAssignmentReasonException InvalidLengthException NotAuthorizedException UserDoesNotExistException WorkItemDoesNotExistException ObjectDoesNotExistException ParameterNullException TaskDelegationNotSupportedException WorkItemManagerException WrongKindException WrongStateException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 5.1.1 Change History Release Modification 6.0.2 Throws a TaskDelegationNotSupportedException when task delegation is not supported. 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### transferWorkItem

```
void transferWorkItem(TKIID tkiid,
                    int assignmentReason,
                    java.lang.String fromOwner,
                    java.lang.String toOwner)
                      throws ApplicationVetoException,
                             ArchiveUnsupportedOperationException,
                             EverybodyWorkItemException,
                             IdWrongFormatException,
                             InvalidAssignmentReasonException,
                             InvalidLengthException,
                             NotAuthorizedException,
                             UserDoesNotExistException,
                             WorkItemDoesNotExistException,
                             ObjectDoesNotExistException,
                             ParameterNullException,
                             TaskDelegationNotSupportedException,
                             WorkItemManagerException,
                             WrongKindException,
                             WrongStateException,
                             UnexpectedFailureException,
                             java.rmi.RemoteException,
                             javax.ejb.EJBException
```

The caller must be an owner, starter, originator, or administrator of the task instance.
 The task can be escalated. suspended, or waiting for subtasks.
 
 The following specific rules apply for the transfer of work items:
 
Work items assigned to "everybody" cannot be transferred.
 The owner of a task instance can transfer the "owner" work item to a potential owner
 or an administrator of the task instance.
 The starter of a task instance can transfer the "starter" work item to a potential starter
 or an administrator of the task instance.
 A "starter" work item can be transferred in the expired, terminated, finished, failed, and running state.
 The originator of a task instance can transfer the "originator" work item to a potential instance creator
 or an administrator of the task instance.
 The originator of a task instance can transfer a "potential starter" work item to any person.
 A "potential starter" work item can be transferred in the inactive state.
 The administrator of a task instance can transfer all work items to any person.
 A "starter" work item can be transferred in the expired, terminated, finished, failed, and running state.
 A "potential starter" work item can be transferred in the inactive state.
 A "reader" or "administrator" work item can be transferred in all but the inactive state.
 A "potential owner" or "editor" work item can be transferred in the ready or claimed state.
 

 The action associated to this method is TaskActions.TRANSFERWORKITEM.
 
 This method is not supported in archive mode.

Change History

Release
 Modification
 
6.0.2
 
 Throws a TaskDelegationNotSupportedException when task delegation is not supported.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- transferWorkItem java.util.List transferWorkItem(java.lang.String[] identifiers, int assignmentReason, java.lang.String fromOwner, java.lang.String toOwner) throws ArchiveUnsupportedOperationException , IdWrongFormatException , IdWrongTypeException , InvalidAssignmentReasonException , InvalidLengthException , ParameterNullException , WorkItemNotFoundException , WorkItemManagerException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Transfers the specified work items for the specified escalation or task instances using string representations of escalation or task instance IDs. Note: All transfer work item operations are executed within the current transaction. If a transaction timeout occurs, then all already executed transfer operations are rolled back. Because of this, you may consider to use bulkTransferWorkItem . When work items of a task instance are transferred, then the caller must be an owner, starter, originator, or administrator of the task instances. The task can be escalated. suspended, or waiting for subtasks. When work items of an escalation instance are transferred, then the caller must be an administrator of the associated task instances. "Escalation receiver" work items can be transferred when the task is escalated, that is, the escalation is in the escalated state. An e-mail is not sent to the user or group that receives the transferred work item. The following specific rules apply for the transfer of work items: The action associated to this method is TaskActions.TRANSFERWORKITEM or EscalationActions.TRANSFERWORKITEM . This method is not supported in archive mode. Parameters: identifiers - An array of either escalation instance IDs or task instance IDs that are used to identify the work items to be transferred. assignmentReason - The reason why the work item is assigned - refer to the work item assignment reasons . fromOwner - The user ID or the name of the group the work item currently belongs to. toOwner - The user ID or the name of the group the work item is to be transferred to. Work items can be transferred from a user to a user or from a group of users to a group of users. If a user work item is transferred, it is checked whether the user transferred to exists but the check may be executed case insensitively. The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments' custom property of the Human Task Manager configuration to 'true'. Returns: List - A list of EscalationResult or TaskResult objects, one for every escalation or task instance specified. Refer to EscalationResult or to TaskResult . If a single transfer operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all transfer operations are undone. Throws: ArchiveUnsupportedOperationException IdWrongFormatException IdWrongTypeException InvalidAssignmentReasonException InvalidLengthException ParameterNullException WorkItemNotFoundException WorkItemManagerException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.1 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### transferWorkItem

```
java.util.List transferWorkItem(java.lang.String[] identifiers,
                              int assignmentReason,
                              java.lang.String fromOwner,
                              java.lang.String toOwner)
                                throws ArchiveUnsupportedOperationException,
                                       IdWrongFormatException,
                                       IdWrongTypeException,
                                       InvalidAssignmentReasonException,
                                       InvalidLengthException,
                                       ParameterNullException,
                                       WorkItemNotFoundException,
                                       WorkItemManagerException,
                                       UnexpectedFailureException,
                                       java.rmi.RemoteException,
                                       javax.ejb.EJBException
```

Note: 
 All transfer work item operations are executed within the current transaction.
 If a transaction timeout occurs, then all already executed transfer operations are rolled back.
 Because of this, you may consider to use
 bulkTransferWorkItem.
 
 When work items of a task instance are transferred, then
 the caller must be an owner, starter, originator, or administrator of the task instances.
 The task can be escalated. suspended, or waiting for subtasks.
 
 When work items of an escalation instance are transferred, then
 the caller must be an administrator of the associated task instances.
 "Escalation receiver" work items can be transferred
 when the task is escalated, that is, the escalation is in the escalated state.
 An e-mail is not sent to the user or group that receives the transferred work item.
 
 The following specific rules apply for the transfer of work items:
 
Work items assigned to "everybody" cannot be transferred.
 The owner of a task instance can transfer the "owner" work item to a potential owner
 or an administrator of the task instance.
 The starter of a task instance can transfer the "starter" work item to a potential starter
 or an administrator of the task instance.
 A "starter" work item can be transferred in the expired, terminated, finished, failed, and running state.
 The originator of a task instance can transfer the "originator" work item to a potential instance creator
 or an administrator of the task instance.
 The originator of a task instance can transfer a "potential starter" work item to any person.
 A "potential starter" work item can be transferred in the inactive state.
 The administrator of a task instance can transfer all work items to any person.
 A "starter" work item can be transferred in the expired, terminated, finished, failed, and running state.
 A "potential starter" work item can be transferred in the inactive state.
 A "reader" or "administrator" work items can be transferred in all but the inactive state.
 A "potential owner" or "editor" work item can be transferred in the ready or claimed state.
 An "escalation receiver" work item can be transferred in the ready, running, or claimed state.
 

 The action associated to this method is TaskActions.TRANSFERWORKITEM or
 EscalationActions.TRANSFERWORKITEM.
 
 This method is not supported in archive mode.

If a single transfer operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.UserDoesNotExistException
 com.ibm.task.api.ObjectDoesNotExistException
 com.ibm.task.api.TaskDelegationNotSupportedException
 com.ibm.task.api.WrongKindException
 com.ibm.task.api.WrongStateException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all transfer operations are undone.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- transferWorkItem java.util.List transferWorkItem(ESIID [] esiids, int assignmentReason, java.lang.String fromOwner, java.lang.String toOwner) throws ArchiveUnsupportedOperationException , IdWrongFormatException , InvalidAssignmentReasonException , InvalidLengthException , ParameterNullException , WorkItemNotFoundException , WorkItemManagerException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Transfers the specified work items for the specified escalation instances using escalation instance IDs. Note: All transfer work item operations are executed within the current transaction. If a transaction timeout occurs, then all already executed transfer operations are rolled back. Because of this, you may consider to use bulkTransferWorkItem . The caller must be an administrator of the associated task instances. "Escalation receiver" work items can be transferred when the task is escalated, that is, the escalation is in the escalated state. An e-mail is not sent to the user or group that receives the transferred work item. The action associated to this method is EscalationActions.TRANSFERWORKITEM . This method is not supported in archive mode. Parameters: esiids - An array of escalation instance IDs that are used to identify the work items to be transferred. assignmentReason - The reason why the work item is assigned - refer to the work item assignment reasons . fromOwner - The user ID or the name of the group the work item currently belongs to. toOwner - The user ID or the name of the group the work item is to be transferred to. Work items can be transferred from a user to a user or from a group of users to a group of users. If a user work item is transferred, it is checked whether the user transferred to exists but the check may be executed case insensitively. The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments' custom property of the Human Task Manager configuration to 'true'. Returns: List - A list of EscalationResult objects, one for every escalation instance specified. Refer to EscalationResult . If a single transfer operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all transfer operations are undone. Throws: ArchiveUnsupportedOperationException IdWrongFormatException InvalidAssignmentReasonException InvalidLengthException ParameterNullException WorkItemNotFoundException WorkItemManagerException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.1 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### transferWorkItem

```
java.util.List transferWorkItem(ESIID[] esiids,
                              int assignmentReason,
                              java.lang.String fromOwner,
                              java.lang.String toOwner)
                                throws ArchiveUnsupportedOperationException,
                                       IdWrongFormatException,
                                       InvalidAssignmentReasonException,
                                       InvalidLengthException,
                                       ParameterNullException,
                                       WorkItemNotFoundException,
                                       WorkItemManagerException,
                                       UnexpectedFailureException,
                                       java.rmi.RemoteException,
                                       javax.ejb.EJBException
```

Note: 
 All transfer work item operations are executed within the current transaction.
 If a transaction timeout occurs, then all already executed transfer operations are rolled back.
 Because of this, you may consider to use
 bulkTransferWorkItem.
 
 The caller must be an administrator of the associated task instances.
 "Escalation receiver" work items can be transferred
 when the task is escalated, that is, the escalation is in the escalated state.
 An e-mail is not sent to the user or group that receives the transferred work item.
 
 The action associated to this method is
 EscalationActions.TRANSFERWORKITEM.
 
 This method is not supported in archive mode.

If a single transfer operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.EscalationDoesNotExistException
 com.ibm.task.api.TaskDelegationNotSupportedException
 com.ibm.task.api.UserDoesNotExistException
 com.ibm.task.api.WrongKindException
 com.ibm.task.api.WrongStateException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all transfer operations are undone.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- transferWorkItem java.util.List transferWorkItem(TKIID [] tkiids, int assignmentReason, java.lang.String fromOwner, java.lang.String toOwner) throws ArchiveUnsupportedOperationException , IdWrongFormatException , InvalidAssignmentReasonException , InvalidLengthException , ParameterNullException , WorkItemNotFoundException , WorkItemManagerException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Transfers the specified work items for the specified task instances using task instance IDs. Note: All transfer work item operations are executed within the current transaction. If a transaction timeout occurs, then all already executed transfer operations are rolled back. Because of this, you may consider to use bulkTransferWorkItem . The caller must be an owner, starter, originator, or administrator of the task instances. The task can be escalated. suspended, or waiting for subtasks. The following specific rules apply for the transfer of work items: The action associated to this method is TaskActions.TRANSFERWORKITEM . This method is not supported in archive mode. Parameters: tkiids - An array of task instance IDs that are used to identify the work items to be transferred. assignmentReason - The reason why the work item is assigned - refer to the work item assignment reasons . fromOwner - The user ID or the name of the group the work item currently belongs to. toOwner - The user ID or the name of the group the work item is to be transferred to. Work items can be transferred from a user to a user or from a group of users to a group of users. If a user work item is transferred, it is checked whether the user transferred to exists but the check may be executed case insensitively. The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments' custom property of the Human Task Manager configuration to 'true'. Returns: List - A list of TaskResult objects, one for every task instance specified. Refer to TaskResult . If a single transfer operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all transfer operations are undone. Throws: ArchiveUnsupportedOperationException IdWrongFormatException InvalidAssignmentReasonException InvalidLengthException ParameterNullException WorkItemNotFoundException WorkItemManagerException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.1 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### transferWorkItem

```
java.util.List transferWorkItem(TKIID[] tkiids,
                              int assignmentReason,
                              java.lang.String fromOwner,
                              java.lang.String toOwner)
                                throws ArchiveUnsupportedOperationException,
                                       IdWrongFormatException,
                                       InvalidAssignmentReasonException,
                                       InvalidLengthException,
                                       ParameterNullException,
                                       WorkItemNotFoundException,
                                       WorkItemManagerException,
                                       UnexpectedFailureException,
                                       java.rmi.RemoteException,
                                       javax.ejb.EJBException
```

Note: 
 All transfer work item operations are executed within the current transaction.
 If a transaction timeout occurs, then all already executed transfer operations are rolled back.
 Because of this, you may consider to use
 bulkTransferWorkItem.
 
 The caller must be an owner, starter, originator, or administrator of the task instances.
 The task can be escalated. suspended, or waiting for subtasks.
 
 The following specific rules apply for the transfer of work items:
 
Work items assigned to "everybody" cannot be transferred.
 The owner of a task instance can transfer the "owner" work item to a potential owner
 or an administrator of the task instance.
 The starter of a task instance can transfer the "starter" work item to a potential starter
 or an administrator of the task instance.
 A "starter" work item can be transferred in the expired, terminated, finished, failed, and running state.
 The originator of a task instance can transfer the "originator" work item to a potential instance creator
 or an administrator of the task instance.
 The originator of a task instance can transfer a "potential starter" work item to any person.
 A "potential starter" work item can be transferred in the inactive state.
 The administrator of a task instance can transfer all work items to any person.
 A "starter" work item can be transferred in the expired, terminated, finished, failed, and running state.
 A "potential starter" work item can be transferred in the inactive state.
 A "reader" or "administrator" work item can be transferred in all but the inactive state.
 A "potential owner" or "editor" work item can be transferred in the ready or claimed state.
 

 The action associated to this method is TaskActions.TRANSFERWORKITEM.
 
 This method is not supported in archive mode.

If a single transfer operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.TaskDoesNotExistException
 com.ibm.task.api.TaskDelegationNotSupportedException
 com.ibm.task.api.UserDoesNotExistException
 com.ibm.task.api.WrongKindException
 com.ibm.task.api.WrongStateException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all transfer operations are undone.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- triggerEscalation
void triggerEscalation(java.lang.String esiid)
                       throws ApplicationVetoException,
                              ArchiveUnsupportedOperationException,
                              CannotCreateWorkItemException,
                              EscalationNotificationException,
                              IdWrongFormatException,
                              IdWrongTypeException,
                              NotAuthorizedException,
                              ObjectDoesNotExistException,
                              SchedulingFailedException,
                              WrongStateException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Manually triggers the specified escalation instance
 using a string representation of the escalation instance ID.
 
 The escalation must be in the waiting state. The caller must be an administrator of
 the escalation.
 
 The action associated to this method is EscalationActions.TRIGGERESCALATION.
 
 This method is not supported in archive mode.
Parameters:esiid - A string representation of the escalation instance ID that is used
    to identify the escalation to be triggered.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
EscalationNotificationException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
SchedulingFailedException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- triggerEscalation
void triggerEscalation(ESIID esiid)
                       throws ApplicationVetoException,
                              ArchiveUnsupportedOperationException,
                              CannotCreateWorkItemException,
                              EscalationNotificationException,
                              IdWrongFormatException,
                              NotAuthorizedException,
                              ObjectDoesNotExistException,
                              SchedulingFailedException,
                              WrongStateException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Manually triggers the specified escalation instance
 using the escalation instance ID.
 
 The escalation must be in the waiting state. The caller must be an administrator of
 the escalation.
 
 The action associated to this method is EscalationActions.TRIGGERESCALATION.
 
 This method is not supported in archive mode.
Parameters:esiid - The escalation instance ID that is used
    to identify the escalation to be triggered.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
EscalationNotificationException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
SchedulingFailedException
WrongStateException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- update void update(Task task) throws ApplicationVetoException , ArchiveUnsupportedOperationException , InvalidLengthException , NotAuthorizedException , ObjectDoesNotExistException , ParameterNullException , PropertyVetoException , WrongKindException , WrongStateException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Updates a persistently stored task instance. The task and the properties to be updated are identified by the provided task object. Only the properties changed within the previously retrieved task instance are updated. When the same task property is updated in parallel, the last writer wins. The action associated to this method is TaskActions.UPDATE . This method is not supported in archive mode. Parameters: task - The task instance and the properties to be updated. Throws: ApplicationVetoException ArchiveUnsupportedOperationException InvalidLengthException NotAuthorizedException ObjectDoesNotExistException ParameterNullException PropertyVetoException WrongKindException WrongStateException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.0 Change History Release Modification 6.0.2 Allows to update the business relevance flag, the context authorization, the duration until deleted, the event handler name, namespace, parent context ID, the claim if suspended flag, the supports delegation flag, the supports follow-on flag, the supports subtasks flag, and the type. 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode. 7.0 Allows to update the deletion time, the due time, the expiration time, the duration until expiration, the escalation state, the read property, and the work basket name.

#### update

```
void update(Task task)
            throws ApplicationVetoException,
                   ArchiveUnsupportedOperationException,
                   InvalidLengthException,
                   NotAuthorizedException,
                   ObjectDoesNotExistException,
                   ParameterNullException,
                   PropertyVetoException,
                   WrongKindException,
                   WrongStateException,
                   UnexpectedFailureException,
                   java.rmi.RemoteException,
                   javax.ejb.EJBException
```

business relevance flag
   
The caller must be the owner, the starter, the originator, an editor, or an administrator of the task.
   The task can be a stand-alone task that is derived from a task template or
             created at Runtime.
   The task can be in an inactive, ready, running, or claimed state and
             can be escalated.
   
context authorization
   
The caller must be the originator or an administrator of the task.
   The task can be in an inline task that is derived from a task template.
   The task can be in an inactive or ready state, can be escalated, or waiting for subtasks.
   
custom properties
   
Refer to setCustomProperty.
   
deletion time
   
The caller must be the originator or an administrator of the task.
   The task can be a stand-alone task with "peer" autonomy or an invocation aka
             originating task that is derived from a task template or
             created at Runtime. Inline, child, follow-on, or subtasks are not supported.
   The task can be in an end state, can be escalated.
   Note, when you update this time, a duration until deletion is not calculated
             when you restart the task instance. A deletion timer is not set up.
   
description
   
The caller must be the owner, the starter, the originator, an editor, or an administrator of the task.
   The task can be a stand-alone task that is derived from a task template or
             created at Runtime.
   The task can be in all states, can be escalated, or waiting for subtasks.
   
display name
   
The caller must be the owner, the starter, the originator, an editor, or an administrator of the task.
   The task can be a stand-alone task that is derived from a task template or
             created at Runtime.
   The task can be in all states, can be escalated, or waiting for subtasks.
   
due time
   
The caller must be the owner, the starter, the originator, an editor, or an administrator of the task.
   The task can be a stand-alone or inline task
             that is derived from a task template or created at Runtime.
   The task can be in a ready, running, or claimed state,
             can be escalated, or waiting for subtasks.
   Note, when you update this time, a duration until due is not calculated
             when you restart the task instance.
   
duration until deleted
   
The caller must be the originator or an administrator of the task.
   The task can be a stand-alone task with "peer" autonomy or an invocation aka
             originating task that is derived from a task template or
             created at Runtime. Inline, child, follow-on, or subtasks are not supported.
   The task can be in an inactive, ready, running, claimed, or end state,
             can be escalated, or waiting for subtasks.
   Note, this is the duration taken when restarting the task instance.
   
duration until due
   
The caller must be the owner, the starter, the originator, an editor, or an administrator of the task.
   The task can be a stand-alone or inline task that is derived from a task template or
             created at Runtime.
   The task can be in an inactive, ready, running, or claimed state,
             can be escalated, or waiting for subtasks.
   Note, this is the duration taken when restarting the task instance.
   
duration until expires
   
The caller must be the originator or an administrator of the task.
   The task can be derived from a task template or created at Runtime.
             Inline, child, and follow-on tasks are not supported.
   The task can be in an inactive, ready, running, claimed, or forwarded state,
             can be escalated, or waiting for subtasks.
   Note, this is the duration taken when restarting the task instance.
   
escalation state
   
The caller must be the originator, starter, or an administrator of the task.
   The task can be derived from a task template or created at Runtime.
   The task can be in a ready, running, claimed, or forwarded state,
             can be escalated, or waiting for subtasks.
             If the task belongs to a chain of follow-on tasks,
             all tasks in the chain will be escalated or de-escalated.
   
event handler name
   
The caller must be the originator or an administrator of the task.
   The task can be a stand-alone or inline task that is derived from a task template or
             created at Runtime.
   The task can be in all states, can be escalated, or waiting for subtasks.
   
expiration time
   
The caller must be the originator or an administrator of the task.
   The task can be derived from a task template or created at Runtime.
             Inline, child, and follow-on tasks are not supported.
   The task can be in a ready, running, claimed, or forwarded state,
             can be escalated, or waiting for subtasks.
   Note, when you update this time, a duration until expiration is not calculated
             when you restart the task instance. An expiration timer is not set up.
   
name
   
The caller must be the owner, the starter, the originator, an editor, or an administrator of the task.
   The task can be a stand-alone task that is derived from a task template or
             created at Runtime.
   The task can be in all states, can be escalated, or waiting for subtasks.
   
namespace
   
The caller must be the owner, the starter, the originator, an editor, or an administrator of the task.
   The task can be a stand-alone task that is derived from a task template or
             created at Runtime.
   The task can be in all states, can be escalated, or waiting for subtasks.
   
parent context ID
   
The caller must be the originator or an administrator of the task.
   The task can be a stand-alone task that is derived from a task template or
             created at Runtime. It can, however, not be a to-do task with "child" autonomy,
             not be a subtask, or follow-on task,
   The task can be in all states, can be escalated, or waiting for subtasks.
   
priority
   
The caller must be the potential starter, the starter, the originator, or an administrator of the task.
   The task can be a stand-alone or inline task that is derived from a task template or
             created at Runtime.
   The task can be in an inactive, ready, running, or claimed state,
             can be escalated, or waiting for subtasks.
   
read flag
   
The caller must have at least reader authority for the task.
   The task can be a stand-alone or inline task that is derived from a task template or
             created at Runtime.
   The task can be in any state,
             can be escalated, or waiting for subtasks.
   
supports claim if suspended flag
   
The caller must be the owner, the originator, an editor, or an administrator of the task.
   The task can be a stand-alone or inline to-do task or a collaboration task
             that is derived from a task template or created at Runtime.
             Note that to-do and collaboration tasks are also known as participating
             and human tasks.
   The task can be in an inactive or ready state and can be escalated.
   
supports delegation flag
   
The caller must be the owner or an administrator of the task.
   The task can be a stand-alone or inline task that is derived from a task template or
             created at Runtime.
   The task can be in an inactive, ready, running, or claimed state,
             can be escalated, or waiting for subtasks.
   
supports follow-on tasks flag
   
The caller must be the owner or an administrator of the task.
   The task can be a stand-alone or inline to-do task or a collaboration task
             that is derived from a task template or created at Runtime.
             Note that to-do and collaboration tasks are also known as participating
             and human tasks.
   The task can be in an inactive, ready, running, or claimed state,
             can be escalated, or waiting for subtasks.
   
supports subtasks flag
   
The caller must be the owner or an administrator of the task.
   The task can be a stand-alone or inline to-do task or a collaboration task
             that is derived from a task template or created at Runtime.
             Note that to-do and collaboration tasks are also known as participating
             and human tasks.
   The task can be in an inactive, ready, running, or claimed state,
             and can be escalated.
   
type
   
The caller must be the owner, the starter, the originator, an editor, or an administrator of the task.
   The task can be a stand-alone or inline task that is derived from a task template or
             created at Runtime.
   The task can be in all states, can be escalated, or waiting for subtasks.
   
work basket name
   
The caller must be the the originator of the task.
   The task can be a stand-alone or inline task that is derived from a task template or
             created at Runtime.
   The task must be in the inactive state. Note that setting the work basket name
             does not update the isTransferredToWorkBasket property.
   

 The action associated to this method is TaskActions.UPDATE.
 
 This method is not supported in archive mode.

Change History

Release
 Modification
 
6.0.2
 
 Allows to update the business relevance flag, the context authorization,
 the duration until deleted, the event handler name, namespace, parent context ID,
 the claim if suspended flag, the supports delegation flag, the supports follow-on flag,
 the supports subtasks flag, and the type.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Allows to update the deletion time, the due time, the expiration time, the duration until expiration,
 the escalation state, the read property, and the work basket name.

- update
void update(java.lang.String tkiid,
          TaskModel taskModel,
          java.lang.String applicationName,
          java.lang.String parentContext,
          ClientObjectWrapper input)
            throws ApplicationVetoException,
                   ArchiveUnsupportedOperationException,
                   CannotCreateWorkItemException,
                   IdWrongFormatException,
                   IdWrongTypeException,
                   InvalidLengthException,
                   NotAuthorizedException,
                   ObjectDoesNotExistException,
                   ParameterNullException,
                   WrongKindException,
                   WrongMessageTypeException,
                   WrongStateException,
                   UnexpectedFailureException,
                   TaskDeploymentException,
                   TELValidationException,
                   java.rmi.RemoteException,
                   javax.ejb.EJBException
Updates a task instance that has been created at Runtime
 using a string representation of the task instance ID.
 All properties are changed according to the values provided by the task model.
 Actually, the specified task instance is deleted and a new task instance is created.
 
 The task must still be in the inactive state.
 The caller must be the originator of the task instance.
 
 The action associated to this method is TaskActions.UPDATEINACTIVETASK.
 
 This method is not supported in archive mode.
Parameters:tkiid - A string representation of the task instance ID that is used
    to identify the task instance to be updated.taskModel - The model that specifies the task properties and their new values.applicationName - The name of the enterprise application that contains the message
    or business calendar definitions used in the TaskModel.
    If the message definitions are simple types only or if you do not use a business
    calendar, null may be specified.parentContext - The object ID (ACOID) or the name of the application component to be associated.
    If not specified, the parent context of the updated task instance is kept.input - The input message.
    If not specified, the input message of the updated task instance is kept, if any.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
TaskDeploymentException
TELValidationException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- update
void update(TKIID tkiid,
          TaskModel taskModel,
          java.lang.String applicationName,
          java.lang.String parentContext,
          ClientObjectWrapper input)
            throws ApplicationVetoException,
                   ArchiveUnsupportedOperationException,
                   CannotCreateWorkItemException,
                   IdWrongFormatException,
                   IdWrongTypeException,
                   InvalidLengthException,
                   NotAuthorizedException,
                   ObjectDoesNotExistException,
                   ParameterNullException,
                   WrongKindException,
                   WrongMessageTypeException,
                   WrongStateException,
                   UnexpectedFailureException,
                   TaskDeploymentException,
                   TELValidationException,
                   java.rmi.RemoteException,
                   javax.ejb.EJBException
Updates a task instance that has been created at Runtime
 using the task instance ID.
 All properties are changed according to the values provided by the task model.
 Actually, the specified task instance is deleted and a new task instance is created.
 
 The task must still be in the inactive state.
 The caller must be the originator of the task instance.
 
 The action associated to this method is TaskActions.UPDATEINACTIVETASK.
 
 This method is not supported in archive mode.
Parameters:tkiid - The task instance ID that is used
    to identify the task instance to be updated.taskModel - The model that specifies the task properties and their new values.applicationName - The name of the enterprise application that contains the message
    or business calendar definitions used in the TaskModel.
    If the message definitions are simple types only or if you do not use a business
    calendar, null may be specified.parentContext - The object ID (ACOID) or the name of the application component to be associated.
    If not specified, the parent context of the updated task instance is kept.input - The input message.
    If not specified, the input message of the updated task instance is kept, if any.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WrongKindException
WrongMessageTypeException
WrongStateException
UnexpectedFailureException
TaskDeploymentException
TELValidationException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- update void update(Escalation escalation) throws ApplicationVetoException , ArchiveUnsupportedOperationException , InvalidLengthException , NotAuthorizedException , ObjectDoesNotExistException , ParameterNullException , PropertyVetoException , WrongStateException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Updates a persistently stored escalation instance. The escalation and the properties to be updated are identified by the provided escalation object. Only the properties changed within the previously retrieved escalation instance are updated. When the same escalation property is updated in parallel, the last writer wins. The action associated to this method is EscalationActions.UPDATE . This method is not supported in archive mode. Parameters: escalation - The escalation instance and the properties to be updated. Throws: ApplicationVetoException ArchiveUnsupportedOperationException InvalidLengthException NotAuthorizedException ObjectDoesNotExistException ParameterNullException PropertyVetoException WrongStateException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 7.0 Change History Release Modification 7.0.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### update

```
void update(Escalation escalation)
            throws ApplicationVetoException,
                   ArchiveUnsupportedOperationException,
                   InvalidLengthException,
                   NotAuthorizedException,
                   ObjectDoesNotExistException,
                   ParameterNullException,
                   PropertyVetoException,
                   WrongStateException,
                   UnexpectedFailureException,
                   java.rmi.RemoteException,
                   javax.ejb.EJBException
```

duration until escalated
   
The caller must be an administrator of the escalation.
   The escalation can be in an inactive or waiting state,
   
duration until repeated
   
The caller must be an administrator of the escalation.
   The escalation can be in an inactive, waiting, or escalated state,
   Any running timer is canceled. A new timer is created.
   
escalation time
   
The caller must be an administrator of the escalation.
   The escalation can be in a waiting or escalated state,
   Any running timer is canceled. A new timer is created.
             Note that if no timer is running, the new timer is a only run once.
   
name
   
The caller must be an administrator of the escalation.
   The escalation can be in an inactive, waiting, or escalated state,
   

 The action associated to this method is EscalationActions.UPDATE.
 
 This method is not supported in archive mode.

Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- findQueryTableMetaData
java.util.List findQueryTableMetaData(MetaDataOptions metaDataOptions)
                                      throws UnexpectedFailureException,
                                             TaskException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Queries the meta data of query tables.
 
 You can specify options to limit the number of query tables
 for which the meta data is returned.
 
 Note that the TaskException contains a com.ibm.bpe.api.ProcessException.
Parameters:metaDataOptions - The options to be applied - refer to MetaDataOptions.
    If no restrictions are to be applied, null can be specified.
 
Returns:List -
    A list of QueryTableMetaData objects.
 
Throws:
UnexpectedFailureException
TaskException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0

- getQueryTableMetaData
QueryTableMetaData getQueryTableMetaData(java.lang.String queryTableName,
                                       java.util.Locale locale)
                                         throws ParameterNullException,
                                                UnexpectedFailureException,
                                                TaskException,
                                                java.rmi.RemoteException,
                                                javax.ejb.EJBException
Returns the meta data of the specified query table.
 
 Note that the TaskException contains a com.ibm.bpe.api.ProcessException.
Parameters:queryTableName - The name of the query table.locale - The locale that is used to calculate the value of the $LOCALE variable. If
    no locale is specified, defaults are used for the calculation.
 
Returns:QueryTableMetaData -
    The meta data of the query table -
    refer to QueryTableMetaData.
 
Throws:
ParameterNullException
UnexpectedFailureException
TaskException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0

- queryEntities
EntityResultSet queryEntities(java.lang.String queryTableName,
                            FilterOptions filterOptions,
                            AuthorizationOptions authorizationOptions,
                            java.util.List parameters)
                              throws InvalidParameterException,
                                     NotAuthorizedException,
                                     ParameterNullException,
                                     UserDoesNotExistException,
                                     UserRegistryException,
                                     UnexpectedFailureException,
                                     TaskException,
                                     java.rmi.RemoteException,
                                     javax.ejb.EJBException
Queries entities using the specified query table.
 
 You can specify filter and authorization options to limit the number of entities returned
 and values for parameters used in query table filters and selection criteria.
 
 Note that the TaskException contains a com.ibm.bpe.api.ProcessException.
Parameters:queryTableName - The name of the query table.filterOptions - The filter options to be applied in addition to any filters defined
    for the query table.
    Refer to FilterOptions.authorizationOptions - The authorization options to be applied in addition to any authorization
    specifications defined for the query table.
    
    Authorization options can be specified for predefined query tables that contain
    instance data or for composite query tables that define a primary query table which
    contains instance data and that use instance-based authorization.
    If authorization options are specified for query tables that do not contain instance
    but template data, a NotAuthorizedException is thrown.
    They are ignored for supplemental query tables.
    
    System administrators and monitors can use the AdminAuthorizationOptions to
    run queries that need special authorization, for example, to run a query on behalf
    of another user. These options must be specified when the query is run on
    predefined query tables. When the query is run on composite query tables and
    the primary view contains template data, administrative options must be specified
    if role-based authorization is required.
    When specified for a predefined query table that contains instance data or for
    a composite query table with a primary view that contains instance data, then
    all data contained in the query table is returned.
    
    Refer to AuthorizationOptions or
    AdminAuthorizationOptions.parameters - A list of Parameter objects to set values for parameters used
    in query table filters and selection criteria.
    Refer to Parameter.
 
Returns:EntityResultSet -
    The entity result set containing the qualifying entities. If no qualifying entities
    are found, an empty result set is returned. Refer to EntityResultSet
    for information on how to analyze the result set.
 
Throws:
InvalidParameterException
NotAuthorizedException
ParameterNullException
UserDoesNotExistException
UserRegistryException
UnexpectedFailureException
TaskException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0

- queryEntityCount
int queryEntityCount(java.lang.String queryTableName,
                   FilterOptions filterOptions,
                   AuthorizationOptions authorizationOptions,
                   java.util.List parameters)
                     throws InvalidParameterException,
                            NotAuthorizedException,
                            ParameterNullException,
                            UserDoesNotExistException,
                            UserRegistryException,
                            UnexpectedFailureException,
                            TaskException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Counts qualifying entities of a potential query for entities.
 
 Note that the TaskException contains a com.ibm.bpe.api.ProcessException.
Parameters:queryTableName - The name of the query table.filterOptions - The filter options to limit the number of entities and attributes.
    Refer to FilterOptions.authorizationOptions - The authorization options to limit the number of entities.
    Refer to AuthorizationOptions or
    AdminAuthorizationOptions.parameters - A list of Parameter objects to replace parameters in the query condition.
    Refer to Parameter.
 
Returns:int -
    The number of qualifying entities.
 
Throws:
InvalidParameterException
NotAuthorizedException
ParameterNullException
UserDoesNotExistException
UserRegistryException
UnexpectedFailureException
TaskException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0

- queryRows
RowResultSet queryRows(java.lang.String queryTableName,
                     FilterOptions filterOptions,
                     AuthorizationOptions authorizationOptions,
                     java.util.List parameters)
                       throws InvalidParameterException,
                              NotAuthorizedException,
                              ParameterNullException,
                              UserDoesNotExistException,
                              UserRegistryException,
                              UnexpectedFailureException,
                              TaskException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Queries attributes using the specified query table.
 
 You can specify filter and authorization options to limit the number of rows returned
 and values for parameters used in query table filters and selection criteria.
 
 Note that the TaskException contains a com.ibm.bpe.api.ProcessException.
Parameters:queryTableName - The name of the query table.filterOptions - The filter options to be applied in addition to any filters defined
    for the query table.
    Refer to FilterOptions.authorizationOptions - The authorization options to be applied in addition to any authorization
    specifications defined for the query table.
    
    Authorization options can be specified for predefined query tables that contain
    instance data or for composite query tables that define a primary query table which
    contains instance data and that use instance-based authorization.
    If authorization options are specified for query tables that do not contain instance
    but template data, a NotAuthorizedException is thrown.
    They are ignored for supplemental query tables.
    
    System administrators and monitors can use the AdminAuthorizationOptions to
    run queries that need special authorization, for example, to run a query on behalf
    of another user. These options must be specified when the predefined query table
    or the primary view of a composite query table contains template data.
    
    Refer to AuthorizationOptions or
    AdminAuthorizationOptions.parameters - A list of Parameter objects to set values for parameters used
    in query table filters and selection criteria.
    Refer to Parameter.
 
Returns:RowResultSet -
    The row result set containing the qualifying objects. If no qualifying objects
    are found, an empty result set is returned. Refer to RowResultSet
    for information on how to analyze the result set.
 
Throws:
InvalidParameterException
NotAuthorizedException
ParameterNullException
UserDoesNotExistException
UserRegistryException
UnexpectedFailureException
TaskException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0

- queryRowCount
int queryRowCount(java.lang.String queryTableName,
                FilterOptions filterOptions,
                AuthorizationOptions authorizationOptions,
                java.util.List parameters)
                  throws InvalidParameterException,
                         NotAuthorizedException,
                         ParameterNullException,
                         UserDoesNotExistException,
                         UserRegistryException,
                         UnexpectedFailureException,
                         TaskException,
                         java.rmi.RemoteException,
                         javax.ejb.EJBException
Counts qualifying objects of a potential query table query.
 
 Note that the TaskException contains a com.ibm.bpe.api.ProcessException.
Parameters:queryTableName - The name of the query table.filterOptions - The filter options to limit the number of rows or attributes.
    Refer to FilterOptions.authorizationOptions - The authorization options to limit the number of rows.
    Refer to AuthorizationOptions or
    AdminAuthorizationOptions.parameters - A list of Parameter objects to replace parameters in the query condition.
    Refer to Parameter.
 
Returns:int -
    The number of qualifying objects in rows.
 
Throws:
InvalidParameterException
NotAuthorizedException
ParameterNullException
UserDoesNotExistException
UserRegistryException
UnexpectedFailureException
TaskException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0