- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class DynamicTask

- java.lang.Object
    - com.ibm.casemgmt.api.tasks.Task
        - com.ibm.casemgmt.api.tasks.DynamicTask

- public class DynamicTask
extends Task
Represents a custom task in IBM Case Manager. To obtain an instance of a DynamicTask object, use one of the 
 following factory methods: createPendingInstance or fetchInstance.
 
 To create a new custom task, call the factory method createPendingInstance. This method creates the custom task
 in a pending state. The actual task is not created in the repository until you call the save() method.
 
 To obtain an instance that represents an existing task, call the factory method fetchInstance. This method fetches
 information about the state of the object, such as properties of the task, from the repository. The information is
 maintained in the returned instance.
 
 After a Task instance is obtained, call other methods, such as the method that enables a task, 
 to modify the state of the object. Methods that modify the state of the object do not take effect until 
 you call the save() method to save the changes.
 
 Several methods establish an intent to perform some action when the task is saved. For example, the start 
 method establishes the intent to start the task. However, the task is not started until you call the save() 
 method. Before the save() is called, the method getState indicates that the task is still in the READY
 state, and not yet in the WORKING state. Only a single action such as this can be established at a 
 time. Other methods, such as the method that enables a task, might or might not be able to be combined with certain 
 actions.

ID status:
ID review by Frankie Mosher, 19 Dec 2012.

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description com.filenet.api.core.BatchItemHandle addToBatch (com.filenet.api.core.UpdatingBatch ub) The Dynamic Task does not support batch operations. static DynamicTask createPendingInstance (java.lang.String taskName, boolean valid, java.lang.String flowJson, Case caseInstance) A factory method that returns an instance of DynamicTask that represents a pending dynamic task. java.lang.String getFlowData () Returns a String object that represents the flow data currently set on the task. boolean isFlowDataValid () Returns a boolean that indicates if the flow data currently stored on the task object is valid. void refreshFromBatch (com.filenet.api.core.UpdatingBatch ub, com.filenet.api.core.BatchItemHandle bih) The Dynamic Task does not support batch operations. void save (com.filenet.api.constants.RefreshMode mode) Saves this task instance with any changes to the properties and any pending actions that have been established. void setFlowData (java.lang.String taskName, boolean valid, java.lang.String flowJson) Specifies the flow data of the task. void setStarted () Establishes the intent to start the task.

### Method Summary

| Modifier and Type                    | Method and Description                                                                                                                                                                                                                                                        |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| com.filenet.api.core.BatchItemHandle | addToBatch(com.filenet.api.core.UpdatingBatch ub) The Dynamic Task does not support batch operations.                                                                                                                                                                         |
| static DynamicTask                   | createPendingInstance(java.lang.String taskName,                      boolean valid,                      java.lang.String flowJson,                      Case caseInstance) A factory method that returns an instance of DynamicTask that represents a pending dynamic task. |
| java.lang.String                     | getFlowData() Returns a String object that represents the flow data currently set on the task.                                                                                                                                                                                |
| boolean                              | isFlowDataValid() Returns a boolean that indicates if the flow data currently stored on the  task object is valid.                                                                                                                                                            |
| void                                 | refreshFromBatch(com.filenet.api.core.UpdatingBatch ub,                 com.filenet.api.core.BatchItemHandle bih) The Dynamic Task does not support batch operations.                                                                                                         |
| void                                 | save(com.filenet.api.constants.RefreshMode mode) Saves this task instance with any changes to the properties and any pending actions that have been established.                                                                                                              |
| void                                 | setFlowData(java.lang.String taskName,            boolean valid,            java.lang.String flowJson) Specifies the flow data of the task.                                                                                                                                   |
| void                                 | setStarted() Establishes the intent to start the task.                                                                                                                                                                                                                        |

    - Methods inherited from class com.ibm.casemgmt.api.tasks.Task
createPendingInstance, fetchInstance, getCaseFolderId, getCaseType, getCreator, getDateCompleted, getDateCreated, getDateLastModified, getDateStarted, getDefaultView, getDisabledState, getDuplicateLaunchedTask, getFetchlessCaseType, getId, getInstanceFromCmTask, getLastFailureReason, getLastRestartDate, getLaunchMode, getLaunchStep, getName, getProcessInstanceId, getProcessPageTypeName, getProperties, getProperties, getRequiredState, getRestartCount, getRosterName, getState, getTaskReference, getTaskTypeName, getUnmodifiableProperties, getUpdateSequenceNumber, initializeInProgressLaunchStep, initializeNewLaunchStep, isContainer, isCreatePending, isCustomTask, isHidden, isLaunchStepRequired, isRestartPending, isStartPending, isStopPending, isTaskBPM, isToDo, setCompleted, setDisabled, setEnabled, setName, setRestarted, setStopped, setUpdateSequenceNumber
    - Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait