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

## Interface APIEventHandlerPlugin6

- All Superinterfaces:
APIEventHandlerPlugin, APIEventHandlerPlugin2, APIEventHandlerPlugin3, APIEventHandlerPlugin4, APIEventHandlerPlugin5

All Known Implementing Classes:
APIEventHandler

public interface APIEventHandlerPlugin6
extends APIEventHandlerPlugin5
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
 post-events (extends APIEventHandlerPlugin5).
Since:
7.5.1
Version:
7.5.1

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description void postSetInlineCustomProperties (Task task, java.util.List inlineCustomProperties, TaskException taskException) This method is called after a "SET INLINE CUSTOM PROPERTIES" request was executed. void postSetInlineCustomProperty (Task task, InlineCustomProperty inlineCustomProperty, TaskException taskException) This method is called after a "SET INLINE CUSTOM PROPERTY" request was executed. void preSetInlineCustomProperties (Task task, java.util.List inlineCustomProperties) This method is called before a "SET INLINE CUSTOM PROPERTIES" request is executed. void preSetInlineCustomProperty (Task task, InlineCustomProperty inlineCustomProperty) This method is called before a "SET INLINE CUSTOM PROPERTY" request is executed.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                                                                                                                    |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                | postSetInlineCustomProperties(Task task,                              java.util.List inlineCustomProperties,                              TaskException taskException) This method is called after a "SET INLINE CUSTOM PROPERTIES" request was executed. |
| void                | postSetInlineCustomProperty(Task task,                            InlineCustomProperty inlineCustomProperty,                            TaskException taskException) This method is called after a "SET INLINE CUSTOM PROPERTY" request was executed.     |
| void                | preSetInlineCustomProperties(Task task,                             java.util.List inlineCustomProperties) This method is called before a "SET INLINE CUSTOM PROPERTIES" request is executed.                                                             |
| void                | preSetInlineCustomProperty(Task task,                           InlineCustomProperty inlineCustomProperty) This method is called before a "SET INLINE CUSTOM PROPERTY" request is executed.                                                               |

- Methods inherited from interface com.ibm.task.spi.APIEventHandlerPlugin5
postGetTaskAndMarkRead, postSetCustomProperties, postSetTaskRead, postTransferToWorkBasket, postTriggerEscalation, preGetTaskAndMarkRead, preSetCustomProperties, preSetTaskRead, preTransferToWorkBasket, preTriggerEscalation

- Methods inherited from interface com.ibm.task.spi.APIEventHandlerPlugin4
postSetInputMessage, postUpdateEscalation, preSetInputMessage, preUpdateEscalation

- Methods inherited from interface com.ibm.task.spi.APIEventHandlerPlugin3
postSuspendTaskUntil, postSuspendTaskUntil, postSuspendTaskWithCancelClaim, postSuspendTaskWithCancelClaim, preSuspendTaskUntil, preSuspendTaskUntil, preSuspendTaskWithCancelClaim, preSuspendTaskWithCancelClaim

- Methods inherited from interface com.ibm.task.spi.APIEventHandlerPlugin2
postClaim, postCreateWorkItem, postDeleteWorkItem, postSetBinaryCustomProperty, postSetBinaryCustomProperty, postSuspendTaskUntil, postSuspendTaskWithCancelClaim, postTransferWorkItem, preCreateWorkItem, preDeleteWorkItem, preSetBinaryCustomProperty, preSetBinaryCustomProperty, preSuspendTaskUntil, preSuspendTaskWithCancelClaim, preTransferWorkItem

- Methods inherited from interface com.ibm.task.spi.APIEventHandlerPlugin
postCallTask, postCancelClaim, postClaim, postComplete, postCompleteWithFollowOnTask, postCompleteWithNewFollowOnTask, postCreateAndCallTask, postCreateAndStartTask, postCreateAndStartTaskAsSubTask, postCreateTask, postCreateWorkItem, postDeleteTask, postDeleteWorkItem, postReplaceWorkItem, postRestartTask, postResumeTask, postSetBinaryCustomProperty, postSetCustomProperty, postSetFaultMessage, postSetOutputMessage, postStartTask, postStartTaskAsSubTask, postSuspendTask, postTerminateTask, postTransferWorkItem, postUpdateInactiveTask, postUpdateTask, preCallTask, preCancelClaim, preClaim, preComplete, preCompleteWithFollowOnTask, preCompleteWithNewFollowOnTask, preCreateAndCallTask, preCreateAndStartTask, preCreateAndStartTaskAsSubTask, preCreateTask, preCreateWorkItem, preDeleteTask, preDeleteWorkItem, preReplaceWorkItem, preRestartTask, preResumeTask, preSetBinaryCustomProperty, preSetCustomProperty, preSetFaultMessage, preSetOutputMessage, preStartTask, preStartTaskAsSubTask, preSuspendTask, preTerminateTask, preTransferWorkItem, preUpdateInactiveTask, preUpdateTask