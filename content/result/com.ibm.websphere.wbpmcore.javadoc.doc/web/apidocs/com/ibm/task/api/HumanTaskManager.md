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

## Interface HumanTaskManager

- All Superinterfaces:
BusinessCategoryManagerService, javax.ejb.EJBObject, HumanTaskManagerService, java.rmi.Remote, WorkBasketManagerService

public interface HumanTaskManager
extends javax.ejb.EJBObject, HumanTaskManagerService, BusinessCategoryManagerService, WorkBasketManagerService
Remote EJB interface for Enterprise Bean: HumanTaskManager

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

### Method Summary

- Methods inherited from interface javax.ejb.EJBObject
getEJBHome, getHandle, getPrimaryKey, isIdentical, remove

- Methods inherited from interface com.ibm.task.api.HumanTaskManagerService
bulkTransferWorkItem, bulkTransferWorkItem, bulkTransferWorkItem, callTask, callTask, cancelClaim, cancelClaim, cancelClaim, cancelClaim, cancelClaim, cancelClaim, claim, claim, claim, claim, claim, claim, complete, complete, complete, complete, complete, complete, complete, complete, completeWithFollowOnTask, completeWithFollowOnTask, completeWithNewFollowOnTask, completeWithNewFollowOnTask, completeWithNewFollowOnTask, completeWithNewFollowOnTask, createAndCallTask, createAndCallTask, createAndCallTask, createAndStartTask, createAndStartTask, createAndStartTask, createAndStartTask, createAndStartTaskAsSubTask, createAndStartTaskAsSubTask, createAndStartTaskAsSubTask, createAndStartTaskAsSubTask, createAndStartTaskAsSubTask, createAndStartTaskAsSubTask, createFaultMessage, createFaultMessage, createFaultMessage, createInputMessage, createInputMessage, createInputMessage, createMessage, createMessage, createOutputMessage, createOutputMessage, createOutputMessage, createStoredQuery, createStoredQuery, createStoredQuery, createTask, createTask, createTask, createTask, createTask, createTask, createTaskTemplate, createWorkItem, createWorkItem, createWorkItem, delete, delete, delete, delete, deleteStoredQuery, deleteStoredQuery, deleteWorkItem, deleteWorkItem, deleteWorkItem, findQueryTableMetaData, getAbsence, getAbsence, getActivityID, getActivityID, getAllCustomProperties, getAllCustomProperties, getAllCustomProperties, getAllWorkItems, getAllWorkItems, getAllWorkItems, getApplicationComponent, getApplicationComponent, getAvailableActionFlags, getAvailableActionFlags, getAvailableActionFlags, getAvailableActions, getAvailableActions, getAvailableActions, getAvailableActions, getAvailableActions, getBinaryCustomProperty, getBinaryCustomProperty, getBinaryCustomProperty, getBinaryCustomPropertyNames, getBinaryCustomPropertyNames, getBinaryCustomPropertyNames, getCustomProperties, getCustomProperties, getCustomProperties, getCustomProperties, getCustomProperties, getCustomProperty, getCustomProperty, getCustomProperty, getCustomProperty, getCustomProperty, getCustomPropertyInfo, getCustomPropertyNames, getCustomPropertyNames, getCustomPropertyNames, getCustomPropertyNames, getCustomPropertyNames, getDocumentation, getDocumentation, getDocumentation, getDocumentation, getDocumentation, getEscalation, getEscalation, getEscalation, getEscalation, getEscalationInfo, getEscalationInfo, getEscalationTemplate, getEscalationTemplate, getFaultMessage, getFaultMessage, getFaultNames, getFaultNames, getFaultNames, getGroupDetails, getGroupNames, getHtmConfiguration, getInlineCustomProperty, getInlineCustomProperty, getInlineCustomProperty, getInputMessage, getInputMessage, getMessageTextOfException, getOperationMode, getOutputMessage, getOutputMessage, getProcessID, getProcessID, getQueryTableMetaData, getStoredQuery, getStoredQuery, getStoredQuery, getStoredQueryNames, getStoredQueryNames, getStoredQueryNames, getSubstitutes, getSubstitutes, getSubTaskIDs, getSubTaskIDs, getTask, getTask, getTaskAndMarkRead, getTaskAndMarkRead, getTaskHistory, getTaskHistory, getTaskRead, getTaskRead, getTaskTemplate, getTaskTemplate, getUISettings, getUISettings, getUISettings, getUserDetails, getUsersInRole, getUsersInRole, getUsersInRole, getUserSubstitutionDetail, getUserSubstitutionDetail, getWorkItems, getWorkItems, getWorkItems, isSystemAdministrator, isSystemMonitor, isUserInRole, isUserInRole, isUserInRole, query, query, query, query, query, query, query, query, queryAll, queryEntities, queryEntityCount, queryRowCount, queryRows, queryTaskTemplates, resolveStaffQuery, restart, restart, resume, resume, searchGroupDetails, searchUserDetails, setAbsence, setAbsence, setBinaryCustomProperty, setBinaryCustomProperty, setBinaryCustomProperty, setCustomProperties, setCustomProperties, setCustomProperty, setCustomProperty, setCustomProperty, setCustomProperty, setCustomProperty, setFaultMessage, setFaultMessage, setInlineCustomProperties, setInlineCustomProperties, setInlineCustomProperty, setInlineCustomProperty, setInlineCustomProperty, setInlineCustomProperty, setInputMessage, setInputMessage, setOutputMessage, setOutputMessage, setSubstitutes, setSubstitutes, setTaskRead, setTaskRead, setUserSubstitutionDetail, setUserSubstitutionDetail, startTask, startTask, startTaskAsSubTask, startTaskAsSubTask, startTaskTemplate, startTaskTemplate, stopTaskTemplate, stopTaskTemplate, suspend, suspend, suspend, suspend, suspend, suspend, suspend, suspend, suspendAndCancelClaim, suspendAndCancelClaim, suspendAndCancelClaim, suspendAndCancelClaim, suspendAndCancelClaim, suspendAndCancelClaim, terminate, terminate, transferToWorkBasket, transferToWorkBasket, transferWorkItem, transferWorkItem, transferWorkItem, transferWorkItem, transferWorkItem, transferWorkItem, triggerEscalation, triggerEscalation, update, update, update, update

- Methods inherited from interface com.ibm.task.api.BusinessCategoryManagerService
createBusinessCategory, createBusinessCategory, createBusinessCategory, deleteBusinessCategory, deleteBusinessCategory, getAllWorkItemsForBusinessCategory, getAllWorkItemsForBusinessCategory, getAvailableActionFlagsForBusinessCategories, getAvailableActionFlagsForBusinessCategories, getAvailableActionsForBusinessCategory, getAvailableActionsForBusinessCategory, getBusinessCategory, getBusinessCategory, getBusinessCategoryDefinition, getBusinessCategoryDefinition, getWorkItemsForBusinessCategory, getWorkItemsForBusinessCategory, isBusinessCategorySystemAdministrator, setBusinessCategoryOnTasks, setBusinessCategoryOnTasks, setParentBusinessCategory, setParentBusinessCategory, setPriorityOfBusinessCategories, setPriorityOfBusinessCategories, updateBusinessCategory

- Methods inherited from interface com.ibm.task.api.WorkBasketManagerService
createWorkBasket, deleteWorkBasket, deleteWorkBasket, distributeTasksToWorkBasket, distributeTasksToWorkBasket, getAllWorkItemsForWorkBasket, getAllWorkItemsForWorkBasket, getAvailableActionFlagsForWorkBaskets, getAvailableActionFlagsForWorkBaskets, getAvailableActionsForWorkBasket, getAvailableActionsForWorkBasket, getDistributionTargets, getDistributionTargets, getWorkBasket, getWorkBasket, getWorkBasketDefinition, getWorkBasketDefinition, getWorkItemsForWorkBasket, getWorkItemsForWorkBasket, isWorkBasketSystemAdministrator, removeAsDistributionTarget, removeAsDistributionTarget, transferTasksToWorkBasket, transferTasksToWorkBasket, updateWorkBasket