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

## Interface APIEventHandlerPlugin3

- All Superinterfaces:
APIEventHandlerPlugin, APIEventHandlerPlugin2

All Known Subinterfaces:
APIEventHandlerPlugin4, APIEventHandlerPlugin5, APIEventHandlerPlugin6

All Known Implementing Classes:
APIEventHandler

public interface APIEventHandlerPlugin3
extends APIEventHandlerPlugin2
This interface supports the creation of API event handlers.
 
 API events occur when a human task changes its state or when a task property is
 updated. These events can be used by other components and applications to
 participate in state transitions of human tasks. Use the APIEventHandlerPlugin3
 service provider interface (SPI) to create plug-ins to get informed about
 events sent by the API or the internal events that have equivalent API
 events.
 
 To handle API events, the event handler is invoked directly before a
 modification is done (pre-event method) and after the modification is done
 (post-event method).
 
 This interface provides for methods that are called as API pre- or
 post-events (extends APIEventHandlerPlugin2).
Since:
6.0.2
Version:
6.1.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description void postSuspendTaskUntil (Task task, java.util.Calendar timeStamp, TaskException taskException) This method is called after a "SUSPEND TASK UNTIL" request was executed. void postSuspendTaskUntil (Task task, int duration, TaskException taskException) This method is called after a "SUSPEND TASK UNTIL" request was executed. void postSuspendTaskWithCancelClaim (Task task, java.util.Calendar timeStamp, TaskException taskException) This method is called after a "SUSPEND TASK WITH CANCEL CLAIM" request was executed. void postSuspendTaskWithCancelClaim (Task task, int duration, TaskException taskException) This method is called after a "SUSPEND TASK WITH CANCEL CLAIM" request was executed. void preSuspendTaskUntil (Task task, java.util.Calendar timeStamp) This method is called before a "SUSPEND TASK UNTIL" request is executed. void preSuspendTaskUntil (Task task, int duration) This method is called before a "SUSPEND TASK UNTIL" request is executed. void preSuspendTaskWithCancelClaim (Task task, java.util.Calendar timeStamp) This method is called before a "SUSPEND TASK WITH CANCEL CLAIM" request is executed. void preSuspendTaskWithCancelClaim (Task task, int duration) This method is called before a "SUSPEND TASK WITH CANCEL CLAIM" request is executed.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                                                                                                                |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                | postSuspendTaskUntil(Task task,                     java.util.Calendar timeStamp,                     TaskException taskException) This method is called after a "SUSPEND TASK UNTIL" request was executed.                                           |
| void                | postSuspendTaskUntil(Task task,                     int duration,                     TaskException taskException) This method is called after a "SUSPEND TASK UNTIL" request was executed.                                                           |
| void                | postSuspendTaskWithCancelClaim(Task task,                               java.util.Calendar timeStamp,                               TaskException taskException) This method is called after a "SUSPEND TASK WITH CANCEL CLAIM" request was executed. |
| void                | postSuspendTaskWithCancelClaim(Task task,                               int duration,                               TaskException taskException) This method is called after a "SUSPEND TASK WITH CANCEL CLAIM" request was executed.                 |
| void                | preSuspendTaskUntil(Task task,                    java.util.Calendar timeStamp) This method is called before a "SUSPEND TASK UNTIL" request is executed.                                                                                              |
| void                | preSuspendTaskUntil(Task task,                    int duration) This method is called before a "SUSPEND TASK UNTIL" request is executed.                                                                                                              |
| void                | preSuspendTaskWithCancelClaim(Task task,                              java.util.Calendar timeStamp) This method is called before a "SUSPEND TASK WITH CANCEL CLAIM" request is  executed.                                                             |
| void                | preSuspendTaskWithCancelClaim(Task task,                              int duration) This method is called before a "SUSPEND TASK WITH CANCEL CLAIM" request is  executed.                                                                             |

- Methods inherited from interface com.ibm.task.spi.APIEventHandlerPlugin2
postClaim, postCreateWorkItem, postDeleteWorkItem, postSetBinaryCustomProperty, postSetBinaryCustomProperty, postSuspendTaskUntil, postSuspendTaskWithCancelClaim, postTransferWorkItem, preCreateWorkItem, preDeleteWorkItem, preSetBinaryCustomProperty, preSetBinaryCustomProperty, preSuspendTaskUntil, preSuspendTaskWithCancelClaim, preTransferWorkItem

- Methods inherited from interface com.ibm.task.spi.APIEventHandlerPlugin
postCallTask, postCancelClaim, postClaim, postComplete, postCompleteWithFollowOnTask, postCompleteWithNewFollowOnTask, postCreateAndCallTask, postCreateAndStartTask, postCreateAndStartTaskAsSubTask, postCreateTask, postCreateWorkItem, postDeleteTask, postDeleteWorkItem, postReplaceWorkItem, postRestartTask, postResumeTask, postSetBinaryCustomProperty, postSetCustomProperty, postSetFaultMessage, postSetOutputMessage, postStartTask, postStartTaskAsSubTask, postSuspendTask, postTerminateTask, postTransferWorkItem, postUpdateInactiveTask, postUpdateTask, preCallTask, preCancelClaim, preClaim, preComplete, preCompleteWithFollowOnTask, preCompleteWithNewFollowOnTask, preCreateAndCallTask, preCreateAndStartTask, preCreateAndStartTaskAsSubTask, preCreateTask, preCreateWorkItem, preDeleteTask, preDeleteWorkItem, preReplaceWorkItem, preRestartTask, preResumeTask, preSetBinaryCustomProperty, preSetCustomProperty, preSetFaultMessage, preSetOutputMessage, preStartTask, preStartTaskAsSubTask, preSuspendTask, preTerminateTask, preTransferWorkItem, preUpdateInactiveTask, preUpdateTask