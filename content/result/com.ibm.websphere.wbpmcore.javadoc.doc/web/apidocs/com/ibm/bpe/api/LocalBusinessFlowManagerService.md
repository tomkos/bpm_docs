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

## Interface LocalBusinessFlowManagerService

- All Superinterfaces:
BusinessFlowManagerService

All Known Subinterfaces:
LocalBusinessFlowManager

public interface LocalBusinessFlowManagerService
extends BusinessFlowManagerService
LocalBusinessFlowManagerService defines the business functions that can be called by a local client.
Since:
6.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

### Method Summary

- Methods inherited from interface com.ibm.bpe.api.BusinessFlowManagerService
call, call, call, call, callServiceWithReplyContext, callServiceWithReplyContext, callWithReplyContext, callWithReplyContext, callWithReplyContext, callWithReplyContext, callWithUISettings, callWithUISettings, callWithUISettings, cancelClaim, cancelClaim, cancelClaim, cancelClaim, cancelSkipRequest, cancelSkipRequest, cancelSkipRequest, cancelSkipRequest, claim, claim, claim, claimProcessOwnership, claimProcessOwnership, complete, complete, complete, complete, complete, complete, completeAndClaimSuccessor, completeAndClaimSuccessor, completeAndJump, completeAndJump, completeAndJump, completeAndJump, createMessage, createMessage, createMessage, createMessage, createMessage, createMessage, createMessage, createMessageWithCorrelationSets, createMessageWithCorrelationSets, createMessageWithCorrelationSets, createMessageWithCorrelationSets, createMessageWithCorrelationSetsForEventHandler, createMessageWithCorrelationSetsForEventHandler, createStoredQuery, createStoredQuery, createStoredQuery, createWorkItem, createWorkItem, createWorkItem, delete, delete, deleteStoredQuery, deleteStoredQuery, deleteWorkItem, deleteWorkItem, deleteWorkItem, deleteWorkList, executeWorkList, findQueryTableMetaData, forceComplete, forceComplete, forceComplete, forceComplete, forceComplete, forceComplete, forceCompleteAndJump, forceCompleteAndJump, forceForEachCounterValues, forceForEachCounterValues, forceJoinCondition, forceJoinCondition, forceLoopCondition, forceLoopCondition, forceNavigate, forceNavigate, forceNavigate, forceNavigate, forceRetry, forceRetry, forceRetry, forceRetry, forceRetry, forceRetry, forceRetry, forceRetry, forceTerminate, forceTerminate, forceTerminate, forceTerminate, getActiveEventHandlers, getActiveEventHandlers, getActivityInstance, getActivityInstance, getActivityInstance, getActivityInstance, getActivityServiceTemplate, getActivityServiceTemplate, getAllActivities, getAllActivities, getAllBasicActivityNames, getAllBasicActivityNames, getAllCustomProperties, getAllCustomProperties, getAllCustomProperties, getAllQueryProperties, getAllVariableNames, getAllVariableNames, getAllVariableNames, getAllVariableNames, getAllVariableNames, getAllWorkItems, getAllWorkItems, getAllWorkItems, getAvailableActionFlags, getAvailableActionFlags, getAvailableActionFlags, getBfmConfiguration, getBinaryCustomProperty, getBinaryCustomProperty, getBinaryCustomProperty, getBinaryCustomProperty, getBinaryCustomProperty, getBinaryCustomPropertyNames, getBinaryCustomPropertyNames, getBinaryCustomPropertyNames, getBinaryCustomPropertyNames, getBinaryCustomPropertyNames, getBranches, getBranches, getClientUISettings, getClientUISettings, getClientUISettings, getClientUISettings, getClientUISettings, getClientUISettings, getCorrelationSetInstances, getCorrelationSetInstances, getCorrelationSetInstances, getCorrelationSetInstances, getCustomProperties, getCustomProperties, getCustomProperties, getCustomProperties, getCustomProperties, getCustomProperties, getCustomProperty, getCustomProperty, getCustomProperty, getCustomProperty, getCustomProperty, getCustomProperty, getCustomPropertyInfo, getCustomPropertyNames, getCustomPropertyNames, getCustomPropertyNames, getCustomPropertyNames, getCustomPropertyNames, getCustomPropertyNames, getFaultMessage, getFaultMessage, getFaultMessage, getFaultNames, getFaultNames, getGraphics, getGraphics, getInitialVariableValue, getInitialVariableValue, getInitialVariableValue, getInitialVariableValue, getInitialVariableValue, getInlineCustomProperty, getInlineCustomProperty, getInlineCustomProperty, getInputClientUISettings, getInputClientUISettings, getInputMessage, getInputMessage, getInputMessage, getInputVariableNames, getInputVariableNames, getInputVariableNames, getInputVariableNames, getJumpTargetNames, getJumpTargetNames, getMappingToGraphics, getMappingToGraphics, getMessageTextOfException, getMigrationTargets, getMigrationTargets, getOperationMode, getOutgoingLinks, getOutgoingLinks, getOutputClientUISettings, getOutputClientUISettings, getOutputMessage, getOutputMessage, getOutputMessage, getOutputVariableNames, getOutputVariableNames, getOutputVariableNames, getOutputVariableNames, getParticipatingTaskID, getParticipatingTaskID, getProcessInstance, getProcessInstance, getProcessTemplate, getProcessTemplate, getQueryProperties, getQueryProperties, getQueryTableMetaData, getStartActivities, getStartActivities, getStoredQuery, getStoredQuery, getStoredQuery, getStoredQueryNames, getStoredQueryNames, getStoredQueryNames, getUsersInRole, getUsersInRole, getUsersInRole, getVariable, getVariable, getVariable, getVariable, getVariable, getVariableNames, getVariableNames, getVariableNames, getVariableNames, getVariableNames, getWaitingActivities, getWaitingActivities, getWorkItems, getWorkItems, getWorkItems, getWorkList, getWorkListActions, getWorkListNames, initializeCorrelationSet, initializeCorrelationSet, initiate, initiate, initiate, initiate, initiateAndClaimFirst, initiateAndClaimFirst, initiateAndClaimFirst, initiateAndClaimFirst, initiateAndClaimFirst, initiateAndClaimFirst, initiateAndSuspend, initiateAndSuspend, initiateAndSuspend, initiateAndSuspend, isBusinessProcessAdministrator, isBusinessProcessMonitor, jump, jump, migrate, migrate, newWorkList, query, query, query, query, query, query, query, query, queryAll, queryEntities, queryEntityCount, queryProcessTemplates, queryRowCount, queryRows, rescheduleTimer, rescheduleTimer, restart, restart, resume, resume, sendMessage, sendMessage, sendMessage, sendMessage, sendMessage, sendMessage, sendMessage, sendMessage, setBinaryCustomProperty, setBinaryCustomProperty, setBinaryCustomProperty, setBinaryCustomProperty, setBinaryCustomProperty, setCustomProperty, setCustomProperty, setCustomProperty, setCustomProperty, setCustomProperty, setFaultMessage, setFaultMessage, setInlineCustomProperties, setInlineCustomProperties, setInlineCustomProperty, setInlineCustomProperty, setInlineCustomProperty, setInlineCustomProperty, setOutputMessage, setOutputMessage, setVariable, setVariable, setVariable, setVariable, setVariable, skip, skip, skip, skip, skipAndJump, skipAndJump, suspend, suspend, suspend, suspend, suspend, suspend, suspend, suspend, testMigration, testMigration, transferWorkItem, transferWorkItem, transferWorkItem, uninitializeCorrelationSet, uninitializeCorrelationSet