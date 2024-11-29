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

## Interface APIEventHandlerPlugin

- All Known Subinterfaces:
APIEventHandlerPlugin2, APIEventHandlerPlugin3, APIEventHandlerPlugin4, APIEventHandlerPlugin5, APIEventHandlerPlugin6

All Known Implementing Classes:
APIEventHandler

public interface APIEventHandlerPlugin
This interface supports the creation of API event handlers.
 
 API events occur when a human task changes its state or when a task property is
 updated. These events can be used by other components and applications to
 participate in state transitions of human tasks. Use the APIEventHandlerPlugin
 service provider interface (SPI) to create plug-ins to get informed about
 events send by the API or the internal events that have equivalent API
 events.
 
 To handle API events, the event handler is invoked directly before a
 modification is done (pre-event method) and after the modification is done
 (post-event method).
 
 This interface provides methods that are called when an API pre event or
 post event occurs.
Since:
6.0
Version:
7.0.0

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

void
postCallTask(Task task,
            java.io.Serializable inputMessage,
            java.io.Serializable returnMessage,
            TaskException taskException)
This method is called after a "CALL TASK" request was executed.

void
postCancelClaim(Task task,
               TaskException taskException)
This method is called after a "CANCEL CLAIM" request was executed.

void
postClaim(Task task,
         java.lang.Object inputMessage,
         TaskException taskException)
Deprecated. 
since v6.0.2 - use postClaim(Task, Serializable, TaskException)

void
postComplete(Task task,
            java.io.Serializable outputMessage,
            java.lang.String faultName,
            java.io.Serializable faultMessage,
            TaskException taskException)
This method is called after a "COMPLETE" request was executed.

void
postCompleteWithFollowOnTask(Task task,
                            Task previousTask,
                            TaskException taskException)
This method is called after a "COMPLETE WITH FOLLOW-ON TASK" request
 was executed.

void
postCompleteWithNewFollowOnTask(Task newTask,
                               TaskModel newTaskModel,
                               TaskTemplate template,
                               Task previousTask,
                               java.io.Serializable inputMessage,
                               TaskException taskException)
This method is called after a "COMPLETE WITH NEW FOLLOW-ON TASK" request
 was executed.

void
postCreateAndCallTask(Task task,
                     TaskModel newTaskModel,
                     TaskTemplate template,
                     java.io.Serializable inputMessage,
                     TaskException taskException)
This method is called after a "CREATE AND CALL TASK" request was executed.

void
postCreateAndStartTask(Task newTask,
                      TaskModel newTaskModel,
                      TaskTemplate template,
                      java.io.Serializable inputMessage,
                      ReplyHandler replyHandler,
                      TaskException taskException)
This method is called after a "CREATE AND START TASK" request was executed.

void
postCreateAndStartTaskAsSubTask(Task newTask,
                               TaskModel newTaskModel,
                               TaskTemplate template,
                               Task parentTask,
                               java.io.Serializable inputMessage,
                               TaskException taskException)
This method is called after a "CREATE AND START TASK AS SUBTASK" request was executed.

void
postCreateTask(Task newTask,
              TaskModel newTaskModel,
              TaskTemplate template,
              java.io.Serializable inputMessage,
              ReplyHandler replyHandler,
              TaskException taskException)
This method is called after a "CREATE TASK" request was executed.

void
postCreateWorkItem(Task task,
                  int assignmentReason,
                  java.lang.String id,
                  TaskException taskException)
This method is called after a "CREATE WORKITEM" request was executed.

void
postDeleteTask(Task task,
              TaskException taskException)
This method is called after a 2DELETE TASK" request was executed.

void
postDeleteWorkItem(Task task,
                  int assignmentReason,
                  java.lang.String id,
                  TaskException taskException)
This method is called after a "DELETE WORKITEM" request was executed.

void
postReplaceWorkItem(Task task,
                   int assignmentReason,
                   java.lang.String staffQuery,
                   TaskException taskException)
Deprecated. 
since v7.0 - this method is not used.

void
postRestartTask(Task task,
               TaskException taskException)
This method is called after a "RESTART TASK" request was executed.

void
postResumeTask(Task task,
              TaskException taskException)
This method is called after a "RESUME TASK" request was executed.

void
postSetBinaryCustomProperty(Task task,
                           java.lang.String propertyName,
                           java.lang.String dataType,
                           java.io.Serializable propertyValue,
                           TaskException taskException)
Deprecated. 
since v6.0.2 - use postSetBinaryCustomProperty(Task, BinaryCustomProperty)

void
postSetCustomProperty(Task task,
                     java.lang.String propertyName,
                     java.lang.String propertyValue,
                     TaskException taskException)
This method is called after a "SET CUSTOM PROPERTY" request was executed.

void
postSetFaultMessage(Task task,
                   java.lang.String faultName,
                   java.io.Serializable faultMessage,
                   TaskException taskException)
This method is called after a "SET FAULT MESSAGE" request was executed.

void
postSetOutputMessage(Task task,
                    java.io.Serializable outputMessage,
                    TaskException taskException)
This method is called after a "SET OUTPUT MESSAGE" request was executed.

void
postStartTask(Task task,
             java.io.Serializable inputMessage,
             ReplyHandler replyHandler,
             TaskException taskException)
This method is called after a "START TASK" request was executed.

void
postStartTaskAsSubTask(Task task,
                      Task parentTask,
                      java.io.Serializable inputMessage,
                      TaskException taskException)
This method is called after a "START TASK AS SUBTASK" request was executed.

void
postSuspendTask(Task task,
               TaskException taskException)
This method is called after a "SUSPEND TASK" request was executed.

void
postTerminateTask(Task task,
                 TaskException taskException)
This method is called after a "TERMINATE TASK" request was executed.

void
postTransferWorkItem(Task task,
                    int assignmentReason,
                    java.lang.String fromUserId,
                    java.lang.String toUserId,
                    TaskException taskException)
This method is called after a "TRANSFER WORKITEM" request was executed.

void
postUpdateInactiveTask(Task task,
                      java.io.Serializable inputMessage,
                      ReplyHandler replyHandler,
                      TaskException taskException)
This method is called after a "UPDATE INACTIVE TASK" request was executed.

void
postUpdateTask(Task task,
              TaskException taskException)
This method is called after a "UPDATE TASK" request was executed.

void
preCallTask(Task task,
           java.io.Serializable inputMessage)
This method is called before a "CALL TASK" request is executed.

void
preCancelClaim(Task task)
This method is called before a "CANCEL CLAIM" request is executed.

void
preClaim(Task task)
This method is called before a "CLAIM" request is executed.

void
preComplete(Task task)
This method is called before a "COMPLETE" request is executed.

void
preCompleteWithFollowOnTask(Task task,
                           Task previousTask)
This method is called before a "COMPLETE WITH FOLLOW-ON TASK" request
 is executed.

void
preCompleteWithNewFollowOnTask(TaskModel newTaskModel,
                              TaskTemplate template,
                              Task previousTask)
This method is called before a "COMPLETE WITH NEW FOLLOW-ON TASK" request
 is executed.

void
preCreateAndCallTask(TaskModel newTaskModel,
                    TaskTemplate template,
                    java.io.Serializable inputMessage)
This method is called before a "CREATE AND CALL TASK" request is executed.

void
preCreateAndStartTask(TaskModel newTaskModel,
                     TaskTemplate template,
                     java.io.Serializable inputMessage,
                     ReplyHandler replyHandler)
This method is called before a "CREATE AND START TASK" request is executed.

void
preCreateAndStartTaskAsSubTask(TaskModel newTaskModel,
                              TaskTemplate template,
                              Task parentTask,
                              java.io.Serializable inputMessage)
This method is called before a "CREATE AND START TASK AS SUBTASK" request
 is executed.

void
preCreateTask(TaskModel newTaskModel,
             TaskTemplate template,
             java.io.Serializable inputMessage,
             ReplyHandler replyHandler)
This method is called before a "CREATE TASK" request is executed.

void
preCreateWorkItem(Task task,
                 int assignmentReason,
                 java.lang.String id)
This method is called before a "CREATE WORKITEM" request is executed.

void
preDeleteTask(Task task)
This method is called before a "DELETE TASK" request is executed.

void
preDeleteWorkItem(Task task,
                 int assignmentReason,
                 java.lang.String id)
This method is called before a "DELETE WORKITEM" request is executed.

void
preReplaceWorkItem(Task task,
                  int assignmentReason,
                  java.lang.String staffQuery)
Deprecated. 
since v7.0 - this method is not used.

void
preRestartTask(Task task)
This method is called before a "RESTART TASK" request is executed.

void
preResumeTask(Task task)
This method is called before a "RESUME TASK" request is executed.

void
preSetBinaryCustomProperty(Task task,
                          java.lang.String propertyName,
                          java.lang.String dataType,
                          java.io.Serializable propertyValue)
Deprecated. 
since v6.0.2 - use preSetBinaryCustomProperty(Task, BinaryCustomProperty)

void
preSetCustomProperty(Task task,
                    java.lang.String propertyName,
                    java.lang.String propertyValue)
This method is called before a "SET CUSTOM PROPERTY" request is executed.

void
preSetFaultMessage(Task task,
                  java.lang.String faultName,
                  java.io.Serializable faultMessage)
This method is called before a "SET FAULT MESSAGE" request is executed.

void
preSetOutputMessage(Task task,
                   java.io.Serializable outputMessage)
This method is called before a "SET OUTPUT MESSAGE" request is executed.

void
preStartTask(Task task,
            java.io.Serializable inputMessage,
            ReplyHandler replyHandler)
This method is called before a "START TASK" request is executed.

void
preStartTaskAsSubTask(Task task,
                     Task parentTask,
                     java.io.Serializable inputMessage)
This method is called before a "START TASK AS SUBTASK" request is executed.

void
preSuspendTask(Task task)
This method is called before a "SUSPEND TASK" request is executed.

void
preTerminateTask(Task task)
This method is called before a "TERMINATE TASK" request is executed.

void
preTransferWorkItem(Task task,
                   int assignmentReason,
                   java.lang.String fromUserId,
                   java.lang.String toUserId)
This method is called before a "TRANSFER WORKITEM" request is executed.

void
preUpdateInactiveTask(Task task,
                     TaskModel model,
                     java.io.Serializable inputMessage,
                     ReplyHandler replyHandler)
This method is called before a "UPDATE INACTIVE TASK" request is executed.

void
preUpdateTask(Task task)
This method is called before a "UPDATE TASK" request is executed.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - preCallTask
void preCallTask(Task task,
               java.io.Serializable inputMessage)
                 throws ApplicationVetoException
This method is called before a "CALL TASK" request is executed.
Parameters:task - The task to be called.inputMessage - The input message - may be null.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postCallTask
void postCallTask(Task task,
                java.io.Serializable inputMessage,
                java.io.Serializable returnMessage,
                TaskException taskException)
This method is called after a "CALL TASK" request was executed.
Parameters:task - task that has been 'called'inputMessage - The input message - may be null.returnMessage - The return message - may be null.taskException - The TaskException that occurred or null if no exception occurred.
    - preCancelClaim
void preCancelClaim(Task task)
                    throws ApplicationVetoException
This method is called before a "CANCEL CLAIM" request is executed.
Parameters:task - The task that has been claimed and where the claim is to be canceled.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postCancelClaim
void postCancelClaim(Task task,
                   TaskException taskException)
This method is called after a "CANCEL CLAIM" request was executed.
Parameters:task - The task that has been claimed and where the claim was requested to be canceled.taskException - The TaskException that occurred or null if no exception occurred.
    - preClaim
void preClaim(Task task)
              throws ApplicationVetoException
This method is called before a "CLAIM" request is executed.
Parameters:task - The task to be claimed.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postClaim
void postClaim(Task task,
             java.lang.Object inputMessage,
             TaskException taskException)
Deprecated. since v6.0.2 - use postClaim(Task, Serializable, TaskException)
This method is called after a "CLAIM" request was executed.
Parameters:task - The task that was requested to be claimed.inputMessage - The input message.taskException - The TaskException that occurred or null if no exception occurred.
    - preComplete
void preComplete(Task task)
                 throws ApplicationVetoException
This method is called before a "COMPLETE" request is executed.
Parameters:task - The task to be completed.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postComplete
void postComplete(Task task,
                java.io.Serializable outputMessage,
                java.lang.String faultName,
                java.io.Serializable faultMessage,
                TaskException taskException)
This method is called after a "COMPLETE" request was executed.
Parameters:task - The task that was requested to be completed.outputMessage - The output message - may be null.faultName - The fault name if a fault message is passed.faultMessage - The fault message -may be null.taskException - The TaskException that occurred or null if no exception occurred.
    - preCompleteWithFollowOnTask
void preCompleteWithFollowOnTask(Task task,
                               Task previousTask)
                                 throws ApplicationVetoException
This method is called before a "COMPLETE WITH FOLLOW-ON TASK" request
 is executed.
Parameters:task - The task to be started.previousTask - The predecessor task to be completed.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postCompleteWithFollowOnTask
void postCompleteWithFollowOnTask(Task task,
                                Task previousTask,
                                TaskException taskException)
This method is called after a "COMPLETE WITH FOLLOW-ON TASK" request
 was executed.
Parameters:task - The task that was requested to be started.previousTask - The predecessor task that was requested to be completed.taskException - The TaskException that occurred or null if no exception occurred.
    - preCompleteWithNewFollowOnTask
void preCompleteWithNewFollowOnTask(TaskModel newTaskModel,
                                  TaskTemplate template,
                                  Task previousTask)
                                    throws ApplicationVetoException
This method is called before a "COMPLETE WITH NEW FOLLOW-ON TASK" request
 is executed.
 
Note: Either the newTaskModel parameter or the template parameter must be set.
Parameters:newTaskModel - The task model from which a follow-on task is to be created.template - The task template from which a follow-on task is to be created.previousTask - The predecessor task that is to be completed.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postCompleteWithNewFollowOnTask
void postCompleteWithNewFollowOnTask(Task newTask,
                                   TaskModel newTaskModel,
                                   TaskTemplate template,
                                   Task previousTask,
                                   java.io.Serializable inputMessage,
                                   TaskException taskException)
This method is called after a "COMPLETE WITH NEW FOLLOW-ON TASK" request
 was executed.
 
Note: Either the newTaskModel parameter or the template parameter must be set.
Parameters:newTask - The task that was requested to be created.newTaskModel - The task model data from which the task was requested to be created.template - The task template from which the task was requested to be created.previousTask - The the predecessor task that was requested to be completed.inputMessage - An optional input message - may be null.taskException - The TaskException that occurred or null if no exception occurred.
    - preCreateAndCallTask
void preCreateAndCallTask(TaskModel newTaskModel,
                        TaskTemplate template,
                        java.io.Serializable inputMessage)
                          throws ApplicationVetoException
This method is called before a "CREATE AND CALL TASK" request is executed.
 
Note: Either the newTaskModel parameter or the template parameter must be set.
Parameters:newTaskModel - The task model data which the task is to be created.template - The task template from which the new task is to be created.inputMessage - An optional input message - may be null.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postCreateAndCallTask
void postCreateAndCallTask(Task task,
                         TaskModel newTaskModel,
                         TaskTemplate template,
                         java.io.Serializable inputMessage,
                         TaskException taskException)
This method is called after a "CREATE AND CALL TASK" request was executed.
 
Note: Either the newTaskModel parameter or the template parameter must be set.
Parameters:task - The task that was requested to be created and called.newTaskModel - The task model data from which the task was requested to be created.template - The task template from which the task was requested to be created.inputMessage - An optional input message - may be null.taskException - The TaskException that occurred or null if no exception occurred.
    - preCreateAndStartTask
void preCreateAndStartTask(TaskModel newTaskModel,
                         TaskTemplate template,
                         java.io.Serializable inputMessage,
                         ReplyHandler replyHandler)
                           throws ApplicationVetoException
This method is called before a "CREATE AND START TASK" request is executed.
 
Note: Either the newTaskModel parameter or the template parameter must be set.
Parameters:newTaskModel - The task model data which the task is to be created.template - The task template from which the task is to be created.inputMessage - An optional input message - may be null.replyHandler - An optional reply handler - may be null.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postCreateAndStartTask
void postCreateAndStartTask(Task newTask,
                          TaskModel newTaskModel,
                          TaskTemplate template,
                          java.io.Serializable inputMessage,
                          ReplyHandler replyHandler,
                          TaskException taskException)
This method is called after a "CREATE AND START TASK" request was executed.
 
Note: Either the newTaskModel parameter or the template parameter must be set.
Parameters:newTask - The task that was requested to be created and called.newTaskModel - The task model data from which the task was requested to be created.template - The task template from which the task was requested to be created.inputMessage - An optional input message - may be null.replyHandler - An optional reply handler - may be null.taskException - The TaskException that occurred or null if no exception occurred.
    - preCreateAndStartTaskAsSubTask
void preCreateAndStartTaskAsSubTask(TaskModel newTaskModel,
                                  TaskTemplate template,
                                  Task parentTask,
                                  java.io.Serializable inputMessage)
                                    throws ApplicationVetoException
This method is called before a "CREATE AND START TASK AS SUBTASK" request
 is executed.
 
Note: Either the newTaskModel parameter or the template parameter must be set.
Parameters:newTaskModel - The task model data which the subtask is to be created.template - The task template from which the subtask is to be created.parentTask - The parent task.inputMessage - An optional input message - may be null.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postCreateAndStartTaskAsSubTask
void postCreateAndStartTaskAsSubTask(Task newTask,
                                   TaskModel newTaskModel,
                                   TaskTemplate template,
                                   Task parentTask,
                                   java.io.Serializable inputMessage,
                                   TaskException taskException)
This method is called after a "CREATE AND START TASK AS SUBTASK" request was executed.
 
Note: Either the newTaskModel parameter or the template parameter must be set.
Parameters:newTask - The task that was requested to be created and started.newTaskModel - The task model data from which the task was requested to be created.template - The task template from which the task was requested to be created.parentTask - The parent task.inputMessage - An optional input message - may be null.taskException - The TaskException that occurred or null if no exception occurred.
    - preCreateTask
void preCreateTask(TaskModel newTaskModel,
                 TaskTemplate template,
                 java.io.Serializable inputMessage,
                 ReplyHandler replyHandler)
                   throws ApplicationVetoException
This method is called before a "CREATE TASK" request is executed.
Parameters:newTaskModel - The task model data which the task is to be created.template - The task template from which the task is to be created.inputMessage - An optional input message - may be null.replyHandler - An optional reply handler - may be null.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postCreateTask
void postCreateTask(Task newTask,
                  TaskModel newTaskModel,
                  TaskTemplate template,
                  java.io.Serializable inputMessage,
                  ReplyHandler replyHandler,
                  TaskException taskException)
This method is called after a "CREATE TASK" request was executed.
Parameters:newTask - The task that was requested to be created.newTaskModel - The task model data from which the task was requested to be created.template - The task template from which the task was requested to be created.inputMessage - An optional input message - may be null.replyHandler - An optional reply handler - may be null.taskException - The TaskException that occurred or null if no exception occurred.
    - preCreateWorkItem
void preCreateWorkItem(Task task,
                     int assignmentReason,
                     java.lang.String id)
                       throws ApplicationVetoException
This method is called before a "CREATE WORKITEM" request is executed.
Parameters:task - The task for which a work item is to be created.assignmentReason - The reason why the work item is assigned.id - The user or group that is to be associated.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postCreateWorkItem
void postCreateWorkItem(Task task,
                      int assignmentReason,
                      java.lang.String id,
                      TaskException taskException)
This method is called after a "CREATE WORKITEM" request was executed.
Parameters:task - The task for which a work item was requested to be created.assignmentReason - The reason why the work item is assigned.id - The user or group that is to be associated.taskException - The TaskException that occurred or null if no exception occurred.
    - preDeleteTask
void preDeleteTask(Task task)
                   throws ApplicationVetoException
This method is called before a "DELETE TASK" request is executed.
Parameters:task - The task that is to be deleted.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postDeleteTask
void postDeleteTask(Task task,
                  TaskException taskException)
This method is called after a 2DELETE TASK" request was executed.
Parameters:task - The task that was requested to be deleted.taskException - The TaskException that occurred or null if no exception occurred.
    - preDeleteWorkItem
void preDeleteWorkItem(Task task,
                     int assignmentReason,
                     java.lang.String id)
                       throws ApplicationVetoException
This method is called before a "DELETE WORKITEM" request is executed.
Parameters:task - The task for which a work item is to be deleted.assignmentReason - The reason why the work item is assigned.id - The user or group that is to be associated.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postDeleteWorkItem
void postDeleteWorkItem(Task task,
                      int assignmentReason,
                      java.lang.String id,
                      TaskException taskException)
This method is called after a "DELETE WORKITEM" request was executed.
Parameters:task - The task for which a work item was requested to be deleted.assignmentReason - The reason why the work item is assigned.id - The user or group that is to be associated.taskException - The TaskException that occurred or null if no exception occurred.
    - preReplaceWorkItem
void preReplaceWorkItem(Task task,
                      int assignmentReason,
                      java.lang.String staffQuery)
                        throws ApplicationVetoException
Deprecated. since v7.0 - this method is not used.
This method is called before a "REPLACE WORKITEM" request is executed.
Parameters:task - The task whose work item is to be replaced.assignmentReason - The reason why the work item is assigned.staffQuery - The staff query to replace the associated staff.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postReplaceWorkItem
void postReplaceWorkItem(Task task,
                       int assignmentReason,
                       java.lang.String staffQuery,
                       TaskException taskException)
Deprecated. since v7.0 - this method is not used.
This method is called after a "REPLACE WORKITEM" request was executed.
Parameters:task - The task whose work item was requested to be replaced.assignmentReason - The reason why the work item is assigned.staffQuery - The staff query to replace the associated staff. sontaskException - The TaskException that occurred or null if no exception occurred.
    - preRestartTask
void preRestartTask(Task task)
                    throws ApplicationVetoException
This method is called before a "RESTART TASK" request is executed.
Parameters:task - The task that is to be restarted.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postRestartTask
void postRestartTask(Task task,
                   TaskException taskException)
This method is called after a "RESTART TASK" request was executed.
Parameters:task - The task that was requested to be restarted.taskException - The TaskException that occurred or null if no exception occurred.
    - preResumeTask
void preResumeTask(Task task)
                   throws ApplicationVetoException
This method is called before a "RESUME TASK" request is executed.
Parameters:task - The task that is to be resumed.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postResumeTask
void postResumeTask(Task task,
                  TaskException taskException)
This method is called after a "RESUME TASK" request was executed.
Parameters:task - The task that was requested to be resumed.taskException - The TaskException that occurred or null if no exception occurred.
    - preSetBinaryCustomProperty
void preSetBinaryCustomProperty(Task task,
                              java.lang.String propertyName,
                              java.lang.String dataType,
                              java.io.Serializable propertyValue)
                                throws ApplicationVetoException
Deprecated. since v6.0.2 - use preSetBinaryCustomProperty(Task, BinaryCustomProperty)
This method is called before a "SET BINARY CUSTOM PROPERTY" request is
 executed.
Parameters:task - The task for that the custom property is to be set.propertyName - The property name.dataType - The property data type.propertyValue - The property value.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postSetBinaryCustomProperty
void postSetBinaryCustomProperty(Task task,
                               java.lang.String propertyName,
                               java.lang.String dataType,
                               java.io.Serializable propertyValue,
                               TaskException taskException)
Deprecated. since v6.0.2 - use postSetBinaryCustomProperty(Task, BinaryCustomProperty)
This method is called after a "SET BINARY CUSTOM PROPERTY" request was
 executed.
Parameters:task - The task for which the custom property was requested to be set.propertyName - The property name.dataType - The property data type.propertyValue - The property value.taskException - The TaskException that occurred or null if no exception occurred.
    - preSetCustomProperty
void preSetCustomProperty(Task task,
                        java.lang.String propertyName,
                        java.lang.String propertyValue)
                          throws ApplicationVetoException
This method is called before a "SET CUSTOM PROPERTY" request is executed.
Parameters:task - The task for which the custom property is to be set.propertyName - The property name.propertyValue - The property value.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postSetCustomProperty
void postSetCustomProperty(Task task,
                         java.lang.String propertyName,
                         java.lang.String propertyValue,
                         TaskException taskException)
This method is called after a "SET CUSTOM PROPERTY" request was executed.
Parameters:task - The task for which the custom property was requested to be set.propertyName - The property name.propertyValue - The property value.taskException - The TaskException that occurred or null if no exception occurred.
    - preSetFaultMessage
void preSetFaultMessage(Task task,
                      java.lang.String faultName,
                      java.io.Serializable faultMessage)
                        throws ApplicationVetoException
This method is called before a "SET FAULT MESSAGE" request is executed.
Parameters:task - The task for which the fault message is to be set.faultName - The fault name.faultMessage - The fault message.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postSetFaultMessage
void postSetFaultMessage(Task task,
                       java.lang.String faultName,
                       java.io.Serializable faultMessage,
                       TaskException taskException)
This method is called after a "SET FAULT MESSAGE" request was executed.
Parameters:task - The task for which the fault message was requested to be set.faultName - The fault name.faultMessage - The fault message.taskException - The TaskException that occurred or null if no exception occurred.
    - preSetOutputMessage
void preSetOutputMessage(Task task,
                       java.io.Serializable outputMessage)
                         throws ApplicationVetoException
This method is called before a "SET OUTPUT MESSAGE" request is executed.
Parameters:task - The task for which the output message is to be set.outputMessage - The output message.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postSetOutputMessage
void postSetOutputMessage(Task task,
                        java.io.Serializable outputMessage,
                        TaskException taskException)
This method is called after a "SET OUTPUT MESSAGE" request was executed.
Parameters:task - The task for which the output message was requested to be set.outputMessage - The output message.taskException - The TaskException that occurred or null if no exception occurred.
    - preStartTask
void preStartTask(Task task,
                java.io.Serializable inputMessage,
                ReplyHandler replyHandler)
                  throws ApplicationVetoException
This method is called before a "START TASK" request is executed.
Parameters:task - The task to be started.inputMessage - The optional input message - may be null.replyHandler - An optional reply handler - may be null.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postStartTask
void postStartTask(Task task,
                 java.io.Serializable inputMessage,
                 ReplyHandler replyHandler,
                 TaskException taskException)
This method is called after a "START TASK" request was executed.
Parameters:task - The task that was requested to be started.inputMessage - the optional input message - may be null.replyHandler - An optiona reply handler - may be null.taskException - The TaskException that occurred or null if no exception occurred.
    - preStartTaskAsSubTask
void preStartTaskAsSubTask(Task task,
                         Task parentTask,
                         java.io.Serializable inputMessage)
                           throws ApplicationVetoException
This method is called before a "START TASK AS SUBTASK" request is executed.
Parameters:task - The task to be started.parentTask - The parent task.inputMessage - The optional input message - may be null.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postStartTaskAsSubTask
void postStartTaskAsSubTask(Task task,
                          Task parentTask,
                          java.io.Serializable inputMessage,
                          TaskException taskException)
This method is called after a "START TASK AS SUBTASK" request was executed.
Parameters:task - The task that was requested to be started.parentTask - The parent task.inputMessage - The optional input message - may be null.taskException - The TaskException that occurred or null if no exception occurred.
    - preSuspendTask
void preSuspendTask(Task task)
                    throws ApplicationVetoException
This method is called before a "SUSPEND TASK" request is executed.
Parameters:task - The task to be suspended.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postSuspendTask
void postSuspendTask(Task task,
                   TaskException taskException)
This method is called after a "SUSPEND TASK" request was executed.
Parameters:task - The task that was requested to be suspended.taskException - The TaskException that occurred or null if no exception occurred.
    - preTerminateTask
void preTerminateTask(Task task)
                      throws ApplicationVetoException
This method is called before a "TERMINATE TASK" request is executed.
Parameters:task - The task to be terminated.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postTerminateTask
void postTerminateTask(Task task,
                     TaskException taskException)
This method is called after a "TERMINATE TASK" request was executed.
Parameters:task - The task that was requested to be terminated.taskException - The TaskException that occurred or null if no exception occurred.
    - preTransferWorkItem
void preTransferWorkItem(Task task,
                       int assignmentReason,
                       java.lang.String fromUserId,
                       java.lang.String toUserId)
                         throws ApplicationVetoException
This method is called before a "TRANSFER WORKITEM" request is executed.
Parameters:task - The task whose work item is to be transferred.assignmentReason - The reason why the work item is assigned.fromUserId - The user who is the owner of the work item.toUserId - The user that is to be associated.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postTransferWorkItem
void postTransferWorkItem(Task task,
                        int assignmentReason,
                        java.lang.String fromUserId,
                        java.lang.String toUserId,
                        TaskException taskException)
This method is called after a "TRANSFER WORKITEM" request was executed.
Parameters:task - The task whose work item was requested to be transferred.assignmentReason - The reason why the work item is assigned.fromUserId - The user who is the owner of the work item.toUserId - The user that is to be associated.taskException - The TaskException that occurred or null if no exception occurred.
    - preUpdateTask
void preUpdateTask(Task task)
                   throws ApplicationVetoException
This method is called before a "UPDATE TASK" request is executed.
Parameters:task - The task to be updated.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postUpdateTask
void postUpdateTask(Task task,
                  TaskException taskException)
This method is called after a "UPDATE TASK" request was executed.
Parameters:task - The task that was requested to be updated.taskException - The TaskException that occurred or null if no exception occurred.
    - preUpdateInactiveTask
void preUpdateInactiveTask(Task task,
                         TaskModel model,
                         java.io.Serializable inputMessage,
                         ReplyHandler replyHandler)
                           throws ApplicationVetoException
This method is called before a "UPDATE INACTIVE TASK" request is executed.
Parameters:task - The task to be updated.model - The task model to be used for the update.inputMessage - The optional input message - may be null.replyHandler - An optional reply handler - may be null.
Throws:
ApplicationVetoException - if the subsequent execution is to be aborted
    - postUpdateInactiveTask
void postUpdateInactiveTask(Task task,
                          java.io.Serializable inputMessage,
                          ReplyHandler replyHandler,
                          TaskException taskException)
This method is called after a "UPDATE INACTIVE TASK" request was executed.
Parameters:task - The task that was requested to be updated.inputMessage - The optional input message - may be null.replyHandler - An optional reply handler - may be null.taskException - The TaskException that occurred or null if no exception occurred.