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

## Interface APIEventHandlerPlugin4

- All Superinterfaces:
APIEventHandlerPlugin, APIEventHandlerPlugin2, APIEventHandlerPlugin3

All Known Subinterfaces:
APIEventHandlerPlugin5, APIEventHandlerPlugin6

All Known Implementing Classes:
APIEventHandler

public interface APIEventHandlerPlugin4
extends APIEventHandlerPlugin3
This interface supports the creation of API event handlers.
 
 API events occur when a human task changes its state or when a task property is
 updated. These events can be used by other components and applications to
 participate in state transitions of human tasks. Use the APIEventHandlerPlugin4
 service provider interface (SPI) to create plug-ins to get informed about
 events sent by the API or the internal events that have equivalent API
 events.
 
 To handle API events, the event handler is invoked directly before a
 modification is done (pre-event method) and after the modification is done
 (post-event method).
 
 This interface provides for methods that are called as API pre- or
 post-events (extends APIEventHandlerPlugin3).
Since:
6.2.0
Version:
6.2.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description void postSetInputMessage (Task task, java.io.Serializable inputMessage, TaskException taskException) This method is called after a "SET INPUT MESSAGE" request was executed. void postUpdateEscalation (Escalation escalation, TaskException taskException) This method is called after an "UPDATE ESCALATION" request was executed. void preSetInputMessage (Task task, java.io.Serializable inputMessage) This method is called before a "SET INPUT MESSAGE" request is executed. void preUpdateEscalation (Escalation escalation) This method is called before an "UPDATE ESCALATION" request is executed.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                                                                       |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                | postSetInputMessage(Task task,                    java.io.Serializable inputMessage,                    TaskException taskException) This method is called after a "SET INPUT MESSAGE" request was executed. |
| void                | postUpdateEscalation(Escalation escalation,                     TaskException taskException) This method is called after an "UPDATE ESCALATION" request was executed.                                        |
| void                | preSetInputMessage(Task task,                   java.io.Serializable inputMessage) This method is called before a "SET INPUT MESSAGE" request is executed.                                                   |
| void                | preUpdateEscalation(Escalation escalation) This method is called before an "UPDATE ESCALATION" request is executed.                                                                                          |

- Methods inherited from interface com.ibm.task.spi.APIEventHandlerPlugin3
postSuspendTaskUntil, postSuspendTaskUntil, postSuspendTaskWithCancelClaim, postSuspendTaskWithCancelClaim, preSuspendTaskUntil, preSuspendTaskUntil, preSuspendTaskWithCancelClaim, preSuspendTaskWithCancelClaim

- Methods inherited from interface com.ibm.task.spi.APIEventHandlerPlugin2
postClaim, postCreateWorkItem, postDeleteWorkItem, postSetBinaryCustomProperty, postSetBinaryCustomProperty, postSuspendTaskUntil, postSuspendTaskWithCancelClaim, postTransferWorkItem, preCreateWorkItem, preDeleteWorkItem, preSetBinaryCustomProperty, preSetBinaryCustomProperty, preSuspendTaskUntil, preSuspendTaskWithCancelClaim, preTransferWorkItem

- Methods inherited from interface com.ibm.task.spi.APIEventHandlerPlugin
postCallTask, postCancelClaim, postClaim, postComplete, postCompleteWithFollowOnTask, postCompleteWithNewFollowOnTask, postCreateAndCallTask, postCreateAndStartTask, postCreateAndStartTaskAsSubTask, postCreateTask, postCreateWorkItem, postDeleteTask, postDeleteWorkItem, postReplaceWorkItem, postRestartTask, postResumeTask, postSetBinaryCustomProperty, postSetCustomProperty, postSetFaultMessage, postSetOutputMessage, postStartTask, postStartTaskAsSubTask, postSuspendTask, postTerminateTask, postTransferWorkItem, postUpdateInactiveTask, postUpdateTask, preCallTask, preCancelClaim, preClaim, preComplete, preCompleteWithFollowOnTask, preCompleteWithNewFollowOnTask, preCreateAndCallTask, preCreateAndStartTask, preCreateAndStartTaskAsSubTask, preCreateTask, preCreateWorkItem, preDeleteTask, preDeleteWorkItem, preReplaceWorkItem, preRestartTask, preResumeTask, preSetBinaryCustomProperty, preSetCustomProperty, preSetFaultMessage, preSetOutputMessage, preStartTask, preStartTaskAsSubTask, preSuspendTask, preTerminateTask, preTransferWorkItem, preUpdateInactiveTask, preUpdateTask