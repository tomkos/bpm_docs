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

## Interface APIEventHandlerPlugin5

- All Superinterfaces:
APIEventHandlerPlugin, APIEventHandlerPlugin2, APIEventHandlerPlugin3, APIEventHandlerPlugin4

All Known Subinterfaces:
APIEventHandlerPlugin6

All Known Implementing Classes:
APIEventHandler

public interface APIEventHandlerPlugin5
extends APIEventHandlerPlugin4
This interface supports the creation of API event handlers.
 
 API events occur when a human task changes its state or when a task property is
 updated. These events can be used by other components and applications to
 participate in state transitions of human tasks. Use the APIEventHandlerPlugin5
 service provider interface (SPI) to create plug-ins to get informed about
 events sent by the API or the internal events that have equivalent API
 events.
 
 To handle API events, the event handler is invoked directly before a
 modification is done (pre-event method) and after the modification is done
 (post-event method).
 
 This interface provides for methods that are called as API pre- or
 post-events (extends APIEventHandlerPlugin4).
Since:
7.0.0
Version:
7.0.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description void postGetTaskAndMarkRead (Task task, TaskException taskException) This method is called after a "GET TASK AND MARK READ" request was executed. void postSetCustomProperties (Task task, java.util.List customProperties, TaskException taskException) This method is called after a "SET CUSTOM PROPERTIES" request was executed. void postSetTaskRead (Task task, boolean taskRead, TaskException taskException) This method is called after a "SET TASK READ" request was executed. void postTransferToWorkBasket (Task task, java.lang.String workBasketName, boolean preserveTransferState, TaskException taskException) This method is called after a "TRANSFER TO WORK BASKET" request was executed. void postTriggerEscalation (Escalation escalation, TaskException taskException) This method is called after a "TRIGGER ESCALATION" request was executed. void preGetTaskAndMarkRead (Task task) This method is called before a "GET TASK AND MARK READ" request is executed. void preSetCustomProperties (Task task, java.util.List customProperties) This method is called before a "SET CUSTOM PROPERTIES" request is executed. void preSetTaskRead (Task task, boolean taskRead) This method is called before a "SET TASK READ" request is executed. void preTransferToWorkBasket (Task task, java.lang.String workBasketName, boolean preserveTransferState) This method is called before a "TRANSFER TO WORK BASKET" request is executed. void preTriggerEscalation (Escalation escalation) This method is called before a "TRIGGER ESCALATION" request is executed.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                                                                                                                                                 |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                | postGetTaskAndMarkRead(Task task,                       TaskException taskException) This method is called after a "GET TASK AND MARK READ" request was executed.                                                                                                                      |
| void                | postSetCustomProperties(Task task,                        java.util.List customProperties,                        TaskException taskException) This method is called after a "SET CUSTOM PROPERTIES" request was executed.                                                             |
| void                | postSetTaskRead(Task task,                boolean taskRead,                TaskException taskException) This method is called after a "SET TASK READ" request was executed.                                                                                                            |
| void                | postTransferToWorkBasket(Task task,                         java.lang.String workBasketName,                         boolean preserveTransferState,                         TaskException taskException) This method is called after a "TRANSFER TO WORK BASKET" request was executed. |
| void                | postTriggerEscalation(Escalation escalation,                      TaskException taskException) This method is called after a "TRIGGER ESCALATION" request was executed.                                                                                                                |
| void                | preGetTaskAndMarkRead(Task task) This method is called before a "GET TASK AND MARK READ" request is executed.                                                                                                                                                                          |
| void                | preSetCustomProperties(Task task,                       java.util.List customProperties) This method is called before a "SET CUSTOM PROPERTIES" request is executed.                                                                                                                   |
| void                | preSetTaskRead(Task task,               boolean taskRead) This method is called before a "SET TASK READ" request is executed.                                                                                                                                                          |
| void                | preTransferToWorkBasket(Task task,                        java.lang.String workBasketName,                        boolean preserveTransferState) This method is called before a "TRANSFER TO WORK BASKET" request is executed.                                                         |
| void                | preTriggerEscalation(Escalation escalation) This method is called before a "TRIGGER ESCALATION" request is executed.                                                                                                                                                                   |

- Methods inherited from interface com.ibm.task.spi.APIEventHandlerPlugin4
postSetInputMessage, postUpdateEscalation, preSetInputMessage, preUpdateEscalation

- Methods inherited from interface com.ibm.task.spi.APIEventHandlerPlugin3
postSuspendTaskUntil, postSuspendTaskUntil, postSuspendTaskWithCancelClaim, postSuspendTaskWithCancelClaim, preSuspendTaskUntil, preSuspendTaskUntil, preSuspendTaskWithCancelClaim, preSuspendTaskWithCancelClaim

- Methods inherited from interface com.ibm.task.spi.APIEventHandlerPlugin2
postClaim, postCreateWorkItem, postDeleteWorkItem, postSetBinaryCustomProperty, postSetBinaryCustomProperty, postSuspendTaskUntil, postSuspendTaskWithCancelClaim, postTransferWorkItem, preCreateWorkItem, preDeleteWorkItem, preSetBinaryCustomProperty, preSetBinaryCustomProperty, preSuspendTaskUntil, preSuspendTaskWithCancelClaim, preTransferWorkItem

- Methods inherited from interface com.ibm.task.spi.APIEventHandlerPlugin
postCallTask, postCancelClaim, postClaim, postComplete, postCompleteWithFollowOnTask, postCompleteWithNewFollowOnTask, postCreateAndCallTask, postCreateAndStartTask, postCreateAndStartTaskAsSubTask, postCreateTask, postCreateWorkItem, postDeleteTask, postDeleteWorkItem, postReplaceWorkItem, postRestartTask, postResumeTask, postSetBinaryCustomProperty, postSetCustomProperty, postSetFaultMessage, postSetOutputMessage, postStartTask, postStartTaskAsSubTask, postSuspendTask, postTerminateTask, postTransferWorkItem, postUpdateInactiveTask, postUpdateTask, preCallTask, preCancelClaim, preClaim, preComplete, preCompleteWithFollowOnTask, preCompleteWithNewFollowOnTask, preCreateAndCallTask, preCreateAndStartTask, preCreateAndStartTaskAsSubTask, preCreateTask, preCreateWorkItem, preDeleteTask, preDeleteWorkItem, preReplaceWorkItem, preRestartTask, preResumeTask, preSetBinaryCustomProperty, preSetCustomProperty, preSetFaultMessage, preSetOutputMessage, preStartTask, preStartTaskAsSubTask, preSuspendTask, preTerminateTask, preTransferWorkItem, preUpdateInactiveTask, preUpdateTask