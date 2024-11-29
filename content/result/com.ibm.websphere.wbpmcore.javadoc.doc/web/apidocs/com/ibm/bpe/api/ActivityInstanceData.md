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

## Interface ActivityInstanceData

- All Superinterfaces:
java.io.Serializable

All Known Implementing Classes:
ActivityInstanceBean

public interface ActivityInstanceData
extends java.io.Serializable
Accesses the properties of an activity instance.
 
 An activity instance is created in its initial state 'inactive'. When all
 control links leading to the activity instance are
 successfully evaluated and the join condition is fulfilled, the activity instance
 is activated. For a human task (staff), receive, or pick activity, the
 people assignment is resolved and work items are created so that the human task activity
 can be claimed and executed or a message can be send to the waiting activity. For
 all other activities, the associated implementation, for example, a Web service,
 is invoked.
 
 If the activity instance completes successfully, navigation continues.
 
 If the activity instance does not complete successfully,
 the fault is propagated to the enclosing scopes of the activity until it is either handled
 or the process scope is reached. When the fault is handled, navigation continues from
 that scope activity. When the fault reaches the process scope, the process
 is put into the 'Failed' state.
 
Since:
7.0 - introduced in 5.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
INVOKED\_INSTANCE\_TYPE\_CHILD\_PROCESS
States that the activity calls a long-running process
 that has "child" autonomy.

static int
INVOKED\_INSTANCE\_TYPE\_CHILD\_TASK
States that the activity calls a stand-alone task
 that has "child" autonomy.

static int
INVOKED\_INSTANCE\_TYPE\_INLINE\_TASK
States that the activity calls an inline human task.

static int
INVOKED\_INSTANCE\_TYPE\_NOT\_SET
States that the activity does not call a process or inline task,
 or does not call a process or stand-alone task that have "child" autonomy.

static int
KIND\_ABSTRACT\_TASK
Do not use - internal only.

static int
KIND\_ASSIGN
States that the activity specifies some assignment.

static int
KIND\_CALL\_ACTIVITY
Do not use - internal only.

static int
KIND\_COMPENSATE
States that the activity is a compensating activity.

static int
KIND\_COMPENSATE\_SCOPE
States that the activity is a compensate scope activity.

static int
KIND\_COMPENSATION\_END\_EVENT
Do not use - internal only.

static int
KIND\_COMPENSATION\_INTERRUPTING\_SUBPROCESS\_START\_EVENT
Do not use - internal only.

static int
KIND\_COMPENSATION\_THROW\_EVENT
Do not use - internal only.

static int
KIND\_CUSTOM
An activity that provides a plug-in mechanism for customer written implementations.

static int
KIND\_EMPTY
States that the activity is an empty activity without any
 implementation.

static int
KIND\_ERROR\_END\_EVENT
Do not use - internal only.

static int
KIND\_ERROR\_EVENT\_SUBPROCESS\_ACTIVITY
Do not use - internal only.

static int
KIND\_ERROR\_INTERRUPTING\_BOUNDARY\_EVENT
Do not use - internal only.

static int
KIND\_ERROR\_INTERRUPTING\_SUBPROCESS\_START\_EVENT
Do not use - internal only.

static int
KIND\_EVENT\_BASED\_GATEWAY
Do not use - internal only.

static int
KIND\_FLOW
An activity that specifies one or more activities to be performed concurrently.

static int
KIND\_FLOW\_END
Do not use - internal only.

static int
KIND\_FOR\_EACH\_PARALLEL
States that the activity is a forEach activity with parallel branches.

static int
KIND\_FOR\_EACH\_PARALLEL\_END
Do not use - internal only.

static int
KIND\_FOR\_EACH\_SERIAL
States that the activity is a forEach activity with no parallel branches.

static int
KIND\_FOR\_EACH\_SERIAL\_END
Do not use - internal only.

static int
KIND\_INVOKE
States that the activity describes some external service to be invoked.

static int
KIND\_INVOKE\_END
Do not use - internal only.

static int
KIND\_IOR\_GATEWAY
Do not use - internal only.

static int
KIND\_IOR\_IN\_GATEWAY
Do not use - internal only.

static int
KIND\_MESSAGE\_CATCH\_EVENT
Do not use - internal only.

static int
KIND\_MESSAGE\_END\_EVENT
Do not use - internal only.

static int
KIND\_MESSAGE\_EVENT\_SUBPROCESS\_ACTIVITY
Do not use - internal only.

static int
KIND\_MESSAGE\_NONINTERRUPTING\_SUBPROCESS\_START\_EVENT
Do not use - internal only.

static int
KIND\_MESSAGE\_START\_EVENT
Do not use - internal only.

static int
KIND\_MESSAGE\_THROW\_EVENT
Do not use - internal only.

static int
KIND\_NONE\_END\_EVENT
Do not use - internal only.

static int
KIND\_NONE\_START\_EVENT
Do not use - internal only.

static int
KIND\_PARALLEL\_GATEWAY
Do not use - internal only.

static int
KIND\_PICK
States that the activity is an activity that waits for various input.

static int
KIND\_PICK\_END
Do not use - internal only.

static int
KIND\_RECEIVE
States that the activity is an activity that waits for input.

static int
KIND\_RECEIVE\_TASK
Do not use - internal only.

static int
KIND\_REPEAT\_UNTIL
An activity that is repeated until an exit condition is met.

static int
KIND\_REPEAT\_UNTIL\_END
Do not use - internal only.

static int
KIND\_REPLY
An activity that allows the process to send a message in reply to a message that was received.

static int
KIND\_RETHROW
States that the activity rethrows a fault.

static int
KIND\_SCOPE
Describes a scope construct that allows for own variable definitions, fault and compensation handlers.

static int
KIND\_SCOPE\_END
Do not use - internal only.

static int
KIND\_SCRIPT
States that the activity is implemented by plain Java code.

static int
KIND\_SCRIPT\_TASK
Do not use - internal only.

static int
KIND\_SEND\_TASK
Do not use - internal only.

static int
KIND\_SEQUENCE
Describes a sequence construct that contains activities to be performed sequentially.

static int
KIND\_SEQUENCE\_END
Do not use - internal only.

static int
KIND\_SERVICE\_TASK
Do not use - internal only.

static int
KIND\_STAFF
States that the activity involves people for its execution.

static int
KIND\_SUBPROCESS\_ACTIVITY
Do not use - internal only.

static int
KIND\_SWITCH
Describes a switch construct that allows to select an activity from a set of choices.

static int
KIND\_SWITCH\_END
Do not use - internal only.

static int
KIND\_TERMINATE
States that the activity terminates execution.

static int
KIND\_TERMINATE\_END\_EVENT
Do not use - internal only.

static int
KIND\_THROW
States that the activity throws a fault.

static int
KIND\_TIMER\_CATCH\_EVENT
Do not use - internal only.

static int
KIND\_TIMER\_EVENT\_SUBPROCESS\_ACTIVITY
Do not use - internal only.

static int
KIND\_TIMER\_INTERRUPTING\_BOUNDARY\_EVENT
Do not use - internal only.

static int
KIND\_TIMER\_NONINTERRUPTING\_SUBPROCESS\_START\_EVENT
Do not use - internal only.

static int
KIND\_USER\_TASK
Do not use - internal only.

static int
KIND\_WAIT
An activity that allows to wait for a given period of time.

static int
KIND\_WHILE
An activity that is repeated until a certain criteria is met.

static int
KIND\_WHILE\_END
Do not use - internal only.

static int
KIND\_XOR\_GATEWAY
Do not use - internal only.

static int
STATE\_CLAIMED
States that the activity has been claimed.

static int
STATE\_EXPIRED
States that the activity ended because its allowed duration timed-out.

static int
STATE\_FAILED
States that the activity failed to execute.

static int
STATE\_FAILING
States that the activity is failing.

static int
STATE\_FINISHED
States that the activity finished execution successfully.

static int
STATE\_INACTIVE
States that the activity has not yet been scheduled for execution.

static int
STATE\_PROCESSING\_UNDO
States that the activity is retried due to a transaction rollback and that
 the activity waits for the microflow that it invokes to complete its compensation actions for the
 first invoke.

static int
STATE\_READY
States that the activity is ready to be started or claimed.

static int
STATE\_RUNNING
States that the activity is running.

static int
STATE\_SKIPPED
States that the activity has been skipped because navigation followed a
 a different control path.

static int
STATE\_STOPPED
States that the activity is stopped because of a failure.

static int
STATE\_TERMINATED
States that the activity has been terminated because of an external or internal request.

static int
STATE\_TERMINATING
States that the activity is terminating.

static int
STATE\_WAITING
States that a receive or pick activity is waiting for a corresponding event to occur.

static int
STOP\_REASON\_ACTIVATION\_FAILED
States that the activation of the activity failed.

static int
STOP\_REASON\_EXIT\_CONDITION\_FALSE
States that the exit condition of the activity evaluated to false.

static int
STOP\_REASON\_FOLLOW\_ON\_NAVIGATION\_FAILED
States that the follow on navigation of the activity failed.

static int
STOP\_REASON\_IMPLEMENTATION\_FAILED
States that the implementation of the activity failed.

static int
STOP\_REASON\_UNSPECIFIED
States that the activity is not stopped.

static int
SUB\_STATE\_EXPIRING
Do not use - internal only.

static int
SUB\_STATE\_FAILING
Do not use - internal only.

static int
SUB\_STATE\_FINISHING
Do not use - internal only.

static int
SUB\_STATE\_NONE
Do not use - internal only.

static int
SUB\_STATE\_RESTARTING
Do not use - internal only.

static int
SUB\_STATE\_SKIPPING
Do not use - internal only.
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.util.Calendar
getActivationTime()
Returns the activation time of the activity instance.

ATID
getActivityTemplateID()
Returns the object ID of the associated activity template.

TKIID
getAdminTaskID()
Returns the ID of the associated administration task.

java.lang.String
getApplicationName()
Returns the name of the enterprise application the activity belongs to.

int[]
getAvailableActions()
Returns the actions that can be called in the current activity instance
 execution state.

java.util.Calendar
getCompletionTime()
Returns the completion time of the activity instance.

java.lang.String
getCustomProperty(java.lang.String arg0)
Returns the value of the specified custom property.

java.lang.String
getDescription()
Returns the description of the activity instance.

java.lang.String
getDisplayName()
Returns the display name of the activity instance.

com.ibm.bpe.api.FEIID
getEnclosingForEachID()
Returns the ID of the enclosing for-each activity if the activity is
 part of an for-each construct.

com.ibm.bpe.api.EHIID
getEventHandlerInstanceID()
Returns the ID of the associated event handler instance if the activity is
 part of an event handler.

int
getExecutionState()
Returns the execution state of the activity instance.

java.util.Calendar
getExpirationTime()
Returns the time when the activity instance will expire or expired.

java.util.List
getFaultNames()
Returns the names of faults associated to the activity instance.

AIID
getID()
Returns the object identifier.

java.lang.String
getInputMessageTypeName()
Returns the name of the input message type.

java.lang.String
getInputMessageTypeTypeSystemName()
Deprecated. 
As of version 6.0, no replacement.

OID
getInvokedInstanceID()
Returns the object ID of the process or task instance that is called by this activity.

int
getInvokedInstanceType()
Returns the type of object called by this activity, that is,
 describes the type of the object ID returned by
 getInvokedInstanceID.

int
getKind()
Returns the kind of the activity, for example, whether the activity is a
 pick or receive activity.

java.util.Calendar
getLastModificationTime()
Returns the last time a property of the activity instance changed.

java.util.Calendar
getLastStateChangeTime()
Returns the last time the execution state of the activity instance changed.

java.lang.String
getName()
Returns the name of the activity instance.

java.util.List
getNamesOfCustomProperties()
Returns the names of all custom properties.

java.lang.String
getOutputMessageTypeName()
Returns the name of the output message type.

java.lang.String
getOutputMessageTypeTypeSystemName()
Deprecated. 
As of version 6.0, no replacement.

java.lang.String
getOwner()
Returns the owner of the activity instance.

java.util.Calendar
getPreviousExpirationTime()
Returns the time the activity instance expired for the first time.

StaffResultSet
getProcessAdministrators()
Returns the administrators of the process instance that contains the activity instance.

TKIID
getProcessAdminTaskID()
Returns the ID of the administration task associated to the containing process instance.

PIID
getProcessInstanceID()
Returns the object ID of the containing process instance.

java.lang.String
getProcessInstanceName()
Returns the name of the process instance the activity belongs to.

PTID
getProcessTemplateID()
Returns the object ID of the process template
 that contains the activity definition.

java.lang.String
getProcessTemplateName()
Returns the name of the first process template in the hierarchy
 that contains the activity definition.

com.ibm.bpe.api.SIID
getScopeID()
Returns the ID of the associated scope.

com.ibm.bpe.api.STID
getScopeTemplateID()
Returns the ID of the scope template that is associated to the
 scope the activity is part of.

java.util.Calendar
getStartTime()
Returns the start time of the activity instance.

int
getStopReason()
Returns the reason why the activity is in the Stopped execution state.

int
getSubState()
Returns the sub state of the activity instance
 
 Possible values are:
 SUB\_STATE\_NONE, SUB\_STATE\_EXPIRING, SUB\_STATE\_SKIPPING, SUB\_STATE\_RESTARTING,
 SUB\_STATE\_FINISHING, SUB\_STATE\_FAILING.

TKIID
getTaskID()
For human task activities, returns the ID of the associated inline to-do aka participating task.

ProcessException
getUnhandledException()
Returns the reason why the activity is in the Stopped execution state.

boolean
isBusinessRelevant()
States whether the activity instance is a business relevant or an "auxiliary" step.

boolean
isContinueOnError()
States whether the activity instance stops navigation of the process
 in case of an unhandled error or not.

boolean
isSkipRequested()
States whether the activity instance is to be skipped when reached during navigation.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- STATE\_FAILING
static final int STATE\_FAILING
States that the activity is failing. The activity is set
 to the Failed execution state when all contained running or terminating activities end.
See Also:Constant Field Values

- STATE\_TERMINATING
static final int STATE\_TERMINATING
States that the activity is terminating. The activity is set
 to the Terminated execution state when all contained running or terminating activities end.
See Also:Constant Field Values

- STATE\_FAILED
static final int STATE\_FAILED
States that the activity failed to execute.
See Also:Constant Field Values

- STATE\_INACTIVE
static final int STATE\_INACTIVE
States that the activity has not yet been scheduled for execution.
See Also:Constant Field Values

- STATE\_FINISHED
static final int STATE\_FINISHED
States that the activity finished execution successfully.
See Also:Constant Field Values

- STATE\_PROCESSING\_UNDO
static final int STATE\_PROCESSING\_UNDO
States that the activity is retried due to a transaction rollback and that
 the activity waits for the microflow that it invokes to complete its compensation actions for the
 first invoke.
See Also:Constant Field Values

- STATE\_READY
static final int STATE\_READY
States that the activity is ready to be started or claimed.
See Also:Constant Field Values

- STATE\_EXPIRED
static final int STATE\_EXPIRED
States that the activity ended because its allowed duration timed-out.
See Also:Constant Field Values

- STATE\_RUNNING
static final int STATE\_RUNNING
States that the activity is running.
See Also:Constant Field Values

- STATE\_TERMINATED
static final int STATE\_TERMINATED
States that the activity has been terminated because of an external or internal request.
See Also:Constant Field Values

- STATE\_WAITING
static final int STATE\_WAITING
States that a receive or pick activity is waiting for a corresponding event to occur.
See Also:Constant Field Values

- STATE\_CLAIMED
static final int STATE\_CLAIMED
States that the activity has been claimed.
See Also:Constant Field Values

- STATE\_SKIPPED
static final int STATE\_SKIPPED
States that the activity has been skipped because navigation followed a
 a different control path.
See Also:Constant Field Values

- STATE\_STOPPED
static final int STATE\_STOPPED
States that the activity is stopped because of a failure. A process administrator
 can repair the activity by either calling forceRetry or forceComplete.
See Also:Constant Field Values

- KIND\_COMPENSATION\_THROW\_EVENT
static final int KIND\_COMPENSATION\_THROW\_EVENT
Do not use - internal only.
See Also:Constant Field Values

- KIND\_TIMER\_CATCH\_EVENT
static final int KIND\_TIMER\_CATCH\_EVENT
Do not use - internal only.
See Also:Constant Field Values

- KIND\_MESSAGE\_CATCH\_EVENT
static final int KIND\_MESSAGE\_CATCH\_EVENT
Do not use - internal only.
See Also:Constant Field Values

- KIND\_COMPENSATE\_SCOPE
static final int KIND\_COMPENSATE\_SCOPE
States that the activity is a compensate scope activity.
See Also:Constant Field Values

- KIND\_COMPENSATION\_INTERRUPTING\_SUBPROCESS\_START\_EVENT
static final int KIND\_COMPENSATION\_INTERRUPTING\_SUBPROCESS\_START\_EVENT
Do not use - internal only.
See Also:Constant Field Values

- KIND\_WHILE\_END
static final int KIND\_WHILE\_END
Do not use - internal only.
See Also:Constant Field Values

- KIND\_REPEAT\_UNTIL\_END
static final int KIND\_REPEAT\_UNTIL\_END
Do not use - internal only.
See Also:Constant Field Values

- KIND\_SEQUENCE
static final int KIND\_SEQUENCE
Describes a sequence construct that contains activities to be performed sequentially.
See Also:Constant Field Values

- KIND\_RECEIVE\_TASK
static final int KIND\_RECEIVE\_TASK
Do not use - internal only.
See Also:Constant Field Values

- KIND\_SWITCH\_END
static final int KIND\_SWITCH\_END
Do not use - internal only.
See Also:Constant Field Values

- KIND\_COMPENSATION\_END\_EVENT
static final int KIND\_COMPENSATION\_END\_EVENT
Do not use - internal only.
See Also:Constant Field Values

- KIND\_MESSAGE\_END\_EVENT
static final int KIND\_MESSAGE\_END\_EVENT
Do not use - internal only.
See Also:Constant Field Values

- KIND\_MESSAGE\_THROW\_EVENT
static final int KIND\_MESSAGE\_THROW\_EVENT
Do not use - internal only.
See Also:Constant Field Values

- KIND\_ERROR\_EVENT\_SUBPROCESS\_ACTIVITY
static final int KIND\_ERROR\_EVENT\_SUBPROCESS\_ACTIVITY
Do not use - internal only.
See Also:Constant Field Values

- KIND\_WAIT
static final int KIND\_WAIT
An activity that allows to wait for a given period of time.
See Also:Constant Field Values

- KIND\_FOR\_EACH\_PARALLEL
static final int KIND\_FOR\_EACH\_PARALLEL
States that the activity is a forEach activity with parallel branches.
See Also:Constant Field Values

- KIND\_IOR\_GATEWAY
static final int KIND\_IOR\_GATEWAY
Do not use - internal only.
See Also:Constant Field Values

- KIND\_FOR\_EACH\_PARALLEL\_END
static final int KIND\_FOR\_EACH\_PARALLEL\_END
Do not use - internal only.
See Also:Constant Field Values

- KIND\_TERMINATE\_END\_EVENT
static final int KIND\_TERMINATE\_END\_EVENT
Do not use - internal only.
See Also:Constant Field Values

- KIND\_USER\_TASK
static final int KIND\_USER\_TASK
Do not use - internal only.
See Also:Constant Field Values

- KIND\_TERMINATE
static final int KIND\_TERMINATE
States that the activity terminates execution.
See Also:Constant Field Values

- KIND\_PICK
static final int KIND\_PICK
States that the activity is an activity that waits for various input.
See Also:Constant Field Values

- KIND\_SWITCH
static final int KIND\_SWITCH
Describes a switch construct that allows to select an activity from a set of choices.
See Also:Constant Field Values

- KIND\_SEND\_TASK
static final int KIND\_SEND\_TASK
Do not use - internal only.
See Also:Constant Field Values

- KIND\_TIMER\_NONINTERRUPTING\_SUBPROCESS\_START\_EVENT
static final int KIND\_TIMER\_NONINTERRUPTING\_SUBPROCESS\_START\_EVENT
Do not use - internal only.
See Also:Constant Field Values

- KIND\_INVOKE
static final int KIND\_INVOKE
States that the activity describes some external service to be invoked.
See Also:Constant Field Values

- KIND\_SCRIPT\_TASK
static final int KIND\_SCRIPT\_TASK
Do not use - internal only.
See Also:Constant Field Values

- KIND\_IOR\_IN\_GATEWAY
static final int KIND\_IOR\_IN\_GATEWAY
Do not use - internal only.
See Also:Constant Field Values

- KIND\_MESSAGE\_START\_EVENT
static final int KIND\_MESSAGE\_START\_EVENT
Do not use - internal only.
See Also:Constant Field Values

- KIND\_CUSTOM
static final int KIND\_CUSTOM
An activity that provides a plug-in mechanism for customer written implementations.
See Also:Constant Field Values

- KIND\_INVOKE\_END
static final int KIND\_INVOKE\_END
Do not use - internal only.
See Also:Constant Field Values

- KIND\_RECEIVE
static final int KIND\_RECEIVE
States that the activity is an activity that waits for input.
See Also:Constant Field Values

- KIND\_SCOPE
static final int KIND\_SCOPE
Describes a scope construct that allows for own variable definitions, fault and compensation handlers.
See Also:Constant Field Values

- KIND\_ABSTRACT\_TASK
static final int KIND\_ABSTRACT\_TASK
Do not use - internal only.
See Also:Constant Field Values

- KIND\_SERVICE\_TASK
static final int KIND\_SERVICE\_TASK
Do not use - internal only.
See Also:Constant Field Values

- KIND\_WHILE
static final int KIND\_WHILE
An activity that is repeated until a certain criteria is met.
See Also:Constant Field Values

- KIND\_NONE\_END\_EVENT
static final int KIND\_NONE\_END\_EVENT
Do not use - internal only.
See Also:Constant Field Values

- KIND\_SCOPE\_END
static final int KIND\_SCOPE\_END
Do not use - internal only.
See Also:Constant Field Values

- KIND\_ERROR\_INTERRUPTING\_BOUNDARY\_EVENT
static final int KIND\_ERROR\_INTERRUPTING\_BOUNDARY\_EVENT
Do not use - internal only.
See Also:Constant Field Values

- KIND\_NONE\_START\_EVENT
static final int KIND\_NONE\_START\_EVENT
Do not use - internal only.
See Also:Constant Field Values

- KIND\_ASSIGN
static final int KIND\_ASSIGN
States that the activity specifies some assignment.
See Also:Constant Field Values

- KIND\_REPLY
static final int KIND\_REPLY
An activity that allows the process to send a message in reply to a message that was received.
See Also:Constant Field Values

- KIND\_MESSAGE\_EVENT\_SUBPROCESS\_ACTIVITY
static final int KIND\_MESSAGE\_EVENT\_SUBPROCESS\_ACTIVITY
Do not use - internal only.
See Also:Constant Field Values

- KIND\_PICK\_END
static final int KIND\_PICK\_END
Do not use - internal only.
See Also:Constant Field Values

- KIND\_RETHROW
static final int KIND\_RETHROW
States that the activity rethrows a fault.
See Also:Constant Field Values

- KIND\_EMPTY
static final int KIND\_EMPTY
States that the activity is an empty activity without any
 implementation. An empty activity is often used as synchronization point of parallel paths in the process.
See Also:Constant Field Values

- KIND\_REPEAT\_UNTIL
static final int KIND\_REPEAT\_UNTIL
An activity that is repeated until an exit condition is met.
See Also:Constant Field Values

- KIND\_EVENT\_BASED\_GATEWAY
static final int KIND\_EVENT\_BASED\_GATEWAY
Do not use - internal only.
See Also:Constant Field Values

- KIND\_SCRIPT
static final int KIND\_SCRIPT
States that the activity is implemented by plain Java code.
See Also:Constant Field Values

- KIND\_SEQUENCE\_END
static final int KIND\_SEQUENCE\_END
Do not use - internal only.
See Also:Constant Field Values

- KIND\_COMPENSATE
static final int KIND\_COMPENSATE
States that the activity is a compensating activity.
See Also:Constant Field Values

- KIND\_SUBPROCESS\_ACTIVITY
static final int KIND\_SUBPROCESS\_ACTIVITY
Do not use - internal only.
See Also:Constant Field Values

- KIND\_ERROR\_INTERRUPTING\_SUBPROCESS\_START\_EVENT
static final int KIND\_ERROR\_INTERRUPTING\_SUBPROCESS\_START\_EVENT
Do not use - internal only.
See Also:Constant Field Values

- KIND\_STAFF
static final int KIND\_STAFF
States that the activity involves people for its execution.
See Also:Constant Field Values

- KIND\_TIMER\_EVENT\_SUBPROCESS\_ACTIVITY
static final int KIND\_TIMER\_EVENT\_SUBPROCESS\_ACTIVITY
Do not use - internal only.
See Also:Constant Field Values

- KIND\_XOR\_GATEWAY
static final int KIND\_XOR\_GATEWAY
Do not use - internal only.
See Also:Constant Field Values

- KIND\_MESSAGE\_NONINTERRUPTING\_SUBPROCESS\_START\_EVENT
static final int KIND\_MESSAGE\_NONINTERRUPTING\_SUBPROCESS\_START\_EVENT
Do not use - internal only.
See Also:Constant Field Values

- KIND\_FLOW
static final int KIND\_FLOW
An activity that specifies one or more activities to be performed concurrently.
See Also:Constant Field Values

- KIND\_FLOW\_END
static final int KIND\_FLOW\_END
Do not use - internal only.
See Also:Constant Field Values

- KIND\_THROW
static final int KIND\_THROW
States that the activity throws a fault.
See Also:Constant Field Values

- KIND\_FOR\_EACH\_SERIAL\_END
static final int KIND\_FOR\_EACH\_SERIAL\_END
Do not use - internal only.
See Also:Constant Field Values

- KIND\_PARALLEL\_GATEWAY
static final int KIND\_PARALLEL\_GATEWAY
Do not use - internal only.
See Also:Constant Field Values

- KIND\_ERROR\_END\_EVENT
static final int KIND\_ERROR\_END\_EVENT
Do not use - internal only.
See Also:Constant Field Values

- KIND\_CALL\_ACTIVITY
static final int KIND\_CALL\_ACTIVITY
Do not use - internal only.
See Also:Constant Field Values

- KIND\_TIMER\_INTERRUPTING\_BOUNDARY\_EVENT
static final int KIND\_TIMER\_INTERRUPTING\_BOUNDARY\_EVENT
Do not use - internal only.
See Also:Constant Field Values

- KIND\_FOR\_EACH\_SERIAL
static final int KIND\_FOR\_EACH\_SERIAL
States that the activity is a forEach activity with no parallel branches.
See Also:Constant Field Values

- STOP\_REASON\_IMPLEMENTATION\_FAILED
static final int STOP\_REASON\_IMPLEMENTATION\_FAILED
States that the implementation of the activity failed.
See Also:Constant Field Values

- STOP\_REASON\_EXIT\_CONDITION\_FALSE
static final int STOP\_REASON\_EXIT\_CONDITION\_FALSE
States that the exit condition of the activity evaluated to false.
 Note: this field must be kept in sync with MigrationFront.stopReason.
See Also:Constant Field Values

- STOP\_REASON\_FOLLOW\_ON\_NAVIGATION\_FAILED
static final int STOP\_REASON\_FOLLOW\_ON\_NAVIGATION\_FAILED
States that the follow on navigation of the activity failed.
See Also:Constant Field Values

- STOP\_REASON\_ACTIVATION\_FAILED
static final int STOP\_REASON\_ACTIVATION\_FAILED
States that the activation of the activity failed.
See Also:Constant Field Values

- STOP\_REASON\_UNSPECIFIED
static final int STOP\_REASON\_UNSPECIFIED
States that the activity is not stopped.
See Also:Constant Field Values

- INVOKED\_INSTANCE\_TYPE\_INLINE\_TASK
static final int INVOKED\_INSTANCE\_TYPE\_INLINE\_TASK
States that the activity calls an inline human task.
See Also:Constant Field Values

- INVOKED\_INSTANCE\_TYPE\_CHILD\_PROCESS
static final int INVOKED\_INSTANCE\_TYPE\_CHILD\_PROCESS
States that the activity calls a long-running process
 that has "child" autonomy. The process
 containing this activity and the process called are both long-running.
See Also:Constant Field Values

- INVOKED\_INSTANCE\_TYPE\_CHILD\_TASK
static final int INVOKED\_INSTANCE\_TYPE\_CHILD\_TASK
States that the activity calls a stand-alone task
 that has "child" autonomy.
See Also:Constant Field Values

- INVOKED\_INSTANCE\_TYPE\_NOT\_SET
static final int INVOKED\_INSTANCE\_TYPE\_NOT\_SET
States that the activity does not call a process or inline task,
 or does not call a process or stand-alone task that have "child" autonomy.
See Also:Constant Field Values

- SUB\_STATE\_EXPIRING
static final int SUB\_STATE\_EXPIRING
Do not use - internal only.
See Also:Constant Field Values

- SUB\_STATE\_SKIPPING
static final int SUB\_STATE\_SKIPPING
Do not use - internal only.
See Also:Constant Field Values

- SUB\_STATE\_RESTARTING
static final int SUB\_STATE\_RESTARTING
Do not use - internal only.
See Also:Constant Field Values

- SUB\_STATE\_FAILING
static final int SUB\_STATE\_FAILING
Do not use - internal only.
See Also:Constant Field Values

- SUB\_STATE\_NONE
static final int SUB\_STATE\_NONE
Do not use - internal only.
See Also:Constant Field Values

- SUB\_STATE\_FINISHING
static final int SUB\_STATE\_FINISHING
Do not use - internal only.
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getID
AIID getID()
Returns the object identifier.
    - getActivationTime
java.util.Calendar getActivationTime()
Returns the activation time of the activity instance.
    - getCompletionTime
java.util.Calendar getCompletionTime()
Returns the completion time of the activity instance. Returns null when
 the activity instance is not yet complete.
    - getLastModificationTime
java.util.Calendar getLastModificationTime()
Returns the last time a property of the activity instance changed.
    - getLastStateChangeTime
java.util.Calendar getLastStateChangeTime()
Returns the last time the execution state of the activity instance changed.
    - getName
java.lang.String getName()
Returns the name of the activity instance. Returns null if there is no name.
    - getDisplayName
java.lang.String getDisplayName()
Returns the display name of the activity instance. Returns null when
 a display name is not assigned.
    - getDescription
java.lang.String getDescription()
Returns the description of the activity instance. If there is no activity
 instance description, the description of the associated activity template is
 returned. If there is no activity template description, null is
 returned. References to variable members specified as %variableName.memberName%
 are resolved.
    - getOwner
java.lang.String getOwner()
Returns the owner of the activity instance. Returns null when
 an owner is not assigned.
    - getStartTime
java.util.Calendar getStartTime()
Returns the start time of the activity instance. Returns null when the
 activity instance is not yet started.
    - getExecutionState
int getExecutionState()
Returns the execution state of the activity instance.
 
 Possible states are: STATE\_INACTIVE, STATE\_READY, STATE\_RUNNING, STATE\_CLAIMED,
 STATE\_FINISHED, STATE\_FAILING, STATE\_FAILED, STATE\_SKIPPED, STATE\_TERMINATED,
 STATE\_TERMINATING, STATE\_WAITING, STATE\_STOPPED, or STATE\_EXPIRED.
    - getExpirationTime
java.util.Calendar getExpirationTime()
Returns the time when the activity instance will expire or expired. Returns
 null when there is no expiration time.
    - getKind
int getKind()
Returns the kind of the activity, for example, whether the activity is a
 pick or receive activity.
    - getUnhandledException
ProcessException getUnhandledException()
Returns the reason why the activity is in the Stopped execution state.
    - getStopReason
int getStopReason()
Returns the reason why the activity is in the Stopped execution state.
 
 Possible values are:
 STOP\_REASON\_UNSPECIFIED, STOP\_REASON\_ACTIVATION\_FAILED,
 STOP\_REASON\_IMPLEMENTATION\_FAILED, STOP\_REASON\_FOLLOW\_ON\_NAVIGATION\_FAILED, or
 STOP\_REASON\_EXIT\_CONDITION\_FALSE.
Since:
6.1.2.
    - getProcessInstanceID
PIID getProcessInstanceID()
Returns the object ID of the containing process instance.
    - getProcessTemplateID
PTID getProcessTemplateID()
Returns the object ID of the process template
 that contains the activity definition.
    - getFaultNames
java.util.List getFaultNames()
Returns the names of faults associated to the activity instance.
    - getInputMessageTypeName
java.lang.String getInputMessageTypeName()
Returns the name of the input message type.
 A BPEL process returns a value only when there is a single input variable associated.
    - getInputMessageTypeTypeSystemName
java.lang.String getInputMessageTypeTypeSystemName()
Deprecated. As of version 6.0, no replacement.
Returns the name of the type system of the input message.
 A BPEL process returns a value only when there is a single input variable associated.
    - getOutputMessageTypeName
java.lang.String getOutputMessageTypeName()
Returns the name of the output message type.
 A BPEL process returns a value only when there is a single output variable associated.
    - getOutputMessageTypeTypeSystemName
java.lang.String getOutputMessageTypeTypeSystemName()
Deprecated. As of version 6.0, no replacement.
Returns the name of the type system of the output message.
 A BPEL process returns a value only when there is a single output variable associated.
    - getAvailableActions
int[] getAvailableActions()
Returns the actions that can be called in the current activity instance
 execution state. Refer to ActivityInstanceActions for the
 set of possible actions.
    - getCustomProperty
java.lang.String getCustomProperty(java.lang.String arg0)
Returns the value of the specified custom property.
 Returns null when the specified custom property is not found.
 
Parameters:arg0 - The name of the custom property for which the value is to be read.
    - getNamesOfCustomProperties
java.util.List getNamesOfCustomProperties()
Returns the names of all custom properties.
 Returns an empty list when there are no custom properties.
    - getProcessAdministrators
StaffResultSet getProcessAdministrators()
                                        throws WorkItemManagerException,
                                               InvalidLengthException
Returns the administrators of the process instance that contains the activity instance.
Throws:
WorkItemManagerException
InvalidLengthException
    - getApplicationName
java.lang.String getApplicationName()
Returns the name of the enterprise application the activity belongs to.
    - getProcessTemplateName
java.lang.String getProcessTemplateName()
Returns the name of the first process template in the hierarchy
 that contains the activity definition.
    - getProcessInstanceName
java.lang.String getProcessInstanceName()
Returns the name of the process instance the activity belongs to.
    - isBusinessRelevant
boolean isBusinessRelevant()
States whether the activity instance is a business relevant or an "auxiliary" step.
    - getTaskID
TKIID getTaskID()
For human task activities, returns the ID of the associated inline to-do aka participating task.
 Returns null when the activity is no human task activity calling an inline to-do task.
    - getAdminTaskID
TKIID getAdminTaskID()
Returns the ID of the associated administration task.
 Returns null if there is no administration task.
    - getProcessAdminTaskID
TKIID getProcessAdminTaskID()
Returns the ID of the administration task associated to the containing process instance.
 Returns null if there is no administration task.
    - getScopeID
com.ibm.bpe.api.SIID getScopeID()
Returns the ID of the associated scope.
Since:
6.1.2.
    - getScopeTemplateID
com.ibm.bpe.api.STID getScopeTemplateID()
Returns the ID of the scope template that is associated to the
 scope the activity is part of.
Since:
6.1.2.
    - getEventHandlerInstanceID
com.ibm.bpe.api.EHIID getEventHandlerInstanceID()
Returns the ID of the associated event handler instance if the activity is
 part of an event handler.
 Returns null when the activity is not part of an event handler.
Since:
6.1.2.
    - getEnclosingForEachID
com.ibm.bpe.api.FEIID getEnclosingForEachID()
Returns the ID of the enclosing for-each activity if the activity is
 part of an for-each construct.
 Returns null when the activity is not part of a for-each construct.
Since:
6.1.2.
    - isSkipRequested
boolean isSkipRequested()
States whether the activity instance is to be skipped when reached during navigation.
Since:
6.1.2.
    - isContinueOnError
boolean isContinueOnError()
States whether the activity instance stops navigation of the process
 in case of an unhandled error or not. True states that navigation
 continues in case of an unhandled error. False states that navigation
 stops in case of an unhandled error to allow for repair.
 
 This setting can be overwritten when calling
 forceComplete or
 forceRetry.
Since:
6.1.2.
    - getActivityTemplateID
ATID getActivityTemplateID()
Returns the object ID of the associated activity template.
Since:
6.2.
    - getInvokedInstanceID
OID getInvokedInstanceID()
Returns the object ID of the process or task instance that is called by this activity.
 Returns null
 for activities navigated by an IBM Websphere Workflow Server Version less than 6.2,
 when the activity does not call a long-running process or task,
 when the long-running process or stand-alone task called does not have child autonomy,
 or when the inline task called is no human task.
 
 You can use
 getInvokedInstanceType
 to determine whether the object ID returned is a PIID or TKIID.
Since:
6.2.
    - getInvokedInstanceType
int getInvokedInstanceType()
Returns the type of object called by this activity, that is,
 describes the type of the object ID returned by
 getInvokedInstanceID.
 Using this method, you can determine whether a PIID or TKIID is returned.
 
 States INVOKED\_INSTANCE\_TYPE\_NOT\_SET when no object ID is returned by
 getInvokedInstanceID.
Since:
6.2.
    - getSubState
int getSubState()
Returns the sub state of the activity instance
 
 Possible values are:
 SUB\_STATE\_NONE, SUB\_STATE\_EXPIRING, SUB\_STATE\_SKIPPING, SUB\_STATE\_RESTARTING,
 SUB\_STATE\_FINISHING, SUB\_STATE\_FAILING.
Since:
7.0.
    - getPreviousExpirationTime
java.util.Calendar getPreviousExpirationTime()
Returns the time the activity instance expired for the first time.
 Returns null when the activity did not expire.
Since:
7.0.