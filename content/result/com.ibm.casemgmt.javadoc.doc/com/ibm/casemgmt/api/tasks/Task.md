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

## Class Task

- java.lang.Object
    - com.ibm.casemgmt.api.tasks.Task

- Direct Known Subclasses:
DynamicTask

public class Task
extends java.lang.Object
Represents a task in IBM Case Manager. To obtain an instance of a Task object, use one of the factory 
 methods -- createPendingInstance or fetchInstance.
 
 A new task is first created in a pending state by using the factory method createPendingInstance. The 
 actual task is not created in the repository until save() is called.
 
 The factory method fetchInstance obtains an instance that represents an existing task. Information about 
 the state of the object, such as properties of the task, is fetched from the repository and maintained in the 
 returned instance.
 
 Once the Task instance is obtained, other methods, such as the method that enables a task, can be called 
 to modify the state of the object. Methods that modify the state of the object do not take effect until 
 save() is called to save the changes.
 
 Several methods establish an intent to perform some action when the task is saved. For example, the start 
 method establishes the intent to start the task. However, the task is not actually started until save() is
 called. Until that happens, the method getState will indicate that the task is still in the READY
 state, and not yet in the WORKING state. The API allows only a single action such as this to be established at a 
 time. Other methods, such as the method that enables a task, may or may not be able to be combined with certain 
 actions.

ID status:
ID review by David Newhall 16 May 2012

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description com.filenet.api.core.BatchItemHandle addToBatch (com.filenet.api.core.UpdatingBatch ub) Adds the changes represented by this instance to an UpdatingBatch instance. static Task createPendingInstance (java.lang.String taskTypeName, Case caseInstance) A factory method that returns an instance of Task that represents a pending task. static Task fetchInstance (ObjectStoreReference targetOS, com.filenet.api.util.Id taskId) A factory method that returns an instance of Task that represents an existing task. com.filenet.api.util.Id getCaseFolderId () Returns the ID of the parent Case folder associated with this Task object. CaseType getCaseType () Returns a CaseType object that represents the type of the parent Case associated with this Task object. java.lang.String getCreator () Returns the creator of the task. java.util.Date getDateCompleted () Returns the date that the task was completed. java.util.Date getDateCreated () Returns the date that the task was created. java.util.Date getDateLastModified () Returns the date that the task was last modified. java.util.Date getDateStarted () Returns the date that the task was started. java.lang.String getDefaultView () Returns the default view reference name for the task. TaskDisabledState getDisabledState () Returns the disabled state of the task. Task getDuplicateLaunchedTask () Returns the actual task that was created for the duplicate launch step, if a previous call to the save method threw an exception with the ErrorCategory of ErrorCategory.DUPLICATE\_LAUNCH . CaseType getFetchlessCaseType () com.filenet.api.util.Id getId () Returns the Id of this task. static Task getInstanceFromCmTask (com.filenet.api.core.CmTask cmTask) A factory method that returns an instance of Task that represents an existing task. java.lang.String getLastFailureReason () Returns the last failure reason of the task. java.util.Date getLastRestartDate () Returns the date that the task was last restarted, if any. TaskLaunchMode getLaunchMode () Returns the launch mode of the task. LaunchStep getLaunchStep () Retrieves the launch step used for launching the workflow associated with the new task. java.lang.String getName () Returns the name of the task. java.lang.String getProcessInstanceId () Returns the process instance ID that identifies the workflow associated with this task. java.lang.String getProcessPageTypeName () Returns a process page type that is associated bpm task type from the case configuration CaseMgmtProperties getProperties () Returns an object that contains the properties of this task. CaseMgmtProperties getProperties (boolean refreshTaskClassMetaData) TaskRequiredState getRequiredState () Returns the required state of the task. java.lang.Integer getRestartCount () Returns the number of times the task has been restarted. java.lang.String getRosterName () Returns the roster name. com.filenet.api.constants.TaskState getState () Returns the state of the task. TaskReference getTaskReference () Returns a TaskReference object that represents a reference to the Content Engine task object. java.lang.String getTaskTypeName () Returns the task type name of this task object. UnmodifiableProperties getUnmodifiableProperties () Returns an interface that allows users to read the properties of this task but not to not modify those properties. java.lang.Integer getUpdateSequenceNumber () Accesses the update sequence number of the Content Engine CmTask object associated with this Task instance. LaunchStep initializeInProgressLaunchStep (java.lang.String workObjectNumber) Initializes an in-progress launch step. LaunchStep initializeNewLaunchStep () Initializes a new launch step. boolean isContainer () Indicates whether this task is a container task. boolean isCreatePending () Indicates whether this instance is in a create pending state. boolean isCustomTask () Indicates whether this task is a Custom task. boolean isHidden () Indicates if this task should be hidden in a user interface. boolean isLaunchStepRequired () Indicates if a launch step must be initialized using either initializeNewLaunchStep() or initializeInProgressLaunchStep(). boolean isRestartPending () Indicates whether an intent has been established to restart the task. boolean isStartPending () Indicates whether the intent has been established to start the task. boolean isStopPending () Indicates whether an intent has been established to stop the task. boolean isTaskBPM () boolean isToDo () Indicates whether this task is a ToDo task. void refreshFromBatch (com.filenet.api.core.UpdatingBatch ub, com.filenet.api.core.BatchItemHandle bih) Refreshes this object after a batch execution. void save (com.filenet.api.constants.RefreshMode mode) Saves this task instance with any changes to the properties and any pending actions that have been established. void setCompleted () Establishes the intent to programatically complete a task. void setDisabled () Modifies the properties cache to disable the task. void setEnabled () Modifies the properties cache to enable the task. void setName (java.lang.String name) Specifies the name of the task. void setRestarted () Establishes the intent to restart the task. void setStarted () Establishes the intent to start the task. void setStopped () Establishes the intent to stop the task. void setUpdateSequenceNumber (java.lang.Integer usn) Specifies the update sequence number of the Content Engine CmTask object associated with this Task instance.

### Method Summary

| Modifier and Type                    | Method and Description                                                                                                                                                                                                  |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| com.filenet.api.core.BatchItemHandle | addToBatch(com.filenet.api.core.UpdatingBatch ub) Adds the changes represented by this instance to an UpdatingBatch instance.                                                                                           |
| static Task                          | createPendingInstance(java.lang.String taskTypeName,                      Case caseInstance) A factory method that returns an instance of Task that represents a pending task.                                          |
| static Task                          | fetchInstance(ObjectStoreReference targetOS,              com.filenet.api.util.Id taskId) A factory method that returns an instance of Task that represents an existing task.                                           |
| com.filenet.api.util.Id              | getCaseFolderId() Returns the ID of the parent Case folder associated with this Task object.                                                                                                                            |
| CaseType                             | getCaseType() Returns a CaseType object that represents the type of the parent Case associated with this Task object.                                                                                                   |
| java.lang.String                     | getCreator() Returns the creator of the task.                                                                                                                                                                           |
| java.util.Date                       | getDateCompleted() Returns the date that the task was completed.                                                                                                                                                        |
| java.util.Date                       | getDateCreated() Returns the date that the task was created.                                                                                                                                                            |
| java.util.Date                       | getDateLastModified() Returns the date that the task was last modified.                                                                                                                                                 |
| java.util.Date                       | getDateStarted() Returns the date that the task was started.                                                                                                                                                            |
| java.lang.String                     | getDefaultView() Returns the default view reference name for the task.                                                                                                                                                  |
| TaskDisabledState                    | getDisabledState() Returns the disabled state of the task.                                                                                                                                                              |
| Task                                 | getDuplicateLaunchedTask() Returns the actual task that was created for the duplicate launch step, if a previous call to the   save method threw an exception with the ErrorCategory of ErrorCategory.DUPLICATE\_LAUNCH. |
| CaseType                             | getFetchlessCaseType()                                                                                                                                                                                                  |
| com.filenet.api.util.Id              | getId() Returns the Id of this task.                                                                                                                                                                                    |
| static Task                          | getInstanceFromCmTask(com.filenet.api.core.CmTask cmTask) A factory method that returns an instance of Task that represents an existing task.                                                                           |
| java.lang.String                     | getLastFailureReason() Returns the last failure reason of the task.                                                                                                                                                     |
| java.util.Date                       | getLastRestartDate() Returns the date that the task was last restarted, if any.                                                                                                                                         |
| TaskLaunchMode                       | getLaunchMode() Returns the launch mode of the task.                                                                                                                                                                    |
| LaunchStep                           | getLaunchStep() Retrieves the launch step used for launching the workflow associated with the new task.                                                                                                                 |
| java.lang.String                     | getName() Returns the name of the task.                                                                                                                                                                                 |
| java.lang.String                     | getProcessInstanceId() Returns the process instance ID that identifies the workflow associated with this task.                                                                                                          |
| java.lang.String                     | getProcessPageTypeName() Returns a  process page type that is associated bpm task type from the case configuration                                                                                                      |
| CaseMgmtProperties                   | getProperties() Returns an  object that contains the properties of this task.                                                                                                                                           |
| CaseMgmtProperties                   | getProperties(boolean refreshTaskClassMetaData)                                                                                                                                                                         |
| TaskRequiredState                    | getRequiredState() Returns the required state of the task.                                                                                                                                                              |
| java.lang.Integer                    | getRestartCount() Returns the number of times the task has been restarted.                                                                                                                                              |
| java.lang.String                     | getRosterName() Returns the roster name.                                                                                                                                                                                |
| com.filenet.api.constants.TaskState  | getState() Returns the state of the task.                                                                                                                                                                               |
| TaskReference                        | getTaskReference() Returns a TaskReference object that represents a reference to the  Content Engine task object.                                                                                                       |
| java.lang.String                     | getTaskTypeName() Returns the task type name of this task object.                                                                                                                                                       |
| UnmodifiableProperties               | getUnmodifiableProperties() Returns an interface that allows users to read the properties of this task but not to   not modify those properties.                                                                        |
| java.lang.Integer                    | getUpdateSequenceNumber() Accesses the update sequence number of the Content Engine CmTask object associated with this  Task instance.                                                                                  |
| LaunchStep                           | initializeInProgressLaunchStep(java.lang.String workObjectNumber) Initializes an in-progress launch step.                                                                                                               |
| LaunchStep                           | initializeNewLaunchStep() Initializes a new launch step.                                                                                                                                                                |
| boolean                              | isContainer() Indicates whether this task is a container task.                                                                                                                                                          |
| boolean                              | isCreatePending() Indicates whether this instance is in a create pending state.                                                                                                                                         |
| boolean                              | isCustomTask() Indicates whether this task is a Custom task.                                                                                                                                                            |
| boolean                              | isHidden() Indicates if this task should be hidden in a user interface.                                                                                                                                                 |
| boolean                              | isLaunchStepRequired() Indicates if a launch step must be initialized using either initializeNewLaunchStep()  or initializeInProgressLaunchStep().                                                                      |
| boolean                              | isRestartPending() Indicates whether an intent has been established to restart the task.                                                                                                                                |
| boolean                              | isStartPending() Indicates whether the intent has been established to start the task.                                                                                                                                   |
| boolean                              | isStopPending() Indicates whether an intent has been established to stop the task.                                                                                                                                      |
| boolean                              | isTaskBPM()                                                                                                                                                                                                             |
| boolean                              | isToDo() Indicates whether this task is a ToDo task.                                                                                                                                                                    |
| void                                 | refreshFromBatch(com.filenet.api.core.UpdatingBatch ub,                 com.filenet.api.core.BatchItemHandle bih) Refreshes this object after a batch execution.                                                        |
| void                                 | save(com.filenet.api.constants.RefreshMode mode) Saves this task instance with any changes to the properties and any pending actions that have been established.                                                        |
| void                                 | setCompleted() Establishes the intent to programatically complete a task.                                                                                                                                               |
| void                                 | setDisabled() Modifies the properties cache to disable the task.                                                                                                                                                        |
| void                                 | setEnabled() Modifies the properties cache to enable the task.                                                                                                                                                          |
| void                                 | setName(java.lang.String name) Specifies the name of the task.                                                                                                                                                          |
| void                                 | setRestarted() Establishes the intent to restart the task.                                                                                                                                                              |
| void                                 | setStarted() Establishes the intent to start the task.                                                                                                                                                                  |
| void                                 | setStopped() Establishes the intent to stop the task.                                                                                                                                                                   |
| void                                 | setUpdateSequenceNumber(java.lang.Integer usn) Specifies the update sequence number of the Content Engine CmTask object associated with this  Task instance.                                                            |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait