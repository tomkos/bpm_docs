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

## Interface BusinessFlowManagerService

- All Known Subinterfaces:
BusinessFlowManager, LocalBusinessFlowManager, LocalBusinessFlowManagerService

public interface BusinessFlowManagerService
BusinessFlowManagerService defines the business functions that can be called by a local or remote client.

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

ClientObjectWrapper
call(java.lang.String processTemplateName,
    ClientObjectWrapper inputMessage)
Creates and executes a process instance that is derived from the specified
 process template.

ClientObjectWrapper
call(java.lang.String vtid,
    java.lang.String atid,
    ClientObjectWrapper inputMessage)
Creates and executes a process instance using a string representation
 of the activity service template ID and the activity template ID.

ClientObjectWrapper
call(java.lang.String processTemplateName,
    java.lang.String nameSpace,
    java.lang.String portType,
    java.lang.String operation,
    ClientObjectWrapper inputMessage)
Creates and executes a process instance that is derived from the specified
 process template by calling the specified starting service.

ClientObjectWrapper
call(VTID vtid,
    ATID atid,
    ClientObjectWrapper inputMessage)
Creates and executes a process instance using
 the activity service template ID and the activity template ID.

void
callServiceWithReplyContext(java.lang.String vtid,
                           java.lang.String atid,
                           java.lang.String processInstanceName,
                           ClientObjectWrapper inputMessage,
                           ReplyContextWrapper replyContext,
                           int invocationCount,
                           java.lang.String requestId)
Creates and executes a process instance using the activity service template ID and the activity template ID
 and asynchronously waits for the result.

void
callServiceWithReplyContext(VTID vtid,
                           ATID atid,
                           java.lang.String processInstanceName,
                           ClientObjectWrapper inputMessage,
                           ReplyContextWrapper replyContext,
                           int invocationCount,
                           java.lang.String requestId)
Creates and executes a process instance using the activity service template ID and the activity template ID
 and asynchronously waits for the result.

void
callWithReplyContext(java.lang.String processTemplateName,
                    ClientObjectWrapper inputMessage,
                    ReplyContextWrapper replyContext)
Creates and executes a process instance from the specified process template and
 asynchronously waits for the result.

void
callWithReplyContext(java.lang.String processTemplateName,
                    ClientObjectWrapper inputMessage,
                    ReplyContextWrapper replyContext,
                    int invocationCount,
                    java.lang.String requestId)
Creates and executes a process instance from the specified process template and
 asynchronously waits for the result of the uniquely identified request.

void
callWithReplyContext(java.lang.String processTemplateName,
                    java.lang.String processInstanceName,
                    ClientObjectWrapper inputMessage,
                    ReplyContextWrapper replyContext)
Creates and executes a named process instance from the specified process template and
 asynchronously waits for the result.

void
callWithReplyContext(java.lang.String processTemplateName,
                    java.lang.String processInstanceName,
                    ClientObjectWrapper inputMessage,
                    ReplyContextWrapper replyContext,
                    int invocationCount,
                    java.lang.String requestId)
Creates and executes a named process instance from the specified process template and
 asynchronously waits for the result of the uniquely identified request.

ProcessResponseWrapper
callWithUISettings(java.lang.String processTemplateName,
                  ClientObjectWrapper inputMessage)
Creates and executes a process instance that is derived from the specified
 process template
 and returns the output message as well as its client UI settings.

ProcessResponseWrapper
callWithUISettings(java.lang.String vtid,
                  java.lang.String atid,
                  ClientObjectWrapper inputMessage)
Creates and executes a process instance
 using a string representation of the activity service template ID and the activity template ID
 and returns the output message as well as its client UI settings.

ProcessResponseWrapper
callWithUISettings(VTID vtid,
                  ATID atid,
                  ClientObjectWrapper inputMessage)
Creates and executes a process instance using the activity service template ID and the activity template ID
 and returns the output message as well as its client UI settings.

void
cancelClaim(AIID aiid)
Cancels the claim of an activity instance using the activity instance ID.

void
cancelClaim(AIID aiid,
           boolean keepData)
Cancels the claim of an activity instance and keeps any data that has been set
 using the activity instance ID.

void
cancelClaim(java.lang.String aiid)
Cancels the claim of an activity instance using a string representation of the activity instance ID.

void
cancelClaim(java.lang.String aiid,
           boolean keepData)
Cancels the claim of an activity instance and keeps any data that has been set
 using a string representation of the activity instance ID.

void
cancelSkipRequest(AIID aiid)
Cancels the skip request for the activity instance using the activity instance ID.

void
cancelSkipRequest(PIID piid,
                 java.lang.String activityName)
Cancels the skip request for the specified activity instance using the associated process instance ID
 and the activity instance name.

void
cancelSkipRequest(java.lang.String aiid)
Cancels the skip request for the activity instance using a string representation of the
 activity instance ID.

void
cancelSkipRequest(java.lang.String piid,
                 java.lang.String activityName)
Cancels the skip request for the specified activity instance using a string representation of the
 associated process instance ID and the activity name.

ClientObjectWrapper
claim(AIID aiid)
Claims a ready activity instance for user processing using the activity instance ID.

ClientObjectWrapper
claim(java.lang.String aiid)
Claims a ready activity instance for user processing
 using a string representation of the activity instance ID.

ActivityInstanceData
claim(java.lang.String whereClause,
     java.lang.String orderByClause,
     java.util.TimeZone timeZone)
Claims a ready activity instance for user processing.

void
claimProcessOwnership(PIID piid)
Claims the ownership for the specified process instance
 using the process instance ID.

void
claimProcessOwnership(java.lang.String piid)
Claims the ownership for the specified process instance
 using a string representation of the process instance ID.

void
complete(AIID aiid)
Completes a claimed activity instance using the activity instance ID.

void
complete(AIID aiid,
        ClientObjectWrapper output)
Completes a claimed activity instance using the activity instance ID
 and passes the result of user processing.

void
complete(AIID aiid,
        ClientObjectWrapper faultMessage,
        java.lang.String faultName)
Completes a claimed activity instance using the activity instance ID
 and denotes the failing of user processing.

void
complete(java.lang.String aiid)
Completes a claimed activity instance using a string representation of the activity instance ID.

void
complete(java.lang.String aiid,
        ClientObjectWrapper output)
Completes a claimed activity instance using a string representation of the activity instance ID
 and passes the result of user processing.

void
complete(java.lang.String aiid,
        ClientObjectWrapper faultMessage,
        java.lang.String faultName)
Completes a claimed activity instance using a string representation of the activity instance ID
 and denotes the failing of user processing.

CompleteAndClaimSuccessorResult
completeAndClaimSuccessor(AIID aiid,
                         ClientObjectWrapper output)
Completes a claimed activity instance using the activity instance ID
 and claims a successor activity.

CompleteAndClaimSuccessorResult
completeAndClaimSuccessor(java.lang.String aiid,
                         ClientObjectWrapper output)
Completes a claimed activity instance using a string representation of the activity instance ID
 and claims a successor activity.

void
completeAndJump(AIID aiid,
               ClientObjectWrapper output,
               java.lang.String targetActivityName)
Completes a claimed activity instance using the activity instance ID
 and some output and continues navigation at the specified target activity.

void
completeAndJump(AIID aiid,
               java.lang.String targetActivityName)
Completes a claimed activity instance using the activity instance ID
 and continues navigation at the specified target activity.

void
completeAndJump(java.lang.String aiid,
               ClientObjectWrapper output,
               java.lang.String targetActivityName)
Completes a claimed activity instance using a string representation of the
 activity instance ID and some output and continues navigation at the specified target activity.

void
completeAndJump(java.lang.String aiid,
               java.lang.String targetActivityName)
Completes a claimed activity instance using a string representation of the
 activity instance ID and continues navigation at the specified target activity.

ClientObjectWrapper
createMessage(AIID aiid,
             java.lang.String messageTypeName)
Creates a message defined by the specified activity instance using the activity instance ID.

ClientObjectWrapper
createMessage(EHTID ehtid,
             java.lang.String messageTypeName)
Creates a message defined by the specified event handler template using the event handler template ID.

ClientObjectWrapper
createMessage(PIID piid,
             java.lang.String messageTypeName)
Creates a message defined by the specified process instance using the process instance ID.

ClientObjectWrapper
createMessage(PTID ptid,
             java.lang.String messageTypeName)
Creates a message defined by the specified process template using the process template ID.

ClientObjectWrapper
createMessage(java.lang.String identifier,
             java.lang.String messageTypeName)
Creates a message defined by the specified process template, process instance,
  activity instance, or event handler template
 using a string representation of the object ID.

ClientObjectWrapper
createMessage(java.lang.String vtid,
             java.lang.String atid,
             java.lang.String messageTypeName)
Creates a message defined by the specified activity service
 using string representations of object IDs.

ClientObjectWrapper
createMessage(VTID vtid,
             ATID atid,
             java.lang.String messageTypeName)
Creates a message defined by the specified activity service using object IDs.

ClientObjectWrapper
createMessageWithCorrelationSets(AIID aiid,
                                java.lang.String messageTypeName)
Creates a message defined by the specified activity instance using the activity instance ID
 and sets the values that are available for initialized correlation sets.

ClientObjectWrapper
createMessageWithCorrelationSets(java.lang.String aiid,
                                java.lang.String messageTypeName)
Creates a message defined by the specified activity instance
 using a string representation of the activity instance ID
 and sets the values that are available for initialized correlation sets.

ClientObjectWrapper
createMessageWithCorrelationSets(java.lang.String vtid,
                                java.lang.String atid,
                                java.lang.String piid,
                                java.lang.String messageTypeName)
Creates a message defined by the specified activity service
 using string representations of object IDs
 and sets the values that are available for initialized correlation sets.

ClientObjectWrapper
createMessageWithCorrelationSets(VTID vtid,
                                ATID atid,
                                PIID piid,
                                java.lang.String messageTypeName)
Creates a message defined by the specified activity service using object IDs
 and sets the values that are available for initialized correlation sets.

ClientObjectWrapper
createMessageWithCorrelationSetsForEventHandler(EHTID ehtid,
                                               PIID piid)
Creates a message defined by the specified event handler using the event handler
 object ID
 and sets the values that are available for initialized correlation sets.

ClientObjectWrapper
createMessageWithCorrelationSetsForEventHandler(java.lang.String ehtid,
                                               java.lang.String piid)
Creates a message defined by the specified event handler
 using a string representation of the event handler template ID
 and sets the values that are available for initialized correlation sets.

void
createStoredQuery(java.lang.String storedQueryName,
                 java.lang.String selectClause,
                 java.lang.String whereClause,
                 java.lang.String orderByClause,
                 java.lang.Integer threshold,
                 java.util.TimeZone timeZone)
Creates a query definition and persistently stores it in the database for
 general usage.

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

void
createWorkItem(AIID aiid,
              int assignmentReason,
              java.lang.String userID)
Creates a work item for activities with the specified assignment reason
 for the specified activity instance and user.

void
createWorkItem(PIID piid,
              int assignmentReason,
              java.lang.String userID)
Creates a work item for processes with the specified assignment reason
 for the specified process instance and user.

void
createWorkItem(java.lang.String identifier,
              int assignmentReason,
              java.lang.String userID)
Creates a work item for processes or activities
 using a string representation of either the process or activity instance ID.

void
delete(PIID piid)
Deletes the specified top-level process instance and its non-autonomous subprocesses
 and tasks using the process instance ID.

void
delete(java.lang.String piid)
Deletes the specified top-level process instance and its non-autonomous subprocesses
 and tasks using a string representation of the process instance ID
 or the process instance name.

void
deleteStoredQuery(java.lang.String storedQueryName)
Deletes the specified stored query.

void
deleteStoredQuery(java.lang.String userID,
                 java.lang.String storedQueryName)
Deletes the specified stored query for the specified user.

void
deleteWorkItem(AIID aiid,
              int assignmentReason,
              java.lang.String userID)
Deletes the specified work item for the specified activity instance.

void
deleteWorkItem(PIID piid,
              int assignmentReason,
              java.lang.String userID)
Deletes the specified work item for the specified process instance.

void
deleteWorkItem(java.lang.String identifier,
              int assignmentReason,
              java.lang.String userID)
Deletes the specified work item using a string representation of
 either the process or activity instance ID.

void
deleteWorkList(java.lang.String workListName)
Deprecated. 
As of version 6.0, replaced by deleteStoredQuery.

QueryResultSet
executeWorkList(java.lang.String workListName)
Deprecated. 
As of version 6.0, replaced by query.

java.util.List
findQueryTableMetaData(MetaDataOptions metaDataOptions)
Queries the meta data of query tables.

void
forceComplete(AIID aiid,
             boolean continueOnError)
Forces the completion of an activity instance using the activity instance ID.

void
forceComplete(AIID aiid,
             ClientObjectWrapper output,
             boolean continueOnError)
Forces the completion of an activity instance using the activity instance ID
 and an output messsage.

void
forceComplete(AIID aiid,
             ClientObjectWrapper message,
             java.lang.String faultName,
             boolean continueOnError)
Forces the completion of an activity instance using the activity instance ID
 and states the actual result of user processing.

void
forceComplete(java.lang.String aiid,
             boolean continueOnError)
Forces the completion of an activity instance
 using a string representation of the activity instance ID.

void
forceComplete(java.lang.String aiid,
             ClientObjectWrapper output,
             boolean continueOnError)
Forces the completion of an activity instance
 using a string representation of the activity instance ID and an output message.

void
forceComplete(java.lang.String aiid,
             ClientObjectWrapper message,
             java.lang.String faultName,
             boolean continueOnError)
Forces the completion of an activity instance
 using a string representation of the activity instance ID
 and states the actual result of user processing.

void
forceCompleteAndJump(AIID aiid,
                    ClientObjectWrapper output,
                    java.lang.String targetActivityName)
Forces the completion of an activity instance using the activity instance ID
 and continues navigation at the specified target activity.

void
forceCompleteAndJump(java.lang.String aiid,
                    ClientObjectWrapper output,
                    java.lang.String targetActivityName)
Forces the completion of an activity instance using a string representation of the
 activity instance ID and continues navigation at the specified target activity.

void
forceForEachCounterValues(AIID aiid,
                         int startCounter,
                         int finalCounter,
                         java.lang.Integer maxCompletedBranches)
Forces the navigation of an activity instance that stopped because
 the evaluation of for-each counter values failed
 using the activity instance ID.

void
forceForEachCounterValues(java.lang.String aiid,
                         int startCounter,
                         int finalCounter,
                         java.lang.Integer maxCompletedBranches)
Forces the navigation of an activity instance that stopped because
 the evaluation of for-each counter values failed
 using a string representation of the activity instance ID.

void
forceJoinCondition(AIID aiid,
                  boolean conditionValue)
Forces the navigation of an activity instance that stopped because
 the join condition evaluation failed
 using the activity instance ID.

void
forceJoinCondition(java.lang.String aiid,
                  boolean conditionValue)
Forces the navigation of an activity instance that stopped because
 the join condition evaluation failed
 using a string representation of the activity instance ID.

void
forceLoopCondition(AIID aiid,
                  boolean conditionValue)
Forces the navigation of an activity instance that stopped because
 a loop condition evaluation failed
 using the activity instance ID.

void
forceLoopCondition(java.lang.String aiid,
                  boolean conditionValue)
Forces the navigation of an activity instance that stopped because
 a loop condition evaluation failed
 using a string representation of the activity instance ID.

void
forceNavigate(AIID aiid,
             int positionOfBranch)
Forces the navigation of a branch of the specified switch activity
 using the activity instance ID.

void
forceNavigate(AIID aiid,
             java.lang.String[] linksToBeFollowed)
Forces the navigation of links leaving the specified activity instance
 using the activity instance ID.

void
forceNavigate(java.lang.String aiid,
             int positionOfBranch)
Forces the navigation of a branch of the specified switch activity
 using a string representation of the activity instance ID.

void
forceNavigate(java.lang.String aiid,
             java.lang.String[] linksToBeFollowed)
Forces the navigation of links leaving the specified activity instance
 using a string representation of the activity instance ID.

void
forceRetry(AIID aiid,
          boolean continueOnError)
Forces the repetition of an activity instance using the activity instance ID.

void
forceRetry(AIID aiid,
          boolean continueOnError,
          int timerBehavior)
Forces the repetition of an activity instance using the activity instance ID
 and specifies how to handle timers.

void
forceRetry(AIID aiid,
          ClientObjectWrapper inputMessage,
          boolean continueOnError)
Forces the repetition of an activity instance using the activity instance ID
 and an input message.

void
forceRetry(AIID aiid,
          ClientObjectWrapper inputMessage,
          boolean continueOnError,
          int timerBehavior)
Forces the repetition of an activity instance using the activity instance ID
 and passes an input message and a timer specification.

void
forceRetry(java.lang.String aiid,
          boolean continueOnError)
Forces the repetition of an activity instance
 using a string representation of the activity instance ID.

void
forceRetry(java.lang.String aiid,
          boolean continueOnError,
          int timerBehavior)
Forces the repetition of an activity instance
 using a string representation of the activity instance ID and specifies how to handle timers.

void
forceRetry(java.lang.String aiid,
          ClientObjectWrapper inputMessage,
          boolean continueOnError)
Forces the repetition of an activity instance
 using a string representation of the activity instance ID and an input message.

void
forceRetry(java.lang.String aiid,
          ClientObjectWrapper inputMessage,
          boolean continueOnError,
          int timerBehavior)
Forces the repetition of an activity instance
 using a string representation of the activity instance ID
 and passes an input message and a timer specification.

void
forceTerminate(PIID piid)
Terminates the specified top-level process instance, its non-autonomous subprocesses, and
 its running, claimed, or waiting activities using the process instance ID.

void
forceTerminate(PIID piid,
              int invokeCompensation)
Terminates the specified top-level process instance, its non-autonomous subprocesses,
 its running, claimed, or waiting activities
 using the process instance ID.

void
forceTerminate(java.lang.String identifier)
Terminates the specified top-level process instance, its non-autonomous subprocesses,
 and its running, claimed, or waiting activities using a string representation of the process instance ID
 or the process instance name.

void
forceTerminate(java.lang.String identifier,
              int invokeCompensation)
Terminates the specified top-level process instance, its non-autonomous subprocesses,
 its running, claimed, or waiting activities
 using a string representation of the process instance ID or the process instance name.

EventHandlerTemplateData[]
getActiveEventHandlers(PIID piid)
Retrieves the active event handlers of the specified
 process instance using the process instance ID.

EventHandlerTemplateData[]
getActiveEventHandlers(java.lang.String piid)
Retrieves the active event handlers of the specified
 process instance using a string representation of the process instance object ID.

ActivityInstanceData
getActivityInstance(AIID aiid)
Retrieves the specified activity instance using the activity instance ID.

ActivityInstanceData
getActivityInstance(PIID piid,
                   java.lang.String activityTemplateName)
Retrieves the specified activity instance using the process instance ID
 and the activity template name.

ActivityInstanceData
getActivityInstance(java.lang.String aiid)
Retrieves the specified activity instance using a string representation of the activity instance ID.

ActivityInstanceData
getActivityInstance(java.lang.String piid,
                   java.lang.String activityTemplateName)
Retrieves the specified activity instance using a string representation of the
 process instance ID and the activity template name.

ActivityServiceTemplateData
getActivityServiceTemplate(java.lang.String vtid,
                          java.lang.String atid)
Retrieves the specified activity service template
 using string representations of the associated object IDs.

ActivityServiceTemplateData
getActivityServiceTemplate(VTID vtid,
                          ATID atid)
Retrieves the specified activity service template using the associated object IDs.

QueryResultSet
getAllActivities(PIID piid,
                java.util.TimeZone timezone)
Queries pre-defined activity instance properties of activities directly contained
 in the specified process instance using the process instance ID.

QueryResultSet
getAllActivities(java.lang.String piid,
                java.util.TimeZone timezone)
Queries pre-defined activity instance properties of activities directly contained
 in the specified process instance using a string representation of the
 process instance ID.

java.util.List
getAllBasicActivityNames(PIID piid)
Retrieves the names of all basic activities that are part of the specified process instance
 using the process instance ID.

java.util.List
getAllBasicActivityNames(java.lang.String piid)
Retrieves the names of all basic activities that are part of the specified process instance
 using a string representation of the process instance ID.

java.util.List
getAllCustomProperties(PIID piid)
Retrieves all custom properties of the specified process instance using the process instance ID.

java.util.List
getAllCustomProperties(PTID ptid)
Retrieves all custom properties of the specified process template using the process template ID.

java.util.List
getAllCustomProperties(java.lang.String identifier)
Retrieves all custom properties of the specified process template or process instance
 using a string representation of the object ID.

java.util.List
getAllQueryProperties(java.lang.String propertyNameFilter,
                     java.lang.Integer threshold)
Retrieves the query properties of all process templates.

java.util.List
getAllVariableNames(AIID aiid)
Retrieves the names of all variables visible by the specified activity instance
 using the activity instance ID.

java.util.List
getAllVariableNames(PIID piid)
Retrieves the names of all variables visible by the specified process instance
 using the process instance ID.

java.util.List
getAllVariableNames(PIID piid,
                   java.lang.String activityName)
Retrieves the names of all variables visible by the specified activity
 using the process instance ID and the activity name.

java.util.List
getAllVariableNames(java.lang.String identifier)
Retrieves the names of all variables visible by the specified process or
 activity instance using a string representation of the process or
 activity instance ID.

java.util.List
getAllVariableNames(java.lang.String piid,
                   java.lang.String activityName)
Retrieves the names of all variables visible by the specified activity
 using a string representation of the process instance ID and the activity name.

WorkItemData[]
getAllWorkItems(AIID aiid)
Retrieves all work item assignments associated to the specified activity instance
 using the activity instance ID.

WorkItemData[]
getAllWorkItems(PIID piid)
Retrieves all work item assignments associated to the specified process instance
 using the process instance ID.

WorkItemData[]
getAllWorkItems(java.lang.String identifier)
Retrieves all work item assignments associated to the specified process or activity instance
 using a string representation of the process or activity instance ID.

boolean[][]
getAvailableActionFlags(AIID[] aiids)
Returns indicators to state the actions that can be called in the current activity
 instance states by the logged-on user using activity instance IDs.

boolean[][]
getAvailableActionFlags(PIID[] piids)
Returns indicators to state the actions that can be called in the current process
 instance states by the logged-on user using process instance IDs.

boolean[][]
getAvailableActionFlags(java.lang.String[] identifiers)
Returns indicators to state the actions that can be called in the current process
 instance states or in the current activity instance states by the logged-on user.

BfmConfiguration
getBfmConfiguration()
Returns configuration settings of the Business Flow Manager.

BinaryCustomProperty
getBinaryCustomProperty(AIID aiid,
                       java.lang.String propertyName)
Retrieves the named binary custom property of the specified
 activity instance using the activity instance object ID.

BinaryCustomProperty
getBinaryCustomProperty(PIID piid,
                       java.lang.String propertyName)
Retrieves the named binary custom property of the specified
 process instance using the process instance the object ID.

BinaryCustomProperty
getBinaryCustomProperty(PIID piid,
                       java.lang.String activityName,
                       java.lang.String propertyName)
Retrieves the named binary custom property of the specified activity instance
 using the process instance ID and the activity name.

BinaryCustomProperty
getBinaryCustomProperty(java.lang.String identifier,
                       java.lang.String propertyName)
Retrieves the named binary custom property of the specified
 process or activity instance using a string representation of the object ID.

BinaryCustomProperty
getBinaryCustomProperty(java.lang.String piid,
                       java.lang.String activityName,
                       java.lang.String propertyName)
Retrieves the named binary custom property of the specified activity instance
 using a string representation of the process instance ID and the activity name.

java.util.List
getBinaryCustomPropertyNames(AIID aiid)
Retrieves the names of all binary custom properties of the specified
 activity instance using the activity instance ID.

java.util.List
getBinaryCustomPropertyNames(PIID piid)
Retrieves the names of all binary custom properties of the specified
 process instance using the process instance ID.

java.util.List
getBinaryCustomPropertyNames(PIID piid,
                            java.lang.String activityName)
Retrieves the names of all binary custom property of the specified activity instance
 using the process instance ID and the activity name.

java.util.List
getBinaryCustomPropertyNames(java.lang.String identifier)
Retrieves the names of all binary custom properties of the specified
 process or activity instance using a string representation of the process or activity instance ID.

java.util.List
getBinaryCustomPropertyNames(java.lang.String piid,
                            java.lang.String activityName)
Retrieves the names of all binary custom property of the specified activity instance
 using a string representation of the process instance ID and the activity name.

BranchTemplateData[]
getBranches(AIID aiid)
Retrieves information about the branches of the specified switch activity instance
 using the activity instance ID.

BranchTemplateData[]
getBranches(java.lang.String aiid)
Retrieves information about the branches of the specified switch activity instance
 using a string representation of the activity instance object ID.

CustomClientSettings
getClientUISettings(AIID aiid)
Retrieves client interface settings for the specified activity instance using the activity instance ID.

CustomClientSettings
getClientUISettings(PIID piid)
Retrieves client interface settings for the specified process instance using the process instance ID.

CustomClientSettings
getClientUISettings(PTID ptid)
Retrieves client interface settings for the specified process template using the process template ID.

CustomClientSettings
getClientUISettings(java.lang.String identifier)
Retrieves client interface settings for the specified process template,
 process instance, or activity instance using a string representation of the object ID.

CustomClientSettings
getClientUISettings(java.lang.String vtid,
                   java.lang.String atid)
Retrieves client interface settings for the specified service using a string representation
 of the activity and service object IDs.

CustomClientSettings
getClientUISettings(VTID vtid,
                   ATID atid)
Retrieves client interface settings for the specified service using the activity
 and service object IDs.

java.util.List
getCorrelationSetInstances(AIID aiid,
                          java.lang.String messageTypeName)
Retrieves the correlation set instances of the specified activity instance
 and message type
 using the activity instance ID.

java.util.List
getCorrelationSetInstances(PIID piid)
Retrieves the correlation set instances of the specified process instance
 using the process instance ID.

java.util.List
getCorrelationSetInstances(java.lang.String piid)
Retrieves the correlation set instances of the specified process instance
 using a string representation of the process instance ID.

java.util.List
getCorrelationSetInstances(java.lang.String aiid,
                          java.lang.String messageTypeName)
Retrieves the correlation set instances of the specified activity instance
 and message type
 using a string representation of the activity instance ID.

java.util.List
getCustomProperties(AIID aiid)
Retrieves the custom properties of the specified activity instance using the activity instance ID.

java.util.List
getCustomProperties(PIID piid)
Retrieves the custom properties of the specified process instance using the process instance ID.

java.util.List
getCustomProperties(PIID piid,
                   java.lang.String activityName)
Retrieves the custom properties of the specified activity instance using
 using the process instance ID and the activity name.

java.util.List
getCustomProperties(PTID ptid)
Retrieves the custom properties of the specified process template using the process template ID.

java.util.List
getCustomProperties(java.lang.String identifier)
Retrieves the custom properties of the specified process template, process instance,
 or activity instance using a string representation of the object ID.

java.util.List
getCustomProperties(java.lang.String identifier,
                   java.lang.String activityName)
Retrieves the custom properties of the specified activity instance
 using a string representation of the process instance ID and the activity name.

java.lang.String
getCustomProperty(AIID aiid,
                 java.lang.String propertyName)
Retrieves the named custom property of the specified activity instance using the activity instance ID.

java.lang.String
getCustomProperty(PIID piid,
                 java.lang.String propertyName)
Retrieves the named custom property of the specified process instance using the process instance ID.

java.lang.String
getCustomProperty(PIID piid,
                 java.lang.String activityName,
                 java.lang.String propertyName)
Retrieves the named custom property of the specified activity instance
 using the process instance ID and the activity name.

java.lang.String
getCustomProperty(PTID ptid,
                 java.lang.String propertyName)
Retrieves the named custom property of the specified process template using the process template ID.

java.lang.String
getCustomProperty(java.lang.String identifier,
                 java.lang.String propertyName)
Retrieves the named custom property of the specified process template, process instance,
 or activity instance using a string representation of the object ID.

java.lang.String
getCustomProperty(java.lang.String piid,
                 java.lang.String activityName,
                 java.lang.String propertyValue)
Retrieves the named custom property of the specified activity instance
 using a string representation of the process instance ID and the activity name.

java.util.List
getCustomPropertyInfo(int objectType,
                     java.lang.String nameFilter,
                     java.lang.Integer threshold)
Retrieves information about custom properties of the specified object types.

java.util.List
getCustomPropertyNames(AIID aiid)
Retrieves the custom property names of the specified activity instance
 using the activity instance ID.

java.util.List
getCustomPropertyNames(PIID piid)
Retrieves the custom property names of the specified process instance
 using the process instance ID.

java.util.List
getCustomPropertyNames(PIID piid,
                      java.lang.String activityName)
Retrieves the custom property names of the specified
 activity instance using the process instance object ID
 and the activity instance name.

java.util.List
getCustomPropertyNames(PTID ptid)
Retrieves the custom property names of the specified process template
 using the process template ID.

java.util.List
getCustomPropertyNames(java.lang.String identifier)
Retrieves the custom property names of the specified process template, process instance,
 or activity instance using a string representation of the object ID.

java.util.List
getCustomPropertyNames(java.lang.String identifier,
                      java.lang.String activityName)
Retrieves the custom property names of the specified
 activity instance using a string representation of the process instance object ID
 and the activity instance name.

ClientObjectWrapper
getFaultMessage(AIID aiid)
Retrieves the fault message of the specified activity instance using the activity instance ID.

ClientObjectWrapper
getFaultMessage(PIID piid)
Retrieves the fault message of the specified process instance using the process instance ID.

ClientObjectWrapper
getFaultMessage(java.lang.String identifier)
Retrieves the fault message of the specified process or activity instance using
 a string representation of the process or activity instance ID.

java.util.List
getFaultNames(AIID aiid)
Retrieves the fault names defined for the specified activity instance
 using the activity instance ID.

java.util.List
getFaultNames(java.lang.String aiid)
Retrieves the fault names defined for the specified activity instance
 using a string representation of the activity instance ID.

byte[]
getGraphics(PTID ptid)
Retrieves a graphical representation of the specified process template using
 the process template ID.

byte[]
getGraphics(java.lang.String identifier)
Retrieves a graphical representation of the specified process template using
 a string representation of the process template ID or the process template name.

ClientObjectWrapper
getInitialVariableValue(AIID aiid,
                       java.lang.String variableName)
Retrieves the initial value of the specified variable visible
 by the specified activity instance using the activity instance ID.

ClientObjectWrapper
getInitialVariableValue(PIID piid,
                       java.lang.String variableName)
Retrieves the initial value of the specified variable
 of the specified process instance using the process instance ID.

ClientObjectWrapper
getInitialVariableValue(PIID piid,
                       java.lang.String activityName,
                       java.lang.String variableName)
Retrieves the initial value of the specified variable visible
 by the specified activity
 using the process instance ID and the activity name.

ClientObjectWrapper
getInitialVariableValue(java.lang.String identifier,
                       java.lang.String variableName)
Retrieves the initial value of the specified variable of the specified process instance
 or the specified variable visible by the specified activity instance
 using a string representation of the process or activity instance ID.

ClientObjectWrapper
getInitialVariableValue(java.lang.String piid,
                       java.lang.String activityName,
                       java.lang.String variableName)
Retrieves the initial value of the specified variable visible
 by the specified activity
 using a string representation of the process instance ID and the activity name.

InlineCustomProperty
getInlineCustomProperty(PIID piid,
                       java.lang.String propertyName)
Retrieves the named inline custom property of the specified process instance using the process instance ID.

InlineCustomProperty
getInlineCustomProperty(PTID ptid,
                       java.lang.String propertyName)
Retrieves the named inline custom property of the specified process template using the process template ID.

InlineCustomProperty
getInlineCustomProperty(java.lang.String identifier,
                       java.lang.String propertyName)
Retrieves the named inline custom property of the specified process template
 or process instance using a string representation of the object ID.

CustomClientSettings
getInputClientUISettings(PIID piid)
Retrieves client interface settings for the input message of the specified
 process instance using the process instance ID.

CustomClientSettings
getInputClientUISettings(java.lang.String piid)
Retrieves client interface settings for the input message of the specified
 process instance using a string representation of the process instance ID.

ClientObjectWrapper
getInputMessage(AIID aiid)
Retrieves the input message of the specified activity instance using the activity instance ID.

ClientObjectWrapper
getInputMessage(PIID piid)
Retrieves the input message of the specified process instance using the process instance ID.

ClientObjectWrapper
getInputMessage(java.lang.String identifier)
Retrieves the input message of the specified process or activity instance using a string representation of the ID.

java.util.List
getInputVariableNames(AIID aiid)
Retrieves the names of all input variables for the specified activity instance
 using the activity instance ID.

java.util.List
getInputVariableNames(PIID piid,
                     java.lang.String activityName)
Retrieves the names of the input variables for the specified activity
 using the process instance ID and the activity name.

java.util.List
getInputVariableNames(java.lang.String aiid)
Retrieves the names of all input variables for the specified activity instance
 using a string representation of the activity instance ID.

java.util.List
getInputVariableNames(java.lang.String piid,
                     java.lang.String activityName)
Retrieves the names of the input variables for the specified activity
 using a string representation of the process instance ID and the activity name.

java.util.List
getJumpTargetNames(AIID aiid)
Retrieves the names of all activities that can be jumped to from the specified
 activity instance using the activity instance ID.

java.util.List
getJumpTargetNames(java.lang.String aiid)
Retrieves the names of all activities that can be jumped to from the specified
 activity instance using a string representation of the activity instance ID.

byte[]
getMappingToGraphics(PTID ptid)
Retrieves the descriptive information of the graphical representation of the specified process template using
 the process template ID.

byte[]
getMappingToGraphics(java.lang.String identifier)
Retrieves the descriptive information of the graphical representation of
 the specified process template using
 a string representation of the process template ID or the process template name.

java.lang.String
getMessageTextOfException(java.util.Locale locale,
                         java.lang.String messageKey,
                         java.lang.Object[] variableValues)
Retrieves the message text associated to the specified message key and locale.

java.util.List
getMigrationTargets(PTID ptid)
Retrieves the object IDs of all process templates that can be migration targets for
 a process instance derived from
 the process template specified by the process template ID.

java.util.List
getMigrationTargets(java.lang.String ptid)
Retrieves the object IDs of all process templates that can be migration targets for
 a process instance derived from
 the process template specified by a string representation of the process template ID.

int
getOperationMode()
Indicates whether the Business Flow Manager database is used as an archive.

LinkTemplateData[]
getOutgoingLinks(AIID aiid)
Retrieves information about the links starting at the specified activity instance
 using the activity instance ID.

LinkTemplateData[]
getOutgoingLinks(java.lang.String aiid)
Retrieves information about the links starting at the specified activity instance
 using a string representation of the activity instance object ID.

CustomClientSettings
getOutputClientUISettings(PIID piid)
Retrieves client interface settings for the output message of the specified
 process instance using the process instance ID.

CustomClientSettings
getOutputClientUISettings(java.lang.String piid)
Retrieves client interface settings for the output message of the specified
 process instance using a string representation of the process instance ID.

ClientObjectWrapper
getOutputMessage(AIID aiid)
Retrieves the output message of the specified activity instance using the activity instance ID.

ClientObjectWrapper
getOutputMessage(PIID piid)
Retrieves the output message of the specified process instance using the process instance ID.

ClientObjectWrapper
getOutputMessage(java.lang.String identifier)
Retrieves the output message of the specified process or activity instance using a string representation of the ID.

java.util.List
getOutputVariableNames(AIID aiid)
Retrieves the names of all output variables for the specified activity instance
 using the activity instance ID.

java.util.List
getOutputVariableNames(PIID piid,
                      java.lang.String activityName)
Retrieves the names of the output variables for the specified activity
 using the process instance ID and the activity name.

java.util.List
getOutputVariableNames(java.lang.String identifier)
Retrieves the names of all output variables for the specified activity instance
 using a string representation of the activity instance ID.

java.util.List
getOutputVariableNames(java.lang.String piid,
                      java.lang.String activityName)
Retrieves the names of the output variables for the specified activity
 using a string representation of the process instance ID and the activity name.

TKIID
getParticipatingTaskID(AIID aiid)
Retrieves the object ID of the task instance associated to the
 specified human task activity using the activity instance ID.

TKIID
getParticipatingTaskID(java.lang.String aiid)
Retrieves the object ID of the task instance associated to the
 specified human task activity using a string representation of the activity instance ID.

ProcessInstanceData
getProcessInstance(PIID piid)
Retrieves the specified process instance using the process instance ID.

ProcessInstanceData
getProcessInstance(java.lang.String identifier)
Retrieves the specified process instance using a string representation of the process instance ID
 or the process instance name.

ProcessTemplateData
getProcessTemplate(PTID ptid)
Retrieves the specified process template using the process template ID.

ProcessTemplateData
getProcessTemplate(java.lang.String identifier)
Retrieves the specified process template using a string representation of the process template ID
 or the process template name.

java.util.List
getQueryProperties(PTID ptid)
Retrieves the query properties of the specified process template using
 the process template ID.

java.util.List
getQueryProperties(java.lang.String identifier)
Retrieves the query properties of the specified process template using
 a string representation of the process template ID
 or the process template name.

QueryTableMetaData
getQueryTableMetaData(java.lang.String queryTableName,
                     java.util.Locale locale)
Returns the meta data of the specified query table.

ActivityServiceTemplateData[]
getStartActivities(PTID ptid)
Retrieves information about activities that can start a process instance from the
 specified process template using the process template ID.

ActivityServiceTemplateData[]
getStartActivities(java.lang.String ptid)
Retrieves information about activities that can start a process instance from the
 specified process template
 using a string representation of the process template ID.

StoredQueryData
getStoredQuery(int kind,
              java.lang.String storedQueryName)
Retrieves the specified private or public stored query definition.

StoredQueryData
getStoredQuery(java.lang.String storedQueryName)
Retrieves the specified stored query definition.

StoredQueryData
getStoredQuery(java.lang.String userID,
              java.lang.String storedQueryName)
Retrieves the specified stored query definition for the specified user.

java.lang.String[]
getStoredQueryNames()
Retrieves the names of stored queries persistently stored in the database.

java.lang.String[]
getStoredQueryNames(int kind)
Retrieves the names of private or public stored queries that are persistently stored in the database.

java.lang.String[]
getStoredQueryNames(java.lang.String userID)
Retrieves the names of stored queries that are persistently stored in the database
 for the specified user.

StaffResultSet
getUsersInRole(AIID aiid,
              int role)
Retrieves the users that are members of the specified role for the
 specified activity instance using the activity instance ID.

StaffResultSet
getUsersInRole(PIID piid,
              int role)
Retrieves the users that are members of the specified role for the
 specified process instance using the process instance ID.

StaffResultSet
getUsersInRole(java.lang.String identifier,
              int role)
Retrieves the users that are members of the specified role for the
 specified process or activity instance using string representations of the object IDs.

ClientObjectWrapper
getVariable(AIID aiid,
           java.lang.String variableName)
Retrieves the specified variable visible by the specified activity instance using the activity instance ID.

ClientObjectWrapper
getVariable(PIID piid,
           java.lang.String variableName)
Retrieves the specified variable of the specified process instance using the process instance ID.

ClientObjectWrapper
getVariable(PIID piid,
           java.lang.String activityName,
           java.lang.String variableName)
Retrieves the specified variable visible by the specified activity
 using the process instance ID and the activity name.

ClientObjectWrapper
getVariable(java.lang.String identifier,
           java.lang.String variableName)
Retrieves the specified variable of the specified process instance
 or the specified variable visible by the specified activity instance
 using a string representation of the process or activity instance ID.

ClientObjectWrapper
getVariable(java.lang.String piid,
           java.lang.String activityName,
           java.lang.String variableName)
Retrieves the specified variable  visible by the specified activity
 using a string representation of the process instance ID and the activity name.

java.util.List
getVariableNames(AIID aiid)
Retrieves the names of all variables for the specified activity instance
 using the activity instance ID.

java.util.List
getVariableNames(EHTID ehtid)
Retrieves the names of all variables for the event handler template
 using the event handler template ID.

java.util.List
getVariableNames(PIID piid,
                java.lang.String activityName)
Retrieves the names of the variables of the specified activity
 using the process instance ID and the activity name.

java.util.List
getVariableNames(java.lang.String identifier)
Retrieves the names of the variables of the specified event handler template or
 activity instance using a string representation of the event handler template ID or
 activity instance ID.

java.util.List
getVariableNames(java.lang.String piid,
                java.lang.String activityName)
Retrieves the names of the variables of the specified activity
 using a string representation of the process instance ID and the activity name.

ActivityServiceTemplateData[]
getWaitingActivities(PIID piid)
Retrieves information about activities of a process instance,
 that are in the waiting execution state.

ActivityServiceTemplateData[]
getWaitingActivities(java.lang.String piid)
Retrieves information about activities of a process instance,
 that are in the waiting execution state.

WorkItemData[]
getWorkItems(AIID aiid)
Retrieves work item assignments for the logged-on user and the specified activity instance
 using the activity instance ID.

WorkItemData[]
getWorkItems(PIID piid)
Retrieves work item assignments for the logged-on user and the specified process instance
 using the process instance ID.

WorkItemData[]
getWorkItems(java.lang.String identifier)
Retrieves work item assignments for the logged-on user and a process or activity instance
 using a string representation of the process or activity instance ID.

WorkListData
getWorkList(java.lang.String workListName)
Deprecated. 
As of version 6.0, replaced by getStoredQuery.

int[]
getWorkListActions()
Deprecated. 
As of version 6.0.2, no replacement.
 

java.lang.String[]
getWorkListNames()
Deprecated. 
As of version 6.0, replaced by getStoredQueryNames.
 

void
initializeCorrelationSet(PIID piid,
                        CorrelationSetInstanceData correlationSetInstance)
Initializes the specified correlation set instance
 using the process instance ID.

void
initializeCorrelationSet(java.lang.String piid,
                        CorrelationSetInstanceData correlationSetInstance)
Initializes the specified correlation set instance
 using a string representation of the process instance ID.

PIID
initiate(java.lang.String processTemplateName,
        ClientObjectWrapper inputMessage)
Creates a process instance from the specified process template,
 passes the specified input message, and initiates processing of the process instance.

PIID
initiate(java.lang.String processTemplateName,
        java.lang.String processInstanceName,
        ClientObjectWrapper inputMessage)
Creates a named process instance from the specified process template,
 passes the specified input message, and initiates processing of the process instance.

PIID
initiate(java.lang.String vtid,
        java.lang.String atid,
        java.lang.String processInstanceName,
        ClientObjectWrapper inputMessage)
Creates a named process instance identifying the starting service by a string representation of its ID,
 passes the specified input message, and initiates processing of the process instance.

PIID
initiate(VTID vtid,
        ATID atid,
        java.lang.String processInstanceName,
        ClientObjectWrapper inputMessage)
Creates a named process instance identifying the starting service by its ID,
 passes the specified input message, and initiates processing of the process instance.

InitiateAndClaimFirstResult
initiateAndClaimFirst(java.lang.String processTemplateName,
                     java.lang.String processInstanceName,
                     ClientObjectWrapper inputMessage)
Creates a process instance from the specified process template
 and claims the first inline human task for the logged-on user.

InitiateAndClaimFirstResult
initiateAndClaimFirst(java.lang.String vtid,
                     java.lang.String atid,
                     java.lang.String processInstanceName,
                     ClientObjectWrapper inputMessage)
Creates and executes a process instance using string representations of object IDs
 identifying a starting activity service template,
 and claims the first inline human task for the logged-on user.

InitiateAndClaimFirstResult
initiateAndClaimFirst(java.lang.String processTemplateName,
                     java.lang.String vtid,
                     java.lang.String atid,
                     java.lang.String processInstanceName,
                     ClientObjectWrapper inputMessage)
Deprecated. 
As of version 7.5, replaced by initiateAndClaimFirst.

InitiateAndClaimFirstResult
initiateAndClaimFirst(java.lang.String processTemplateName,
                     java.lang.String nameSpace,
                     java.lang.String portType,
                     java.lang.String operation,
                     java.lang.String processInstanceName,
                     ClientObjectWrapper inputMessage)
Creates a process instance from the specified process template
 by calling the specified starting service,
 and claims the first inline human task for the logged-on user.

InitiateAndClaimFirstResult
initiateAndClaimFirst(java.lang.String processTemplateName,
                     VTID vtid,
                     ATID atid,
                     java.lang.String processInstanceName,
                     ClientObjectWrapper inputMessage)
Deprecated. 
As of version 7.5, replaced by initiateAndClaimFirst.

InitiateAndClaimFirstResult
initiateAndClaimFirst(VTID vtid,
                     ATID atid,
                     java.lang.String processInstanceName,
                     ClientObjectWrapper inputMessage)
Creates and executes a process instance using object IDs
 identifying a starting activity service template,
 and claims the first inline human task for the logged-on user.

PIID
initiateAndSuspend(java.lang.String processTemplateName,
                  java.lang.String processInstanceName,
                  ClientObjectWrapper inputMessage)
Creates a process instance from the specified process template
 and immediately suspends navigation of the process instance.

PIID
initiateAndSuspend(java.lang.String vtid,
                  java.lang.String atid,
                  java.lang.String processInstanceName,
                  ClientObjectWrapper inputMessage)
Creates a process instance
 by calling the specified starting service identified by string representations of its object IDs,
 and immediately suspends navigation of the process instance.

PIID
initiateAndSuspend(java.lang.String processTemplateName,
                  java.lang.String nameSpace,
                  java.lang.String portType,
                  java.lang.String operation,
                  java.lang.String processInstanceName,
                  ClientObjectWrapper inputMessage)
Creates a process instance from the specified process template
 by calling the specified starting service,
 and immediately suspends navigation of the process instance.

PIID
initiateAndSuspend(VTID vtid,
                  ATID atid,
                  java.lang.String processInstanceName,
                  ClientObjectWrapper inputMessage)
Creates a process instance
 by calling the specified starting service identified by its object IDs,
 and immediately suspends navigation of the process instance.

boolean
isBusinessProcessAdministrator()
Indicates whether the logged-on user is a business process administrator (system administrator).

boolean
isBusinessProcessMonitor()
Indicates whether the logged-on user is a business process monitor
 (system monitor).

void
jump(AIID aiid,
    java.lang.String targetActivityName)
Jumps from an activity instance identified by the activity instance ID
 to the specified target activity.

void
jump(java.lang.String aiid,
    java.lang.String targetActivityName)
Jumps from an activity instance
 identified by a string representation of the activity instance ID
 to the specified target activity.

ProcessInstanceData
migrate(PIID piid,
       PTID ptid)
Migrates the process instance
 identified by the process instance ID to an instance of the specified process template.

ProcessInstanceData
migrate(java.lang.String piid,
       java.lang.String ptid)
Migrates the process instance
 identified by a string representation of the process instance ID
 to an instance of the specified process template.

void
newWorkList(java.lang.String workListName,
           java.lang.String selectClause,
           java.lang.String whereClause,
           java.lang.String orderByClause,
           java.lang.Integer threshold,
           java.util.TimeZone timeZone)
Deprecated. 
As of version 6.0, replaced by createStoredQuery.

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
As of version 6.0.2,  replaced by query(Sting storedQueryName, Integer skipTuples, List parameters),

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

ProcessTemplateData[]
queryProcessTemplates(java.lang.String whereClause,
                     java.lang.String orderByClause,
                     java.lang.Integer threshold,
                     java.util.TimeZone timeZone)
Retrieves process templates persistently stored in the database.

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

void
rescheduleTimer(AIID aiid,
               TimerSpecification timerSpecification)
Reschedules timers of the specified active activity instance
 using the activity instance ID and a timer specification.

void
rescheduleTimer(java.lang.String aiid,
               TimerSpecification timerSpecification)
Reschedules timers of the specified active activity instance
 using a string representation of the activity instance ID and a timer specification.

void
restart(PIID piid)
Restarts the specified top-level process instance and its non-autonomous subprocesses
 using the process instance ID.

void
restart(java.lang.String piid)
Restarts the specified top-level process instance and its non-autonomous subprocesses
 using the process instance ID.

void
resume(PIID piid)
Resumes the specified top-level process instance and its non-autonomous
 subprocesses using the process instance ID.

void
resume(java.lang.String piid)
Resumes the specified top-level process instance and its non-autonomous
 subprocesses using a string representation of the process instance ID.

void
sendMessage(PIID piid,
           VTID vtid,
           ATID atid,
           ClientObjectWrapper message)
Sends the specified message to the specified activity service and process instance
 using the process instance, activity service template, and activity template IDs.

PIID
sendMessage(PTID ptid,
           java.lang.String nameSpace,
           java.lang.String portType,
           java.lang.String operation,
           ClientObjectWrapper message)
Sends the specified message to the specified process template using the process template ID and
 the namespace, port type, and operation of the service to be called.

PIID
sendMessage(java.lang.String vtid,
           java.lang.String atid,
           ClientObjectWrapper message)
Sends the specified message to the specified activity service
 using a string representation of the activity service template ID and the activity template ID.

void
sendMessage(java.lang.String piid,
           java.lang.String vtid,
           java.lang.String atid,
           ClientObjectWrapper message)
Sends the specified message to the specified activity service and process instance
 using a string representation of the process instance, activity service template,
 and activity template IDs.

PIID
sendMessage(java.lang.String processTemplateName,
           java.lang.String nameSpace,
           java.lang.String portType,
           java.lang.String operation,
           ClientObjectWrapper message)
Sends the specified message to the specified process template using
 the namespace, port type, and operation of the service to be called.

void
sendMessage(java.lang.String processTemplateName,
           java.lang.String nameSpace,
           java.lang.String portType,
           java.lang.String operation,
           ClientObjectWrapper message,
           ReplyContextWrapper replyContext)
Sends the specified message to the specified process template, using
 the namespace, port type, and operation of the service to be called and returns the
 result of operation.

void
sendMessage(java.lang.String processTemplateName,
           java.lang.String nameSpace,
           java.lang.String portType,
           java.lang.String operation,
           ClientObjectWrapper message,
           ReplyContextWrapper replyContext,
           int invocationCount,
           java.lang.String requestId)
Sends the specified message to the specified process template, using
 the namespace, port type, and operation of the service to be called and returns the
 result of operation, in case of errors trying multiple times.

PIID
sendMessage(VTID vtid,
           ATID atid,
           ClientObjectWrapper message)
Sends the specified message to the specified activity service using the activity service template ID
 and the activity template ID.

void
setBinaryCustomProperty(AIID aiid,
                       BinaryCustomProperty property)
Stores custom-specific binary values for the specified activity instance using
 the activity instance ID.

void
setBinaryCustomProperty(PIID piid,
                       BinaryCustomProperty property)
Stores custom-specific binary values for the specified process instance using
 the process instance ID.

void
setBinaryCustomProperty(PIID piid,
                       java.lang.String activityName,
                       BinaryCustomProperty property)
Stores custom-specific binary values for the specified activity instance using
 the process instance ID and the activity name.

void
setBinaryCustomProperty(java.lang.String identifier,
                       BinaryCustomProperty property)
Stores custom-specific binary values for the specified process or activity instance
 using a string representation of the process or activity instance ID.

void
setBinaryCustomProperty(java.lang.String piid,
                       java.lang.String activityName,
                       BinaryCustomProperty property)
Stores custom-specific binary values for the specified activity instance using
 a string representation of the process instance ID and the activity name.

void
setCustomProperty(AIID aiid,
                 java.lang.String propertyName,
                 java.lang.String propertyValue)
Stores custom-specific values for the specified activity instance using the activity instance ID.

void
setCustomProperty(PIID piid,
                 java.lang.String propertyName,
                 java.lang.String propertyValue)
Stores custom specific values for the specified process instance using the process instance ID.

void
setCustomProperty(PIID piid,
                 java.lang.String activityName,
                 java.lang.String propertyName,
                 java.lang.String propertyValue)
Stores custom-specific values for the specified activity instance
 using the process instance ID and the activity name.

void
setCustomProperty(java.lang.String identifier,
                 java.lang.String propertyName,
                 java.lang.String propertyValue)
Stores custom-specific values for the specified process or activity instance
 using a string representation of the object ID.

void
setCustomProperty(java.lang.String identifier,
                 java.lang.String activityName,
                 java.lang.String propertyName,
                 java.lang.String propertyValue)
Stores custom-specific values for the specified activity instance
 using a string representation of the  process instance and the activity instance name.

void
setFaultMessage(AIID aiid,
               java.lang.String faultName,
               ClientObjectWrapper faultMessage)
Stores the specified fault message for the specified activity instance into the database
 using the activity instance ID.

void
setFaultMessage(java.lang.String aiid,
               java.lang.String faultName,
               ClientObjectWrapper faultMessage)
Stores the specified fault message for the specified activity instance into the database
 using a string representation of the activity instance ID.

void
setInlineCustomProperties(PIID piid,
                         java.util.List customProperties)
Stores custom-specific values for the specified process instance using
 the process instance ID.

void
setInlineCustomProperties(java.lang.String piid,
                         java.util.List customProperties)
Stores custom-specific values for the specified process instance using
 a string representation of the process instance ID.

java.util.List
setInlineCustomProperty(PIID[] piids,
                       InlineCustomProperty property)
Stores custom-specific values for the specified process instances using
 process instance IDs.

void
setInlineCustomProperty(PIID piid,
                       InlineCustomProperty property)
Stores custom specific values for the specified process instance using the process instance ID.

java.util.List
setInlineCustomProperty(java.lang.String[] piids,
                       InlineCustomProperty property)
Stores custom-specific values for the specified proeess instances using
 string representations of the process instance IDs.

void
setInlineCustomProperty(java.lang.String piid,
                       InlineCustomProperty property)
Stores custom-specific values for the specified process instance
 using a string representation of the process instance ID.

void
setOutputMessage(AIID aiid,
                ClientObjectWrapper outputMessage)
Stores the output message of the specified activity instance into the database using the activity instance ID.

void
setOutputMessage(java.lang.String aiid,
                ClientObjectWrapper outputMessage)
Stores the output message of the specified activity instance into the database
 using a string representation of the activity instance ID.

void
setVariable(AIID aiid,
           java.lang.String variableName,
           ClientObjectWrapper message)
Sets the specified variable
 visible by the activity instance
 using the variable name and the associated activity instance ID.

void
setVariable(PIID piid,
           java.lang.String variableName,
           ClientObjectWrapper message)
Sets the specified variable using the variable name and
 the associated process instance ID.

void
setVariable(PIID piid,
           java.lang.String activityName,
           java.lang.String variableName,
           ClientObjectWrapper message)
Sets the specified variable visible by the activity
 using the process instance ID and the activity and variable names.

void
setVariable(java.lang.String identifier,
           java.lang.String variableName,
           ClientObjectWrapper message)
Sets the specified variable using the variable name and
 a string representation of the associated process or activity instance ID.

void
setVariable(java.lang.String piid,
           java.lang.String activityName,
           java.lang.String variableName,
           ClientObjectWrapper message)
Sets the specified variable visible by the activity
 using a string representation of the process instance ID and the activity
 and variable names.

void
skip(AIID aiid)
Skips the activity instance using the activity instance ID.

void
skip(PIID piid,
    java.lang.String activityName)
Skips the specified activity instance using the associated process instance ID
 and the activity instance name.

void
skip(java.lang.String aiid)
Skips the activity instance using a string representation of the
 activity instance ID.

void
skip(java.lang.String piid,
    java.lang.String activityName)
Skips the specified activity instance using a string representation of the
 associated process instance ID and the activity name.

void
skipAndJump(AIID aiid,
           java.lang.String targetActivityName)
Skips the activity instance using the activity instance ID
 and continues navigation at the specified target activity.

void
skipAndJump(java.lang.String aiid,
           java.lang.String targetActivityName)
Skips the activity instance using a string representation of the
 activity instance ID and continues navigation at the specified target activity.

void
suspend(PIID piid)
Suspends the specified top-level process instance and its non-autonomous subprocesses
 using the process instance ID.

void
suspend(PIID piid,
       java.util.Calendar deadline)
Suspends the specified top-level process instance and its non-autonomous subprocesses
 until the specified point in time is reached using the process instance ID.

void
suspend(PIID piid,
       int duration)
Suspends the specified top-level process instance and its non-autonomous subprocesses
 for the specified duration using the process instance ID.

void
suspend(PIID piid,
       java.lang.String timeoutExpression,
       java.lang.String calendarName,
       java.lang.String JNDINameOfCalendar)
Suspends the specified top-level process instance and its non-autonomous subprocesses
 for a calendar specific time using the process instance ID.

void
suspend(java.lang.String piid)
Suspends the specified top-level process instance and its non-autonomous subprocesses
 using a string representation of the process instance ID.

void
suspend(java.lang.String piid,
       java.util.Calendar deadline)
Suspends the specified top-level process instance and its non-autonomous subprocesses
 until the specified point in time is reached using a string representation of the process instance ID.

void
suspend(java.lang.String piid,
       int duration)
Suspends the specified top-level process instance and its non-autonomous subprocesses
 for the specified duration using a string representation of the process instance ID.

void
suspend(java.lang.String piid,
       java.lang.String timeoutExpression,
       java.lang.String calendarName,
       java.lang.String JNDINameOfCalendar)
Suspends the specified top-level process instance and its non-autonomous subprocesses
 for a calendar specific time using a string representation of the process instance ID.

boolean
testMigration(PIID piid,
             PTID ptid)
Checks whether the process instance identified by the process instance ID
 can be migrated to an instance of the specified process template.

boolean
testMigration(java.lang.String piid,
             java.lang.String ptid)
Checks whether the process instance
 identified by a string representation of the process instance ID can be migrated
 to an instance of the specified process template.

void
transferWorkItem(AIID aiid,
                int assignmentReason,
                java.lang.String fromOwner,
                java.lang.String toOwner)
Transfers the specified work item for the specified activity instance
 using the activity instance ID.

void
transferWorkItem(PIID piid,
                int assignmentReason,
                java.lang.String fromOwner,
                java.lang.String toOwner)
Transfers the specified work item for the specified process instance
 using the process instance ID.

void
transferWorkItem(java.lang.String identifier,
                int assignmentReason,
                java.lang.String fromOwner,
                java.lang.String toOwner)
Transfers the specified work item for a process or activity instance
 using a string representation
 of either the process or activity instance ID.

void
uninitializeCorrelationSet(PIID piid,
                          java.lang.String correlationSetName)
Uninitializes the specified correlation set instance
 using the process instance ID and the correlation set name.

void
uninitializeCorrelationSet(java.lang.String piid,
                          java.lang.String correlationSetName)
Uninitializes the specified correlation set instance
 using a string representation of the process instance ID and the correlation set name.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - call
ClientObjectWrapper call(java.lang.String processTemplateName,
                       ClientObjectWrapper inputMessage)
                         throws ArchiveUnsupportedOperationException,
                                CreateFailedException,
                                EngineAdministratorCannotBeResolvedException,
                                EngineCannotCreateWorkItemException,
                                EngineCannotInitializeVariableException,
                                EngineCannotOpenCompensationSphereException,
                                EngineCannotRunSynchronousException,
                                EngineNotAuthorizedException,
                                EngineProcessModelDoesNotExistException,
                                EngineProcessModelStoppedException,
                                EngineWrongMessageTypeException,
                                FaultReplyException,
                                InvalidLengthException,
                                ProcessException,
                                ServiceNotUniqueException,
                                UnexpectedFailureException,
                                java.rmi.RemoteException,
                                javax.ejb.EJBException
Creates and executes a process instance that is derived from the specified
 process template.
 An input message can be passed to specify initial values for the process instance.
 
 This method returns only when the execution of the process instance finishes with
 the result of execution. If a fault occurs, an exception is thrown.
 
 The process template must specify that derived process instances can run synchronously,
 that is, as a microflow and must return a reply.
 The process must start with a single receive or pick activity.
 The pick activity must specify a single onMessage so that the service to be called can be identified.
 
 A process instance is only created when the currently valid version of the specified process template
 is started and when it belongs to a started application.
 
 This method is not supported in archive mode.
Parameters:processTemplateName - The name of the process template for which an instance is to be created and executed.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The object
    wrapped by the ClientObjectWrapper must be serializable.
 

Returns:ClientObjectWrapper -
    The output message that denotes the result of execution.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineCannotRunSynchronousException
EngineNotAuthorizedException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineWrongMessageTypeException
FaultReplyException
InvalidLengthException
ProcessException
ServiceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - call
ClientObjectWrapper call(java.lang.String vtid,
                       java.lang.String atid,
                       ClientObjectWrapper inputMessage)
                         throws ArchiveUnsupportedOperationException,
                                CreateFailedException,
                                EngineCannotRunSynchronousException,
                                EngineNotAuthorizedException,
                                EngineProcessModelDoesNotExistException,
                                EngineProcessModelStoppedException,
                                FaultReplyException,
                                IdWrongFormatException,
                                IdWrongTypeException,
                                ObjectDoesNotExistException,
                                ProcessException,
                                UnexpectedFailureException,
                                java.rmi.RemoteException,
                                javax.ejb.EJBException
Creates and executes a process instance using a string representation
 of the activity service template ID and the activity template ID.
 An input message can be passed to specify initial values for the process instance.
 
 This method returns only when the execution of the process instance finishes with
 the result of execution. If a fault occurs, an exception is thrown.
 
 The process template must specify that derived process instances can run synchronously,
 that is, as a microflow and must return a reply.
 
 A process instance is only created when the process template containing the specified
 starting service is started and when it belongs to a started application.
 
 This method is not supported in archive mode.
Parameters:vtid - The string representation of the activity service template object ID. This
    is used to identify the starting service to be called.atid - A string representation of the activity template ID. This is used
    to identify the activity the service belongs to.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The object
    wrapped by the ClientObjectWrapper must be serializable.
 

Returns:ClientObjectWrapper -
    The output message that denotes the result of execution.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineCannotRunSynchronousException
EngineNotAuthorizedException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
FaultReplyException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
ProcessException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - call
ClientObjectWrapper call(VTID vtid,
                       ATID atid,
                       ClientObjectWrapper inputMessage)
                         throws ArchiveUnsupportedOperationException,
                                CreateFailedException,
                                EngineCannotRunSynchronousException,
                                EngineNotAuthorizedException,
                                EngineProcessModelDoesNotExistException,
                                EngineProcessModelStoppedException,
                                FaultReplyException,
                                IdWrongFormatException,
                                IdWrongTypeException,
                                ObjectDoesNotExistException,
                                ProcessException,
                                UnexpectedFailureException,
                                java.rmi.RemoteException,
                                javax.ejb.EJBException
Creates and executes a process instance using
 the activity service template ID and the activity template ID.
 An input message can be passed to specify initial values for the process instance.
 
 This method returns only when the execution of the process instance finishes with
 the result of execution. If a fault occurs, an exception is thrown.
 
 The process template must specify that derived process instances can run as a microflow
 and must return a reply.
 
 A process instance is only created when the process template containing the specified
 starting service is started and when it belongs to a started application.
 
 This method is not supported in archive mode.
Parameters:vtid - The object ID of the activity service template
    that is used to identify the starting service to be called.atid - The object ID of the activity the activity service template belongs to.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The object
    wrapped by the ClientObjectWrapper must be serializable.
 

Returns:ClientObjectWrapper -
    The output message that denotes the result of execution.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineCannotRunSynchronousException
EngineNotAuthorizedException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
FaultReplyException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
ProcessException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - call
ClientObjectWrapper call(java.lang.String processTemplateName,
                       java.lang.String nameSpace,
                       java.lang.String portType,
                       java.lang.String operation,
                       ClientObjectWrapper inputMessage)
                         throws ArchiveUnsupportedOperationException,
                                CreateFailedException,
                                EngineAdministratorCannotBeResolvedException,
                                EngineCannotCreateWorkItemException,
                                EngineCannotInitializeVariableException,
                                EngineCannotOpenCompensationSphereException,
                                EngineCannotRunSynchronousException,
                                EngineNotAuthorizedException,
                                EngineParameterNullException,
                                EngineProcessModelDoesNotExistException,
                                EngineProcessModelStoppedException,
                                EngineWrongMessageTypeException,
                                FaultReplyException,
                                InvalidLengthException,
                                ProcessException,
                                ServiceNotUniqueException,
                                UnexpectedFailureException,
                                java.rmi.RemoteException,
                                javax.ejb.EJBException
Creates and executes a process instance that is derived from the specified
 process template by calling the specified starting service.
 An input message can be passed to specify initial values for the process instance.
 
 This method returns only when the execution of the process instance finishes with
 the result of execution. If a fault occurs, an exception is thrown.
 
 The process template must specify that derived process instances can run synchronously,
 that is, as a microflow and must return a reply.
 The process must start with a single receive or pick activity.
 
 A process instance is only created when the currently valid version of the specified process template
 is started and when it belongs to a started application.
 
 This method is not supported in archive mode.
Parameters:processTemplateName - The name of the process template for which an instance is to be created and executed.nameSpace - The namespace of the service to be called.portType - The name of the port type.operation - The operation name of the service.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The object
    wrapped by the ClientObjectWrapper must be serializable.
 
Returns:ClientObjectWrapper -
    The output message that denotes the result of execution.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineCannotRunSynchronousException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineWrongMessageTypeException
FaultReplyException
InvalidLengthException
ProcessException
ServiceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - callServiceWithReplyContext
void callServiceWithReplyContext(java.lang.String vtid,
                               java.lang.String atid,
                               java.lang.String processInstanceName,
                               ClientObjectWrapper inputMessage,
                               ReplyContextWrapper replyContext,
                               int invocationCount,
                               java.lang.String requestId)
                                 throws ArchiveUnsupportedOperationException,
                                        CreateFailedException,
                                        EngineAdministratorCannotBeResolvedException,
                                        EngineCannotCreateWorkItemException,
                                        EngineCannotInitializeVariableException,
                                        EngineCannotOpenCompensationSphereException,
                                        EngineCannotUnwrapReplyContextException,
                                        EngineNotAuthorizedException,
                                        EngineProcessInstanceNameNotUniqueException,
                                        EngineProcessModelDoesNotExistException,
                                        EngineProcessModelStoppedException,
                                        EngineWrongMessageTypeException,
                                        FaultReplyException,
                                        IdWrongFormatException,
                                        InvalidLengthException,
                                        MissingPartsException,
                                        ProcessException,
                                        ProcessInstanceNotUniqueException,
                                        SendReplyErrorException,
                                        ServiceNotUniqueException,
                                        UnexpectedFailureException,
                                        java.rmi.RemoteException,
                                        javax.ejb.EJBException
Creates and executes a process instance using the activity service template ID and the activity template ID
 and asynchronously waits for the result.
 An input message can be passed to specify initial values for the process instance.
 
 A process instance is only created when the process template containing the specified
 starting service is started and when it belongs to a started application.
 
 This method is not supported in archive mode.
Parameters:vtid - The string representation of the activity service template object ID. This
    is used to identify the starting service to be called.atid - A string representation of the activity template ID. This is used
    to identify the activity the service belongs to.processInstanceName - The name of the process instance to be created; must not be greater than 220
    bytes in UTF-8 format. The name must be unique or can be null. This parameter is ignored for microflows.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The object
    wrapped by the ClientObjectWrapper must be serializable.replyContext - The reply context that is to be used to send the result back to the caller.
 invocationCount - The invocation count that specifies the number of invocation attempts. The
    first attempt should be 1, the second 2, and so on. This
    count has to be maintained by the caller and has to be incremented
    after each unsuccesful invocation attempt, that is, when the request ended with an exception. If
    the caller is an MDB that works on behalf of a received JMS message, the JMSXDeliveryCount
    property of the message can be used to count the invocation attempts. A
    value of 0 indicates that the invocation count is not known to the caller.requestId - An ID to identify the request uniquely. If the caller is an MDB that works on
    behalf of a received JMS message, the JMSMessageId can be used as the requestId. A
    value of null implies that a unique requestId is not known to the caller.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineCannotUnwrapReplyContextException
EngineNotAuthorizedException
EngineProcessInstanceNameNotUniqueException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineWrongMessageTypeException
FaultReplyException
IdWrongFormatException
InvalidLengthException
MissingPartsException
ProcessException
ProcessInstanceNotUniqueException
SendReplyErrorException
ServiceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - callServiceWithReplyContext
void callServiceWithReplyContext(VTID vtid,
                               ATID atid,
                               java.lang.String processInstanceName,
                               ClientObjectWrapper inputMessage,
                               ReplyContextWrapper replyContext,
                               int invocationCount,
                               java.lang.String requestId)
                                 throws ArchiveUnsupportedOperationException,
                                        CreateFailedException,
                                        EngineAdministratorCannotBeResolvedException,
                                        EngineCannotCreateWorkItemException,
                                        EngineCannotInitializeVariableException,
                                        EngineCannotOpenCompensationSphereException,
                                        EngineCannotUnwrapReplyContextException,
                                        EngineNotAuthorizedException,
                                        EngineProcessInstanceNameNotUniqueException,
                                        EngineProcessModelDoesNotExistException,
                                        EngineProcessModelStoppedException,
                                        EngineWrongMessageTypeException,
                                        FaultReplyException,
                                        IdWrongFormatException,
                                        InvalidLengthException,
                                        MissingPartsException,
                                        ProcessException,
                                        ProcessInstanceNotUniqueException,
                                        SendReplyErrorException,
                                        ServiceNotUniqueException,
                                        UnexpectedFailureException,
                                        java.rmi.RemoteException,
                                        javax.ejb.EJBException
Creates and executes a process instance using the activity service template ID and the activity template ID
 and asynchronously waits for the result.
 An input message can be passed to specify initial values for the process instance.
 
 A process instance is only created when the process template containing the specified
 starting service is started and when it belongs to a started application.
 
 This method is not supported in archive mode.
Parameters:vtid - The object ID of the activity service template
    that is used to identify the starting service to be called.atid - The object ID of the activity the activity service template belongs to.processInstanceName - The name of the process instance to be created; must not be greater than 220
    bytes in UTF-8 format. The name must be unique or can be null. This parameter is ignored for microflows.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The object
    wrapped by the ClientObjectWrapper must be serializable.replyContext - The reply context that is to be used to send the result back to the caller.
 invocationCount - The invocation count that specifies the number of invocation attempts. The
    first attempt should be 1, the second 2, and so on. This
    count has to be maintained by the caller and has to be incremented
    after each unsuccesful invocation attempt, that is, when the request ended with an exception. If
    the caller is an MDB that works on behalf of a received JMS message, the JMSXDeliveryCount
    property of the message can be used to count the invocation attempts. A
    value of 0 indicates that the invocation count is not known to the caller.requestId - An ID to identify the request uniquely. If the caller is an MDB that works on
    behalf of a received JMS message, the JMSMessageId can be used as the requestId. A
    value of null implies that a unique requestId is not known to the caller.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineCannotUnwrapReplyContextException
EngineNotAuthorizedException
EngineProcessInstanceNameNotUniqueException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineWrongMessageTypeException
FaultReplyException
IdWrongFormatException
InvalidLengthException
MissingPartsException
ProcessException
ProcessInstanceNotUniqueException
SendReplyErrorException
ServiceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - callWithReplyContext
void callWithReplyContext(java.lang.String processTemplateName,
                        ClientObjectWrapper inputMessage,
                        ReplyContextWrapper replyContext)
                          throws ArchiveUnsupportedOperationException,
                                 CreateFailedException,
                                 EngineAdministratorCannotBeResolvedException,
                                 EngineCannotCreateWorkItemException,
                                 EngineCannotInitializeVariableException,
                                 EngineCannotOpenCompensationSphereException,
                                 EngineCannotUnwrapReplyContextException,
                                 EngineNotAuthorizedException,
                                 EngineProcessModelDoesNotExistException,
                                 EngineProcessModelStoppedException,
                                 EngineWrongMessageTypeException,
                                 FaultReplyException,
                                 InvalidLengthException,
                                 MissingPartsException,
                                 ProcessException,
                                 ProcessInstanceNotUniqueException,
                                 SendReplyErrorException,
                                 ServiceNotUniqueException,
                                 UnexpectedFailureException,
                                 java.rmi.RemoteException,
                                 javax.ejb.EJBException
Creates and executes a process instance from the specified process template and
 asynchronously waits for the result.
 An input message can be passed to specify initial values for the process instance.
 
 A process instance is only created when the currently valid version of the specified process template
 is started and when it belongs to a started application.
 
 This method is not supported in archive mode.
Parameters:processTemplateName - The name of the process template for which an instance is to be created and executed.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The object
    wrapped by the ClientObjectWrapper must be serializable.replyContext - The reply context that is to be used to send the result back to the caller.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineCannotUnwrapReplyContextException
EngineNotAuthorizedException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineWrongMessageTypeException
FaultReplyException
InvalidLengthException
MissingPartsException
ProcessException
ProcessInstanceNotUniqueException
SendReplyErrorException
ServiceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - callWithReplyContext
void callWithReplyContext(java.lang.String processTemplateName,
                        java.lang.String processInstanceName,
                        ClientObjectWrapper inputMessage,
                        ReplyContextWrapper replyContext)
                          throws ArchiveUnsupportedOperationException,
                                 CreateFailedException,
                                 EngineAdministratorCannotBeResolvedException,
                                 EngineCannotCreateWorkItemException,
                                 EngineCannotInitializeVariableException,
                                 EngineCannotOpenCompensationSphereException,
                                 EngineCannotUnwrapReplyContextException,
                                 EngineNotAuthorizedException,
                                 EngineProcessInstanceNameNotUniqueException,
                                 EngineProcessModelDoesNotExistException,
                                 EngineProcessModelStoppedException,
                                 EngineWrongMessageTypeException,
                                 FaultReplyException,
                                 InvalidLengthException,
                                 MissingPartsException,
                                 ProcessException,
                                 ProcessInstanceNotUniqueException,
                                 SendReplyErrorException,
                                 ServiceNotUniqueException,
                                 UnexpectedFailureException,
                                 java.rmi.RemoteException,
                                 javax.ejb.EJBException
Creates and executes a named process instance from the specified process template and
 asynchronously waits for the result.
 An input message can be passed to specify initial values for the process instance.
 
 A process instance is only created when the currently valid version of the specified process template
 is started and when it belongs to a started application.
 
 This method is not supported in archive mode.
Parameters:processTemplateName - The name of the process template for which an instance is to be created and executed.processInstanceName - The name of the process instance to be created; must not be greater than 220
    bytes in UTF-8 format. The name must be unique or can be null. This parameter is ignored for microflows.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The object
    wrapped by the ClientObjectWrapper must be serializable.replyContext - The reply context that is to be used to send the result back to the caller.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineCannotUnwrapReplyContextException
EngineNotAuthorizedException
EngineProcessInstanceNameNotUniqueException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineWrongMessageTypeException
FaultReplyException
InvalidLengthException
MissingPartsException
ProcessException
ProcessInstanceNotUniqueException
SendReplyErrorException
ServiceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - callWithReplyContext
void callWithReplyContext(java.lang.String processTemplateName,
                        ClientObjectWrapper inputMessage,
                        ReplyContextWrapper replyContext,
                        int invocationCount,
                        java.lang.String requestId)
                          throws ArchiveUnsupportedOperationException,
                                 CreateFailedException,
                                 EngineAdministratorCannotBeResolvedException,
                                 EngineCannotCreateWorkItemException,
                                 EngineCannotInitializeVariableException,
                                 EngineCannotOpenCompensationSphereException,
                                 EngineCannotUnwrapReplyContextException,
                                 EngineNotAuthorizedException,
                                 EngineProcessModelDoesNotExistException,
                                 EngineProcessModelStoppedException,
                                 EngineWrongMessageTypeException,
                                 FaultReplyException,
                                 InvalidLengthException,
                                 MissingPartsException,
                                 ProcessException,
                                 ProcessInstanceNotUniqueException,
                                 SendReplyErrorException,
                                 ServiceNotUniqueException,
                                 UnexpectedFailureException,
                                 java.rmi.RemoteException,
                                 javax.ejb.EJBException
Creates and executes a process instance from the specified process template and
 asynchronously waits for the result of the uniquely identified request.
 An input message can be passed to specify initial values for the process instance.
 
 A process instance is only created when the currently valid version of the specified process template
 is started and when it belongs to a started application.
 
 This method is not supported in archive mode.
Parameters:processTemplateName - The name of the process template for which an instance is to be created and executed.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The object
    wrapped by the ClientObjectWrapper must be serializable.replyContext - The reply context that is to be used to send the reply back to the caller.invocationCount - The invocation count that specifies the number of invocation attempts. The
    first attempt should be 1, the second 2, and so on. This
    count has to be maintained by the caller and has to be incremented
    after each unsuccesful invocation attempt, that is, when the request ended with an exception. If
    the caller is an MDB that works on behalf of a received JMS message, the JMSXDeliveryCount
    property of the message can be used to count the invocation attempts. A
    value of 0 indicates that the invocation count is not known to the caller.requestId - An ID to identify the request uniquely. If the caller is an MDB that works on
    behalf of a received JMS message, the JMSMessageId can be used as the requestId. A
    value of null implies that a unique requestId is not known to the caller.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineCannotUnwrapReplyContextException
EngineNotAuthorizedException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineWrongMessageTypeException
FaultReplyException
InvalidLengthException
MissingPartsException
ProcessException
ProcessInstanceNotUniqueException
SendReplyErrorException
ServiceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - callWithReplyContext
void callWithReplyContext(java.lang.String processTemplateName,
                        java.lang.String processInstanceName,
                        ClientObjectWrapper inputMessage,
                        ReplyContextWrapper replyContext,
                        int invocationCount,
                        java.lang.String requestId)
                          throws ArchiveUnsupportedOperationException,
                                 CreateFailedException,
                                 EngineAdministratorCannotBeResolvedException,
                                 EngineCannotCreateWorkItemException,
                                 EngineCannotInitializeVariableException,
                                 EngineCannotOpenCompensationSphereException,
                                 EngineCannotUnwrapReplyContextException,
                                 EngineNotAuthorizedException,
                                 EngineProcessInstanceNameNotUniqueException,
                                 EngineProcessModelDoesNotExistException,
                                 EngineProcessModelStoppedException,
                                 EngineWrongMessageTypeException,
                                 FaultReplyException,
                                 InvalidLengthException,
                                 MissingPartsException,
                                 ProcessException,
                                 ProcessInstanceNotUniqueException,
                                 SendReplyErrorException,
                                 ServiceNotUniqueException,
                                 UnexpectedFailureException,
                                 java.rmi.RemoteException,
                                 javax.ejb.EJBException
Creates and executes a named process instance from the specified process template and
 asynchronously waits for the result of the uniquely identified request.
 An input message can be passed to specify initial values for the process instance.
 
 A process instance is only created when the currently valid version of the specified process template
 is started and when it belongs to a started application.
 
 This method is not supported in archive mode.
Parameters:processTemplateName - The name of the process template for which an instance is to be created and executed.processInstanceName - The name of the process instance to be created; must not be greater than 220
    bytes in UTF-8 format. The name must be unique or can be null. This parameter is ignored for microflows.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The
    object wrapped by the ClientObjectWrapper must be serializable.replyContext - The reply context that is to be used to send the reply back to the caller.invocationCount - The invocation count that specifies the number of invocation attempts. The
    first attempt should be 1, the second 2, and so on. This
    count has to be maintained by the caller and has to be incremented
    after each unsuccesful invocation attempt, that is, when the request ended with an exception. If
    the caller is an MDB that works on behalf of a received JMS message, the JMSXDeliveryCount
    property of the message can be used to count the invocation attempts. A
    value of 0 indicates that the invocation count is not known to the caller.requestId - An ID to identify the request uniquely. If the caller is an MDB that works on
    behalf of a received JMS message, the JMSMessageId can be used as the requestId. A
    value of null implies that a unique requestId is not known to the caller.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineCannotUnwrapReplyContextException
EngineNotAuthorizedException
EngineProcessInstanceNameNotUniqueException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineWrongMessageTypeException
FaultReplyException
InvalidLengthException
MissingPartsException
ProcessException
ProcessInstanceNotUniqueException
SendReplyErrorException
ServiceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - callWithUISettings
ProcessResponseWrapper callWithUISettings(java.lang.String processTemplateName,
                                        ClientObjectWrapper inputMessage)
                                          throws ArchiveUnsupportedOperationException,
                                                 CreateFailedException,
                                                 EngineCannotRunSynchronousException,
                                                 EngineNotAuthorizedException,
                                                 EngineProcessModelDoesNotExistException,
                                                 EngineProcessModelStoppedException,
                                                 FaultReplyException,
                                                 ProcessException,
                                                 ServiceNotUniqueException,
                                                 UnexpectedFailureException,
                                                 java.rmi.RemoteException,
                                                 javax.ejb.EJBException
Creates and executes a process instance that is derived from the specified
 process template
 and returns the output message as well as its client UI settings.
 An input message can be passed to specify initial values for the process instance.
 
 This method returns only when the execution of the process instance finishes with
 the result of execution. If a fault occurs, an exception is thrown.
 
 The process template must specify that derived process instances can run as a microflow
 and must return a reply.
 The process must start with a single receive or pick activity.
 The pick activity must specify a single onMessage so that the service to be called can be identified.
 
 A process instance is only created when the currently valid version of the specified process template
 is started and when it belongs to a started application.
 
 This method is not supported in archive mode.
Parameters:processTemplateName - The name of the process template for which an instance is to be created and executed.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The
    object wrapped by the ClientObjectWrapper must be serializable.
 

Returns:ProcessResponseWrapper -
    The output message that denotes the result of execution and its client UI settings -
    refer to ProcessResponseWrapper.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineCannotRunSynchronousException
EngineNotAuthorizedException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
FaultReplyException
ProcessException
ServiceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - callWithUISettings
ProcessResponseWrapper callWithUISettings(java.lang.String vtid,
                                        java.lang.String atid,
                                        ClientObjectWrapper inputMessage)
                                          throws ArchiveUnsupportedOperationException,
                                                 CreateFailedException,
                                                 EngineCannotRunSynchronousException,
                                                 EngineNotAuthorizedException,
                                                 EngineProcessModelDoesNotExistException,
                                                 EngineProcessModelStoppedException,
                                                 FaultReplyException,
                                                 IdWrongFormatException,
                                                 IdWrongTypeException,
                                                 ObjectDoesNotExistException,
                                                 ProcessException,
                                                 ServiceNotUniqueException,
                                                 UnexpectedFailureException,
                                                 java.rmi.RemoteException,
                                                 javax.ejb.EJBException
Creates and executes a process instance
 using a string representation of the activity service template ID and the activity template ID
 and returns the output message as well as its client UI settings.
 An input message can be passed to specify initial values for the process instance.
 
 This method returns only when the execution of the process instance finishes with
 the result of execution. If a fault occurs, an exception is thrown.
 
 The process template must specify that derived process instances can run as a microflow
 and must return a reply.
 
 A process instance is only created when the process template containing the specified
 starting service is started and when it belongs to a started application.
 
 This method is not supported in archive mode.
Parameters:vtid - The string representation of the activity service template object ID. This
    is used to identify the starting service to be called.atid - A string representation of the activity template ID. This is used
    to identify the activity the service belongs to.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The
    object wrapped by the ClientObjectWrapper must be serializable.
 

Returns:ProcessResponseWrapper -
    The output message that denotes the result of execution and its client UI settings -
    refer to ProcessResponseWrapper.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineCannotRunSynchronousException
EngineNotAuthorizedException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
FaultReplyException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
ProcessException
ServiceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - callWithUISettings
ProcessResponseWrapper callWithUISettings(VTID vtid,
                                        ATID atid,
                                        ClientObjectWrapper inputMessage)
                                          throws ArchiveUnsupportedOperationException,
                                                 CreateFailedException,
                                                 EngineCannotRunSynchronousException,
                                                 EngineNotAuthorizedException,
                                                 EngineProcessModelDoesNotExistException,
                                                 EngineProcessModelStoppedException,
                                                 FaultReplyException,
                                                 IdWrongFormatException,
                                                 ObjectDoesNotExistException,
                                                 ProcessException,
                                                 UnexpectedFailureException,
                                                 java.rmi.RemoteException,
                                                 javax.ejb.EJBException
Creates and executes a process instance using the activity service template ID and the activity template ID
 and returns the output message as well as its client UI settings.
 An input message can be passed to specify initial values for the process instance.
 
 This method returns only when the execution of the microflow finishes with
 the result of execution. If a fault occurs, an exception is thrown.
 
 The process template must specify that derived process instances can run as a microflow
 and must return a reply.
 
 A process instance is only created when the process template containing the specified
 starting service is started and when it belongs to a started application.
 
 This method is not supported in archive mode.
Parameters:vtid - The object ID of the activity service template
    that is used to identify the starting service to be called.atid - The object ID of the activity the activity service template belongs to.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The
    object wrapped by the ClientObjectWrapper must be serializable.
 

Returns:ProcessResponseWrapper -
    The output message that denotes the result of execution and its client UI settings -
    refer to ProcessResponseWrapper.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineCannotRunSynchronousException
EngineNotAuthorizedException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
FaultReplyException
IdWrongFormatException
ObjectDoesNotExistException
ProcessException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - cancelClaim
void cancelClaim(java.lang.String aiid)
                 throws ApplicationVetoException,
                        ArchiveUnsupportedOperationException,
                        EngineNotAuthorizedException,
                        EngineWrongKindException,
                        EngineWrongStateException,
                        IdWrongFormatException,
                        IdWrongTypeException,
                        ObjectDoesNotExistException,
                        UnexpectedFailureException,
                        WorkItemManagerException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Cancels the claim of an activity instance using a string representation of the activity instance ID.
 
 The activity instance must have been claimed. It is returned to the ready execution state.
 Any previously stored output or fault message is deleted.
 
 The associated process instance must be in the running, failing, or terminating execution state.
 The caller must be the owner of the activity instance,
 be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
WorkItemManagerException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - cancelClaim
void cancelClaim(AIID aiid)
                 throws ApplicationVetoException,
                        ArchiveUnsupportedOperationException,
                        EngineNotAuthorizedException,
                        EngineWrongKindException,
                        EngineWrongStateException,
                        IdWrongFormatException,
                        ObjectDoesNotExistException,
                        UnexpectedFailureException,
                        WorkItemManagerException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Cancels the claim of an activity instance using the activity instance ID.
 
 The activity instance must have been claimed. It is returned to the ready execution state.
 Any previously stored output or fault message is deleted.
 
 The associated process instance must be in the running, failing, or terminating execution state.
 The caller must be the owner of the activity instance, be an administrator
 of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - The activity instance object ID that is used to identify the activity instance.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
WorkItemManagerException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - cancelClaim
void cancelClaim(java.lang.String aiid,
               boolean keepData)
                 throws ApplicationVetoException,
                        ArchiveUnsupportedOperationException,
                        EngineNotAuthorizedException,
                        EngineWrongKindException,
                        EngineWrongStateException,
                        IdWrongFormatException,
                        IdWrongTypeException,
                        ObjectDoesNotExistException,
                        UnexpectedFailureException,
                        WorkItemManagerException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Cancels the claim of an activity instance and keeps any data that has been set
 using a string representation of the activity instance ID.
 
 The activity instance must have been claimed. It is returned to the ready execution state.
 Any previously stored output or fault message is kept.
 
 The associated process instance must be in the running, failing, or terminating execution state.
 The caller must be the owner of the activity instance, be an administrator
 of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation to the activity instance ID that is used to identify the activity instance.keepData - Specifies whether data saved for the claim activity instance is to be kept.
   True states that any output or fault message set is to be kept.
   False states that any output or fault message set is to be deleted.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
WorkItemManagerException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - cancelClaim
void cancelClaim(AIID aiid,
               boolean keepData)
                 throws ApplicationVetoException,
                        ArchiveUnsupportedOperationException,
                        EngineNotAuthorizedException,
                        EngineWrongKindException,
                        EngineWrongStateException,
                        IdWrongFormatException,
                        ObjectDoesNotExistException,
                        UnexpectedFailureException,
                        WorkItemManagerException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Cancels the claim of an activity instance and keeps any data that has been set
 using the activity instance ID.
 
 The activity instance must have been claimed. It is returned to the ready execution state.
 Any previously stored output or fault message is kept.
 
 The associated process instance must be in the running, failing, or terminating execution state.
 The caller must be the owner of the activity instance, be an administrator
 of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - The activity instance object ID that is used to identify the activity instance.keepData - Specifies whether data saved for the claim activity instance is to be kept.
   True states that any output or fault message set is to be kept.
   False states that any output or fault message set is to be deleted.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
WorkItemManagerException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - cancelSkipRequest
void cancelSkipRequest(java.lang.String piid,
                     java.lang.String activityName)
                       throws ArchiveUnsupportedOperationException,
                              EngineActivityDoesNotExistException,
                              EngineAmbiguousActivityException,
                              EngineNotAuthorizedException,
                              EngineParameterNullException,
                              EngineProcessWrongBuildVersionException,
                              EngineUnknownActivityException,
                              EngineWrongKindException,
                              EngineWrongStateException,
                              IdWrongFormatException,
                              IdWrongTypeException,
                              ObjectDoesNotExistException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Cancels the skip request for the specified activity instance using a string representation of the
 associated process instance ID and the activity name.
 
 The activity can be in any execution state but running.
 The associated process instance must be in the running, failing, or suspended execution state.
 
 The caller must be an administrator of the process instance or
 of a scope that contains the activity instance to be skipped.
 Note that only existing scopes, that is, scopes that are already navigated,
 are considered for the authorization check on scopes.
 
 The activity is "unmarked for skip".
 
 This method is not supported in archive mode.
Parameters:piid - The process instance object ID that is used to identify the process instance.activityName - The name of the activity instance that is to be reset.
 
Throws:
ArchiveUnsupportedOperationException
EngineActivityDoesNotExistException
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessWrongBuildVersionException
EngineUnknownActivityException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - cancelSkipRequest
void cancelSkipRequest(PIID piid,
                     java.lang.String activityName)
                       throws ArchiveUnsupportedOperationException,
                              EngineActivityDoesNotExistException,
                              EngineAmbiguousActivityException,
                              EngineNotAuthorizedException,
                              EngineParameterNullException,
                              EngineProcessWrongBuildVersionException,
                              EngineUnknownActivityException,
                              EngineWrongKindException,
                              EngineWrongStateException,
                              IdWrongFormatException,
                              ObjectDoesNotExistException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Cancels the skip request for the specified activity instance using the associated process instance ID
 and the activity instance name.
 
 The activity can be in any execution state but running.
 The associated process instance must be in the running, failing, or suspended execution state.
 
 The caller must be an administrator of the process instance or
 of a scope that contains the activity instance to be skipped.
 Note that only existing scopes, that is, scopes that are already navigated,
 are considered for the authorization check on scopes.
 
 The activity is "unmarked for skip".
 
 This method is not supported in archive mode.
Parameters:piid - The process instance object ID that is used to identify the process instance.activityName - The name of the activity instance that is to be reset.
 
Throws:
ArchiveUnsupportedOperationException
EngineActivityDoesNotExistException
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessWrongBuildVersionException
EngineUnknownActivityException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - cancelSkipRequest
void cancelSkipRequest(java.lang.String aiid)
                       throws ArchiveUnsupportedOperationException,
                              EngineNotAuthorizedException,
                              EngineProcessWrongBuildVersionException,
                              EngineWrongKindException,
                              EngineWrongStateException,
                              IdWrongFormatException,
                              IdWrongTypeException,
                              ObjectDoesNotExistException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Cancels the skip request for the activity instance using a string representation of the
 activity instance ID.
 
 The activity can be in any execution state but running.
 
 The caller must be an administrator of the process instance or
 of a scope that contains the activity instance to be skipped.
 
 The activity is "unmarked for skip".
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance to be skipped.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineProcessWrongBuildVersionException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - cancelSkipRequest
void cancelSkipRequest(AIID aiid)
                       throws ArchiveUnsupportedOperationException,
                              EngineNotAuthorizedException,
                              EngineProcessWrongBuildVersionException,
                              EngineWrongKindException,
                              EngineWrongStateException,
                              IdWrongFormatException,
                              ObjectDoesNotExistException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Cancels the skip request for the activity instance using the activity instance ID.
 
 The activity can be in any execution state but running.
 
 The caller must be an administrator of the process instance or
 of a scope that contains the activity instance to be skipped.
 
 The activity is "unmarked for skip".
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID to identify the activity instance to be skipped.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineProcessWrongBuildVersionException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - claim
ClientObjectWrapper claim(java.lang.String aiid)
                          throws ArchiveUnsupportedOperationException,
                                 ApplicationVetoException,
                                 EngineCannotCreateWorkItemException,
                                 EngineNotAuthorizedException,
                                 EngineWrongKindException,
                                 EngineWrongStateException,
                                 IdWrongFormatException,
                                 IdWrongTypeException,
                                 InvalidLengthException,
                                 ObjectDoesNotExistException,
                                 UnexpectedFailureException,
                                 WorkItemManagerException,
                                 java.rmi.RemoteException,
                                 javax.ejb.EJBException
Claims a ready activity instance for user processing
 using a string representation of the activity instance ID.
 
 The activity instance must be a human task activity (staff activity) instance and be in the ready
 execution state. The associated process instance must be in the running execution state.
 
 The caller must be a potential owner of the activity instance,
 be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 The execution state of the activity instance is changed to claimed.
 Refer to complete for information on how to complete an activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance to be claimed.
 
Returns:ClientObjectWrapper -
    The input message of the claimed activity instance.
 
Throws:
ArchiveUnsupportedOperationException
ApplicationVetoException
EngineCannotCreateWorkItemException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
WorkItemManagerException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - claim
ClientObjectWrapper claim(AIID aiid)
                          throws ArchiveUnsupportedOperationException,
                                 ApplicationVetoException,
                                 EngineCannotCreateWorkItemException,
                                 EngineNotAuthorizedException,
                                 EngineWrongKindException,
                                 EngineWrongStateException,
                                 IdWrongFormatException,
                                 InvalidLengthException,
                                 ObjectDoesNotExistException,
                                 UnexpectedFailureException,
                                 WorkItemManagerException,
                                 java.rmi.RemoteException,
                                 javax.ejb.EJBException
Claims a ready activity instance for user processing using the activity instance ID.
 
 The activity instance must be a human task activity (staff activity) instance and be in the ready
 execution state. The associated process instance must be in the running execution state.
 
 The caller must be a potential owner of the activity instance,
 be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 The execution state of the activity instance is changed to claimed.
 Refer to complete for information on how to complete an activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID of the activity instance to be claimed.
 

Returns:ClientObjectWrapper -
    The input message of the claimed activity instance.
 
Throws:
ArchiveUnsupportedOperationException
ApplicationVetoException
EngineCannotCreateWorkItemException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
WorkItemManagerException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - claim ActivityInstanceData claim(java.lang.String whereClause, java.lang.String orderByClause, java.util.TimeZone timeZone) throws ArchiveUnsupportedOperationException , ApplicationVetoException , EngineCannotCreateWorkItemException , EngineNotAuthorizedException , UnexpectedFailureException , WorkItemManagerException , java.rmi.RemoteException, javax.ejb.EJBException Claims a ready activity instance for user processing. The activity instance that is claimed is identified by the specified where- and order-by-clauses, and by the following conditions: It must be a human task aka staff activity in the ready execution state. The caller must be a potential owner of the activity instance, be an administrator of the associated process instance, or be an administrator of a scope that contains the activity instance. The first activity instance that qualifies under these conditions is claimed. Refer to complete for information on how to complete an activity instance. This method is not supported in archive mode. Parameters: whereClause - The search condition to be applied to the query domain. The search condition is used to filter the set of ready human task activities that can be claimed by the logged-on user. Its syntax is an SQL where-clause. The following rules apply: If a filter is not to be applied, null must be specified. orderByClause - Sorts the query result set by the values of the columns you identify. The orderby-clause sorts the set of qualifying ready activities; the first activity of the sorted result is claimed. Its syntax is an SQL order-by-clause. Each comma separated part of the order-by-clause must specify a property from the published process views - see the InfoCenter for details. If you identify more that one property, the query result set is ordered by the values of the first property you identify, then by the values of the second property, and so on. If sort criteria are not to be applied, null must be specified. Note that sort criteria are applied on the server, that is, the locale of the server is used for sorting. timeZone - Specifies the time zone of the timestamp constants in the whereClause. If a timezone is not specified, UTC is assumed. Returns: ActivityInstanceData - The activity instance that is claimed. If there is no ready activity instance that qualifies, null is returned. Refer to ActivityInstanceData to view the activity instance properties. Throws: ArchiveUnsupportedOperationException ApplicationVetoException EngineCannotCreateWorkItemException EngineNotAuthorizedException UnexpectedFailureException WorkItemManagerException java.rmi.RemoteException javax.ejb.EJBException Since: 5.1.1 Change History Release Modification 6.1.2 The caller may have administrator rights for the scope that contains the activity instance. 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### claim

```
ActivityInstanceData claim(java.lang.String whereClause,
                         java.lang.String orderByClause,
                         java.util.TimeZone timeZone)
                           throws ArchiveUnsupportedOperationException,
                                  ApplicationVetoException,
                                  EngineCannotCreateWorkItemException,
                                  EngineNotAuthorizedException,
                                  UnexpectedFailureException,
                                  WorkItemManagerException,
                                  java.rmi.RemoteException,
                                  javax.ejb.EJBException
```

The activity instance that is claimed is identified by the specified where- and order-by-clauses,
 and by the following conditions:
 
 It must be a human task aka staff activity in the ready execution state.
 The caller must be a potential owner of the activity instance,
 be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 The first activity instance that qualifies under these conditions
 is claimed.
 
 Refer to complete for information on how to complete an activity instance.
 
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
    instead of integer enumerations. For example, instead of specifying an activity state expression
    "ACTIVITY.STATE=2" , specify "ACTIVITY.STATE=ACTIVITY.STATE.STATE\_READY".
Duplicate apostrophes (') in comparising values. For example,
    "ACTIVITY.NAME='d''automatisation'".
    To specify a where clause that refers to properties of name-value pairs, like
    custom properties, add a one-digit suffix (0-9) to the view name.
    

    For example, to have only tuples returned where an activity custom property "prop1" has
    the value "v1" or where an activity custom property "prop2" has the value v2", the where clause
    can look like
    "ACTIVITY\_ATTRIBUTE1.NAME='prop1' AND ACTIVITY\_ATTRIBUTE1.VALUE='v1' OR
    ACTIVITY\_ATTRIBUTE2.NAME='prop2' AND ACTIVITY\_ATTRIBUTE2.VALUE = 'v2'".
    For performance reasons, you should not use more than one "OR" construct; use "IN" instead.
    

    For example, to retrieve the values of custom properties "prop1" and "prop2" of all activity instances,
    the select clause can look like
    "DISTINCT ACTIVITY.AIID, ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE" and the where-clause
    "ACTIVITY\_ATTRIBUTE1.NAME = 'prop1' AND ACTIVITY\_ATTRIBUTE2.NAME = 'prop2'".

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
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- claimProcessOwnership
void claimProcessOwnership(java.lang.String piid)
                           throws ArchiveUnsupportedOperationException,
                                  EngineNotAuthorizedException,
                                  EngineWrongStateException,
                                  HumanTaskManagerException,
                                  IdWrongFormatException,
                                  IdWrongTypeException,
                                  ObjectDoesNotExistException,
                                  WorkItemManagerException,
                                  UnexpectedFailureException,
                                  java.rmi.RemoteException,
                                  javax.ejb.EJBException
Claims the ownership for the specified process instance
 using a string representation of the process instance ID.
 
 Claiming the ownership for a process instance means that the logged-on user becomes the
 starter of the process instance so that script activities aka java snippets are
 executed with this changed authorization.
 
 The process instance can be in any execution state.
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - A string representation of the process instance object ID that is used to identify
    the process instance.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongStateException
HumanTaskManagerException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- claimProcessOwnership
void claimProcessOwnership(PIID piid)
                           throws ArchiveUnsupportedOperationException,
                                  EngineNotAuthorizedException,
                                  EngineWrongStateException,
                                  HumanTaskManagerException,
                                  IdWrongFormatException,
                                  ObjectDoesNotExistException,
                                  WorkItemManagerException,
                                  UnexpectedFailureException,
                                  java.rmi.RemoteException,
                                  javax.ejb.EJBException
Claims the ownership for the specified process instance
 using the process instance ID.
 
 Claiming the ownership for a process instance means that the logged-on user becomes the
 starter of the process instance so that script activities aka java snippets are
 executed with this changed authorization.
 
 The process instance can be in any execution state.
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance that is used to identify the process instance.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongStateException
HumanTaskManagerException
IdWrongFormatException
ObjectDoesNotExistException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- complete
void complete(java.lang.String aiid)
              throws ApplicationVetoException,
                     ArchiveUnsupportedOperationException,
                     EngineNotAuthorizedException,
                     EngineWrongKindException,
                     EngineWrongStateException,
                     IdWrongFormatException,
                     IdWrongTypeException,
                     ObjectDoesNotExistException,
                     UnexpectedFailureException,
                     java.rmi.RemoteException,
                     javax.ejb.EJBException
Completes a claimed activity instance using a string representation of the activity instance ID.
 
 The activity instance must be in the claimed execution state and the associated
 process instance must be in the running, failing, or terminating execution state.
 
 The caller must be the owner of the activity instance,
 be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 Completion of an activity instance means that user processing has finished and that
 navigation of the process instance can continue. If user processing completed successfully,
 the activity instance
 is put into the finished execution state.
 
 If user processing did not complete successfully, that is, if a fault message is set,
 the activity instance is put into the failed or stopped execution state depending on the
 process instance "continue on error" flag.
 If set into the failed execution state and
 if the fault is not handled, the associated process instance is put into the finished
 execution state or the failed execution state if the fault is also not handled there.
 The exit condition is not evaluated when a fault occurs.
 
 Stored output or fault message values are used to continue navigation.
 
 Note that an output or fault message does not need to be set; navigation
 can continue with an empty message.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance to be completed.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- complete
void complete(AIID aiid)
              throws ApplicationVetoException,
                     ArchiveUnsupportedOperationException,
                     EngineNotAuthorizedException,
                     EngineWrongKindException,
                     EngineWrongStateException,
                     IdWrongFormatException,
                     ObjectDoesNotExistException,
                     UnexpectedFailureException,
                     java.rmi.RemoteException,
                     javax.ejb.EJBException
Completes a claimed activity instance using the activity instance ID.
 
 The activity instance must be in the claimed execution state and the associated
 process instance must be in the running, failing, or terminating execution state.
 
 The caller must be the owner of the activity instance,
 be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 Completion of an activity instance means that user processing has finished and that
 navigation of the process instance can continue. If user processing completed successfully,
 the activity instance
 is put into the finished execution state.
 
 If user processing did not complete successfully, that is, if a fault message is set,
 the activity instance is put into the failed or stopped execution state depending on the
 process instance "continue on error" flag.
 If set into the failed execution state and
 if the fault is not handled, the associated process instance is put into the finished
 execution state or the failed execution state if the fault is also not handled there.
 The exit condition is not evaluated when a fault occurs.
 
 Stored output or fault message values are used to continue navigation.
 
 Note that an output or fault message does not need to be set; navigation
 can continue with an empty message.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID to identify the activity instance to be completed.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- complete
void complete(AIID aiid,
            ClientObjectWrapper output)
              throws ApplicationVetoException,
                     ArchiveUnsupportedOperationException,
                     EngineNotAuthorizedException,
                     EngineParameterNullException,
                     EngineWrongKindException,
                     EngineWrongMessageTypeException,
                     EngineWrongStateException,
                     IdWrongFormatException,
                     ObjectDoesNotExistException,
                     UnexpectedFailureException,
                     java.rmi.RemoteException,
                     javax.ejb.EJBException
Completes a claimed activity instance using the activity instance ID
 and passes the result of user processing.
 
 The activity instance must be in the claimed execution state and the associated
 process instance must be in the running, failing, or terminating execution state.
 
 The caller must be the owner of the activity instance,
 be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 Completion of an activity instance means that user processing finished and that
 navigation of the process instance can continue. An output message
 is passed to denote the successful execution of user processing. The activity instance
 is put into the finished execution state.
 
 When finished, output message values are used to continue navigation.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID to identify the activity instance to be completed.output - The output message that denotes the result of processing.
    When no output is passed or when the contents of the ClientObjectWrapper is null,
    the output variable is updated with null.
    Note that an object wrapped by the ClientObjectWrapper must be serializable.
 
    Any previously set output or fault is ignored.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- complete
void complete(java.lang.String aiid,
            ClientObjectWrapper output)
              throws ApplicationVetoException,
                     ArchiveUnsupportedOperationException,
                     EngineNotAuthorizedException,
                     EngineParameterNullException,
                     EngineWrongKindException,
                     EngineWrongMessageTypeException,
                     EngineWrongStateException,
                     IdWrongFormatException,
                     IdWrongTypeException,
                     ObjectDoesNotExistException,
                     UnexpectedFailureException,
                     java.rmi.RemoteException,
                     javax.ejb.EJBException
Completes a claimed activity instance using a string representation of the activity instance ID
 and passes the result of user processing.
 
 The activity instance must be in the claimed execution state and the associated
 process instance must be in the running, failing, or terminating execution state.
 
 The caller must be the owner of the activity instance,
 be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 Completion of an activity instance means that user processing finished and that
 navigation of the process instance can continue. An output message
 is passed to denote the successful execution of user processing. The activity instance
 is put into the finished execution state.
 
 When finished, output message values are used to continue navigation.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance to be completed.output - The output message that denotes the result of processing.
    When no output is passed or when the contents of the ClientObjectWrapper is null,
    the output variable is updated with null.
    Note that an object wrapped by the ClientObjectWrapper must be serializable.
 
    Any previously set output or fault is ignored.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- complete
void complete(AIID aiid,
            ClientObjectWrapper faultMessage,
            java.lang.String faultName)
              throws ApplicationVetoException,
                     ArchiveUnsupportedOperationException,
                     EngineNotAuthorizedException,
                     EngineParameterNullException,
                     EngineWrongKindException,
                     EngineWrongMessageTypeException,
                     EngineWrongStateException,
                     IdWrongFormatException,
                     ObjectDoesNotExistException,
                     UnexpectedFailureException,
                     java.rmi.RemoteException,
                     javax.ejb.EJBException
Completes a claimed activity instance using the activity instance ID
 and denotes the failing of user processing.
 
 The activity instance must be in the claimed execution state and the associated
 process instance must be in the running, failing, or terminating execution state.
 
 The caller must be the owner of the activity instance,
 be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 Completion of an activity instance means that user processing finished and that
 navigation of the process instance can continue.
 A fault message is passed to denote the unsuccessful execution of user processing.
 The activity instance is put into the stopped execution state when the fault is not handled
 and when the "continue on error" flag of the associated process instance is set.
 Otherwise, it is set into the failed execution state.
 If set into the failed execution state and
 if the fault is not handled, the associated process instance is put into the finished
 execution state or the failed execution state if the fault is also not handled there.
 The exit condition is not evaluated.
 
 Fault message values are used to continue navigation.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID to identify the activity instance to be completed.faultMessage - The fault message. The object
    wrapped by the ClientObjectWrapper must be serializable. Any
    previously set output or fault is ignored.faultName - A fault to denote unsuccessful processing. Must be a fault defined for the activity. Refer
    to getFaultNames.
    Note that the structure of a BPEL fault name is a QName.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- complete
void complete(java.lang.String aiid,
            ClientObjectWrapper faultMessage,
            java.lang.String faultName)
              throws ApplicationVetoException,
                     ArchiveUnsupportedOperationException,
                     EngineNotAuthorizedException,
                     EngineParameterNullException,
                     EngineWrongKindException,
                     EngineWrongMessageTypeException,
                     EngineWrongStateException,
                     IdWrongFormatException,
                     IdWrongTypeException,
                     ObjectDoesNotExistException,
                     UnexpectedFailureException,
                     java.rmi.RemoteException,
                     javax.ejb.EJBException
Completes a claimed activity instance using a string representation of the activity instance ID
 and denotes the failing of user processing.
 
 The activity instance must be in the claimed execution state and the associated
 process instance must be in the running, failing, or terminating execution state.
 
 The caller must be the owner of the activity instance,
 be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 Completion of an activity instance means that user processing finished and that
 navigation of the process instance can continue.
 A fault message is passed to denote the unsuccessful execution of user processing.
 The activity instance is put into the stopped execution state when the fault is not handled
 and when the "continue on error" flag of the associated process instance is set.
 Otherwise, it is set into the failed execution state.
 If set into the failed execution state and
 if the fault is not handled, the associated process instance is put into the finished
 execution state or the failed execution state if the fault is also not handled there.
 The exit condition is not evaluated.
 
 Fault message values are used to continue navigation.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance to be completed.faultMessage - The fault message. The object
    wrapped by the ClientObjectWrapper must be serializable.
    Any previously set output or fault is ignored.faultName - A fault to denote unsuccessful processing. Must be a fault defined for the activity. Refer
    to getFaultNames.
    Note that the structure of a BPEL fault name is a QName.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- completeAndClaimSuccessor
CompleteAndClaimSuccessorResult completeAndClaimSuccessor(java.lang.String aiid,
                                                        ClientObjectWrapper output)
                                                          throws ApplicationVetoException,
                                                                 ArchiveUnsupportedOperationException,
                                                                 EngineNotAuthorizedException,
                                                                 EngineParameterNullException,
                                                                 EngineWrongKindException,
                                                                 EngineWrongMessageTypeException,
                                                                 EngineWrongStateException,
                                                                 IdWrongFormatException,
                                                                 IdWrongTypeException,
                                                                 ObjectDoesNotExistException,
                                                                 DataHandlingException,
                                                                 UnexpectedFailureException,
                                                                 java.rmi.RemoteException,
                                                                 javax.ejb.EJBException
Completes a claimed activity instance using a string representation of the activity instance ID
 and claims a successor activity. In other words,
 this method supports "single person workflow" scenarios.
 
 A successor activity is only claimed when it becomes available within the same
 transaction as the completed activity.
 This means that the transactional boundaries must have been set so that
 the activity to be claimed participates in the same transaction as the completed activity.
 
 The activity instance that is completed must be in the claimed execution state and the associated
 process instance must be in the running, failing, or terminating execution state.
 The caller must be the owner of the activity instance,
 an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 Completion of an activity instance means that user processing finished and that
 navigation of the process instance can continue. An output message
 is passed to denote the successful execution of user processing. The activity instance
 is put into the finished execution state.
 
 Output message values are then used to continue navigation.
 
 A successor human task activity instance is claimed
 when the associated process instance is in the running execution state.
 The caller must be a potential owner of the successor activity instance, be an administrator
 of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 The execution state of the activity instance is changed to claimed.
 
 When there are several activities that can be claimed, that is, there
 is more than one path that can be followed after the completed activity, then
 an arbitrary activity is claimed.
 When multiple activities are claimed automatically, an arbitrary claimed activity is
 returned.
 
 Note that an activity instance may have been claimed because the associated task instance
 is requested to be claimed automatically.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance to be completed.output - The output message that denotes the result of processing.
    When the contents of the ClientObjectWrapper is null, the output variable is updated with null.
    An object wrapped by the ClientObjectWrapper must be serializable.
 
    Any previously set output or fault is ignored.
 
Returns:CompleteAndClaimSuccessorResult -
    Descriptive Information of the claimed activity instance and its
    input message.
    Refer to CompleteAndClaimSuccessorResult.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
DataHandlingException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- completeAndClaimSuccessor
CompleteAndClaimSuccessorResult completeAndClaimSuccessor(AIID aiid,
                                                        ClientObjectWrapper output)
                                                          throws ApplicationVetoException,
                                                                 ArchiveUnsupportedOperationException,
                                                                 EngineNotAuthorizedException,
                                                                 EngineParameterNullException,
                                                                 EngineWrongKindException,
                                                                 EngineWrongMessageTypeException,
                                                                 EngineWrongStateException,
                                                                 IdWrongFormatException,
                                                                 ObjectDoesNotExistException,
                                                                 DataHandlingException,
                                                                 UnexpectedFailureException,
                                                                 java.rmi.RemoteException,
                                                                 javax.ejb.EJBException
Completes a claimed activity instance using the activity instance ID
 and claims a successor activity. In other words,
 this method supports "single person workflow" scenarios.
 
 A successor activity is only claimed when it becomes available within the same
 transaction as the completed activity.
 This means that the transactional boundaries must have been set so that
 the activity to be claimed participates in the same transaction as the completed activity.
 
 The activity instance that is completed must be in the claimed execution state and the associated
 process instance must be in the running, failing, or terminating execution state.
 The caller must be the owner of the activity instance,
 be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 Completion of an activity instance means that user processing finished and that
 navigation of the process instance can continue. An output message
 is passed to denote the successful execution of user processing. The activity instance
 is put into the finished execution state.
 
 Output message values are then used to continue navigation.
 
 A successor human task activity instance is claimed
 when the associated process instance is in the running execution state.
 The caller must be a potential owner of the successor activity instance or be an administrator
 of the associated process instance.
 The execution state of the activity instance is changed to claimed.
 
 When there are several activities that can be claimed, that is, there
 is more than one path that can be followed after the completed activity, then
 an arbitrary activity is claimed.
 When multiple activities are claimed automatically, an arbitrary claimed activity is
 returned.
 
 Note that an activity instance may have been claimed because the associated task instance
 is requested to be claimed automatically.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID to identify the activity instance to be completed.output - The output message that denotes the result of processing.
    When the contents of the ClientObjectWrapper is null, the output variable is updated with null.
    An object wrapped by the ClientObjectWrapper must be serializable.
 
    Any previously set output or fault is ignored.
 
Returns:CompleteAndClaimSuccessorResult -
    Descriptive Information of the claimed activity instance and its
    input message.
    Refer to CompleteAndClaimSuccessorResult.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
DataHandlingException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- completeAndJump
void completeAndJump(java.lang.String aiid,
                   java.lang.String targetActivityName)
                     throws ApplicationVetoException,
                            ArchiveUnsupportedOperationException,
                            EngineAmbiguousActivityException,
                            EngineNotAuthorizedException,
                            EngineParameterNullException,
                            EngineProcessWrongBuildVersionException,
                            EngineUnknownActivityException,
                            EngineUnsupportedJumpException,
                            EngineWrongKindException,
                            EngineWrongStateException,
                            IdWrongFormatException,
                            IdWrongTypeException,
                            ObjectDoesNotExistException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Completes a claimed activity instance using a string representation of the
 activity instance ID and continues navigation at the specified target activity.
 
 The activity instance that is completed must be in the claimed execution state and the associated
 process instance must be in the running, failing, or suspended execution state.
 The caller must be an administrator of the associated process instance or
 of a scope that contains the activity instance to be completed.
 
 Completion of an activity instance means that user processing finished and that
 navigation of the process instance can continue.
 The activity instance is put into the finished execution state.
 
 Output message values that have been set previously are used to update the output variable -
 refer to setOutputMessage.
 In difference to the complete request,
 output message values are, however, not used to continue navigation, that is, transition conditions
 are not evaluated. Navigation continues at the specified target activity.
 
 If a fault message is set for the activity, then an EngineUnsupportedJumpException is thrown.
 You cannot jump into a fault handler.
 
 The activity to jump to must be in the same cyclic flow or sequence. You can jump forwards
 or backwards. When jumping backwards within a sequence, the activity instances between the completed
 activity instance and the jumped-to activity are deleted but compensation is not triggered.
 Compensation handlers are, however, registered for scopes so that compensation may run later.
 
 If the activity to jump to is inside a forEach construct or an event handler,
 then the activity jumped to must be within the same forEach iteration or event handler instance
 as the completed activity.
 
 The exit condition on the entry of the activity to jump to is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance to be completed.targetActivityName - The name of an activity to jump to. The activity can be a basic activity
 as well as a structured activity.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessWrongBuildVersionException
EngineUnknownActivityException
EngineUnsupportedJumpException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- completeAndJump
void completeAndJump(AIID aiid,
                   java.lang.String targetActivityName)
                     throws ApplicationVetoException,
                            ArchiveUnsupportedOperationException,
                            EngineAmbiguousActivityException,
                            EngineNotAuthorizedException,
                            EngineParameterNullException,
                            EngineProcessWrongBuildVersionException,
                            EngineUnknownActivityException,
                            EngineUnsupportedJumpException,
                            EngineWrongKindException,
                            EngineWrongStateException,
                            IdWrongFormatException,
                            ObjectDoesNotExistException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Completes a claimed activity instance using the activity instance ID
 and continues navigation at the specified target activity.
 
 The activity instance that is completed must be in the claimed execution state and the associated
 process instance must be in the running, failing, or suspended execution state.
 The caller must be an administrator of the associated process instance or
 of a scope that contains the activity instance to be completed.
 
 Completion of an activity instance means that user processing finished and that
 navigation of the process instance can continue. An output message can be passed
 to denote the result of user processing. The activity instance
 is put into the finished execution state.
 
 Output message values that have been set previously are used to update the output variable -
 refer to setOutputMessage.
 In difference to the complete request,
 output message values are, however, not used to continue navigation, that is, transition conditions
 are not evaluated. Navigation continues at the specified target activity.
 
 If a fault message is set for the activity, then an EngineUnsupportedJumpException is thrown.
 You cannot jump into a fault handler.
 
 The activity to jump to must be in the same cyclic flow or sequence. You can jump forwards
 or backwards. When jumping backwards within a sequence, the activity instances between the completed
 activity instance and the jumped-to activity are deleted but compensation is not triggered.
 Compensation handlers are, however, registered for scopes so that compensation may run later.
 
 If the activity to jump to is inside a forEach construct or an event handler,
 then the activity jumped to must be within the same forEach iteration or event handler instance
 as the completed activity.
 
 The exit condition on the entry of the activity to jump to is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID to identify the activity instance to be completed.targetActivityName - The name of an activity to jump to. The activity can be a basic activity
 as well as a structured activity.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessWrongBuildVersionException
EngineUnknownActivityException
EngineUnsupportedJumpException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- completeAndJump
void completeAndJump(java.lang.String aiid,
                   ClientObjectWrapper output,
                   java.lang.String targetActivityName)
                     throws ApplicationVetoException,
                            ArchiveUnsupportedOperationException,
                            EngineAmbiguousActivityException,
                            EngineNotAuthorizedException,
                            EngineParameterNullException,
                            EngineProcessWrongBuildVersionException,
                            EngineUnknownActivityException,
                            EngineUnsupportedJumpException,
                            EngineWrongKindException,
                            EngineWrongMessageTypeException,
                            EngineWrongStateException,
                            IdWrongFormatException,
                            IdWrongTypeException,
                            ObjectDoesNotExistException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Completes a claimed activity instance using a string representation of the
 activity instance ID and some output and continues navigation at the specified target activity.
 
 The activity instance that is completed must be in the claimed execution state and the associated
 process instance must be in the running, failing, or suspended execution state.
 The caller must be an administrator of the associated process instance or
 of a scope that contains the activity instance to be completed.
 
 Completion of an activity instance means that user processing finished and that
 navigation of the process instance can continue. An output message is passed
 to denote the result of user processing. The activity instance
 is put into the finished execution state.
 
 In difference to the complete request,
 output message values are not used to continue navigation, that is, transition conditions
 are not evaluated. Navigation continues at the specified target activity.
 
 The activity to jump to must be in the same cyclic flow or sequence. You can jump forwards
 or backwards. When jumping backwards within a sequence, the activity instances between the completed
 activity instance and the jumped-to activity are deleted but compensation is not triggered.
 Compensation handlers are, however, registered for scopes so that compensation may run later.
 
 If the activity to jump to is inside a forEach construct or an event handler,
 then the activity jumped to must be within the same forEach iteration or event handler instance
 as the completed activity.
 
 The exit condition on the entry of the activity to jump to is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance to be completed.output - The output message that denotes the result of processing.
    When the contents of the ClientObjectWrapper is null, the output variable is updated with null.
    Note that an object wrapped by the ClientObjectWrapper must be serializable.
 
    Any previously set output or fault is ignored.targetActivityName - The name of an activity to jump to. The activity can be a basic activity
 as well as a structured activity.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessWrongBuildVersionException
EngineUnknownActivityException
EngineUnsupportedJumpException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- completeAndJump
void completeAndJump(AIID aiid,
                   ClientObjectWrapper output,
                   java.lang.String targetActivityName)
                     throws ApplicationVetoException,
                            ArchiveUnsupportedOperationException,
                            EngineAmbiguousActivityException,
                            EngineNotAuthorizedException,
                            EngineParameterNullException,
                            EngineProcessWrongBuildVersionException,
                            EngineUnknownActivityException,
                            EngineUnsupportedJumpException,
                            EngineWrongKindException,
                            EngineWrongMessageTypeException,
                            EngineWrongStateException,
                            IdWrongFormatException,
                            ObjectDoesNotExistException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Completes a claimed activity instance using the activity instance ID
 and some output and continues navigation at the specified target activity.
 
 The activity instance that is completed must be in the claimed execution state and the associated
 process instance must be in the running, failing, or suspended execution state.
 The caller must be an administrator of the associated process instance or
 of a scope that contains the activity instance to be completed.
 
 Completion of an activity instance means that user processing finished and that
 navigation of the process instance can continue. An output message is passed
 to denote the result of user processing. The activity instance
 is put into the finished execution state.
 
 In difference to the complete request,
 output message values are not used to continue navigation, that is, transition conditions
 are not evaluated. Navigation continues at the specified target activity.
 
 The activity to jump to must be in the same cyclic flow or sequence. You can jump forwards
 or backwards. When jumping backwards within a sequence, the activity instances between the completed
 activity instance and the jumped-to activity are deleted but compensation is not triggered.
 Compensation handlers are, however, registered for scopes so that compensation may run later.
 
 If the activity to jump to is inside a forEach construct or an event handler,
 then the activity jumped to must be within the same forEach iteration or event handler instance
 as the completed activity.
 
 The exit condition on the entry of the activity to jump to is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID to identify the activity instance to be completed.output - The output message that denotes the result of processing.
    When the contents of the ClientObjectWrapper is null, the output variable is updated with null.
    Note that an object wrapped by the ClientObjectWrapper must be serializable.
 
    Any previously set output or fault is ignored.targetActivityName - The name of an activity to jump to. The activity can be a basic activity
 as well as a structured activity.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessWrongBuildVersionException
EngineUnknownActivityException
EngineUnsupportedJumpException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createMessage
ClientObjectWrapper createMessage(java.lang.String identifier,
                                java.lang.String messageTypeName)
                                  throws ArchiveUnsupportedOperationException,
                                         EngineNotAuthorizedException,
                                         EngineWrongKindException,
                                         IdWrongFormatException,
                                         IdWrongTypeException,
                                         ObjectDoesNotExistException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Creates a message defined by the specified process template, process instance,
  activity instance, or event handler template
 using a string representation of the object ID.
 For example, creates a message that can be used when instantiating a process instance.
 
 This method is not supported in archive mode.
Parameters:identifier - A string representation of the object ID that is used to identify the process
    template, process instance, event handler template, or activity instance for which a message is to be created.messageTypeName - The name of the message type for which a message is to be created.
    Refer to ProcessTemplateData.getInputMessageTypeName(),
    ProcessInstanceData.getInputMessageTypeName(),
    ActivityInstanceData.getInputMessageTypeName(),
    ActivityInstanceData.getOutputMessageTypeName(),
    getFaultNames, or to
    EventHandlerTemplateData.getInputMessageTypeName().
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when the specified
    message type cannot be found.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createMessage
ClientObjectWrapper createMessage(PTID ptid,
                                java.lang.String messageTypeName)
                                  throws ArchiveUnsupportedOperationException,
                                         EngineNotAuthorizedException,
                                         IdWrongFormatException,
                                         ObjectDoesNotExistException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Creates a message defined by the specified process template using the process template ID.
 For example, creates an input message that can be used when
 an instance is created from the specified process template.
 
 This method is not supported in archive mode.
Parameters:ptid - The object ID of the process template for which a message is to be created.messageTypeName - The name of the message type for which a message is to be created.
    Refer to ProcessTemplateData.getInputMessageTypeName().
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when the specified
    message type cannot be found.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createMessage
ClientObjectWrapper createMessage(PIID piid,
                                java.lang.String messageTypeName)
                                  throws ArchiveUnsupportedOperationException,
                                         EngineNotAuthorizedException,
                                         IdWrongFormatException,
                                         ObjectDoesNotExistException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Creates a message defined by the specified process instance using the process instance ID.
 For example, creates a message that can be sent to
 the specified process instance.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance for which a message is to be created.messageTypeName - The name of the message type for which a message is to be created.
    Refer to ProcessInstanceData.getInputMessageTypeName().
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when the specified
    message type cannot be found.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createMessage
ClientObjectWrapper createMessage(AIID aiid,
                                java.lang.String messageTypeName)
                                  throws ArchiveUnsupportedOperationException,
                                         EngineNotAuthorizedException,
                                         EngineWrongKindException,
                                         IdWrongFormatException,
                                         ObjectDoesNotExistException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Creates a message defined by the specified activity instance using the activity instance ID.
 For example, creates a message that can be used to complete a human task activity (staff activity).
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID of the activity instance for which a message is to be created.messageTypeName - The name of the message type for which a message is to be created.
    Refer to ActivityInstanceData.getInputMessageTypeName() or
    to ActivityInstanceData.getOutputMessageTypeName().
    
    The message type can be the name of a fault defined for the activity - refer
    to getFaultNames.
    Note that the structure of a BPEL fault name is a QName.
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when the specified
    message type cannot be found for the activity.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createMessage
ClientObjectWrapper createMessage(EHTID ehtid,
                                java.lang.String messageTypeName)
                                  throws ArchiveUnsupportedOperationException,
                                         EngineNotAuthorizedException,
                                         IdWrongFormatException,
                                         ObjectDoesNotExistException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Creates a message defined by the specified event handler template using the event handler template ID.
 For example, creates a message that can be sent to a waiting event.
 
 This method is not supported in archive mode.
Parameters:ehtid - The object ID of the event handler template for which a message is to be created.messageTypeName - The name of the message type for which a message is to be created.
    Refer to EvetnHandlerTemplateData.getInputMessageTypeName().
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when the specified
    message type cannot be found.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createMessage
ClientObjectWrapper createMessage(java.lang.String vtid,
                                java.lang.String atid,
                                java.lang.String messageTypeName)
                                  throws ArchiveUnsupportedOperationException,
                                         EngineNotAuthorizedException,
                                         IdWrongFormatException,
                                         IdWrongTypeException,
                                         ObjectDoesNotExistException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Creates a message defined by the specified activity service
 using string representations of object IDs.
 For example, creates a message that can be used when calling a service.
 
 This method is not supported in archive mode.
Parameters:vtid - A string representation of the activity service template ID. This is used
    to identify the service for which a message is to be created.atid - A string representation of the activity template ID. This is used
    to identify the activity the service belongs to.messageTypeName - The name of the message type for which a message is to be created.
    Refer to ActivityServiceTemplateData.getInputMessageTypeName().
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when the specified
    message type cannot be found for the activity service.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createMessage
ClientObjectWrapper createMessage(VTID vtid,
                                ATID atid,
                                java.lang.String messageTypeName)
                                  throws ArchiveUnsupportedOperationException,
                                         EngineNotAuthorizedException,
                                         IdWrongFormatException,
                                         ObjectDoesNotExistException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Creates a message defined by the specified activity service using object IDs.
 For example, creates a message that can be used when calling a service.
 
 This method is not supported in archive mode.
Parameters:vtid - The object ID of the activity service template for which a message is to be created.atid - The object ID of the activity the activity service template belongs to.messageTypeName - The name of the message type for which a message is to be created.
    Refer to ActivityServiceTemplateData.getInputMessageTypeName().
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when the specified
    message type cannot be found for the activity service.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createMessageWithCorrelationSets
ClientObjectWrapper createMessageWithCorrelationSets(java.lang.String aiid,
                                                   java.lang.String messageTypeName)
                                                     throws ArchiveUnsupportedOperationException,
                                                            EngineNotAuthorizedException,
                                                            EngineParameterNullException,
                                                            EngineVariableDoesNotExistException,
                                                            EngineWrongKindException,
                                                            EngineWrongStateException,
                                                            IdWrongFormatException,
                                                            IdWrongTypeException,
                                                            ObjectDoesNotExistException,
                                                            UnexpectedFailureException,
                                                            java.rmi.RemoteException,
                                                            javax.ejb.EJBException
Creates a message defined by the specified activity instance
 using a string representation of the activity instance ID
 and sets the values that are available for initialized correlation sets.
 For example, creates a message that can be used to force complete an activity.
 
 The activity instance can be a receive, reply, pick, or invoke activity.
 It can be in all execution states but the associated process
 instance must be in the running, failing, suspended, or terminating execution state.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance.messageTypeName - The name of the message type for which a message is to be created.
    Refer to
    ActivityInstanceData.getInputMessageTypeName(),
    ActivityInstanceData.getOutputMessageTypeName().
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when the specified
    message type cannot be found.
    If there are no initialized correlation sets, no values are set.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineVariableDoesNotExistException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
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

- createMessageWithCorrelationSets
ClientObjectWrapper createMessageWithCorrelationSets(AIID aiid,
                                                   java.lang.String messageTypeName)
                                                     throws ArchiveUnsupportedOperationException,
                                                            EngineNotAuthorizedException,
                                                            EngineParameterNullException,
                                                            EngineVariableDoesNotExistException,
                                                            EngineWrongKindException,
                                                            EngineWrongStateException,
                                                            IdWrongFormatException,
                                                            ObjectDoesNotExistException,
                                                            UnexpectedFailureException,
                                                            java.rmi.RemoteException,
                                                            javax.ejb.EJBException
Creates a message defined by the specified activity instance using the activity instance ID
 and sets the values that are available for initialized correlation sets.
 For example, creates a message that can be used to force complete an activity.
 
 The activity instance can be a receive, reply, pick, or invoke activity.
 It can be in all execution states but the associated process
 instance must be in the running, failing, suspended, or terminating execution state.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID of the activity instance for which a message is to be created.messageTypeName - The name of the message type for which a message is to be created.
    Refer to ActivityInstanceData.getInputMessageTypeName() or
    to ActivityInstanceData.getOutputMessageTypeName().
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when the specified
    message type cannot be found for the activity.
    If there are no initialized correlation sets, no values are set.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineVariableDoesNotExistException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
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

- createMessageWithCorrelationSets
ClientObjectWrapper createMessageWithCorrelationSets(java.lang.String vtid,
                                                   java.lang.String atid,
                                                   java.lang.String piid,
                                                   java.lang.String messageTypeName)
                                                     throws ArchiveUnsupportedOperationException,
                                                            EngineNotAuthorizedException,
                                                            EngineParameterNullException,
                                                            EngineProcessDoesNotExistException,
                                                            EngineVariableDoesNotExistException,
                                                            EngineWrongKindException,
                                                            EngineWrongStateException,
                                                            IdWrongFormatException,
                                                            IdWrongTypeException,
                                                            ObjectDoesNotExistException,
                                                            UnexpectedFailureException,
                                                            java.rmi.RemoteException,
                                                            javax.ejb.EJBException
Creates a message defined by the specified activity service
 using string representations of object IDs
 and sets the values that are available for initialized correlation sets.
 For example, creates a message that can be used to send a message to a waiting activity.
 
 The associated activity can be a receive, reply, pick, or invoke activity.
 It can be in all execution states but the associated process
 instance must be in the running, failing, suspended, or terminating execution state.
 
 This method is not supported in archive mode.
Parameters:vtid - A string representation of the activity service template ID. This is used
    to identify the service for which a message is to be created.atid - A string representation of the activity template ID. This is used
    to identify the activity the service belongs to.piid - A string representation of the process instance ID. This is used to access
    the correlations sets.messageTypeName - The name of the message type for which a message is to be created.
    Refer to ActivityServiceTemplateData.getInputMessageTypeName().
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when the specified
    message type cannot be found for the activity service.
    If there are no initialized correlation sets, no values are set.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessDoesNotExistException
EngineVariableDoesNotExistException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
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

- createMessageWithCorrelationSets
ClientObjectWrapper createMessageWithCorrelationSets(VTID vtid,
                                                   ATID atid,
                                                   PIID piid,
                                                   java.lang.String messageTypeName)
                                                     throws ArchiveUnsupportedOperationException,
                                                            EngineNotAuthorizedException,
                                                            EngineParameterNullException,
                                                            EngineProcessDoesNotExistException,
                                                            EngineVariableDoesNotExistException,
                                                            EngineWrongKindException,
                                                            EngineWrongStateException,
                                                            IdWrongFormatException,
                                                            ObjectDoesNotExistException,
                                                            UnexpectedFailureException,
                                                            java.rmi.RemoteException,
                                                            javax.ejb.EJBException
Creates a message defined by the specified activity service using object IDs
 and sets the values that are available for initialized correlation sets.
 For example, creates a message that can be used to send a message to a waiting activity.
 
 The associated activity can be a receive, reply, pick, or invoke activity.
 It can be in all execution states but the associated process
 instance must be in the running, failing, suspended, or terminating execution state.
 
 This method is not supported in archive mode.
Parameters:vtid - The object ID of the activity service template for which a message is to be created.atid - The object ID of the activity the activity service template belongs to.piid - The object ID of the process instance. This is used to access
    the correlations sets.messageTypeName - The name of the message type for which a message is to be created.
    Refer to ActivityServiceTemplateData.getInputMessageTypeName().
 
Returns:ClientObjectWrapper -
    The message created. An empty client object wrapper is returned, when the specified
    message type cannot be found for the activity service.
    If there are no initialized correlation sets, no values are set.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessDoesNotExistException
EngineVariableDoesNotExistException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
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

- createMessageWithCorrelationSetsForEventHandler
ClientObjectWrapper createMessageWithCorrelationSetsForEventHandler(java.lang.String ehtid,
                                                                  java.lang.String piid)
                                                                    throws ArchiveUnsupportedOperationException,
                                                                           EngineNotAuthorizedException,
                                                                           EngineProcessDoesNotExistException,
                                                                           EngineWrongKindException,
                                                                           EngineWrongStateException,
                                                                           IdWrongFormatException,
                                                                           IdWrongTypeException,
                                                                           ObjectDoesNotExistException,
                                                                           UnexpectedFailureException,
                                                                           java.rmi.RemoteException,
                                                                           javax.ejb.EJBException
Creates a message defined by the specified event handler
 using a string representation of the event handler template ID
 and sets the values that are available for initialized correlation sets.
 For example, creates a message that can be used to send a message to an event handler.
 
 The associated process
 instance must be in the running, failing, suspended, or terminating execution state.
 
 This method is not supported in archive mode.
Parameters:ehtid - A string representation of the event handler template ID
    that is used to identify the event handler template.piid - A string representation of the process instance ID that is used
    to access the correlation sets.
 
Returns:ClientObjectWrapper -
    The message created.
    If there are no initialized correlation sets, no values are set.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineProcessDoesNotExistException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- createMessageWithCorrelationSetsForEventHandler
ClientObjectWrapper createMessageWithCorrelationSetsForEventHandler(EHTID ehtid,
                                                                  PIID piid)
                                                                    throws ArchiveUnsupportedOperationException,
                                                                           EngineNotAuthorizedException,
                                                                           EngineProcessDoesNotExistException,
                                                                           EngineWrongKindException,
                                                                           EngineWrongStateException,
                                                                           IdWrongFormatException,
                                                                           ObjectDoesNotExistException,
                                                                           UnexpectedFailureException,
                                                                           java.rmi.RemoteException,
                                                                           javax.ejb.EJBException
Creates a message defined by the specified event handler using the event handler
 object ID
 and sets the values that are available for initialized correlation sets.
 For example, creates a message that can be used to send a message to an active event handler.
 
 The associated process
 instance must be in the running, failing, suspended, or terminating execution state.
 
 This method is not supported in archive mode.
Parameters:ehtid - The object ID of the event handler for which a message is to be created.piid - The object ID of the process instance. This is used to access
    the correlations sets.
 
Returns:ClientObjectWrapper -
    The message created.
    If there are no initialized correlation sets, no values are set.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineProcessDoesNotExistException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- createStoredQuery void createStoredQuery(java.lang.String storedQueryName, java.lang.String selectClause, java.lang.String whereClause, java.lang.String orderByClause, java.lang.Integer threshold, java.util.TimeZone timeZone) throws EngineNotAuthorizedException , EngineParameterNullException , InvalidLengthException , StoredQueryNameNotUniqueException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Creates a query definition and persistently stores it in the database for general usage. If this method is called by a business process administrator, then a stored query is created that is available for public usage. If this method is called by a regular user, then a stored query is created that is privately available for the logged-on user. A stored query represents a set of selected object properties. The number of tuples in the set can be restricted by a filter or threshold. When executing the stored query, that set can additionally be restricted by specifying a starting tuple parameter. To allow for the re-use of stored queries, parameters can be specified in the where-clause so that, for example, the owner of activities can be specified when the stored query is executed. Besides defining filtering criteria, sort criteria can be defined that are applied on the server. Sorting on the server means that the locale of the server is used. Specify the parameters of the query definition, the select-, where-, and order-by-clause, using SQL based on the published views. Execution of the query can thus be shifted to SQL and becomes portable and optimizable. Note, however, when you use a combination of the order-by-clause, threshold, or skipTupels parameters, the tuples returned depend on your database system. For example, some database systems order all records and then return the requested number of tuples. Other database systems first take the requested number of tuples and then apply the order criteria. The domain of the query, that is, the SQL from-clause, is determined automatically. All properties of objects are returned for which you own a work item or which can be transitively reached via your work item. As a rule of thumb, all objects except process templates can be reached via work items. This means that you cannot use process template properties only but that you must specify a non process template property in the select- or where-clause. Note that a business process administrator has special rights and can retrieve information on objects associated to other users. When the stored query is executed, it returns the selected properties of all objects for which there are work items to the business process administrator, no matter whether there is a personally owned work item or another user's work item. Although stored query definitions are stored persistently, object properties contained in the stored query are assembled dynamically when they are queried. Refer to query for the execution of stored queries. When a stored query definition needs to be updated, it must be deleted and recreated - refer to deleteStoredQuery for the deletion of stored queries. Parameters: storedQueryName - The name of the stored query to be created; must not be greater than 64 bytes in UTF-8 format. The name must be unique. selectClause - Describes the query result produced that is returned when the stored query is executed. Its syntax is an SQL select-clause. It either declares a list of names that identify the object properties (columns of the result) to be returned or it specifies the COUNT keyword. Aggregation functions like AVG(), SUM(), MIN(), and MAX() are not supported. Each part of the select-clause separated by a comma must specify a property from the published views - see the InfoCenter for details. To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the view name. For example, "ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE". To count the number of potentially qualifying tuples, use the COUNT keyword. For example, to count the number of activity instance IDs that satisfy the where-clause, specify a select-clause such as "COUNT(DISTINCT ACTIVITY.AIID)". If you use the more generic "COUNT(*)", then you must specify a where-clause so that the tuples to be counted can be determined. For example, to count all activities, specify a where-clause such as "ACTIVITY.AIID=ACTIVITY.AIID" that always evaluates to true. A selectClause must not be greater than 512 bytes in UTF-8 format. The QueryResultSet contains columns in the same order as specified in the selectClause. If tuples are to be counted, an int value is returned (row 1, column 1). whereClause - Specifies the search condition that is applied when the stored query is executed. Its syntax is an SQL where-clause. The following rules apply: If a filter is not to be applied, null must be specified. A whereClause must not be greater than 2047 bytes in UTF-8 format. orderByClause - Orders the result of the stored query execution by the values of the columns you identify. Its syntax is an SQL order-by-clause. Each part of the order-by-clause separated by a comma must specify a property from the published views. If you identify more that one property, the stored query execution result is ordered by the values of the first property you identify, then by the values of the second property, and so on. If sort criteria are not to be applied, null must be specified. An orderByClause must not be greater than 254 bytes in UTF-8 format. Note that sort criteria are applied on the server, that is, the locale of the server is used for sorting. threshold - The maximum number of stored query execution result tuples to be returned from the server to the client. If a threshold is not to be applied, null must be specified. timeZone - Specifies the time zone of the timestamp constants in the whereClause. If a timezone is not specified, UTC is assumed. Throws: EngineNotAuthorizedException EngineParameterNullException InvalidLengthException StoredQueryNameNotUniqueException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.0 Change History Release Modification 6.0.2 Can create a private stored query.

#### createStoredQuery

```
void createStoredQuery(java.lang.String storedQueryName,
                     java.lang.String selectClause,
                     java.lang.String whereClause,
                     java.lang.String orderByClause,
                     java.lang.Integer threshold,
                     java.util.TimeZone timeZone)
                       throws EngineNotAuthorizedException,
                              EngineParameterNullException,
                              InvalidLengthException,
                              StoredQueryNameNotUniqueException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
```

A stored query represents a set of selected object properties. The number of tuples in the set
 can be restricted by a filter or threshold. When executing the stored query, that set
 can additionally be restricted by specifying a starting tuple parameter.
 
 To allow for the re-use of stored queries, parameters can be specified in the where-clause
 so that, for example, the owner of activities can be specified when the stored query is executed.
 
 Besides defining filtering criteria, sort criteria can be defined that are applied on the server.
 Sorting on the server means that the locale of the server is used.
 
 Specify the parameters of the query definition, the select-, where-, and order-by-clause,
 using SQL based on the published views.
 Execution of the query can thus be shifted to SQL and becomes portable and optimizable.
 
 Note, however, when you use a combination of the order-by-clause, threshold, or skipTupels
 parameters, the tuples returned depend on your database system.
 For example, some database systems order all records and then return the requested number of tuples.
 Other database systems first take the requested number of tuples and then apply the order criteria.
 
 The domain of the query, that is, the SQL from-clause, is determined automatically.
 All properties of objects are returned for which you own a work item
 or which can be transitively reached via your work item.
 As a rule of thumb, all objects except process templates can be reached via work items.
 This means that you cannot use process template properties only but that you
 must specify a non process template property in the select- or where-clause.
 
 Note that a business process administrator has special rights and can retrieve
 information on objects associated to other users. When the stored query is executed,
 it returns the selected properties of all objects for which there are
 work items to the business process administrator, no matter whether there is a personally
 owned work item or another user's work item.
 
 Although stored query definitions are stored persistently, object properties contained in
 the stored query are assembled dynamically when they are queried.
 Refer to query for the execution of stored queries.
 
 When a stored query definition needs to be updated, it must be deleted and recreated -
 refer to deleteStoredQuery for the deletion of stored queries.

It either declares a list of names that identify the object properties (columns of the result)
    to be returned or it specifies the COUNT keyword. Aggregation functions like AVG(), SUM(),
    MIN(), and MAX() are not supported.
    
    Each part of the select-clause separated by a comma must specify a property from the
    published views - see the InfoCenter for details.
    
    To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the
    view name. For example, "ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE".
    

    To count the number of potentially qualifying tuples, use the COUNT keyword.
    For example, to count the number of activity instance IDs that satisfy the
    where-clause, specify a select-clause such as "COUNT(DISTINCT ACTIVITY.AIID)".
    If you use the more generic "COUNT(*)", then you must specify a where-clause
    so that the tuples to be counted can be determined.
    For example, to count all activities,
    specify a where-clause such as "ACTIVITY.AIID=ACTIVITY.AIID" that always evaluates to true.
    
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
    instead of integer enumerations. For example, instead of specifying an activity state expression
    "ACTIVITY.STATE=2" , specify "ACTIVITY.STATE=ACTIVITY.STATE.STATE\_READY".
Duplicate apostrophes (') in comparising values. For example,
    "ACTIVITY.NAME='d''automatisation'".
    To specify a where clause that refers to properties of name-value pairs, like
    custom properties, add a one-digit suffix (0-9) to the view name.
    

    For example, to have only tuples returned where an activity custom property "prop1" has
    the value "v1" or where an activity custom property "prop2" has the value v2", the where clause
    can look like
    "ACTIVITY\_ATTRIBUTE1.NAME='prop1' AND ACTIVITY\_ATTRIBUTE1.VALUE='v1' OR
    ACTIVITY\_ATTRIBUTE2.NAME='prop2' AND ACTIVITY\_ATTRIBUTE2.VALUE = 'v2'".
    For performance reasons, you should not use more than one "OR" construct; use "IN" instead.
    

    For example, to retrieve the values of custom properties "prop1" and "prop2" of all activity instances,
    the select clause can look like
    "DISTINCT ACTIVITY.AIID, ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE" and the where-clause
    "ACTIVITY\_ATTRIBUTE1.NAME = 'prop1' AND ACTIVITY\_ATTRIBUTE2.NAME = 'prop2'".
    Specify parameters as @param followed by a number suffix. The number of the
    first parameter must be 1, of the second 2, and so on.
    For example, "ACTIVITY\_ATTRIBUTE.NAME = '@param1'".
    

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

- createStoredQuery void createStoredQuery(java.lang.String storedQueryName, java.lang.String selectClause, java.lang.String whereClause, java.lang.String orderByClause, java.lang.Integer threshold, java.util.TimeZone timeZone, java.util.List storedQueryProperties, java.lang.String clientType) throws EngineParameterNullException , InvalidLengthException , InvalidParameterException , StoredQueryNameNotUniqueException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Creates a query definition and specifies properties to be stored together with the query. If this method is called by a business process administrator, then a stored query is created that is available for public usage. If this method is called by a regular user, then a stored query is created that is privately available for the calling logged-on user. A stored query represents a set of selected object properties. The number of tuples in the set can be restricted by a filter or threshold. When executing the stored query, that set can additionally be restricted by specifying a starting tuple parameter. To allow for the re-use of stored queries, parameters can be specified in the where-clause so that, for example, the owner of activities can be specified when the stored query is executed. Besides defining filtering criteria, sort criteria can be defined that are applied on the server. Sorting on the server means that the locale of the server is used. Specify the parameters of the query definition, the select-, where-, and order-by-clause, using SQL based on the published views. Execution of the query can thus be shifted to SQL and becomes portable and optimizable. Note, however, when you use a combination of the order-by-clause, threshold, or skipTupels parameters, the tuples returned depend on your database system. For example, some database systems order all records and then return the requested number of tuples. Other database systems first take the requested number of tuples and then apply the order criteria. The domain of the query, that is, the SQL from-clause, is determined automatically. All properties of objects are returned for which you own a work item, or which can be transitively reached via your work item. As a rule of thumb, all objects except process templates can be reached via work items. This means that you cannot use process template properties only but that you must specify a non process template property in the select- or where-clause. Note that a business process administrator has special rights and can retrieve information on objects associated to other users. When the stored query is executed, it returns the selected properties of all objects for which there are work items to the business process administrator, no matter whether there is a personally owned work item or another user's work item. Although stored query definitions are stored persistently, object properties contained in the result set are assembled dynamically when they are queried. Refer to query for the execution of stored queries. When a stored query definition needs to be updated, it must be deleted and recreated - refer to deleteStoredQuery for the deletion of stored queries. Parameters: storedQueryName - The name of the stored query to be created; must not be greater than 64 bytes in UTF-8 format. The name must be unique. selectClause - Describes the query result that is returned when the stored query is executed. Its syntax is an SQL select-clause. It either declares a list of names that identify the object properties (columns of the result) to be returned or it specifies the COUNT keyword. Aggregation functions like AVG(), SUM(), MIN(), and MAX() are not supported. Each part of the select-clause separated by a comma must specify a property from the published views - see the InfoCenter for details. To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the view name. For example, "ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE". To count the number of potentially qualifying tuples, use the COUNT keyword. For example, to count the number of activity instance IDs that satisfy the where-clause, specify a select-clause such as "COUNT(DISTINCT ACTIVITY.AIID)". If you use the more generic "COUNT(*)", then you must specify a where-clause so that the tuples to be counted can be determined. For example, to count all activities, specify a where-clause such as "ACTIVITY.AIID=ACTIVITY.AIID" that always evaluates to true. A selectClause must not be greater than 512 bytes in UTF-8 format. The QueryResultSet contains columns in the same order as specified in the selectClause. If tuples are to be counted, an int value is returned (row 1, column 1). whereClause - Specifies the search condition that is applied when the stored query is executed. Its syntax is an SQL where-clause. The following rules apply: If a filter is not to be applied, null must be specified. A whereClause must not be greater than 2047 bytes in UTF-8 format. orderByClause - Orders the result of the stored query execution by the values of the columns you identify. Its syntax is an SQL order-by-clause. Each part of the order-by-clause separated by a comma must specify a property from the published views. If you identify more that one property, the stored query execution result is ordered by the values of the first property you identify, then by the values of the second property, and so on. If sort criteria are not to be applied, null must be specified. An orderByClause must not be greater than 254 bytes in UTF-8 format. Note that sort criteria are applied on the server, that is, the locale of the server is used for sorting. threshold - The maximum number of stored query execution result tuples to be returned from the server to the client. If a threshold is not to be applied, null must be specified. timeZone - Specifies the time zone of the timestamp constants in the whereClause. If a timezone is not specified, UTC is assumed. storedQueryProperties - Specifies user-defined properties to be attached to the stored query. Must be a list of StoredQueryProperty objects - see StoredQueryProperty . If no properties are to be attached, null must be passed. clientType - A user-defined client type to specify the creator of the stored query, for example, Web, Portal, or Custom. The client type must not be greater than 128 bytes in UTF-8 format. Throws: EngineParameterNullException InvalidLengthException InvalidParameterException StoredQueryNameNotUniqueException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.0.2

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
                       throws EngineParameterNullException,
                              InvalidLengthException,
                              InvalidParameterException,
                              StoredQueryNameNotUniqueException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
```

A stored query represents a set of selected object properties. The number of tuples in the set
 can be restricted by a filter or threshold. When executing the stored query, that set
 can additionally be restricted by specifying a starting tuple parameter.
 
 To allow for the re-use of stored queries, parameters can be specified in the where-clause
 so that, for example, the owner of activities can be specified when the stored query is executed.
 
 Besides defining filtering criteria, sort criteria can be defined that are applied on the server.
 Sorting on the server means that the locale of the server is used.
 
 Specify the parameters of the query definition, the select-, where-, and order-by-clause,
 using SQL based on the published views.
 Execution of the query can thus be shifted to SQL and becomes portable and optimizable.
 
 Note, however, when you use a combination of the order-by-clause, threshold, or skipTupels
 parameters, the tuples returned depend on your database system.
 For example, some database systems order all records and then return the requested number of tuples.
 Other database systems first take the requested number of tuples and then apply the order criteria.
 
 The domain of the query, that is, the SQL from-clause, is determined automatically.
 All properties of objects are returned for which you own a work item,
 or which can be transitively reached via your work item.
 As a rule of thumb, all objects except process templates can be reached via work items.
 This means that you cannot use process template properties only but that you
 must specify a non process template property in the select- or where-clause.
 
 Note that a business process administrator has special rights and can retrieve
 information on objects associated to other users. When the stored query is executed,
 it returns the selected properties of all objects for which there are
 work items to the business process administrator, no matter whether there is a personally
 owned work item or another user's work item.
 
 Although stored query definitions are stored persistently, object properties contained in
 the result set are assembled dynamically when they are queried.
 Refer to query for the execution of stored queries.
 
 When a stored query definition needs to be updated, it must be deleted and recreated -
 refer to deleteStoredQuery for the deletion of
 stored queries.

It either declares a list of names that identify the object properties (columns of the result)
    to be returned or it specifies the COUNT keyword. Aggregation functions like AVG(), SUM(),
    MIN(), and MAX() are not supported.
    
    Each part of the select-clause separated by a comma must specify a property from the
    published views - see the InfoCenter for details.
    
    To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the
    view name. For example, "ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE".
    
    To count the number of potentially qualifying tuples, use the COUNT keyword.
    For example, to count the number of activity instance IDs that satisfy the
    where-clause, specify a select-clause such as "COUNT(DISTINCT ACTIVITY.AIID)".
    If you use the more generic "COUNT(*)", then you must specify a where-clause
    so that the tuples to be counted can be determined.
    For example, to count all activities,
    specify a where-clause such as "ACTIVITY.AIID=ACTIVITY.AIID" that always evaluates to true.
    
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
    instead of integer enumerations. For example, instead of specifying an activity instance state expression
    "ACTIVITY.STATE=2" , specify "ACTIVITY.STATE=ACTIVITY.STATE.STATE\_READY".
Duplicate apostrophes (') in comparising values. For example,
    "ACTIVITY.NAME='d''automatisation'".
    To specify a where clause that refers to properties of name-value pairs, like
    custom properties, add a one-digit suffix (0-9) to the view name.
    

    For example, to have only tuples returned where a activity custom property "prop1" has
    the value "v1" or where a activity custom property "prop2" has the value v2", the where clause
    can look like
    "ACTIVITY\_ATTRIBUTE1.NAME='prop1' AND ACTIVITY\_ATTRIBUTE1.VALUE='v1' OR
    ACTIVITY\_ATTRIBUTE2.NAME='prop2' AND ACTIVITY\_ATTRIBUTE2.VALUE = 'v2'".
    For performance reasons, you should not use more than one "OR" construct; use "IN" instead.
    

    For example, to retrieve the values of custom properties "prop1" and "prop2" of all acitvity instances,
    the select clause can look like
    "DISTINCT ACTIVITY.AIID, ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE" and the where-clause
    "ACTIVITY\_ATTRIBUTE1.NAME = 'prop1' AND ACTIVITY\_ATTRIBUTE2.NAME = 'prop2'".
    Specify parameters as @param followed by a number suffix. The number of the
    first parameter must be 1, of the second 2, and so on.
    For example, "ACTIVITY\_ATTRIBUTE.NAME = '@param1'".
    

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

- createStoredQuery void createStoredQuery(java.lang.String userID, java.lang.String storedQueryName, java.lang.String selectClause, java.lang.String whereClause, java.lang.String orderByClause, java.lang.Integer threshold, java.util.TimeZone timeZone, java.util.List storedQueryProperties, java.lang.String clientType) throws EngineNotAuthorizedException , EngineParameterNullException , InvalidLengthException , InvalidParameterException , StoredQueryNameNotUniqueException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Creates a query definition for the specified user. A regular user can only create stored queries that are available for his personal usage. A business process system administrator can create stored queries that are available for public usage or for the usage of the specified person. A stored query represents a set of selected object properties. The number of tuples in the set can be restricted by a filter or threshold. When executing the stored query, that set can additionally be restricted by specifying a starting tuple parameter. To allow for the re-use of stored queries, parameters can be specified in the where-clause so that, for example, the owner of activities can be specified when the stored query is executed. Besides defining filtering criteria, sort criteria can be defined that are applied on the server. Sorting on the server means that the locale of the server is used. Specify the parameters of the query definition, the select-, where-, and order-by-clause, using SQL based on the published views. Execution of the query can thus be shifted to SQL and becomes portable and optimizable. Note, however, when you use a combination of the order-by-clause, threshold, or skipTupels parameters, the tuples returned depend on your database system. For example, some database systems order all records and then return the requested number of tuples. Other database systems first take the requested number of tuples and then apply the order criteria. The domain of the query, that is, the SQL from-clause, is determined automatically. All properties of objects are returned for which you own a work item, or which can be transitively reached via your work item. As a rule of thumb, all objects except process templates can be reached via work items. This means that you cannot use process template properties only but that you must specify a non process template property in the select- or where-clause. Note that a business process administrator has special rights and can retrieve information on objects associated to other users. When the stored query is executed, it returns the selected properties of all objects for which there are work items to the business process administrator, no matter whether there is a personally owned work item or another user's work item. Although stored query definitions are stored persistently, object properties contained in the result set are assembled dynamically when they are queried. Refer to query for the execution of stored queries. When a stored query definition needs to be updated, it must be deleted and recreated - refer to deleteStoredQuery for the deletion of stored queries. Parameters: userID - The name of a user who is to become the owner of the stored query. Null means that a public stored query is created. storedQueryName - The name of the stored query to be created; must not be greater than 64 bytes in UTF-8 format. The name must be unique. selectClause - Describes the query result that is returned when the stored query is executed. Its syntax is an SQL select-clause. It either declares a list of names that identify the object properties (columns of the result) to be returned or it specifies the COUNT keyword. Aggregation functions like AVG(), SUM(), MIN(), and MAX() are not supported. Each part of the select-clause separated by a comma must specify a property from the published views - see the InfoCenter for details. To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the view name. For example, "ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE". To count the number of potentially qualifying tuples, use the COUNT keyword. For example, to count the number of activity instance IDs that satisfy the where-clause, specify a select-clause such as "COUNT(DISTINCT ACTIVITY.AIID)". If you use the more generic "COUNT(*)", then you must specify a where-clause so that the tuples to be counted can be determined. For example, to count all activities, specify a where-clause such as "ACTIVITY.AIID=ACTIVITY.AIID" that always evaluates to true. A selectClause must not be greater than 512 bytes in UTF-8 format. The QueryResultSet contains columns in the same order as specified in the selectClause. If tuples are to be counted, an int value is returned (row 1, column 1). whereClause - Specifies the search condition that is applied when the stored query is executed. Its syntax is an SQL where-clause. The following rules apply: If a filter is not to be applied, null must be specified. A whereClause must not be greater than 2047 bytes in UTF-8 format. orderByClause - Orders the result of the stored query execution by the values of the columns you identify. Its syntax is an SQL order-by-clause. Each part of the order-by-clause separated by a comma must specify a property from the published views. If you identify more that one property, the stored query execution result is ordered by the values of the first property you identify, then by the values of the second property, and so on. If sort criteria are not to be applied, null must be specified. An orderByClause must not be greater than 254 bytes in UTF-8 format. Note that sort criteria are applied on the server, that is, the locale of the server is used for sorting. threshold - The maximum number of stored query execution result tuples to be returned from the server to the client. If a threshold is not to be applied, null must be specified. timeZone - Specifies the time zone of the timestamp constants in the whereClause. If a timezone is not specified, UTC is assumed. storedQueryProperties - Specifies user-defined properties to be attached to the stored query. Must be a list of StoredQueryProperty objects - see StoredQueryProperty . If no properties are to be attached, null must be passed. clientType - A user-defined client type to specify the creator of the stored query, for example, Web, Portal, or Custom. The client type must not be greater than 128 bytes in UTF-8 format. Throws: EngineNotAuthorizedException EngineParameterNullException InvalidLengthException InvalidParameterException StoredQueryNameNotUniqueException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.0.2

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
                       throws EngineNotAuthorizedException,
                              EngineParameterNullException,
                              InvalidLengthException,
                              InvalidParameterException,
                              StoredQueryNameNotUniqueException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
```

A regular user can only create stored queries that are available for his personal usage.
 A business process system administrator can create stored queries that are available for public usage
 or for the usage of the specified person.
 
 A stored query represents a set of selected object properties. The number of tuples in the set
 can be restricted by a filter or threshold. When executing the stored query, that set
 can additionally be restricted by specifying a starting tuple parameter.
 
 To allow for the re-use of stored queries, parameters can be specified in the where-clause
 so that, for example, the owner of activities can be specified when the stored query is executed.
 
 Besides defining filtering criteria, sort criteria can be defined that are applied on the server.
 Sorting on the server means that the locale of the server is used.
 
 Specify the parameters of the query definition, the select-, where-, and order-by-clause,
 using SQL based on the published views.
 Execution of the query can thus be shifted to SQL and becomes portable and optimizable.
 
 Note, however, when you use a combination of the order-by-clause, threshold, or skipTupels
 parameters, the tuples returned depend on your database system.
 For example, some database systems order all records and then return the requested number of tuples.
 Other database systems first take the requested number of tuples and then apply the order criteria.
 
 The domain of the query, that is, the SQL from-clause, is determined automatically.
 All properties of objects are returned for which you own a work item,
 or which can be transitively reached via your work item.
 As a rule of thumb, all objects except process templates can be reached via work items.
 This means that you cannot use process template properties only but that you
 must specify a non process template property in the select- or where-clause.
 
 Note that a business process administrator has special rights and can retrieve
 information on objects associated to other users. When the stored query is executed,
 it returns the selected properties of all objects for which there are
 work items to the business process administrator, no matter whether there is a personally
 owned work item or another user's work item.
 
 Although stored query definitions are stored persistently, object properties contained in
 the result set are assembled dynamically when they are queried.
 Refer to query for the execution of stored queries.
 
 When a stored query definition needs to be updated, it must be deleted and recreated -
 refer to deleteStoredQuery for the deletion of
 stored queries.

It either declares a list of names that identify the object properties (columns of the result)
    to be returned or it specifies the COUNT keyword. Aggregation functions like AVG(), SUM(),
    MIN(), and MAX() are not supported.
    
    Each part of the select-clause separated by a comma must specify a property from the
    published views - see the InfoCenter for details.
    
    To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the
    view name. For example, "ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE".
    
    To count the number of potentially qualifying tuples, use the COUNT keyword.
    For example, to count the number of activity instance IDs that satisfy the
    where-clause, specify a select-clause such as "COUNT(DISTINCT ACTIVITY.AIID)".
    If you use the more generic "COUNT(*)", then you must specify a where-clause
    so that the tuples to be counted can be determined.
    For example, to count all activities,
    specify a where-clause such as "ACTIVITY.AIID=ACTIVITY.AIID" that always evaluates to true.
    
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
    instead of integer enumerations. For example, instead of specifying a activity instance state expression
    "ACTIVITY.STATE=2" , specify "ACTIVITY.STATE=ACTIVITY.STATE.STATE\_READY".
Duplicate apostrophes (') in comparising values. For example,
    "ACTIVITY.NAME='d''automatisation'".
    To specify a where clause that refers to properties of name-value pairs, like
    custom properties, add a one-digit suffix (0-9) to the view name.
    

    For example, to have only tuples returned where an activity custom property "prop1" has
    the value "v1" or where an activity custom property "prop2" has the value v2", the where clause
    can look like
    "ACTIVITY\_ATTRIBUTE1.NAME='prop1' AND ACTIVITY\_ATTRIBUTE1.VALUE='v1' OR
    ACTIVITY\_ATTRIBUTE2.NAME='prop2' AND ACTIVITY\_ATTRIBUTE2.VALUE = 'v2'".
    For performance reasons, you should not use more than one "OR" construct; use "IN" instead.
    

    For example, to retrieve the values of custom properties "prop1" and "prop2" of all activity instances,
    the select clause can look like
    "DISTINCT ACTIVITY.AIID, ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE" and the where-clause
    "ACTIVITY\_ATTRIBUTE1.NAME = 'prop1' AND ACTIVITY\_ATTRIBUTE2.NAME = 'prop2'".
    Specify parameters as @param followed by a number suffix. The number of the
    first parameter must be 1, of the second 2, and so on.
    For example, "ACTIVITY\_ATTRIBUTE.NAME = '@param1'".
    

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

- createWorkItem
void createWorkItem(java.lang.String identifier,
                  int assignmentReason,
                  java.lang.String userID)
                    throws ApplicationVetoException,
                           ArchiveUnsupportedOperationException,
                           EngineEverybodyWorkItemException,
                           EngineNotAuthorizedException,
                           EngineParameterNullException,
                           EngineProcessReaderWorkItemException,
                           EngineWrongKindException,
                           EngineWrongStateException,
                           GroupWorkItemException,
                           HumanTaskManagerException,
                           IdWrongFormatException,
                           IdWrongTypeException,
                           InvalidLengthException,
                           UserDoesNotExistException,
                           ObjectDoesNotExistException,
                           UnexpectedFailureException,
                           WorkItemManagerException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
Creates a work item for processes or activities
 using a string representation of either the process or activity instance ID.
 The work item is created with the specified assignment reason
 for the specified process or activity instance and the specified user.
 
 Work items with assignment reasons "starter" or "owner" cannot be explicitly created.
 Work items with assignment reasons "administrator" can only be created on the process instance.
 
 Work items with assignment reasons "administrator" or "reader" for the process instance
 are automatically propagated to all enclosed activity instances.
 
 The process instance must be in the running, failing, or terminating execution state.
 When a work item for an activity instance is to be created,
 the activity instance must be in the claimed, ready, running, or stopped execution state.
 The activity must be an invoke, script, wait, or human task activity.
 A human task activity is also known as staff activity.
 
 The caller must be an administrator of the process instance
 or be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:identifier - A string representation of the process or activity instance ID that is used to identify
    the object the new work item should belong to.assignmentReason - The reason why the work item is assigned - refer to
     the work item assignment reasons.userID - The user the work item should belong to.
    It is checked whether the user exists but the check may be executed case insensitively.
    The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments'
    custom property of the Human Task Manager configuration to 'true'.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineEverybodyWorkItemException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessReaderWorkItemException
EngineWrongKindException
EngineWrongStateException
GroupWorkItemException
HumanTaskManagerException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
UserDoesNotExistException
ObjectDoesNotExistException
UnexpectedFailureException
WorkItemManagerException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 The activity can be a wait activity if "admin task for all activities" is specified for the
 containing process.

- createWorkItem
void createWorkItem(PIID piid,
                  int assignmentReason,
                  java.lang.String userID)
                    throws ApplicationVetoException,
                           ArchiveUnsupportedOperationException,
                           EngineEverybodyWorkItemException,
                           EngineNotAuthorizedException,
                           EngineParameterNullException,
                           EngineProcessReaderWorkItemException,
                           EngineWrongKindException,
                           EngineWrongStateException,
                           GroupWorkItemException,
                           HumanTaskManagerException,
                           IdWrongFormatException,
                           InvalidLengthException,
                           UserDoesNotExistException,
                           ObjectDoesNotExistException,
                           UnexpectedFailureException,
                           WorkItemManagerException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
Creates a work item for processes with the specified assignment reason
 for the specified process instance and user.
 
 A work item with an assignment reason "starter" cannot be explicitly created.
 Work items with assignment reasons "administrator" or "reader"
 are automatically propagated to all enclosed activity instances.
 
 The process instance must be in the running, failing, or terminating execution state.
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance the new work item should belong to.assignmentReason - The reason why the work item is assigned - refer to
     the work item assignment reasons.userID - The user the work item should belong to.
    It is checked whether the user exists but the check may be executed case insensitively.
    The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments'
    custom property of the Human Task Manager configuration to 'true'.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineEverybodyWorkItemException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessReaderWorkItemException
EngineWrongKindException
EngineWrongStateException
GroupWorkItemException
HumanTaskManagerException
IdWrongFormatException
InvalidLengthException
UserDoesNotExistException
ObjectDoesNotExistException
UnexpectedFailureException
WorkItemManagerException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.0.2
 
 Throws an ApplicationVetoException when the application refuses to execute the method.
 
6.0.2
 
 Throws an EngineProcessReaderWorkItemException when a process reader work item already exists.
 
6.0.2
 
 Throws a HumanTaskManagerException when the Human Task Manager reports an error.
 
6.0.2
 
 Throws a UserDoesNotExistException when the specified user does not exist.
 
6.1
 
 Custom property 'SupportVirtualUserIdsForPeopleAssignments' is acknowledged.
 Throws a GroupWorkItemException when a group is specified as user ID.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- createWorkItem
void createWorkItem(AIID aiid,
                  int assignmentReason,
                  java.lang.String userID)
                    throws ApplicationVetoException,
                           ArchiveUnsupportedOperationException,
                           EngineEverybodyWorkItemException,
                           EngineNotAuthorizedException,
                           EngineParameterNullException,
                           EngineProcessReaderWorkItemException,
                           EngineWrongKindException,
                           EngineWrongStateException,
                           GroupWorkItemException,
                           HumanTaskManagerException,
                           IdWrongFormatException,
                           InvalidLengthException,
                           UserDoesNotExistException,
                           ObjectDoesNotExistException,
                           UnexpectedFailureException,
                           WorkItemManagerException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
Creates a work item for activities with the specified assignment reason
 for the specified activity instance and user.
 
 A work item with an assignment reason "owner" cannot be explicitly created.
 Work items with assignment reasons "administrator" can only be created on the process instance.
 
 The activity instance must be in the claimed, ready, running, or stopped execution state.
 The associated process instance must be in the running, failing, or terminating execution state.
 The activity must be an invoke, script, wait, or human task activity.
 A human task activity is also known as staff activity.
 
 The caller must be an administrator of the associated process instance
 or be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID of the activity instance the new work item should belong to.assignmentReason - The reason why the work item is assigned - refer to
     the work item assignment reasons.userID - The user the work item should belong to.
    It is checked whether the user exists but the check may be executed case insensitively.
    The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments'
    custom property of the Human Task Manager configuration to 'true'.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineEverybodyWorkItemException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessReaderWorkItemException
EngineWrongKindException
EngineWrongStateException
GroupWorkItemException
HumanTaskManagerException
IdWrongFormatException
InvalidLengthException
UserDoesNotExistException
ObjectDoesNotExistException
UnexpectedFailureException
WorkItemManagerException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 The activity can be a wait activity if "admin task for all activities" is specified for the
 containing process.

- delete
void delete(java.lang.String piid)
            throws EngineNotAuthorizedException,
                   EngineWrongKindException,
                   EngineWrongStateException,
                   IdWrongFormatException,
                   IdWrongTypeException,
                   ObjectDoesNotExistException,
                   UnexpectedFailureException,
                   java.rmi.RemoteException,
                   javax.ejb.EJBException
Deletes the specified top-level process instance and its non-autonomous subprocesses
 and tasks using a string representation of the process instance ID
 or the process instance name.
 
 The process instance must be in the finished, terminated, compensated, or failed execution state.
 The caller must be an administrator of the process instance.
Parameters:piid - A string representation of the process instance object ID or the process instance
 name that is used to identify the process instance to be deleted.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.2
 Deletes
 the inline tasks together with the process instance.
 
8.0
 Allows for
 the specification of the process instance name instead of the process instance ID.

- delete
void delete(PIID piid)
            throws EngineNotAuthorizedException,
                   EngineWrongKindException,
                   EngineWrongStateException,
                   IdWrongFormatException,
                   ObjectDoesNotExistException,
                   UnexpectedFailureException,
                   java.rmi.RemoteException,
                   javax.ejb.EJBException
Deletes the specified top-level process instance and its non-autonomous subprocesses
 and tasks using the process instance ID.
 
 The process instance must be in the finished, terminated, compensated, or failed execution state.
 The caller must be an administrator of the process instance.
Parameters:piid - The object ID of the process instance to be deleted.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.2
 Deletes
 the inline tasks together with the process instance.

- deleteStoredQuery
void deleteStoredQuery(java.lang.String storedQueryName)
                       throws EngineNotAuthorizedException,
                              EngineParameterNullException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Deletes the specified stored query.
 If this method is called by a business process administrator, then a stored query is deleted
 that is available for public usage.
 If this method is called by a regular user, then a stored query is deleted
 that is privately available for the calling logged-on user.
 
 No error is signalled when the specified stored query does no longer exist.
 
 Refer to createStoredQuery for the creation of stored queries.
 
Parameters:storedQueryName - The name of the stored query to be deleted -
    refer to getStoredQueryNames for the retrieval of existing stored query names.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
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
                       throws EngineNotAuthorizedException,
                              EngineParameterNullException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Deletes the specified stored query for the specified user.
 
 A regular user can only delete stored queries that are available for his personal usage.
 A business process administrator can also delete stored queries that are available
 for the usage of the specified person.
 
 No error is signalled when the specified stored query does no longer exist.
 
 Refer to createStoredQuery for
 the creation of stored queries.
Parameters:userID - The name of the user who is the owner of the stored query.storedQueryName - The name of the stored query to be deleted -
    refer to getStoredQueryNames
    for the retrieval of existing stored query names.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- deleteWorkItem void deleteWorkItem(java.lang.String identifier, int assignmentReason, java.lang.String userID) throws ApplicationVetoException , ArchiveUnsupportedOperationException , EngineEverybodyWorkItemException , EngineLastAdminWorkItemException , EngineNotAuthorizedException , EngineParameterNullException , EngineProcessReaderWorkItemException , EngineWrongKindException , EngineWrongStateException , GroupWorkItemException , HumanTaskManagerException , IdWrongFormatException , IdWrongTypeException , InvalidLengthException , ObjectDoesNotExistException , UnexpectedFailureException , WorkItemManagerException , java.rmi.RemoteException, javax.ejb.EJBException Deletes the specified work item using a string representation of either the process or activity instance ID. Following restrictions apply: The process instance must be in the running, failing, or terminating execution state. When a work item for an activity instance is to be deleted, the activity instance must be in the claimed, ready, running, or stopped execution state. The activity must be an invoke, script, or human task activity. A human task activity is also known as staff activity. The caller must be an administrator of the process instance or be an administrator of a scope that contains the activity instance. This method is not supported in archive mode. Parameters: identifier - A string representation of the process or activity instance ID that is used to identify the object the work item belongs to. assignmentReason - The reason why the work item has been assigned - refer to the work item assignment reasons . userID - The user the work item belongs to. Throws: ApplicationVetoException ArchiveUnsupportedOperationException EngineEverybodyWorkItemException EngineLastAdminWorkItemException EngineNotAuthorizedException EngineParameterNullException EngineProcessReaderWorkItemException EngineWrongKindException EngineWrongStateException GroupWorkItemException HumanTaskManagerException IdWrongFormatException IdWrongTypeException InvalidLengthException ObjectDoesNotExistException UnexpectedFailureException WorkItemManagerException java.rmi.RemoteException javax.ejb.EJBException Since: 5.1 Change History Release Modification 6.1.2 The caller may have administrator rights for the scope that contains the activity instance. 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### deleteWorkItem

```
void deleteWorkItem(java.lang.String identifier,
                  int assignmentReason,
                  java.lang.String userID)
                    throws ApplicationVetoException,
                           ArchiveUnsupportedOperationException,
                           EngineEverybodyWorkItemException,
                           EngineLastAdminWorkItemException,
                           EngineNotAuthorizedException,
                           EngineParameterNullException,
                           EngineProcessReaderWorkItemException,
                           EngineWrongKindException,
                           EngineWrongStateException,
                           GroupWorkItemException,
                           HumanTaskManagerException,
                           IdWrongFormatException,
                           IdWrongTypeException,
                           InvalidLengthException,
                           ObjectDoesNotExistException,
                           UnexpectedFailureException,
                           WorkItemManagerException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
```

Following restrictions apply:
 
A work item with an assignment reason "owner" or "starter" cannot be deleted.
 A work item with an assignment reason "administrator" can only
 be deleted as long as it is not the last work item with this assignment reason for
 the associated process instance.
 A "reader" or "administrator" work item that has been propagated from the process instance
 to the activity instance can only be deleted on the process instance.
 A work item for a specific user cannot be deleted when the work item is assigned to everybody.
 

 The process instance must be in the running, failing, or terminating execution state.
 When a work item for an activity instance is to be deleted,
 the activity instance must be in the claimed, ready, running, or stopped execution state.
 The activity must be an invoke, script, or human task activity.
 A human task activity is also known as staff activity.
 
 The caller must be an administrator of the process instance
 or be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.

Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- deleteWorkItem void deleteWorkItem(PIID piid, int assignmentReason, java.lang.String userID) throws ApplicationVetoException , ArchiveUnsupportedOperationException , EngineEverybodyWorkItemException , EngineLastAdminWorkItemException , EngineNotAuthorizedException , EngineParameterNullException , EngineProcessReaderWorkItemException , EngineWrongKindException , EngineWrongStateException , GroupWorkItemException , HumanTaskManagerException , IdWrongFormatException , InvalidLengthException , ObjectDoesNotExistException , UnexpectedFailureException , WorkItemManagerException , java.rmi.RemoteException, javax.ejb.EJBException Deletes the specified work item for the specified process instance. Following restrictions apply: The deletion of a process reader or administrator work item is automatically propagated to all enclosed activities. The process instance must be in the running, failing, or terminating execution state. The caller must be an administrator of the process instance. This method is not supported in archive mode. Parameters: piid - The object ID of the process instance the work item belongs to. assignmentReason - The reason why the work item has been assigned - refer to the work item assignment reasons . userID - The user the work item belongs to. Throws: ApplicationVetoException ArchiveUnsupportedOperationException EngineEverybodyWorkItemException EngineLastAdminWorkItemException EngineNotAuthorizedException EngineParameterNullException EngineProcessReaderWorkItemException EngineWrongKindException EngineWrongStateException GroupWorkItemException HumanTaskManagerException IdWrongFormatException InvalidLengthException ObjectDoesNotExistException UnexpectedFailureException WorkItemManagerException java.rmi.RemoteException javax.ejb.EJBException Since: 5.1 Change History Release Modification 6.0.2 Throws an ApplicationVetoException when the application refuses to execute the method. 6.0.2 Throws an EngineProcessReaderWorkItemException when a process reader work item already exists. 6.0.2 Throws a HumanTaskManagerException when the Human Task Manager reports an error. 6.0.2 Throws a UserDoesNotExistException when the specified user does not exist. 6.1 Throws a GroupWorkItemException when a group is specified as user ID. 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### deleteWorkItem

```
void deleteWorkItem(PIID piid,
                  int assignmentReason,
                  java.lang.String userID)
                    throws ApplicationVetoException,
                           ArchiveUnsupportedOperationException,
                           EngineEverybodyWorkItemException,
                           EngineLastAdminWorkItemException,
                           EngineNotAuthorizedException,
                           EngineParameterNullException,
                           EngineProcessReaderWorkItemException,
                           EngineWrongKindException,
                           EngineWrongStateException,
                           GroupWorkItemException,
                           HumanTaskManagerException,
                           IdWrongFormatException,
                           InvalidLengthException,
                           ObjectDoesNotExistException,
                           UnexpectedFailureException,
                           WorkItemManagerException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
```

Following restrictions apply:
 
A work item with an assignment reason "starter" cannot be deleted.
 A work item with an assignment reason "administrator" can only
 be deleted as long as it is not the last work item with this assignment reason for
 the process instance.
 A work item for a specific user cannot be deleted when the work item is assigned to everybody.
 

 The deletion of a process reader or administrator work item is automatically propagated to all enclosed activities.
 
 The process instance must be in the running, failing, or terminating execution state.
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.

Change History

Release
 Modification
 
6.0.2
 
 Throws an ApplicationVetoException when the application refuses to execute the method.
 
6.0.2
 
 Throws an EngineProcessReaderWorkItemException when a process reader work item already exists.
 
6.0.2
 
 Throws a HumanTaskManagerException when the Human Task Manager reports an error.
 
6.0.2
 
 Throws a UserDoesNotExistException when the specified user does not exist.
 
6.1
 
 Throws a GroupWorkItemException when a group is specified as user ID.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- deleteWorkItem void deleteWorkItem(AIID aiid, int assignmentReason, java.lang.String userID) throws ApplicationVetoException , ArchiveUnsupportedOperationException , EngineEverybodyWorkItemException , EngineLastAdminWorkItemException , EngineNotAuthorizedException , EngineParameterNullException , EngineProcessReaderWorkItemException , EngineWrongKindException , EngineWrongStateException , GroupWorkItemException , HumanTaskManagerException , IdWrongFormatException , InvalidLengthException , ObjectDoesNotExistException , UnexpectedFailureException , WorkItemManagerException , java.rmi.RemoteException, javax.ejb.EJBException Deletes the specified work item for the specified activity instance. Following restrictions apply: The caller must be an administrator of the process instance or be an administrator of a scope that contains the activity instance. This method is not supported in archive mode. Parameters: aiid - The object ID of the activity instance the work item belongs to. assignmentReason - The reason why the work item has been assigned - refer to the work item assignment reasons . userID - The user the work item belongs to. Throws: ApplicationVetoException ArchiveUnsupportedOperationException EngineEverybodyWorkItemException EngineLastAdminWorkItemException EngineNotAuthorizedException EngineParameterNullException EngineProcessReaderWorkItemException EngineWrongKindException EngineWrongStateException GroupWorkItemException HumanTaskManagerException IdWrongFormatException InvalidLengthException ObjectDoesNotExistException UnexpectedFailureException WorkItemManagerException java.rmi.RemoteException javax.ejb.EJBException Since: 5.1 Change History Release Modification 6.1.2 The caller may have administrator rights for the scope that contains the activity instance. 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### deleteWorkItem

```
void deleteWorkItem(AIID aiid,
                  int assignmentReason,
                  java.lang.String userID)
                    throws ApplicationVetoException,
                           ArchiveUnsupportedOperationException,
                           EngineEverybodyWorkItemException,
                           EngineLastAdminWorkItemException,
                           EngineNotAuthorizedException,
                           EngineParameterNullException,
                           EngineProcessReaderWorkItemException,
                           EngineWrongKindException,
                           EngineWrongStateException,
                           GroupWorkItemException,
                           HumanTaskManagerException,
                           IdWrongFormatException,
                           InvalidLengthException,
                           ObjectDoesNotExistException,
                           UnexpectedFailureException,
                           WorkItemManagerException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
```

Following restrictions apply:
 
A work item with an assignment reason "owner" cannot be deleted.
 A "reader" or "administrator" work item that has been propagated from the process instance
 to the activity instance can only be deleted on the process instance.
 A work item for a specific user cannot be deleted when the work item is assigned to everybody.
 
 The activity instance must be in the claimed, ready, running, or stopped execution state.
 The associated process instance must be in the running, failing, or terminating execution state.
 The activity must be an invoke, script, or human task activity.
 A human task activity is also known as staff activity.
 

 The caller must be an administrator of the process instance
 or be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.

Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- deleteWorkList
void deleteWorkList(java.lang.String workListName)
                    throws EngineNotAuthorizedException,
                           UnexpectedFailureException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
Deprecated. As of version 6.0, replaced by deleteStoredQuery.
Deletes the specified worklist.
 Only a business process administrator can delete a worklist.
 No error is signalled when the specified worklist does no longer exist.
 
 Refer to newWorkList for the creation of worklists.
Parameters:workListName - The name of the worklist to be deleted -
    refer to getWorkListNames for the retrieval of existing worklist names.
 
Throws:
EngineNotAuthorizedException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0

- executeWorkList
QueryResultSet executeWorkList(java.lang.String workListName)
                               throws IdWrongFormatException,
                                      ObjectDoesNotExistException,
                                      QueryInvalidOperandException,
                                      QueryInvalidTimestampException,
                                      QueryUndefinedParameterException,
                                      QueryUnknownColumnException,
                                      QueryUnknownOperatorException,
                                      QueryUnknownTableException,
                                      UnexpectedFailureException,
                                      java.rmi.RemoteException,
                                      javax.ejb.EJBException
Deprecated. As of version 6.0, replaced by query.
Executes the query defined by the worklist and returns the qualifying object properties.
 Only properties of objects are returned for which the logged-on user has a work item.
 Note that the business process administrator has special rights and can access all objects.
 
 Refer to newWorkList for the creation of worklists.
Parameters:workListName - The name of the worklist to be executed -
    refer to getWorkListNames for the retrieval of existing worklist names.
 
Returns:QueryResultSet -
    The qualifying object properties. If
    qualifying objects are not found, an empty query result set is returned. Refer
    to QueryResultSet
    for information on how to analyze the query result set.
 
Throws:
IdWrongFormatException
ObjectDoesNotExistException
QueryInvalidOperandException
QueryInvalidTimestampException
QueryUndefinedParameterException
QueryUnknownColumnException
QueryUnknownOperatorException
QueryUnknownTableException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0

- forceComplete
void forceComplete(java.lang.String aiid,
                 boolean continueOnError)
                   throws ArchiveUnsupportedOperationException,
                          EngineNotAuthorizedException,
                          EngineWrongKindException,
                          EngineWrongStateException,
                          IdWrongFormatException,
                          IdWrongTypeException,
                          InvalidLengthException,
                          ObjectDoesNotExistException,
                          UnexpectedFailureException,
                          java.rmi.RemoteException,
                          javax.ejb.EJBException
Forces the completion of an activity instance
 using a string representation of the activity instance ID.
 
 The activity instance must be in the stopped, running, ready, or claimed execution state
 or a wait activity in the waiting execution state.
 The running execution state requires that the activity does not invoke a sub-process.
 The associated process instance must be in the running, failing, terminating, or suspended execution state.
 
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 Forcing the completion of an activity instance states that navigation of the process
 instance can continue. Since no ouput is provided, the output variable is not updated.
 Any previously set output or fault is ignored.
 The exit condition of the activity is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance to be completed.continueOnError - A flag that indicates what should happen in case of an error, that is, when a
    system exception or an unhandled fault occurs. True
    states that navigation should continue, that is,
    the activity instance is set into execution state failed and the error is propagated
    to the associated process instance. False
    states that the activity instance should stay in execution state stopped.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- forceComplete
void forceComplete(AIID aiid,
                 boolean continueOnError)
                   throws ArchiveUnsupportedOperationException,
                          EngineNotAuthorizedException,
                          EngineWrongKindException,
                          EngineWrongStateException,
                          IdWrongFormatException,
                          InvalidLengthException,
                          ObjectDoesNotExistException,
                          UnexpectedFailureException,
                          java.rmi.RemoteException,
                          javax.ejb.EJBException
Forces the completion of an activity instance using the activity instance ID.
 
 The activity instance must be in the stopped, running, ready, or claimed execution state
 or a wait activity in the waiting execution state.
 The running execution state requires that the activity does not invoke a sub-process.
 The associated process instance must be in the running, failing, terminating, or suspended execution state.
 
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 Forcing the completion of an activity instance states that navigation of the process
 instance can continue. Since no ouput is provided, the output variable is not updated.
 Any previously set output or fault is ignored.
 The exit condition of the activity is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID to identify the activity instance to be completed.continueOnError - A flag that indicates what should happen in case of an error, that is, when a
    system exception or an unhandled fault occurs. True
    states that navigation should continue, that is,
    the activity instance is set into execution state failed and the error is propagated
    to the associated process instance. False
    states that the activity instance should stay in execution state stopped.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- forceComplete
void forceComplete(java.lang.String aiid,
                 ClientObjectWrapper output,
                 boolean continueOnError)
                   throws ArchiveUnsupportedOperationException,
                          EngineMessageAndCorrelationSetMismatchException,
                          EngineNotAuthorizedException,
                          EngineWrongKindException,
                          EngineWrongMessageTypeException,
                          EngineWrongStateException,
                          IdWrongFormatException,
                          IdWrongTypeException,
                          InvalidLengthException,
                          ObjectDoesNotExistException,
                          UnexpectedFailureException,
                          java.rmi.RemoteException,
                          javax.ejb.EJBException
Forces the completion of an activity instance
 using a string representation of the activity instance ID and an output message.
 
 The activity instance must be in the stopped, running, ready, or claimed execution state.
 The running execution state requires that the activity does not invoke a sub-process.
 The associated process instance must be in the running, failing, terminating, or suspended execution state.
 
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 Completion of an activity instance means that user processing finished and that
 navigation of the process instance can continue. An output message
 is passed to denote the successful execution of user processing. The activity instance
 is put into the finished execution state.
 
 Output message values are used to continue navigation.
 The exit condition of the activity is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance to be completed.output - The output message that denotes the successful result of processing.
    When the contents of the ClientObjectWrapper is null, the output variable is updated with null.
    If no output is passed, the output variable is not updated.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.
 

    Any previously set output or fault is ignored.continueOnError - A flag that indicates what should happen in case of an error, that is, when a
    system exception or an unhandled fault occurs. True
    states that navigation should continue, that is,
    the activity instance is set into execution state failed and the error is propagated
    to the associated process instance. False
    states that the activity instance should stay in execution state stopped.
 
Throws:
ArchiveUnsupportedOperationException
EngineMessageAndCorrelationSetMismatchException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 Throws an
 EngineWrongStateException when the activity instance is not in the stopped, running,
 ready, or claimed execution state.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 Throws an
 EngineMessageAndCorrelationSetMismatchException when the message
 and the correlation sets of the activity do not match.
 
7.0
 
 Throws an EngineWrongStateException when the process instance is not in the running, failing,
 suspended, or terminating execution state.

- forceComplete
void forceComplete(AIID aiid,
                 ClientObjectWrapper output,
                 boolean continueOnError)
                   throws ArchiveUnsupportedOperationException,
                          EngineMessageAndCorrelationSetMismatchException,
                          EngineNotAuthorizedException,
                          EngineWrongKindException,
                          EngineWrongMessageTypeException,
                          EngineWrongStateException,
                          IdWrongFormatException,
                          InvalidLengthException,
                          ObjectDoesNotExistException,
                          UnexpectedFailureException,
                          java.rmi.RemoteException,
                          javax.ejb.EJBException
Forces the completion of an activity instance using the activity instance ID
 and an output messsage.
 
 The activity instance must be in the stopped, running, ready, or claimed execution state.
 The running execution state requires that the activity does not invoke a sub-process.
 The associated process instance must be in the running, failing, terminating, or suspended execution state.
 
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 Completion of an activity instance means that user processing finished and that
 navigation of the process instance can continue. An output message
 is passed to denote the successful execution of user processing. The activity instance
 is put into the finished execution state.
 
 Output message values are used to continue navigation.
 The exit condition of the activity is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID to identify the activity instance to be completed.output - The output message that denotes the successful result of processing.
    When the contents of the ClientObjectWrapper is null, the output variable is updated with null.
    If no output is passed, the output variable is not updated.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.
 

    Any previously set output or fault is ignored.continueOnError - A flag that indicates what should happen in case of an error, that is, when a
    system exception or an unhandled fault occurs. True
    states that navigation should continue, that is,
    the activity instance is set into execution state failed and the error is propagated
    to the associated process instance. False
    states that the activity instance should stay in execution state stopped.
 
Throws:
ArchiveUnsupportedOperationException
EngineMessageAndCorrelationSetMismatchException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 Throws an
 EngineWrongStateException when the activity instance is not in the stopped, running,
 ready, or claimed execution state.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws an EngineMessageAndCorrelationSetMismatchException when the message
 and the correlation sets of the activity do not match.
 
7.0
 
 Throws an EngineWrongStateException when the process instance is not in the running, failing,
 suspended, or terminating execution state.

- forceComplete
void forceComplete(java.lang.String aiid,
                 ClientObjectWrapper message,
                 java.lang.String faultName,
                 boolean continueOnError)
                   throws ArchiveUnsupportedOperationException,
                          EngineMessageAndCorrelationSetMismatchException,
                          EngineNotAuthorizedException,
                          EngineParameterNullException,
                          EngineWrongKindException,
                          EngineWrongMessageTypeException,
                          EngineWrongStateException,
                          IdWrongFormatException,
                          IdWrongTypeException,
                          InvalidLengthException,
                          ObjectDoesNotExistException,
                          UnexpectedFailureException,
                          java.rmi.RemoteException,
                          javax.ejb.EJBException
Forces the completion of an activity instance
 using a string representation of the activity instance ID
 and states the actual result of user processing.
 
 The activity instance must be in the stopped, running, ready, or claimed execution state.
 The running execution state requires that the activity does not invoke a sub-process.
 The associated process instance must be in the running, failing, terminating, or suspended execution state.
 
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 Forcing the completion of an activity instance states that navigation of the process
 instance can continue.
 
 If user processing did not complete successfully, that is, if a fault message is
 passed, the activity instance is put into the failed execution state when the fault is handled
 or when the continueOnError flag is set to true. It remains in the
 stopped execution state when the fault is not handled and the continueOnError flag is set to false.
 
 Depending on the result of user processing, output or fault message values are used to
 continue navigation.
 The exit condition of the activity is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID to identify the activity instance to be completed.message - The fault message. If
    a fault is not to be provided, null must be specified; the process engine then uses
    the fault available to the system. The
    object wrapped by the ClientObjectWrapper must be serializable.
 

    If specified, any previously set output or fault is ignored.faultName - The name of the fault.
    The fault must have been defined for the activity. Refer
    to getFaultNames.
    Note that the structure of a BPEL fault name is a QName.continueOnError - A flag that indicates what should happen in case of an error, that is, when a
    system exception or an unhandled fault occurs. True
    states that navigation should continue, that is,
    the activity instance is set into execution state failed and the error is propagated
    to the associated process instance. False
    states that the activity instance should stay in execution state stopped.
 
Throws:
ArchiveUnsupportedOperationException
EngineMessageAndCorrelationSetMismatchException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 Throws an
 EngineWrongStateException when the activity instance is not in the stopped, running,
 ready, or claimed execution state.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws an EngineWrongStateException when the process instance is not in the running, failing,
 suspended, or terminating execution state.
 
7.0
 
 Throws an EngineMessageAndCorrelationSetMismatchException when the message
 and the correlation sets of the activity do not match.

- forceComplete
void forceComplete(AIID aiid,
                 ClientObjectWrapper message,
                 java.lang.String faultName,
                 boolean continueOnError)
                   throws ArchiveUnsupportedOperationException,
                          EngineMessageAndCorrelationSetMismatchException,
                          EngineNotAuthorizedException,
                          EngineParameterNullException,
                          EngineWrongKindException,
                          EngineWrongMessageTypeException,
                          EngineWrongStateException,
                          IdWrongFormatException,
                          InvalidLengthException,
                          ObjectDoesNotExistException,
                          UnexpectedFailureException,
                          java.rmi.RemoteException,
                          javax.ejb.EJBException
Forces the completion of an activity instance using the activity instance ID
 and states the actual result of user processing.
 
 The activity instance must be in the stopped, running, ready, or claimed execution state.
 The running execution state requires that the activity does not invoke a sub-process.
 The associated process instance must be in the running, failing, terminating, or suspended execution state.
 
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 Forcing the completion of an activity instance states that navigation of the process
 instance can continue.
 
 If user processing did not complete successfully, that is, if a fault message is
 passed, the activity instance is put into the failed execution state when the fault is handled
 or when the continueOnError flag is set to true. It remains in the
 stopped execution state when the fault is not handled and the continueOnError flag is set to false.
 
 Depending on the result of user processing, output or fault message values are used to
 continue navigation.
 The exit condition of the activity is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID to identify the activity instance to be completed.message - The fault message. If
    a fault is not to be provided, null must be specified; the process engine then uses
    the fault available to the system. The
    object wrapped by the ClientObjectWrapper must be serializable.
 
    If specified, any previously set output or fault is ignored.faultName - The name of the fault.
    The fault must have been defined for the activity. Refer
    to getFaultNames.
    Note that the structure of a BPEL fault name is a QName.continueOnError - A flag that indicates what should happen in case of an error, that is, when a
    system exception or an unhandled fault occurs. True
    states that navigation should continue, that is,
    the activity instance is set into execution state failed and the error is propagated
    to the associated process instance. False
    states that the activity instance should stay in execution state stopped.
 
Throws:
ArchiveUnsupportedOperationException
EngineMessageAndCorrelationSetMismatchException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 Throws an
 EngineWrongStateException when the activity instance is not in the stopped, running,
 ready, or claimed execution state.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws an EngineMessageAndCorrelationSetMismatchException when the message
 and the correlation sets of the activity do not match.
 
7.0
 
 Throws an EngineWrongStateException when the process instance is not in the running, failing,
 suspended, or terminating execution state.

- forceCompleteAndJump
void forceCompleteAndJump(java.lang.String aiid,
                        ClientObjectWrapper output,
                        java.lang.String targetActivityName)
                          throws ArchiveUnsupportedOperationException,
                                 EngineAmbiguousActivityException,
                                 EngineInvalidNamespaceURIException,
                                 EngineMessageAndCorrelationSetMismatchException,
                                 EngineNotAuthorizedException,
                                 EngineParameterNullException,
                                 EngineProcessWrongBuildVersionException,
                                 EngineUnknownActivityException,
                                 EngineUnsupportedJumpException,
                                 EngineWrongKindException,
                                 EngineWrongMessageTypeException,
                                 EngineWrongStateException,
                                 IdWrongFormatException,
                                 IdWrongTypeException,
                                 InvalidLengthException,
                                 ObjectDoesNotExistException,
                                 UnexpectedFailureException,
                                 java.rmi.RemoteException,
                                 javax.ejb.EJBException
Forces the completion of an activity instance using a string representation of the
 activity instance ID and continues navigation at the specified target activity.
 
 The activity to be completed
 must be in the ready, claimed, running, or stopped execution state,
 or a wait activity in the waiting execution state.
 The running execution state requires that the activity does not invoke a sub-process.
 The associated process instance must be in the running, failing, terminating, or suspended execution state.
 The caller must be an administrator of the associated process instance or
 of a scope that contains the activity instance to be completed.
 
 Completion of an activity instance means that user processing finished and that
 navigation of the process instance can continue. An output message can be passed
 to denote the result of user processing. The activity instance
 is put into the finished execution state.
 
 In difference to the forceComplete request,
 output message values are not used to continue navigation, that is, transition conditions
 are not evaluated. Navigation continues at the specified target activity.
 The exit condition of the completed activity is not evaluated.
 
 The activity to jump to must be in the same cyclic flow or sequence. You can jump forwards
 or backwards. When jumping backwards within a sequence, the activity instances between the completed
 activity instance and the jumped-to activity are deleted but compensation is not triggered.
 Compensation handlers are, however, registered for scopes so that compensation may run later.
 
 If the activity to jump to is inside a forEach construct or an event handler,
 then the activity jumped to must be within the same forEach iteration or event handler instance
 as the completed activity.
 
 The exit condition on the entry of the activity to jump to is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance to be completed.output - An optional output message that denotes the result of processing.
    When the contents of the ClientObjectWrapper is null, the output variable is updated with null.
    If output is not to be provided, null must be specified.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.
 

    Any previously set output or fault is ignored.targetActivityName - The name of an activity to jump to. The activity can be a basic activity
 as well as a structured activity.
 
Throws:
ArchiveUnsupportedOperationException
EngineAmbiguousActivityException
EngineInvalidNamespaceURIException
EngineMessageAndCorrelationSetMismatchException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessWrongBuildVersionException
EngineUnknownActivityException
EngineUnsupportedJumpException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws an EngineMessageAndCorrelationSetMismatchException when the message
 and the correlation sets of the activity do not match.

- forceCompleteAndJump
void forceCompleteAndJump(AIID aiid,
                        ClientObjectWrapper output,
                        java.lang.String targetActivityName)
                          throws ArchiveUnsupportedOperationException,
                                 EngineAmbiguousActivityException,
                                 EngineInvalidNamespaceURIException,
                                 EngineMessageAndCorrelationSetMismatchException,
                                 EngineNotAuthorizedException,
                                 EngineParameterNullException,
                                 EngineProcessWrongBuildVersionException,
                                 EngineUnknownActivityException,
                                 EngineUnsupportedJumpException,
                                 EngineWrongKindException,
                                 EngineWrongMessageTypeException,
                                 EngineWrongStateException,
                                 IdWrongFormatException,
                                 InvalidLengthException,
                                 ObjectDoesNotExistException,
                                 UnexpectedFailureException,
                                 java.rmi.RemoteException,
                                 javax.ejb.EJBException
Forces the completion of an activity instance using the activity instance ID
 and continues navigation at the specified target activity.
 
 The activity to be completed
 must be in the ready, claimed, running, or stopped execution state,
 or a wait activity in the waiting execution state.
 The running execution state requires that the activity does not invoke a sub-process.
 The associated process instance must be in the running, failing, terminating, or suspended execution state.
 The caller must be an administrator of the associated process instance or
 of a scope that contains the activity instance to be completed.
 
 Completion of an activity instance means that user processing finished and that
 navigation of the process instance can continue. An output message can be passed
 to denote the result of user processing. The activity instance
 is put into the finished execution state.
 
 In difference to the complete request,
 output message values are not used to continue navigation, that is, transition conditions
 are not evaluated. Navigation continues at the specified target activity.
 The exit condition of the completed activity is not evaluated.
 
 The activity to jump to must be in the same cyclic flow or sequence. You can jump forwards
 or backwards. When jumping backwards within a sequence, the activity instances between the completed
 activity instance and the jumped-to activity are deleted but compensation is not triggered.
 Compensation handlers are, however, registered for scopes so that compensation may run later.
 
 If the activity to jump to is inside a forEach construct or an event handler,
 then the activity jumped to must be within the same forEach iteration or event handler instance
 as the completed activity.
 
 The exit condition on the entry of the activity to jump to is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID to identify the activity instance to be completed.output - An optional output message that denotes the result of processing.
    When the contents of the ClientObjectWrapper is null, the output variable is updated with null.
    If output is not to be provided, null must be specified.
    Note that the object wrapped by the ClientObjectWrapper must be serializable.
 

    Any previously set output or fault is ignored.targetActivityName - The name of an activity to jump to. The activity can be a basic activity
 as well as a structured activity.
 
Throws:
ArchiveUnsupportedOperationException
EngineAmbiguousActivityException
EngineInvalidNamespaceURIException
EngineMessageAndCorrelationSetMismatchException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessWrongBuildVersionException
EngineUnknownActivityException
EngineUnsupportedJumpException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 
 Throws an EngineMessageAndCorrelationSetMismatchException when the message
 and the correlation sets of the activity do not match.

- forceForEachCounterValues
void forceForEachCounterValues(java.lang.String aiid,
                             int startCounter,
                             int finalCounter,
                             java.lang.Integer maxCompletedBranches)
                               throws ArchiveUnsupportedOperationException,
                                      EngineInvalidMaxCompletedBranchesException,
                                      EngineNotAuthorizedException,
                                      EngineWrongKindException,
                                      EngineWrongStateException,
                                      IdWrongFormatException,
                                      IdWrongTypeException,
                                      ObjectDoesNotExistException,
                                      UnexpectedFailureException,
                                      java.rmi.RemoteException,
                                      javax.ejb.EJBException
Forces the navigation of an activity instance that stopped because
 the evaluation of for-each counter values failed
 using a string representation of the activity instance ID.
 
 The specified values are used as the result of the forEach counter evaluations.
 Note that the value passed as parameter maxCompletedBranches must not be greater
 than the number of iterations evaluated through the values passed as parameters
 startCounter and finalCounter.
 If so, the completion condition of the forEach activity can never be true.
 
 The activity instance must be in the stopped execution state with stop reason
 IMPLEMENTATION\_FAILED.
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance.startCounter - The start counter.finalCounter - The final counter.maxCompletedBranches - An optional number of branches that must be completed before the forEach activity can be completed.
 
Throws:
ArchiveUnsupportedOperationException
EngineInvalidMaxCompletedBranchesException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
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

- forceForEachCounterValues
void forceForEachCounterValues(AIID aiid,
                             int startCounter,
                             int finalCounter,
                             java.lang.Integer maxCompletedBranches)
                               throws ArchiveUnsupportedOperationException,
                                      EngineInvalidMaxCompletedBranchesException,
                                      EngineNotAuthorizedException,
                                      EngineWrongKindException,
                                      EngineWrongStateException,
                                      IdWrongFormatException,
                                      ObjectDoesNotExistException,
                                      UnexpectedFailureException,
                                      java.rmi.RemoteException,
                                      javax.ejb.EJBException
Forces the navigation of an activity instance that stopped because
 the evaluation of for-each counter values failed
 using the activity instance ID.
 
 The specified values are used as the result of the forEach counter evaluations.
 Note that the value passed as parameter maxCompletedBranches must not be greater
 than the number of iterations evaluated through the values passed as parameters
 startCounter and finalCounter.
 If so, the completion condition of the forEach activity can never be true.
 
 The activity instance must be in the stopped execution state with stop reason
 IMPLEMENTATION\_FAILED.
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID of the activity instance that is used
    to identify the activity instance.startCounter - The start counter.finalCounter - The final counter.maxCompletedBranches - An optional number of branches that must be completed before the forEach activity can be completed.
 
Throws:
ArchiveUnsupportedOperationException
EngineInvalidMaxCompletedBranchesException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
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

- forceJoinCondition
void forceJoinCondition(java.lang.String aiid,
                      boolean conditionValue)
                        throws ArchiveUnsupportedOperationException,
                               EngineNotAuthorizedException,
                               EngineWrongKindException,
                               EngineWrongStateException,
                               IdWrongFormatException,
                               IdWrongTypeException,
                               ObjectDoesNotExistException,
                               UnexpectedFailureException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
Forces the navigation of an activity instance that stopped because
 the join condition evaluation failed
 using a string representation of the activity instance ID.
 The specified condition value is used as the result of the join condition evaluation.
 
 The activity instance must be in the stopped execution state with stop reason
 ACTIVATION\_FAILED.
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance.conditionValue - The value that is to be used as the result of the join condition evaluation.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
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

- forceJoinCondition
void forceJoinCondition(AIID aiid,
                      boolean conditionValue)
                        throws ArchiveUnsupportedOperationException,
                               EngineNotAuthorizedException,
                               EngineWrongKindException,
                               EngineWrongStateException,
                               IdWrongFormatException,
                               ObjectDoesNotExistException,
                               UnexpectedFailureException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
Forces the navigation of an activity instance that stopped because
 the join condition evaluation failed
 using the activity instance ID.
 The specified condition value is used as the result of the join condition evaluation.
 
 The activity instance must be in the stopped execution state with stop reason
 ACTIVATION\_FAILED.
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID of the activity instance that is used
    to identify the activity instance.conditionValue - The value that is to be used as the result of the join condition evaluation.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
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

- forceLoopCondition
void forceLoopCondition(java.lang.String aiid,
                      boolean conditionValue)
                        throws ArchiveUnsupportedOperationException,
                               EngineNotAuthorizedException,
                               EngineWrongKindException,
                               EngineWrongStateException,
                               IdWrongFormatException,
                               IdWrongTypeException,
                               ObjectDoesNotExistException,
                               UnexpectedFailureException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
Forces the navigation of an activity instance that stopped because
 a loop condition evaluation failed
 using a string representation of the activity instance ID.
 
 The specified condition value is used as the result of a while or repeat-until condition evaluation
 to determine whether the next iteration should be performed
 A condition value of true means for a while activity that the next iteration should be started.
 A condition value of true means for a repeat-until activity that iterating should be stopped.
 
 The activity instance must be in the stopped execution state with stop reason
 IMPLEMENTATION\_FAILED.
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance.conditionValue - The value that is to be used as the result of the loop condition evaluation.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
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

- forceLoopCondition
void forceLoopCondition(AIID aiid,
                      boolean conditionValue)
                        throws ArchiveUnsupportedOperationException,
                               EngineNotAuthorizedException,
                               EngineWrongKindException,
                               EngineWrongStateException,
                               IdWrongFormatException,
                               ObjectDoesNotExistException,
                               UnexpectedFailureException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
Forces the navigation of an activity instance that stopped because
 a loop condition evaluation failed
 using the activity instance ID.
 
 The specified condition value is used as the result of a while or repeat-until condition evaluation
 to determine whether the next iteration should be performed
 A condition value of true means for a while activity that the next iteration should be started.
 A condition value of true means for a repeat-until activity that iterating should be stopped.
 
 The activity instance must be in the stopped execution state with stop reason
 IMPLEMENTATION\_FAILED.
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID of the activity instance that is used
    to identify the activity instance.conditionValue - The value that is to be used as the result of the loop condition evaluation.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
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

- forceNavigate
void forceNavigate(java.lang.String aiid,
                 java.lang.String[] linksToBeFollowed)
                   throws ArchiveUnsupportedOperationException,
                          InvalidParameterValueException,
                          EngineNotAuthorizedException,
                          EngineParameterNullException,
                          EngineWrongStateException,
                          IdWrongFormatException,
                          IdWrongTypeException,
                          ObjectDoesNotExistException,
                          UnexpectedFailureException,
                          java.rmi.RemoteException,
                          javax.ejb.EJBException
Forces the navigation of links leaving the specified activity instance
 using a string representation of the activity instance ID.
 The specified links are then followed without evaluation of their conditions.
 
 The activity instance must be in the stopped execution state with stop reason
 FOLLOW\_ON\_NAVIGATION\_FAILED.
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance.linksToBeFollowed - An array of link
    names identifying the links to be followed. The conditions
    of links that are not specified are set to false.
 
Throws:
ArchiveUnsupportedOperationException
InvalidParameterValueException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- forceNavigate
void forceNavigate(AIID aiid,
                 java.lang.String[] linksToBeFollowed)
                   throws ArchiveUnsupportedOperationException,
                          InvalidParameterValueException,
                          EngineNotAuthorizedException,
                          EngineParameterNullException,
                          EngineWrongStateException,
                          IdWrongFormatException,
                          ObjectDoesNotExistException,
                          UnexpectedFailureException,
                          java.rmi.RemoteException,
                          javax.ejb.EJBException
Forces the navigation of links leaving the specified activity instance
 using the activity instance ID.
 The specified links are then followed without evaluation of their conditions.
 
 The activity instance must be in the stopped execution state with stop reason
 FOLLOW\_ON\_NAVIGATION\_FAILED.
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID of the activity instance that is used
    to identify the activity instance.linksToBeFollowed - An array of link
    names identifying the links to be followed. The conditions
    of links that are not specified are set to false.
 
Throws:
ArchiveUnsupportedOperationException
InvalidParameterValueException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- forceNavigate
void forceNavigate(java.lang.String aiid,
                 int positionOfBranch)
                   throws ArchiveUnsupportedOperationException,
                          EngineNotAuthorizedException,
                          EngineWrongKindException,
                          EngineWrongStateException,
                          IdWrongFormatException,
                          IdWrongTypeException,
                          InvalidParameterValueException,
                          ObjectDoesNotExistException,
                          UnexpectedFailureException,
                          java.rmi.RemoteException,
                          javax.ejb.EJBException
Forces the navigation of a branch of the specified switch activity
 using a string representation of the activity instance ID.
 The specified branch is then followed without evaluation of its condition.
 
 The activity instance must be in the stopped execution state with stop reason
 IMPLEMENTATION\_FAILED.
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance.positionOfBranch - The branch of the switch activity that is to be followed. The branch
    is identified by its position in the BranchTemplateData array returned by the
    getBranches method.
    Note that valid positions are 0 to array size minus 1.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
InvalidParameterValueException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- forceNavigate
void forceNavigate(AIID aiid,
                 int positionOfBranch)
                   throws ArchiveUnsupportedOperationException,
                          EngineNotAuthorizedException,
                          EngineWrongKindException,
                          EngineWrongStateException,
                          IdWrongFormatException,
                          InvalidParameterValueException,
                          ObjectDoesNotExistException,
                          UnexpectedFailureException,
                          java.rmi.RemoteException,
                          javax.ejb.EJBException
Forces the navigation of a branch of the specified switch activity
 using the activity instance ID.
 The specified branch is then followed without evaluation of its condition.
 
 The activity instance must be in the stopped execution state with stop reason
 IMPLEMENTATION\_FAILED.
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID of the activity instance that is used
    to identify the activity instance.positionOfBranch - The branch of the switch activity that is to be followed. The branch
    is identified by its position in the BranchTemplateData array returned by the
    getBranches method.
    Note that valid positions are 0 to array size minus 1.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
InvalidParameterValueException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- forceRetry
void forceRetry(java.lang.String aiid,
              boolean continueOnError)
                throws ArchiveUnsupportedOperationException,
                       EngineNotAuthorizedException,
                       EngineWrongKindException,
                       EngineWrongMessageTypeException,
                       EngineWrongStateException,
                       IdWrongFormatException,
                       IdWrongTypeException,
                       ObjectDoesNotExistException,
                       UnexpectedFailureException,
                       java.rmi.RemoteException,
                       javax.ejb.EJBException
Forces the repetition of an activity instance
 using a string representation of the activity instance ID.
 
 The activity instance must be in the stopped, running, ready, or claimed execution state.
 The associated process instance must be in the running execution state.
 
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 If the activity has been stopped because of a timeout, then the expiration timer
 is reset.
 
 Since no input message is passed, the process engine uses the input message
 available to the system.
 The exit condition on the entry of the activity is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance to be retried.continueOnError - A flag that indicates what should happen in case of an error, that is, when a
    system exception or an unhandled fault occurs. True
    states that navigation should continue, that is,
    the activity instance is set into execution state failed and the error is propagated
    to the associated process instance. False
    states that the activity instance should stay in execution state stopped.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- forceRetry
void forceRetry(AIID aiid,
              boolean continueOnError)
                throws ArchiveUnsupportedOperationException,
                       EngineNotAuthorizedException,
                       EngineWrongKindException,
                       EngineWrongMessageTypeException,
                       EngineWrongStateException,
                       IdWrongFormatException,
                       ObjectDoesNotExistException,
                       UnexpectedFailureException,
                       java.rmi.RemoteException,
                       javax.ejb.EJBException
Forces the repetition of an activity instance using the activity instance ID.
 
 The activity instance must be in the stopped, running, ready, or claimed execution state.
 The associated process instance must be in the running execution state.
 
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 If the activity has been stopped because of a timeout, then the expiration timer
 is reset.
 
 Since no input message is passed, the process engine uses the input message
 available to the system.
 The exit condition on the entry of the activity is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID to identify the activity instance to be retried.continueOnError - A flag that indicates what should happen in case of an error, that is, when a
    system exception or an unhandled fault occurs. True
    states that navigation should continue, that is,
    the activity instance is set into execution state failed and the error is propagated
    to the associated process instance. False
    states that the activity instance should stay in execution state stopped.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- forceRetry
void forceRetry(java.lang.String aiid,
              boolean continueOnError,
              int timerBehavior)
                throws ArchiveUnsupportedOperationException,
                       EngineNotAuthorizedException,
                       EngineWrongKindException,
                       EngineWrongStateException,
                       IdWrongFormatException,
                       IdWrongTypeException,
                       InvalidParameterValueException,
                       ObjectDoesNotExistException,
                       UnexpectedFailureException,
                       java.rmi.RemoteException,
                       javax.ejb.EJBException
Forces the repetition of an activity instance
 using a string representation of the activity instance ID and specifies how to handle timers.
 
 The activity instance must be in the stopped, running, ready, or claimed execution state.
 The associated process instance must be in the running execution state.
 
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 If an input message is needed, the process engine uses the input message
 available to the system.
 The exit condition on the entry of the activity is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance to be retried.continueOnError - A flag that indicates what should happen in case of an error, that is, when
    a system exception, an unhandled fault, or an exception during scheduling of the
    expiration occurs.
    True states that navigation should continue, that is,
    the activity instance is set into execution state failed and the error is propagated
    to the associated process instance. False
    states that the activity instance should stay in execution state stopped.timerBehavior - An indicator that specifies how to handle timers when the activity is retried -
    refer to TimerBehavior for valid values.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
InvalidParameterValueException
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

- forceRetry
void forceRetry(AIID aiid,
              boolean continueOnError,
              int timerBehavior)
                throws ArchiveUnsupportedOperationException,
                       EngineNotAuthorizedException,
                       EngineWrongKindException,
                       EngineWrongStateException,
                       IdWrongFormatException,
                       InvalidParameterValueException,
                       ObjectDoesNotExistException,
                       UnexpectedFailureException,
                       java.rmi.RemoteException,
                       javax.ejb.EJBException
Forces the repetition of an activity instance using the activity instance ID
 and specifies how to handle timers.
 
 The activity instance must be in the stopped, running, ready, or claimed execution state.
 The associated process instance must be in the running execution state.
 
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 If an input message is needed, the process engine uses the input message
 available to the system.
 The exit condition on the entry of the activity is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID to identify the activity instance to be retried.continueOnError - A flag that indicates what should happen in case of an error, that is, when
    a system exception, an unhandled fault, or an exception during scheduling of the
    expiration occurs.
    True states that navigation should continue, that is,
    the activity instance is set into execution state failed and the error is propagated
    to the associated process instance. False
    states that the activity instance should stay in execution state stopped.timerBehavior - An indicator that specifies how to handle timers when the activity is retried -
    refer to TimerBehavior for valid values.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
InvalidParameterValueException
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

- forceRetry
void forceRetry(java.lang.String aiid,
              ClientObjectWrapper inputMessage,
              boolean continueOnError)
                throws ArchiveUnsupportedOperationException,
                       EngineMessageAndCorrelationSetMismatchException,
                       EngineNotAuthorizedException,
                       EngineWrongKindException,
                       EngineWrongMessageTypeException,
                       EngineWrongStateException,
                       IdWrongFormatException,
                       IdWrongTypeException,
                       ObjectDoesNotExistException,
                       UnexpectedFailureException,
                       java.rmi.RemoteException,
                       javax.ejb.EJBException
Forces the repetition of an activity instance
 using a string representation of the activity instance ID and an input message.
 
 The activity instance must be in the stopped, running, ready, or claimed execution state.
 The associated process instance must be in the running execution state.
 
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 If the activity has been stopped because of a timeout, then the expiration timer
 is reset.
 
 The exit condition on the entry of the activity is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance to be retried.inputMessage - The input message that specifies the values to be used by the activity instance. If
    input is not to be provided, null must be specified; the process engine then uses
    the input available to the system. An empty ClientObjectWrapper causes the input message
    to be set to null. The
    object wrapped by the ClientObjectWrapper must be serializable.continueOnError - A flag that indicates what should happen in case of an error, that is, when a
    system exception or an unhandled fault occurs. True
    states that navigation should continue, that is,
    the activity instance is set into execution state failed and the error is propagated
    to the associated process instance. False
    states that the activity instance should stay in execution state stopped.
 
Throws:
ArchiveUnsupportedOperationException
EngineMessageAndCorrelationSetMismatchException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2
 
 Throws an EngineMessageAndCorrelationSetMismatchException when the message
 and the correlation sets of the activity do not match.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- forceRetry
void forceRetry(AIID aiid,
              ClientObjectWrapper inputMessage,
              boolean continueOnError)
                throws ArchiveUnsupportedOperationException,
                       EngineMessageAndCorrelationSetMismatchException,
                       EngineNotAuthorizedException,
                       EngineWrongKindException,
                       EngineWrongMessageTypeException,
                       EngineWrongStateException,
                       IdWrongFormatException,
                       ObjectDoesNotExistException,
                       UnexpectedFailureException,
                       java.rmi.RemoteException,
                       javax.ejb.EJBException
Forces the repetition of an activity instance using the activity instance ID
 and an input message.
 
 The activity instance must be in the stopped, running, ready, or claimed execution state.
 The associated process instance must be in the running execution state.
 
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 If the activity has been stopped because of a timeout, then the expiration timer
 is reset.
 
 The exit condition on the entry of the activity is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID to identify the activity instance to be retried.inputMessage - The input message that specifies the values to be used by the activity instance. If
    input is not to be provided, null must be specified; the process engine then uses
    the input available to the system. An empty ClientObjectWrapper causes the input message
    to be set to null. The
    object wrapped by the ClientObjectWrapper must be serializable.continueOnError - A flag that indicates what should happen in case of an error, that is, when a
    system exception or an unhandled fault occurs. True
    states that navigation should continue, that is,
    the activity instance is set into execution state failed and the error is propagated
    to the associated process instance. False
    states that the activity instance should stay in execution state stopped.
 
Throws:
ArchiveUnsupportedOperationException
EngineMessageAndCorrelationSetMismatchException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2
 
 Throws an EngineMessageAndCorrelationSetMismatchException when the message
 and the correlation sets of the activity do not match.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- forceRetry
void forceRetry(java.lang.String aiid,
              ClientObjectWrapper inputMessage,
              boolean continueOnError,
              int timerBehavior)
                throws ArchiveUnsupportedOperationException,
                       EngineMessageAndCorrelationSetMismatchException,
                       EngineNotAuthorizedException,
                       EngineWrongKindException,
                       EngineWrongMessageTypeException,
                       EngineWrongStateException,
                       IdWrongFormatException,
                       IdWrongTypeException,
                       InvalidParameterValueException,
                       ObjectDoesNotExistException,
                       UnexpectedFailureException,
                       java.rmi.RemoteException,
                       javax.ejb.EJBException
Forces the repetition of an activity instance
 using a string representation of the activity instance ID
 and passes an input message and a timer specification.
 
 The activity instance must be in the stopped, running, ready, or claimed execution state.
 The associated process instance must be in the running execution state.
 
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 Optionally, an input message may be provided. The process engine uses the input message
 provided.
 The exit condition on the entry of the activity is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance to be retried.inputMessage - The input message that specifies the values to be used by the activity instance. If
    input is not to be provided, null must be specified; the process engine then uses
    the input available to the system. An empty ClientObjectWrapper causes the input message
    to be set to null. The
    object wrapped by the ClientObjectWrapper must be serializable.continueOnError - A flag that indicates what should happen in case of an error, that is, when
    a system exception, an unhandled fault, or an exception during scheduling of the
    expiration occurs.
    True states that navigation should continue, that is,
    the activity instance is set into execution state failed and the error is propagated
    to the associated process instance. False
    states that the activity instance should stay in execution state stopped.timerBehavior - An indicator that specifies how to handle timers when the activity is retried -
    refer to TimerBehavior for valid values.
 
Throws:
ArchiveUnsupportedOperationException
EngineMessageAndCorrelationSetMismatchException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
InvalidParameterValueException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2
 
 The expiration behavior is replaced by a more generic timer behavior.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 Throws an
 EngineMessageAndCorrelationSetMismatchException when the message
 and the correlation sets of the activity do not match.

- forceRetry
void forceRetry(AIID aiid,
              ClientObjectWrapper inputMessage,
              boolean continueOnError,
              int timerBehavior)
                throws ArchiveUnsupportedOperationException,
                       EngineMessageAndCorrelationSetMismatchException,
                       EngineNotAuthorizedException,
                       EngineWrongKindException,
                       EngineWrongMessageTypeException,
                       EngineWrongStateException,
                       IdWrongFormatException,
                       InvalidParameterValueException,
                       ObjectDoesNotExistException,
                       UnexpectedFailureException,
                       java.rmi.RemoteException,
                       javax.ejb.EJBException
Forces the repetition of an activity instance using the activity instance ID
 and passes an input message and a timer specification.
 
 The activity instance must be in the stopped, running, ready, or claimed execution state.
 The associated process instance must be in the running execution state.
 
 The caller must be an administrator of the activity instance, the associated process instance,
 or of a scope that contains the activity instance.
 
 Optionally, an input message may be provided. The process engine then uses the input message
 provided.
 The exit condition on the entry of the activity is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID to identify the activity instance to be retried.inputMessage - The input message that specifies the values to be used by the activity instance. If
    input is not to be provided, null must be specified; the process engine then uses
    the input available to the system. An empty ClientObjectWrapper causes the input message
    to be set to null. The
    object wrapped by the ClientObjectWrapper must be serializable.continueOnError - A flag that indicates what should happen in case of an error, that is, when
    a system exception, an unhandled fault, or an exception during scheduling of the
    expiration occurs.
    True states that navigation should continue, that is,
    the activity instance is set into execution state failed and the error is propagated
    to the associated process instance. False
    states that the activity instance should stay in execution state stopped.timerBehavior - An indicator that specifies how to handle timers when the activity is retried -
    refer to TimerBehavior for valid values.
 
Throws:
ArchiveUnsupportedOperationException
EngineMessageAndCorrelationSetMismatchException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
InvalidParameterValueException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2
 
 The expiration behavior is replaced by a more generic timer behavior.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 Throws an
 EngineMessageAndCorrelationSetMismatchException when the message
 and the correlation sets of the activity do not match.

- forceTerminate
void forceTerminate(java.lang.String identifier)
                    throws ArchiveUnsupportedOperationException,
                           EngineNotAuthorizedException,
                           EngineWrongKindException,
                           EngineWrongStateException,
                           IdWrongTypeException,
                           ObjectDoesNotExistException,
                           UnexpectedFailureException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
Terminates the specified top-level process instance, its non-autonomous subprocesses,
 and its running, claimed, or waiting activities using a string representation of the process instance ID
 or the process instance name.
 For example, you can use
 these capabilities to remove failed process instances that are still in a
 running state. This example might result from an invoked application that
 failed and that did not return to a dormant state.
 
 Use the process termination capabilities as a last resort only.
 The process instance is immediately terminated without waiting for outstanding activities to complete.
 Process instances that are terminated are not compensated.
 
 The process instance must be in the running, suspended, or failing execution state.
 Only an administrator of the process instance can terminate the process instance.
 
 The process instance is put into the terminated execution state.
 
 If the "auto delete" option is not set or set to 'true',
 the process instance is automatically deleted.
 
 This method is not supported in archive mode.
Parameters:identifier - The string representation of the process instance object ID or the name of the
    process instance. This is used to identify the process instance that is to be terminated.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- forceTerminate
void forceTerminate(PIID piid)
                    throws ArchiveUnsupportedOperationException,
                           EngineNotAuthorizedException,
                           EngineWrongKindException,
                           EngineWrongStateException,
                           IdWrongFormatException,
                           ObjectDoesNotExistException,
                           UnexpectedFailureException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
Terminates the specified top-level process instance, its non-autonomous subprocesses, and
 its running, claimed, or waiting activities using the process instance ID.
 For example, you can use
 these capabilities to remove failed process instances that are still in a
 running state. This example might result from an invoked application that
 failed and that did not return to a dormant state.
 
 Use the process termination capabilities as a last resort only.
 The process instance is immediately terminated without waiting for outstanding activities to complete.
 Process instances that are terminated are not compensated.
 
 The process instance must be in the running, suspended, or failing execution state.
 Only an administrator of the process instance can terminate the process instance.
 
 The process instance is put into the terminated execution state.
 
 If the "auto delete" option is not set or set to 'true',
 the process instance is automatically deleted.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance to be terminated.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- forceTerminate
void forceTerminate(java.lang.String identifier,
                  int invokeCompensation)
                    throws ArchiveUnsupportedOperationException,
                           EngineNotAuthorizedException,
                           EngineWrongKindException,
                           EngineWrongStateException,
                           IdWrongTypeException,
                           InvalidParameterValueException,
                           ObjectDoesNotExistException,
                           UnexpectedFailureException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
Terminates the specified top-level process instance, its non-autonomous subprocesses,
 its running, claimed, or waiting activities
 using a string representation of the process instance ID or the process instance name.
 For example, you can use
 these capabilities to remove failed process instances that are still in a
 running state. This example might result from an invoked application that
 failed and that did not return to a dormant state.
 
 Use the process termination capabilities as a last resort only.
 The process instance is immediately terminated without waiting for outstanding activities to complete.
 
 Depending on the invokeCompensation indicator, the process instance is compensated or not.
 If compensation is to be ignored, the process instance is immediately terminated.
 If compensation is to be invoked, the process instance is
 compensated before it is terminated provided that compensation is defined at all. Otherwise,
 the process instance is terminated without compensation.
 
 The process instance must be in the running, suspended, or failing execution state.
 Only an administrator of the process instance can terminate the process instance.
 
 The process instance is put into the terminated execution state.
 
 If the "auto delete" option is not set or set to 'true',
 the process instance is automatically deleted.
 
 This method is not supported in archive mode.
Parameters:identifier - The string representation of the process instance object ID or the name of the
    process instance. This is used to identify the process instance that is to be terminated.invokeCompensation - An indicator whether compensation is to be executed or not - refer to
    CompensationBehaviour for valid values. If
    compensation is to be ignored, compensation is not invoked even if defined. If
    compensation is to be invoked, compensation is executed if defined.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongTypeException
InvalidParameterValueException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- forceTerminate
void forceTerminate(PIID piid,
                  int invokeCompensation)
                    throws ArchiveUnsupportedOperationException,
                           EngineNotAuthorizedException,
                           EngineWrongKindException,
                           EngineWrongStateException,
                           IdWrongFormatException,
                           InvalidParameterValueException,
                           ObjectDoesNotExistException,
                           UnexpectedFailureException,
                           java.rmi.RemoteException,
                           javax.ejb.EJBException
Terminates the specified top-level process instance, its non-autonomous subprocesses,
 its running, claimed, or waiting activities
 using the process instance ID.
 For example, you can use
 these capabilities to remove failed process instances that are still in a
 running state. This example might result from an invoked application that
 failed and that did not return to a dormant state.
 
 Use the process termination capabilities as a last resort only.
 The process instance is immediately terminated without waiting for outstanding activities to complete.
 Process instances that are terminated are not compensated.
 
 Depending on the invokeCompensation flag, the process instance is compensated or not.
 If compensation is to be ignored, the process instance is immediately terminated.
 If compensation is to be invoked, the process instance is
 compensated before it is terminated provided that compensation is defined at all. Otherwise,
 the process instance is terminated without compensation.
 
 The process instance must be in the running, suspended, or failing execution state.
 Only an administrator of the process instance can terminate the process instance.
 
 The process instance is put into the terminated execution state.
 
 If the "auto delete" option is not set or set to 'true',
 the process instance is automatically deleted.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance to be terminated.invokeCompensation - An indicator whether compensation is to be executed or not - refer to
    CompensationBehaviour for valid values. If
    compensation is to be ignored, compensation is not invoked even if defined. If
    compensation is to be invoked, compensation is executed if defined.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
InvalidParameterValueException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- getActiveEventHandlers
EventHandlerTemplateData[] getActiveEventHandlers(java.lang.String piid)
                                                  throws EngineNotAuthorizedException,
                                                         IdWrongFormatException,
                                                         IdWrongTypeException,
                                                         ObjectDoesNotExistException,
                                                         UnexpectedFailureException,
                                                         java.rmi.RemoteException,
                                                         javax.ejb.EJBException
Retrieves the active event handlers of the specified
 process instance using a string representation of the process instance object ID.
 
 The caller must have at least reader authority for the process instance
 or be the process starter.
Parameters:piid - A string representation of the object ID of the process instance.
 

Returns:EventHandlerTemplateData[] -
    An array of qualifying event handler templates. If no templates qualify, an empty
    array is returned.
    Refer to EventHandlerTemplateData
    to view the event handler template properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getActiveEventHandlers
EventHandlerTemplateData[] getActiveEventHandlers(PIID piid)
                                                  throws EngineNotAuthorizedException,
                                                         IdWrongFormatException,
                                                         ObjectDoesNotExistException,
                                                         UnexpectedFailureException,
                                                         java.rmi.RemoteException,
                                                         javax.ejb.EJBException
Retrieves the active event handlers of the specified
 process instance using the process instance ID.
 
 The caller must have at least reader authority for the process instance
 or be the process starter.
Parameters:piid - The object ID of the process instance.
 
Returns:EventHandlerTemplateData[] -
    An array of qualifying event handler templates. If no templates qualify, an empty
    array is returned.
    Refer to EventHandlerTemplateData
    to view the event handler template properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getActivityInstance
ActivityInstanceData getActivityInstance(java.lang.String aiid)
                                         throws EngineNotAuthorizedException,
                                                EngineWrongKindException,
                                                EngineWrongStateException,
                                                IdWrongFormatException,
                                                IdWrongTypeException,
                                                InvalidLengthException,
                                                ObjectDoesNotExistException,
                                                UnexpectedFailureException,
                                                java.rmi.RemoteException,
                                                javax.ejb.EJBException
Retrieves the specified activity instance using a string representation of the activity instance ID.
 
 The activity instance and the associated process instance can be in any execution state.
 The caller must have at least reader authority for the activity instance,
 for the associated process instance,
 or for a scope that contains the activity instance.
Parameters:aiid - A string representation of the activity instance object ID. This is used
    to identify the activity instance to be retrieved.
 

Returns:ActivityInstanceData -
    The activity instance.
    Refer to ActivityInstanceData to view the activity instance properties.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getActivityInstance
ActivityInstanceData getActivityInstance(AIID aiid)
                                         throws EngineNotAuthorizedException,
                                                IdWrongFormatException,
                                                InvalidLengthException,
                                                ObjectDoesNotExistException,
                                                UnexpectedFailureException,
                                                java.rmi.RemoteException,
                                                javax.ejb.EJBException
Retrieves the specified activity instance using the activity instance ID.
 
 The activity instance and the associated process instance can be in any execution state.
 The caller must have at least reader authority for the activity instance, for the
 associated process instance,
 or for a scope that contains the activity instance.
Parameters:aiid - The object ID of the activity instance to be retrieved.
 

Returns:ActivityInstanceData -
    The activity instance.
    Refer to ActivityInstanceData to view the activity instance properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getActivityInstance
ActivityInstanceData getActivityInstance(java.lang.String piid,
                                       java.lang.String activityTemplateName)
                                         throws ActivityNameNotUniqueException,
                                                EngineNotAuthorizedException,
                                                EngineParameterNullException,
                                                EngineWrongKindException,
                                                EngineWrongStateException,
                                                IdWrongFormatException,
                                                IdWrongTypeException,
                                                InvalidLengthException,
                                                ObjectDoesNotExistException,
                                                UnexpectedFailureException,
                                                java.rmi.RemoteException,
                                                javax.ejb.EJBException
Retrieves the specified activity instance using a string representation of the
 process instance ID and the activity template name.
 
 The activity instance and the associated process instance can be in any execution state.
 The caller must have at least reader authority for the activity instance, for the
 associated process instance,
 or for a scope that contains the activity instance.
 
 Note that an activity instance is only returned if it can be uniquely identified
 by the specified activity template name.
 That is, if the activity instance is contained within an event handler or for-each instance,
 then an ObjectDoesNotExistException is thrown although an activity with the specified name
 could be found. There may be multiple activity instances with the specified name because
 there may be multiple event handler or for-each instances.
Parameters:piid - A string representation of the object ID of the containing process instance.activityTemplateName - The name of the activity template that describes the activity instance
    to be retrieved.
 

Returns:ActivityInstanceData -
    The activity instance retrieved.
    Refer to ActivityInstanceData to view the activity instance properties.
 
Throws:
ActivityNameNotUniqueException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getActivityInstance
ActivityInstanceData getActivityInstance(PIID piid,
                                       java.lang.String activityTemplateName)
                                         throws ActivityNameNotUniqueException,
                                                EngineNotAuthorizedException,
                                                EngineParameterNullException,
                                                EngineWrongKindException,
                                                EngineWrongStateException,
                                                IdWrongFormatException,
                                                IdWrongTypeException,
                                                InvalidLengthException,
                                                ObjectDoesNotExistException,
                                                UnexpectedFailureException,
                                                java.rmi.RemoteException,
                                                javax.ejb.EJBException
Retrieves the specified activity instance using the process instance ID
 and the activity template name.
 
 The activity instance and the associated process instance can be in any execution state.
 The caller must have at least reader authority for the activity instance, for the
 associated process instance,
 or for a scope that contains the activity instance.
 
 Note that an activity instance is only returned if it can be uniquely identified
 by the specified activity template name.
 That is, if the activity instance is contained within an event handler or for-each instance,
 then an ObjectDoesNotExistException is thrown although an activity with the specified name
 could be found. There may be multiple activity instances with the specified name because
 there may be multiple event handler or for-each instances.
Parameters:piid - The object ID of the process instance.activityTemplateName - The name of the activity template that describes the activity instance
    to be retrieved.
 

Returns:ActivityInstanceData -
    The activity instance retrieved.
    Refer to ActivityInstanceData to view the activity instance properties.
 
Throws:
ActivityNameNotUniqueException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getActivityServiceTemplate
ActivityServiceTemplateData getActivityServiceTemplate(java.lang.String vtid,
                                                     java.lang.String atid)
                                                       throws EngineNotAuthorizedException,
                                                              IdWrongFormatException,
                                                              IdWrongTypeException,
                                                              ObjectDoesNotExistException,
                                                              UnexpectedFailureException,
                                                              java.rmi.RemoteException,
                                                              javax.ejb.EJBException
Retrieves the specified activity service template
 using string representations of the associated object IDs.
 
 The caller must have at least reader authority for the associated activity or be a process administrator.
Parameters:vtid - A string representation of the activity service template ID. This is used
    to identify the service to be retrieved.atid - A string representation of the activity template ID. This is used
    to identify the activity the service belongs to.
 

Returns:ActivityServiceTemplateData -
    The activity service template information.
    Refer to ActivityServiceTemplateData to view the properties
    of an activity service template.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1

- getActivityServiceTemplate
ActivityServiceTemplateData getActivityServiceTemplate(VTID vtid,
                                                     ATID atid)
                                                       throws EngineNotAuthorizedException,
                                                              IdWrongFormatException,
                                                              ObjectDoesNotExistException,
                                                              UnexpectedFailureException,
                                                              java.rmi.RemoteException,
                                                              javax.ejb.EJBException
Retrieves the specified activity service template using the associated object IDs.
 
 The caller must have at least reader authority for the associated activity or be a process administrator.
Parameters:vtid - The object ID of the activity service template to be retrieved.atid - The object ID of the activity the activity service template belongs to.
 

Returns:ActivityServiceTemplateData -
    The activity service template information.
    Refer to ActivityServiceTemplateData to view the properties
    of an activity service template.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1

- getAllActivities QueryResultSet getAllActivities(java.lang.String piid, java.util.TimeZone timezone) throws EngineNotAuthorizedException , IdWrongFormatException , IdWrongTypeException , ObjectDoesNotExistException , UnexpectedFailureException , WorkItemManagerException , java.rmi.RemoteException, javax.ejb.EJBException Queries pre-defined activity instance properties of activities directly contained in the specified process instance using a string representation of the process instance ID. Following properties of an activity instance (columns of the query result set) are returned in the stated sequence: Note that only business-relevant activities are returned. Starting with 6.1.2, structural activities like "sequence" are also returned. The process instance can be in any execution state. The caller must have reader authority for the process instance, be the process administrator, or be the business process administrator or monitor. Parameters: piid - A string representation of the object ID of the process instance. timezone - The timezone of all timestamp properties returned. If a timezone is not specified, timestamps are returned in UTC. Returns: QueryResultSet - An object containing the query result. If qualifying tuples are not found, an empty query result set is returned. Refer to QueryResultSet for information on how to analyze the query result set. Throws: EngineNotAuthorizedException IdWrongFormatException IdWrongTypeException ObjectDoesNotExistException UnexpectedFailureException WorkItemManagerException java.rmi.RemoteException javax.ejb.EJBException Since: 5.0 Change History Release Modification 6.0.2 Removed Version 5 EngineCannotInitializePluginException. 6.1.2 Structural activities like "sequence" are returned.

#### getAllActivities

```
QueryResultSet getAllActivities(java.lang.String piid,
                              java.util.TimeZone timezone)
                                throws EngineNotAuthorizedException,
                                       IdWrongFormatException,
                                       IdWrongTypeException,
                                       ObjectDoesNotExistException,
                                       UnexpectedFailureException,
                                       WorkItemManagerException,
                                       java.rmi.RemoteException,
                                       javax.ejb.EJBException
```

    1. ID
    Name
    Execution state
    Kind
    Activation time
    ID of the associated activitiy template

Note that only business-relevant activities are returned.
 Starting with 6.1.2, structural activities like "sequence" are also returned.
 
 The process instance can be in any execution state.
 The caller must have reader authority for the process instance, be the process
 administrator, or be the business process administrator or monitor.

Change History

Release
 Modification
 
6.0.2
 
 Removed Version 5 EngineCannotInitializePluginException.
 
6.1.2
 
 Structural activities like "sequence" are returned.

- getAllActivities QueryResultSet getAllActivities(PIID piid, java.util.TimeZone timezone) throws EngineNotAuthorizedException , IdWrongFormatException , ObjectDoesNotExistException , UnexpectedFailureException , WorkItemManagerException , java.rmi.RemoteException, javax.ejb.EJBException Queries pre-defined activity instance properties of activities directly contained in the specified process instance using the process instance ID. Following properties of an activity instance (columns of the query result set) are returned in the stated sequence: Note that only business-relevant activities are returned. Starting with 6.1.2, structural activities like "sequence" are also returned. The process instance can be in any execution state. The caller must have reader authority for the process instance, be the process administrator, or be the business process administrator or monitor. Parameters: piid - The object ID of the process instance. timezone - The timezone of all timestamp properties returned. If a timezone is not specified, timestamps are returned in UTC. Returns: QueryResultSet - An object containing the query result. If qualifying tuples are not found, an empty query result set is returned. Refer to QueryResultSet for information on how to analyze the query result set. Throws: EngineNotAuthorizedException IdWrongFormatException ObjectDoesNotExistException UnexpectedFailureException WorkItemManagerException java.rmi.RemoteException javax.ejb.EJBException Since: 5.0 Change History Release Modification 6.0.2 Removed Version 5 EngineCannotInitializePluginException. 6.1.2 Structural activities like "sequence" are returned.

#### getAllActivities

```
QueryResultSet getAllActivities(PIID piid,
                              java.util.TimeZone timezone)
                                throws EngineNotAuthorizedException,
                                       IdWrongFormatException,
                                       ObjectDoesNotExistException,
                                       UnexpectedFailureException,
                                       WorkItemManagerException,
                                       java.rmi.RemoteException,
                                       javax.ejb.EJBException
```

    1. ID
    Name
    Execution state
    Kind
    Activation time
    ID of the associated activitiy template

Note that only business-relevant activities are returned.
 Starting with 6.1.2, structural activities like "sequence" are also returned.
 
 The process instance can be in any execution state.
 The caller must have reader authority for the process instance, be the process
 administrator, or be the business process administrator or monitor.

Change History

Release
 Modification
 
6.0.2
 
 Removed Version 5 EngineCannotInitializePluginException.
 
6.1.2
 
 Structural activities like "sequence" are returned.

- getAllBasicActivityNames
java.util.List getAllBasicActivityNames(java.lang.String piid)
                                        throws IdWrongFormatException,
                                               IdWrongTypeException,
                                               ObjectDoesNotExistException,
                                               UnexpectedFailureException,
                                               java.rmi.RemoteException,
                                               javax.ejb.EJBException
Retrieves the names of all basic activities that are part of the specified process instance
 using a string representation of the process instance ID.
 
 Only names of basic activities are returned that you are authorized to see.
 That is, all basic activity names are returned if you have at least
 reader authority for the process instance. Otherwise, only the names of basic
 activities are returned that are part of a scope for which you have at least
 reader authority.
Parameters:piid - A string representation of the process instance object ID. This is used
    to identify the process instance.
 
Returns:List -
    A list of basic activity names. If there are no basic activities that have a name,
    or if you are not authorized to see basic activities that have a name,
    an empty list is returned.
 
Throws:
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getAllBasicActivityNames
java.util.List getAllBasicActivityNames(PIID piid)
                                        throws IdWrongFormatException,
                                               ObjectDoesNotExistException,
                                               UnexpectedFailureException,
                                               java.rmi.RemoteException,
                                               javax.ejb.EJBException
Retrieves the names of all basic activities that are part of the specified process instance
 using the process instance ID.
 
 Only names of basic activities are returned that you are authorized to see.
 That is, all basic activity names are returned if you have at least
 reader authority for the process instance. Otherwise, only the names of basic
 activities are returned that are part of a scope for which you have at least
 reader authority.
Parameters:piid - The process instance object ID. This is used
    to identify the process instance.
 
Returns:List -
    A list of basic activity names. If there are no basic activities that have a name,
    or if you are not authorized to see basic activities that have a name,
    an empty list is returned.
 
Throws:
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getAllCustomProperties
java.util.List getAllCustomProperties(java.lang.String identifier)
                                      throws EngineNotAuthorizedException,
                                             IdWrongFormatException,
                                             IdWrongTypeException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves all custom properties of the specified process template or process instance
 using a string representation of the object ID.
 
 Custom properties allow a user to add additional properties to processes and activities,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the object. Thus, using inline custom properties
 can increase performance.
 
 This method returns the custom properties that are attached to the object as well as
 the inline custom properties.
 
 Custom properties can be retrieved in any execution state of the process instance.
 The caller must have at least reader authority for the process instance.
Parameters:identifier - A string representation of the process template or process instance object ID. This
    string is used to identify the object for which the custom properties are to be retrieved.
 
Returns:List -
    A list of CustomProperty or
    InlineCustomProperty objects.
    The list is empty if there are no custom properties attached to the specified object
    and if the inline custom properties are not set (null or empty string).
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- getAllCustomProperties
java.util.List getAllCustomProperties(PTID ptid)
                                      throws EngineNotAuthorizedException,
                                             IdWrongFormatException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves all custom properties of the specified process template using the process template ID.
 
 Custom properties allow a user to add additional properties to a process,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment.
 
 In contrast to custom properties that are attached to a process template, inline custom properties
 are an integral part of the process template. Thus, using inline custom properties
 can increase performance.
 
 This method returns the custom properties that are attached to the process template as well as
 the inline custom properties.
 
 The caller must be authorized for the process template.
Parameters:ptid - The process template object ID whose custom properties are to be retrieved.
 
Returns:List -
    A list of CustomProperty or
    InlineCustomProperty objects.
    The list is empty if there are no custom properties attached to the specified object
    and if the inline custom properties are not set (null or empty string).
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- getAllCustomProperties
java.util.List getAllCustomProperties(PIID piid)
                                      throws EngineNotAuthorizedException,
                                             IdWrongFormatException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves all custom properties of the specified process instance using the process instance ID.
 
 Custom properties allow a user to add additional properties to a process,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances.
 
 In contrast to custom properties that are attached to a process instance, inline custom properties
 are an integral part of the process instance. Thus, using inline custom properties
 can increase performance.
 
 This method returns the custom properties that are attached to the process instance as well as
 the inline custom properties.
 
 Custom properties can be retrieved in any execution state of the process instance.
 The caller must have at least reader authority for the process instance
 or be the process starter.
Parameters:piid - The process instance object ID whose custom properties are to be retrieved.
 
Returns:List -
    A list of CustomProperty or
    InlineCustomProperty objects.
    The list is empty if there are no custom properties attached to the specified object
    and if the inline custom properties are not set (null or empty string).
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- getAllQueryProperties
java.util.List getAllQueryProperties(java.lang.String propertyNameFilter,
                                   java.lang.Integer threshold)
                                     throws WorkItemManagerException,
                                            UnexpectedFailureException,
                                            java.rmi.RemoteException,
                                            javax.ejb.EJBException
Retrieves the query properties of all process templates.
 
 Query properties in the BPEL process definition are used to declare
 which parts of a variable should be accessible with the query API function.
 
 Optionally, you can specify a threshold or a filter to reduce
 the number of query properties returned.
Parameters:propertyNameFilter - A filter to restrict the query properties to be returned. A SQL LIKE
  predicate is used for the name filter provided.threshold - Specifies the maximum number of query properties to be returned from the
    server to the client. If a threshold is not to be applied, null must be specified.
 
Returns:List -
    A list of query properties and information about the associated process template -
  refer to QueryPropertyExtension.
 
Throws:
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2

- getAllVariableNames
java.util.List getAllVariableNames(java.lang.String piid,
                                 java.lang.String activityName)
                                   throws EngineAmbiguousActivityException,
                                          EngineNotAuthorizedException,
                                          EngineParameterNullException,
                                          EngineUnknownActivityException,
                                          EngineWrongKindException,
                                          IdWrongFormatException,
                                          IdWrongTypeException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the names of all variables visible by the specified activity
 using a string representation of the process instance ID and the activity name.
 
 The activity need not be navigated.
 The caller must have at least reader authority for the
 process instance or for a scope that contains the activity provided that
 the scope is already navigated.
Parameters:piid - A string representation of the process instance object ID. This is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.
 
Returns:List -
    A list of variable names. If there are no variables, an empty list is returned.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
7.0
 Throws an
 EngineWrongKindException when an activity is specified that is for internal use only.

- getAllVariableNames
java.util.List getAllVariableNames(PIID piid,
                                 java.lang.String activityName)
                                   throws EngineAmbiguousActivityException,
                                          EngineNotAuthorizedException,
                                          EngineParameterNullException,
                                          EngineUnknownActivityException,
                                          EngineWrongKindException,
                                          IdWrongFormatException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the names of all variables visible by the specified activity
 using the process instance ID and the activity name.
 
 The activity need not be navigated.
 The caller must have at least reader authority for the
 process instance or for a scope that contains the activity provided that
 the scope is already navigated.
Parameters:piid - A string representation of the process instance object ID. This is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.
 
Returns:List -
    A list of variable names. If there are no variables, an empty list is returned.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
7.0
 Throws an
 EngineWrongKindException when an activity is specified that is for internal use only.

- getAllVariableNames
java.util.List getAllVariableNames(java.lang.String identifier)
                                   throws EngineNotAuthorizedException,
                                          EngineWrongKindException,
                                          IdWrongFormatException,
                                          IdWrongTypeException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the names of all variables visible by the specified process or
 activity instance using a string representation of the process or
 activity instance ID.
 
 The variable names can be retrieved in any execution state of the process or activity instance.
 
 The caller must have at least reader authority for the process instance or for a scope
 that contains the activity instance.
Parameters:identifier - A string representation of the process or activity instance object ID.
 
Returns:List -
    A list of variable names. If there are no variables, an empty list is returned.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
7.0
 Throws an
 EngineWrongKindException when an activity is specified that is for internal use only.

- getAllVariableNames
java.util.List getAllVariableNames(PIID piid)
                                   throws EngineNotAuthorizedException,
                                          IdWrongFormatException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the names of all variables visible by the specified process instance
 using the process instance ID.
 
 The variable names can be retrieved in any execution state of the process instance.
 
 The caller must have at least reader authority for the process instance.
Parameters:piid - The object ID of the process instance whose variable names are to be retrieved.
 
Returns:List -
    A list of variable names. If there are no variables, an empty list is returned.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2

- getAllVariableNames
java.util.List getAllVariableNames(AIID aiid)
                                   throws EngineNotAuthorizedException,
                                          EngineWrongKindException,
                                          IdWrongFormatException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the names of all variables visible by the specified activity instance
 using the activity instance ID.
 
 The variable names can be retrieved in any execution state of the activity instance.
 
 The caller must have at least reader authority for the associated process instance
 or for a scope that contains the activity instance.
Parameters:aiid - The object ID of the activity instance whose variable names are to be retrieved.
 
Returns:List -
    A list of variable names. If there are no variables, an empty list is returned.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
7.0
 Throws an
 EngineWrongKindException when an activity is specified that is for internal use only.

- getAllWorkItems
WorkItemData[] getAllWorkItems(java.lang.String identifier)
                               throws EngineNotAuthorizedException,
                                      IdWrongFormatException,
                                      IdWrongTypeException,
                                      ObjectDoesNotExistException,
                                      UserRegistryException,
                                      WorkItemManagerException,
                                      UnexpectedFailureException,
                                      java.rmi.RemoteException,
                                      javax.ejb.EJBException
Retrieves all work item assignments associated to the specified process or activity instance
 using a string representation of the process or activity instance ID.
 
 The activity or process instance can be in any execution state but terminated.
 
 The caller must have reader authority for the process instance, be the process
 administrator, have a work item for the activity instance, or
 be an administrator of a scope that contains the activity instance,
 if an activity instance is specified,
 or be a business process administrator or monitor.
Parameters:identifier - A string representation of the process or activity instance object ID. The string is used
    to identify the process instance or activity instance.
 

Returns:WorkItemData[] -
    An array of work items. If there are no work items, an empty
    array is returned.
    Refer to WorkItemData to view the work item properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UserRegistryException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.

- getAllWorkItems
WorkItemData[] getAllWorkItems(PIID piid)
                               throws EngineNotAuthorizedException,
                                      IdWrongFormatException,
                                      ObjectDoesNotExistException,
                                      UserRegistryException,
                                      WorkItemManagerException,
                                      UnexpectedFailureException,
                                      java.rmi.RemoteException,
                                      javax.ejb.EJBException
Retrieves all work item assignments associated to the specified process instance
 using the process instance ID.
 
 The process instance can be in any execution state.
 
 The caller must have reader authority for the process instance, be the process
 administrator, or be the business process administrator or monitor.
Parameters:piid - The object ID of the process instance.
 

Returns:WorkItemData[] -
    An array of work items. If there are no work items, an empty
    array is returned.
    Refer to WorkItemData to view the work item properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UserRegistryException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.0.2
 
 Removed Version 5 EngineCannotInitializePluginException.
 
6.1
 
 A business process monitor may retrieve all work items.

- getAllWorkItems
WorkItemData[] getAllWorkItems(AIID aiid)
                               throws EngineNotAuthorizedException,
                                      IdWrongFormatException,
                                      ObjectDoesNotExistException,
                                      UserRegistryException,
                                      WorkItemManagerException,
                                      UnexpectedFailureException,
                                      java.rmi.RemoteException,
                                      javax.ejb.EJBException
Retrieves all work item assignments associated to the specified activity instance
 using the activity instance ID.
 
 The activity instance and the associated process instance can be in any execution state but terminated.
 
 The caller must have reader authority for the process instance, be the process
 administrator, have a work item for the activity instance,
 be an administrator of a scope that contains the activity instance,
 or be a business process administrator or monitor.
Parameters:aiid - The object ID of the activity instance.
 

Returns:WorkItemData[] -
    An array of work items. If there are no work items, an empty
    array is returned.
    Refer to WorkItemData to view the work item properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UserRegistryException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.

- getAvailableActionFlags
boolean[][] getAvailableActionFlags(java.lang.String[] identifiers)
                                    throws IdWrongFormatException,
                                           IdWrongTypeException,
                                           EngineNotAuthorizedException,
                                           ObjectDoesNotExistException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Returns indicators to state the actions that can be called in the current process
 instance states or in the current activity instance states by the logged-on user.
 Refer to ProcessInstanceActions
 or to ActivityInstanceActions
 for the set of possible actions.
Parameters:identifiers - An array of string representation of object IDs. These objects IDs
 must either all represent process instance IDs or activity instance IDs.
 
Returns:boolean[][] -
    An array of actions that can be called for each specified process or activity instance.
 The array returns a row per process or activity instance. The columns indicate whether a possible action
 can be called for the process or activity instance. True states that the action can be called. False states
 that the action cannot be called by the logged-on user in the current process or activity instance state.
 Refer to ProcessInstanceActionIndex for index constants that can
 be used to access the columns of the two-dimensional array for process instances.
 Refer to ActivityInstanceActionIndex for index constants that can
 be used to access the columns of the two-dimensional array for activity instances.
 
Throws:
IdWrongFormatException
IdWrongTypeException
EngineNotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getAvailableActionFlags
boolean[][] getAvailableActionFlags(PIID[] piids)
                                    throws EngineNotAuthorizedException,
                                           IdWrongFormatException,
                                           ObjectDoesNotExistException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Returns indicators to state the actions that can be called in the current process
 instance states by the logged-on user using process instance IDs.
 Refer to ProcessInstanceActions for the set of possible actions.
Parameters:piids - An array of process instance IDs.
 
Returns:boolean[][] -
    An array of actions that can be called for each specified process instance.
 The array returns a row per process instance. The columns indicate whether a possible action
 can be called for the process instance. True states that the action can be called. False states
 that the action cannot be called by the logged-on user in the current process instance state.
 Refer to ProcessInstanceActionIndex for index constants that can
 be used to access the columns of the two-dimensional array.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getAvailableActionFlags
boolean[][] getAvailableActionFlags(AIID[] aiids)
                                    throws EngineNotAuthorizedException,
                                           IdWrongFormatException,
                                           ObjectDoesNotExistException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Returns indicators to state the actions that can be called in the current activity
 instance states by the logged-on user using activity instance IDs.
 Refer to ActivityInstanceActions for the set of possible actions.
Parameters:aiids - An array of activity instance IDs.
 
Returns:boolean[][] -
    An array of actions that can be called for each specified activity instance.
 The array returns a row per activity instance. The columns indicate whether a possible action
 can be called for the activity instance. True states that the action can be called. False states
 that the action cannot be called by the logged-on user in the current activity instance state.
 Refer to ActivityInstanceActionIndex for index constants that can
 be used to access the columns of the two-dimensional array.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getBfmConfiguration
BfmConfiguration getBfmConfiguration()
                                     throws java.rmi.RemoteException,
                                            javax.ejb.EJBException
Returns configuration settings of the Business Flow Manager.
 
Returns:BfmConfiguration -
    Business Flow Manager configuration settings.
    Refer to BfmConfiguration to view the Business Flow Manager
    configuration settings returned.
 
Throws:
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5

- getBinaryCustomProperty
BinaryCustomProperty getBinaryCustomProperty(java.lang.String identifier,
                                           java.lang.String propertyName)
                                             throws EngineNotAuthorizedException,
                                                    EngineParameterNullException,
                                                    EngineWrongKindException,
                                                    IdWrongFormatException,
                                                    IdWrongTypeException,
                                                    ObjectDoesNotExistException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Retrieves the named binary custom property of the specified
 process or activity instance using a string representation of the object ID.
 
 Custom properties allow a user to add additional properties to processes or activities
 beyond those provided and managed by ProcessChoreographer. Binary custom properties allow,
 for example, to attach a Java object to an activity instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 A binary custom property can be retrieved in any state of the process or activity instance.
 An activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the process instance ,
 for the activity instance or for a scope that contains the activity instance.
Parameters:identifier - A string representation of the process or activity instance ID. This
    string is used to identify the process or activity instance for which the binary
    custom property is to be retrieved.propertyName - The name of the binary custom property to be retrieved.
 
Returns:BinaryCustomProperty -
    The BinaryCustomProperty object.
    Returns null when the named binary custom property cannot be found.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getBinaryCustomProperty
BinaryCustomProperty getBinaryCustomProperty(PIID piid,
                                           java.lang.String propertyName)
                                             throws EngineNotAuthorizedException,
                                                    EngineParameterNullException,
                                                    IdWrongFormatException,
                                                    ObjectDoesNotExistException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Retrieves the named binary custom property of the specified
 process instance using the process instance the object ID.
 
 Custom properties allow a user to add additional properties to processes
 beyond those provided and managed by ProcessChoreographer. Binary custom properties allow,
 for example, to attach a Java object to a process instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 A binary custom property can be retrieved in any state of the process instance.
 The caller must have at least reader authority for the process instance.
Parameters:piid - The process instance ID. This ID
    is used to identify the process instance for which the binary
    custom property is to be retrieved.propertyName - The name of the binary custom property to be retrieved.
 
Returns:BinaryCustomProperty -
    The BinaryCustomProperty object.
    Returns null when the named binary custom property cannot be found.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getBinaryCustomProperty
BinaryCustomProperty getBinaryCustomProperty(AIID aiid,
                                           java.lang.String propertyName)
                                             throws EngineNotAuthorizedException,
                                                    EngineParameterNullException,
                                                    EngineWrongKindException,
                                                    IdWrongFormatException,
                                                    ObjectDoesNotExistException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Retrieves the named binary custom property of the specified
 activity instance using the activity instance object ID.
 
 Custom properties allow a user to add additional properties to activities
 beyond those provided and managed by ProcessChoreographer. Binary custom properties allow,
 for example, to attach a Java object to an activity instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 A binary custom property can be retrieved in any state of the activity instance.
 The activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the process instance,
 for the activity instance, or for a scope that contains the activity instance.
Parameters:aiid - The activity instance ID. This ID
    is used to identify the activity instance for which the binary
    custom property is to be retrieved.propertyName - The name of the binary custom property to be retrieved.
 
Returns:BinaryCustomProperty -
    The BinaryCustomProperty object.
    Returns null when the named binary custom property cannot be found.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getBinaryCustomProperty
BinaryCustomProperty getBinaryCustomProperty(java.lang.String piid,
                                           java.lang.String activityName,
                                           java.lang.String propertyName)
                                             throws EngineAmbiguousActivityException,
                                                    EngineNotAuthorizedException,
                                                    EngineParameterNullException,
                                                    EngineUnknownActivityException,
                                                    EngineWrongKindException,
                                                    IdWrongFormatException,
                                                    IdWrongTypeException,
                                                    ObjectDoesNotExistException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Retrieves the named binary custom property of the specified activity instance
 using a string representation of the process instance ID and the activity name.
 
 Custom properties allow a user to add additional properties to activities
 beyond those provided and managed by ProcessChoreographer. Binary custom properties allow,
 for example, to attach a Java object to an activity instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 A binary custom property can be retrieved in any state of the activity instance.
 The activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the process instance, for
 the activity instance, or for a scope that contains the activity instance.
Parameters:piid - A string representation of the process instance object ID. This is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.propertyName - The name of the binary custom property to be retrieved.
 
Returns:BinaryCustomProperty -
    The BinaryCustomProperty object.
    Returns null when the named binary custom property cannot be found.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getBinaryCustomProperty
BinaryCustomProperty getBinaryCustomProperty(PIID piid,
                                           java.lang.String activityName,
                                           java.lang.String propertyName)
                                             throws EngineAmbiguousActivityException,
                                                    EngineNotAuthorizedException,
                                                    EngineParameterNullException,
                                                    EngineUnknownActivityException,
                                                    EngineWrongKindException,
                                                    IdWrongFormatException,
                                                    ObjectDoesNotExistException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Retrieves the named binary custom property of the specified activity instance
 using the process instance ID and the activity name.
 
 Custom properties allow a user to add additional properties to activities
 beyond those provided and managed by ProcessChoreographer. Binary custom properties allow,
 for example, to attach a Java object to an activity instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 A binary custom property can be retrieved in any state of the activity instance.
 The activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the process instance, for
 the activity instance, or for a scope that contains the activity instance.
Parameters:piid - The object ID of the process instance that is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.propertyName - The name of the binary custom property to be retrieved.
 
Returns:BinaryCustomProperty -
    The BinaryCustomProperty object.
    Returns null when the named binary custom property cannot be found.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getBinaryCustomPropertyNames
java.util.List getBinaryCustomPropertyNames(java.lang.String identifier)
                                            throws EngineNotAuthorizedException,
                                                   EngineWrongKindException,
                                                   IdWrongFormatException,
                                                   IdWrongTypeException,
                                                   ObjectDoesNotExistException,
                                                   UnexpectedFailureException,
                                                   java.rmi.RemoteException,
                                                   javax.ejb.EJBException
Retrieves the names of all binary custom properties of the specified
 process or activity instance using a string representation of the process or activity instance ID.
 
 Custom properties allow a user to add additional properties to processes or activities
 beyond those provided and managed by ProcessChoreographer. Binary custom properties allow,
 for example, to attach a Java object to an activity instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 Binary custom properties names can be retrieved in any state of the process or activity instance.
 The activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the process instance, for
 the activity instance, or for a scope that contains the activity instance.
Parameters:identifier - A string representation of the process or activity instance ID. This
    string is used to identify the process or activity instance for which the binary
    custom property names are to be retrieved.
 
Returns:List -
    A list of binary custom property names.
    Returns an empty list when there are no binary custom properties.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getBinaryCustomPropertyNames
java.util.List getBinaryCustomPropertyNames(PIID piid)
                                            throws EngineNotAuthorizedException,
                                                   IdWrongFormatException,
                                                   ObjectDoesNotExistException,
                                                   UnexpectedFailureException,
                                                   java.rmi.RemoteException,
                                                   javax.ejb.EJBException
Retrieves the names of all binary custom properties of the specified
 process instance using the process instance ID.
 
 Custom properties allow a user to add additional properties to processes or activities
 beyond those provided and managed by ProcessChoreographer. Binary custom properties allow,
 for example, to attach a Java object to a process instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 Binary custom properties names can be retrieved in any state of the process instance.
 The caller must have at least reader authority for the process instance.
Parameters:piid - The process instance ID. This ID
    is used to identify the process instance for which the binary
    custom property names are to be retrieved.
 
Returns:List -
    A list of binary custom property names.
    Returns an empty list when there are no binary custom properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getBinaryCustomPropertyNames
java.util.List getBinaryCustomPropertyNames(AIID aiid)
                                            throws EngineNotAuthorizedException,
                                                   EngineWrongKindException,
                                                   IdWrongFormatException,
                                                   ObjectDoesNotExistException,
                                                   UnexpectedFailureException,
                                                   java.rmi.RemoteException,
                                                   javax.ejb.EJBException
Retrieves the names of all binary custom properties of the specified
 activity instance using the activity instance ID.
 
 Custom properties allow a user to add additional properties to processes or activities
 beyond those provided and managed by ProcessChoreographer. Binary custom properties allow,
 for example, to attach a Java object to an activity instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 Binary custom properties names can be retrieved in any state of the activity instance.
 The activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the process instance, for
 the activity instance, or for a scope that contains the activity instance.
Parameters:aiid - The activity instance ID. This ID
    is used to identify the activity instance for which the binary
    custom property names are to be retrieved.
 
Returns:List -
    A list of binary custom property names.
    Returns an empty list when there are no binary custom properties.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getBinaryCustomPropertyNames
java.util.List getBinaryCustomPropertyNames(java.lang.String piid,
                                          java.lang.String activityName)
                                            throws EngineAmbiguousActivityException,
                                                   EngineNotAuthorizedException,
                                                   EngineParameterNullException,
                                                   EngineUnknownActivityException,
                                                   EngineWrongKindException,
                                                   IdWrongFormatException,
                                                   IdWrongTypeException,
                                                   ObjectDoesNotExistException,
                                                   UnexpectedFailureException,
                                                   java.rmi.RemoteException,
                                                   javax.ejb.EJBException
Retrieves the names of all binary custom property of the specified activity instance
 using a string representation of the process instance ID and the activity name.
 
 Custom properties allow a user to add additional properties to activities
 beyond those provided and managed by ProcessChoreographer. Binary custom properties allow,
 for example, to attach a Java object to an activity instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 Binary custom properties names can be retrieved in any state of the process or activity instance.
 The activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the process instance, for
 the activity instance, or for a scope that contains the activity instance.
Parameters:piid - A string representation of the process instance object ID. This is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.
 
Returns:List -
    A list of binary custom property names.
    Returns an empty list when there are no binary custom properties.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getBinaryCustomPropertyNames
java.util.List getBinaryCustomPropertyNames(PIID piid,
                                          java.lang.String activityName)
                                            throws EngineAmbiguousActivityException,
                                                   EngineNotAuthorizedException,
                                                   EngineParameterNullException,
                                                   EngineUnknownActivityException,
                                                   EngineWrongKindException,
                                                   IdWrongFormatException,
                                                   ObjectDoesNotExistException,
                                                   UnexpectedFailureException,
                                                   java.rmi.RemoteException,
                                                   javax.ejb.EJBException
Retrieves the names of all binary custom property of the specified activity instance
 using the process instance ID and the activity name.
 
 Custom properties allow a user to add additional properties to activities
 beyond those provided and managed by ProcessChoreographer. Binary custom properties allow,
 for example, to attach a Java object to an activity instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 Binary custom properties names can be retrieved in any state of the process or activity instance.
 The activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the process instance, for
 the activity instance, or for a scope that contains the activity instance.
Parameters:piid - The object ID of the process instance that is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.
 
Returns:List -
    A list of binary custom property names.
    Returns an empty list when there are no binary custom properties.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getBranches
BranchTemplateData[] getBranches(java.lang.String aiid)
                                 throws EngineNotAuthorizedException,
                                        EngineWrongKindException,
                                        IdWrongFormatException,
                                        IdWrongTypeException,
                                        ObjectDoesNotExistException,
                                        UnexpectedFailureException,
                                        java.rmi.RemoteException,
                                        javax.ejb.EJBException
Retrieves information about the branches of the specified switch activity instance
 using a string representation of the activity instance object ID.
 
 Information about the branches can be retrieved in any execution state of the activity instance.
 The caller must have at least reader authority for the activity instance,
 for the associated process instance,
 or for a scope that contains the activity instance.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance.
 
Returns:BranchTemplateData[] -
    The branches of the switch activity. A branch
    can be selected to continue navigation of a stopped activitiy - see
    forceNavigate.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getBranches
BranchTemplateData[] getBranches(AIID aiid)
                                 throws EngineNotAuthorizedException,
                                        EngineWrongKindException,
                                        IdWrongFormatException,
                                        ObjectDoesNotExistException,
                                        UnexpectedFailureException,
                                        java.rmi.RemoteException,
                                        javax.ejb.EJBException
Retrieves information about the branches of the specified switch activity instance
 using the activity instance ID.
 
 Information about the branches can be retrieved in any execution state of the activity instance.
 The caller must have at least reader authority for the activity instance,
 for the associated process instance,
 or for a scope that contains the activity instance.
Parameters:aiid - The object ID of the activity instance.
 
Returns:BranchTemplateData[] -
    The branches of the switch activity. A branch
    can be selected to continue navigation of a stopped activitiy - see
    forceNavigate.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getClientUISettings
CustomClientSettings getClientUISettings(java.lang.String identifier)
                                         throws EngineNotAuthorizedException,
                                                EngineWrongKindException,
                                                IdWrongFormatException,
                                                IdWrongTypeException,
                                                ObjectDoesNotExistException,
                                                ServiceNotUniqueException,
                                                UnexpectedFailureException,
                                                java.rmi.RemoteException,
                                                javax.ejb.EJBException
Retrieves client interface settings for the specified process template,
 process instance, or activity instance using a string representation of the object ID.
 
 Client interface settings allow for the specification of presentations that can
 be used by the caller to present objects and data to an end user.
 It is not only possible to display data handled by activities in a specific way but
 also to specify JSPs that display the properties of process instances and their templates specifically.
 
 Client interface settings can always be retrieved.
 When they are to be retrieved for a process or activity instance,
 the caller must have at least reader authority for the process or activity instance,
 be the starter of the process instance,
 or have reader authority for a scope that contains the activity instance.
Parameters:identifier - A string representation of either a process template, a process instance, or an activity instance object ID.
 
Returns:CustomClientSettings -
    The customized client interface settings.
    Returns null if there are no customized client interface settings.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
ServiceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getClientUISettings
CustomClientSettings getClientUISettings(PTID ptid)
                                         throws EngineNotAuthorizedException,
                                                EngineWrongKindException,
                                                IdWrongFormatException,
                                                ObjectDoesNotExistException,
                                                UnexpectedFailureException,
                                                java.rmi.RemoteException,
                                                javax.ejb.EJBException
Retrieves client interface settings for the specified process template using the process template ID.
 
 Client interface settings allow for the specification of presentations that can
 be used by the caller to present objects and data to an end user.
 It is not only possible to display data handled by activities in a specific way but
 also to specify JSPs that display the properties of process instances and their templates specifically.
 
 The caller must be authorized for the process template.
 
Parameters:ptid - The object ID of the process template.
 

Returns:CustomClientSettings -
    The customized client interface settings.
    Returns null if there are no customized client interface settings.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1

- getClientUISettings
CustomClientSettings getClientUISettings(PIID piid)
                                         throws EngineNotAuthorizedException,
                                                EngineWrongKindException,
                                                IdWrongFormatException,
                                                ObjectDoesNotExistException,
                                                UnexpectedFailureException,
                                                java.rmi.RemoteException,
                                                javax.ejb.EJBException
Retrieves client interface settings for the specified process instance using the process instance ID.
 
 Client interface settings allow for the specification of presentations that can
 be used by the caller to present objects and data to an end user.
 It is not only possible to display data handled by activities in a specific way but
 also to specify JSPs that display the properties of process instances and their templates specifically.
 
 Client interface settings can be retrieved in any execution state of the process instance.
 The caller must have at least reader authority for the process instance
 or be the starter of the process instance.
Parameters:piid - The object ID of the process instance.
 

Returns:CustomClientSettings -
    The customized client interface settings.
    Returns null if there are no customized client interface settings.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1

- getClientUISettings
CustomClientSettings getClientUISettings(AIID aiid)
                                         throws EngineNotAuthorizedException,
                                                EngineWrongKindException,
                                                IdWrongFormatException,
                                                ObjectDoesNotExistException,
                                                ServiceNotUniqueException,
                                                UnexpectedFailureException,
                                                java.rmi.RemoteException,
                                                javax.ejb.EJBException
Retrieves client interface settings for the specified activity instance using the activity instance ID.
 
 Client interface settings allow for the specification of presentations that can
 be used by the caller to present objects and data to an end user.
 It is not only possible to display data handled by activities in a specific way but
 also to specify JSPs that display the properties of process instances and their templates specifically.
 
 Client interface settings can be retrieved in any execution state of the activity
 and associated process instance.
 The caller must have at least reader authority for the activity instance, for the
 associated process instance,
 or for a scope that contains the activity instance.
Parameters:aiid - The object ID of the activity instance.
 
Returns:CustomClientSettings -
    The customized client interface settings.
    Returns null if there are no customized client interface settings.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
ServiceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getClientUISettings
CustomClientSettings getClientUISettings(java.lang.String vtid,
                                       java.lang.String atid)
                                         throws EngineNotAuthorizedException,
                                                EngineWrongKindException,
                                                IdWrongFormatException,
                                                IdWrongTypeException,
                                                ObjectDoesNotExistException,
                                                UnexpectedFailureException,
                                                java.rmi.RemoteException,
                                                javax.ejb.EJBException
Retrieves client interface settings for the specified service using a string representation
 of the activity and service object IDs.
 
 Client interface settings allow for the specification of presentations that can
 be used by the caller to present objects and data to an end user.
 It is not only possible to display data handled by activities in a specific way but
 also to specify JSPs that display the properties of process instances and their templates specifically.
 
 Client interface settings can be retrieved in any execution state of the activity
 and associated process instance.
 The caller must have at least reader authority for the activity instance, for the
 associated process instance,
 or for a scope that contains the activity instance.
Parameters:vtid - A string representation of the activity service template ID. This is used
    to identify the service whose settings are to be retrieved.atid - A string representation of the activity template ID. This is used
    to identify the activity the service belongs to.
 

Returns:CustomClientSettings -
    The customized client interface settings.
    Returns null if there are no customized client interface settings.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getClientUISettings
CustomClientSettings getClientUISettings(VTID vtid,
                                       ATID atid)
                                         throws EngineNotAuthorizedException,
                                                EngineWrongKindException,
                                                IdWrongFormatException,
                                                ObjectDoesNotExistException,
                                                UnexpectedFailureException,
                                                java.rmi.RemoteException,
                                                javax.ejb.EJBException
Retrieves client interface settings for the specified service using the activity
 and service object IDs.
 
 Client interface settings allow for the specification of presentations that can
 be used by the caller to present objects and data to an end user.
 It is not only possible to display data handled by activities in a specific way but
 also to specify JSPs that display the properties of process instances and their templates specifically.
 
 Client interface settings can be retrieved in any execution state of the activity
 and associated process instance.
 The caller must have at least reader authority for the activity instance, for the
 associated process instance,
 or for a scope that contains the activity instance.
Parameters:vtid - The object ID of the activity service template whose settings are to be retrieved.atid - The object ID of the activity the activity service template belongs to.
 

Returns:CustomClientSettings -
    The customized client interface settings.
    Returns null if there are no customized client interface settings.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getCorrelationSetInstances
java.util.List getCorrelationSetInstances(java.lang.String piid)
                                          throws EngineNotAuthorizedException,
                                                 IdWrongFormatException,
                                                 IdWrongTypeException,
                                                 ObjectDoesNotExistException,
                                                 UnexpectedFailureException,
                                                 java.rmi.RemoteException,
                                                 javax.ejb.EJBException
Retrieves the correlation set instances of the specified process instance
 using a string representation of the process instance ID.
 
 Correlation set instances can be retrieved in any execution state of the process instance.
 The caller must have at least reader authority for the process instance.
Parameters:piid - A string representation of the process instance object ID that is used
    to identify the process instance.
 
Returns:List -
    A list of CorrelationSetInstanceData objects.
    Returns an empty list if there are no correlation set instances.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0

- getCorrelationSetInstances
java.util.List getCorrelationSetInstances(PIID piid)
                                          throws EngineNotAuthorizedException,
                                                 IdWrongFormatException,
                                                 ObjectDoesNotExistException,
                                                 UnexpectedFailureException,
                                                 java.rmi.RemoteException,
                                                 javax.ejb.EJBException
Retrieves the correlation set instances of the specified process instance
 using the process instance ID.
 
 Correlation set instances can be retrieved in any execution state of the process instance.
 The caller must have at least reader authority for the process instance.
Parameters:piid - The process instance object ID that is used to identify the process instance.
 
Returns:List -
    A list of CorrelationSetInstanceData objects.
    Returns an empty list if there are no correlation set instances.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0

- getCorrelationSetInstances
java.util.List getCorrelationSetInstances(java.lang.String aiid,
                                        java.lang.String messageTypeName)
                                          throws EngineNotAuthorizedException,
                                                 EngineParameterNullException,
                                                 EngineVariableDoesNotExistException,
                                                 EngineWrongKindException,
                                                 EngineWrongStateException,
                                                 IdWrongFormatException,
                                                 IdWrongTypeException,
                                                 ObjectDoesNotExistException,
                                                 UnexpectedFailureException,
                                                 java.rmi.RemoteException,
                                                 javax.ejb.EJBException
Retrieves the correlation set instances of the specified activity instance
 and message type
 using a string representation of the activity instance ID.
 
 Correlation set instances can be retrieved in any execution state of the activity instance.
 The activity instance must be a receive, pick, invoke, or reply activity.
 The caller must have at least reader authority for the activity instance, for the
 associated process instance,
 or for a scope that contains the activity instance.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance.messageTypeName - The name of the message type for which corrrelation set instances are to be retrieved.
    Refer to ActivityInstanceData.getInputMessageTypeName().
 
Returns:List -
    A list of CorrelationSetInstanceData objects.
    Returns an empty list if there are no correlation set instances.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
EngineVariableDoesNotExistException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0

- getCorrelationSetInstances
java.util.List getCorrelationSetInstances(AIID aiid,
                                        java.lang.String messageTypeName)
                                          throws EngineNotAuthorizedException,
                                                 EngineParameterNullException,
                                                 EngineVariableDoesNotExistException,
                                                 EngineWrongKindException,
                                                 EngineWrongStateException,
                                                 IdWrongFormatException,
                                                 ObjectDoesNotExistException,
                                                 UnexpectedFailureException,
                                                 java.rmi.RemoteException,
                                                 javax.ejb.EJBException
Retrieves the correlation set instances of the specified activity instance
 and message type
 using the activity instance ID.
 
 Correlation set instances can be retrieved in any execution state of the activity instance.
 The activity instance must be a receive, pick, invoke, or reply activity.
 The caller must have at least reader authority for the activity instance, for the
 associated process instance,
 or for a scope that contains the activity instance.
Parameters:aiid - The activity instance object ID that is used to identify the activity instance.messageTypeName - The name of the message type for which corrrelation set instances are to be retrieved.
    Refer to ActivityInstanceData.getInputMessageTypeName().
 
Returns:List -
    A list of CorrelationSetInstanceData objects.
    Returns an empty list if there are no correlation set instances.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
EngineVariableDoesNotExistException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0

- getCustomProperties
java.util.List getCustomProperties(java.lang.String identifier)
                                   throws EngineNotAuthorizedException,
                                          EngineWrongKindException,
                                          EngineWrongStateException,
                                          IdWrongFormatException,
                                          IdWrongTypeException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the custom properties of the specified process template, process instance,
 or activity instance using a string representation of the object ID.
 
 Custom properties allow a user to add additional properties to processes and activities,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances and activities.
 
 Custom properties can be retrieved in any execution state of the process or activity instance.
 An activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the process or activity instance,
 or for a scope that contains the activity instance.
Parameters:identifier - A string representation of the process template, process instance, or activity instance object ID. This
    string is used to identify the object for which the custom properties are to be retrieved.
 
Returns:List -
    A list of CustomProperty objects.
    The list is empty if there are no custom properties.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getCustomProperties
java.util.List getCustomProperties(PTID ptid)
                                   throws EngineNotAuthorizedException,
                                          IdWrongFormatException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the custom properties of the specified process template using the process template ID.
 
 Custom properties allow a user to add additional properties to a process,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances and activities.
 
 The caller must be authorized for the process template.
Parameters:ptid - The process template object ID whose custom properties are to be retrieved.
 
Returns:List -
    A list of CustomProperty objects.
    The list is empty if there are no custom properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getCustomProperties
java.util.List getCustomProperties(PIID piid)
                                   throws EngineNotAuthorizedException,
                                          EngineWrongKindException,
                                          EngineWrongStateException,
                                          IdWrongFormatException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the custom properties of the specified process instance using the process instance ID.
 
 Custom properties allow a user to add additional properties to a process,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances and activities.
 
 Custom properties can be retrieved in any execution state of the process instance.
 The caller must have at least reader authority for the process instance
 or be the process starter.
Parameters:piid - The process instance object ID whose custom properties are to be retrieved.
 
Returns:List -
    A list of CustomProperty objects.
    The list is empty if there are no custom properties.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getCustomProperties
java.util.List getCustomProperties(AIID aiid)
                                   throws EngineNotAuthorizedException,
                                          EngineWrongKindException,
                                          EngineWrongStateException,
                                          IdWrongFormatException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the custom properties of the specified activity instance using the activity instance ID.
 
 Custom properties allow a user to add additional properties to an activity,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances and activities.
 
 Custom properties can be retrieved in any execution state of the activity and
 associated process instance.
 The activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the activity instance, for the
 associated process instance,
 or for a scope that contains the activity instance.
Parameters:aiid - The activity instance object ID whose custom properties are to be retrieved.
 
Returns:List -
    A list of CustomProperty objects.
    The list is empty if there are no custom properties.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getCustomProperties
java.util.List getCustomProperties(PIID piid,
                                 java.lang.String activityName)
                                   throws EngineAmbiguousActivityException,
                                          EngineNotAuthorizedException,
                                          EngineParameterNullException,
                                          EngineWrongKindException,
                                          EngineWrongStateException,
                                          EngineUnknownActivityException,
                                          IdWrongFormatException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the custom properties of the specified activity instance using
 using the process instance ID and the activity name.
 
 Custom properties allow a user to add additional properties to an activity,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances and activities.
 
 Custom properties can be retrieved in any execution state of the activity and
 associated process instance.
 The activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the activity instance, for the
 associated process instance,
 or for a scope that contains the activity instance.
Parameters:piid - The process instance object ID whose custom properties are to be retrieved.activityName - The name of the activity instance that is used
    to identify the activity instance.
 
Returns:List -
    A list of CustomProperty objects.
    The list is empty if there are no custom properties.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongStateException
EngineUnknownActivityException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getCustomProperties
java.util.List getCustomProperties(java.lang.String identifier,
                                 java.lang.String activityName)
                                   throws EngineAmbiguousActivityException,
                                          EngineNotAuthorizedException,
                                          EngineParameterNullException,
                                          EngineWrongKindException,
                                          EngineWrongStateException,
                                          EngineUnknownActivityException,
                                          IdWrongFormatException,
                                          IdWrongTypeException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the custom properties of the specified activity instance
 using a string representation of the process instance ID and the activity name.
 
 Custom properties allow a user to add additional properties to an activity,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances and activities.
 
 Custom properties can be retrieved in any execution state of the activity and
 associated process instance.
 The activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the activity instance, for the
 associated process instance,
 or for a scope that contains the activity instance.
Parameters:identifier - A string representation of the process instance object ID that is used
    to identify the process instance.activityName - The name of the activity instance that is used
    to identify the activity instance.
 
Returns:List -
    A list of CustomProperty objects.
    The list is empty if there are no custom properties.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongStateException
EngineUnknownActivityException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getCustomProperty
java.lang.String getCustomProperty(java.lang.String identifier,
                                 java.lang.String propertyName)
                                   throws EngineNotAuthorizedException,
                                          EngineParameterNullException,
                                          EngineWrongKindException,
                                          EngineWrongStateException,
                                          IdWrongFormatException,
                                          IdWrongTypeException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the named custom property of the specified process template, process instance,
 or activity instance using a string representation of the object ID.
 
 Custom properties allow a user to add additional properties to processes and activities,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances and activities.
 
 A custom property can be retrieved in any execution state of the process or activity instance.
 An activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the process template, the process instance,
 or activity instance, be the starter of the process instance,
 or have reader authority for a scope that contains the activity instance.
Parameters:identifier - A string representation of the process template, process instance, or activity instance object ID. This
    string is used to identify the object for which the custom property is to be retrieved.propertyName - The name of the custom property for which the value is to be retrieved.
 

Returns:String -
    The value of the specified custom property.
    Returns null if the specified property cannot be found.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2 - introdued in 5.1

- getCustomProperty
java.lang.String getCustomProperty(PTID ptid,
                                 java.lang.String propertyName)
                                   throws EngineNotAuthorizedException,
                                          EngineParameterNullException,
                                          EngineWrongKindException,
                                          IdWrongFormatException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the named custom property of the specified process template using the process template ID.
 
 Custom properties allow a user to add additional properties to a process,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment.
 
 The caller must be authorized for the process template.
 
Parameters:ptid - The process template object ID whose named custom property is to be retrieved.propertyName - The name of the custom property for which the value is to be read.
 
Returns:String -
    The value of the specified custom property.
    Returns null if the specified property cannot be found.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1

- getCustomProperty
java.lang.String getCustomProperty(PIID piid,
                                 java.lang.String propertyName)
                                   throws EngineNotAuthorizedException,
                                          EngineParameterNullException,
                                          EngineWrongStateException,
                                          IdWrongFormatException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the named custom property of the specified process instance using the process instance ID.
 
 Custom properties allow a user to add additional properties to a process,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances.
 
 Custom property can be retrieved in any execution state of the process instance.
 The caller must have at least reader authority for the process instance
 or be the process starter.
Parameters:piid - The process instance object ID for which the named custom property is to be retrieved.propertyName - The name of the custom property for which the value is to be retrieved.
 

Returns:String -
    The value of the specified custom property.
    Returns null if the specified property cannot be found.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1

- getCustomProperty
java.lang.String getCustomProperty(AIID aiid,
                                 java.lang.String propertyName)
                                   throws EngineNotAuthorizedException,
                                          EngineParameterNullException,
                                          EngineWrongKindException,
                                          EngineWrongStateException,
                                          IdWrongFormatException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the named custom property of the specified activity instance using the activity instance ID.
 
 Custom properties allow a user to add additional properties to an activity,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances and activities.
 
 A custom property can be retrieved in any execution state of the activity and
 associated process instance.
 The activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the activity instance, for the
 associated process instance,
 or for a scope that contains the activity instance.
Parameters:aiid - The activity instance object ID whose named custom property is to be retrieved.propertyName - The name of the custom property for which the value is to be read.
 
Returns:String -
    The value of the specified custom property.
    Returns null if the specified property cannot be found.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getCustomProperty
java.lang.String getCustomProperty(java.lang.String piid,
                                 java.lang.String activityName,
                                 java.lang.String propertyValue)
                                   throws EngineAmbiguousActivityException,
                                          EngineNotAuthorizedException,
                                          EngineParameterNullException,
                                          EngineUnknownActivityException,
                                          EngineWrongKindException,
                                          EngineWrongStateException,
                                          IdWrongFormatException,
                                          IdWrongTypeException,
                                          InvalidLengthException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the named custom property of the specified activity instance
 using a string representation of the process instance ID and the activity name.
 
 Custom properties allow a user to add additional properties to processes and activities,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances and activities.
 
 A custom property has a name and a value of type string.
 
 A custom property can be retrieved in any execution state of the activity and
 associated process instance.
 The activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the activity instance, for the
 associated process instance,
 or for a scope that contains the activity instance.
Parameters:piid - A string representation of the process instance object ID that is used
    to identify the process instance.activityName - The name of the activity instance whose named custom property is to be retrieved.propertyValue - The name of the custom property for which the value is to be read.
 
Returns:String -
    The value of the specified custom property.
    Returns null if the specified property cannot be found.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getCustomProperty
java.lang.String getCustomProperty(PIID piid,
                                 java.lang.String activityName,
                                 java.lang.String propertyName)
                                   throws EngineAmbiguousActivityException,
                                          EngineNotAuthorizedException,
                                          EngineParameterNullException,
                                          EngineUnknownActivityException,
                                          EngineWrongKindException,
                                          EngineWrongStateException,
                                          IdWrongFormatException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the named custom property of the specified activity instance
 using the process instance ID and the activity name.
 
 Custom properties allow a user to add additional properties to processes and activities,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances and activities.
 
 A custom property has a name and a value of type string.
 
 A custom property can be retrieved in any execution state of the activity and
 associated process instance.
 The activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the activity instance, for the
 associated process instance,
 or for a scope that contains the activity instance.
Parameters:piid - The process instance object ID that is used to identify the process instance.activityName - The name of the activity instance whose named custom property is to be retrieved.propertyName - The name of the custom property for which the value is to be read.
 
Returns:String -
    The value of the specified custom property.
    Returns null if the specified property cannot be found.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getCustomPropertyInfo
java.util.List getCustomPropertyInfo(int objectType,
                                   java.lang.String nameFilter,
                                   java.lang.Integer threshold)
                                     throws InvalidParameterValueException,
                                            WorkItemManagerException,
                                            UnexpectedFailureException,
                                            java.rmi.RemoteException,
                                            javax.ejb.EJBException
Retrieves information about custom properties of the specified object types.
 
 Custom properties allow a user to add additional properties to objects
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime.
 
 Besides specifying an object type, you can specify a threshold or a filter to reduce
 the custom property information returned.
Parameters:objectType - An indicator that specifies for which object type custom property information
    is to be retrieved. If there are multiple custom properties with the same name for the
    same object type, a single information entry is returned.nameFilter - A filter on the names of custom properties.
    A SQL LIKE predicate is used for the name filter provided.threshold - Specifies the maximum number of custom property information entries to be returned from the
    server to the client. If a threshold is not to be applied, null must be specified.
 
Returns:List -
    A list of CustomPropertyInfo objects.
    For instances, information is only returned for custom properties the logged-on
    user is authorized to read.
    
    The list is empty if there are no custom properties for the specified object type
    the user is authorized to read.
 
Throws:
InvalidParameterValueException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2

- getCustomPropertyNames
java.util.List getCustomPropertyNames(java.lang.String identifier)
                                      throws EngineNotAuthorizedException,
                                             IdWrongFormatException,
                                             IdWrongTypeException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves the custom property names of the specified process template, process instance,
 or activity instance using a string representation of the object ID.
 
 The process instance or activity instance can be in any execution state.
 An activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the process or activity instance,
 or for a scope that contains the activity instance.
Parameters:identifier - A string representation of the process template, process instance or activity instance object ID. This
    string is used to identify the object for which the custom properties are to be retrieved.
 
Returns:List -
    A list of custom property names. The list is empty, if there
  are no custom properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getCustomPropertyNames
java.util.List getCustomPropertyNames(PTID ptid)
                                      throws EngineNotAuthorizedException,
                                             IdWrongFormatException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves the custom property names of the specified process template
 using the process template ID.
 
 The caller must have at least reader authority for the process template.
Parameters:ptid - The object ID of the process template.
 

Returns:List -
    A list of custom property names. The list is empty, if there
  are no custom properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getCustomPropertyNames
java.util.List getCustomPropertyNames(PIID piid)
                                      throws EngineNotAuthorizedException,
                                             IdWrongFormatException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves the custom property names of the specified process instance
 using the process instance ID.
 
 The process instance can be in any execution state.
 The caller must have at least reader authority for the process instance
 or be the process starter.
Parameters:piid - The object ID of the process instance.
 

Returns:List -
    An list of custom property names. The list is empty, if there
  are no custom properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getCustomPropertyNames
java.util.List getCustomPropertyNames(AIID aiid)
                                      throws EngineNotAuthorizedException,
                                             IdWrongFormatException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves the custom property names of the specified activity instance
 using the activity instance ID.
 
 The activity instance can be in any execution state.
 The activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the activity instance
 or for a scope that contains the activity instance.
Parameters:aiid - The object ID of the activity instance.
 
Returns:List -
    An list of custom property names. The list is empty, if there
  are no custom properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getCustomPropertyNames
java.util.List getCustomPropertyNames(java.lang.String identifier,
                                    java.lang.String activityName)
                                      throws EngineAmbiguousActivityException,
                                             EngineNotAuthorizedException,
                                             EngineParameterNullException,
                                             EngineWrongKindException,
                                             EngineWrongStateException,
                                             EngineUnknownActivityException,
                                             IdWrongFormatException,
                                             IdWrongTypeException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves the custom property names of the specified
 activity instance using a string representation of the process instance object ID
 and the activity instance name.
 
 The process instance or activity instance can be in any execution state.
 The activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the process or activity instance
 or for a scope that contains the activity instance.
Parameters:identifier - A string representation of the process instance object ID.activityName - The name of the activity instance that is used
    to identify the activity instance.
 
Returns:List -
    A list of custom property names. The list is empty, if there
  are no custom properties.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongStateException
EngineUnknownActivityException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getCustomPropertyNames
java.util.List getCustomPropertyNames(PIID piid,
                                    java.lang.String activityName)
                                      throws EngineAmbiguousActivityException,
                                             EngineNotAuthorizedException,
                                             EngineParameterNullException,
                                             EngineWrongKindException,
                                             EngineWrongStateException,
                                             EngineUnknownActivityException,
                                             IdWrongFormatException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves the custom property names of the specified
 activity instance using the process instance object ID
 and the activity instance name.
 
 The process instance or activity instance can be in any execution state.
 The activity instance must be a basic activity or a pick activity.
 The caller must have at least reader authority for the process or activity instance
 or for a scope that contains the activity instance.
Parameters:piid - The process instance object ID.activityName - The name of the activity instance that is used
    to identify the activity instance.
 
Returns:List -
    A list of custom property names. The list is empty, if there
  are no custom properties.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongStateException
EngineUnknownActivityException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getFaultMessage
ClientObjectWrapper getFaultMessage(java.lang.String identifier)
                                    throws DataHandlingException,
                                           EngineNotAuthorizedException,
                                           EngineWrongKindException,
                                           EngineWrongStateException,
                                           IdWrongFormatException,
                                           IdWrongTypeException,
                                           ObjectDoesNotExistException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Retrieves the fault message of the specified process or activity instance using
 a string representation of the process or activity instance ID.
 
 The fault message can be retrieved in any execution state of the process instance.
 The activity instance must be in the claimed, expired, failed,
 finished, terminated, ready, or stopped execution state.
 The activity can be an request-response invoke, script, or human task activity.
 A human task activity is also known as staff activity.
 Note that that any saved fault message of an expired, that is, non-completed
 human task activity has been deleted.
 
 The caller must have at least reader authority for the process or activity instance,
 be the starter of the process instance,
 or have reader authority for a scope that contains the activity instance.
Parameters:identifier - A string representation of the process or activity instance object ID. This string is used to
    identify the process instance or activity instance for which the fault message is to be retrieved.
 

Returns:ClientObjectWrapper -
    The fault message. If there is no fault message, an empty client object wrapper is returned.
 
Throws:
DataHandlingException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getFaultMessage
ClientObjectWrapper getFaultMessage(PIID piid)
                                    throws EngineNotAuthorizedException,
                                           EngineWrongKindException,
                                           EngineWrongStateException,
                                           IdWrongFormatException,
                                           ObjectDoesNotExistException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Retrieves the fault message of the specified process instance using the process instance ID.
 
 The fault message can be retrieved in any execution state of the process instance.
 The caller must have at least reader authority for the process instance
 or be the starter of the process instance.
Parameters:piid - The object ID of the process instance for which the fault message is to be retrieved.
 
Returns:ClientObjectWrapper -
    The fault message. If there is no fault message, an empty client object wrapper is returned.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1

- getFaultMessage
ClientObjectWrapper getFaultMessage(AIID aiid)
                                    throws DataHandlingException,
                                           EngineNotAuthorizedException,
                                           EngineWrongKindException,
                                           EngineWrongStateException,
                                           IdWrongFormatException,
                                           ObjectDoesNotExistException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Retrieves the fault message of the specified activity instance using the activity instance ID.
 
 The fault message can be retrieved in any execution state of the associated process instance.
 The activity instance must be in the claimed, expired, failed,
 finished, terminated, ready, or stopped execution state.
 The activity can be an request-response invoke, script, or human task activity.
 A human task activity is also known as staff activity.
 Note that that any saved fault message of an expired, that is, non-completed
 human task activity has been deleted.
 
 The caller must have at least reader authority for the activity instance, for the
 associated process instance,
 or for a scope that contains the activity instance.
Parameters:aiid - The object ID of the activity instance for which the fault message is to be retrieved.
 
Returns:ClientObjectWrapper -
    The fault message. If there is no fault message, an empty client object wrapper is returned.
 
Throws:
DataHandlingException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getFaultNames
java.util.List getFaultNames(java.lang.String aiid)
                             throws EngineNotAuthorizedException,
                                    EngineWrongKindException,
                                    EngineWrongStateException,
                                    IdWrongFormatException,
                                    IdWrongTypeException,
                                    ObjectDoesNotExistException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Retrieves the fault names defined for the specified activity instance
 using a string representation of the activity instance ID.
 
 Fault names can be retrieved in any execution state of the associated process instance.
 The activity instance must be in the claimed, expired, failed,
 finished, terminated, ready, or stopped execution state.
 The activity can be a human task activity.
 A human task activity is also known as staff activity.
 
 The caller must have at least reader authority for the activity instance,
 for the associated process instance
 or for a scope that contains the activity instance.
Parameters:aiid - A string representation of the activity instance object ID that
    is used to identify the activity instance for which fault names are to be retrieved.
 
Returns:List -
    A list of fault names. If there are no faults, an empty list is returned.
    Fault names are to be specified when a fault message is set -
 refer to complete,
 forceComplete
setFaultMessage,
 or to createMessage.
 
 Note that, although strings are returned, the structure of a fault name is a QName.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getFaultNames
java.util.List getFaultNames(AIID aiid)
                             throws EngineNotAuthorizedException,
                                    EngineWrongKindException,
                                    EngineWrongStateException,
                                    IdWrongFormatException,
                                    ObjectDoesNotExistException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Retrieves the fault names defined for the specified activity instance
 using the activity instance ID.
 
 Fault names can be retrieved in any execution state of the associated process instance.
 The activity instance must be in the claimed, expired, failed,
 finished, terminated, ready, or stopped execution state.
 The activity can be a human task activity.
 A human task activity is also known as staff activity.
 
 The caller must have at least reader authority for the activity instance,
 for the associated process instance
 or for a scope that contains the activity instance.
Parameters:aiid - The object ID of the activity instance for which the fault names are to be retrieved.
 
Returns:List -
    A list of fault names. If there are no faults, an empty list is returned.
    Fault names are to be specified when a fault message is set.
 Refer to complete,
 forceComplete
setFaultMessage,
 or to createMessage.
 
 Note that, although strings are returned, the structure of a fault name is a QName.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getGraphics
byte[] getGraphics(java.lang.String identifier)
                   throws EngineNotAuthorizedException,
                          EngineParameterNullException,
                          IdWrongTypeException,
                          ObjectDoesNotExistException,
                          ProcessException,
                          UnexpectedFailureException,
                          java.rmi.RemoteException,
                          javax.ejb.EJBException
Retrieves a graphical representation of the specified process template using
 a string representation of the process template ID or the process template name.
 When the process template name is specified, the graphical representation of the
 currently valid process template is returned.
 
 A possible representation can be a Scalable Vector Graphics (SVG).
 
 The caller must be authorized for the process template.
Parameters:identifier - A string representation of the process template ID
 or the process template name to identify the process
    template for which a graphical representation is to be retrieved.
 
Returns:byte[] -
    The graphical representation of the process template. If there is no
    graphical representation, null is returned.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
IdWrongTypeException
ObjectDoesNotExistException
ProcessException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getGraphics
byte[] getGraphics(PTID ptid)
                   throws EngineNotAuthorizedException,
                          ObjectDoesNotExistException,
                          ProcessException,
                          UnexpectedFailureException,
                          java.rmi.RemoteException,
                          javax.ejb.EJBException
Retrieves a graphical representation of the specified process template using
 the process template ID.
 A possible representation can be a Scalable Vector Graphics (SVG).
 
 The caller must be authorized for the process template.
Parameters:ptid - The object ID of the process template for which a graphical representation
    is to be retrieved.
 
Returns:byte[] -
    The graphical representation of the process template. If there is no
    graphical representation, null is returned.
 
Throws:
EngineNotAuthorizedException
ObjectDoesNotExistException
ProcessException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getInitialVariableValue
ClientObjectWrapper getInitialVariableValue(java.lang.String piid,
                                          java.lang.String activityName,
                                          java.lang.String variableName)
                                            throws ArchiveUnsupportedOperationException,
                                                   EngineAmbiguousActivityException,
                                                   EngineInitializingScopeNotReachedException,
                                                   EngineNotAuthorizedException,
                                                   EngineParameterNullException,
                                                   EngineUnknownActivityException,
                                                   EngineVariableNotVisibleException,
                                                   EngineWrongKindException,
                                                   EngineWrongStateException,
                                                   IdWrongFormatException,
                                                   IdWrongTypeException,
                                                   ObjectDoesNotExistException,
                                                   UnexpectedFailureException,
                                                   java.rmi.RemoteException,
                                                   javax.ejb.EJBException
Retrieves the initial value of the specified variable visible
 by the specified activity
 using a string representation of the process instance ID and the activity name.
 
 Initial value means that the value returned essentially contains the type information of the variable only.
 For Java primitive types, their boxed types are returned.
 For complex types, DataObject's are returned that are created with type information only.
 
 Variables allow to store business data for the process instance, across activity invocations or for the activity.
 
 The activity need not be navigated.
 If the activity is navigated,
 the caller must have at least reader authority for the activity instance, for the
 process instance, or for a scope that contains the activity instance.
 If the activity is not navigated,
 the caller must have at least reader authority for the
 process instance or for a scope that contains the activity provided that
 the scope is already navigated.
 
 This method is not supported in archive mode.
Parameters:piid - A string representation of the process instance object ID. This is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.variableName - The name of the variable to be retrieved.
 
Returns:ClientObjectWrapper -
    The initial variable value. Variable values that are already set are not
    returned. Refer to getVariable
    for the retrieval of variable data.
 
Throws:
ArchiveUnsupportedOperationException
EngineAmbiguousActivityException
EngineInitializingScopeNotReachedException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineVariableNotVisibleException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 Throws an
 EngineWrongKindException when an activity is specified that is for internal use only.
 
7.0
 Throws an
 EngineWrongStateException when an activity is specified that has not been migrated as
 part of a migrated process instance.

- getInitialVariableValue
ClientObjectWrapper getInitialVariableValue(PIID piid,
                                          java.lang.String activityName,
                                          java.lang.String variableName)
                                            throws ArchiveUnsupportedOperationException,
                                                   EngineAmbiguousActivityException,
                                                   EngineInitializingScopeNotReachedException,
                                                   EngineNotAuthorizedException,
                                                   EngineParameterNullException,
                                                   EngineUnknownActivityException,
                                                   EngineVariableNotVisibleException,
                                                   EngineWrongKindException,
                                                   EngineWrongStateException,
                                                   IdWrongFormatException,
                                                   ObjectDoesNotExistException,
                                                   UnexpectedFailureException,
                                                   java.rmi.RemoteException,
                                                   javax.ejb.EJBException
Retrieves the initial value of the specified variable visible
 by the specified activity
 using the process instance ID and the activity name.
 
 Initial value means that the value returned essentially contains the type information of the variable only.
 For Java primitive types, their boxed types are returned.
 For complex types, DataObject's are returned that are created with type information only.
 
 Variables allow to store business data for the process instance, across activity invocations or for the activity.
 
 The activity need not be navigated.
 If the activity is navigated,
 the caller must have at least reader authority for the activity instance, for the
 process instance, or for a scope that contains the activity instance.
 If the activity is not navigated,
 the caller must have at least reader authority for the
 process instance or for a scope that contains the activity provided that
 the scope is already navigated.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance that is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.variableName - The name of the variable to be retrieved.
 
Returns:ClientObjectWrapper -
    The initial variable value. Variable values that are already set are not
    returned. Refer to getVariable
    for the retrieval of variable data.
 
Throws:
ArchiveUnsupportedOperationException
EngineAmbiguousActivityException
EngineInitializingScopeNotReachedException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineVariableNotVisibleException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 Throws an
 EngineWrongKindException when an activity is specified that is for internal use only.
 
7.0
 Throws an
 EngineWrongStateException when an activity is specified that has not been migrated as
 part of a migrated process instance.

- getInitialVariableValue
ClientObjectWrapper getInitialVariableValue(java.lang.String identifier,
                                          java.lang.String variableName)
                                            throws ArchiveUnsupportedOperationException,
                                                   EngineNotAuthorizedException,
                                                   EngineParameterNullException,
                                                   EngineVariableDoesNotExistException,
                                                   EngineWrongKindException,
                                                   EngineWrongStateException,
                                                   IdWrongFormatException,
                                                   IdWrongTypeException,
                                                   ObjectDoesNotExistException,
                                                   UnexpectedFailureException,
                                                   java.rmi.RemoteException,
                                                   javax.ejb.EJBException
Retrieves the initial value of the specified variable of the specified process instance
 or the specified variable visible by the specified activity instance
 using a string representation of the process or activity instance ID.
 Initial value means that the value returned essentially contains the type information of the variable only.
 For Java primitive types, their boxed types are returned.
 For complex types, DataObject's are returned that are created with type information only.
 
 Variables allow to store business data for the process, across activity invocations.
 They can be retrieved in any execution state of the process or activity instance.
 The caller must have at least reader authority for the process instance or activity instance
 or for a scope that contains the activity instance
 or be the starter of the process instance.
 
 This method is not supported in archive mode.
Parameters:identifier - A string representation of the process instance object ID or activity instance object ID.
    This string is used to
    identify the process instance or activity instance for which the specified variable
    is to be retrieved.variableName - The name of the variable to be retrieved.
 
Returns:ClientObjectWrapper -
    The initial variable value. Variable values that are already set are not
    returned. Refer to getVariable(PIID,String)
    or getVariable(AIID,String)
    for the retrieval of variable data.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineVariableDoesNotExistException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 Throws an
 EngineWrongKindException when an activity is specified that is for internal use only.
 
7.0
 Throws an
 EngineWrongStateException when an activity is specified that has not been migrated as
 part of a migrated process instance.

- getInitialVariableValue
ClientObjectWrapper getInitialVariableValue(PIID piid,
                                          java.lang.String variableName)
                                            throws ArchiveUnsupportedOperationException,
                                                   EngineNotAuthorizedException,
                                                   EngineParameterNullException,
                                                   EngineVariableDoesNotExistException,
                                                   IdWrongFormatException,
                                                   ObjectDoesNotExistException,
                                                   UnexpectedFailureException,
                                                   java.rmi.RemoteException,
                                                   javax.ejb.EJBException
Retrieves the initial value of the specified variable
 of the specified process instance using the process instance ID.
 
 Initial value means that the value returned essentially contains the type information of the variable only.
 For Java primitive types, their boxed types are returned.
 For complex types, DataObject's are returned that are created with type information only.
 
 Variables allow to store business data for the process, across activity invocations.
 They can be retrieved in any execution state of the process instance.
 The caller must have at least reader authority for the process instance
 or be the starter of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance for which the specified variable is to be retrieved.variableName - The name of the variable to be retrieved.
 
Returns:ClientObjectWrapper -
    The initial variable value. Variable values that are already set are not
    returned. Refer to getVariable
    for the retrieval of variable data.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineVariableDoesNotExistException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- getInitialVariableValue
ClientObjectWrapper getInitialVariableValue(AIID aiid,
                                          java.lang.String variableName)
                                            throws ArchiveUnsupportedOperationException,
                                                   EngineNotAuthorizedException,
                                                   EngineParameterNullException,
                                                   EngineVariableDoesNotExistException,
                                                   EngineWrongKindException,
                                                   EngineWrongStateException,
                                                   IdWrongFormatException,
                                                   ObjectDoesNotExistException,
                                                   UnexpectedFailureException,
                                                   java.rmi.RemoteException,
                                                   javax.ejb.EJBException
Retrieves the initial value of the specified variable visible
 by the specified activity instance using the activity instance ID.
 
 Initial value means that the value returned essentially contains the type information of the variable only.
 For Java primitive types, their boxed types are returned.
 For complex types, DataObject's are returned that are created with type information only.
 
 Variables allow to store business data for the process instance, across activity invocations or for the activity.
 They can be retrieved in any execution state of the activity instance.
 The caller must have at least reader authority for the activity instance
 or for a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID of the activity instance for which the specified variable is to be retrieved.variableName - The name of the variable to be retrieved.
 
Returns:ClientObjectWrapper -
    The initial variable value. Variable values that are already set are not
    returned. Refer to getVariable
    for the retrieval of variable data.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineVariableDoesNotExistException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 Throws an
 EngineWrongKindException when an activity is specified that is for internal use only.
 
7.0
 Throws an
 EngineWrongStateException when an activity is specified that has not been migrated as
 part of a migrated process instance.

- getInlineCustomProperty
InlineCustomProperty getInlineCustomProperty(java.lang.String identifier,
                                           java.lang.String propertyName)
                                             throws EngineNotAuthorizedException,
                                                    EngineParameterNullException,
                                                    IdWrongFormatException,
                                                    IdWrongTypeException,
                                                    InvalidParameterValueException,
                                                    ObjectDoesNotExistException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Retrieves the named inline custom property of the specified process template
 or process instance using a string representation of the object ID.
 
 Custom properties allow a user to add additional properties to processes and activities,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the process template or instance. Thus, using inline custom properties
 can increase performance.
 
 A custom property can be retrieved in any execution state of the process instance.
 The caller must have at least reader authority for the process template or process instance
 or be the starter of the process instance.
Parameters:identifier - A string representation of the process template or process instance object ID. This
    string is used to identify the object for which the inline custom property is to be retrieved.propertyName - The name of the inline custom property for which the value is to be retrieved.
    The name can be one of the predefined names
    InlineCustomProperty.CUSTOM\_TEXT\_1 etc.
 
Returns:InlineCustomProperty -
    The InlineCustomProperty.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
IdWrongFormatException
IdWrongTypeException
InvalidParameterValueException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- getInlineCustomProperty
InlineCustomProperty getInlineCustomProperty(PTID ptid,
                                           java.lang.String propertyName)
                                             throws EngineNotAuthorizedException,
                                                    EngineParameterNullException,
                                                    IdWrongFormatException,
                                                    InvalidParameterValueException,
                                                    ObjectDoesNotExistException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Retrieves the named inline custom property of the specified process template using the process template ID.
 
 Custom properties allow a user to add additional properties to a process,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the process template. Thus, using inline custom properties
 can increase performance.
 
 The caller must be authorized for the process template.
 
Parameters:ptid - The process template object ID whose named custom property is to be retrieved.propertyName - The name of the inline custom property for which the value is to be read.
    The name can be one of the predefined names
    InlineCustomProperty.CUSTOM\_TEXT\_1 etc.
 
Returns:InlineCustomProperty -
    The InlineCustomProperty.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
IdWrongFormatException
InvalidParameterValueException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- getInlineCustomProperty
InlineCustomProperty getInlineCustomProperty(PIID piid,
                                           java.lang.String propertyName)
                                             throws EngineNotAuthorizedException,
                                                    EngineParameterNullException,
                                                    IdWrongFormatException,
                                                    InvalidParameterValueException,
                                                    ObjectDoesNotExistException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Retrieves the named inline custom property of the specified process instance using the process instance ID.
 
 Custom properties allow a user to add additional properties to a process,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the process instance. Thus, using inline custom properties
 can increase performance.
 
 A custom property can be retrieved in any execution state of the process instance.
 The caller must have at least reader authority for the process instance
 or be the process starter.
Parameters:piid - The process instance object ID for which the named custom property is to be retrieved.propertyName - The name of the custom property for which the value is to be retrieved.
    The name can be one of the predefined names
    InlineCustomProperty.CUSTOM\_TEXT\_1 etc.
 
Returns:InlineCustomProperty -
    The InlineCustomProperty.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
IdWrongFormatException
InvalidParameterValueException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- getInputClientUISettings
CustomClientSettings getInputClientUISettings(java.lang.String piid)
                                              throws EngineNotAuthorizedException,
                                                     EngineWrongKindException,
                                                     IdWrongFormatException,
                                                     IdWrongTypeException,
                                                     ObjectDoesNotExistException,
                                                     UnexpectedFailureException,
                                                     java.rmi.RemoteException,
                                                     javax.ejb.EJBException
Retrieves client interface settings for the input message of the specified
 process instance using a string representation of the process instance ID.
 
 Client interface settings allow for the specification of presentations that can
 be used by the caller to present objects and data to an end user in a specific way.
 
 Client interface settings can be retrieved in any execution state of the process instance.
 The caller must have at least reader authority for the process instance
 or be the starter of the process instance.
Parameters:piid - The string representation of the process instance object ID. This
    is used to identify the process instance whose input UI settings are to be retrieved.
 

Returns:CustomClientSettings -
    The customized client interface settings of the input message.
    Returns null if there are no customized client interface settings.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1

- getInputClientUISettings
CustomClientSettings getInputClientUISettings(PIID piid)
                                              throws EngineNotAuthorizedException,
                                                     EngineWrongKindException,
                                                     IdWrongFormatException,
                                                     ObjectDoesNotExistException,
                                                     UnexpectedFailureException,
                                                     java.rmi.RemoteException,
                                                     javax.ejb.EJBException
Retrieves client interface settings for the input message of the specified
 process instance using the process instance ID.
 
 Client interface settings allow for the specification of presentations that can
 be used by the caller to present objects and data to an end user in a specific way.
 
 Client interface settings can be retrieved in any execution state of the process instance.
 The caller must have at least reader authority for the process instance
 or be the starter of the process instance.
Parameters:piid - The object ID of the process instance.
 

Returns:CustomClientSettings -
    The customized client interface settings of the input message.
    Returns null if there are no customized client interface settings.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1

- getInputMessage
ClientObjectWrapper getInputMessage(java.lang.String identifier)
                                    throws DataHandlingException,
                                           EngineNotAuthorizedException,
                                           EngineWrongKindException,
                                           EngineWrongStateException,
                                           IdWrongFormatException,
                                           IdWrongTypeException,
                                           ObjectDoesNotExistException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Retrieves the input message of the specified process or activity instance using a string representation of the ID.
 
 The input message can be retrieved in any execution state of the process instance.
 The input message can be retrieved in the claimed, expired, failed,
 finished, terminated, ready, running, or stopped execution state of the activity instance.
 The activity can be an invoke or human task activity.
 A human task activity is also known as staff activity.
 
 The caller must have at least reader authority for the process or activity instance,
 be the starter of the process instance,
 or have reader authority for a scope that contains the activity instance.
Parameters:identifier - A string representation of the process or activity instance object ID. The string is used
    to identify the process instance or activity instance for which the input message
    is to be retrieved.
 

Returns:ClientObjectWrapper -
    The input message.
 
Throws:
DataHandlingException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getInputMessage
ClientObjectWrapper getInputMessage(PIID piid)
                                    throws EngineNotAuthorizedException,
                                           EngineWrongKindException,
                                           EngineWrongStateException,
                                           IdWrongFormatException,
                                           ObjectDoesNotExistException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Retrieves the input message of the specified process instance using the process instance ID.
 
 The input message can be retrieved in any execution state of the process instance.
 The caller must have at least reader authority for the process instance
 or be the starter of the process instance.
Parameters:piid - The object ID of the process instance whose input message is to be retrieved.
 
Returns:ClientObjectWrapper -
    The input message.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0

- getInputMessage
ClientObjectWrapper getInputMessage(AIID aiid)
                                    throws DataHandlingException,
                                           EngineNotAuthorizedException,
                                           EngineWrongKindException,
                                           EngineWrongStateException,
                                           IdWrongFormatException,
                                           ObjectDoesNotExistException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Retrieves the input message of the specified activity instance using the activity instance ID.
 
 The input message can be retrieved in any execution state of the associated process instance.
 The input message can be retrieved in the claimed, expired, failed,
 finished, terminated, ready, running, or stopped execution state of the activity instance.
 The activity can be an invoke or human task activity.
 A human task activity is also known as staff activity.
 
 The caller must have at least reader authority for the activity instance or for the
 associated process instance
 or have reader authority for a scope that contains the activity instance.
Parameters:aiid - The object ID of the activity instance whose input message is to be retrieved.
 
Returns:ClientObjectWrapper -
    The input message.
 
Throws:
DataHandlingException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getInputVariableNames
java.util.List getInputVariableNames(java.lang.String piid,
                                   java.lang.String activityName)
                                     throws EngineAmbiguousActivityException,
                                            EngineNotAuthorizedException,
                                            EngineParameterNullException,
                                            EngineUnknownActivityException,
                                            EngineWrongKindException,
                                            IdWrongFormatException,
                                            IdWrongTypeException,
                                            ObjectDoesNotExistException,
                                            UnexpectedFailureException,
                                            java.rmi.RemoteException,
                                            javax.ejb.EJBException
Retrieves the names of the input variables for the specified activity
 using a string representation of the process instance ID and the activity name.
 
 The activity can be an invoke or human task activity and need not be navigated.
 Note that a human task activity is also known as staff activity.
 
 If the activity is navigated,
 the caller must have at least reader authority for the activity instance, for the
 process instance, or for a scope that contains the activity instance.
 If the activity is not navigated,
 the caller must have at least reader authority for the
 process instance or for a scope that contains the activity provided that
 the scope is already navigated.
Parameters:piid - A string representation of the process instance object ID. This is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.
 
Returns:List -
    A list of input variable names. If there are no input variables, an empty list is returned.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getInputVariableNames
java.util.List getInputVariableNames(PIID piid,
                                   java.lang.String activityName)
                                     throws EngineAmbiguousActivityException,
                                            EngineNotAuthorizedException,
                                            EngineParameterNullException,
                                            EngineUnknownActivityException,
                                            EngineWrongKindException,
                                            IdWrongFormatException,
                                            ObjectDoesNotExistException,
                                            UnexpectedFailureException,
                                            java.rmi.RemoteException,
                                            javax.ejb.EJBException
Retrieves the names of the input variables for the specified activity
 using the process instance ID and the activity name.
 
 The activity can be an invoke or human task activity and need not be navigated.
 Note that a human task activity is also known as staff activity.
 
 If the activity is navigated,
 the caller must have at least reader authority for the activity instance, for the
 process instance, or for a scope that contains the activity instance.
 If the activity is not navigated,
 the caller must have at least reader authority for the
 process instance or for a scope that contains the activity provided that
 the scope is already navigated.
Parameters:piid - The object ID of the process instance that is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.
 
Returns:List -
    A list of input variable names. If there are no input variables, an empty list is returned.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getInputVariableNames
java.util.List getInputVariableNames(java.lang.String aiid)
                                     throws EngineNotAuthorizedException,
                                            EngineWrongKindException,
                                            IdWrongFormatException,
                                            IdWrongTypeException,
                                            ObjectDoesNotExistException,
                                            UnexpectedFailureException,
                                            java.rmi.RemoteException,
                                            javax.ejb.EJBException
Retrieves the names of all input variables for the specified activity instance
 using a string representation of the activity instance ID.
 
 The activity can be an invoke or human task activity.
 A human task activity is also known as staff activity.
 
 The input variable names can be retrieved in any execution state of the activity instance.
 The caller must have at least reader authority for the activity instance or for the
 associated process instance,
 or have reader authority for a scope that contains the activity instance.
Parameters:aiid - A string representation of the activity instance object ID. This is used
    to identify the activity instance whose input variable names are to be retrieved.
 
Returns:List -
    A list of input variable names. If there are no input variables, an empty list is returned.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getInputVariableNames
java.util.List getInputVariableNames(AIID aiid)
                                     throws EngineNotAuthorizedException,
                                            EngineWrongKindException,
                                            IdWrongFormatException,
                                            ObjectDoesNotExistException,
                                            UnexpectedFailureException,
                                            java.rmi.RemoteException,
                                            javax.ejb.EJBException
Retrieves the names of all input variables for the specified activity instance
 using the activity instance ID.
 
 The activity can be an invoke or human task activity.
 A human task activity is also known as staff activity.
 
 The input variable names can be retrieved in any execution state of the activity instance.
 The caller must have at least reader authority for the activity instance or for the
 associated process instance,
 or have reader authority for a scope that contains the activity instance.
Parameters:aiid - The object ID of the activity instance whose input variable names are to be retrieved.
 
Returns:List -
    A list of input variable names. If there are no input variables, an empty list is returned.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getJumpTargetNames
java.util.List getJumpTargetNames(java.lang.String aiid)
                                  throws EngineAmbiguousActivityException,
                                         EngineNotAuthorizedException,
                                         EngineUnknownActivityException,
                                         IdWrongFormatException,
                                         IdWrongTypeException,
                                         ObjectDoesNotExistException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Retrieves the names of all activities that can be jumped to from the specified
 activity instance using a string representation of the activity instance ID.
 
 Names of activities that are not unique within the containing process are not returned.
 
 The caller must have at least reader authority for the process instance,
 or for a scope that contains the activity and the jump targets.
Parameters:aiid - A string representation of the activity instance object ID. This is used
    to identify the activity instance whose jump target names are to be retrieved.
 
Returns:List -
    A list of names of activities that can be jumped to.
    The list may be empty, for example,
    if there is no activity that can be jumped to,
    if there are no names for activities that can be jumped,
    or if there are no unique names for activities that can be jumped to.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineUnknownActivityException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getJumpTargetNames
java.util.List getJumpTargetNames(AIID aiid)
                                  throws EngineAmbiguousActivityException,
                                         EngineNotAuthorizedException,
                                         EngineUnknownActivityException,
                                         IdWrongFormatException,
                                         ObjectDoesNotExistException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Retrieves the names of all activities that can be jumped to from the specified
 activity instance using the activity instance ID.
 
 Names of activities that are not unique within the containing process are not returned.
 
 The caller must have at least reader authority for the process instance,
 or for a scope that contains the activity and the jump targets.
Parameters:aiid - The object ID of the activity instance whose jump targets are to be retrieved.
 
Returns:List -
    A list of names of activities that can be jumped to.
    The list may be empty, for example,
    if there is no activity that can be jumped to,
    if there are no names for activities that can be jumped,
    or if there are no unique names for activities that can be jumped to.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineUnknownActivityException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getMappingToGraphics
byte[] getMappingToGraphics(java.lang.String identifier)
                            throws EngineNotAuthorizedException,
                                   EngineParameterNullException,
                                   IdWrongTypeException,
                                   ObjectDoesNotExistException,
                                   ProcessException,
                                   UnexpectedFailureException,
                                   java.rmi.RemoteException,
                                   javax.ejb.EJBException
Retrieves the descriptive information of the graphical representation of
 the specified process template using
 a string representation of the process template ID or the process template name.
 When the process template name is specified, the descriptive information of a
 graphical representation of the currently valid process template is returned.
 
 The caller must be authorized for the process template.
Parameters:identifier - A string representation of the process template ID
 or the process template name to identify the process
    template for which a graphical representation is to be retrieved.
 
Returns:byte[] -
    The descriptive information of the graphical representation of the process template.
  If there is no the descriptive information null is returned.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
IdWrongTypeException
ObjectDoesNotExistException
ProcessException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getMappingToGraphics
byte[] getMappingToGraphics(PTID ptid)
                            throws EngineNotAuthorizedException,
                                   ObjectDoesNotExistException,
                                   ProcessException,
                                   UnexpectedFailureException,
                                   java.rmi.RemoteException,
                                   javax.ejb.EJBException
Retrieves the descriptive information of the graphical representation of the specified process template using
 the process template ID.
 
 The caller must be authorized for the process template.
Parameters:ptid - The object ID of the process template for which the descriptive information of
 the graphical representation is to be retrieved.
 
Returns:byte[] -
    The descriptive information of the graphical representation of the process template.
  If there is no the descriptive information null is returned.
 
Throws:
EngineNotAuthorizedException
ObjectDoesNotExistException
ProcessException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getMessageTextOfException
java.lang.String getMessageTextOfException(java.util.Locale locale,
                                         java.lang.String messageKey,
                                         java.lang.Object[] variableValues)
                                           throws EngineParameterNullException,
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
EngineParameterNullException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getMigrationTargets
java.util.List getMigrationTargets(java.lang.String ptid)
                                   throws ArchiveUnsupportedOperationException,
                                          EngineNotAuthorizedException,
                                          EngineProcessWrongBuildVersionException,
                                          IdWrongFormatException,
                                          IdWrongTypeException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the object IDs of all process templates that can be migration targets for
 a process instance derived from
 the process template specified by a string representation of the process template ID.
 
 In other words, it is checked whether
 there exist migration specifications so that instances of the specified process template
 can be migrated to the process templates returned.
 
 This method is not supported in archive mode.
Parameters:ptid - A string representation of the process template ID to identify the process template
    whose migration targets are to be retrieved.
 
Returns:List -
    A list of process template IDs identifying possible migration targets.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineProcessWrongBuildVersionException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.1

- getMigrationTargets
java.util.List getMigrationTargets(PTID ptid)
                                   throws ArchiveUnsupportedOperationException,
                                          EngineNotAuthorizedException,
                                          EngineProcessWrongBuildVersionException,
                                          IdWrongFormatException,
                                          ObjectDoesNotExistException,
                                          UnexpectedFailureException,
                                          java.rmi.RemoteException,
                                          javax.ejb.EJBException
Retrieves the object IDs of all process templates that can be migration targets for
 a process instance derived from
 the process template specified by the process template ID.
 
 In other words, it is checked whether
 there exist migration specifications so that instances of the specified process template
 can be migrated to the process templates returned.
 
 This method is not supported in archive mode.
Parameters:ptid - The object ID of the process template whose migration targets are to be retrieved.
 
Returns:List -
    A list of process template IDs identifying possible migration targets.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineProcessWrongBuildVersionException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.1

- getOperationMode
int getOperationMode()
                     throws java.rmi.RemoteException,
                            javax.ejb.EJBException
Indicates whether the Business Flow Manager database is used as an archive.
 
 If the Business Flow Manager database is used as an archive, then
 only reading methods can be called. All method calls that try to change the archive throw
 an ArchiveUnsupportedOperationException.
 
Returns:int -
    States whether the Business Flow Manager database is used as an archive or not.
    Refer to OperationMode for more details.
 
Throws:
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2.0.3

- getOutgoingLinks
LinkTemplateData[] getOutgoingLinks(java.lang.String aiid)
                                    throws EngineNotAuthorizedException,
                                           IdWrongFormatException,
                                           IdWrongTypeException,
                                           ObjectDoesNotExistException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Retrieves information about the links starting at the specified activity instance
 using a string representation of the activity instance object ID.
 
 Link information can be retrieved in any execution state of the activity instance.
 The caller must have at least reader authority for the activity instance,
 the associated process instance,
 or for a scope that contains the activity instance.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance for which link information is to be retrieved.
 
Returns:LinkTemplateData[] -
    The outgoing links. If there are no outgoing links,
    an empty array is returned. A link can be specified to continue navigation of
    a stopped activity - see
    forceNavigate.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getOutgoingLinks
LinkTemplateData[] getOutgoingLinks(AIID aiid)
                                    throws EngineNotAuthorizedException,
                                           IdWrongFormatException,
                                           ObjectDoesNotExistException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Retrieves information about the links starting at the specified activity instance
 using the activity instance ID.
 
 Link information can be retrieved in any execution state of the activity instance.
 The caller must have at least reader authority for the activity instance,
 the associated process instance,
 or for a scope that contains the activity instance.
Parameters:aiid - The object ID of the activity instance whose link information is to be retrieved.
 
Returns:LinkTemplateData[] -
    The outgoing links. If there are no outgoing links,
    an empty array is returned. A link can be specified to continue navigation of
    a stopped activity - see
    forceNavigate.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getOutputClientUISettings
CustomClientSettings getOutputClientUISettings(java.lang.String piid)
                                               throws EngineNotAuthorizedException,
                                                      EngineWrongKindException,
                                                      IdWrongFormatException,
                                                      IdWrongTypeException,
                                                      ObjectDoesNotExistException,
                                                      UnexpectedFailureException,
                                                      java.rmi.RemoteException,
                                                      javax.ejb.EJBException
Retrieves client interface settings for the output message of the specified
 process instance using a string representation of the process instance ID.
 
 Client interface settings allow for the specification of presentations that can
 be used by the caller to present objects and data to an end user in a specific way.
 
 Client interface settings can be retrieved in any execution state of the process instance.
 The caller must have at least reader authority for the process instance
 or be the starter of the process instance.
Parameters:piid - The string representation of the process instance object ID. This
    is used to identify the process instance whose output UI settings are to be retrieved.
 

Returns:CustomClientSettings -
    The customized client interface settings of the output message.
    Returns null if there are no customized client interface settings.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1

- getOutputClientUISettings
CustomClientSettings getOutputClientUISettings(PIID piid)
                                               throws EngineNotAuthorizedException,
                                                      EngineWrongKindException,
                                                      IdWrongFormatException,
                                                      ObjectDoesNotExistException,
                                                      UnexpectedFailureException,
                                                      java.rmi.RemoteException,
                                                      javax.ejb.EJBException
Retrieves client interface settings for the output message of the specified
 process instance using the process instance ID.
 
 Client interface settings allow for the specification of presentations that can
 be used by the caller to present objects and data to an end user in a specific way.
 
 Client interface settings can be retrieved in any execution state of the process instance.
 The caller must have at least reader authority for the process instance
 or be the starter of the process instance.
Parameters:piid - The object ID of the process instance.
 

Returns:CustomClientSettings -
    The customized client interface settings of the output message.
    Returns null if there are no customized client interface settings.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1

- getOutputMessage
ClientObjectWrapper getOutputMessage(java.lang.String identifier)
                                     throws DataHandlingException,
                                            EngineNotAuthorizedException,
                                            EngineWrongKindException,
                                            EngineWrongStateException,
                                            IdWrongFormatException,
                                            IdWrongTypeException,
                                            ObjectDoesNotExistException,
                                            UnexpectedFailureException,
                                            java.rmi.RemoteException,
                                            javax.ejb.EJBException
Retrieves the output message of the specified process or activity instance using a string representation of the ID.
 
 An output message can be retrieved in any execution state of the process instance.
 The output message can be retrieved in the claimed, expired, failed,
 finished, terminated, ready, or stopped execution state of the activity instance.
 The activity can be a request-response invoke or a human task activity.
 A human task activity is also known as staff activity.
 Note that that any saved output message of an expired, that is, non-completed
 human task activity has been deleted.
 
 The caller must have at least reader authority for the process or activity instance
 be the starter of the process instance,
 or have reader authority for a scope that contains the activity instance.
Parameters:identifier - A string representation of the process or activity instance object ID that is used
    to identify the process instance or activity instance for which the output message is to be retrieved.
 
Returns:ClientObjectWrapper -
    The output message. If the output message has not yet been created,
    a empty client object wrapper is returned.
 
Throws:
DataHandlingException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getOutputMessage
ClientObjectWrapper getOutputMessage(PIID piid)
                                     throws EngineNotAuthorizedException,
                                            EngineWrongKindException,
                                            EngineWrongStateException,
                                            IdWrongFormatException,
                                            ObjectDoesNotExistException,
                                            UnexpectedFailureException,
                                            java.rmi.RemoteException,
                                            javax.ejb.EJBException
Retrieves the output message of the specified process instance using the process instance ID.
 
 The output message can be retrieved in any execution state of the process instance.
 The caller must have at least reader authority for the process instance
 or be the starter of the process instance.
Parameters:piid - The object ID of the process instance whose output message is to be retrieved.
 
Returns:ClientObjectWrapper -
    The output message. If an output message has not yet been created,
    an empty client object wrapper is returned.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0

- getOutputMessage
ClientObjectWrapper getOutputMessage(AIID aiid)
                                     throws DataHandlingException,
                                            EngineNotAuthorizedException,
                                            EngineWrongKindException,
                                            EngineWrongStateException,
                                            IdWrongFormatException,
                                            ObjectDoesNotExistException,
                                            UnexpectedFailureException,
                                            java.rmi.RemoteException,
                                            javax.ejb.EJBException
Retrieves the output message of the specified activity instance using the activity instance ID.
 
 An output message can be retrieved in any execution state of the associated process instance.
 The output message can be retrieved in the claimed, expired, failed,
 finished, terminated, ready, or stopped execution state of the activity instance.
 The activity can be a request-response invoke or a human task activity.
 A human task activity is also known as staff activity.
 Note that that any saved output message of an expired, that is, non-completed
 human task activity has been deleted.
 
 The caller must have at least reader authority for the activity instance or for the
 associated process instance,
 or have reader authority for a scope that contains the activity instance.
Parameters:aiid - The object ID of the activity instance whose output message is to be retrieved.
 
Returns:ClientObjectWrapper -
    The output message. If the output message has not yet been created,
    an empty client object wrapper is returned.
 
Throws:
DataHandlingException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getOutputVariableNames
java.util.List getOutputVariableNames(java.lang.String piid,
                                    java.lang.String activityName)
                                      throws EngineAmbiguousActivityException,
                                             EngineNotAuthorizedException,
                                             EngineParameterNullException,
                                             EngineUnknownActivityException,
                                             EngineWrongKindException,
                                             IdWrongFormatException,
                                             IdWrongTypeException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves the names of the output variables for the specified activity
 using a string representation of the process instance ID and the activity name.
 
 The activity can be a request-response invoke or human task activity and need not be navigated.
 Note that a human task activity is also known as staff activity.
 
 If the activity is navigated,
 the caller must have at least reader authority for the activity instance, for the
 process instance, or for a scope that contains the activity instance.
 If the activity is not navigated,
 the caller must have at least reader authority for the
 process instance or for a scope that contains the activity provided that
 the scope is already navigated.
Parameters:piid - A string representation of the process instance object ID. This is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.
 
Returns:List -
    A list of output variable names. If there are no output variables, an empty list is returned.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getOutputVariableNames
java.util.List getOutputVariableNames(PIID piid,
                                    java.lang.String activityName)
                                      throws EngineAmbiguousActivityException,
                                             EngineNotAuthorizedException,
                                             EngineParameterNullException,
                                             EngineUnknownActivityException,
                                             EngineWrongKindException,
                                             IdWrongFormatException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves the names of the output variables for the specified activity
 using the process instance ID and the activity name.
 
 The activity can be a request-response invoke or human task activity and need not be navigated.
 Note that a human task activity is also known as staff activity.
 
 If the activity is navigated,
 the caller must have at least reader authority for the activity instance, for the
 process instance, or for a scope that contains the activity instance.
 If the activity is not navigated,
 the caller must have at least reader authority for the
 process instance or for a scope that contains the activity provided that
 the scope is already navigated.
Parameters:piid - The object ID of the process instance that is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.
 
Returns:List -
    A list of output variable names. If there are no output variables, an empty list is returned.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getOutputVariableNames
java.util.List getOutputVariableNames(java.lang.String identifier)
                                      throws EngineNotAuthorizedException,
                                             EngineWrongKindException,
                                             IdWrongFormatException,
                                             IdWrongTypeException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves the names of all output variables for the specified activity instance
 using a string representation of the activity instance ID.
 
 The activity can be a request-response invoke or human task activity.
 A human task activity is also known as staff activity.
 The output variable names can be retrieved in any execution state of the activity instance.
 
 The caller must have at least reader authority for the activity instance or for the
 associated process instance,
 or have reader authority for a scope that contains the activity instance.
Parameters:identifier - A string representation of the activity instance object ID. This is used
    to identify the activity instance whose output variable names are to be retrieved.
 
Returns:List -
    A list of output variable names. If there are no output variables, an empty list is returned.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getOutputVariableNames
java.util.List getOutputVariableNames(AIID aiid)
                                      throws EngineNotAuthorizedException,
                                             EngineWrongKindException,
                                             IdWrongFormatException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves the names of all output variables for the specified activity instance
 using the activity instance ID.
 
 The activity can be a request-response invoke or human task activity.
 A human task activity is also known as staff activity.
 The output variable names can be retrieved in any execution state of the activity instance.
 
 The caller must have at least reader authority for the activity instance or for the
 associated process instance,
 or have reader authority for a scope that contains the activity instance.
Parameters:aiid - The object ID of the activity instance whose output variable names are to be retrieved.
 
Returns:List -
    A list of output variable names. If there are no output variables, an empty list is returned.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getParticipatingTaskID
TKIID getParticipatingTaskID(java.lang.String aiid)
                             throws EngineNotAuthorizedException,
                                    IdWrongFormatException,
                                    IdWrongTypeException,
                                    ObjectDoesNotExistException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Retrieves the object ID of the task instance associated to the
 specified human task activity using a string representation of the activity instance ID.
 A human task activity is also known as staff activity.
 
 The human task activity instance can be in any state.
 The caller must have at least reader authority for the activity instance.
Parameters:aiid - A string representation of the activity instance ID.
 
Returns:TKIID -
    The object ID of the associated to-do task instance.
    The to-do task instance is also known as participating task instance.
    Returns null when there is no associated to-do task instance, that is,
    when the activity is no human task activity.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getParticipatingTaskID
TKIID getParticipatingTaskID(AIID aiid)
                             throws EngineNotAuthorizedException,
                                    IdWrongFormatException,
                                    ObjectDoesNotExistException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Retrieves the object ID of the task instance associated to the
 specified human task activity using the activity instance ID.
 A human task activity is also known as staff activity.
 
 The human task activity instance can be in any state.
 The caller must have at least reader authority for the activity instance.
Parameters:aiid - The object ID of the activity instance.
 
Returns:TKIID -
    The object ID of the associated to-do task instance.
    The to-do task instance is also known as participating task instance.
    Returns null when there is no associated to-do task instance, that is,
    when the activity is no human task activity.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1

- getProcessInstance
ProcessInstanceData getProcessInstance(java.lang.String identifier)
                                       throws EngineNotAuthorizedException,
                                              EngineParameterNullException,
                                              IdWrongTypeException,
                                              InvalidLengthException,
                                              ObjectDoesNotExistException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
Retrieves the specified process instance using a string representation of the process instance ID
 or the process instance name.
 
 The process instance can be in any execution state.
 The caller must have at least reader authority for the process instance
 or be the starter of the process instance.
Parameters:identifier - The string representation of the process instance object ID or the process instance
    name. This is used to identify the process instance to be retrieved.
 

Returns:ProcessInstanceData -
    The process instance.
    Refer to ProcessInstanceData to view the process instance properties.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
IdWrongTypeException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0

- getProcessInstance
ProcessInstanceData getProcessInstance(PIID piid)
                                       throws EngineNotAuthorizedException,
                                              IdWrongFormatException,
                                              InvalidLengthException,
                                              ObjectDoesNotExistException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
Retrieves the specified process instance using the process instance ID.
 
 The process instance can be in any execution state.
 The caller must have at least reader authority for the process instance
 or be the starter of the process instance.
Parameters:piid - The object ID of the process instance to be retrieved.
 

Returns:ProcessInstanceData -
    The process instance.
    Refer to ProcessInstanceData to view the process instance properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0

- getProcessTemplate
ProcessTemplateData getProcessTemplate(PTID ptid)
                                       throws EngineNotAuthorizedException,
                                              IdWrongFormatException,
                                              InvalidLengthException,
                                              ObjectDoesNotExistException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
Retrieves the specified process template using the process template ID.
 
 The caller must be authorized for the process template.
Parameters:ptid - The object ID of the process template to be retrieved.
 

Returns:ProcessTemplateData -
    The process template.
    Refer to ProcessTemplateData to view the process template properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0

- getProcessTemplate
ProcessTemplateData getProcessTemplate(java.lang.String identifier)
                                       throws EngineNotAuthorizedException,
                                              EngineParameterNullException,
                                              IdWrongTypeException,
                                              InvalidLengthException,
                                              ObjectDoesNotExistException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
Retrieves the specified process template using a string representation of the process template ID
 or the process template name. When a process template name is provided and there exists more than one
 template with this name, then the currently valid template is returned.
 
 The caller must be authorized for the process template.
Parameters:identifier - The string representation of the process template object ID or the process template
    name. This is used to identify the process template to be retrieved.
 

Returns:ProcessTemplateData -
    The process template.
    Refer to ProcessTemplateData to view the process template properties.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
IdWrongTypeException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0

- getQueryProperties
java.util.List getQueryProperties(java.lang.String identifier)
                                  throws EngineNotAuthorizedException,
                                         EngineParameterNullException,
                                         ObjectDoesNotExistException,
                                         ProcessException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Retrieves the query properties of the specified process template using
 a string representation of the process template ID
 or the process template name.
 
 Query properties in the BPEL process definition are used to declare
 which parts of a variable should be accessible with the query() API function.
 
 The caller must be authorized for the process template.
Parameters:identifier - The string representation of the process template object ID
  or the process template name
  of the process template for which the query properties
 are to be retrieved.
 
Returns:List -
    A list of query properties.
  Refer to QueryProperty to view the query properties.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
ObjectDoesNotExistException
ProcessException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getQueryProperties
java.util.List getQueryProperties(PTID ptid)
                                  throws EngineNotAuthorizedException,
                                         ObjectDoesNotExistException,
                                         ProcessException,
                                         UnexpectedFailureException,
                                         java.rmi.RemoteException,
                                         javax.ejb.EJBException
Retrieves the query properties of the specified process template using
 the process template ID.
 
 Query properties in the BPEL process definition are used to declare
 which parts of a variable should be accessible with the query() API function.
 
 The caller must be authorized for the process template.
Parameters:ptid - The object ID of the process template for which the query properties
 are to be retrieved.
 
Returns:List -
    A list of query properties.
  Refer to QueryProperty to view the query properties.
 
Throws:
EngineNotAuthorizedException
ObjectDoesNotExistException
ProcessException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getStartActivities
ActivityServiceTemplateData[] getStartActivities(java.lang.String ptid)
                                                 throws EngineNotAuthorizedException,
                                                        IdWrongFormatException,
                                                        IdWrongTypeException,
                                                        ObjectDoesNotExistException,
                                                        UnexpectedFailureException,
                                                        java.rmi.RemoteException,
                                                        javax.ejb.EJBException
Retrieves information about activities that can start a process instance from the
 specified process template
 using a string representation of the process template ID.
 
 The caller must be authorized for the process template.
 
Parameters:ptid - The string representation of the process template object ID. This
    is used to identify the process template.
 

Returns:ActivityServiceTemplateData[] -
    An array of activity service templates.
    If no information is available for the logged-on user, an empty array is returned.
    Refer to ActivityServiceTemplateData to view the properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1

- getStartActivities
ActivityServiceTemplateData[] getStartActivities(PTID ptid)
                                                 throws EngineNotAuthorizedException,
                                                        ObjectDoesNotExistException,
                                                        UnexpectedFailureException,
                                                        java.rmi.RemoteException,
                                                        javax.ejb.EJBException
Retrieves information about activities that can start a process instance from the
 specified process template using the process template ID.
 
 The caller must be authorized for the process template.
 
Parameters:ptid - The object ID of the process template.
 

Returns:ActivityServiceTemplateData[] -
    An array of activity service templates.
    If no information is available for the logged-on user, an empty array is returned.
    Refer to ActivityServiceTemplateData to view the properties.
 
Throws:
EngineNotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1

- getStoredQuery
StoredQueryData getStoredQuery(java.lang.String storedQueryName)
                               throws EngineParameterNullException,
                                      ObjectDoesNotExistException,
                                      UnexpectedFailureException,
                                      java.rmi.RemoteException,
                                      javax.ejb.EJBException
Retrieves the specified stored query definition. If a private stored query
 exists for the calling user, then the private stored query is returned; otherwise
 the public stored query with the specified name.
Parameters:storedQueryName - The name of the stored query to be retrieved -
    refer to getStoredQueryNames for the retrieval of existing stored query names.
 
Returns:StoredQueryData -
    StoredQueryData -
    The definition of the stored query retrieved - refer to StoredQueryData
    to view the stored query definition.
 
Throws:
EngineParameterNullException
ObjectDoesNotExistException
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
StoredQueryData getStoredQuery(java.lang.String userID,
                             java.lang.String storedQueryName)
                               throws EngineNotAuthorizedException,
                                      EngineParameterNullException,
                                      ObjectDoesNotExistException,
                                      UnexpectedFailureException,
                                      java.rmi.RemoteException,
                                      javax.ejb.EJBException
Retrieves the specified stored query definition for the specified user.
    You must be a business process administrator to retrieve the private stored query of a different user.
Parameters:userID - The name of the user who is the owner of the stored query. If no user is
    specified, a public stored query with the specified name is retrieved.storedQueryName - The name of the stored query to be retrieved -
    refer to getStoredQueryNames
    for the retrieval of existing stored query names.
 
Returns:StoredQueryData -
    StoredQueryData -
    The definition of the stored query retrieved - refer to StoredQueryData
    to view the stored query definition.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getStoredQuery
StoredQueryData getStoredQuery(int kind,
                             java.lang.String storedQueryName)
                               throws EngineParameterNullException,
                                      InvalidParameterValueException,
                                      ObjectDoesNotExistException,
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
 
Returns:StoredQueryData -
    StoredQueryData -
    The definition of the stored query retrieved - refer to StoredQueryData
    to view the stored query definition.
 
Throws:
EngineParameterNullException
InvalidParameterValueException
ObjectDoesNotExistException
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
Retrieves the names of stored queries persistently stored in the database.
 Both the names of public and private stored queries are returned.
 
 Refer to createStoredQuery for the creation of stored queries.
 
Returns:String[] -
    An array of stored query names. If there are no stored queries, an empty array is returned.
 
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
                                       throws EngineNotAuthorizedException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
Retrieves the names of stored queries that are persistently stored in the database
 for the specified user. Both the names of public and private stored queries are returned.
 You must be a business process administrator to retrieve informations of a different user.
 
 Refer to createStoredQuery for the
 creation of stored queries.
Parameters:userID - The name of the user who is the owner of the private stored queries whose names are to
    be retrieved together with any public names. A regular user can only specify his
    own name; a business process administrator can also specify the name of a different user.
 
Returns:String[] -
    String[] -
    An array of stored query names. If there are no stored queries, an empty
    array is returned.
 
Throws:
EngineNotAuthorizedException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getStoredQueryNames
java.lang.String[] getStoredQueryNames(int kind)
                                       throws InvalidParameterValueException,
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
InvalidParameterValueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getUsersInRole
StaffResultSet getUsersInRole(java.lang.String identifier,
                            int role)
                              throws EngineNotAuthorizedException,
                                     IdWrongFormatException,
                                     IdWrongTypeException,
                                     InvalidAssignmentReasonException,
                                     ObjectDoesNotExistException,
                                     UnexpectedFailureException,
                                     java.rmi.RemoteException,
                                     javax.ejb.EJBException
Retrieves the users that are members of the specified role for the
 specified process or activity instance using string representations of the object IDs.
Parameters:identifier - A string representation of the process or activity instance ID that is used to identify the
    process or activity instance.role - The role whose members are to be queried. Refer to the work item assignment
    reasons.
 
Returns:StaffResultSet -
    The users that are members of the specified role.
    Refer to StaffResultSet for more information.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
IdWrongTypeException
InvalidAssignmentReasonException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0.0.2

- getUsersInRole
StaffResultSet getUsersInRole(PIID piid,
                            int role)
                              throws EngineNotAuthorizedException,
                                     IdWrongFormatException,
                                     InvalidAssignmentReasonException,
                                     ObjectDoesNotExistException,
                                     UnexpectedFailureException,
                                     java.rmi.RemoteException,
                                     javax.ejb.EJBException
Retrieves the users that are members of the specified role for the
 specified process instance using the process instance ID.
Parameters:piid - The object ID of the process instance that is used to identify the
    process instance.role - The role whose members are to be queried. Refer to the work item assignment
    reasons.
 
Returns:StaffResultSet -
    The users that are members of the specified role.
    Refer to StaffResultSet for more information.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
InvalidAssignmentReasonException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0.0.2

- getUsersInRole
StaffResultSet getUsersInRole(AIID aiid,
                            int role)
                              throws EngineNotAuthorizedException,
                                     IdWrongFormatException,
                                     InvalidAssignmentReasonException,
                                     ObjectDoesNotExistException,
                                     UnexpectedFailureException,
                                     java.rmi.RemoteException,
                                     javax.ejb.EJBException
Retrieves the users that are members of the specified role for the
 specified activity instance using the activity instance ID.
Parameters:aiid - The object ID of the activity instance that is used to identify the
    activity instance.role - The role whose members are to be queried, Refer to the work item assignment
    reasons.
 
Returns:StaffResultSet -
    The users that are members of the specified role.
    Refer to StaffResultSet for more information.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
InvalidAssignmentReasonException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0.0.2

- getVariable
ClientObjectWrapper getVariable(java.lang.String piid,
                              java.lang.String activityName,
                              java.lang.String variableName)
                                throws EngineAmbiguousActivityException,
                                       EngineInitializingScopeNotReachedException,
                                       EngineNotAuthorizedException,
                                       EngineParameterNullException,
                                       EngineUnknownActivityException,
                                       EngineVariableDoesNotExistException,
                                       EngineVariableNotVisibleException,
                                       EngineWrongKindException,
                                       EngineWrongStateException,
                                       IdWrongFormatException,
                                       IdWrongTypeException,
                                       ObjectDoesNotExistException,
                                       UnexpectedFailureException,
                                       java.rmi.RemoteException,
                                       javax.ejb.EJBException
Retrieves the specified variable  visible by the specified activity
 using a string representation of the process instance ID and the activity name.
 
 Variables allow to store business data for the process instance, across activity invocations or for the activity.
 
 The activity need not be navigated.
 If the activity is navigated,
 the caller must have at least reader authority for the activity instance, for the
 process instance, or for a scope that contains the activity instance.
 If the activity is not navigated,
 the caller must have at least reader authority for the
 process instance or for a scope that contains the activity provided that
 the scope is already navigated.
Parameters:piid - A string representation of the process instance object ID. This is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.variableName - The name of the variable to be retrieved.
 
Returns:ClientObjectWrapper -
    The variable. If the specified variable is not initialized or set to null,
    an empty client object wrapper is returned.
 
Throws:
EngineAmbiguousActivityException
EngineInitializingScopeNotReachedException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineVariableDoesNotExistException
EngineVariableNotVisibleException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
7.0
 Throws an
 EngineWrongKindException when an activity is specified that is for internal use only.
 
7.0
 Throws an
 EngineWrongStateException when an activity is specified that has not been migrated as
 part of a migrated process instance.

- getVariable
ClientObjectWrapper getVariable(PIID piid,
                              java.lang.String activityName,
                              java.lang.String variableName)
                                throws EngineAmbiguousActivityException,
                                       EngineInitializingScopeNotReachedException,
                                       EngineNotAuthorizedException,
                                       EngineParameterNullException,
                                       EngineUnknownActivityException,
                                       EngineVariableDoesNotExistException,
                                       EngineVariableNotVisibleException,
                                       EngineWrongKindException,
                                       EngineWrongStateException,
                                       IdWrongFormatException,
                                       ObjectDoesNotExistException,
                                       UnexpectedFailureException,
                                       java.rmi.RemoteException,
                                       javax.ejb.EJBException
Retrieves the specified variable visible by the specified activity
 using the process instance ID and the activity name.
 
 Variables allow to store business data for the process instance, across activity invocations or for the activity.
 
 The activity need not be navigated.
 If the activity is navigated,
 the caller must have at least reader authority for the activity instance, for the
 process instance, or for a scope that contains the activity instance.
 If the activity is not navigated,
 the caller must have at least reader authority for the
 process instance or for a scope that contains the activity provided that
 the scope is already navigated.
Parameters:piid - The object ID of the process instance that is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.variableName - The name of the variable to be retrieved.
 
Returns:ClientObjectWrapper -
    The variable. If the specified variable is not initialized or set to null,
    an empty client object wrapper is returned.
 
Throws:
EngineAmbiguousActivityException
EngineInitializingScopeNotReachedException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineVariableDoesNotExistException
EngineVariableNotVisibleException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
7.0
 Throws an
 EngineWrongKindException when an activity is specified that is for internal use only.
 
7.0
 Throws an
 EngineWrongStateException when an activity is specified that has not been migrated as
 part of a migrated process instance.

- getVariable
ClientObjectWrapper getVariable(java.lang.String identifier,
                              java.lang.String variableName)
                                throws EngineNotAuthorizedException,
                                       EngineParameterNullException,
                                       EngineVariableDoesNotExistException,
                                       EngineWrongKindException,
                                       EngineWrongStateException,
                                       IdWrongFormatException,
                                       IdWrongTypeException,
                                       ObjectDoesNotExistException,
                                       UnexpectedFailureException,
                                       java.rmi.RemoteException,
                                       javax.ejb.EJBException
Retrieves the specified variable of the specified process instance
 or the specified variable visible by the specified activity instance
 using a string representation of the process or activity instance ID.
 
 Variables allow to store business data for the process, across activity invocations.
 They can be retrieved in any execution state of the process or activity instance.
 The caller must have at least reader authority for the process instance or activity instance
 or for a scope that contains the activity instance,
 or be the starter of the process instance.
Parameters:identifier - A string representation of the process instance object ID or activity instance object ID.
    This string is used to
    identify the process instance or activity instance for which the specified variable
    is to be retrieved.variableName - The name of the variable to be retrieved.
 
Returns:ClientObjectWrapper -
    The variable. If the specified variable is not initialized or set to null,
    an empty client object wrapper is returned.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
EngineVariableDoesNotExistException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getVariable
ClientObjectWrapper getVariable(PIID piid,
                              java.lang.String variableName)
                                throws EngineNotAuthorizedException,
                                       EngineParameterNullException,
                                       EngineVariableDoesNotExistException,
                                       IdWrongFormatException,
                                       ObjectDoesNotExistException,
                                       UnexpectedFailureException,
                                       java.rmi.RemoteException,
                                       javax.ejb.EJBException
Retrieves the specified variable of the specified process instance using the process instance ID.
 
 Variables allow to store business data for the process, across activity invocations.
 They can be retrieved in any execution state of the process instance.
 The caller must have at least reader authority for the process instance
 or be the starter of the process instance.
Parameters:piid - The object ID of the process instance for which the specified variable is to be retrieved.variableName - The name of the variable to be retrieved.
 
Returns:ClientObjectWrapper -
    The variable. If the specified variable is not initialized or set to null,
    an empty client object wrapper is returned.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
EngineVariableDoesNotExistException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0

- getVariable
ClientObjectWrapper getVariable(AIID aiid,
                              java.lang.String variableName)
                                throws EngineNotAuthorizedException,
                                       EngineParameterNullException,
                                       EngineVariableDoesNotExistException,
                                       EngineWrongKindException,
                                       EngineWrongStateException,
                                       IdWrongFormatException,
                                       ObjectDoesNotExistException,
                                       UnexpectedFailureException,
                                       java.rmi.RemoteException,
                                       javax.ejb.EJBException
Retrieves the specified variable visible by the specified activity instance using the activity instance ID.
 
 Variables allow to store business data for the process instance, across activity invocations or for the activity.
 They can be retrieved in any execution state of the activity instance.
 The caller must have at least reader authority for the activity instance.
 or for a scope that contains the activity instance
Parameters:aiid - The object ID of the activity instance for which the specified variable is to be retrieved.variableName - The name of the variable to be retrieved.
 
Returns:ClientObjectWrapper -
    The variable. If the specified variable is not initialized or set to null,
    an empty client object wrapper is returned.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
EngineVariableDoesNotExistException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getVariableNames
java.util.List getVariableNames(java.lang.String piid,
                              java.lang.String activityName)
                                throws EngineAmbiguousActivityException,
                                       EngineNotAuthorizedException,
                                       EngineParameterNullException,
                                       EngineUnknownActivityException,
                                       EngineWrongKindException,
                                       IdWrongFormatException,
                                       IdWrongTypeException,
                                       ObjectDoesNotExistException,
                                       UnexpectedFailureException,
                                       java.rmi.RemoteException,
                                       javax.ejb.EJBException
Retrieves the names of the variables of the specified activity
 using a string representation of the process instance ID and the activity name.
 
 The activity can be a receive, reply, throw, or pick activity.
 If a pick activity has not yet received a message, the names of
 all potential input variables are returned. If a pick activity has received a message,
 the names of the actual input variables are returned.
 
 The activity need not be navigated.
 If the activity is navigated,
 the caller must have at least reader authority for the activity instance, for the
 process instance, or for a scope that contains the activity instance.
 If the activity is not navigated,
 the caller must have at least reader authority for the
 process instance or for a scope that contains the activity provided that
 the scope is already navigated.
Parameters:piid - A string representation of the process instance object ID. This is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.
 
Returns:List -
    A list of variable names. If there are no variables, an empty list is returned.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getVariableNames
java.util.List getVariableNames(PIID piid,
                              java.lang.String activityName)
                                throws EngineAmbiguousActivityException,
                                       EngineNotAuthorizedException,
                                       EngineParameterNullException,
                                       EngineUnknownActivityException,
                                       EngineWrongKindException,
                                       IdWrongFormatException,
                                       ObjectDoesNotExistException,
                                       UnexpectedFailureException,
                                       java.rmi.RemoteException,
                                       javax.ejb.EJBException
Retrieves the names of the variables of the specified activity
 using the process instance ID and the activity name.
 
 The activity can be a receive, reply, throw, or pick activity.
 If a pick activity has not yet received a message, the names of
 all potential input variables are returned. If a pick activity has received a message,
 the names of the actual input variables are returned.
 
 The activity need not be navigated.
 If the activity is navigated,
 the caller must have at least reader authority for the activity instance, for the
 process instance, or for a scope that contains the activity instance.
 If the activity is not navigated,
 the caller must have at least reader authority for the
 process instance or for a scope that contains the activity provided that
 the scope is already navigated.
Parameters:piid - The object ID of the process instance that is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.
 
Returns:List -
    A list of variable names. If there are no variables, an empty list is returned.
 
Throws:
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineWrongKindException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2

- getVariableNames
java.util.List getVariableNames(java.lang.String identifier)
                                throws EngineNotAuthorizedException,
                                       EngineWrongKindException,
                                       EngineWrongStateException,
                                       IdWrongFormatException,
                                       IdWrongTypeException,
                                       ObjectDoesNotExistException,
                                       UnexpectedFailureException,
                                       java.rmi.RemoteException,
                                       javax.ejb.EJBException
Retrieves the names of the variables of the specified event handler template or
 activity instance using a string representation of the event handler template ID or
 activity instance ID.
 
 The activity can be a receive, reply, throw, pick, or onEvent activity.
 If a pick activity has not yet received a message, the names of
 all potential input variables are returned. If a pick activity has received a message,
 the names of the actual input variables are returned.
 
 The variable names can be retrieved in any execution state of the activity instance.
 The caller must have at least reader authority for the activity instance or for the
 associated process instance,
 or have reader authority for a scope that contains the activity instance,
 or must be authorized for the event handler template.
Parameters:identifier - A string representation of the event handler template ID or
 activity instance object ID.
 
Returns:List -
    A list of variable names. If there are no variables, an empty list is returned.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getVariableNames
java.util.List getVariableNames(AIID aiid)
                                throws EngineNotAuthorizedException,
                                       EngineWrongKindException,
                                       EngineWrongStateException,
                                       IdWrongFormatException,
                                       ObjectDoesNotExistException,
                                       UnexpectedFailureException,
                                       java.rmi.RemoteException,
                                       javax.ejb.EJBException
Retrieves the names of all variables for the specified activity instance
 using the activity instance ID.
 
 The activity can be a receive, reply, throw, or pick activity.
 If a pick activity has not yet received a message, the names of
 all potential input variables are returned. If a pick activity has received a message,
 the names of the actual input variables are returned.
 
 The variable names can be retrieved in any execution state.
 The caller must have at least reader authority for the activity instance or for the
 associated process instance,
 or have reader authority for a scope that contains the activity instance.
Parameters:aiid - The object ID of the activity instance whose variable names are to be retrieved.
 
Returns:List -
    A list of variable names. If there are no variables, an empty list is returned.
 
Throws:
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getVariableNames
java.util.List getVariableNames(EHTID ehtid)
                                throws EngineNotAuthorizedException,
                                       IdWrongFormatException,
                                       ObjectDoesNotExistException,
                                       UnexpectedFailureException,
                                       java.rmi.RemoteException,
                                       javax.ejb.EJBException
Retrieves the names of all variables for the event handler template
 using the event handler template ID.
 
 The caller must be authorized for the event handler template.
Parameters:ehtid - The object ID of the event handler template whose variable names are to be retrieved.
 
Returns:List -
    A list of variable names. If there are no variables, an empty list is returned.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2

- getWaitingActivities
ActivityServiceTemplateData[] getWaitingActivities(java.lang.String piid)
                                                   throws EngineNotAuthorizedException,
                                                          IdWrongFormatException,
                                                          IdWrongTypeException,
                                                          ObjectDoesNotExistException,
                                                          UnexpectedFailureException,
                                                          java.rmi.RemoteException,
                                                          javax.ejb.EJBException
Retrieves information about activities of a process instance,
 that are in the waiting execution state.
 The process instance is identified
 using a string representation of the process instance ID.
Parameters:piid - The string representation of the process instance object ID. This
    is used to identify the process instance.
 

Returns:ActivityServiceTemplateData[] -
    An array of activity service templates.
    If no information is available for the logged-on user, an empty array is returned.
    Refer to ActivityServiceTemplateData to view the properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getWaitingActivities
ActivityServiceTemplateData[] getWaitingActivities(PIID piid)
                                                   throws EngineNotAuthorizedException,
                                                          IdWrongFormatException,
                                                          ObjectDoesNotExistException,
                                                          UnexpectedFailureException,
                                                          java.rmi.RemoteException,
                                                          javax.ejb.EJBException
Retrieves information about activities of a process instance,
 that are in the waiting execution state.
 The process instance is identified using the process instance ID.
Parameters:piid - The object ID of the process instance.
 

Returns:ActivityServiceTemplateData[] -
    An array of activity service templates.
    If no information is available for the logged-on user, an empty array is returned.
    Refer to ActivityServiceTemplateData to view the properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- getWorkItems
WorkItemData[] getWorkItems(java.lang.String identifier)
                            throws EngineNotAuthorizedException,
                                   IdWrongFormatException,
                                   IdWrongTypeException,
                                   ObjectDoesNotExistException,
                                   UserRegistryException,
                                   WorkItemManagerException,
                                   UnexpectedFailureException,
                                   java.rmi.RemoteException,
                                   javax.ejb.EJBException
Retrieves work item assignments for the logged-on user and a process or activity instance
 using a string representation of the process or activity instance ID.
 
 The activity or process instance can be in any execution state.
 
 The caller must have at least reader authority for the process instance,
 have a work item for the activity instance,
 have reader authority for a scope that contains the activity instance,
 or be a business process administrator or monitor.
 
 Note that a business process administrator is treated like any other user, that is,
 does only see the personally owned work items.
Parameters:identifier - A string representation of the process or activity instance object ID. The string is used
    to identify the process instance or activity instance for which work item assignments
    are to be returned.
 
Returns:WorkItemData[] -
    An array of work items. If there are no work items, an empty
    array is returned. Refer
    to WorkItemData to view the work item properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UserRegistryException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getWorkItems
WorkItemData[] getWorkItems(AIID aiid)
                            throws EngineNotAuthorizedException,
                                   IdWrongFormatException,
                                   ObjectDoesNotExistException,
                                   UserRegistryException,
                                   WorkItemManagerException,
                                   UnexpectedFailureException,
                                   java.rmi.RemoteException,
                                   javax.ejb.EJBException
Retrieves work item assignments for the logged-on user and the specified activity instance
 using the activity instance ID.
 
 The activity instance can be in any execution state.
 
 The caller must have at least reader authority for the process instance,
 have a work item for the activity instance,
 have reader authority for a scope that contains the activity instance,
 or be a business process administrator or monitor.
 
 Note that a business process administrator is treated like any other user, that is,
 does only see the personally owned work items.
Parameters:aiid - The object ID of the activity instance for which work item assignments are to be returned.
 
Returns:WorkItemData[] -
    An array of work items. If there are no work items, an empty
    array is returned. Refer
    to WorkItemData to view the work item properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UserRegistryException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have reader authority for the scope that contains the activity instance.

- getWorkItems
WorkItemData[] getWorkItems(PIID piid)
                            throws EngineNotAuthorizedException,
                                   IdWrongFormatException,
                                   ObjectDoesNotExistException,
                                   UserRegistryException,
                                   WorkItemManagerException,
                                   UnexpectedFailureException,
                                   java.rmi.RemoteException,
                                   javax.ejb.EJBException
Retrieves work item assignments for the logged-on user and the specified process instance
 using the process instance ID.
 
 The process instance can be in any execution state.
 
 The caller must have reader authority for the process instance, be the process
 administrator, or be the business process administrator or monitor.
 
 Note that a business process administrator is treated like any other user, that is,
 does only see the personally owned work items.
Parameters:piid - The object ID of the process instance for which work item assignments are to be returned.
 
Returns:WorkItemData[] -
    An array of work items. If there are no work items, an empty
    array is returned. Refer
    to WorkItemData to view the work item properties.
 
Throws:
EngineNotAuthorizedException
IdWrongFormatException
ObjectDoesNotExistException
UserRegistryException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
5.1
 
 Throws an EngineNotAuthorizedException when the user is not authorized to call the method.
 
5.1
 
 Throws an ObjectDoesNotExistException when the process instance does not exist.
 
6.1
 
 A business process monitor may retrieve work items.

- getWorkList
WorkListData getWorkList(java.lang.String workListName)
                         throws UnexpectedFailureException,
                                java.rmi.RemoteException,
                                javax.ejb.EJBException
Deprecated. As of version 6.0, replaced by getStoredQuery.
Retrieves the specified worklist definition.
Parameters:workListName - The name of the worklist to be retrieved -
    refer to getWorkListNames for the retrieval of existing worklist names.
 
Returns:WorkListData -
    The definition of the worklist retrieved - refer to WorkListData
    to view the worklist definition. If
    the specified worklist is not found, a null object is returned.
 
Throws:
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0

- getWorkListActions
int[] getWorkListActions()
                         throws java.rmi.RemoteException,
                                javax.ejb.EJBException
Deprecated. As of version 6.0.2, no replacement.
 
Retrieves the actions that can be called by the logged-on user related to worklists.
Returns:int[] -
    An array of worklist actions.
    Refer to WorkListActions for the set of available actions.
 
Throws:
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0

- getWorkListNames
java.lang.String[] getWorkListNames()
                                    throws WorkItemManagerException,
                                           UnexpectedFailureException,
                                           java.rmi.RemoteException,
                                           javax.ejb.EJBException
Deprecated. As of version 6.0, replaced by getStoredQueryNames.
 
Retrieves the names of worklists persistently stored in the database.
 Refer to newWorkList for the creation of worklists.
Returns:String[] -
    An array of worklist names. If there are no worklists defined, an empty array is returned.
 
Throws:
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0

- initializeCorrelationSet
void initializeCorrelationSet(java.lang.String piid,
                            CorrelationSetInstanceData correlationSetInstance)
                              throws ArchiveUnsupportedOperationException,
                                     EngineCorrelationSetAlreadyInitializedException,
                                     EngineCorrelationSetDoesNotExistException,
                                     EngineNotAuthorizedException,
                                     EngineParameterNullException,
                                     EngineWrongStateException,
                                     IdWrongFormatException,
                                     IdWrongTypeException,
                                     InvalidLengthException,
                                     InvalidPropertyAliasTypeException,
                                     ObjectDoesNotExistException,
                                     UnexpectedFailureException,
                                     java.rmi.RemoteException,
                                     javax.ejb.EJBException
Initializes the specified correlation set instance
 using a string representation of the process instance ID.
 
 The process instance must be in the running, suspended, or failing execution state.
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - A string representation of the process instance object ID that is used to identify
    the process instance.correlationSetInstance - The correlation set instance data that is to be used - refer to CorrelationSetInstanceData.
 
Throws:
ArchiveUnsupportedOperationException
EngineCorrelationSetAlreadyInitializedException
EngineCorrelationSetDoesNotExistException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
InvalidPropertyAliasTypeException
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

- initializeCorrelationSet
void initializeCorrelationSet(PIID piid,
                            CorrelationSetInstanceData correlationSetInstance)
                              throws ArchiveUnsupportedOperationException,
                                     EngineCorrelationSetAlreadyInitializedException,
                                     EngineCorrelationSetDoesNotExistException,
                                     EngineNotAuthorizedException,
                                     EngineParameterNullException,
                                     EngineWrongStateException,
                                     IdWrongFormatException,
                                     InvalidLengthException,
                                     InvalidPropertyAliasTypeException,
                                     ObjectDoesNotExistException,
                                     UnexpectedFailureException,
                                     java.rmi.RemoteException,
                                     javax.ejb.EJBException
Initializes the specified correlation set instance
 using the process instance ID.
 
 The process instance must be in the running, suspended, or failing execution state.
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance.correlationSetInstance - The correlation set instance data that is to be used - refer to CorrelationSetInstanceData.
 
Throws:
ArchiveUnsupportedOperationException
EngineCorrelationSetAlreadyInitializedException
EngineCorrelationSetDoesNotExistException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongStateException
IdWrongFormatException
InvalidLengthException
InvalidPropertyAliasTypeException
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

- initiate
PIID initiate(java.lang.String processTemplateName,
            ClientObjectWrapper inputMessage)
              throws ArchiveUnsupportedOperationException,
                     CreateFailedException,
                     EngineAdministratorCannotBeResolvedException,
                     EngineCannotCreateWorkItemException,
                     EngineCannotInitializeVariableException,
                     EngineCannotOpenCompensationSphereException,
                     EngineCannotRunSynchronousException,
                     EngineNotAuthorizedException,
                     EngineParameterNullException,
                     EngineProcessModelDoesNotExistException,
                     EngineProcessModelStoppedException,
                     EngineWrongMessageTypeException,
                     FaultReplyException,
                     InvalidLengthException,
                     InvalidObjectNameException,
                     MissingPartsException,
                     ProcessException,
                     ProcessInstanceNotUniqueException,
                     ServiceNotUniqueException,
                     UnexpectedFailureException,
                     java.rmi.RemoteException,
                     javax.ejb.EJBException
Creates a process instance from the specified process template,
 passes the specified input message, and initiates processing of the process instance.
 
 If the process is a long running process, then
 the name of the newly created process instance is derived from its object identifier.
 The caller of this method becomes the starter of the process instance
 and receives a starter work item for the process instance.
 Readers and process administrators are determined and receive work items for the process instance.
 
 A process instance is only created when the currently valid version of the specified process template
 is started and when it belongs to a started application.
 
 This method is not supported in archive mode.
Parameters:processTemplateName - The name of the process template from which an instance is to be created. A
    process template name only can be specified when the starting service is unique, that is,
    the process starts with a single receive or pick.
    The pick activity must specify a single onMessage so that the service to be called can be identified.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The
    object wrapped by the ClientObjectWrapper must be serializable.
 

Returns:PIID -
    For long running processes, the ID of the process instance created else null.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineCannotRunSynchronousException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineWrongMessageTypeException
FaultReplyException
InvalidLengthException
InvalidObjectNameException
MissingPartsException
ProcessException
ProcessInstanceNotUniqueException
ServiceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- initiate
PIID initiate(java.lang.String processTemplateName,
            java.lang.String processInstanceName,
            ClientObjectWrapper inputMessage)
              throws ArchiveUnsupportedOperationException,
                     CreateFailedException,
                     EngineAdministratorCannotBeResolvedException,
                     EngineCannotCreateWorkItemException,
                     EngineCannotInitializeVariableException,
                     EngineCannotOpenCompensationSphereException,
                     EngineCannotRunSynchronousException,
                     EngineNotAuthorizedException,
                     EngineParameterNullException,
                     EngineProcessInstanceNameNotUniqueException,
                     EngineProcessModelDoesNotExistException,
                     EngineProcessModelStoppedException,
                     EngineWrongMessageTypeException,
                     FaultReplyException,
                     InvalidLengthException,
                     InvalidObjectNameException,
                     MissingPartsException,
                     ProcessException,
                     ProcessInstanceNotUniqueException,
                     ServiceNotUniqueException,
                     UnexpectedFailureException,
                     java.rmi.RemoteException,
                     javax.ejb.EJBException
Creates a named process instance from the specified process template,
 passes the specified input message, and initiates processing of the process instance.
 
 If the process is a long running process, then
 the caller of this method becomes the starter of the process instance
 and receives a starter work item for the process instance.
 Readers and process administrators are determined and receive work items for the process instance.
 
 A process instance is only created when the currently valid version of the specified process template
 is started and when it belongs to a started application.
 
 This method is not supported in archive mode.
Parameters:processTemplateName - The name of the process template from which an instance is to be created. A
    process template name only can be specified when the starting service is unique, that is,
    the process starts with a single receive or pick.
    The pick activity must specify a single onMessage so that the service to be called can be identified.processInstanceName - The name of the process instance to be created; must not be greater than 220
    bytes in UTF-8 format. The name must be unique. This parameter is ignored for microflows.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The
    object wrapped by the ClientObjectWrapper must be serializable.
 

Returns:PIID -
    For long running processes, the ID of the process instance created else null.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineCannotRunSynchronousException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessInstanceNameNotUniqueException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineWrongMessageTypeException
FaultReplyException
InvalidLengthException
InvalidObjectNameException
MissingPartsException
ProcessException
ProcessInstanceNotUniqueException
ServiceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- initiate
PIID initiate(java.lang.String vtid,
            java.lang.String atid,
            java.lang.String processInstanceName,
            ClientObjectWrapper inputMessage)
              throws ArchiveUnsupportedOperationException,
                     CreateFailedException,
                     EngineNotAuthorizedException,
                     EngineParameterNullException,
                     EngineProcessInstanceNameNotUniqueException,
                     EngineProcessModelDoesNotExistException,
                     EngineProcessModelStoppedException,
                     IdWrongFormatException,
                     IdWrongTypeException,
                     InvalidObjectNameException,
                     MissingPartsException,
                     NoMacroFlowException,
                     ObjectDoesNotExistException,
                     ProcessException,
                     ProcessInstanceNotUniqueException,
                     UnexpectedFailureException,
                     java.rmi.RemoteException,
                     javax.ejb.EJBException
Creates a named process instance identifying the starting service by a string representation of its ID,
 passes the specified input message, and initiates processing of the process instance.
 
 The process must be a long running process.
 The caller of this method becomes the starter of the process instance
 and receives a starter work item for the process instance.
 Readers and process administrators are determined and receive work items for the process instance.
 
 A process instance is only created when the process template containing the specified
 starting service is started and when it belongs to a started application.
 
 This method is not supported in archive mode.
Parameters:vtid - The string representation of the activity service template object ID. This
    is used to identify the starting service.atid - A string representation of the activity template ID. This is used
    to identify the activity the service belongs to.processInstanceName - The name of the process instance to be created; must not be greater than 220
    bytes in UTF-8 format. The name must be unique. This parameter is ignored for microflows.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The
    object wrapped by the ClientObjectWrapper must be serializable.
 

Returns:PIID -
    The ID of the process instance created.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessInstanceNameNotUniqueException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
IdWrongFormatException
IdWrongTypeException
InvalidObjectNameException
MissingPartsException
NoMacroFlowException
ObjectDoesNotExistException
ProcessException
ProcessInstanceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- initiate
PIID initiate(VTID vtid,
            ATID atid,
            java.lang.String processInstanceName,
            ClientObjectWrapper inputMessage)
              throws ArchiveUnsupportedOperationException,
                     CreateFailedException,
                     EngineNotAuthorizedException,
                     EngineParameterNullException,
                     EngineProcessInstanceNameNotUniqueException,
                     EngineProcessModelDoesNotExistException,
                     EngineProcessModelStoppedException,
                     IdWrongFormatException,
                     InvalidObjectNameException,
                     MissingPartsException,
                     NoMacroFlowException,
                     ObjectDoesNotExistException,
                     ProcessException,
                     ProcessInstanceNotUniqueException,
                     UnexpectedFailureException,
                     java.rmi.RemoteException,
                     javax.ejb.EJBException
Creates a named process instance identifying the starting service by its ID,
 passes the specified input message, and initiates processing of the process instance.
 
 The process must be a long running process.
 The caller of this method becomes the starter of the process instance
 and receives a starter work item for the process instance.
 Readers and process administrators are determined and receive work items for the process instance.
 
 A process instance is only created when the process template containing the specified
 starting service is started and when it belongs to a started application.
 
 This method is not supported in archive mode.
Parameters:vtid - The object ID of the activity service template. This is used to identify the starting service.atid - The object ID of the activity the activity service template belongs to.processInstanceName - The name of the process instance to be created; must not be greater than 220
    bytes in UTF-8 format. The name must be unique. This parameter is ignored for microflows.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The
    object wrapped by the ClientObjectWrapper must be serializable.
 

Returns:PIID -
    The ID of the process instance created.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessInstanceNameNotUniqueException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
IdWrongFormatException
InvalidObjectNameException
MissingPartsException
NoMacroFlowException
ObjectDoesNotExistException
ProcessException
ProcessInstanceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- initiateAndClaimFirst
InitiateAndClaimFirstResult initiateAndClaimFirst(java.lang.String processTemplateName,
                                                java.lang.String processInstanceName,
                                                ClientObjectWrapper inputMessage)
                                                  throws ArchiveUnsupportedOperationException,
                                                         CreateFailedException,
                                                         EngineAdministratorCannotBeResolvedException,
                                                         EngineCannotCreateWorkItemException,
                                                         EngineCannotInitializeVariableException,
                                                         EngineCannotOpenCompensationSphereException,
                                                         EngineNotAuthorizedException,
                                                         EngineParameterNullException,
                                                         EngineProcessInstanceNameNotUniqueException,
                                                         EngineProcessModelDoesNotExistException,
                                                         EngineProcessModelStoppedException,
                                                         EngineWrongMessageTypeException,
                                                         FaultReplyException,
                                                         InvalidLengthException,
                                                         InvalidObjectNameException,
                                                         NoMacroFlowException,
                                                         ObjectDoesNotExistException,
                                                         ProcessInstanceNotUniqueException,
                                                         ServiceNotUniqueException,
                                                         UnexpectedFailureException,
                                                         ProcessException,
                                                         java.rmi.RemoteException,
                                                         javax.ejb.EJBException
Creates a process instance from the specified process template
 and claims the first inline human task for the logged-on user.
 This method supports "single person workflow" scenarios.
 
 A human task activity is claimed when it becomes available within the same
 transaction as the creation of the process instance.
 This means that the transactional boundaries must have been set so that
 the activity to be claimed participates in the same transaction as the creation of the
 process instance.
 
 The caller must be a process administrator or a potential owner of the starting activity.
 in order to create and start the process instance.
 To claim the human task activity,
 the caller must be a potential owner of the activity, an administrator
 of the process instance, or an administrator of a scope that contains the activity.
 If no activity is claimed, the result object only contains the object ID of the process instance.
 
 The caller of this method becomes the starter of the process instance
 and receives a starter work item for the process instance.
 Readers and process administrators are determined and receive work items for the process instance.
 
 The process instance is only created when the currently valid version of the specified process template
 is started and when it belongs to a started application.
 
 The execution state of the claimed activity instance is set to claimed.
 
 When there are several activities that can be claimed, that is, there
 is more than one path that can be followed after the creation of the process instance,
 then an arbitrary activity is claimed.
 When multiple activities are claimed automatically, an arbitrary claimed activity is
 returned.
 
 Note that an activity instance may have been claimed because the associated task instance
 is requested to be claimed automatically.
 
 This method is not supported in archive mode.
Parameters:processTemplateName - The name of the process template from which an instance is to be created.
    Specifying the process template name only requires that the starting service is unique, that is,
    the process starts with a single receive or pick.
    A pick activity must specify a single onMessage so that the service to be called can be identified.processInstanceName - An optional name of the process instance to be created; must not be greater than 220
    bytes in UTF-8 format. The name must be unique.
    If no name is to be provided, null must be specified.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The
    object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:InitiateAndClaimFirstResult -
    Contains the object ID of the process instance created and information
    about the claimed activity instance, if any activity is claimed.
    Refer to InitiateAndClaimFirstResult.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessInstanceNameNotUniqueException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineWrongMessageTypeException
FaultReplyException
InvalidLengthException
InvalidObjectNameException
NoMacroFlowException
ObjectDoesNotExistException
ProcessInstanceNotUniqueException
ServiceNotUniqueException
UnexpectedFailureException
ProcessException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- initiateAndClaimFirst
InitiateAndClaimFirstResult initiateAndClaimFirst(java.lang.String processTemplateName,
                                                java.lang.String nameSpace,
                                                java.lang.String portType,
                                                java.lang.String operation,
                                                java.lang.String processInstanceName,
                                                ClientObjectWrapper inputMessage)
                                                  throws ArchiveUnsupportedOperationException,
                                                         CreateFailedException,
                                                         EngineAdministratorCannotBeResolvedException,
                                                         EngineCannotCreateWorkItemException,
                                                         EngineCannotInitializeVariableException,
                                                         EngineCannotOpenCompensationSphereException,
                                                         EngineNotAuthorizedException,
                                                         EngineParameterNullException,
                                                         EngineProcessInstanceNameNotUniqueException,
                                                         EngineProcessModelDoesNotExistException,
                                                         EngineProcessModelStoppedException,
                                                         EngineWrongMessageTypeException,
                                                         FaultReplyException,
                                                         InvalidLengthException,
                                                         InvalidObjectNameException,
                                                         NoMacroFlowException,
                                                         ObjectDoesNotExistException,
                                                         ProcessInstanceNotUniqueException,
                                                         UnexpectedFailureException,
                                                         ProcessException,
                                                         java.rmi.RemoteException,
                                                         javax.ejb.EJBException
Creates a process instance from the specified process template
 by calling the specified starting service,
 and claims the first inline human task for the logged-on user.
 This method supports "single person workflow" scenarios.
 
 A human task activity is claimed when it becomes available within the same
 transaction as the creation of the process instance.
 This means that the transactional boundaries must have been set so that
 the activity to be claimed participates in the same transaction as the creation of the
 process instance.
 
 The caller must be a process administrator or a potential owner of the starting activity.
 in order to create and start the process instance.
 To claim the human task activity,
 the caller must be a potential owner of the activity, an administrator
 of the process instance, or an administrator of a scope that contains the activity.
 If no activity is claimed, the result object only contains the object ID of the process instance.
 
 The caller of this method becomes the starter of the process instance
 and receives a starter work item for the process instance.
 Readers and process administrators are determined and receive work items for the process instance.
 
 The process instance is only created when the currently valid version of the specified process template
 is started and when it belongs to a started application.
 
 The execution state of the claimed activity instance is set to claimed.
 
 When there are several activities that can be claimed, that is, there
 is more than one path that can be followed after the creation of the process instance,
 then an arbitrary activity is claimed.
 When multiple activities are claimed automatically, an arbitrary claimed activity is
 returned.
 
 Note that an activity instance may have been claimed because the associated task instance
 is requested to be claimed automatically.
 
 This method is not supported in archive mode.
Parameters:processTemplateName - The name of the process template from which an instance is to be created.
    by calling the specified starting service.nameSpace - The namespace of the service to be called.portType - The name of the port type.operation - The operation name of the service.processInstanceName - An optional name of the process instance to be created; must not be greater than 220
    bytes in UTF-8 format. The name must be unique.
    If no name is to be provided, null must be specified.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The
    object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:InitiateAndClaimFirstResult -
    Contains the object ID of the process instance created and information
    about the claimed activity instance, if any activity is claimed.
    Refer to InitiateAndClaimFirstResult.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessInstanceNameNotUniqueException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineWrongMessageTypeException
FaultReplyException
InvalidLengthException
InvalidObjectNameException
NoMacroFlowException
ObjectDoesNotExistException
ProcessInstanceNotUniqueException
UnexpectedFailureException
ProcessException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- initiateAndClaimFirst
InitiateAndClaimFirstResult initiateAndClaimFirst(java.lang.String processTemplateName,
                                                java.lang.String vtid,
                                                java.lang.String atid,
                                                java.lang.String processInstanceName,
                                                ClientObjectWrapper inputMessage)
                                                  throws ArchiveUnsupportedOperationException,
                                                         CreateFailedException,
                                                         EngineAdministratorCannotBeResolvedException,
                                                         EngineCannotCreateWorkItemException,
                                                         EngineCannotInitializeVariableException,
                                                         EngineCannotOpenCompensationSphereException,
                                                         EngineNotAuthorizedException,
                                                         EngineParameterNullException,
                                                         EngineProcessInstanceNameNotUniqueException,
                                                         EngineProcessModelDoesNotExistException,
                                                         EngineProcessModelStoppedException,
                                                         EngineWrongMessageTypeException,
                                                         FaultReplyException,
                                                         IdWrongFormatException,
                                                         IdWrongTypeException,
                                                         InvalidLengthException,
                                                         InvalidObjectNameException,
                                                         NoMacroFlowException,
                                                         ObjectDoesNotExistException,
                                                         ProcessInstanceNotUniqueException,
                                                         UnexpectedFailureException,
                                                         ProcessException,
                                                         java.rmi.RemoteException,
                                                         javax.ejb.EJBException
Deprecated. As of version 7.5, replaced by initiateAndClaimFirst.
Creates and executes a process instance using string representations of object IDs
 identifying a starting activity service template,
 and claims the first inline human task for the logged-on user.
 This method supports "single person workflow" scenarios.
 
 A human task activity is claimed when it becomes available within the same
 transaction as the creation of the process instance.
 This means that the transactional boundaries must have been set so that
 the activity to be claimed participates in the same transaction as the creation of the
 process instance.
 
 The caller must be a process administrator or a potential owner of the starting activity.
 in order to create and start the process instance.
 To claim the human task activity,
 the caller must be a potential owner of the activity, an administrator
 of the process instance, or an administrator of a scope that contains the activity.
 If no activity is claimed, the result object only contains the object ID of the process instance.
 
 The caller of this method becomes the starter of the process instance
 and receives a starter work item for the process instance.
 Readers and process administrators are determined and receive work items for the process instance.
 
 The process instance is only created when the currently valid version of the specified process template
 is started and when it belongs to a started application.
 
 The execution state of the claimed activity instance is set to claimed.
 
 When there are several activities that can be claimed, that is, there
 is more than one path that can be followed after the creation of the process instance,
 then an arbitrary activity is claimed.
 When multiple activities are claimed automatically, an arbitrary claimed activity is
 returned.
 
 Note that an activity instance may have been claimed because the associated task instance
 is requested to be claimed automatically.
 
 This method is not supported in archive mode.
Parameters:processTemplateName - The name of the process template from which an instance is to be created.
    by calling the specified starting service.vtid - The string representation of the activity service template object ID. This
    is used to identify the service.atid - A string representation of the activity template ID. This is used
    to identify the activity the service belongs to.processInstanceName - An optional name of the process instance to be created; must not be greater than 220
    bytes in UTF-8 format. The name must be unique.
    If no name is to be provided, null must be specified.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The
    object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:InitiateAndClaimFirstResult -
    Contains the object ID of the process instance created and information
    about the claimed activity instance, if any activity is claimed.
    Refer to InitiateAndClaimFirstResult.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessInstanceNameNotUniqueException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineWrongMessageTypeException
FaultReplyException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
InvalidObjectNameException
NoMacroFlowException
ObjectDoesNotExistException
ProcessInstanceNotUniqueException
UnexpectedFailureException
ProcessException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- initiateAndClaimFirst
InitiateAndClaimFirstResult initiateAndClaimFirst(java.lang.String processTemplateName,
                                                VTID vtid,
                                                ATID atid,
                                                java.lang.String processInstanceName,
                                                ClientObjectWrapper inputMessage)
                                                  throws ArchiveUnsupportedOperationException,
                                                         CreateFailedException,
                                                         EngineAdministratorCannotBeResolvedException,
                                                         EngineCannotCreateWorkItemException,
                                                         EngineCannotInitializeVariableException,
                                                         EngineCannotOpenCompensationSphereException,
                                                         EngineNotAuthorizedException,
                                                         EngineParameterNullException,
                                                         EngineProcessInstanceNameNotUniqueException,
                                                         EngineProcessModelDoesNotExistException,
                                                         EngineProcessModelStoppedException,
                                                         EngineWrongMessageTypeException,
                                                         FaultReplyException,
                                                         IdWrongFormatException,
                                                         InvalidLengthException,
                                                         InvalidObjectNameException,
                                                         NoMacroFlowException,
                                                         ObjectDoesNotExistException,
                                                         ProcessInstanceNotUniqueException,
                                                         UnexpectedFailureException,
                                                         ProcessException,
                                                         java.rmi.RemoteException,
                                                         javax.ejb.EJBException
Deprecated. As of version 7.5, replaced by initiateAndClaimFirst.
Creates and executes a process instance using object IDs
 identifying a starting activity service template,
 and claims the first inline human task for the logged-on user.
 This method supports "single person workflow" scenarios.
 
 A human task activity is claimed when it becomes available within the same
 transaction as the creation of the process instance.
 This means that the transactional boundaries must have been set so that
 the activity to be claimed participates in the same transaction as the creation of the
 process instance.
 
 The caller must be a process administrator or a potential owner of the starting activity.
 in order to create and start the process instance.
 To claim the human task activity,
 the caller must be a potential owner of the activity, an administrator
 of the process instance, or an administrator of a scope that contains the activity.
 If no activity is claimed, the result object only contains the object ID of the process instance.
 
 The caller of this method becomes the starter of the process instance
 and receives a starter work item for the process instance.
 Readers and process administrators are determined and receive work items for the process instance.
 
 The process instance is only created when the currently valid version of the specified process template
 is started and when it belongs to a started application.
 
 The execution state of the claimed activity instance is set to claimed.
 
 When there are several activities that can be claimed, that is, there
 is more than one path that can be followed after the creation of the process instance,
 then an arbitrary activity is claimed.
 When multiple activities are claimed automatically, an arbitrary claimed activity is
 returned.
 
 Note that an activity instance may have been claimed because the associated task instance
 is requested to be claimed automatically.
 
 This method is not supported in archive mode.
Parameters:processTemplateName - The name of the process template from which an instance is to be created.
    by calling the specified starting service.vtid - The object ID of the activity service template. This is used to identify the service.atid - The object ID of the activity the activity service template belongs to.processInstanceName - An optional name of the process instance to be created; must not be greater than 220
    bytes in UTF-8 format. The name must be unique.
    If no name is to be provided, null must be specified.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The
    object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:InitiateAndClaimFirstResult -
    Contains the object ID of the process instance created and information
    about the claimed activity instance, if any activity is claimed.
    Refer to InitiateAndClaimFirstResult.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessInstanceNameNotUniqueException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineWrongMessageTypeException
FaultReplyException
IdWrongFormatException
InvalidLengthException
InvalidObjectNameException
NoMacroFlowException
ObjectDoesNotExistException
ProcessInstanceNotUniqueException
UnexpectedFailureException
ProcessException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- initiateAndClaimFirst
InitiateAndClaimFirstResult initiateAndClaimFirst(java.lang.String vtid,
                                                java.lang.String atid,
                                                java.lang.String processInstanceName,
                                                ClientObjectWrapper inputMessage)
                                                  throws ArchiveUnsupportedOperationException,
                                                         CreateFailedException,
                                                         EngineAdministratorCannotBeResolvedException,
                                                         EngineCannotCreateWorkItemException,
                                                         EngineCannotInitializeVariableException,
                                                         EngineCannotOpenCompensationSphereException,
                                                         EngineNotAuthorizedException,
                                                         EngineProcessInstanceNameNotUniqueException,
                                                         EngineProcessModelDoesNotExistException,
                                                         EngineProcessModelStoppedException,
                                                         EngineWrongMessageTypeException,
                                                         FaultReplyException,
                                                         IdWrongFormatException,
                                                         IdWrongTypeException,
                                                         InvalidLengthException,
                                                         InvalidObjectNameException,
                                                         NoMacroFlowException,
                                                         ObjectDoesNotExistException,
                                                         ProcessInstanceNotUniqueException,
                                                         UnexpectedFailureException,
                                                         ProcessException,
                                                         java.rmi.RemoteException,
                                                         javax.ejb.EJBException
Creates and executes a process instance using string representations of object IDs
 identifying a starting activity service template,
 and claims the first inline human task for the logged-on user.
 This method supports "single person workflow" scenarios.
 
 A human task activity is claimed when it becomes available within the same
 transaction as the creation of the process instance.
 This means that the transactional boundaries must have been set so that
 the activity to be claimed participates in the same transaction as the creation of the
 process instance.
 
 The caller must be a process administrator or a potential owner of the starting activity.
 in order to create and start the process instance.
 To claim the human task activity,
 the caller must be a potential owner of the activity, an administrator
 of the process instance, or an administrator of a scope that contains the activity.
 If no activity is claimed, the result object only contains the object ID of the process instance.
 
 The caller of this method becomes the starter of the process instance
 and receives a starter work item for the process instance.
 Readers and process administrators are determined and receive work items for the process instance.
 
 The process instance is only created when the process template containing the specified
 starting service is started and when it belongs to a started application.
 
 The execution state of the claimed activity instance is set to claimed.
 
 When there are several activities that can be claimed, that is, there
 is more than one path that can be followed after the creation of the process instance,
 then an arbitrary activity is claimed.
 When multiple activities are claimed automatically, an arbitrary claimed activity is
 returned.
 
 Note that an activity instance may have been claimed because the associated task instance
 is requested to be claimed automatically.
 
 This method is not supported in archive mode.
Parameters:vtid - The string representation of the activity service template object ID. This
    is used to identify the service.atid - A string representation of the activity template ID. This is used
    to identify the activity the service belongs to.processInstanceName - An optional name of the process instance to be created; must not be greater than 220
    bytes in UTF-8 format. The name must be unique.
    If no name is to be provided, null must be specified.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The
    object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:InitiateAndClaimFirstResult -
    Contains the object ID of the process instance created and information
    about the claimed activity instance, if any activity is claimed.
    Refer to InitiateAndClaimFirstResult.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineNotAuthorizedException
EngineProcessInstanceNameNotUniqueException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineWrongMessageTypeException
FaultReplyException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
InvalidObjectNameException
NoMacroFlowException
ObjectDoesNotExistException
ProcessInstanceNotUniqueException
UnexpectedFailureException
ProcessException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- initiateAndClaimFirst
InitiateAndClaimFirstResult initiateAndClaimFirst(VTID vtid,
                                                ATID atid,
                                                java.lang.String processInstanceName,
                                                ClientObjectWrapper inputMessage)
                                                  throws ArchiveUnsupportedOperationException,
                                                         CreateFailedException,
                                                         EngineAdministratorCannotBeResolvedException,
                                                         EngineCannotCreateWorkItemException,
                                                         EngineCannotInitializeVariableException,
                                                         EngineCannotOpenCompensationSphereException,
                                                         EngineNotAuthorizedException,
                                                         EngineProcessInstanceNameNotUniqueException,
                                                         EngineProcessModelDoesNotExistException,
                                                         EngineProcessModelStoppedException,
                                                         EngineWrongMessageTypeException,
                                                         FaultReplyException,
                                                         IdWrongFormatException,
                                                         InvalidLengthException,
                                                         InvalidObjectNameException,
                                                         NoMacroFlowException,
                                                         ObjectDoesNotExistException,
                                                         ProcessInstanceNotUniqueException,
                                                         UnexpectedFailureException,
                                                         ProcessException,
                                                         java.rmi.RemoteException,
                                                         javax.ejb.EJBException
Creates and executes a process instance using object IDs
 identifying a starting activity service template,
 and claims the first inline human task for the logged-on user.
 This method supports "single person workflow" scenarios.
 
 A human task activity is claimed when it becomes available within the same
 transaction as the creation of the process instance.
 This means that the transactional boundaries must have been set so that
 the activity to be claimed participates in the same transaction as the creation of the
 process instance.
 
 The caller must be a process administrator or a potential owner of the starting activity.
 in order to create and start the process instance.
 To claim the human task activity,
 the caller must be a potential owner of the activity, an administrator
 of the process instance, or an administrator of a scope that contains the activity.
 If no activity is claimed, the result object only contains the object ID of the process instance.
 
 The caller of this method becomes the starter of the process instance
 and receives a starter work item for the process instance.
 Readers and process administrators are determined and receive work items for the process instance.
 
 The process instance is only created when the process template containing the specified
 starting service is started and when it belongs to a started application.
 
 The execution state of the claimed activity instance is set to claimed.
 
 When there are several activities that can be claimed, that is, there
 is more than one path that can be followed after the creation of the process instance,
 then an arbitrary activity is claimed.
 When multiple activities are claimed automatically, an arbitrary claimed activity is
 returned.
 
 Note that an activity instance may have been claimed because the associated task instance
 is requested to be claimed automatically.
 
 This method is not supported in archive mode.
Parameters:vtid - The object ID of the activity service template. This is used to identify the service.atid - The object ID of the activity the activity service template belongs to.processInstanceName - An optional name of the process instance to be created; must not be greater than 220
    bytes in UTF-8 format. The name must be unique.
    If no name is to be provided, null must be specified.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The
    object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:InitiateAndClaimFirstResult -
    Contains the object ID of the process instance created and information
    about the claimed activity instance, if any activity is claimed.
    Refer to InitiateAndClaimFirstResult.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineNotAuthorizedException
EngineProcessInstanceNameNotUniqueException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineWrongMessageTypeException
FaultReplyException
IdWrongFormatException
InvalidLengthException
InvalidObjectNameException
NoMacroFlowException
ObjectDoesNotExistException
ProcessInstanceNotUniqueException
UnexpectedFailureException
ProcessException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- initiateAndSuspend
PIID initiateAndSuspend(java.lang.String processTemplateName,
                      java.lang.String processInstanceName,
                      ClientObjectWrapper inputMessage)
                        throws ArchiveUnsupportedOperationException,
                               CreateFailedException,
                               EngineAdministratorCannotBeResolvedException,
                               EngineCannotCreateWorkItemException,
                               EngineCannotInitializeVariableException,
                               EngineCannotOpenCompensationSphereException,
                               EngineNotAuthorizedException,
                               EngineParameterNullException,
                               EngineProcessInstanceNameNotUniqueException,
                               EngineProcessModelDoesNotExistException,
                               EngineProcessModelStoppedException,
                               EngineProcessWrongBuildVersionException,
                               EngineWrongMessageTypeException,
                               FaultReplyException,
                               InvalidLengthException,
                               InvalidObjectNameException,
                               NoMacroFlowException,
                               ObjectDoesNotExistException,
                               ProcessInstanceNotUniqueException,
                               ServiceNotUniqueException,
                               UnexpectedFailureException,
                               ProcessException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
Creates a process instance from the specified process template
 and immediately suspends navigation of the process instance.
 
 The caller must be a process administrator in order to create and suspend a process instance.
 
 The caller of this method becomes the starter of the process instance
 and receives a starter work item for the process instance.
 Readers and process administrators are determined and receive work items for the process instance.
 
 The process instance is only created when the currently valid version of the specified process template
 is started and when it belongs to a started application.
 
 The execution state of the start activity instance is set to finished.
 The execution state of the process instance is set to suspended.
 
 This method is not supported in archive mode.
Parameters:processTemplateName - The name of the process template from which an instance is to be created.
    Specifying the process template name only requires that the starting service is unique, that is,
    the process starts with a single receive or pick.
    A pick activity must specify a single onMessage so that the service to be called can be identified.processInstanceName - An optional name of the process instance to be created; must not be greater than 220
    bytes in UTF-8 format. The name must be unique.
    If no name is to be provided, null must be specified.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The
    object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:PIID -
    The ID of the process instance created.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessInstanceNameNotUniqueException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineProcessWrongBuildVersionException
EngineWrongMessageTypeException
FaultReplyException
InvalidLengthException
InvalidObjectNameException
NoMacroFlowException
ObjectDoesNotExistException
ProcessInstanceNotUniqueException
ServiceNotUniqueException
UnexpectedFailureException
ProcessException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2.0.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- initiateAndSuspend
PIID initiateAndSuspend(java.lang.String processTemplateName,
                      java.lang.String nameSpace,
                      java.lang.String portType,
                      java.lang.String operation,
                      java.lang.String processInstanceName,
                      ClientObjectWrapper inputMessage)
                        throws ArchiveUnsupportedOperationException,
                               CreateFailedException,
                               EngineAdministratorCannotBeResolvedException,
                               EngineCannotCreateWorkItemException,
                               EngineCannotInitializeVariableException,
                               EngineCannotOpenCompensationSphereException,
                               EngineNotAuthorizedException,
                               EngineParameterNullException,
                               EngineProcessInstanceNameNotUniqueException,
                               EngineProcessModelDoesNotExistException,
                               EngineProcessModelStoppedException,
                               EngineProcessWrongBuildVersionException,
                               EngineWrongMessageTypeException,
                               FaultReplyException,
                               InvalidLengthException,
                               InvalidObjectNameException,
                               NoMacroFlowException,
                               ObjectDoesNotExistException,
                               ProcessInstanceNotUniqueException,
                               UnexpectedFailureException,
                               ProcessException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
Creates a process instance from the specified process template
 by calling the specified starting service,
 and immediately suspends navigation of the process instance.
 
 The caller must be a process administrator in order to create and suspend a process instance.
 
 The caller of this method becomes the starter of the process instance
 and receives a starter work item for the process instance.
 Readers and process administrators are determined and receive work items for the process instance.
 
 The process instance is only created when the currently valid version of the specified process template
 is started and when it belongs to a started application.
 
 The execution state of the specified start activity instance is set to finished.
 The execution state of the process instance is set to suspended.
 
 This method is not supported in archive mode.
Parameters:processTemplateName - The name of the process template from which an instance is to be created
    by calling the specified starting service.nameSpace - The namespace of the service to be called.portType - The name of the port type.operation - The operation name of the service.processInstanceName - An optional name of the process instance to be created; must not be greater than 220
    bytes in UTF-8 format. The name must be unique.
    If no name is to be provided, null must be specified.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The
    object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:PIID -
    The ID of the process instance created.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessInstanceNameNotUniqueException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineProcessWrongBuildVersionException
EngineWrongMessageTypeException
FaultReplyException
InvalidLengthException
InvalidObjectNameException
NoMacroFlowException
ObjectDoesNotExistException
ProcessInstanceNotUniqueException
UnexpectedFailureException
ProcessException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2.0.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- initiateAndSuspend
PIID initiateAndSuspend(java.lang.String vtid,
                      java.lang.String atid,
                      java.lang.String processInstanceName,
                      ClientObjectWrapper inputMessage)
                        throws ArchiveUnsupportedOperationException,
                               CreateFailedException,
                               EngineAdministratorCannotBeResolvedException,
                               EngineCannotCreateWorkItemException,
                               EngineCannotInitializeVariableException,
                               EngineCannotOpenCompensationSphereException,
                               EngineNotAuthorizedException,
                               EngineParameterNullException,
                               EngineProcessInstanceNameNotUniqueException,
                               EngineProcessModelDoesNotExistException,
                               EngineProcessModelStoppedException,
                               EngineProcessWrongBuildVersionException,
                               EngineWrongMessageTypeException,
                               FaultReplyException,
                               IdWrongFormatException,
                               IdWrongTypeException,
                               InvalidLengthException,
                               InvalidObjectNameException,
                               NoMacroFlowException,
                               ObjectDoesNotExistException,
                               ProcessInstanceNotUniqueException,
                               UnexpectedFailureException,
                               ProcessException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
Creates a process instance
 by calling the specified starting service identified by string representations of its object IDs,
 and immediately suspends navigation of the process instance.
 
 The caller must be a process administrator in order to create and suspend a process instance.
 
 The caller of this method becomes the starter of the process instance
 and receives a starter work item for the process instance.
 Readers and process administrators are determined and receive work items for the process instance.
 
 A process instance is only created when the process template containing the specified
 starting service is started and when it belongs to a started application.
 
 The execution state of the start activity instance is set to finished.
 The execution state of the process instance is set to suspended.
 
 This method is not supported in archive mode.
Parameters:vtid - The string representation of the activity service template object ID. This
    is used to identify the service.atid - A string representation of the activity template ID. This is used
    to identify the activity the service belongs to.processInstanceName - An optional name of the process instance to be created; must not be greater than 220
    bytes in UTF-8 format. The name must be unique.
    If no name is to be provided, null must be specified.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The
    object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:PIID -
    The ID of the process instance created.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessInstanceNameNotUniqueException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineProcessWrongBuildVersionException
EngineWrongMessageTypeException
FaultReplyException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
InvalidObjectNameException
NoMacroFlowException
ObjectDoesNotExistException
ProcessInstanceNotUniqueException
UnexpectedFailureException
ProcessException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2.0.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- initiateAndSuspend
PIID initiateAndSuspend(VTID vtid,
                      ATID atid,
                      java.lang.String processInstanceName,
                      ClientObjectWrapper inputMessage)
                        throws ArchiveUnsupportedOperationException,
                               CreateFailedException,
                               EngineAdministratorCannotBeResolvedException,
                               EngineCannotCreateWorkItemException,
                               EngineCannotInitializeVariableException,
                               EngineCannotOpenCompensationSphereException,
                               EngineNotAuthorizedException,
                               EngineParameterNullException,
                               EngineProcessInstanceNameNotUniqueException,
                               EngineProcessModelDoesNotExistException,
                               EngineProcessModelStoppedException,
                               EngineProcessWrongBuildVersionException,
                               EngineWrongMessageTypeException,
                               FaultReplyException,
                               IdWrongFormatException,
                               InvalidLengthException,
                               InvalidObjectNameException,
                               NoMacroFlowException,
                               ObjectDoesNotExistException,
                               ProcessInstanceNotUniqueException,
                               UnexpectedFailureException,
                               ProcessException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
Creates a process instance
 by calling the specified starting service identified by its object IDs,
 and immediately suspends navigation of the process instance.
 
 The caller must be a process administrator in order to create and suspend a process instance.
 
 The caller of this method becomes the starter of the process instance
 and receives a starter work item for the process instance.
 Readers and process administrators are determined and receive work items for the process instance.
 
 A process instance is only created when the process template containing the specified
 starting service is started and when it belongs to a started application.
 
 The execution state of the start activity instance is set to finished.
 The execution state of the process instance is set to suspended.
 
 This method is not supported in archive mode.
Parameters:vtid - The object ID of the activity service template. This is used to identify the service.atid - The object ID of the activity the activity service template belongs to.processInstanceName - An optional name of the process instance to be created; must not be greater than 220
    bytes in UTF-8 format. The name must be unique.
    If no name is to be provided, null must be specified.inputMessage - The input message that specifies the initial values of the process instance. If
    input is not to be provided, null must be specified. The
    object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:PIID -
    The ID of the process instance created.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineAdministratorCannotBeResolvedException
EngineCannotCreateWorkItemException
EngineCannotInitializeVariableException
EngineCannotOpenCompensationSphereException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessInstanceNameNotUniqueException
EngineProcessModelDoesNotExistException
EngineProcessModelStoppedException
EngineProcessWrongBuildVersionException
EngineWrongMessageTypeException
FaultReplyException
IdWrongFormatException
InvalidLengthException
InvalidObjectNameException
NoMacroFlowException
ObjectDoesNotExistException
ProcessInstanceNotUniqueException
UnexpectedFailureException
ProcessException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2.0.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- isBusinessProcessAdministrator
boolean isBusinessProcessAdministrator()
                                       throws java.rmi.RemoteException,
                                              javax.ejb.EJBException
Indicates whether the logged-on user is a business process administrator (system administrator).
 
 In general, authorization is granted to persons explicitly when a process model
 is defined or implicitly, for example, by starting a process instance.
 Above that, special authority is granted to a person playing the role of a
 business process (system) administrator. A business process administrator has all priviledges.
 

Returns:boolean -
    True states that the logged-on user is a business process administrator.
    False states that the logged-on user is no business process administrator.
 
Throws:
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1

- isBusinessProcessMonitor
boolean isBusinessProcessMonitor()
                                 throws java.rmi.RemoteException,
                                        javax.ejb.EJBException
Indicates whether the logged-on user is a business process monitor
 (system monitor).
 
 In general, authorization is granted to persons explicitly when a process template is
 defined or implicitly, for example, when a process instance is started.
 Above that, special authority is granted to a person playing the role of a business process
 (system) monitor. A business process monitor has the priviledge to read all objects.
 
Returns:boolean -
    
    True states that the logged-on user is a business process monitor.
    False states that the logged-on user is no business process monitor.
 
Throws:
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0

- jump
void jump(java.lang.String aiid,
        java.lang.String targetActivityName)
          throws ArchiveUnsupportedOperationException,
                 EngineActivityMultipleJumpRequestsException,
                 EngineAmbiguousActivityException,
                 EngineNotAuthorizedException,
                 EngineParameterNullException,
                 EngineProcessWrongBuildVersionException,
                 EngineUnknownActivityException,
                 EngineUnsupportedJumpException,
                 EngineWrongKindException,
                 EngineWrongStateException,
                 IdWrongFormatException,
                 IdWrongTypeException,
                 ObjectDoesNotExistException,
                 UnexpectedFailureException,
                 java.rmi.RemoteException,
                 javax.ejb.EJBException
Jumps from an activity instance
 identified by a string representation of the activity instance ID
 to the specified target activity.
 
 The activity instance that is the source of the jump operation must be a basic activity
 in the skipped, finished, failed, or expired execution state.
 It must be the last activity that is navigated on the path
 that contains the activity.
 
 The associated process instance must be in the suspended execution state.
 When the process instance is resumed,
 navigation is continued at the specified target activity.
 
 The caller must be an administrator of the associated process instance or
 of a scope that contains the activity instance to be jumped from.
 
 The activity to jump to must be in the same cyclic flow or sequence. You can jump forwards
 or backwards. When jumping backwards within a sequence, the activity instances between the completed
 activity instance and the jumped-to activity are deleted but compensation is not triggered.
 Compensation handlers are, however, registered for scopes so that compensation may run later.
 
 If the activity to jump to is inside a forEach construct or an event handler,
 then the activity jumped to must be within the same forEach iteration or event handler instance
 as the source activity.
 
 The exit condition on the entry of the activity to jump to is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance to be jumped from.targetActivityName - The name of an activity to jump to. The activity can be a basic activity
 as well as a structured activity.
 
Throws:
ArchiveUnsupportedOperationException
EngineActivityMultipleJumpRequestsException
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessWrongBuildVersionException
EngineUnknownActivityException
EngineUnsupportedJumpException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2.0.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- jump
void jump(AIID aiid,
        java.lang.String targetActivityName)
          throws ArchiveUnsupportedOperationException,
                 EngineActivityMultipleJumpRequestsException,
                 EngineAmbiguousActivityException,
                 EngineNotAuthorizedException,
                 EngineParameterNullException,
                 EngineProcessWrongBuildVersionException,
                 EngineUnknownActivityException,
                 EngineUnsupportedJumpException,
                 EngineWrongKindException,
                 EngineWrongStateException,
                 IdWrongFormatException,
                 ObjectDoesNotExistException,
                 UnexpectedFailureException,
                 java.rmi.RemoteException,
                 javax.ejb.EJBException
Jumps from an activity instance identified by the activity instance ID
 to the specified target activity.
 
 The activity instance that is the source of the jump operation must be a basic activity
 in the skipped, finished, failed, or expired execution state.
 It must be the last activity that is navigated on the path
 that contains the activity.
 
 The associated process instance must be in the suspended execution state.
 When the process instance is resumed,
 navigation is continued at the specified target activity.
 
 The caller must be an administrator of the associated process instance or
 of a scope that contains the activity instance to be jumped from.
 
 The activity to jump to must be in the same cyclic flow or sequence. You can jump forwards
 or backwards. When jumping backwards within a sequence, the activity instances between the completed
 activity instance and the jumped-to activity are deleted but compensation is not triggered.
 Compensation handlers are, however, registered for scopes so that compensation may run later.
 
 If the activity to jump to is inside a forEach construct or an event handler,
 then the activity jumped to must be within the same forEach iteration or event handler instance
 as the completed activity.
 
 The exit condition on the entry of the activity to jump to is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID to identify the activity instance to be jumped from.targetActivityName - The name of an activity to jump to. The activity can be a basic activity
 as well as a structured activity.
 
Throws:
ArchiveUnsupportedOperationException
EngineActivityMultipleJumpRequestsException
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessWrongBuildVersionException
EngineUnknownActivityException
EngineUnsupportedJumpException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2.0.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- migrate
ProcessInstanceData migrate(java.lang.String piid,
                          java.lang.String ptid)
                            throws ApplicationNotStartedException,
                                   ArchiveUnsupportedOperationException,
                                   com.ibm.bpe.api.EngineDuplicateCorrelationSetValueException,
                                   EngineInvalidMigrationTargetException,
                                   EngineProcessCannotBeMigratedException,
                                   EngineNotAuthorizedException,
                                   EngineProcessModelStoppedException,
                                   EngineProcessTemplateDoesNotExistException,
                                   EngineProcessWrongBuildVersionException,
                                   EngineScopeInitializationFailureException,
                                   EngineWrongStateException,
                                   IdWrongFormatException,
                                   IdWrongTypeException,
                                   ObjectDoesNotExistException,
                                   UnexpectedFailureException,
                                   java.rmi.RemoteException,
                                   javax.ejb.EJBException
Migrates the process instance
 identified by a string representation of the process instance ID
 to an instance of the specified process template.
 
 The process instance must be an instance of a process template with a version 7 schema.
 It must be in the running, failing, or suspended execution state.
 
 The process template must have a later valid-from date as the process template
 the process instance is currently derived from.
 It must be started and belong to a started application.
 
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - A string representation of the process instance object ID that is
    to be migrated.ptid - A string representation of the process template object ID that identifies
    the process template the process instance is to be migrated to.
    If not specified, the currently valid process template is identified.
 
Returns:ProcessInstanceData -
    Information about the migrated process instance
    - refer to ProcessInstanceData.
 
Throws:
ApplicationNotStartedException
ArchiveUnsupportedOperationException
com.ibm.bpe.api.EngineDuplicateCorrelationSetValueException
EngineInvalidMigrationTargetException
EngineProcessCannotBeMigratedException
EngineNotAuthorizedException
EngineProcessModelStoppedException
EngineProcessTemplateDoesNotExistException
EngineProcessWrongBuildVersionException
EngineScopeInitializationFailureException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
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
 
7.0.0.3
 
 Supports migration of a process instance in the failing execution state.
 
7.5
 
 Throws an EngineDuplicateCorrelationSetValueException when correlation set values are not unique.

- migrate
ProcessInstanceData migrate(PIID piid,
                          PTID ptid)
                            throws ApplicationNotStartedException,
                                   ArchiveUnsupportedOperationException,
                                   com.ibm.bpe.api.EngineDuplicateCorrelationSetValueException,
                                   EngineInvalidMigrationTargetException,
                                   EngineProcessCannotBeMigratedException,
                                   EngineNotAuthorizedException,
                                   EngineProcessModelStoppedException,
                                   EngineProcessTemplateDoesNotExistException,
                                   EngineProcessWrongBuildVersionException,
                                   EngineScopeInitializationFailureException,
                                   EngineWrongStateException,
                                   IdWrongFormatException,
                                   ObjectDoesNotExistException,
                                   UnexpectedFailureException,
                                   java.rmi.RemoteException,
                                   javax.ejb.EJBException
Migrates the process instance
 identified by the process instance ID to an instance of the specified process template.
 
 The process instance must be an instance of a process template with a version 7 schema.
 It must be in the running, failing, or suspended execution state.
 
 The process template must have a later valid-from date as the process template
 the process instance is currently derived from.
 It must be started and belong to a started application.
 
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID to identify the process instance to be migrated.ptid - The process template object ID that identifies
    the process template the process instance is to be migrated to.
    If not specified, the currently valid process template is identified.
 
Returns:ProcessInstanceData -
    Information about the migrated process instance
    - refer to ProcessInstanceData.
 
Throws:
ApplicationNotStartedException
ArchiveUnsupportedOperationException
com.ibm.bpe.api.EngineDuplicateCorrelationSetValueException
EngineInvalidMigrationTargetException
EngineProcessCannotBeMigratedException
EngineNotAuthorizedException
EngineProcessModelStoppedException
EngineProcessTemplateDoesNotExistException
EngineProcessWrongBuildVersionException
EngineScopeInitializationFailureException
EngineWrongStateException
IdWrongFormatException
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
 
7.0.0.3
 
 Supports migration of a process instance in the failing execution state.
 
7.5
 
 Throws an EngineDuplicateCorrelationSetValueException when correlation set values are not unique.

- newWorkList void newWorkList(java.lang.String workListName, java.lang.String selectClause, java.lang.String whereClause, java.lang.String orderByClause, java.lang.Integer threshold, java.util.TimeZone timeZone) throws EngineNotAuthorizedException , InvalidLengthException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Deprecated. As of version 6.0, replaced by createStoredQuery . Creates a worklist and persistently stores it in the database. Only a business process administrator can create a worklist. A worklist represents a set of selected object properties. The number of tuples in the set can be restricted by a filter or threshold. Additionally, sort criteria can be defined that are applied on the server. The domain of the query, that is, the SQL from-clause, is determined automatically. In principle, all properties of objects are selectable for which you own a work item, or which can be transitively reached via your work item. As a rule of thumb, all objects except process templates can be reached via work items. This means that you cannot use process template properties only but that you must specify a non process template property in the select- or where-clause. Although worklist definitions are stored persistently, object properties contained in the worklist are assembled dynamically when they are queried. All worklists are publicly accessible - refer to executeWorkList for the execution of worklists. When a worklist definition needs to be updated, it must be deleted and recreated - refer to deleteWorkList for the deletion of worklists. Parameters: workListName - The name of the worklist to be created; must not be greater than 64 bytes in UTF-8 format. The name must be unique. selectClause - Describes the query result returned when the worklist is executed. It declares a list of names that identify the object properties (columns of the result) to be returned. Its syntax is an SQL select-clause. Aggregation functions like AVG(), SUM(), MIN(), and MAX() are, however, not supported. Each part of the select-clause separated by a comma must specify a property from the published views. To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the view name. For example, "ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE". To count the number of potentially qualifying tuples, use the COUNT keyword. For example, to count the number of activity instance IDs that satisfy the where-clause, specify a select-clause such as "COUNT(DISTINCT ACTIVITY.AIID)". If you use the more generic "COUNT(*)", then you must specify a where-clause so that the tuples to be counted can be determined. For example, to count all activities, specify a where-clause such as "ACTIVITY.AIID=ACTIVITY.AIID" that always evaluates to true. The QueryResultSet contains columns in the same order as specified in the selectClause. If tuples are to be counted, an int value is returned (row 1, column 1). whereClause - Specifies the search condition that is applied when the worklist is executed. Its syntax is an SQL where-clause. The following rules apply: If a filter is not to be applied, null must be specified. A whereClause must not be greater than 2048 bytes in UTF-8 format. orderByClause - Orders the result of the worklist execution by the values of the columns you identify. Its syntax is an SQL order-by-clause. Each part of the order-by-clause separated by a comma must specify a property from the published views. If you identify more that one property, the worklist execution result is ordered by the values of the first property you identify, then by the values of the second property, and so on. If sort criteria are not to be applied, null must be specified. An orderByClause must not be greater than 254 bytes in UTF-8 format. Note that sort criteria are applied on the server, that is, the locale of the server is used for sorting. threshold - The maximum number of worklist execution result tuples to be returned from the server to the client. If a threshold is not to be applied, null must be specified. timeZone - Specifies the time zone of the timestamp constants in the whereClause. If a timezone is not specified, UTC is assumed. Throws: EngineNotAuthorizedException InvalidLengthException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 5.0

#### newWorkList

```
void newWorkList(java.lang.String workListName,
               java.lang.String selectClause,
               java.lang.String whereClause,
               java.lang.String orderByClause,
               java.lang.Integer threshold,
               java.util.TimeZone timeZone)
                 throws EngineNotAuthorizedException,
                        InvalidLengthException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
```

A worklist represents a set of selected object properties. The number of tuples in the set
 can be restricted by a filter or threshold.
 Additionally, sort criteria can be defined that are applied on the server.
 
 The domain of the query, that is, the SQL from-clause, is determined automatically.
 In principle, all properties of objects are selectable for which you own a work item,
 or which can be transitively reached via your work item.
 As a rule of thumb, all objects except process templates can be reached via work items.
 This means that you cannot use process template properties only but that you
 must specify a non process template property in the select- or where-clause.
 
 Although worklist definitions are stored persistently, object properties contained in
 the worklist are assembled dynamically when they are queried. All worklists are publicly
 accessible -
 refer to executeWorkList for the execution of worklists.
 
 When a worklist definition needs to be updated, it must be deleted and recreated -
 refer to deleteWorkList for the deletion of worklists.

To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the
    view name. For example, "ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE".
    
    To count the number of potentially qualifying tuples, use the COUNT keyword.
    For example, to count the number of activity instance IDs that satisfy the
    where-clause, specify a select-clause such as "COUNT(DISTINCT ACTIVITY.AIID)".
    If you use the more generic "COUNT(*)", then you must specify a where-clause
    so that the tuples to be counted can be determined.
    For example, to count all activities,
    specify a where-clause such as "ACTIVITY.AIID=ACTIVITY.AIID" that always evaluates to true.
    
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
    instead of integer enumerations. For example, instead of specifying an activity state expression
    "ACTIVITY.STATE=2" , specify "ACTIVITY.STATE=ACTIVITY.STATE.STATE\_READY".
Duplicate apostrophes (') in comparising values. For example,
    "ACTIVITY.NAME='d''automatisation'".
    To specify a where clause that refers to properties of name-value pairs, like
    custom properties, add a one-digit suffix (0-9) to the view name.
    

    For example, to have only tuples returned where an activity custom property "prop1" has
    the value "v1" or where an activity custom property "prop2" has the value v2", the where clause
    can look like
    "ACTIVITY\_ATTRIBUTE1.NAME='prop1' AND ACTIVITY\_ATTRIBUTE1.VALUE='v1' OR
    ACTIVITY\_ATTRIBUTE2.NAME='prop2' AND ACTIVITY\_ATTRIBUTE2.VALUE = 'v2'".
    For performance reasons, you should not use more than one "OR" construct; use "IN" instead.
    

    For example, to retrieve the values of custom properties "prop1" and "prop2" of all activity instances,
    the select clause can look like
    "DISTINCT ACTIVITY.AIID, ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE" and the where-clause
    "ACTIVITY\_ATTRIBUTE1.NAME = 'prop1' AND ACTIVITY\_ATTRIBUTE2.NAME = 'prop2'".

If a filter is not to be applied, null must be specified.
    
    A whereClause must not be greater than 2048 bytes in UTF-8 format.

If you identify more that one property, the worklist execution result is ordered by the
    values of the first property you identify, then by the values of the second property,
    and so on.
    
    If sort criteria are not to be applied, null must be specified.
    
    An orderByClause must not be greater than 254 bytes in UTF-8 format.
    
    Note that sort criteria are applied on the server, that is, the locale of the
    server is used for sorting.

- query QueryResultSet query(java.lang.String selectClause, java.lang.String whereClause, java.lang.String orderByClause, java.lang.Integer threshold, java.util.TimeZone timeZone) throws WorkItemManagerException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Retrieves selected object properties persistently stored in the database. You can specify a filter or a threshold to restrict the number of tuples returned. The tuples are sorted on the server according to the specified sort criteria. Sorting on the server means that the locale of the server is used. Specify the parameters of the query, the select-, where-, and order-by-clause, using SQL based on the published process views. Execution of the query can thus be shifted to SQL and becomes portable and optimizable. Note, however, when you use a combination of the order-by-clause and threshold parameters, the tuples returned depend on your database system. For example, some database systems order all records and then return the requested number of tuples. Other database systems first take the requested number of tuples and then apply the order criteria. The domain of the query, that is, the SQL from-clause, is determined automatically. In principle, all properties of objects are selectable for which you own a work item or which can be transitively reached via your work item. As a rule of thumb, all objects except process templates can be reached via work items. This means that you cannot use process template properties only but that you must specify a non process template property in the select- or where-clause. Note that a business process administrator has special rights and can retrieve information on objects associated to other users. query thus returns the selected properties of all objects for which there are work items to the business process administrator, no matter whether there is a personally owned work item or another user's work item. If the business process administrator wants to view everything that is stored on the database, independently from the existence of a work item, he/she can use queryAll(). Parameters: selectClause - Describes the query result, that is, declares a list of names that identify the object properties (columns of the result) to be returned. Its syntax is an SQL select-clause. Aggregation functions like AVG(), SUM(), MIN(), and MAX() are not supported. Each comma separated part of the select-clause must specify a property from the published process views - see the InfoCenter for details. To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the view name. For example, "ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE". To count the number of potentially qualifying tuples, use the COUNT keyword. For example, to count the number of activity instance IDs that satisfy the where-clause, specify a select-clause such as "COUNT(DISTINCT ACTIVITY.AIID)". If you use the more generic "COUNT(*)", then you must specify a where-clause so that the tuples to be counted can be determined. For example, to count all activities, specify a where-clause such as "ACTIVITY.AIID=ACTIVITY.AIID" that always evaluates to true. The QueryResultSet contains columns in the same order as specified in the selectClause. If tuples are to be counted, an int value is returned (row 1, column 1). whereClause - The search condition to be applied to the query domain. Its syntax is an SQL where-clause. The following rules apply: If a filter is not to be applied, null must be specified. orderByClause - Sorts the query result set by the values of the columns you identify. Its syntax is an SQL order-by-clause. Each comma separated part of the order-by-clause must specify a property from the published process views - see the InfoCenter for details. If you identify more that one property, the query result set is ordered by the values of the first property you identify, then by the values of the second property, and so on. If sort criteria are not to be applied, null must be specified. Note that sort criteria are applied on the server, that is, the locale of the server is used for sorting. threshold - The maximum number of query result set tuples to be returned from the server to the client. If a threshold is not to be applied, null must be specified. timeZone - The time zone of the timestamp constants in the whereClause. If a timezone is not specified, UTC is assumed. Returns: QueryResultSet - An object containing the query result. If qualifying tuples are not found, an empty query result set is returned. Refer to QueryResultSet for information on how to analyze the query result set. Throws: WorkItemManagerException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 5.0

#### query

```
QueryResultSet query(java.lang.String selectClause,
                   java.lang.String whereClause,
                   java.lang.String orderByClause,
                   java.lang.Integer threshold,
                   java.util.TimeZone timeZone)
                     throws WorkItemManagerException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
```

You can specify a filter or a threshold to restrict the number of tuples
 returned. The tuples are sorted on the server according to the specified sort criteria.
 Sorting on the server means that the locale of the server is used.
 
 Specify the parameters of the query, the select-, where-, and order-by-clause,
 using SQL based on the published process views.
 Execution of the query can thus be shifted to SQL and becomes portable and optimizable.
 
 Note, however, when you use a combination of the order-by-clause and threshold
 parameters, the tuples returned depend on your database system.
 For example, some database systems order all records and then return the requested number of tuples.
 Other database systems first take the requested number of tuples and then apply the order criteria.
 
 The domain of the query, that is, the SQL from-clause, is determined automatically.
 In principle, all properties of objects are selectable for which you own a work item
 or which can be transitively reached via your work item.
 As a rule of thumb, all objects except process templates can be reached via work items.
 This means that you cannot use process template properties only but that you
 must specify a non process template property in the select- or where-clause.
 
 Note that a business process administrator has special rights and can retrieve
 information on objects associated to other users.
 query thus returns the selected properties of all objects for which there are
 work items to the business process administrator, no matter whether there is a personally
 owned work item or another user's work item.
 If the business process administrator wants to view everything that is stored
 on the database, independently from the existence of a work item, he/she can use queryAll().

To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the
    view name. For example, "ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE".
    
    To count the number of potentially qualifying tuples, use the COUNT keyword.
    For example, to count the number of activity instance IDs that satisfy the
    where-clause, specify a select-clause such as "COUNT(DISTINCT ACTIVITY.AIID)".
    If you use the more generic "COUNT(*)", then you must specify a where-clause
    so that the tuples to be counted can be determined.
    For example, to count all activities,
    specify a where-clause such as "ACTIVITY.AIID=ACTIVITY.AIID" that always evaluates to true.
    
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
    instead of integer enumerations. For example, instead of specifying an activity state expression
    "ACTIVITY.STATE=2" , specify "ACTIVITY.STATE=ACTIVITY.STATE.STATE\_READY".
Duplicate apostrophes (') in comparising values. For example,
    "ACTIVITY.NAME='d''automatisation'".
    To specify a where clause that refers to properties of name-value pairs, like
    custom properties, add a one-digit suffix (0-9) to the view name.
    

    For example, to have only tuples returned where an activity custom property "prop1" has
    the value "v1" or where an activity custom property "prop2" has the value v2", the where clause
    can look like
    "ACTIVITY\_ATTRIBUTE1.NAME='prop1' AND ACTIVITY\_ATTRIBUTE1.VALUE='v1' OR
    ACTIVITY\_ATTRIBUTE2.NAME='prop2' AND ACTIVITY\_ATTRIBUTE2.VALUE = 'v2'".
    For performance reasons, you should not use more than one "OR" construct; use "IN" instead.
    

    For example, to retrieve the values of custom properties "prop1" and "prop2" of all activity instances,
    the select clause can look like
    "DISTINCT ACTIVITY.AIID, ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE" and the where-clause
    "ACTIVITY\_ATTRIBUTE1.NAME = 'prop1' AND ACTIVITY\_ATTRIBUTE2.NAME = 'prop2'".

If a filter is not to be applied, null must be specified.

If you identify more that one property, the query result set is ordered by the
    values of the first property you identify, then by the values of the second property,
    and so on.
    
    If sort criteria are not to be applied, null must be specified.
    
    Note that sort criteria are applied on the server, that is, the locale of the
    server is used for sorting.

- query QueryResultSet query(java.lang.String selectClause, java.lang.String whereClause, java.lang.String orderByClause, java.lang.Integer skipTuples, java.lang.Integer threshold, java.util.TimeZone timeZone) throws WorkItemManagerException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Retrieves selected object properties persistently stored in the database and allows for retrieving a specified set of data only. You can specify a filter, a starting tuple, or a threshold to restrict the number of tuples returned. The tuples are sorted on the server according to the specified sort criteria. Sorting on the server means that the locale of the server is used. Specify the parameters of the query, the select-, where-, and order-by-clause, using SQL based on the published process views. Execution of the query can thus be shifted to SQL and becomes portable and optimizable. Note, however, when you use a combination of the order-by-clause, threshold, or skipTupels parameters, the tuples returned depend on your database system. For example, some database systems order all records and then return the requested number of tuples. Other database systems first take the requested number of tuples and then apply the order criteria. The domain of the query, that is, the SQL from-clause, is determined automatically. In principle, all properties of objects are selectable for which you own a work item or which can be transitively reached via your work item. As a rule of thumb, all objects except process templates can be reached via work items. This means that you cannot use process template properties only but that you must specify a non process template property in the select- or where-clause. Note that a business process administrator has special rights and can retrieve information on objects associated to other users. query thus returns the selected properties of all objects for which there are work items to the business process administrator, no matter whether there is a personally owned work item or another user's work item. If the business process administrator wants to view everything that is stored on the database, independently from the existence of a work item, he/she can use queryAll(). Parameters: selectClause - Describes the query result, that is, declares a list of names that identify the object properties (columns of the result) to be returned. Its syntax is an SQL select-clause. Aggregation functions like AVG(), SUM(), MIN(), and MAX() are, however, not supported. Each comma separated part of the select-clause must specify a property from the published process views - see the InfoCenter for details. To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the view name. For example, "ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE". To count the number of potentially qualifying tuples, use the COUNT keyword. For example, to count the number of activity instance IDs that satisfy the where-clause, specify a select-clause such as "COUNT(DISTINCT ACTIVITY.AIID)". If you use the more generic "COUNT(*)", then you must specify a where-clause so that the tuples to be counted can be determined. For example, to count all activities, specify a where-clause such as "ACTIVITY.AIID=ACTIVITY.AIID" that always evaluates to true. The QueryResultSet contains columns in the same order as specified in the selectClause. If tuples are to be counted, an int value is returned (row 1, column 1). whereClause - The search condition to be applied to the query domain. Its syntax is an SQL where-clause. The following rules apply: If a filter is not to be applied, null must be specified. orderByClause - Sorts the query result set by the values of the columns you identify. Its syntax is an SQL order-by-clause. Each comma separated part of the order-by-clause must specify a property from the published process views - see the InfoCenter for details. If you identify more that one property, the query result set is ordered by the values of the first property you identify, then by the values of the second property, and so on. If sort criteria are not to be applied, null must be specified. Note that sort criteria are applied on the server, that is, the locale of the server is used for sorting. skipTuples - The number of query result set tuples to be ignored and not to be returned to the caller. For example, a value of '5' means that the first 5 qualifying tuples are not returned. Use this parameter together with the threshold to implement paging in your client application. If all qualifying tuples are to be returned, null or 0 must be specified. threshold - The maximum number of query result set tuples to be returned from the server to the client. If a threshold is not to be applied, null must be specified. timeZone - The time zone of the timestamp constants in the whereClause. If a timezone is not specified, UTC is assumed. Returns: QueryResultSet - An object containing the query result. If qualifying tuples are not found, an empty query result set is returned. Refer to QueryResultSet for information on how to analyze the query result set. Throws: WorkItemManagerException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.0

#### query

```
QueryResultSet query(java.lang.String selectClause,
                   java.lang.String whereClause,
                   java.lang.String orderByClause,
                   java.lang.Integer skipTuples,
                   java.lang.Integer threshold,
                   java.util.TimeZone timeZone)
                     throws WorkItemManagerException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
```

You can specify a filter, a starting tuple, or a threshold to restrict the number of tuples
 returned. The tuples are sorted on the server according to the specified sort criteria.
 Sorting on the server means that the locale of the server is used.
 
 Specify the parameters of the query, the select-, where-, and order-by-clause,
 using SQL based on the published process views.
 Execution of the query can thus be shifted to SQL and becomes portable and optimizable.
 
 Note, however, when you use a combination of the order-by-clause, threshold, or skipTupels
 parameters, the tuples returned depend on your database system.
 For example, some database systems order all records and then return the requested number of tuples.
 Other database systems first take the requested number of tuples and then apply the order criteria.
 
 The domain of the query, that is, the SQL from-clause, is determined automatically.
 In principle, all properties of objects are selectable for which you own a work item
 or which can be transitively reached via your work item.
 As a rule of thumb, all objects except process templates can be reached via work items.
 This means that you cannot use process template properties only but that you
 must specify a non process template property in the select- or where-clause.
 
 Note that a business process administrator has special rights and can retrieve
 information on objects associated to other users.
 query thus returns the selected properties of all objects for which there are
 work items to the business process administrator, no matter whether there is a personally
 owned work item or another user's work item.
 If the business process administrator wants to view everything that is stored
 on the database, independently from the existence of a work item, he/she can use queryAll().

To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the
    view name. For example, "ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE".
    
    To count the number of potentially qualifying tuples, use the COUNT keyword.
    For example, to count the number of activity instance IDs that satisfy the
    where-clause, specify a select-clause such as "COUNT(DISTINCT ACTIVITY.AIID)".
    If you use the more generic "COUNT(*)", then you must specify a where-clause
    so that the tuples to be counted can be determined.
    For example, to count all activities,
    specify a where-clause such as "ACTIVITY.AIID=ACTIVITY.AIID" that always evaluates to true.
    
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
    instead of integer enumerations. For example, instead of specifying an activity state expression
    "ACTIVITY.STATE=2" , specify "ACTIVITY.STATE=ACTIVITY.STATE.STATE\_READY".
Duplicate apostrophes (') in comparising values. For example,
    "ACTIVITY.NAME='d''automatisation'".
    To specify a where clause that refers to properties of name-value pairs, like
    custom properties, add a one-digit suffix (0-9) to the view name.
    

    For example, to have only tuples returned where an activity custom property "prop1" has
    the value "v1" or where an activity custom property "prop2" has the value v2", the where clause
    can look like
    "ACTIVITY\_ATTRIBUTE1.NAME='prop1' AND ACTIVITY\_ATTRIBUTE1.VALUE='v1' OR
    ACTIVITY\_ATTRIBUTE2.NAME='prop2' AND ACTIVITY\_ATTRIBUTE2.VALUE = 'v2'".
    For performance reasons, you should not use more than one "OR" construct; use "IN" instead.
    

    For example, to retrieve the values of custom properties "prop1" and "prop2" of all activity instances,
    the select clause can look like
    "DISTINCT ACTIVITY.AIID, ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE" and the where-clause
    "ACTIVITY\_ATTRIBUTE1.NAME = 'prop1' AND ACTIVITY\_ATTRIBUTE2.NAME = 'prop2'".

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
                     throws EngineParameterNullException,
                            IdWrongFormatException,
                            ObjectDoesNotExistException,
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
Deprecated. As of version 6.0.2,  replaced by query(Sting storedQueryName, Integer skipTuples, List parameters),
Performs the specified stored query and returns the qualifying object properties.
 
 If a private stored query with the specified name
 exists for the calling user, then the private stored query is performed; otherwise
 the public stored query with the specified name.
 
 Only properties of objects are returned for which the logged-on user has a work item.
 Note that a business process administrator has special rights and can retrieve
 all properties of objects for which there is a user's work item.
 
 Refer to createStoredQuery for the creation of stored queries.
Parameters:storedQueryName - The name of the stored query to be executed -
    refer to getStoredQueryNames for the retrieval of existing stored query names.skipTuples - The number of query result set tuples to be ignored and not to be
    returned to the caller. For example, a value of '5' means that the first 5
    qualifying tuples are not returned. Use this parameter together with the threshold
    to implement paging in your client application.
    
    If all qualifying tuples are to be returned, null or 0 must be specified.
 
Returns:QueryResultSet -
    The qualifying object properties. If
    qualifying objects are not found, an empty query result set is returned. Refer
    to QueryResultSet
    for information on how to analyze the query result set.
 
Throws:
EngineParameterNullException
IdWrongFormatException
ObjectDoesNotExistException
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
                     throws EngineParameterNullException,
                            IdWrongFormatException,
                            InvalidStoredQueryParametersException,
                            ObjectDoesNotExistException,
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
 Note that a business process administrator has special rights and can retrieve
 all properties of objects for which there is a user's work item.
 
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
EngineParameterNullException
IdWrongFormatException
InvalidStoredQueryParametersException
ObjectDoesNotExistException
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
 
6.0.2
 
 Supports private stored queries.
 
6.1
 
 Throws a QueryCannotJoinException when views that are used cannot be joined.

- query
QueryResultSet query(java.lang.String storedQueryName,
                   java.lang.Integer skipTuples,
                   java.lang.Integer threshold)
                     throws EngineParameterNullException,
                            IdWrongFormatException,
                            ObjectDoesNotExistException,
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
Performs the specified stored query and returns the qualifying object properties
 in the specified range.
 
 If a private stored query with the specified name
 exists for the calling user, then the private stored query is performed; otherwise
 the public stored query with the specified name.
 
 Only properties of objects are returned for which the logged-on user has a work item.
 Note that a business process administrator has special rights and can retrieve
 all properties of objects for which there is a user's work item.
 
 Refer to createStoredQuery for
 the creation of stored queries.
Parameters:storedQueryName - The name of the stored query to be executed -
    refer to getStoredQueryNames for the retrieval of existing stored query names.skipTuples - The number of query result set tuples to be ignored and not to be
    returned to the caller. For example, a value of '5' means that the first 5
    qualifying tuples are not returned. Use this parameter together with the threshold
    to implement paging in your client application.
    
    If all qualifying tuples are to be returned, null or 0 must be specified.threshold - The maximum number of result set tuples to be returned from the
    server to the client.
    If the threshold is to be taken from the stored query definition, use
    query or specify null.
 
Returns:QueryResultSet -
    The qualifying object properties. If
    qualifying objects are not found, an empty query result set is returned. Refer
    to QueryResultSet
    for information on how to analyze the query result set.
 
Throws:
EngineParameterNullException
IdWrongFormatException
ObjectDoesNotExistException
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
                     throws EngineParameterNullException,
                            IdWrongFormatException,
                            InvalidStoredQueryParametersException,
                            ObjectDoesNotExistException,
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
 Note that a business process administrator has special rights and can retrieve
 all properties of objects for which there is a user's work item.
 
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
EngineParameterNullException
IdWrongFormatException
InvalidStoredQueryParametersException
ObjectDoesNotExistException
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
                     throws EngineNotAuthorizedException,
                            EngineParameterNullException,
                            IdWrongFormatException,
                            InvalidStoredQueryParametersException,
                            ObjectDoesNotExistException,
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
 Note that a business process administrator has special rights and can retrieve
 all properties of objects for which there is a user's work item.
 
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
EngineNotAuthorizedException
EngineParameterNullException
IdWrongFormatException
InvalidStoredQueryParametersException
ObjectDoesNotExistException
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
                     throws EngineParameterNullException,
                            IdWrongFormatException,
                            InvalidParameterValueException,
                            InvalidStoredQueryParametersException,
                            ObjectDoesNotExistException,
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
 Note that a business process administrator has special rights and can retrieve
 all properties of objects for which there is a user's work item.
 
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
EngineParameterNullException
IdWrongFormatException
InvalidParameterValueException
InvalidStoredQueryParametersException
ObjectDoesNotExistException
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

- queryAll QueryResultSet queryAll(java.lang.String selectClause, java.lang.String whereClause, java.lang.String orderByClause, java.lang.Integer skipTuples, java.lang.Integer threshold, java.util.TimeZone timeZone) throws EngineNotAuthorizedException , EngineParameterNullException , WorkItemManagerException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Retrieves selected object properties of all objects persistently stored in the database and allows for retrieving a specified set of data only. You can specify a filter, a starting tuple, or a threshold to restrict the number of tuples returned. The tuples are sorted on the server according to the specified sort criteria. Sorting on the server means that the locale of the server is used. Specify the parameters of the query, the select-, where-, and order-by-clause, using SQL based on the published process views. Execution of the query can thus be shifted to SQL and becomes portable and optimizable. Note, however, when you use a combination of the order-by-clause, threshold, or skipTupels parameters, the tuples returned depend on your database system. For example, some database systems order all records and then return the requested number of tuples. Other database systems first take the requested number of tuples and then apply the order criteria. The domain of the query, that is, the SQL from-clause, is determined automatically. The caller must be a business process administrator or business process monitor. Parameters: selectClause - Describes the query result, that is, declares a list of names that identify the object properties (columns of the result) to be returned. Its syntax is an SQL select-clause. Aggregation functions like AVG(), SUM(), MIN(), and MAX() are, however, not supported. Each comma separated part of the select-clause must specify a property from the published process views - see the InfoCenter for details. To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the view name. For example, "ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE". To count the number of potentially qualifying tuples, use the COUNT keyword. For example, to count the number of activity instance IDs that satisfy the where-clause, specify a select-clause such as "COUNT(DISTINCT ACTIVITY.AIID)". If you use the more generic "COUNT(*)", then you must specify a where-clause so that the tuples to be counted can be determined. For example, to count all activities, specify a where-clause such as "ACTIVITY.AIID=ACTIVITY.AIID" that always evaluates to true. The QueryResultSet contains columns in the same order as specified in the selectClause. If tuples are to be counted, an int value is returned (row 1, column 1). whereClause - The search condition to be applied to the query domain. Its syntax is an SQL where-clause. The following rules apply: If a filter is not to be applied, null must be specified. orderByClause - Sorts the query result set by the values of the columns you identify. Its syntax is an SQL order-by-clause. Each comma separated part of the order-by-clause must specify a property from the published process views - see the InfoCenter for details. If you identify more that one property, the query result set is ordered by the values of the first property you identify, then by the values of the second property, and so on. If sort criteria are not to be applied, null must be specified. Note that sort criteria are applied on the server, that is, the locale of the server is used for sorting. skipTuples - The number of query result set tuples to be ignored and not to be returned to the caller. For example, a value of '5' means that the first 5 qualifying tuples are not returned. Use this parameter together with the threshold to implement paging in your client application. If all qualifying tuples are to be returned, null or 0 must be specified. threshold - The maximum number of query result set tuples to be returned from the server to the client. If a threshold is not to be applied, null must be specified. timeZone - The time zone of the timestamp constants in the whereClause. If a timezone is not specified, UTC is assumed. Returns: QueryResultSet - An object containing the query result. If qualifying tuples are not found, an empty query result set is returned. Refer to QueryResultSet for information on how to analyze the query result set. Throws: EngineNotAuthorizedException EngineParameterNullException WorkItemManagerException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.0

#### queryAll

```
QueryResultSet queryAll(java.lang.String selectClause,
                      java.lang.String whereClause,
                      java.lang.String orderByClause,
                      java.lang.Integer skipTuples,
                      java.lang.Integer threshold,
                      java.util.TimeZone timeZone)
                        throws EngineNotAuthorizedException,
                               EngineParameterNullException,
                               WorkItemManagerException,
                               UnexpectedFailureException,
                               java.rmi.RemoteException,
                               javax.ejb.EJBException
```

You can specify a filter, a starting tuple, or a threshold to restrict the number of tuples
 returned. The tuples are sorted on the server according to the specified sort criteria.
 Sorting on the server means that the locale of the server is used.
 
 Specify the parameters of the query, the select-, where-, and order-by-clause,
 using SQL based on the published process views.
 Execution of the query can thus be shifted to SQL and becomes portable and optimizable.
 
 Note, however, when you use a combination of the order-by-clause, threshold, or skipTupels
 parameters, the tuples returned depend on your database system.
 For example, some database systems order all records and then return the requested number of tuples.
 Other database systems first take the requested number of tuples and then apply the order criteria.
 
 The domain of the query, that is, the SQL from-clause, is determined automatically.
 
 The caller must be a business process administrator or business process monitor.

To select properties of name-value pairs like custom properties, add a one-digit suffix (0-9) to the
    view name. For example, "ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE".
    
    To count the number of potentially qualifying tuples, use the COUNT keyword.
    For example, to count the number of activity instance IDs that satisfy the
    where-clause, specify a select-clause such as "COUNT(DISTINCT ACTIVITY.AIID)".
    If you use the more generic "COUNT(*)", then you must specify a where-clause
    so that the tuples to be counted can be determined.
    For example, to count all activities,
    specify a where-clause such as "ACTIVITY.AIID=ACTIVITY.AIID" that always evaluates to true.
    
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
    instead of integer enumerations. For example, instead of specifying an activity state expression
    "ACTIVITY.STATE=2" , specify "ACTIVITY.STATE=ACTIVITY.STATE.STATE\_READY".
Duplicate apostrophes (') in comparising values. For example,
    "ACTIVITY.NAME='d''automatisation'".
    To specify a where clause that refers to properties of name-value pairs, like
    custom properties, add a one-digit suffix (0-9) to the view name.
    

    For example, to have only tuples returned where an activity custom property "prop1" has
    the value "v1" or where an activity custom property "prop2" has the value v2", the where clause
    can look like
    "ACTIVITY\_ATTRIBUTE1.NAME='prop1' AND ACTIVITY\_ATTRIBUTE1.VALUE='v1' OR
    ACTIVITY\_ATTRIBUTE2.NAME='prop2' AND ACTIVITY\_ATTRIBUTE2.VALUE = 'v2'".
    For performance reasons, you should not use more than one "OR" construct; use "IN" instead.
    

    For example, to retrieve the values of custom properties "prop1" and "prop2" of all activity instances,
    the select clause can look like
    "DISTINCT ACTIVITY.AIID, ACTIVITY\_ATTRIBUTE1.VALUE, ACTIVITY\_ATTRIBUTE2.VALUE" and the where-clause
    "ACTIVITY\_ATTRIBUTE1.NAME = 'prop1' AND ACTIVITY\_ATTRIBUTE2.NAME = 'prop2'".

If a filter is not to be applied, null must be specified.

If you identify more that one property, the query result set is ordered by the
    values of the first property you identify, then by the values of the second property,
    and so on.
    
    If sort criteria are not to be applied, null must be specified.
    
    Note that sort criteria are applied on the server, that is, the locale of the
    server is used for sorting.

If all qualifying tuples are to be returned, null or 0 must be specified.

- queryProcessTemplates ProcessTemplateData [] queryProcessTemplates(java.lang.String whereClause, java.lang.String orderByClause, java.lang.Integer threshold, java.util.TimeZone timeZone) throws IdWrongFormatException , InvalidLengthException , ObjectDoesNotExistException , QueryCannotJoinException , QueryInvalidOperandException , QueryInvalidTimestampException , QueryUndefinedParameterException , QueryUnknownColumnException , QueryUnknownOperatorException , QueryUnknownTableException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Retrieves process templates persistently stored in the database. You can specify a threshold or a filter to reduce the number of process templates returned. If the number is not restricted, all process templates you are authorized to see are returned. Process templates are only returned if the enterprise application they belong to is not stopped. Process templates are sorted on the server according to the specified sort criteria. Sorting on the server means that the locale of the server is used. The parameters of the query, the where- and order-by-clause, are specified using SQL based on the PROCESS\_TEMPLATE view. Execution of the query can thus be shifted to SQL and becomes portable and optimizable. Note, however, when you use a combination of the order-by-clause and threshold parameters, the tuples returned depend on your database system. For example, some database systems order all records and then return the requested number of tuples. Other database systems first take the requested number of tuples and then apply the order criteria. Parameters: whereClause - The search condition to be applied to the set of available templates. Its syntax is an SQL where-clause. The following rules apply: If a filter is not to be applied, null must be specified. orderByClause - Sorts the qualifying process templates by the values of the columns specified. Its syntax is an SQL order-by-clause. Each comma separated part of the order-by-clause must specify a property from the PROCESS\_TEMPLATE view. If you specify more than one column, the process templates are ordered by the values of the first column specified, then by the values of the second column, and so on. If the process templates are not to be sorted, null must be specified. Note that sort criteria are applied on the server, that is, the locale of the server is used for sorting. threshold - Specifies the maximum number of process templates to be returned from the server to the client. If a threshold is not to be applied, null must be specified. timeZone - The time zone of the timestamp constants in the whereClause. If a timezone is not specified, UTC is assumed. Returns: ProcessTemplateData[] - An array of qualifying process templates. If no templates qualify, an empty array is returned. Refer to ProcessTemplateData to view the process template properties. Throws: IdWrongFormatException InvalidLengthException ObjectDoesNotExistException QueryCannotJoinException QueryInvalidOperandException QueryInvalidTimestampException QueryUndefinedParameterException QueryUnknownColumnException QueryUnknownOperatorException QueryUnknownTableException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 5.0 Change History Release Modification 6.1 Throws a QueryCannotJoinException when views that are used cannot be joined.

#### queryProcessTemplates

```
ProcessTemplateData[] queryProcessTemplates(java.lang.String whereClause,
                                          java.lang.String orderByClause,
                                          java.lang.Integer threshold,
                                          java.util.TimeZone timeZone)
                                            throws IdWrongFormatException,
                                                   InvalidLengthException,
                                                   ObjectDoesNotExistException,
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

You can specify a threshold or a filter to reduce the number of process templates returned.
 If the number is not restricted, all process templates you are authorized to see are returned.
 Process templates are only returned if the enterprise application they belong to
 is not stopped.
 
 Process templates are sorted on the server according to the specified sort criteria.
 Sorting on the server means that the locale of the server is used.
 
 The parameters of the query, the where- and order-by-clause, are
 specified using SQL based on the PROCESS\_TEMPLATE view.
 Execution of the query can thus be shifted to SQL and becomes portable and optimizable.
 
 Note, however, when you use a combination of the order-by-clause and threshold
 parameters, the tuples returned depend on your database system.
 For example, some database systems order all records and then return the requested number of tuples.
 Other database systems first take the requested number of tuples and then apply the order criteria.

    - Specify object ID constants as ID('string-rep-of-ptid').
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
    Use constants instead of integer enumerations. For example, instead of specifying
     a process template state expression "PROCESS\_TEMPLATE.STATE=2" specify
    "PROCESS\_TEMPLATE.STATE=PROCESS\_TEMPLATE.STATE.STATE\_STOPPED".
Duplicate apostrophes (') in comparising values. For example,
    "PROCESS\_TEMPLATE.NAME='d''automatisation'".

If a filter is not to be applied, null must be specified.

If you specify more than one column, the process templates are ordered by the
    values of the first column specified, then by the values of the second column,
    and so on.
    
    If the process templates are not to be sorted, null must be specified.
    
    Note that sort criteria are applied on the server, that is, the locale of the
    server is used for sorting.

Change History

Release
 Modification
 
6.1
 
 Throws a QueryCannotJoinException when views that are used cannot be joined.

- rescheduleTimer
void rescheduleTimer(java.lang.String aiid,
                   TimerSpecification timerSpecification)
                     throws ArchiveUnsupportedOperationException,
                            EngineAmbiguousOnAlarmBranchException,
                            EngineCalendarNotFoundException,
                            EngineInvalidDurationException,
                            EngineNoExpirationDefinedException,
                            EngineNotAuthorizedException,
                            EngineParameterNullException,
                            EngineSchedulerException,
                            EngineSchedulerNotFoundException,
                            EngineWrongKindException,
                            EngineWrongStateException,
                            IdWrongFormatException,
                            IdWrongTypeException,
                            ObjectDoesNotExistException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Reschedules timers of the specified active activity instance
 using a string representation of the activity instance ID and a timer specification.
 
 The activity instance must be a wait activity in the waiting execution state,
 a human task activity in the ready or claimed execution state,
 an invoke activity in the running execution state,
 or a pick activity in the waiting execution state.
 
 If there is no expiration defined for a human task or invoke activity, an EngineNoExpirationDefinedException
 is thrown.
 If the pick activity has more than one onAlarm branch, rescheduling the timer applies
 to the onAlarm branch that is currently scheduled. If no onAlarm branch is scheduled,
 an AmbigousOnAlarmBranchException is thrown.
 
 The caller must be an administrator of the process instance, of the activity instance,
 or of a scope that contains the activity instance.
 
 A new scheduler task is then set up according to the specified
 timer specification.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance ID that identifies
    the activity.timerSpecification - The timer specification - refer to TimerSpecification.
 
Throws:
ArchiveUnsupportedOperationException
EngineAmbiguousOnAlarmBranchException
EngineCalendarNotFoundException
EngineInvalidDurationException
EngineNoExpirationDefinedException
EngineNotAuthorizedException
EngineParameterNullException
EngineSchedulerException
EngineSchedulerNotFoundException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
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

- rescheduleTimer
void rescheduleTimer(AIID aiid,
                   TimerSpecification timerSpecification)
                     throws ArchiveUnsupportedOperationException,
                            EngineAmbiguousOnAlarmBranchException,
                            EngineCalendarNotFoundException,
                            EngineInvalidDurationException,
                            EngineNoExpirationDefinedException,
                            EngineNotAuthorizedException,
                            EngineParameterNullException,
                            EngineSchedulerException,
                            EngineSchedulerNotFoundException,
                            EngineWrongKindException,
                            EngineWrongStateException,
                            IdWrongFormatException,
                            ObjectDoesNotExistException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Reschedules timers of the specified active activity instance
 using the activity instance ID and a timer specification.
 
 The activity instance must be a wait activity in the waiting execution state,
 a human task activity in the ready or claimed execution state,
 an invoke activity in the running execution state,
 or a pick activity in the waiting execution state.
 
 If there is no expiration defined for a human task or invoke activity, an EngineNoExpirationDefinedException
 is thrown.
 If the pick activity has more than one onAlarm branch, rescheduling the timer applies
 to the onAlarm branch that is currently scheduled. If no onAlarm branch is scheduled,
 an AmbigousOnAlarmBranchException is thrown.
 
 The caller must be an administrator of the process instance, of the activity instance,
 or of a scope that contains the activity instance.
 
 A new scheduler task is then set up according to the specified
 timer specification.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID of the activity instance.timerSpecification - The timer specification - refer to TimerSpecification.
 
Throws:
ArchiveUnsupportedOperationException
EngineAmbiguousOnAlarmBranchException
EngineCalendarNotFoundException
EngineInvalidDurationException
EngineNoExpirationDefinedException
EngineNotAuthorizedException
EngineParameterNullException
EngineSchedulerException
EngineSchedulerNotFoundException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
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

- restart
void restart(PIID piid)
             throws ArchiveUnsupportedOperationException,
                    EngineNotAuthorizedException,
                    EngineProcessModelStoppedException,
                    EngineWrongKindException,
                    EngineWrongStateException,
                    IdWrongFormatException,
                    ObjectDoesNotExistException,
                    UnexpectedFailureException,
                    ProcessException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Restarts the specified top-level process instance and its non-autonomous subprocesses
 using the process instance ID.
 
 The process instance must be in the finished, terminated, compensated, or failed execution state.
 A process instance may only be restarted, if the corresponding schema version of
 the process template is at least 6.0.
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance to be restarted.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineProcessModelStoppedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
ProcessException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- restart
void restart(java.lang.String piid)
             throws ArchiveUnsupportedOperationException,
                    EngineNotAuthorizedException,
                    EngineProcessModelStoppedException,
                    EngineWrongKindException,
                    EngineWrongStateException,
                    IdWrongFormatException,
                    IdWrongTypeException,
                    ObjectDoesNotExistException,
                    UnexpectedFailureException,
                    ProcessException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Restarts the specified top-level process instance and its non-autonomous subprocesses
 using the process instance ID.
 
 The process instance must be in the finished, terminated, compensated, or failed execution state.
 A process instance may only be restarted, if the corresponding schema version of
 the process template is at least 6.0.
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - A string representation of the process instance object ID that is used to identify
    the process instance to be restarted.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineProcessModelStoppedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
ProcessException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- resume
void resume(PIID piid)
            throws ArchiveUnsupportedOperationException,
                   EngineNotAuthorizedException,
                   EngineWrongKindException,
                   EngineWrongStateException,
                   IdWrongFormatException,
                   ObjectDoesNotExistException,
                   UnexpectedFailureException,
                   java.rmi.RemoteException,
                   javax.ejb.EJBException
Resumes the specified top-level process instance and its non-autonomous
 subprocesses using the process instance ID.
 
 The process instance must be in the suspended execution state.
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance to be resumed.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
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
void resume(java.lang.String piid)
            throws ArchiveUnsupportedOperationException,
                   EngineNotAuthorizedException,
                   EngineWrongKindException,
                   EngineWrongStateException,
                   IdWrongFormatException,
                   IdWrongTypeException,
                   ObjectDoesNotExistException,
                   UnexpectedFailureException,
                   java.rmi.RemoteException,
                   javax.ejb.EJBException
Resumes the specified top-level process instance and its non-autonomous
 subprocesses using a string representation of the process instance ID.
 
 The process instance must be in the suspended execution state.
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - A string representation of the process instance object ID that is used to identify
    the process instance to be resumed.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- sendMessage
PIID sendMessage(java.lang.String vtid,
               java.lang.String atid,
               ClientObjectWrapper message)
                 throws ArchiveUnsupportedOperationException,
                        CreateFailedException,
                        EngineNotAuthorizedException,
                        EngineProcessModelStoppedException,
                        FaultReplyException,
                        IdWrongFormatException,
                        IdWrongTypeException,
                        MissingPartsException,
                        ObjectDoesNotExistException,
                        ProcessException,
                        ProcessInstanceNotUniqueException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Sends the specified message to the specified activity service
 using a string representation of the activity service template ID and the activity template ID.
 The process instance that contains the activity service to be called is identified
 by the correlation set values contained in the message. If the process instance does
 not yet exist and the messsage is send to a starting receive or pick activity,
 then the process instance is automatically created.
 
 A process instance is only created when the process template containing the specified
 starting service is started and when it belongs to a started application.
 
 The caller must be a potential owner of the associated activity or a process administrator.
 
 This method is not supported in archive mode.
Parameters:vtid - The string representation of the activity service template object ID. This
    is used to identify the service.atid - A string representation of the activity template ID. This is used
    to identify the activity the service belongs to.message - The message. The object wrapped by the ClientObjectWrapper must be serializable.
 

Returns:PIID -
    The ID of the process instance created or identified.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineNotAuthorizedException
EngineProcessModelStoppedException
FaultReplyException
IdWrongFormatException
IdWrongTypeException
MissingPartsException
ObjectDoesNotExistException
ProcessException
ProcessInstanceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- sendMessage
PIID sendMessage(VTID vtid,
               ATID atid,
               ClientObjectWrapper message)
                 throws ArchiveUnsupportedOperationException,
                        CreateFailedException,
                        EngineNotAuthorizedException,
                        EngineProcessModelStoppedException,
                        FaultReplyException,
                        IdWrongFormatException,
                        MissingPartsException,
                        ObjectDoesNotExistException,
                        ProcessException,
                        ProcessInstanceNotUniqueException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Sends the specified message to the specified activity service using the activity service template ID
 and the activity template ID.
 The process instance that contains the activity service to be called is identified
 by the correlation set values contained in the message. If the process instance does
 not yet exist and the messsage is send to a starting receive or pick activity,
 then the process instance is automatically created.
 
 A process instance is only created when the process template containing the specified
 starting service is started and when it belongs to a started application.
 
 The caller must be a potential owner of the associated activity or a process administrator.
 
 This method is not supported in archive mode.
Parameters:vtid - The object ID of the activity service template. This is used to identify the service.atid - The object ID of the activity the activity service template belongs to.message - The message. The object wrapped by the ClientObjectWrapper must be serializable.
 

Returns:PIID -
    The ID of the process instance created or identified.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineNotAuthorizedException
EngineProcessModelStoppedException
FaultReplyException
IdWrongFormatException
MissingPartsException
ObjectDoesNotExistException
ProcessException
ProcessInstanceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- sendMessage
void sendMessage(java.lang.String piid,
               java.lang.String vtid,
               java.lang.String atid,
               ClientObjectWrapper message)
                 throws ArchiveUnsupportedOperationException,
                        EngineNotAuthorizedException,
                        IdAndCorrelationSetMismatchException,
                        IdWrongFormatException,
                        IdWrongTypeException,
                        MissingPartsException,
                        ObjectDoesNotExistException,
                        ProcessException,
                        ProcessInstanceNotUniqueException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Sends the specified message to the specified activity service and process instance
 using a string representation of the process instance, activity service template,
 and activity template IDs.
 The process instance identified by the object ID must be the same process instance
 that is identified by the correlation set values in the message.
 
 The caller must be a potential owner of the associated activity or a process administrator.
 
 This method is not supported in archive mode.
Parameters:piid - The string representation of the process instance object ID. This
    is used to identify the process instance.vtid - The string representation of the activity service template object ID. This
    is used to identify the service.atid - A string representation of the activity template ID. This is used
    to identify the activity the service belongs to.message - The message. The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
IdAndCorrelationSetMismatchException
IdWrongFormatException
IdWrongTypeException
MissingPartsException
ObjectDoesNotExistException
ProcessException
ProcessInstanceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- sendMessage
void sendMessage(PIID piid,
               VTID vtid,
               ATID atid,
               ClientObjectWrapper message)
                 throws ArchiveUnsupportedOperationException,
                        EngineNotAuthorizedException,
                        IdAndCorrelationSetMismatchException,
                        IdWrongFormatException,
                        MissingPartsException,
                        ObjectDoesNotExistException,
                        ProcessException,
                        ProcessInstanceNotUniqueException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Sends the specified message to the specified activity service and process instance
 using the process instance, activity service template, and activity template IDs.
 The process instance identified by the object ID must be the same process instance
 that is identified by the correlation set values in the message.
 
 The caller must be a potential owner of the associated activity or a process administrator.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance, a message is to be send to.vtid - The object ID of the activity service template. This is used to identify the service.atid - The object ID of the activity the activity service template belongs to.message - The message. The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
IdAndCorrelationSetMismatchException
IdWrongFormatException
MissingPartsException
ObjectDoesNotExistException
ProcessException
ProcessInstanceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- sendMessage
PIID sendMessage(java.lang.String processTemplateName,
               java.lang.String nameSpace,
               java.lang.String portType,
               java.lang.String operation,
               ClientObjectWrapper message)
                 throws ArchiveUnsupportedOperationException,
                        CreateFailedException,
                        EngineNotAuthorizedException,
                        EngineParameterNullException,
                        EngineProcessModelStoppedException,
                        FaultReplyException,
                        IdAndCorrelationSetMismatchException,
                        IdWrongFormatException,
                        IdWrongTypeException,
                        MissingPartsException,
                        ObjectDoesNotExistException,
                        ProcessException,
                        ProcessInstanceNotUniqueException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Sends the specified message to the specified process template using
 the namespace, port type, and operation of the service to be called.
 
 The process template is identified by its name or by the string representation of its object ID.
 
 This method is not supported in archive mode.
Parameters:processTemplateName - The name or the object ID of a process template, a message is to be send to.nameSpace - The namespace of the service to be called.portType - The name of the port type.operation - The operation name of the service.message - The message. The object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:PIID -
    The ID of the process instance created or identified.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessModelStoppedException
FaultReplyException
IdAndCorrelationSetMismatchException
IdWrongFormatException
IdWrongTypeException
MissingPartsException
ObjectDoesNotExistException
ProcessException
ProcessInstanceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.5.1
 
 Allows for the specification of the process template ID instead of the process template name
 in order to support early binding besides late binding. Can throw an IdWrongTypeException.

- sendMessage
PIID sendMessage(PTID ptid,
               java.lang.String nameSpace,
               java.lang.String portType,
               java.lang.String operation,
               ClientObjectWrapper message)
                 throws ArchiveUnsupportedOperationException,
                        CreateFailedException,
                        EngineNotAuthorizedException,
                        EngineParameterNullException,
                        EngineProcessModelStoppedException,
                        FaultReplyException,
                        IdAndCorrelationSetMismatchException,
                        IdWrongFormatException,
                        MissingPartsException,
                        ObjectDoesNotExistException,
                        ProcessException,
                        ProcessInstanceNotUniqueException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Sends the specified message to the specified process template using the process template ID and
 the namespace, port type, and operation of the service to be called.
 
 This method is not supported in archive mode.
Parameters:ptid - The object ID of a process template, a message is to be send to.nameSpace - The namespace of the service to be called.portType - The name of the port type.operation - The operation name of the service.message - The message. The object wrapped by the ClientObjectWrapper must be serializable.
 
Returns:PIID -
    The ID of the process instance created or identified.
 
Throws:
ArchiveUnsupportedOperationException
CreateFailedException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessModelStoppedException
FaultReplyException
IdAndCorrelationSetMismatchException
IdWrongFormatException
MissingPartsException
ObjectDoesNotExistException
ProcessException
ProcessInstanceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- sendMessage
void sendMessage(java.lang.String processTemplateName,
               java.lang.String nameSpace,
               java.lang.String portType,
               java.lang.String operation,
               ClientObjectWrapper message,
               ReplyContextWrapper replyContext)
                 throws ArchiveUnsupportedOperationException,
                        EngineNotAuthorizedException,
                        EngineParameterNullException,
                        IdAndCorrelationSetMismatchException,
                        IdWrongFormatException,
                        MissingPartsException,
                        ObjectDoesNotExistException,
                        ProcessException,
                        ProcessInstanceNotUniqueException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Sends the specified message to the specified process template, using
 the namespace, port type, and operation of the service to be called and returns the
 result of operation.
 
 The process template is identified by its name.
 
 This method is not supported in archive mode.
Parameters:processTemplateName - The name of a process template, a message is to be send to.nameSpace - The namespace of the service to be called.portType - The name of the port type.operation - The operation name of the service.message - The message. The object wrapped by the ClientObjectWrapper must be serializable.replyContext - The reply context that is to be used to send the result back to the caller.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
IdAndCorrelationSetMismatchException
IdWrongFormatException
MissingPartsException
ObjectDoesNotExistException
ProcessException
ProcessInstanceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- sendMessage
void sendMessage(java.lang.String processTemplateName,
               java.lang.String nameSpace,
               java.lang.String portType,
               java.lang.String operation,
               ClientObjectWrapper message,
               ReplyContextWrapper replyContext,
               int invocationCount,
               java.lang.String requestId)
                 throws ArchiveUnsupportedOperationException,
                        EngineNotAuthorizedException,
                        EngineParameterNullException,
                        IdAndCorrelationSetMismatchException,
                        IdWrongFormatException,
                        MissingPartsException,
                        ObjectDoesNotExistException,
                        ProcessException,
                        ProcessInstanceNotUniqueException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Sends the specified message to the specified process template, using
 the namespace, port type, and operation of the service to be called and returns the
 result of operation, in case of errors trying multiple times.
 
 The process template is identified by its name.
 
 This method is not supported in archive mode.
Parameters:processTemplateName - The name of a process template, a message is to be send to.nameSpace - The namespace of the service to be called.portType - The name of the port type.operation - The operation name of the service.message - The message. The object wrapped by the ClientObjectWrapper must be serializable.
 replyContext - The reply context that is to be used to send the result back to the caller.invocationCount - The invocation count that specifies the number of invocation attempts. The
    first attempt should be 1, the second 2, and so on. This
    count has to be maintained by the caller and has to be incremented
    after each unsuccesful invocation attempt, that is, when the request ended with an exception. If
    the caller is an MDB that works on behalf of a received JMS message, the JMSXDeliveryCount
    property of the message can be used to count the invocation attempts. A
    value of 0 indicates that the invocation count is not known to the caller.requestId - An ID to identify the request uniquely. If the caller is an MDB that works on
    behalf of a received JMS message, the JMSMessageId can be used as the requestId. A
    value of null implies that a unique requestId is not known to the caller.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
IdAndCorrelationSetMismatchException
IdWrongFormatException
MissingPartsException
ObjectDoesNotExistException
ProcessException
ProcessInstanceNotUniqueException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setBinaryCustomProperty
void setBinaryCustomProperty(java.lang.String identifier,
                           BinaryCustomProperty property)
                             throws ArchiveUnsupportedOperationException,
                                    EngineNotAuthorizedException,
                                    EngineParameterNullException,
                                    EngineWrongKindException,
                                    IdWrongFormatException,
                                    IdWrongTypeException,
                                    InvalidLengthException,
                                    ObjectDoesNotExistException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Stores custom-specific binary values for the specified process or activity instance
 using a string representation of the process or activity instance ID.
 
 Custom properties allow a user to add additional properties to processes or activities
 beyond those provided and managed by ProcessChoreographer. Binary custom properties allow,
 for example, to attach a Java object to a process instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 Custom properties can be provided in any state of the process or activity instance.
 An activity instance must be a basic activity or a pick activity.
 The caller must be an administrator or starter of the process instance respectively
 be an editor, owner, or administrator of the activity instance or
 be an administrator of a scope that contains the activity instance.
Parameters:identifier - A string representation of the process or activity instance ID that is used to identify the object.property - The BinaryCustomProperty object.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setBinaryCustomProperty
void setBinaryCustomProperty(PIID piid,
                           BinaryCustomProperty property)
                             throws ArchiveUnsupportedOperationException,
                                    EngineNotAuthorizedException,
                                    EngineParameterNullException,
                                    IdWrongFormatException,
                                    InvalidLengthException,
                                    ObjectDoesNotExistException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Stores custom-specific binary values for the specified process instance using
 the process instance ID.
 
 Custom properties allow a user to add additional properties to processes
 beyond those provided and managed by ProcessChoreographer. Binary custom properties allow,
 for example, to attach a Java object to a process instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 Custom properties can be provided in any state of the process instance.
 The caller must be an administrator or starter of the process instance.
Parameters:piid - The process instance ID that is used to identify the process instance.property - The BinaryCustomProperty object.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
IdWrongFormatException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setBinaryCustomProperty
void setBinaryCustomProperty(AIID aiid,
                           BinaryCustomProperty property)
                             throws ArchiveUnsupportedOperationException,
                                    EngineNotAuthorizedException,
                                    EngineParameterNullException,
                                    EngineWrongKindException,
                                    IdWrongFormatException,
                                    InvalidLengthException,
                                    ObjectDoesNotExistException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Stores custom-specific binary values for the specified activity instance using
 the activity instance ID.
 
 Custom properties allow a user to add additional properties to activities
 beyond those provided and managed by ProcessChoreographer. Binary custom properties allow,
 for example, to attach a Java object to an activity instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 Custom properties can be provided in any state of the activity instance.
 The activity instance must be a basic activity or a pick activity.
 The caller must be an administrator of the process instance or
 be an editor, owner, or administrator of the activity instance or
 be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - The activity instance ID that is used to identify the activity instance.property - The BinaryCustomProperty object.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
IdWrongFormatException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setBinaryCustomProperty
void setBinaryCustomProperty(java.lang.String piid,
                           java.lang.String activityName,
                           BinaryCustomProperty property)
                             throws ArchiveUnsupportedOperationException,
                                    EngineAmbiguousActivityException,
                                    EngineNotAuthorizedException,
                                    EngineParameterNullException,
                                    EngineUnknownActivityException,
                                    EngineWrongKindException,
                                    IdWrongFormatException,
                                    IdWrongTypeException,
                                    InvalidLengthException,
                                    ObjectDoesNotExistException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Stores custom-specific binary values for the specified activity instance using
 a string representation of the process instance ID and the activity name.
 
 Custom properties allow a user to add additional properties to activities
 beyond those provided and managed by ProcessChoreographer. Binary custom properties allow,
 for example, to attach a Java object to an activity instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 Custom properties can be provided in any state of the activity instance.
 The activity instance must be a basic activity or a pick activity.
 The caller must be an administrator of the process instance or
 be an editor, owner, or administrator of the activity instance or
 be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:piid - A string representation of the process instance object ID. This is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.property - The BinaryCustomProperty object.
 
Throws:
ArchiveUnsupportedOperationException
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineWrongKindException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setBinaryCustomProperty
void setBinaryCustomProperty(PIID piid,
                           java.lang.String activityName,
                           BinaryCustomProperty property)
                             throws ArchiveUnsupportedOperationException,
                                    EngineAmbiguousActivityException,
                                    EngineNotAuthorizedException,
                                    EngineParameterNullException,
                                    EngineUnknownActivityException,
                                    EngineWrongKindException,
                                    IdWrongFormatException,
                                    InvalidLengthException,
                                    ObjectDoesNotExistException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Stores custom-specific binary values for the specified activity instance using
 the process instance ID and the activity name.
 
 Custom properties allow a user to add additional properties to activities
 beyond those provided and managed by ProcessChoreographer. Binary custom properties allow,
 for example, to attach a Java object to an activity instance. Binary custom properties cannot
 be searched for directly. It is, however, possible to specify an additional
 queryable string.
 
 Custom properties can be provided in any state of the activity instance.
 The activity instance must be a basic activity or a pick activity.
 The caller must be an administrator of the process instance or
 be an editor, owner, or administrator of the activity instance or
 be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance that is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.property - The BinaryCustomProperty object.
 
Throws:
ArchiveUnsupportedOperationException
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineWrongKindException
IdWrongFormatException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setCustomProperty
void setCustomProperty(java.lang.String identifier,
                     java.lang.String propertyName,
                     java.lang.String propertyValue)
                       throws ArchiveUnsupportedOperationException,
                              EngineNotAuthorizedException,
                              EngineParameterNullException,
                              EngineWrongKindException,
                              EngineWrongStateException,
                              IdWrongFormatException,
                              IdWrongTypeException,
                              InvalidLengthException,
                              ObjectDoesNotExistException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Stores custom-specific values for the specified process or activity instance
 using a string representation of the object ID.
 
 Custom properties allow a user to add additional properties to processes and activities,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances and activities.
 
 A custom property has a name and a value of type string.
 
 Custom properties can be provided in any execution state of the process or activity instance.
 An activity instance must be a basic activity or a pick activity.
 To set custom properties for a process instance, the caller must be the starter of the process instance
 or be an administrator of the process instance.
 To set custom properties for an activity instance,
 the caller must have editor authority for the activity instance, be the owner of the
 activity instance, be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:identifier - A string representation of the process or activity instance object ID that is used
    to identify the process or activity instance.propertyName - The name of the custom property to be set. The
    name must not be greater than 220 bytes in UTF-8 format.
    
    Note that custom property names should conform to the XML NCName specification
    which guarantees their complete functionality.propertyValue - The custom value to be set. The
    value must not be greater than 254 bytes in UTF-8 format.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setCustomProperty
void setCustomProperty(PIID piid,
                     java.lang.String propertyName,
                     java.lang.String propertyValue)
                       throws ArchiveUnsupportedOperationException,
                              EngineNotAuthorizedException,
                              EngineParameterNullException,
                              EngineWrongKindException,
                              EngineWrongStateException,
                              IdWrongFormatException,
                              InvalidLengthException,
                              ObjectDoesNotExistException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Stores custom specific values for the specified process instance using the process instance ID.
 
 Custom properties allow a user to add additional properties to processes and activities,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances and activities.
 
 A custom property has a name and a value of type string.
 
 The process instance can be in any execution state.
 The caller must be the starter or an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance for which the custom property
 is set.propertyName - The name of the custom property to be set. The
    name must not be greater than 220 bytes in UTF-8 format.
    
    Note that custom property names should conform to the XML NCName specification
    which guarantees their complete functionality.propertyValue - The custom value to be set. The
    value must not be greater than 254 bytes in UTF-8 format.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setCustomProperty
void setCustomProperty(AIID aiid,
                     java.lang.String propertyName,
                     java.lang.String propertyValue)
                       throws ArchiveUnsupportedOperationException,
                              EngineNotAuthorizedException,
                              EngineParameterNullException,
                              EngineWrongKindException,
                              EngineWrongStateException,
                              IdWrongFormatException,
                              InvalidLengthException,
                              ObjectDoesNotExistException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Stores custom-specific values for the specified activity instance using the activity instance ID.
 
 Custom properties allow a user to add additional properties to activities,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances and activities.
 
 A custom property has a name and a value of type string.
 
 The activity instance and the associated process instance can be in any execution state.
 The activity instance must be a basic activity or a pick activity.
 The caller must have editor authority for the activity instance, be the owner of the
 activity instance, be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance.propertyName - The name of the custom property to be set. The
    name must not be greater than 220 bytes in UTF-8 format.
    
    Note that custom property names should conform to the XML NCName specification
    which guarantees their complete functionality.propertyValue - The custom value to be set. The
    value must not be greater than 254 bytes in UTF-8 format.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setCustomProperty
void setCustomProperty(java.lang.String identifier,
                     java.lang.String activityName,
                     java.lang.String propertyName,
                     java.lang.String propertyValue)
                       throws ArchiveUnsupportedOperationException,
                              EngineAmbiguousActivityException,
                              EngineNotAuthorizedException,
                              EngineParameterNullException,
                              EngineUnknownActivityException,
                              EngineWrongKindException,
                              EngineWrongStateException,
                              IdWrongFormatException,
                              IdWrongTypeException,
                              InvalidLengthException,
                              ObjectDoesNotExistException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Stores custom-specific values for the specified activity instance
 using a string representation of the  process instance and the activity instance name.
 
 Custom properties allow a user to add additional properties to processes and activities,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances and activities.
 
 A custom property has a name and a value of type string.
 
 Custom properties can be provided in any execution state of the activity instance
 and the associated process instance.
 The activity instance must be a basic activity or a pick activity.
 The caller must have editor authority for the activity instance, be the owner of the
 activity instance, be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:identifier - A string representation of the process instance object ID that is used
    to identify the process instance.activityName - The name of the activity instance that is used
    to identify the activity instance.propertyName - The name of the custom property to be set. The
    name must not be greater than 220 bytes in UTF-8 format.
    
    Note that custom property names should conform to the XML NCName specification
    which guarantees their complete functionality.propertyValue - The custom value to be set. The
    value must not be greater than 254 bytes in UTF-8 format.
 
Throws:
ArchiveUnsupportedOperationException
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setCustomProperty
void setCustomProperty(PIID piid,
                     java.lang.String activityName,
                     java.lang.String propertyName,
                     java.lang.String propertyValue)
                       throws ArchiveUnsupportedOperationException,
                              EngineAmbiguousActivityException,
                              EngineNotAuthorizedException,
                              EngineParameterNullException,
                              EngineUnknownActivityException,
                              EngineWrongKindException,
                              EngineWrongStateException,
                              IdWrongFormatException,
                              InvalidLengthException,
                              ObjectDoesNotExistException,
                              UnexpectedFailureException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Stores custom-specific values for the specified activity instance
 using the process instance ID and the activity name.
 
 Custom properties allow a user to add additional properties to processes and activities,
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances and activities.
 
 A custom property has a name and a value of type string.
 
 Custom properties can be provided in any execution state of the activity instance
 and the associated process instance.
 The activity instance must be a basic activity or a pick activity.
 The caller must have editor authority for the activity instance, be the owner of the
 activity instance, be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:piid - The process instance object ID that is used to identify the process instance.activityName - The name of the activity instance that is used
    to identify the activity instance.propertyName - The name of the custom property to be set. The
    name must not be greater than 220 bytes in UTF-8 format.
    
    Note that custom property names should conform to the XML NCName specification
    which guarantees their complete functionality.propertyValue - The custom value to be set. The
    value must not be greater than 254 bytes in UTF-8 format.
 
Throws:
ArchiveUnsupportedOperationException
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
InvalidLengthException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0.2
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setFaultMessage
void setFaultMessage(java.lang.String aiid,
                   java.lang.String faultName,
                   ClientObjectWrapper faultMessage)
                     throws ArchiveUnsupportedOperationException,
                            EngineNotAuthorizedException,
                            EngineParameterNullException,
                            EngineWrongKindException,
                            EngineWrongMessageTypeException,
                            EngineWrongStateException,
                            IdWrongFormatException,
                            IdWrongTypeException,
                            ObjectDoesNotExistException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Stores the specified fault message for the specified activity instance into the database
 using a string representation of the activity instance ID.
 The fault message is saved only, that is, navigation does not continue.
 Refer to complete
 or forceComplete
 for information on how to complete an activity instance.
 
 Any previously stored fault or output message is deleted.
 
 The activity instance must be in the claimed or stopped execution state and the associated process
 instance must be in the running, failing, or terminating execution state.
 The caller must have editor authority for the activity instance, be the owner of the
 activity instance, be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 The activity must be a human task aka staff activity. To repair variables used by
 a stopped invoke or script activity, refer to
 setVariable.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID. This string is used
    to identify the activity instance whose fault message is to be set.faultName - The name of the fault message to be set. Must be a fault defined for the activity. Refer
    to getFaultNames.
    Note that the structure of a BPEL fault name is a QName.faultMessage - The fault message. The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setFaultMessage
void setFaultMessage(AIID aiid,
                   java.lang.String faultName,
                   ClientObjectWrapper faultMessage)
                     throws ArchiveUnsupportedOperationException,
                            EngineNotAuthorizedException,
                            EngineParameterNullException,
                            EngineWrongKindException,
                            EngineWrongMessageTypeException,
                            EngineWrongStateException,
                            IdWrongFormatException,
                            ObjectDoesNotExistException,
                            UnexpectedFailureException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Stores the specified fault message for the specified activity instance into the database
 using the activity instance ID.
 The fault message is saved only, that is, navigation does not continue.
 Refer to complete
 or forceComplete
 for information on how to complete an activity instance.
 
 Any previously stored fault or output message is deleted.
 
 The activity instance must be in the claimed or stopped execution state and the associated process
 instance must be in the running, failing, or terminating execution state.
 The caller must have editor authority for the activity instance, be the owner of the
 activity instance, be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 The activity must be a human task aka staff activity. To repair variables used by
 a stopped invoke or script activity, refer to
 setVariable.
 
 This method is not supported in archive mode.
Parameters:aiid - The activity instance object ID that is used
    to identify the activity instance whose fault message is to be set.faultName - The name of the fault message to be set. Must be a fault defined for the activity. Refer
    to getFaultNames.
    Note that the structure of a BPEL fault name is a QName.faultMessage - The fault message. The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setInlineCustomProperties
void setInlineCustomProperties(java.lang.String piid,
                             java.util.List customProperties)
                               throws ArchiveUnsupportedOperationException,
                                      EngineNotAuthorizedException,
                                      EngineParameterNullException,
                                      IdWrongFormatException,
                                      IdWrongTypeException,
                                      InvalidLengthException,
                                      InvalidParameterValueException,
                                      ObjectDoesNotExistException,
                                      UnexpectedFailureException,
                                      java.rmi.RemoteException,
                                      javax.ejb.EJBException
Stores custom-specific values for the specified process instance using
 a string representation of the process instance ID.
 
 Custom properties allow a user to add additional properties to processes
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the process instance. Thus, using inline custom properties
 can increase performance.
 
 An inline custom property has a predefined name and a value of type string.
 It may be constructed using the CustomPropertyFactory.
 
 Custom properties can be provided in any execution state of the process instance.
 The caller must be the starter of the process instance
 or be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - A string representation of the process instance object ID that is used
    to identify the process instance.customProperties - A list of InlineCustomProperty objects.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
InvalidParameterValueException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- setInlineCustomProperties
void setInlineCustomProperties(PIID piid,
                             java.util.List customProperties)
                               throws ArchiveUnsupportedOperationException,
                                      EngineNotAuthorizedException,
                                      EngineParameterNullException,
                                      IdWrongFormatException,
                                      InvalidLengthException,
                                      InvalidParameterValueException,
                                      ObjectDoesNotExistException,
                                      UnexpectedFailureException,
                                      java.rmi.RemoteException,
                                      javax.ejb.EJBException
Stores custom-specific values for the specified process instance using
 the process instance ID.
 
 Custom properties allow a user to add additional properties to processes
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the process instance. Thus, using inline custom properties
 can increase performance.
 
 An inline custom property has a predefined name and a value of type string.
 It may be constructed using the CustomPropertyFactory.
 
 Custom properties can be provided in any execution state of the process instance.
 The caller must be the starter of the process instance
 or be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance for which the inline custom properties
 are to be set.customProperties - A list of InlineCustomProperty objects.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
IdWrongFormatException
InvalidLengthException
InvalidParameterValueException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- setInlineCustomProperty
void setInlineCustomProperty(java.lang.String piid,
                           InlineCustomProperty property)
                             throws ArchiveUnsupportedOperationException,
                                    EngineNotAuthorizedException,
                                    EngineParameterNullException,
                                    IdWrongFormatException,
                                    IdWrongTypeException,
                                    InvalidLengthException,
                                    InvalidParameterValueException,
                                    ObjectDoesNotExistException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Stores custom-specific values for the specified process instance
 using a string representation of the process instance ID.
 
 Custom properties allow a user to add additional properties to processes
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the process instance. Thus, using inline custom properties
 can increase performance.
 
 An inline custom property has a predefined name and a value of type string.
 It may be constructed using the CustomPropertyFactory.
 
 Custom properties can be provided in any execution state of the process instance.
 The caller must be the starter of the process instance
 or be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - A string representation of the process instance object ID that is used
    to identify the process instance.property - The inline custom property to be set.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
IdWrongFormatException
IdWrongTypeException
InvalidLengthException
InvalidParameterValueException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- setInlineCustomProperty
void setInlineCustomProperty(PIID piid,
                           InlineCustomProperty property)
                             throws ArchiveUnsupportedOperationException,
                                    EngineNotAuthorizedException,
                                    EngineParameterNullException,
                                    IdWrongFormatException,
                                    InvalidLengthException,
                                    InvalidParameterValueException,
                                    ObjectDoesNotExistException,
                                    UnexpectedFailureException,
                                    java.rmi.RemoteException,
                                    javax.ejb.EJBException
Stores custom specific values for the specified process instance using the process instance ID.
 
 Custom properties allow a user to add additional properties to processes
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the process instance. Thus, using inline custom properties
 can increase performance.
 
 An inline custom property has a predefined name and a value of type string.
 It may be constructed using the CustomPropertyFactory.
 
 The process instance can be in any execution state.
 The caller must be the starter or an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance for which the inline custom property
 is to be set.property - The inline custom property to be set.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
IdWrongFormatException
InvalidLengthException
InvalidParameterValueException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.5.1

- setInlineCustomProperty java.util.List setInlineCustomProperty(java.lang.String[] piids, InlineCustomProperty property) throws ArchiveUnsupportedOperationException , EngineParameterNullException , IdWrongFormatException , IdWrongTypeException , InvalidLengthException , InvalidParameterValueException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Stores custom-specific values for the specified proeess instances using string representations of the process instance IDs. Custom properties allow a user to add additional properties to processes beyond those provided and managed by the process engine. Custom properties are an extension to the BPEL notion of properties. While the values of BPEL properties can only be derived from messages, the values of custom properties can also be set in the process model during deployment or at runtime for process instances. In contrast to custom properties that are attached to an object, inline custom properties are an integral part of the process instance. Thus, using inline custom properties can increase performance. An inline custom property has a predefined name and a value of type string. It may be constructed using the CustomPropertyFactory . The process instance can be in any execution state. The caller must be the starter or an administrator of the process instance. This method is not supported in archive mode. Parameters: piids - An array of process instance IDs that are used to identify the process instances, property - The inline custom property to be set. Returns: List - A list of ProcessResult objects, one for every process instance specified. Refer to ProcessResult . If a single operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the ProcessException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all operations are undone. Throws: ArchiveUnsupportedOperationException EngineParameterNullException IdWrongFormatException IdWrongTypeException InvalidLengthException InvalidParameterValueException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 7.5.1

#### setInlineCustomProperty

```
java.util.List setInlineCustomProperty(java.lang.String[] piids,
                                     InlineCustomProperty property)
                                       throws ArchiveUnsupportedOperationException,
                                              EngineParameterNullException,
                                              IdWrongFormatException,
                                              IdWrongTypeException,
                                              InvalidLengthException,
                                              InvalidParameterValueException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
```

Custom properties allow a user to add additional properties to processes
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the process instance. Thus, using inline custom properties
 can increase performance.
 
 An inline custom property has a predefined name and a value of type string.
 It may be constructed using the CustomPropertyFactory.
 
 The process instance can be in any execution state.
 The caller must be the starter or an administrator of the process instance.
 
 This method is not supported in archive mode.

If a single operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the ProcessException property is null.
 
com.ibm.bpe.api.EngineNotAuthorizedException
 com.ibm.bpe.api.ObjectDoesNotExistException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all operations are undone.

- setInlineCustomProperty java.util.List setInlineCustomProperty(PIID [] piids, InlineCustomProperty property) throws ArchiveUnsupportedOperationException , EngineParameterNullException , IdWrongFormatException , InvalidLengthException , InvalidParameterValueException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Stores custom-specific values for the specified process instances using process instance IDs. Custom properties allow a user to add additional properties to processes beyond those provided and managed by the process engine. Custom properties are an extension to the BPEL notion of properties. While the values of BPEL properties can only be derived from messages, the values of custom properties can also be set in the process model during deployment or at runtime for process instances. In contrast to custom properties that are attached to an object, inline custom properties are an integral part of the process instance. Thus, using inline custom properties can increase performance. An inline custom property has a predefined name and a value of type string. It may be constructed using the CustomPropertyFactory . The process instance can be in any execution state. The caller must be the starter or an administrator of the process instance. This method is not supported in archive mode. Parameters: piids - An array of process instance IDs that are used to identify the process instances, property - The inline custom property to be set. Returns: List - A list of ProcessResult objects, one for every process instance specified. Refer to ProcessResult . If a single operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the ProcessException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all operations are undone. Throws: ArchiveUnsupportedOperationException EngineParameterNullException IdWrongFormatException InvalidLengthException InvalidParameterValueException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 7.5.1

#### setInlineCustomProperty

```
java.util.List setInlineCustomProperty(PIID[] piids,
                                     InlineCustomProperty property)
                                       throws ArchiveUnsupportedOperationException,
                                              EngineParameterNullException,
                                              IdWrongFormatException,
                                              InvalidLengthException,
                                              InvalidParameterValueException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
```

Custom properties allow a user to add additional properties to processes
 beyond those provided and managed by the process engine.
 Custom properties are an extension to the BPEL notion of properties.
 While the values of BPEL properties can only be derived from messages, the values of custom
 properties can also be set in the process model during deployment or at runtime for
 process instances.
 
 In contrast to custom properties that are attached to an object, inline custom properties
 are an integral part of the process instance. Thus, using inline custom properties
 can increase performance.
 
 An inline custom property has a predefined name and a value of type string.
 It may be constructed using the CustomPropertyFactory.
 
 The process instance can be in any execution state.
 The caller must be the starter or an administrator of the process instance.
 
 This method is not supported in archive mode.

If a single operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the ProcessException property is null.
 
com.ibm.bpe.api.EngineNotAuthorizedException
 com.ibm.bpe.api.ObjectDoesNotExistException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all operations are undone.

- setOutputMessage
void setOutputMessage(java.lang.String aiid,
                    ClientObjectWrapper outputMessage)
                      throws ArchiveUnsupportedOperationException,
                             EngineNotAuthorizedException,
                             EngineParameterNullException,
                             EngineWrongKindException,
                             EngineWrongMessageTypeException,
                             EngineWrongStateException,
                             IdWrongFormatException,
                             IdWrongTypeException,
                             ObjectDoesNotExistException,
                             UnexpectedFailureException,
                             java.rmi.RemoteException,
                             javax.ejb.EJBException
Stores the output message of the specified activity instance into the database
 using a string representation of the activity instance ID.
 The output message is saved only, that is, navigation does not continue.
 Refer to complete
 or to forceComplete
 for information on how to complete an activity instance.
 
 Any previously stored output or fault message is deleted.
 
 The activity instance must be in the claimed or stopped execution state and the associated process
 instance must be in the running, failing, or terminating execution state.
 The caller must have editor authority for the activity instance, be the owner of the
 activity instance, be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 The activity must be a human task activity (staff activity).
 To repair variables used by a stopped invoke or script activity, refer to
 setVariable.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID. This is used
    to identify the activity instance whose output message is to be set.outputMessage - The output message. The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setOutputMessage
void setOutputMessage(AIID aiid,
                    ClientObjectWrapper outputMessage)
                      throws ArchiveUnsupportedOperationException,
                             EngineNotAuthorizedException,
                             EngineParameterNullException,
                             EngineWrongKindException,
                             EngineWrongMessageTypeException,
                             EngineWrongStateException,
                             IdWrongFormatException,
                             ObjectDoesNotExistException,
                             UnexpectedFailureException,
                             java.rmi.RemoteException,
                             javax.ejb.EJBException
Stores the output message of the specified activity instance into the database using the activity instance ID.
 The output message is saved only, that is, navigation does not continue.
 Refer to complete
 or to forceComplete
 for information on how to complete an instance.
 
 Any previously stored output or fault message is deleted.
 
 The activity instance must be in the claimed or stopped execution state and the associated process
 instance must be in the running, failing, or terminating execution state.
 The caller must have editor authority for the activity instance, be the owner of the
 activity instance, be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 The activity must be a human task activity (staff activity).
 To repair variables used by a stopped invoke or script activity, refer to
 setVariable.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID of the activity instance whose output message is to be set.outputMessage - The output message. The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setVariable
void setVariable(java.lang.String piid,
               java.lang.String activityName,
               java.lang.String variableName,
               ClientObjectWrapper message)
                 throws ArchiveUnsupportedOperationException,
                        EngineAmbiguousActivityException,
                        EngineInitializingScopeNotReachedException,
                        EngineNotAuthorizedException,
                        EngineParameterNullException,
                        EngineUnknownActivityException,
                        EngineVariableDoesNotExistException,
                        EngineVariableNotVisibleException,
                        EngineWrongKindException,
                        EngineWrongMessageTypeException,
                        EngineWrongStateException,
                        IdWrongFormatException,
                        IdWrongTypeException,
                        ObjectDoesNotExistException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Sets the specified variable visible by the activity
 using a string representation of the process instance ID and the activity
 and variable names.
 
 The process instance must be in the running, failing, suspended, or terminating execution state.
 The caller must be an administrator of the process instance
 or of a scope that contains the activity provided that
 the scope is already navigated.
 
 This method is not supported in archive mode.
Parameters:piid - A string representation of the process instance object ID. This is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.variableName - The name of the variable to be set.message - The message. The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ArchiveUnsupportedOperationException
EngineAmbiguousActivityException
EngineInitializingScopeNotReachedException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineVariableDoesNotExistException
EngineVariableNotVisibleException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 Throws an
 EngineWrongStateException when the process instance is not in the running, failing,
 suspended, or terminating execution state.
 
7.0
 Throws an
 EngineWrongKindException when an activity is specified that is for internal use only.

- setVariable
void setVariable(PIID piid,
               java.lang.String activityName,
               java.lang.String variableName,
               ClientObjectWrapper message)
                 throws ArchiveUnsupportedOperationException,
                        EngineAmbiguousActivityException,
                        EngineInitializingScopeNotReachedException,
                        EngineNotAuthorizedException,
                        EngineParameterNullException,
                        EngineUnknownActivityException,
                        EngineVariableDoesNotExistException,
                        EngineVariableNotVisibleException,
                        EngineWrongKindException,
                        EngineWrongMessageTypeException,
                        EngineWrongStateException,
                        IdWrongFormatException,
                        ObjectDoesNotExistException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Sets the specified variable visible by the activity
 using the process instance ID and the activity and variable names.
 
 The process instance must be in the running, failing, suspended, or terminating execution state.
 The caller must be an administrator of the process instance
 or of a scope that contains the activity provided that
 the scope is already navigated.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance that is used
    to identify the process instance that contains the specified activity.activityName - The name of the activity that is used to identify the activity.variableName - The name of the variable to be set.message - The message. The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ArchiveUnsupportedOperationException
EngineAmbiguousActivityException
EngineInitializingScopeNotReachedException
EngineNotAuthorizedException
EngineParameterNullException
EngineUnknownActivityException
EngineVariableDoesNotExistException
EngineVariableNotVisibleException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
 
7.0
 Throws an
 EngineWrongStateException when the process instance is not in the running, failing,
 suspended, or terminating execution state.
 
7.0
 Throws an
 EngineWrongKindException when an activity is specified that is for internal use only.

- setVariable
void setVariable(java.lang.String identifier,
               java.lang.String variableName,
               ClientObjectWrapper message)
                 throws ArchiveUnsupportedOperationException,
                        EngineNotAuthorizedException,
                        EngineParameterNullException,
                        EngineVariableDoesNotExistException,
                        EngineWrongKindException,
                        EngineWrongMessageTypeException,
                        EngineWrongStateException,
                        IdWrongFormatException,
                        IdWrongTypeException,
                        ObjectDoesNotExistException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Sets the specified variable using the variable name and
 a string representation of the associated process or activity instance ID.
 
 Variables allow to store business data for the process, across activity invocations
 or for the activity.
 This function supports process repair scenarios.
 
 The process instance must be in the running, failing, suspended, or terminating execution state.
 The caller must be an administrator of the process instance
 or be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:identifier - A string representation of the process or activity instance object ID. This string is used to
    identify the process instance or the activity instance for which the specified variable is to be set.variableName - The name of the variable to be set.message - The message. The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineVariableDoesNotExistException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setVariable
void setVariable(PIID piid,
               java.lang.String variableName,
               ClientObjectWrapper message)
                 throws ArchiveUnsupportedOperationException,
                        EngineNotAuthorizedException,
                        EngineParameterNullException,
                        EngineVariableDoesNotExistException,
                        EngineWrongKindException,
                        EngineWrongMessageTypeException,
                        EngineWrongStateException,
                        IdWrongFormatException,
                        ObjectDoesNotExistException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Sets the specified variable using the variable name and
 the associated process instance ID.
 
 Variables allow to store business data for the process, across activity invocations.
 This function supports process repair scenarios.
 
 The process instance must be in the running, failing, suspended, or terminating execution state.
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - The process instance object ID. The ID is used to
    identify the process instance for which the specified variable is to be set.variableName - The name of the variable to be set.message - The message. The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineVariableDoesNotExistException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setVariable
void setVariable(AIID aiid,
               java.lang.String variableName,
               ClientObjectWrapper message)
                 throws ArchiveUnsupportedOperationException,
                        EngineNotAuthorizedException,
                        EngineParameterNullException,
                        EngineVariableDoesNotExistException,
                        EngineWrongKindException,
                        EngineWrongMessageTypeException,
                        EngineWrongStateException,
                        IdWrongFormatException,
                        ObjectDoesNotExistException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Sets the specified variable
 visible by the activity instance
 using the variable name and the associated activity instance ID.
 
 The process instance that contains the activity instance
 must be in the running, failing, suspended, or terminating execution state.
 The caller must be an administrator of the process instance
 or be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.
Parameters:aiid - The activity instance object ID. The ID is used to
    identify the activity instance for which the specified variable is to be set.variableName - The name of the variable to be set.message - The message. The object wrapped by the ClientObjectWrapper must be serializable.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineVariableDoesNotExistException
EngineWrongKindException
EngineWrongMessageTypeException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- skip void skip(java.lang.String piid, java.lang.String activityName) throws ArchiveUnsupportedOperationException , EngineAmbiguousActivityException , EngineNotAuthorizedException , EngineParameterNullException , EngineProcessWrongBuildVersionException , EngineUnknownActivityException , EngineWrongKindException , EngineWrongStateException , IdWrongFormatException , IdWrongTypeException , ObjectDoesNotExistException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Skips the specified activity instance using a string representation of the associated process instance ID and the activity name. The activity to be skipped must be a basic activity. It can be inactive, that is, it has not yet been reached during process navigation, or it can be in the ready, claimed, running, waiting, stopped, finished, failed, terminated, or skipped execution state. The associated process instance must be in the running, failing, or suspended execution state. The caller must be an administrator of the process instance or of a scope that contains the activity instance to be skipped. If the activity is still active, that is in the ready, claimed, running, waiting, or stopped execution state, then the caller can also be an administrator of the activity instance itself. Note that only existing scopes, that is, scopes that are already navigated, are considered for the authorization check on scopes. When the activity to be skipped is navigated, then it is not executed but navigation continues. If the activity has one or more outgoing links with associated transition conditions, these transition conditions are evaluated to continue navigation. It is, however, not checked whether the activity to be skipped will ever be navigated. If not, the skip request is ignored. Note that skipping an activity may result in uninitialized values. For example, the transition conditions of outgoing links may refer to values of an output message that are not set because the activity is skipped. Use setVariable to initialize the appropriate values. Skipping an activity means: This method is not supported in archive mode. Parameters: piid - The process instance object ID that is used to identify the process instance. activityName - The name of the activity instance that is to be skipped. Throws: ArchiveUnsupportedOperationException EngineAmbiguousActivityException EngineNotAuthorizedException EngineParameterNullException EngineProcessWrongBuildVersionException EngineUnknownActivityException EngineWrongKindException EngineWrongStateException IdWrongFormatException IdWrongTypeException ObjectDoesNotExistException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.1.2 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### skip

```
void skip(java.lang.String piid,
        java.lang.String activityName)
          throws ArchiveUnsupportedOperationException,
                 EngineAmbiguousActivityException,
                 EngineNotAuthorizedException,
                 EngineParameterNullException,
                 EngineProcessWrongBuildVersionException,
                 EngineUnknownActivityException,
                 EngineWrongKindException,
                 EngineWrongStateException,
                 IdWrongFormatException,
                 IdWrongTypeException,
                 ObjectDoesNotExistException,
                 UnexpectedFailureException,
                 java.rmi.RemoteException,
                 javax.ejb.EJBException
```

The activity to be skipped must be a basic activity. It can be inactive, that is, it
 has not yet been reached during process navigation, or it can be in the
 ready, claimed, running, waiting, stopped, finished, failed, terminated, or skipped execution state.
 The associated process instance must be in the running, failing, or suspended execution state.
 
 The caller must be an administrator of the process instance or
 of a scope that contains the activity instance to be skipped. If the activity is still
 active, that is in the ready, claimed, running, waiting, or stopped execution state,
 then the caller can also be an administrator of the activity instance itself.
 Note that only existing scopes, that is, scopes that are already navigated,
 are considered for the authorization check on scopes.
 
 When the activity to be skipped is navigated, then it is not executed but navigation continues.
 If the activity has one or more outgoing links with associated transition conditions,
 these transition conditions are evaluated to continue navigation.
 
 It is, however,  not checked whether the activity to be skipped will ever be navigated.
 If not, the skip request is ignored.
 
 Note that skipping an activity may result in uninitialized values. For example,
 the transition conditions of outgoing links may refer to values of an output message
 that are not set because the activity is skipped. Use
 setVariable to initialize the appropriate values.
 
 Skipping an activity means:
 

 If the activity has not yet been reached during navigation, it is "marked for skip".
 If it is navigated later on, then it is "unmarked for skip" and the activity state is
 set to skipped. Navigation continues immediately.
 
 If the activity is in an end state, it is "marked for skip".
 If it is navigated later on, then it is "unmarked for skip" and the activity state is
 set to skipped. Navigation continues immediately.
 Skipping itself is carried out on the next iteration of, for example, a while loop.
 
 If the activity is in a running state, the meaning of skipping depends on the activity type:
 
If the activity is a human task activity, the corresponding task is terminated
 and the activity is put into the skipped state.
 If the activity is an invoke activity which has started a subprocess, a terminate
 and compensate signal is sent to the subprocess and the activity stays in the running
 state until the subprocess has been terminated and compensated.
 Then the activity state is set to skipped.
 In all other cases, the activity is immediately set into the skipped execution state.
 

 Independently from the activity type, any outstanding scheduler task is canceled.
 

 This method is not supported in archive mode.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- skip void skip(PIID piid, java.lang.String activityName) throws ArchiveUnsupportedOperationException , EngineAmbiguousActivityException , EngineNotAuthorizedException , EngineParameterNullException , EngineProcessWrongBuildVersionException , EngineUnknownActivityException , EngineWrongKindException , EngineWrongStateException , IdWrongFormatException , ObjectDoesNotExistException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Skips the specified activity instance using the associated process instance ID and the activity instance name. The activity to be skipped must be a basic activity. It can be inactive, that is, it has not yet been reached during process navigation, or it can be in the ready, claimed, running, waiting, stopped, finished, failed, terminated, or skipped execution state. The associated process instance must be in the running, failing, or suspended execution state. The caller must be an administrator of the process instance or of a scope that contains the activity instance to be skipped. If the activity is still active, that is in the ready, claimed, running, waiting, or stopped execution state, then the caller can also be an administrator of the activity instance itself. Note that only existing scopes, that is, scopes that are already navigated, are considered for the authorization check on scopes. When the activity to be skipped is navigated, then it is not executed but navigation continues. If the activity has one or more outgoing links with associated transition conditions, these transition conditions are evaluated to continue navigation. It is, however, not checked whether the activity to be skipped will ever be navigated. If not, the skip request is ignored. Note that skipping an activity may result in uninitialized values. For example, the transition conditions of outgoing links may refer to values of an output message that are not set because the activity is skipped. Use setVariable to initialize the appropriate values. Skipping an activity means: This method is not supported in archive mode. Parameters: piid - The process instance object ID that is used to identify the process instance. activityName - The name of the activity instance that is to be skipped. Throws: ArchiveUnsupportedOperationException EngineAmbiguousActivityException EngineNotAuthorizedException EngineParameterNullException EngineProcessWrongBuildVersionException EngineUnknownActivityException EngineWrongKindException EngineWrongStateException IdWrongFormatException ObjectDoesNotExistException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.1.2 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### skip

```
void skip(PIID piid,
        java.lang.String activityName)
          throws ArchiveUnsupportedOperationException,
                 EngineAmbiguousActivityException,
                 EngineNotAuthorizedException,
                 EngineParameterNullException,
                 EngineProcessWrongBuildVersionException,
                 EngineUnknownActivityException,
                 EngineWrongKindException,
                 EngineWrongStateException,
                 IdWrongFormatException,
                 ObjectDoesNotExistException,
                 UnexpectedFailureException,
                 java.rmi.RemoteException,
                 javax.ejb.EJBException
```

The activity to be skipped must be a basic activity. It can be inactive, that is, it
 has not yet been reached during process navigation, or it can be in the
 ready, claimed, running, waiting, stopped, finished, failed, terminated, or skipped execution state.
 The associated process instance must be in the running, failing, or suspended execution state.
 
 The caller must be an administrator of the process instance or
 of a scope that contains the activity instance to be skipped. If the activity is still
 active, that is in the ready, claimed, running, waiting, or stopped execution state,
 then the caller can also be an administrator of the activity instance itself.
 Note that only existing scopes, that is, scopes that are already navigated,
 are considered for the authorization check on scopes.
 
 When the activity to be skipped is navigated, then it is not executed but navigation continues.
 If the activity has one or more outgoing links with associated transition conditions,
 these transition conditions are evaluated to continue navigation.
 
 It is, however,  not checked whether the activity to be skipped will ever be navigated.
 If not, the skip request is ignored.
 
 Note that skipping an activity may result in uninitialized values. For example,
 the transition conditions of outgoing links may refer to values of an output message
 that are not set because the activity is skipped. Use
 setVariable to initialize the appropriate values.
 
 Skipping an activity means:
 

 If the activity has not yet been reached during navigation, it is "marked for skip".
 If it is navigated later on, then it is "unmarked for skip" and the activity state is
 set to skipped. Navigation continues immediately.
 
 If the activity is in an end state, it is "marked for skip".
 If it is navigated later on, then it is "unmarked for skip" and the activity state is
 set to skipped. Navigation continues immediately.
 Skipping itself is carried out on the next iteration of, for example, a while loop.
 
 If the activity is in a running state, the meaning of skipping depends on the activity type:
 
If the activity is a human task activity, the corresponding task is terminated
 and the activity is put into the skipped state.
 If the activity is an invoke activity which has started a subprocess, a terminate
 and compensate signal is sent to the subprocess and the activity stays in the running
 state until the subprocess has been terminated and compensated.
 Then the activity state is set to skipped.
 In all other cases, the activity is immediately set into the skipped execution state.
 

 Independently from the activity type, any outstanding scheduler task is canceled.
 

 This method is not supported in archive mode.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- skip void skip(java.lang.String aiid) throws ArchiveUnsupportedOperationException , EngineNotAuthorizedException , EngineProcessWrongBuildVersionException , EngineWrongKindException , EngineWrongStateException , IdWrongFormatException , IdWrongTypeException , ObjectDoesNotExistException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Skips the activity instance using a string representation of the activity instance ID. The activity to be skipped must be a basic activity. It can be in the ready, claimed, running, waiting, stopped, finished, failed, terminated, or skipped execution state. The associated process instance must be in the running, failing, or suspended execution state. The caller must be an administrator of the process instance or of a scope that contains the activity instance to be skipped. If the activity is still active, that is in the ready, claimed, running, waiting, or stopped execution state, then the caller can also be an administrator of the activity instance itself. If the activity has one or more outgoing links with associated transition conditions, these transition conditions are evaluated to continue navigation. Note that skipping an activity may result in uninitialized values. For example, the transition conditions of outgoing links may refer to values of an output message that are not set because the activity is skipped. Use setVariable to initialize the appropriate values. Skipping an activity means: This method is not supported in archive mode. Parameters: aiid - A string representation of the activity instance object ID that is used to identify the activity instance to be skipped. Throws: ArchiveUnsupportedOperationException EngineNotAuthorizedException EngineProcessWrongBuildVersionException EngineWrongKindException EngineWrongStateException IdWrongFormatException IdWrongTypeException ObjectDoesNotExistException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.1.2 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### skip

```
void skip(java.lang.String aiid)
          throws ArchiveUnsupportedOperationException,
                 EngineNotAuthorizedException,
                 EngineProcessWrongBuildVersionException,
                 EngineWrongKindException,
                 EngineWrongStateException,
                 IdWrongFormatException,
                 IdWrongTypeException,
                 ObjectDoesNotExistException,
                 UnexpectedFailureException,
                 java.rmi.RemoteException,
                 javax.ejb.EJBException
```

The activity to be skipped must be a basic activity. It can be in the
 ready, claimed, running, waiting, stopped, finished, failed, terminated, or skipped execution state.
 The associated process instance must be in the running, failing, or suspended execution state.
 
 The caller must be an administrator of the process instance or
 of a scope that contains the activity instance to be skipped. If the activity is still
 active, that is in the ready, claimed, running, waiting, or stopped execution state,
 then the caller can also be an administrator of the activity instance itself.
 
 If the activity has one or more outgoing links with associated transition conditions,
 these transition conditions are evaluated to continue navigation.
 
 Note that skipping an activity may result in uninitialized values. For example,
 the transition conditions of outgoing links may refer to values of an output message
 that are not set because the activity is skipped. Use
 setVariable to initialize the appropriate values.
 
 Skipping an activity means:
 

 If the activity is in an end state, it is "marked for skip".
 If it is navigated later on, then it is "unmarked for skip" and the activity state is
 set to skipped. Navigation continues immediately.
 Skipping itself is carried out on the next iteration of, for example, a while loop.
 
 If the activity is in a running state, the meaning of skipping depends on the activity type:
 
If the activity is a human task activity, the corresponding task is terminated
 and the activity is put into the skipped state.
 If the activity is an invoke activity which has invoked a subprocess, a terminate
 and compensate signal is sent to the subprocess and the activity stays in the running
 state until the subprocess has been terminated and compensated.
 Then the activity state is set to skipped.
 In all other cases, the activity is immediately set into the skipped execution state.
 

 Independently from the activity type, any outstanding scheduler task is canceled.
 

 This method is not supported in archive mode.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- skip void skip(AIID aiid) throws ArchiveUnsupportedOperationException , EngineNotAuthorizedException , EngineProcessWrongBuildVersionException , EngineWrongKindException , EngineWrongStateException , IdWrongFormatException , ObjectDoesNotExistException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Skips the activity instance using the activity instance ID. The activity to be skipped must be a basic activity. It can be in the ready, claimed, running, waiting, stopped, finished, failed, terminated, or skipped execution state. The associated process instance must be in the running, failing, or suspended execution state. The caller must be an administrator of the process instance or of a scope that contains the activity instance to be skipped. If the activity is still active, that is in the ready, claimed, running, waiting, or stopped execution state, then the caller can also be an administrator of the activity instance itself. If the activity has one or more outgoing links with associated transition conditions, these transition conditions are evaluated to continue navigation. Note that skipping an activity may result in uninitialized values. For example, the transition conditions of outgoing links may refer to values of an output message that are not set because the activity is skipped. Use setVariable to initialize the appropriate values. Skipping an activity means: This method is not supported in archive mode. Parameters: aiid - The object ID to identify the activity instance to be skipped. Throws: ArchiveUnsupportedOperationException EngineNotAuthorizedException EngineProcessWrongBuildVersionException EngineWrongKindException EngineWrongStateException IdWrongFormatException ObjectDoesNotExistException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 6.1.2 Change History Release Modification 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### skip

```
void skip(AIID aiid)
          throws ArchiveUnsupportedOperationException,
                 EngineNotAuthorizedException,
                 EngineProcessWrongBuildVersionException,
                 EngineWrongKindException,
                 EngineWrongStateException,
                 IdWrongFormatException,
                 ObjectDoesNotExistException,
                 UnexpectedFailureException,
                 java.rmi.RemoteException,
                 javax.ejb.EJBException
```

The activity to be skipped must be a basic activity. It can be in the
 ready, claimed, running, waiting, stopped, finished, failed, terminated, or skipped execution state.
 The associated process instance must be in the running, failing, or suspended execution state.
 
 The caller must be an administrator of the process instance or
 of a scope that contains the activity instance to be skipped. If the activity is still
 active, that is in the ready, claimed, running, waiting, or stopped execution state,
 then the caller can also be an administrator of the activity instance itself.
 
 If the activity has one or more outgoing links with associated transition conditions,
 these transition conditions are evaluated to continue navigation.
 
 Note that skipping an activity may result in uninitialized values. For example,
 the transition conditions of outgoing links may refer to values of an output message
 that are not set because the activity is skipped. Use
 setVariable to initialize the appropriate values.
 
 Skipping an activity means:
 

 If the activity is in an end state, it is "marked for skip".
 If it is navigated later on, then it is "unmarked for skip" and the activity state is
 set to skipped. Navigation continues immediately.
 Skipping itself is carried out on the next iteration of, for example, a while loop.
 
 If the activity is in a running state, the meaning of skipping depends on the activity type:
 
If the activity is a human task activity, the corresponding task is terminated
 and the activity is put into the skipped state.
 If the activity is an invoke activity which has invoked a subprocess, a terminate
 and compensate signal is sent to the subprocess and the activity stays in the running
 state until the subprocess has been terminated and compensated.
 Then the activity state is set to skipped.
 In all other cases, the activity is immediately set into the skipped execution state.
 

 Independently from the activity type, any outstanding scheduler task is canceled.
 

 This method is not supported in archive mode.

Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- skipAndJump
void skipAndJump(java.lang.String aiid,
               java.lang.String targetActivityName)
                 throws ArchiveUnsupportedOperationException,
                        EngineAmbiguousActivityException,
                        EngineNotAuthorizedException,
                        EngineParameterNullException,
                        EngineProcessWrongBuildVersionException,
                        EngineUnknownActivityException,
                        EngineUnsupportedJumpException,
                        EngineWrongKindException,
                        EngineWrongStateException,
                        IdWrongFormatException,
                        IdWrongTypeException,
                        ObjectDoesNotExistException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Skips the activity instance using a string representation of the
 activity instance ID and continues navigation at the specified target activity.
 
 The activity to be skipped must be a basic activity.
 It can be be in the ready, claimed, running, waiting, or stopped execution state.
 A receive activity instance must be in the stopped execution state.
 The associated process instance must be in the running, failing, or suspended execution state.
 
 The caller must be an administrator of the associated process instance or
 of a scope that contains the activity instance to be skipped.
 
 The activity to jump to must be in the same cyclic flow or sequence. You can jump forwards
 or backwards. When jumping backwards within a sequence, the activity instances between the completed
 activity instance and the jumped-to activity are deleted but compensation is not triggered.
 Compensation handlers are, however, registered for scopes so that compensation may run later.
 
 If the activity to jump to is inside a forEach construct or an event handler,
 then the activity jumped to is within the same forEach iteration or event handler instance
 as the completed activity.
 
 The exit condition on the entry of the activity to jump to is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - A string representation of the activity instance object ID that is used
    to identify the activity instance to be skipped.targetActivityName - The name of an activity to jump to. The activity can be a basic activity
 as well as a structured activity.
 
Throws:
ArchiveUnsupportedOperationException
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessWrongBuildVersionException
EngineUnknownActivityException
EngineUnsupportedJumpException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- skipAndJump
void skipAndJump(AIID aiid,
               java.lang.String targetActivityName)
                 throws ArchiveUnsupportedOperationException,
                        EngineAmbiguousActivityException,
                        EngineNotAuthorizedException,
                        EngineParameterNullException,
                        EngineProcessWrongBuildVersionException,
                        EngineUnknownActivityException,
                        EngineUnsupportedJumpException,
                        EngineWrongKindException,
                        EngineWrongStateException,
                        IdWrongFormatException,
                        ObjectDoesNotExistException,
                        UnexpectedFailureException,
                        java.rmi.RemoteException,
                        javax.ejb.EJBException
Skips the activity instance using the activity instance ID
 and continues navigation at the specified target activity.
 
 The activity to be skipped must be a basic activity.
 It can be be in the ready, claimed, running, waiting, or stopped execution state.
 A receive activity instance must be in the stopped execution state.
 The associated process instance must be in the running, failing, or suspended execution state.
 
 The caller must be an administrator of the associated process instance or
 of a scope that contains the activity instance to be skipped.
 
 The activity to jump to must be in the same cyclic flow or sequence. You can jump forwards
 or backwards. When jumping backwards within a sequence, the activity instances between the completed
 activity instance and the jumped-to activity are deleted but compensation is not triggered.
 Compensation handlers are, however, registered for scopes so that compensation may run later.
 
 If the activity to jump to is inside a forEach construct or an event handler,
 then the activity jumped to is within the same forEach iteration or event handler instance
 as the completed activity.
 
 The exit condition on the entry of the activity to jump to is not evaluated.
 
 This method is not supported in archive mode.
Parameters:aiid - The object ID to identify the activity instance to be skipped.targetActivityName - The name of an activity to jump to. The activity can be a basic activity
 as well as a structured activity.
 
Throws:
ArchiveUnsupportedOperationException
EngineAmbiguousActivityException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessWrongBuildVersionException
EngineUnknownActivityException
EngineUnsupportedJumpException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1.2
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- suspend
void suspend(java.lang.String piid)
             throws ArchiveUnsupportedOperationException,
                    EngineNotAuthorizedException,
                    EngineWrongKindException,
                    EngineWrongStateException,
                    IdWrongFormatException,
                    IdWrongTypeException,
                    ObjectDoesNotExistException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Suspends the specified top-level process instance and its non-autonomous subprocesses
 using a string representation of the process instance ID.
 
 The process instance must be in the running or failing execution state.
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - A string representation of the process instance object ID that is used to identify
    the process instance to be suspended.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- suspend
void suspend(PIID piid)
             throws ArchiveUnsupportedOperationException,
                    EngineNotAuthorizedException,
                    EngineWrongKindException,
                    EngineWrongStateException,
                    IdWrongFormatException,
                    ObjectDoesNotExistException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Suspends the specified top-level process instance and its non-autonomous subprocesses
 using the process instance ID.
 
 The process instance must be in the running or failing execution state.
 Subprocesses are suspended if they are in state running, failing or terminating.
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance to be suspended.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.0
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- suspend
void suspend(java.lang.String piid,
           int duration)
             throws ArchiveUnsupportedOperationException,
                    EngineNotAuthorizedException,
                    EngineSchedulerException,
                    EngineSchedulerNotFoundException,
                    EngineWrongKindException,
                    EngineWrongStateException,
                    IdWrongFormatException,
                    IdWrongTypeException,
                    InvalidParameterValueException,
                    ObjectDoesNotExistException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Suspends the specified top-level process instance and its non-autonomous subprocesses
 for the specified duration using a string representation of the process instance ID.
 
 The process instance must be in the running or failing execution state.
 Subprocesses are suspended if they are in state running, failing or terminating.
 The caller must be an administrator of the process instance.
 
 The process instance is then suspended for the specified duration or until an explicit
 resume request is issued.
 
 This method is not supported in archive mode.
Parameters:piid - A string representation of the process instance ID to be suspended.duration - The seconds for which the process instance is to be suspended. When the specified
    duration has passed, the process instance and its suspended subprocesses are
    automatically resumed.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineSchedulerException
EngineSchedulerNotFoundException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
InvalidParameterValueException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- suspend
void suspend(PIID piid,
           int duration)
             throws ArchiveUnsupportedOperationException,
                    EngineNotAuthorizedException,
                    EngineSchedulerException,
                    EngineSchedulerNotFoundException,
                    EngineWrongKindException,
                    EngineWrongStateException,
                    IdWrongFormatException,
                    InvalidParameterValueException,
                    ObjectDoesNotExistException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Suspends the specified top-level process instance and its non-autonomous subprocesses
 for the specified duration using the process instance ID.
 
 The process instance must be in the running or failing execution state.
 Subprocesses are suspended if they are in state running, failing or terminating.
 The caller must be an administrator of the process instance.
 
 The process instance is then suspended for the specified duration or until an explicit
 resume request is issued.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance to be suspended.duration - The seconds for which the process instance is to be suspended. When the specified
    duration has passed, the process instance and its suspended subprocesses are
    automatically resumed.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineSchedulerException
EngineSchedulerNotFoundException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
InvalidParameterValueException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- suspend
void suspend(java.lang.String piid,
           java.util.Calendar deadline)
             throws ArchiveUnsupportedOperationException,
                    EngineNotAuthorizedException,
                    EngineParameterNullException,
                    EngineSchedulerException,
                    EngineSchedulerNotFoundException,
                    EngineWrongKindException,
                    EngineWrongStateException,
                    IdWrongFormatException,
                    IdWrongTypeException,
                    ObjectDoesNotExistException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Suspends the specified top-level process instance and its non-autonomous subprocesses
 until the specified point in time is reached using a string representation of the process instance ID.
 
 The process instance must be in the running or failing execution state.
 Subprocesses are suspended if they are in state running, failing or terminating.
 The caller must be an administrator of the process instance.
 
 The process instance is then suspended until the specified point in time or until an explicit
 resume request is issued.
 
 This method is not supported in archive mode.
Parameters:piid - A string representation of the process instance ID to be suspended.deadline - The time up to which the process instance is to be suspended. When the specified
    time has been reached, the process instance and its suspended subprocesses are
    automatically resumed.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineSchedulerException
EngineSchedulerNotFoundException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- suspend
void suspend(PIID piid,
           java.util.Calendar deadline)
             throws ArchiveUnsupportedOperationException,
                    EngineNotAuthorizedException,
                    EngineParameterNullException,
                    EngineSchedulerException,
                    EngineSchedulerNotFoundException,
                    EngineWrongKindException,
                    EngineWrongStateException,
                    IdWrongFormatException,
                    ObjectDoesNotExistException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Suspends the specified top-level process instance and its non-autonomous subprocesses
 until the specified point in time is reached using the process instance ID.
 
 The process instance must be in the running or failing execution state.
 Subprocesses are suspended if they are in state running, failing or terminating.
 The caller must be an administrator of the process instance.
 
 The process instance is then suspended until the specified point in time or until an explicit
 resume request is issued.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance to be suspended.deadline - The time up to which the process instance is to be suspended. When the specified
    time has been reached, the process instance and its suspended subprocesses are
    automatically resumed.
 
Throws:
ArchiveUnsupportedOperationException
EngineNotAuthorizedException
EngineParameterNullException
EngineSchedulerException
EngineSchedulerNotFoundException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- suspend
void suspend(java.lang.String piid,
           java.lang.String timeoutExpression,
           java.lang.String calendarName,
           java.lang.String JNDINameOfCalendar)
             throws ArchiveUnsupportedOperationException,
                    EngineCalendarNotFoundException,
                    EngineNotAuthorizedException,
                    EngineParameterNullException,
                    EngineSchedulerException,
                    EngineSchedulerNotFoundException,
                    EngineWrongKindException,
                    EngineWrongStateException,
                    IdWrongFormatException,
                    IdWrongTypeException,
                    ObjectDoesNotExistException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Suspends the specified top-level process instance and its non-autonomous subprocesses
 for a calendar specific time using a string representation of the process instance ID.
 
 The process instance must be in the running or failing execution state.
 Subprocesses are suspended if they are in state running, failing or terminating.
 The caller must be an administrator of the process instance.
 
 The process instance is then suspended until the specified point in time or until an explicit
 resume request is issued.
 
 This method is not supported in archive mode.
Parameters:piid - A string representation of the process instance ID to be suspended.timeoutExpression - A calendar specific expression that is used to calculate the time up to when
    the process instance is to be suspended. When the specified
    time has been reached, the process instance and its suspended subprocesses are
    automatically resumed.calendarName - The name of a user-provided calendar. If the JNDI name of the calendar is not
    specified, the name may be "SIMPLE" or "CRON" to select one of WebSphere's
    calendars. If neither a calendar nor a JNDI name is specified, then the WebSphere
    default calendar (SIMPLE) is used.JNDINameOfCalendar - The JNDI name of the EJB providing the user's calendar; may be null so that
    one of WebSphere's calendars is used.
 
Throws:
ArchiveUnsupportedOperationException
EngineCalendarNotFoundException
EngineNotAuthorizedException
EngineParameterNullException
EngineSchedulerException
EngineSchedulerNotFoundException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- suspend
void suspend(PIID piid,
           java.lang.String timeoutExpression,
           java.lang.String calendarName,
           java.lang.String JNDINameOfCalendar)
             throws ArchiveUnsupportedOperationException,
                    EngineCalendarNotFoundException,
                    EngineNotAuthorizedException,
                    EngineParameterNullException,
                    EngineSchedulerException,
                    EngineSchedulerNotFoundException,
                    EngineWrongKindException,
                    EngineWrongStateException,
                    IdWrongFormatException,
                    ObjectDoesNotExistException,
                    UnexpectedFailureException,
                    java.rmi.RemoteException,
                    javax.ejb.EJBException
Suspends the specified top-level process instance and its non-autonomous subprocesses
 for a calendar specific time using the process instance ID.
 
 The process instance must be in the running or failing execution state.
 Subprocesses are suspended if they are in state running, failing or terminating.
 The caller must be an administrator of the process instance.
 
 The process instance is then suspended until the specified point in time or until an explicit
 resume request is issued.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance to be suspended.timeoutExpression - A calendar specific expression that is used to calculate the time up to when
    the process instance is to be suspended. When the specified
    time has been reached, the process instance and its suspended subprocesses are
    automatically resumed.calendarName - The name of a user-provided calendar. If the JNDI name of the calendar is not
    specified, the name may be "SIMPLE" or "CRON" to select one of WebSphere's
    calendars. If neither a calendar nor a JNDI name is specified, then the WebSphere
    default calendar (SIMPLE) is used.JNDINameOfCalendar - The JNDI name of the EJB providing the user's calendar; may be null so that
    one of WebSphere's calendars is used.
 
Throws:
ArchiveUnsupportedOperationException
EngineCalendarNotFoundException
EngineNotAuthorizedException
EngineParameterNullException
EngineSchedulerException
EngineSchedulerNotFoundException
EngineWrongKindException
EngineWrongStateException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.1
 
Change History

Release
 Modification
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- testMigration
boolean testMigration(java.lang.String piid,
                    java.lang.String ptid)
                      throws ApplicationNotStartedException,
                             ArchiveUnsupportedOperationException,
                             EngineInvalidMigrationTargetException,
                             EngineNotAuthorizedException,
                             EngineWrongStateException,
                             EngineProcessModelStoppedException,
                             EngineProcessTemplateDoesNotExistException,
                             EngineProcessWrongBuildVersionException,
                             IdWrongFormatException,
                             IdWrongTypeException,
                             ObjectDoesNotExistException,
                             UnexpectedFailureException,
                             java.rmi.RemoteException,
                             javax.ejb.EJBException
Checks whether the process instance
 identified by a string representation of the process instance ID can be migrated
 to an instance of the specified process template.
 
 The process instance must be an instance of a process template with a version 7 schema.
 It must be in the running, failing, or suspended execution state.
 
 The process template must have a later valid-from date as the process template
 the process instance is currently derived from.
 It must be started and belong to a started application.
 
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - A string representation of the process instance object ID that is
    to be tested.ptid - A string representation of the process template object ID that identifies
    the process template to be tested for process instance migration.
    If not specified, the currently valid process template is used.
 
Returns:boolean -
    True states that the process instance can be migrated to an instance of the
    specified process template.
    False states that the process instance cannot be migrated to an instance of the
    specified process template.
 
Throws:
ApplicationNotStartedException
ArchiveUnsupportedOperationException
EngineInvalidMigrationTargetException
EngineNotAuthorizedException
EngineWrongStateException
EngineProcessModelStoppedException
EngineProcessTemplateDoesNotExistException
EngineProcessWrongBuildVersionException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.1
 
Change History

Release
 Modification
 
7.5.1
 
 Throws an EngineWrongStateException when the state of the process instance does not allow for a migration.

- testMigration
boolean testMigration(PIID piid,
                    PTID ptid)
                      throws ApplicationNotStartedException,
                             ArchiveUnsupportedOperationException,
                             EngineInvalidMigrationTargetException,
                             EngineNotAuthorizedException,
                             EngineWrongStateException,
                             EngineProcessModelStoppedException,
                             EngineProcessTemplateDoesNotExistException,
                             EngineProcessWrongBuildVersionException,
                             IdWrongFormatException,
                             ObjectDoesNotExistException,
                             UnexpectedFailureException,
                             java.rmi.RemoteException,
                             javax.ejb.EJBException
Checks whether the process instance identified by the process instance ID
 can be migrated to an instance of the specified process template.
 
 The process instance must be an instance of a process template with a version 7 schema.
 It must be in the running, failing, or suspended execution state.
 
 The process template must have a later valid-from date as the process template
 the process instance is currently derived from.
 It must be started and belong to a started application.
 
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID to identify the process instance to be tested.ptid - The process template object ID that identifies
    the process template to be tested for process instance migration.
    If not specified, the currently valid process template is identified.
 
Returns:boolean -
    True states that the process instance can be migrated to an instance of the
    specified process template.
    False states that the process instance cannot be migrated to an instance of the
    specified process template.
 
Throws:
ApplicationNotStartedException
ArchiveUnsupportedOperationException
EngineInvalidMigrationTargetException
EngineNotAuthorizedException
EngineWrongStateException
EngineProcessModelStoppedException
EngineProcessTemplateDoesNotExistException
EngineProcessWrongBuildVersionException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.1
 
Change History

Release
 Modification
 
7.5.1
 
 Throws an EngineWrongStateException when the state of the process instance does not allow for a migration.

- transferWorkItem void transferWorkItem(java.lang.String identifier, int assignmentReason, java.lang.String fromOwner, java.lang.String toOwner) throws ApplicationVetoException , ArchiveUnsupportedOperationException , EngineEverybodyWorkItemException , EngineNotAuthorizedException , EngineParameterNullException , EngineProcessReaderWorkItemException , EngineWrongKindException , EngineWrongStateException , HumanTaskManagerException , IdWrongFormatException , IdWrongTypeException , InvalidLengthException , UserDoesNotExistException , WorkItemDoesNotExistException , ObjectDoesNotExistException , UnexpectedFailureException , WorkItemManagerException , java.rmi.RemoteException, javax.ejb.EJBException Transfers the specified work item for a process or activity instance using a string representation of either the process or activity instance ID. Following restrictions apply: When work items with assignment reasons "administrator" or "reader" for the process instance are transferred, the transfer is automatically propagated to all enclosed activity instances. The process instance must be in the running, failing, or terminating execution state. When a work item for an activity instance is to be transferred, the activity instance must be in the claimed, ready, running, or stopped execution state. The activity must be an invoke, script, or human task activity. A human task activity is also known as staff activity. The caller must own the work item with an assignment reason "owner", be an administrator of the process instance, or be an administrator of a scope that contains the activity instance. This method is not supported in archive mode. Parameters: identifier - A string representation of the process or activity instance ID that is used to identify the work item to be transferred. assignmentReason - The reason why the work item has been assigned - refer to the work item assignment reasons . fromOwner - The user ID or the name of the group the work item currently belongs to. toOwner - The user ID or the name of the group the work item is to be transferred to. Work items can be transferred from a user to a user or from a group of users to a group of users. If the work item is transferred to a user, it is checked whether the user exists but the check may be executed case insensitively. The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments' custom property of the Human Task Manager configuration to 'true'. Throws: ApplicationVetoException ArchiveUnsupportedOperationException EngineEverybodyWorkItemException EngineNotAuthorizedException EngineParameterNullException EngineProcessReaderWorkItemException EngineWrongKindException EngineWrongStateException HumanTaskManagerException IdWrongFormatException IdWrongTypeException InvalidLengthException UserDoesNotExistException WorkItemDoesNotExistException ObjectDoesNotExistException UnexpectedFailureException WorkItemManagerException java.rmi.RemoteException javax.ejb.EJBException Since: 5.1 Change History Release Modification 6.1.2 The caller may have administrator rights for the scope that contains the activity instance. 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### transferWorkItem

```
void transferWorkItem(java.lang.String identifier,
                    int assignmentReason,
                    java.lang.String fromOwner,
                    java.lang.String toOwner)
                      throws ApplicationVetoException,
                             ArchiveUnsupportedOperationException,
                             EngineEverybodyWorkItemException,
                             EngineNotAuthorizedException,
                             EngineParameterNullException,
                             EngineProcessReaderWorkItemException,
                             EngineWrongKindException,
                             EngineWrongStateException,
                             HumanTaskManagerException,
                             IdWrongFormatException,
                             IdWrongTypeException,
                             InvalidLengthException,
                             UserDoesNotExistException,
                             WorkItemDoesNotExistException,
                             ObjectDoesNotExistException,
                             UnexpectedFailureException,
                             WorkItemManagerException,
                             java.rmi.RemoteException,
                             javax.ejb.EJBException
```

Following restrictions apply:
 
A work item with an assignment reason "starter" cannot be transferred.
 When a work item with assignment reason "owner" is transferred and the caller is not
 an administrator, then the user the work item is transferred to must be an administrator
 or own the same work item with an assignment reason "potential owner".
 Work items with assignment reason "administrator" can only be transferred on the process instance.
 Work items with assignment reason "reader" can only be transferred on the activity instance,
 when the work item
 has not been propagated from the process instance, that is, when the work item  denotes
 an activity reader but no process reader.
 

 When work items with assignment reasons "administrator" or "reader" for the process instance
 are transferred, the transfer is automatically propagated to all enclosed activity instances.
 
 The process instance must be in the running, failing, or terminating execution state.
 When a work item for an activity instance is to be transferred,
 the activity instance must be in the claimed, ready, running, or stopped execution state.
 The activity must be an invoke, script, or human task activity.
 A human task activity is also known as staff activity.
 
 The caller must own the work item with an assignment reason "owner",
 be an administrator of the process instance,
 or be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.

Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- transferWorkItem
void transferWorkItem(PIID piid,
                    int assignmentReason,
                    java.lang.String fromOwner,
                    java.lang.String toOwner)
                      throws ApplicationVetoException,
                             ArchiveUnsupportedOperationException,
                             EngineEverybodyWorkItemException,
                             EngineNotAuthorizedException,
                             EngineParameterNullException,
                             EngineProcessReaderWorkItemException,
                             EngineWrongKindException,
                             EngineWrongStateException,
                             HumanTaskManagerException,
                             IdWrongFormatException,
                             InvalidLengthException,
                             UserDoesNotExistException,
                             WorkItemDoesNotExistException,
                             ObjectDoesNotExistException,
                             UnexpectedFailureException,
                             WorkItemManagerException,
                             java.rmi.RemoteException,
                             javax.ejb.EJBException
Transfers the specified work item for the specified process instance
 using the process instance ID.
 
 A work item with an assignment reason "starter" cannot be transferred.
 
 When work items with assignment reasons "administrator" or "reader"
 are transferred, the transfer is automatically propagated to all enclosed activity instances.
 
 The process instance must be in the running, failing, or terminating execution state.
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance the work item belongs to.assignmentReason - The reason why the work item has been assigned - refer to
     the work item assignment reasons.fromOwner - The user ID or the name of the group the work item currently belongs to.toOwner - The user ID or the name of the group the work item is to be transferred to.
    Work items can be transferred from a user to a user or from a group of users to a group of users.
    If the work item is transferred to a user,
    it is checked whether the user exists but the check may be executed case insensitively.
    The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments'
    custom property of the Human Task Manager configuration to 'true'.
 
Throws:
ApplicationVetoException
ArchiveUnsupportedOperationException
EngineEverybodyWorkItemException
EngineNotAuthorizedException
EngineParameterNullException
EngineProcessReaderWorkItemException
EngineWrongKindException
EngineWrongStateException
HumanTaskManagerException
IdWrongFormatException
InvalidLengthException
UserDoesNotExistException
WorkItemDoesNotExistException
ObjectDoesNotExistException
UnexpectedFailureException
WorkItemManagerException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
5.1
 
Change History

Release
 Modification
 
6.0.2
 
 Throws an ApplicationVetoException when the application refuses to execute the method.
 
6.0.2
 
 Throws an EngineProcessReaderWorkItemException when a process reader work item already exists.
 
6.0.2
 
 Throws a HumanTaskManagerException when the Human Task Manager reports an error.
 
6.0.2
 
 Throws a UserDoesNotExistException when the specified user does not exist.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- transferWorkItem void transferWorkItem(AIID aiid, int assignmentReason, java.lang.String fromOwner, java.lang.String toOwner) throws ApplicationVetoException , ArchiveUnsupportedOperationException , EngineEverybodyWorkItemException , EngineNotAuthorizedException , EngineParameterNullException , EngineProcessReaderWorkItemException , EngineWrongKindException , EngineWrongStateException , HumanTaskManagerException , IdWrongFormatException , InvalidLengthException , UserDoesNotExistException , WorkItemDoesNotExistException , ObjectDoesNotExistException , UnexpectedFailureException , WorkItemManagerException , java.rmi.RemoteException, javax.ejb.EJBException Transfers the specified work item for the specified activity instance using the activity instance ID. Following restrictions apply: The activity instance must be in the claimed, ready, running, or stopped execution state. The associated process instance must be in the running, failing, or terminating execution state. The activity must be an invoke, script, or human task activity. A human task activity is also known as staff activity. The caller must own the work item with an assignment reason "owner", be an administrator of the associated process instance, or be an administrator of a scope that contains the activity instance. This method is not supported in archive mode. Parameters: aiid - The object ID of the activity instance the work item belongs to. assignmentReason - The reason why the work item has been assigned - refer to the work item assignment reasons . fromOwner - The user ID or the name of the group the work item currently belongs to. toOwner - The user ID or the name of the group the work item is to be transferred to. Work items can be transferred from a user to a user or from a group of users to a group of users. If the work item is transferred to a user, it is checked whether the user exists but the check may be executed case insensitively. The check can be suppressed by setting the 'SupportVirtualUserIdsForPeopleAssignments' custom property of the Human Task Manager configuration to 'true'. Throws: ApplicationVetoException ArchiveUnsupportedOperationException EngineEverybodyWorkItemException EngineNotAuthorizedException EngineParameterNullException EngineProcessReaderWorkItemException EngineWrongKindException EngineWrongStateException HumanTaskManagerException IdWrongFormatException InvalidLengthException UserDoesNotExistException WorkItemDoesNotExistException ObjectDoesNotExistException UnexpectedFailureException WorkItemManagerException java.rmi.RemoteException javax.ejb.EJBException Since: 5.1 Change History Release Modification 6.1.2 The caller may have administrator rights for the scope that contains the activity instance. 6.2.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### transferWorkItem

```
void transferWorkItem(AIID aiid,
                    int assignmentReason,
                    java.lang.String fromOwner,
                    java.lang.String toOwner)
                      throws ApplicationVetoException,
                             ArchiveUnsupportedOperationException,
                             EngineEverybodyWorkItemException,
                             EngineNotAuthorizedException,
                             EngineParameterNullException,
                             EngineProcessReaderWorkItemException,
                             EngineWrongKindException,
                             EngineWrongStateException,
                             HumanTaskManagerException,
                             IdWrongFormatException,
                             InvalidLengthException,
                             UserDoesNotExistException,
                             WorkItemDoesNotExistException,
                             ObjectDoesNotExistException,
                             UnexpectedFailureException,
                             WorkItemManagerException,
                             java.rmi.RemoteException,
                             javax.ejb.EJBException
```

Following restrictions apply:
 
When a work item with assignment reason "owner" is transferred and the caller is not
 an administrator, then the user the work item is transferred to must be an administrator
 or own the same work item with an assignment reason "potential owner".
 Work items with assignment reason "administrator" can only be transferred on the process instance.
 Work items with assignment reason "reader" can only be transferred, when the work item
 has not been propagated from the process instance, that is, when the work item  denotes
 an activity reader but no process reader.
 

 The activity instance must be in the claimed, ready, running, or stopped execution state.
 The associated process instance must be in the running, failing, or terminating execution state.
 The activity must be an invoke, script, or human task activity.
 A human task activity is also known as staff activity.
 
 The caller must own the work item with an assignment reason "owner",
 be an administrator of the associated process instance,
 or be an administrator of a scope that contains the activity instance.
 
 This method is not supported in archive mode.

Change History

Release
 Modification
 
6.1.2
 
 The caller may have administrator rights for the scope that contains the activity instance.
 
6.2.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- uninitializeCorrelationSet
void uninitializeCorrelationSet(java.lang.String piid,
                              java.lang.String correlationSetName)
                                throws ArchiveUnsupportedOperationException,
                                       EngineCorrelationSetDoesNotExistException,
                                       EngineNotAuthorizedException,
                                       EngineParameterNullException,
                                       EngineWrongStateException,
                                       IdWrongFormatException,
                                       IdWrongTypeException,
                                       ObjectDoesNotExistException,
                                       UnexpectedFailureException,
                                       java.rmi.RemoteException,
                                       javax.ejb.EJBException
Uninitializes the specified correlation set instance
 using a string representation of the process instance ID and the correlation set name.
 
 The process instance must be in the running, suspended, or failing execution state.
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - A string representation of the process instance object ID that is used to identify
    the process instance.correlationSetName - The name of the correlation set.
 
Throws:
ArchiveUnsupportedOperationException
EngineCorrelationSetDoesNotExistException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongStateException
IdWrongFormatException
IdWrongTypeException
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

- uninitializeCorrelationSet
void uninitializeCorrelationSet(PIID piid,
                              java.lang.String correlationSetName)
                                throws ArchiveUnsupportedOperationException,
                                       EngineCorrelationSetDoesNotExistException,
                                       EngineNotAuthorizedException,
                                       EngineParameterNullException,
                                       EngineWrongStateException,
                                       IdWrongFormatException,
                                       ObjectDoesNotExistException,
                                       UnexpectedFailureException,
                                       java.rmi.RemoteException,
                                       javax.ejb.EJBException
Uninitializes the specified correlation set instance
 using the process instance ID and the correlation set name.
 
 The process instance must be in the running, suspended, or failing execution state.
 The caller must be an administrator of the process instance.
 
 This method is not supported in archive mode.
Parameters:piid - The object ID of the process instance.correlationSetName - The name of the correlation set.
 
Throws:
ArchiveUnsupportedOperationException
EngineCorrelationSetDoesNotExistException
EngineNotAuthorizedException
EngineParameterNullException
EngineWrongStateException
IdWrongFormatException
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

- findQueryTableMetaData
java.util.List findQueryTableMetaData(MetaDataOptions metaDataOptions)
                                      throws ProcessException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Queries the meta data of query tables.
 
 You can specify options to limit the number of query tables
 for which the meta data is returned.
Parameters:metaDataOptions - The options to be applied - refer to MetaDataOptions.
    If no restrictions are to be applied, null can be specified.
 
Returns:List -
    A list of QueryTableMetaData objects.
 
Throws:
ProcessException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2.0.1

- getQueryTableMetaData
QueryTableMetaData getQueryTableMetaData(java.lang.String queryTableName,
                                       java.util.Locale locale)
                                         throws EngineParameterNullException,
                                                ProcessException,
                                                java.rmi.RemoteException,
                                                javax.ejb.EJBException
Returns the meta data of the specified query table.
Parameters:queryTableName - The name of the query table.locale - The locale that is used to calculate the value of the $LOCALE variable. If
    no locale is specified, defaults are used for the calculation.
 
Returns:QueryTableMetaData -
    The meta data of the query table -
    refer to QueryTableMetaData.
 
Throws:
EngineParameterNullException
ProcessException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2.0.1

- queryEntities
EntityResultSet queryEntities(java.lang.String queryTableName,
                            FilterOptions filterOptions,
                            AuthorizationOptions authorizationOptions,
                            java.util.List parameters)
                              throws EngineNotAuthorizedException,
                                     EngineParameterNullException,
                                     InvalidParameterException,
                                     UserDoesNotExistException,
                                     UserRegistryException,
                                     ProcessException,
                                     java.rmi.RemoteException,
                                     javax.ejb.EJBException
Queries entities using the specified query table.
 
 You can specify filter and authorization options to limit the number of entities returned
 and values for parameters used in query table filters and selection criteria.
Parameters:queryTableName - The name of the query table.filterOptions - The filter options to be applied in addition to any filters defined
    for the query table.
    Refer to FilterOptions.authorizationOptions - The authorization options to be applied in addition to any authorization
    specifications defined for the query table.
    
    Authorization options can be specified for predefined query tables that contain
    instance data or for composite query tables that define a primary query table which
    contains instance data and that use instance-based authorization.
    If authorization options are specified for query tables that do not contain instance
    but template data, an EngineNotAuthorizedException is thrown.
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
EngineNotAuthorizedException
EngineParameterNullException
InvalidParameterException
UserDoesNotExistException
UserRegistryException
ProcessException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
7.0
 
 Throws an InvalidParameterException when the list of parameters contains an object
 of a type other than com.ibm.bpe.api.Parameter.

- queryEntityCount
int queryEntityCount(java.lang.String queryTableName,
                   FilterOptions filterOptions,
                   AuthorizationOptions authorizationOptions,
                   java.util.List parameters)
                     throws EngineNotAuthorizedException,
                            EngineParameterNullException,
                            InvalidParameterException,
                            UserDoesNotExistException,
                            UserRegistryException,
                            ProcessException,
                            java.rmi.RemoteException,
                            javax.ejb.EJBException
Counts qualifying entities of a potential query for entities.
Parameters:queryTableName - The name of the query table.filterOptions - The filter options to limit the number of entities and attributes.
    Refer to FilterOptions.authorizationOptions - The authorization options to limit the number of entities.
    Refer to AuthorizationOptions or
    AdminAuthorizationOptions.parameters - A list of Parameter objects to replace parameters in the query condition.
    Refer to Parameter.
 
Returns:int -
    The number of qualifying entities.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
InvalidParameterException
UserDoesNotExistException
UserRegistryException
ProcessException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
7.0
 
 Throws an InvalidParameterException when the list of parameters contains an object
 of a type other than com.ibm.bpe.api.Parameter.

- queryRows
RowResultSet queryRows(java.lang.String queryTableName,
                     FilterOptions filterOptions,
                     AuthorizationOptions authorizationOptions,
                     java.util.List parameters)
                       throws EngineNotAuthorizedException,
                              EngineParameterNullException,
                              InvalidParameterException,
                              UserDoesNotExistException,
                              UserRegistryException,
                              ProcessException,
                              java.rmi.RemoteException,
                              javax.ejb.EJBException
Queries attributes using the specified query table.
 
 You can specify filter and authorization options to limit the number of rows returned
 and values for parameters used in query table filters and selection criteria.
Parameters:queryTableName - The name of the query table.filterOptions - The filter options to be applied in addition to any filters defined
    for the query table.
    Refer to FilterOptions.authorizationOptions - The authorization options to be applied in addition to any authorization
    specifications defined for the query table.
    
    Authorization options can be specified for predefined query tables that contain
    instance data or for composite query tables that define a primary query table which
    contains instance data and that use instance-based authorization.
    If authorization options are specified for query tables that do not contain instance
    but template data, an EngineNotAuthorizedException is thrown.
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
EngineNotAuthorizedException
EngineParameterNullException
InvalidParameterException
UserDoesNotExistException
UserRegistryException
ProcessException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
7.0
 
 Throws an InvalidParameterException when the list of parameters contains an object
 of a type other than com.ibm.bpe.api.Parameter.

- queryRowCount
int queryRowCount(java.lang.String queryTableName,
                FilterOptions filterOptions,
                AuthorizationOptions authorizationOptions,
                java.util.List parameters)
                  throws EngineNotAuthorizedException,
                         EngineParameterNullException,
                         InvalidParameterException,
                         UserDoesNotExistException,
                         UserRegistryException,
                         ProcessException,
                         java.rmi.RemoteException,
                         javax.ejb.EJBException
Counts qualifying objects of a potential query table query.
Parameters:queryTableName - The name of the query table.filterOptions - The filter options to limit the number of rows or attributes.
    Refer to FilterOptions.authorizationOptions - The authorization options to limit the number of rows.
    Refer to AuthorizationOptions or
    AdminAuthorizationOptions.parameters - A list of Parameter objects to replace parameters in the query condition.
    Refer to Parameter.
 
Returns:int -
    The number of qualifying objects in rows.
 
Throws:
EngineNotAuthorizedException
EngineParameterNullException
InvalidParameterException
UserDoesNotExistException
UserRegistryException
ProcessException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
6.2
 
Change History

Release
 Modification
 
7.0
 
 Throws an InvalidParameterException when the list of parameters contains an object
 of a type other than com.ibm.bpe.api.Parameter.