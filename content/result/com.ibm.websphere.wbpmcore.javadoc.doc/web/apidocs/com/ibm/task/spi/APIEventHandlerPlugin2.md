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

## Interface APIEventHandlerPlugin2

- All Superinterfaces:
APIEventHandlerPlugin

All Known Subinterfaces:
APIEventHandlerPlugin3, APIEventHandlerPlugin4, APIEventHandlerPlugin5, APIEventHandlerPlugin6

All Known Implementing Classes:
APIEventHandler

public interface APIEventHandlerPlugin2
extends APIEventHandlerPlugin
This interface supports the creation of API event handlers that deal with work items.
 
 API events occur when a human task changes its state or when a task property is
 updated. These events can be used by other components and applications to
 participate in state transitions of human tasks. Use the APIEventHandlerPlugin2
 service provider interface (SPI) to create plug-ins to get informed about
 events sent by the API or the internal events that have equivalent API
 events.
 
 To handle API events, the event handler is invoked directly before a
 modification is done (pre-event method) and after the modification is done
 (post-event method).
 
 This interface provides for methods that are called as API pre- or
 post-events (extends APIEventHandlerPlugin).
Since:
6.0.2
Version:
6.0.2

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description void postClaim (Task task, java.io.Serializable inputMessage, TaskException taskException) This method is called after a "CLAIM" request was executed. void postCreateWorkItem (Escalation escalation, int assignmentReason, java.lang.String id, TaskException taskException) This method is called after a "CREATE WORKITEM" request was executed. void postDeleteWorkItem (Escalation escalation, int assignmentReason, java.lang.String id, TaskException taskException) This method is called after a "DELETE WORKITEM" request was executed. void postSetBinaryCustomProperty (Escalation escalation, BinaryCustomProperty property, TaskException taskException) This method is called after a "SET BINARY CUSTOM PROPERTY" for an escalation request was executed. void postSetBinaryCustomProperty (Task task, BinaryCustomProperty property, TaskException taskException) This method is called after a "SET BINARY CUSTOM PROPERTY" for a task request was executed. void postSuspendTaskUntil (Task task, java.lang.String duration, TaskException taskException) This method is called after a "SUSPEND TASK UNTIL" request was executed. void postSuspendTaskWithCancelClaim (Task task, java.lang.String duration, TaskException taskException) This method is called after a "SUSPEND TASK WITH CANCEL CLAIM" request was executed. void postTransferWorkItem (Escalation escalation, int assignmentReason, java.lang.String fromUserId, java.lang.String toUserId, TaskException taskException) This method is called after a "TRANSFER WORKITEM" request was executed. void preCreateWorkItem (Escalation escalation, int assignmentReason, java.lang.String id) This method is called before a "CREATE WORKITEM" request is executed. void preDeleteWorkItem (Escalation escalation, int assignmentReason, java.lang.String id) This method is called before a "DELETE WORKITEM" request is executed. void preSetBinaryCustomProperty (Escalation escalation, BinaryCustomProperty property) This method is called before a "SET BINARY CUSTOM PROPERTY" for an escalation request is executed. void preSetBinaryCustomProperty (Task task, BinaryCustomProperty property) This method is called before a "SET BINARY CUSTOM PROPERTY" for a task request is executed. void preSuspendTaskUntil (Task task, java.lang.String duration) This method is called before a "SUSPEND TASK UNTIL" request is executed. void preSuspendTaskWithCancelClaim (Task task, java.lang.String duration) This method is called before a "SUSPEND TASK WITH CANCEL CLAIM" request is executed. void preTransferWorkItem (Escalation escalation, int assignmentReason, java.lang.String fromUserId, java.lang.String toUserId) This method is called before a "TRANSFER WORKITEM" request is executed.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                                                                                                                                                                         |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                | postClaim(Task task,          java.io.Serializable inputMessage,          TaskException taskException) This method is called after a "CLAIM" request was executed.                                                                                                                                             |
| void                | postCreateWorkItem(Escalation escalation,                   int assignmentReason,                   java.lang.String id,                   TaskException taskException) This method is called after a "CREATE WORKITEM" request was executed.                                                                  |
| void                | postDeleteWorkItem(Escalation escalation,                   int assignmentReason,                   java.lang.String id,                   TaskException taskException) This method is called after a "DELETE WORKITEM" request was executed.                                                                  |
| void                | postSetBinaryCustomProperty(Escalation escalation,                            BinaryCustomProperty property,                            TaskException taskException) This method is called after a "SET BINARY CUSTOM PROPERTY" for an escalation request was  executed.                                       |
| void                | postSetBinaryCustomProperty(Task task,                            BinaryCustomProperty property,                            TaskException taskException) This method is called after a "SET BINARY CUSTOM PROPERTY" for a task request was  executed.                                                          |
| void                | postSuspendTaskUntil(Task task,                     java.lang.String duration,                     TaskException taskException) This method is called after a "SUSPEND TASK UNTIL" request was executed.                                                                                                       |
| void                | postSuspendTaskWithCancelClaim(Task task,                               java.lang.String duration,                               TaskException taskException) This method is called after a "SUSPEND TASK WITH CANCEL CLAIM" request was executed.                                                             |
| void                | postTransferWorkItem(Escalation escalation,                     int assignmentReason,                     java.lang.String fromUserId,                     java.lang.String toUserId,                     TaskException taskException) This method is called after a "TRANSFER WORKITEM" request was executed. |
| void                | preCreateWorkItem(Escalation escalation,                  int assignmentReason,                  java.lang.String id) This method is called before a "CREATE WORKITEM" request is executed.                                                                                                                    |
| void                | preDeleteWorkItem(Escalation escalation,                  int assignmentReason,                  java.lang.String id) This method is called before a "DELETE WORKITEM" request is executed.                                                                                                                    |
| void                | preSetBinaryCustomProperty(Escalation escalation,                           BinaryCustomProperty property) This method is called before a "SET BINARY CUSTOM PROPERTY" for an escalation request is  executed.                                                                                                 |
| void                | preSetBinaryCustomProperty(Task task,                           BinaryCustomProperty property) This method is called before a "SET BINARY CUSTOM PROPERTY" for a task request is  executed.                                                                                                                    |
| void                | preSuspendTaskUntil(Task task,                    java.lang.String duration) This method is called before a "SUSPEND TASK UNTIL" request is executed.                                                                                                                                                          |
| void                | preSuspendTaskWithCancelClaim(Task task,                              java.lang.String duration) This method is called before a "SUSPEND TASK WITH CANCEL CLAIM" request is  executed.                                                                                                                         |
| void                | preTransferWorkItem(Escalation escalation,                    int assignmentReason,                    java.lang.String fromUserId,                    java.lang.String toUserId) This method is called before a "TRANSFER WORKITEM" request is executed.                                                      |

- Methods inherited from interface com.ibm.task.spi.APIEventHandlerPlugin
postCallTask, postCancelClaim, postClaim, postComplete, postCompleteWithFollowOnTask, postCompleteWithNewFollowOnTask, postCreateAndCallTask, postCreateAndStartTask, postCreateAndStartTaskAsSubTask, postCreateTask, postCreateWorkItem, postDeleteTask, postDeleteWorkItem, postReplaceWorkItem, postRestartTask, postResumeTask, postSetBinaryCustomProperty, postSetCustomProperty, postSetFaultMessage, postSetOutputMessage, postStartTask, postStartTaskAsSubTask, postSuspendTask, postTerminateTask, postTransferWorkItem, postUpdateInactiveTask, postUpdateTask, preCallTask, preCancelClaim, preClaim, preComplete, preCompleteWithFollowOnTask, preCompleteWithNewFollowOnTask, preCreateAndCallTask, preCreateAndStartTask, preCreateAndStartTaskAsSubTask, preCreateTask, preCreateWorkItem, preDeleteTask, preDeleteWorkItem, preReplaceWorkItem, preRestartTask, preResumeTask, preSetBinaryCustomProperty, preSetCustomProperty, preSetFaultMessage, preSetOutputMessage, preStartTask, preStartTaskAsSubTask, preSuspendTask, preTerminateTask, preTransferWorkItem, preUpdateInactiveTask, preUpdateTask