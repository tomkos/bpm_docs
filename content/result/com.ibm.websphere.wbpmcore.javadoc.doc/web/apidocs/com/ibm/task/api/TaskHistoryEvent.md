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

## Interface TaskHistoryEvent

- All Superinterfaces:
java.io.Serializable

public interface TaskHistoryEvent
extends java.io.Serializable
Accesses the properties of a task history event.
 
 A task history event represents an event that occurrs during the lifetime of a task instance.
 Note that task history events are only written when writing these records is enabled.
 
Since:
7.5

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
EVENT\_ESCALATION\_CUSTOMPROPERTY\_SET
States that a custom property is set for an escalation.

static int
EVENT\_ESCALATION\_FIRED
States that an escalation is fired.

static int
EVENT\_ESCALATION\_STARTED
States that an escalation is started.

static int
EVENT\_ESCALATION\_UPDATED
States that an escalation is updated.

static int
EVENT\_ESCALATION\_WORKITEM\_CREATED
States that a work item is created for an escalation.

static int
EVENT\_ESCALATION\_WORKITEM\_DELETED
States that a work item is deleted for an escalation.

static int
EVENT\_ESCALATION\_WORKITEM\_REFRESHED
States that a work item is refreshed for an escalation.

static int
EVENT\_ESCALATION\_WORKITEM\_TRANSFERRED
States that a work item is transferred for an escalation.

static int
EVENT\_TASK\_CLAIM\_CANCELLED
States that the claim of the task is cancelled.

static int
EVENT\_TASK\_CLAIMED
States that the task is claimed.

static int
EVENT\_TASK\_COMPLETED
States that the task is completed.

static int
EVENT\_TASK\_COMPLETED\_WITH\_FOLLOW\_ON\_TASK
States that the task completed and created follow-on tasks.

static int
EVENT\_TASK\_CREATED
States that the task is created.

static int
EVENT\_TASK\_CUSTOMPROPERTY\_SET
States that a custom property is set on the task.

static int
EVENT\_TASK\_DELETED
States that the task is deleted.

static int
EVENT\_TASK\_EXPIRED
States that the task is expired.

static int
EVENT\_TASK\_FAILED
States that the task is failed.

static int
EVENT\_TASK\_FAULT\_MESSAGE\_UPDATED
States that a fault message of the task is updated.

static int
EVENT\_TASK\_INPUT\_MESSAGE\_UPDATED
States that the input message of the task is updated.

static int
EVENT\_TASK\_OUTPUT\_MESSAGE\_UPDATED
States that the output message of the task is updated.

static int
EVENT\_TASK\_RESTARTED
States that the task is restarted.

static int
EVENT\_TASK\_RESUMED
States that the task is resumed.

static int
EVENT\_TASK\_STARTED
States that the task is started.

static int
EVENT\_TASK\_SUBTASKS\_COMPLETED
States that subtasks completed for the task.

static int
EVENT\_TASK\_SUSPENDED
States that the task is suspended.

static int
EVENT\_TASK\_TEMPLATE\_INSTALLED
States that a task template is installed.

static int
EVENT\_TASK\_TEMPLATE\_UNINSTALLED
States that a task template is uninstalled.

static int
EVENT\_TASK\_TERMINATED
States that the task is terminated.

static int
EVENT\_TASK\_UPDATED
States that the task is updated.

static int
EVENT\_TASK\_WAITING\_FOR\_SUBTASK
States that the task is waiting for subtasks to complete.

static int
EVENT\_TASK\_WORKITEM\_CREATED
States that a work item is created for the task.

static int
EVENT\_TASK\_WORKITEM\_DELETED
States that a work item is deleted for the task.

static int
EVENT\_TASK\_WORKITEM\_REFRESHED
States that a work item is refreshed for the task,

static int
EVENT\_TASK\_WORKITEM\_TRANSFERRED
States that a work item is transferred for the task.

static int
REASON\_ADMINISTRATOR
States that operations can be executed on the associated object that require
 administrator rights, for example, deletion of an object.

static int
REASON\_EDITOR
States that operations can be executed on the associated object that require
 editor authority, for example, setting the output message of an object.

static int
REASON\_ESCALATION\_RECEIVER
States that operations can be executed on the associated object that require
 escalation receiver rights, for example, reading properties of an object that is escalated.

static int
REASON\_MAX
Do not use - internal only.

static int
REASON\_NONE
States that no reason is logged.

static int
REASON\_ORIGINATOR
States that operations can be executed on the associated object that require
 originator rights.

static int
REASON\_OWNER
States that the associated object can be completed.

static int
REASON\_POTENTIAL\_INSTANCE\_CREATOR
States that operations can be executed on the associated object that require
 instance creator rights, for example, creating objects.

static int
REASON\_POTENTIAL\_OWNER
States that the associated object can be claimed.

static int
REASON\_POTENTIAL\_SENDER
Do not use - internal only.

static int
REASON\_POTENTIAL\_STARTER
States that operations can be executed on the associated object that require
 potential starter rights, for example, creating objects.

static int
REASON\_READER
States that operations can be executed on the associated object that require
 reader authority, for example, reading the properties of an object.

static int
REASON\_STARTER
States that operations can be executed on the associated object that require
 starter authority.

static int
REASON\_STATE\_MACHINE\_END
Do not use - internal only.

static int
REASON\_STATE\_MACHINE\_EVENT\_AVAILABLE
Do not use - internal only.

static int
REASON\_STATE\_MACHINE\_START
Do not use - internal only.

static int
WORK\_ITEM\_KIND\_EVERYBODY
States that the work item is assigned to everybody.

static int
WORK\_ITEM\_KIND\_GROUP
States that the work item is assigned to one or more groups.

static int
WORK\_ITEM\_KIND\_USER
States that the work item is assigned to one or more users.
    - Method Summary

Methods 

Modifier and Type
Method and Description

int
getAssignmentReason()
Returns the reason of work item data logged in this event.

ESIID
getEscalationInstanceID()
Returns the object ID of an escalation instance if the event is associated with
 an escalation.

java.util.Calendar
getEventTime()
Returns the time when the logged event occurred.

int
getEventType()
Returns the type of the event.

java.lang.String
getFromOwner()
Returns the name of the user or group whose work item is transferred to the to-owner,
 or whose work item is deleted.

java.util.Calendar
getNextEventTime()
Returns the time when the next event is due to occur, if any.

TKIID
getParentContextID()
Returns the object ID of a related task instance, if the task instance is a
 subtask or follow-on task of a parent task.

java.lang.String
getPrincipal()
Returns the name of the principal who triggered the event.

TKIID
getTaskInstanceID()
Returns the object ID of the associated task instance.

java.lang.String
getToOwner()
Returns the name of the user or group for whom a work item is created, or transferred to.

int
getWorkItemKind()
States the kind of work item authorization.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- EVENT\_ESCALATION\_UPDATED
static final int EVENT\_ESCALATION\_UPDATED
States that an escalation is updated.
See Also:Constant Field Values

- EVENT\_ESCALATION\_FIRED
static final int EVENT\_ESCALATION\_FIRED
States that an escalation is fired.
See Also:Constant Field Values

- EVENT\_ESCALATION\_WORKITEM\_REFRESHED
static final int EVENT\_ESCALATION\_WORKITEM\_REFRESHED
States that a work item is refreshed for an escalation.
See Also:Constant Field Values

- EVENT\_ESCALATION\_WORKITEM\_DELETED
static final int EVENT\_ESCALATION\_WORKITEM\_DELETED
States that a work item is deleted for an escalation.
See Also:Constant Field Values

- EVENT\_TASK\_UPDATED
static final int EVENT\_TASK\_UPDATED
States that the task is updated.
See Also:Constant Field Values

- EVENT\_TASK\_CLAIMED
static final int EVENT\_TASK\_CLAIMED
States that the task is claimed.
See Also:Constant Field Values

- EVENT\_TASK\_RESUMED
static final int EVENT\_TASK\_RESUMED
States that the task is resumed.
See Also:Constant Field Values

- EVENT\_TASK\_STARTED
static final int EVENT\_TASK\_STARTED
States that the task is started.
See Also:Constant Field Values

- EVENT\_TASK\_TERMINATED
static final int EVENT\_TASK\_TERMINATED
States that the task is terminated.
See Also:Constant Field Values

- EVENT\_TASK\_WORKITEM\_TRANSFERRED
static final int EVENT\_TASK\_WORKITEM\_TRANSFERRED
States that a work item is transferred for the task.
See Also:Constant Field Values

- EVENT\_TASK\_CUSTOMPROPERTY\_SET
static final int EVENT\_TASK\_CUSTOMPROPERTY\_SET
States that a custom property is set on the task.
See Also:Constant Field Values

- EVENT\_TASK\_CLAIM\_CANCELLED
static final int EVENT\_TASK\_CLAIM\_CANCELLED
States that the claim of the task is cancelled.
See Also:Constant Field Values

- EVENT\_TASK\_COMPLETED\_WITH\_FOLLOW\_ON\_TASK
static final int EVENT\_TASK\_COMPLETED\_WITH\_FOLLOW\_ON\_TASK
States that the task completed and created follow-on tasks.
See Also:Constant Field Values

- EVENT\_TASK\_WAITING\_FOR\_SUBTASK
static final int EVENT\_TASK\_WAITING\_FOR\_SUBTASK
States that the task is waiting for subtasks to complete.
See Also:Constant Field Values

- EVENT\_TASK\_WORKITEM\_REFRESHED
static final int EVENT\_TASK\_WORKITEM\_REFRESHED
States that a work item is refreshed for the task,
See Also:Constant Field Values

- EVENT\_TASK\_TEMPLATE\_INSTALLED
static final int EVENT\_TASK\_TEMPLATE\_INSTALLED
States that a task template is installed.
See Also:Constant Field Values

- EVENT\_TASK\_WORKITEM\_DELETED
static final int EVENT\_TASK\_WORKITEM\_DELETED
States that a work item is deleted for the task.
See Also:Constant Field Values

- EVENT\_TASK\_FAILED
static final int EVENT\_TASK\_FAILED
States that the task is failed.
See Also:Constant Field Values

- EVENT\_TASK\_WORKITEM\_CREATED
static final int EVENT\_TASK\_WORKITEM\_CREATED
States that a work item is created for the task.
See Also:Constant Field Values

- EVENT\_ESCALATION\_CUSTOMPROPERTY\_SET
static final int EVENT\_ESCALATION\_CUSTOMPROPERTY\_SET
States that a custom property is set for an escalation.
See Also:Constant Field Values

- EVENT\_TASK\_TEMPLATE\_UNINSTALLED
static final int EVENT\_TASK\_TEMPLATE\_UNINSTALLED
States that a task template is uninstalled.
See Also:Constant Field Values

- EVENT\_TASK\_FAULT\_MESSAGE\_UPDATED
static final int EVENT\_TASK\_FAULT\_MESSAGE\_UPDATED
States that a fault message of the task is updated.
See Also:Constant Field Values

- EVENT\_ESCALATION\_WORKITEM\_CREATED
static final int EVENT\_ESCALATION\_WORKITEM\_CREATED
States that a work item is created for an escalation.
See Also:Constant Field Values

- EVENT\_TASK\_SUSPENDED
static final int EVENT\_TASK\_SUSPENDED
States that the task is suspended.
See Also:Constant Field Values

- EVENT\_ESCALATION\_WORKITEM\_TRANSFERRED
static final int EVENT\_ESCALATION\_WORKITEM\_TRANSFERRED
States that a work item is transferred for an escalation.
See Also:Constant Field Values

- EVENT\_ESCALATION\_STARTED
static final int EVENT\_ESCALATION\_STARTED
States that an escalation is started.
See Also:Constant Field Values

- EVENT\_TASK\_EXPIRED
static final int EVENT\_TASK\_EXPIRED
States that the task is expired.
See Also:Constant Field Values

- EVENT\_TASK\_SUBTASKS\_COMPLETED
static final int EVENT\_TASK\_SUBTASKS\_COMPLETED
States that subtasks completed for the task.
See Also:Constant Field Values

- EVENT\_TASK\_DELETED
static final int EVENT\_TASK\_DELETED
States that the task is deleted.
See Also:Constant Field Values

- EVENT\_TASK\_INPUT\_MESSAGE\_UPDATED
static final int EVENT\_TASK\_INPUT\_MESSAGE\_UPDATED
States that the input message of the task is updated.
See Also:Constant Field Values

- EVENT\_TASK\_COMPLETED
static final int EVENT\_TASK\_COMPLETED
States that the task is completed.
See Also:Constant Field Values

- EVENT\_TASK\_OUTPUT\_MESSAGE\_UPDATED
static final int EVENT\_TASK\_OUTPUT\_MESSAGE\_UPDATED
States that the output message of the task is updated.
See Also:Constant Field Values

- EVENT\_TASK\_CREATED
static final int EVENT\_TASK\_CREATED
States that the task is created.
See Also:Constant Field Values

- EVENT\_TASK\_RESTARTED
static final int EVENT\_TASK\_RESTARTED
States that the task is restarted.
See Also:Constant Field Values

- REASON\_POTENTIAL\_SENDER
static final int REASON\_POTENTIAL\_SENDER
Do not use - internal only.
See Also:Constant Field Values

- REASON\_ESCALATION\_RECEIVER
static final int REASON\_ESCALATION\_RECEIVER
States that operations can be executed on the associated object that require
 escalation receiver rights, for example, reading properties of an object that is escalated.
See Also:Constant Field Values

- REASON\_STARTER
static final int REASON\_STARTER
States that operations can be executed on the associated object that require
 starter authority.
See Also:Constant Field Values

- REASON\_NONE
static final int REASON\_NONE
States that no reason is logged.
See Also:Constant Field Values

- REASON\_POTENTIAL\_INSTANCE\_CREATOR
static final int REASON\_POTENTIAL\_INSTANCE\_CREATOR
States that operations can be executed on the associated object that require
 instance creator rights, for example, creating objects.
See Also:Constant Field Values

- REASON\_STATE\_MACHINE\_EVENT\_AVAILABLE
static final int REASON\_STATE\_MACHINE\_EVENT\_AVAILABLE
Do not use - internal only.
See Also:Constant Field Values

- REASON\_EDITOR
static final int REASON\_EDITOR
States that operations can be executed on the associated object that require
 editor authority, for example, setting the output message of an object.
See Also:Constant Field Values

- REASON\_ORIGINATOR
static final int REASON\_ORIGINATOR
States that operations can be executed on the associated object that require
 originator rights.
See Also:Constant Field Values

- REASON\_MAX
static final int REASON\_MAX
Do not use - internal only.
See Also:Constant Field Values

- REASON\_STATE\_MACHINE\_START
static final int REASON\_STATE\_MACHINE\_START
Do not use - internal only.
See Also:Constant Field Values

- REASON\_POTENTIAL\_STARTER
static final int REASON\_POTENTIAL\_STARTER
States that operations can be executed on the associated object that require
 potential starter rights, for example, creating objects.
See Also:Constant Field Values

- REASON\_POTENTIAL\_OWNER
static final int REASON\_POTENTIAL\_OWNER
States that the associated object can be claimed.
See Also:Constant Field Values

- REASON\_ADMINISTRATOR
static final int REASON\_ADMINISTRATOR
States that operations can be executed on the associated object that require
 administrator rights, for example, deletion of an object.
See Also:Constant Field Values

- REASON\_STATE\_MACHINE\_END
static final int REASON\_STATE\_MACHINE\_END
Do not use - internal only.
See Also:Constant Field Values

- REASON\_READER
static final int REASON\_READER
States that operations can be executed on the associated object that require
 reader authority, for example, reading the properties of an object.
See Also:Constant Field Values

- REASON\_OWNER
static final int REASON\_OWNER
States that the associated object can be completed.
See Also:Constant Field Values

- WORK\_ITEM\_KIND\_EVERYBODY
static final int WORK\_ITEM\_KIND\_EVERYBODY
States that the work item is assigned to everybody.
See Also:Constant Field Values

- WORK\_ITEM\_KIND\_USER
static final int WORK\_ITEM\_KIND\_USER
States that the work item is assigned to one or more users.
See Also:Constant Field Values

- WORK\_ITEM\_KIND\_GROUP
static final int WORK\_ITEM\_KIND\_GROUP
States that the work item is assigned to one or more groups.
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getTaskInstanceID
TKIID getTaskInstanceID()
Returns the object ID of the associated task instance.
    - getEscalationInstanceID
ESIID getEscalationInstanceID()
Returns the object ID of an escalation instance if the event is associated with
 an escalation. Otherwise, returns null.
    - getParentContextID
TKIID getParentContextID()
Returns the object ID of a related task instance, if the task instance is a
 subtask or follow-on task of a parent task. Otherwise, returns null.
    - getEventType
int getEventType()
Returns the type of the event.
 See EVENT\_TASK\_CREATED etc.
    - getEventTime
java.util.Calendar getEventTime()
Returns the time when the logged event occurred.
    - getNextEventTime
java.util.Calendar getNextEventTime()
Returns the time when the next event is due to occur, if any.
 The time depends on the event type.
 
 EVENT\_TASK\_STARTED, the expiration time of the task instance.
 

 EVENT\_TASK\_SUSPENDED, the resumption time of the task instance.
 

 EVENT\_TASK\_COMPLETED, EVENT\_TASK\_TERMINATED, EVENT\_TASK\_EPIRED, and EVENT\_TASK\_FAILED,
 the time when the task instance is deleted automatically.
 

 EVENT\_ESCALATION\_STARTED, the time when the escalation fires.
 

 EVENT\_ESCALATION\_FIRED, the time when the escalation fires again.
    - getPrincipal
java.lang.String getPrincipal()
Returns the name of the principal who triggered the event.
    - getAssignmentReason
int getAssignmentReason()
Returns the reason of work item data logged in this event.
 Returns REASON\_NONE if no reason is logged.
    - getWorkItemKind
int getWorkItemKind()
States the kind of work item authorization.
 
 Possible authorization kinds are WORK\_ITEM\_KIND\_EVERYBODY, WORK\_ITEM\_KIND\_USER, WORK\_ITEM\_KIND\_GROUP.
    - getFromOwner
java.lang.String getFromOwner()
Returns the name of the user or group whose work item is transferred to the to-owner,
 or whose work item is deleted.
 Returns null when no work item is deleted or transferred.
    - getToOwner
java.lang.String getToOwner()
Returns the name of the user or group for whom a work item is created, or transferred to.
 Returns null when no work item is created or transferred.