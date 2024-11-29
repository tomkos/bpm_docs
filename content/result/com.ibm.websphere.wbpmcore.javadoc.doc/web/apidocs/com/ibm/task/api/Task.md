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

## Interface Task

- All Superinterfaces:
java.io.Serializable

All Known Implementing Classes:
TaskInstanceBean

public interface Task
extends java.io.Serializable
Accesses the properties of a task instance.
 
 A task represents a piece of work. It contains all data that is necessary to get
 the job done. For example, a task that is associated to a group of potential owners
 allows a person that belongs to the group to claim the task, work on the task,
 and to complete the task.
 
Since:
7.0 - introduced in 5.1

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
ASSIGNMENT\_TYPE\_PARALLEL
States that the task can be assigned to multiple persons in parallel.

static int
ASSIGNMENT\_TYPE\_SINGLE
States that the task can only be assigned to a single person.

static int
AUTH\_NONE
States that no operations can be executed on the associated context.

static int
AUTH\_READER
States that operations can be executed on the associated context object
 that require Reader authority, for example, reading the properties of a process instance.

static int
AUTO\_DELETE\_ON\_COMPLETION
States that a completed task instance is deleted when
 the duration until deletion has passed.

static int
AUTO\_DELETE\_ON\_SUCCESSFUL\_COMPLETION
States that the task instance is deleted when
 it reaches the FINISHED state.

static java.lang.String
COPYRIGHT 

static int
HIERARCHY\_POSITION\_FOLLOW\_ON\_TASK
The task is a follow-on task in the task collaboration hierarchy.

static int
HIERARCHY\_POSITION\_SUB\_TASK
The task is a subtask in the task collaboration hierarchy.

static int
HIERARCHY\_POSITION\_TOP\_TASK
The task is a toplevel task in the task collaboration hierarchy.

static int
INHERITED\_AUTH\_ADMINISTRATOR
States that administrator authorizations of all parent tasks in the parent task hierarchy
 are inherited by this subtask.

static int
INHERITED\_AUTH\_ALL
States that, additionally to the administrators, all other authorizations for parent tasks
 in the parent task hierarchy are inherited as reader authorization by this subtask.

static int
INHERITED\_AUTH\_NONE
States that no authorization is inherited from parent tasks by this subtask.

static int
INVOKED\_INSTANCE\_TYPE\_ACTIVITY
States that the task invoked an activity in a business process,

static int
INVOKED\_INSTANCE\_TYPE\_CHILD\_PROCESS
States that the activity calls a long-running process
 that has "child" autonomy.

static int
INVOKED\_INSTANCE\_TYPE\_CHILD\_TASK
States that the activity calls a stand-alone task
 that has "child" autonomy.

static int
INVOKED\_INSTANCE\_TYPE\_EVENT
States that the task invoked an activity in an event handler or an activity which is not yet ready to receive the event.

static int
INVOKED\_INSTANCE\_TYPE\_INLINE\_TASK
States that the activity calls an inline human task.

static int
INVOKED\_INSTANCE\_TYPE\_NOT\_SET
States that the activity does not call a process or inline task,
 or does not call a process or stand-alone task that have "child" autonomy.

static int
INVOKED\_INSTANCE\_TYPE\_PROCESS
States that the task invoked a business process,

static int
INVOKED\_INSTANCE\_TYPE\_TASK
States that the task invoked a stand-alone task.

static int
KIND\_ADMINISTRATIVE
States that the task is an administration task.

static int
KIND\_HUMAN
States that the task is created and processed by humans.

static int
KIND\_ORIGINATING
States that the task is a task whose service is invoked and
 tracked by the Human Task Manager.

static int
KIND\_PARTICIPATING
States that the task is processed by humans but tracked by the Human Task Manager.

static int
KIND\_WPC\_STAFF\_ACTIVITY
States that the task is processed by humans but controlled by the Business Flow Manager.

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
Deprecated.  

static int
STATE\_FINISHED
States that the activity finished execution successfully.

static int
STATE\_FORWARDED
States  that the task has been completed with a follow-on task.

static int
STATE\_INACTIVE
States that the activity has not yet been scheduled for execution.

static int
STATE\_PROCESSING\_UNDO
Deprecated.  

static int
STATE\_READY
States that the activity is ready to be started or claimed.

static int
STATE\_RUNNING
States that the activity is running.

static int
STATE\_SKIPPED
Deprecated.  

static int
STATE\_STOPPED
Deprecated.  

static int
STATE\_TERMINATED
States that the activity has been terminated because of an external or internal request.

static int
STATE\_TERMINATING
Deprecated.  

static int
STATE\_WAITING
Deprecated.  

static int
SUBSTITUTION\_POLICY\_NO\_SUBSTITUTION
States that no substitution should take place.

static int
SUBSTITUTION\_POLICY\_SELECT\_USER\_IF\_PRESENT
States that only present users should act for absent users.

static int
SUBSTITUTION\_POLICY\_SUBSTITUTE\_IF\_ABSENT
States that substitutes should act for absent users.
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.util.Calendar
getActivationTime()
Returns the time the task instance is set into the ready state.

ACOID
getApplicationDefaultsID()
Returns the ID of the application component that specifies the defaults for
 the task.

java.lang.String
getApplicationName()
Returns the name of the application the task is part of.

int
getAssignmentType()
Returns whether the task can be assigned to a single person only or
 to multiple persons in parallel.

int
getAutoDeletionMode()
Returns whether the task instance is automatically or
 conditionally deleted when it reaches an end execution state.

java.lang.String
getCalendarName()
Returns the name of the calendar used, for example, for expiration calculations.

java.util.Calendar
getCompletionTime()
Returns the time when the task instance reached an end state.

OID
getContainmentContextID()
Returns the ID of the context which embraces the task instance.

int
getContextAuthorizationOfOwner()
Returns the authorization rights of the task owner to the associated context.

java.lang.String
getCustomText1()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_1.

java.lang.String
getCustomText2()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_2.

java.lang.String
getCustomText3()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_3.

java.lang.String
getCustomText4()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_4.

java.lang.String
getCustomText5()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_5.

java.lang.String
getCustomText6()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_6.

java.lang.String
getCustomText7()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_7.

java.lang.String
getCustomText8()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_8.

java.lang.String
getDefinitionName()
Returns the name of the task definition in the TEL.

java.lang.String
getDefinitionNamespace()
Returns the namespace of the task definition in the TEL.

java.util.Calendar
getDeletionTime()
Returns the time when the task is deleted.

java.lang.String
getDescription(java.util.Locale arg0)
Returns the description in the specified locale.

java.lang.String
getDisplayName(java.util.Locale arg0)
Returns the display name in the specified locale.

java.util.Calendar
getDueTime()
Returns the time when the task is due.

java.lang.String
getDurationUntilDeleted()
Returns the duration that the task is kept after it has
 reached an end state.

java.lang.String
getDurationUntilDue()
Returns the duration that may pass before the task becomes due.

java.lang.String
getDurationUntilExpires()
Returns the duration when the task expires once it is activated.

java.lang.String
getEventHandlerName()
Returns the name of the associated event handler.

java.util.Calendar
getExpirationTime()
Returns the time when the task instance expires or has expired.

java.util.Calendar
getFirstActivationTime()
Returns the time the task instance is set into the ready state for the
 first time.

TKIID
getFollowOnTaskID()
Returns the object ID of the next task instance in a sequence.

TKIID
getID()
Returns the object identifier.

int
getInheritedAuthorization()
States for a subtask which kind of authorization is inherited from a parent task.

java.lang.String
getInputMessageTypeName()
Returns the name of the input message type.

OID
getInvokedInstanceID()
Returns the object ID of the invoked service, for example, the object ID of
 a process, an activity, or task instance.

int
getInvokedInstanceType()
Returns the type of service called by this task, that is,
 describes the type of the object ID returned by
 getInvokedInstanceID.

java.lang.String
getJNDINameOfCalendar()
Returns the JNDI name of a user-defined calendar.

java.lang.String
getJNDINameOfStaffPluginProvider()
Returns the JNDI name of a user-defined people directory configuation.

int
getKind()
Returns the kind of the task.

java.util.Calendar
getLastModificationTime()
Returns the last time a property of the task instance changed.

java.util.Calendar
getLastStateChangeTime()
Returns the last time the state of the task instance changed.

java.util.List
getLocalesOfDescriptions()
Returns the locales of all descriptions.

java.util.List
getLocalesOfDisplayNames()
Returns the locales of all display names.

java.lang.String
getName()
Returns the name of the task instance.

java.lang.String
getNamespace()
Returns the namespace that categorizes the task instance.

java.lang.String
getOriginator()
Returns the user ID of the user that created the task instance or on whose behalf
 the task instance was created.

java.lang.String
getOutputMessageTypeName()
Returns the name of the output message type.

java.lang.String
getOwner()
Returns the owner of the task instance.

OID
getParentContextID()
Returns the object ID of the parent context of the task instance.

int
getPositionInHierarchy()
Returns the position in a possible task instance hierarchy.

java.lang.Integer
getPriority()
Returns the priority of the task instance.

java.util.Calendar
getResumptionTime()
Returns the resumption time of the task instance if the task instance
 is suspended and is to be resumed automatically.

java.lang.String
getStarter()
Returns the starter of the task instance.

java.util.Calendar
getStartTime()
Returns the time when execution of the task started.

int
getState()
Returns the state of the task instance.

int
getSubstitutionPolicy()
Returns the substitution policy that takes place when people assignments are performed.

TKTID
getTaskTemplateID()
Returns the object ID of the task template this instance is derived
 from.

java.lang.String
getTaskTemplateName()
Returns the name of the task template this instance is derived
 from.

TKIID
getTopLevelTaskID()
Returns the object ID of the topmost task instance in a hierarchy of tasks.

java.lang.String
getType()
Returns the type of the task.

java.lang.String
getWorkBasketName()
Returns the name of the work basket the task belongs to.

boolean
isAdHoc()
States whether the task has been created ad hoc.

boolean
isBusinessRelevanceUpdateable()
Signals whether the business relevance property can be changed for the kind and current state of the object.

boolean
isBusinessRelevant()
States whether the task is a business relevant or an "auxiliary" step.

boolean
isChild()
States for stand-alone tasks whether the task instance runs dependently of its parent or not.

boolean
isContextAuthorizationOfOwnerUpdateable()
Signals whether the context authorization property can be changed for the kind and current state of the object.

boolean
isDeletionTimeUpdateable()
Signals whether the deletion time property can be changed for the kind and current state of the object.

boolean
isDescriptionUpdateable()
Signals whether the description property can be changed for the kind and current state of the object.

boolean
isDisplayNameUpdateable()
Signals whether the display name property can be changed for the kind and current state of the object.

boolean
isDueTimeUpdateable()
Signals whether the due time property can be changed for the kind and current state of the object.

boolean
isDurationUntilDeletedUpdateable()
Signals whether the duration until deleted property can be changed for the kind and current state of the object.

boolean
isDurationUntilDueUpdateable()
Signals whether the duration until due property can be changed for the kind and current state of the object.

boolean
isDurationUntilExpiresUpdateable()
Signals whether the duration until expires property can be changed for the kind and current state of the object.

boolean
isEscalated()
States whether an escalation occurred.

boolean
isEscalatedUpdateable()
Signals whether the isEscalated property can be changed for the kind and current state of the object.

boolean
isEventHandlerNameUpdateable()
Signals whether the event handler name property can be changed for the kind and current state of the object.

boolean
isExpirationTimeUpdateable()
Signals whether the expiration time property can be changed for the kind and current state of the object.

boolean
isInline()
States whether the task is an inline task or not.

boolean
isNamespaceUpdateable()
Signals whether the namespace property can be changed for the kind and current state of the object.

boolean
isNameUpdateable()
Signals whether the name property can be changed for the kind and current state of the object.

boolean
isParentContextIDUpdateable()
Signals whether the parent context ID property can be changed for the kind and current state of the object.

boolean
isPriorityUpdateable()
Signals whether the priority property can be changed for the kind and current state of the object.

boolean
isRead()
States whether the task instance is marked read.

boolean
isReadUpdateable()
Signals whether the isRead property can be changed for the kind and current state of the object.

boolean
isSupportsClaimIfSuspendedUpdateable()
Signals whether the supports claim suspended property can be changed for the kind and current state of the object.

boolean
isSupportsDelegationUpdateable()
Signals whether the supports delegation property can be changed for the kind and current state of the object.

boolean
isSupportsFollowOnTasksUpdateable()
Signals whether the supports follow on task property can be changed for the kind and current state of the object.

boolean
isSupportsSubTasksUpdateable()
Signals whether the supports sub task property can be changed for the kind and current state of the object.

boolean
isSuspended()
States whether the task instance is suspended or not.

boolean
isTransferredToWorkBasket()
States whether the task instance had been transferred to some work basket.

boolean
isTypeUpdateable()
Signals whether the type property can be changed for the kind and current state of the object.

boolean
isWaitingForSubTask()
States whether the task is waiting for the completion of a subtask.

boolean
isWorkBasketNameUpdateable()
Signals whether the work basket property can be changed for the kind and current state of the object.

void
setBusinessRelevance(boolean businessRelevance)
Sets whether the task is a business relevant or an "auxiliary" step.

void
setContextAuthorizationOfOwner(int contextAuthorization)
Sets the authorization rights of the task owner to the associated context.

void
setDeletionTime(java.util.Calendar deletionTime)
Sets the time when the task is to be deleted.

void
setDescription(java.lang.String description,
              java.util.Locale locale)
Sets the description in the specified locale.

void
setDisplayName(java.lang.String displayName,
              java.util.Locale locale)
Sets the display name in the specified locale.

void
setDueTime(java.util.Calendar dueTime)
Sets the time the task is expected to become due.

void
setDurationUntilDeleted(java.lang.String durationUntilDeleted)
Sets the duration that passes until the task is deleted after it reached an end state.

void
setDurationUntilDue(java.lang.String durationUntilDue)
Sets the duration the task is expected to become due.

void
setDurationUntilExpires(java.lang.String durationUntilExpires)
Sets the duration that may pass until the task expires.

void
setEscalated(boolean isEscalated)
Sets the escalation state of the task, that is, allows to manually escalate a task.

void
setEventHandlerName(java.lang.String eventHandlerName)
Sets the name of the associated event handler.

void
setExpirationTime(java.util.Calendar expirationTime)
Sets the time when the task expires.

void
setName(java.lang.String name)
Sets the name of the task instance.

void
setNamespace(java.lang.String namespace)
Sets the namespace for the task name and type properties.

void
setParentContextID(OID parentContextID)
Sets the object ID of the parent context.

void
setPriority(java.lang.Integer priority)
Sets the priority of the task instance.

void
setRead(boolean isRead)
Marks the task instance as read.

void
setSupportsClaimIfSuspended(boolean supportsClaimSuspended)
Sets whether the task can be claimed if it is suspended.

void
setSupportsDelegation(boolean supportsDelegation)
Sets whether the task supports delegation, for example, by transferring work items.

void
setSupportsFollowOnTasks(boolean supportsFollowOnTask)
Sets whether the task supports the creation of follow-on tasks.

void
setSupportsSubTasks(boolean supportsSubTask)
Sets whether the task supports the creation of subtasks.

void
setType(java.lang.String type)
Sets the type of the task instance.

void
setWorkBasketName(java.lang.String workBasket)
Sets the name of the work basket the task belongs to.

boolean
supportsAutomaticClaim()
States whether the task is claimed automatically when it becomes ready.

boolean
supportsClaimIfSuspended()
States whether the task can be claimed even if it is suspended.

boolean
supportsDelegation()
States whether the task supports delegation, for example, by transferring work items.

boolean
supportsFollowOnTasks()
States whether the task supports the creation of follow-on tasks.

boolean
supportsSubTasks()
States whether the task supports the creation of subtasks.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- STATE\_FAILING
static final int STATE\_FAILING
Deprecated. 
States that the activity associated to the task is failing. The activity associated to the task is set
 to the Failed execution state when all contained running or terminating activities end.
See Also:Constant Field Values

- STATE\_TERMINATING
static final int STATE\_TERMINATING
Deprecated. 
States that the activity associated to the task is terminating. The activity associated to the task is set
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
Deprecated. 
States that the activity associated to the task is retried due to a transaction rollback and that
 the activity associated to the task waits for the microflow that it invokes to complete its compensation actions for the
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

- STATE\_FORWARDED
static final int STATE\_FORWARDED
States  that the task has been completed with a follow-on task.
See Also:Constant Field Values

- STATE\_WAITING
static final int STATE\_WAITING
Deprecated. 
States that a receive or pick activity associated to the task is waiting for a corresponding event to occur.
See Also:Constant Field Values

- STATE\_CLAIMED
static final int STATE\_CLAIMED
States that the activity has been claimed.
See Also:Constant Field Values

- STATE\_SKIPPED
static final int STATE\_SKIPPED
Deprecated. 
States that the activity associated to the task has been skipped because navigation followed a
 a different control path.
See Also:Constant Field Values

- STATE\_STOPPED
static final int STATE\_STOPPED
Deprecated. 
States that the activity associated to the task is stopped because of a failure. A process administrator
 can repair the activity associated to the task by either calling forceRetry or forceComplete.
See Also:Constant Field Values

- KIND\_PARTICIPATING
static final int KIND\_PARTICIPATING
States that the task is processed by humans but tracked by the Human Task Manager.
See Also:Constant Field Values

- KIND\_ADMINISTRATIVE
static final int KIND\_ADMINISTRATIVE
States that the task is an administration task.
See Also:Constant Field Values

- KIND\_WPC\_STAFF\_ACTIVITY
static final int KIND\_WPC\_STAFF\_ACTIVITY
States that the task is processed by humans but controlled by the Business Flow Manager.
 (deprecated)
See Also:Constant Field Values

- KIND\_HUMAN
static final int KIND\_HUMAN
States that the task is created and processed by humans.
See Also:Constant Field Values

- KIND\_ORIGINATING
static final int KIND\_ORIGINATING
States that the task is a task whose service is invoked and
 tracked by the Human Task Manager.
See Also:Constant Field Values

- AUTH\_READER
static final int AUTH\_READER
States that operations can be executed on the associated context object
 that require Reader authority, for example, reading the properties of a process instance.
See Also:Constant Field Values

- AUTH\_NONE
static final int AUTH\_NONE
States that no operations can be executed on the associated context.
See Also:Constant Field Values

- HIERARCHY\_POSITION\_SUB\_TASK
static final int HIERARCHY\_POSITION\_SUB\_TASK
The task is a subtask in the task collaboration hierarchy.
See Also:Constant Field Values

- HIERARCHY\_POSITION\_FOLLOW\_ON\_TASK
static final int HIERARCHY\_POSITION\_FOLLOW\_ON\_TASK
The task is a follow-on task in the task collaboration hierarchy.
See Also:Constant Field Values

- HIERARCHY\_POSITION\_TOP\_TASK
static final int HIERARCHY\_POSITION\_TOP\_TASK
The task is a toplevel task in the task collaboration hierarchy.
See Also:Constant Field Values

- AUTO\_DELETE\_ON\_SUCCESSFUL\_COMPLETION
static final int AUTO\_DELETE\_ON\_SUCCESSFUL\_COMPLETION
States that the task instance is deleted when
 it reaches the FINISHED state. If the task instance
 completes successfully, then it is deleted when the duration until deletion
 has passed. If the task instance did not complete successfully, it
 it is not deleted regardless of the specification of the duration until deletion.
See Also:Constant Field Values

- AUTO\_DELETE\_ON\_COMPLETION
static final int AUTO\_DELETE\_ON\_COMPLETION
States that a completed task instance is deleted when
 the duration until deletion has passed.
See Also:Constant Field Values

- SUBSTITUTION\_POLICY\_SELECT\_USER\_IF\_PRESENT
static final int SUBSTITUTION\_POLICY\_SELECT\_USER\_IF\_PRESENT
States that only present users should act for absent users.
 If all users and their subsitutes are absent or excluded by people assignment criteria,
 users originally resolved are returned.
See Also:Constant Field Values

- SUBSTITUTION\_POLICY\_NO\_SUBSTITUTION
static final int SUBSTITUTION\_POLICY\_NO\_SUBSTITUTION
States that no substitution should take place.
 All users resolved by people assignment criteria are returned.
See Also:Constant Field Values

- SUBSTITUTION\_POLICY\_SUBSTITUTE\_IF\_ABSENT
static final int SUBSTITUTION\_POLICY\_SUBSTITUTE\_IF\_ABSENT
States that substitutes should act for absent users.
 If all substitutes are absent or explicitely excluded by people assignment criteria,
 default people assignments are performed, for example, task administrators become potential owners.
See Also:Constant Field Values

- ASSIGNMENT\_TYPE\_PARALLEL
static final int ASSIGNMENT\_TYPE\_PARALLEL
States that the task can be assigned to multiple persons in parallel.
See Also:Constant Field Values

- ASSIGNMENT\_TYPE\_SINGLE
static final int ASSIGNMENT\_TYPE\_SINGLE
States that the task can only be assigned to a single person.
See Also:Constant Field Values

- INHERITED\_AUTH\_NONE
static final int INHERITED\_AUTH\_NONE
States that no authorization is inherited from parent tasks by this subtask.
See Also:Constant Field Values

- INHERITED\_AUTH\_ALL
static final int INHERITED\_AUTH\_ALL
States that, additionally to the administrators, all other authorizations for parent tasks
 in the parent task hierarchy are inherited as reader authorization by this subtask.
 For example, reader authorizations, potential\_owner authorizations etc
 are all inherited as reader authorizations.
See Also:Constant Field Values

- INHERITED\_AUTH\_ADMINISTRATOR
static final int INHERITED\_AUTH\_ADMINISTRATOR
States that administrator authorizations of all parent tasks in the parent task hierarchy
 are inherited by this subtask.
See Also:Constant Field Values

- INVOKED\_INSTANCE\_TYPE\_ACTIVITY
static final int INVOKED\_INSTANCE\_TYPE\_ACTIVITY
States that the task invoked an activity in a business process,
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

- INVOKED\_INSTANCE\_TYPE\_TASK
static final int INVOKED\_INSTANCE\_TYPE\_TASK
States that the task invoked a stand-alone task.
See Also:Constant Field Values

- INVOKED\_INSTANCE\_TYPE\_EVENT
static final int INVOKED\_INSTANCE\_TYPE\_EVENT
States that the task invoked an activity in an event handler or an activity which is not yet ready to receive the event.
See Also:Constant Field Values

- INVOKED\_INSTANCE\_TYPE\_PROCESS
static final int INVOKED\_INSTANCE\_TYPE\_PROCESS
States that the task invoked a business process,
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getID
TKIID getID()
Returns the object identifier.
    - getState
int getState()
Returns the state of the task instance. Possible states are:
 STATE\_INACTIVE, STATE\_READY, STATE\_RUNNING, STATE\_FINISHED, STATE\_FAILED,
 STATE\_TERMINATED, STATE\_CLAIMED, STATE\_EXPIRED, STATE\_FORWARDED.
    - isSuspended
boolean isSuspended()
States whether the task instance is suspended or not. Returns
 true when the task is suspended. Returns false when the task is not
 suspended.
    - isAdHoc
boolean isAdHoc()
States whether the task has been created ad hoc. True states that
 the task has been created ad hoc. False states that the task
 has been derived from a task template.
    - isInline
boolean isInline()
States whether the task is an inline task or not. True states that
 the task is an inline task. False states
 that the task is not an inline task.
    - getActivationTime
java.util.Calendar getActivationTime()
Returns the time the task instance is set into the ready state. If the task
 is not yet activated, null is returned. The activation time changes
 each time the task is set into the ready state, for example, when it is
 claimed and when the claim is cancelled.
    - getFirstActivationTime
java.util.Calendar getFirstActivationTime()
Returns the time the task instance is set into the ready state for the
 first time. If the task is not yet activated, null is returned.
    - getCompletionTime
java.util.Calendar getCompletionTime()
Returns the time when the task instance reached an end state. If the task instance
 is not yet completed, null is returned.
    - getLastModificationTime
java.util.Calendar getLastModificationTime()
Returns the last time a property of the task instance changed.
    - getLastStateChangeTime
java.util.Calendar getLastStateChangeTime()
Returns the last time the state of the task instance changed.
    - getExpirationTime
java.util.Calendar getExpirationTime()
Returns the time when the task instance expires or has expired. Returns
 null when there is no expiration time.
 
 This time is either set explicitely or
 calculated from the duration until expiration time.
    - getOriginator
java.lang.String getOriginator()
Returns the user ID of the user that created the task instance or on whose behalf
 the task instance was created. For example, returns the starter of a BPEL process.
    - getStarter
java.lang.String getStarter()
Returns the starter of the task instance. Returns null when
 a starter is not assigned or when the task is not an invocation aka originating task instance.
    - getOwner
java.lang.String getOwner()
Returns the owner of the task instance. Returns null when
 an owner is not assigned.
    - getContainmentContextID
OID getContainmentContextID()
Returns the ID of the context which embraces the task instance. This ID
 is used for task instance deletion. In other words, when the context is deleted,
 the task instance is also deleted. For example, a task instance associated to a BPEL
 process returns the containing process instance ID.
    - getParentContextID
OID getParentContextID()
Returns the object ID of the parent context of the task instance. For example, the parent
 of a human task activity (staff activity), that is, the parent of the associated
 inline to-do task (participating task), is the object ID of the human task activity (AIID).
 The parent context ID of a subtask is the object ID of the parent task (TKIID).
 The parent context ID of a stand-alone task is the object ID of the associated application component (ACOID).
    - getName
java.lang.String getName()
Returns the name of the task instance. Returns null if there is no name.
    - getKind
int getKind()
Returns the kind of the task.
 
 Possible values are:
 KIND\_HUMAN,
 KIND\_ORIGINATING,
 KIND\_PARTICIPATING,
 KIND\_ADMINISTRATIVE,
 KIND\_WPC\_STAFF\_ACTIVITY.
    - getDisplayName
java.lang.String getDisplayName(java.util.Locale arg0)
Returns the display name in the specified locale.
 Returns the display name in the default locale when a display name in
 the specified locale is not found.
 
 If no locale is specified, the display name in the default locale is returned
 or any available display name, if there is only a single display name.
 
Parameters:arg0 - The locale for which the display name is to be provided.
    - getLocalesOfDisplayNames
java.util.List getLocalesOfDisplayNames()
Returns the locales of all display names.
 Returns an empty list when there are no display names.
    - getDescription
java.lang.String getDescription(java.util.Locale arg0)
Returns the description in the specified locale.
 Returns the description in the default locale when a description in
 the specified locale is not found.
 
 If no locale is specified, the description in the default locale is returned
 or any available description, if there is only a single description.
 References to variable members specified as %variableName.memberName%
 are resolved.
 
Parameters:arg0 - The locale for which the description is to be provided.
    - getLocalesOfDescriptions
java.util.List getLocalesOfDescriptions()
Returns the locales of all descriptions.
 Returns an empty list when there are no descriptions.
    - isBusinessRelevant
boolean isBusinessRelevant()
States whether the task is a business relevant or an "auxiliary" step. A
 business relevant step can, for example, be logged into the audit trail.
    - getInputMessageTypeName
java.lang.String getInputMessageTypeName()
Returns the name of the input message type.
 Note that the structure of the input message type name is a QName.
    - getOutputMessageTypeName
java.lang.String getOutputMessageTypeName()
Returns the name of the output message type.
 Note that the structure of the output message type name is a QName.
    - getApplicationDefaultsID
ACOID getApplicationDefaultsID()
Returns the ID of the application component that specifies the defaults for
 the task. If the task is derived from a template, then the information in the template
 overwrites the defaults provided by the application component.
    - supportsAutomaticClaim
boolean supportsAutomaticClaim()
States whether the task is claimed automatically when it becomes ready. Note that the
 task is claimed automatically only when there is a single potential owner.
    - getCalendarName
java.lang.String getCalendarName()
Returns the name of the calendar used, for example, for expiration calculations. If
 not set, null is returned and the WebSphere default calendar is used. If a JNDI name
 for a user-defined calendar is specified, then the calendar name is the name of a
 method implementing that user-defined calendar - see
 getJNDINameOfCalendar.
 
 For details on calendars refer to the WebSphere Application Server documentation.
    - getJNDINameOfCalendar
java.lang.String getJNDINameOfCalendar()
Returns the JNDI name of a user-defined calendar. If
 not set, null is returned and a WebSphere supported calendar is used -
 see getCalendarName.
 
 For details on calendars refer to the WebSphere Application Server documentation.
    - getDueTime
java.util.Calendar getDueTime()
Returns the time when the task is due. The due time is
 either set explicitely or
 calculated from the duration until due time.
 
 If the due time is not set, null is returned.
 
 Note that the task manager does not check whether a task is overdue.
 Instead, the escalation concept can be used to trigger
 notifications.
    - getDurationUntilDeleted
java.lang.String getDurationUntilDeleted()
Returns the duration that the task is kept after it has
 reached an end state. When the duration has passed, it gets deleted.
 
 A specification TimerSpecification.DURATION\_IMMEDIATE
 means that the task is deleted immediately.
 A specification TimerSpecification.DURATION\_INFINITE
 means that the task is not deleted automatically.
 A specification TimerSpecification.DURATION\_NOT\_USED
 means that the deletion time is set explicitely - see
 setDeletionTime.
 
 If not set, then stand-alone invocation or collaboration tasks are kept
 whereas stand-alone to-do tasks are deleted immediately.
 Collaboration, invocation, and to-do tasks are also known as
 human, originating, and participating tasks.
 
 Inline tasks are
 always deleted together with their container, for example, the process instance.
 
 Note that this setting is checked depending on the automatic deletion mode -
 AutoDeletionMode.
    - getDurationUntilDue
java.lang.String getDurationUntilDue()
Returns the duration that may pass before the task becomes due. See
 setDurationUntilDue
 or setDueTime.
 
 A specification TimerSpecification.DURATION\_IMMEDIATE
 means that the task is due immediately.
 A specification TimerSpecification.DURATION\_INFINITE
 means that the task does not become due.
 A specification TimerSpecification.DURATION\_NOT\_USED
 means that the due time is set explicitely - see
 setDueTime.
 
 This property is a WebSphere Application Server calendar expression
 according to the calendar referenced by its name and JNDI name.
    - getDurationUntilExpires
java.lang.String getDurationUntilExpires()
Returns the duration when the task expires once it is activated.
 
 A specification TimerSpecification.DURATION\_IMMEDIATE
 means that the task expires immediately.
 A specification TimerSpecification.DURATION\_INFINITE
 means that the task does not expire.
 A specification TimerSpecification.DURATION\_NOT\_USED
 means that the expiration time is set explicitely - see
 setExpirationTime.
 
 This property is a WebSphere Application Server calendar expression
 according to the calendar referenced by its name and JNDI name.
    - isEscalated
boolean isEscalated()
States whether an escalation occurred.
 Refer to setEscalated for setting the value explicitely.
    - getJNDINameOfStaffPluginProvider
java.lang.String getJNDINameOfStaffPluginProvider()
Returns the JNDI name of a user-defined people directory configuation.
    - getNamespace
java.lang.String getNamespace()
Returns the namespace that categorizes the task instance.
    - getPriority
java.lang.Integer getPriority()
Returns the priority of the task instance. No special meaning is associated
 with this property. Escalations may, however, increase
 the priority of associated tasks. A caller can, for example,
 use it for sorting a list of tasks.
    - getStartTime
java.util.Calendar getStartTime()
Returns the time when execution of the task started. This is, for example, the
 time when a collaboration or to-do task is claimed or
 when an invocation task starts running.
    - supportsDelegation
boolean supportsDelegation()
States whether the task supports delegation, for example, by transferring work items.
    - supportsSubTasks
boolean supportsSubTasks()
States whether the task supports the creation of subtasks.
    - getTopLevelTaskID
TKIID getTopLevelTaskID()
Returns the object ID of the topmost task instance in a hierarchy of tasks.
 If the current tasks instance is the topmost task instance itself, the object ID
 of the current task instance is returned.
    - getFollowOnTaskID
TKIID getFollowOnTaskID()
Returns the object ID of the next task instance in a sequence.
 If there is no follow-on task instance, null is returned.
    - getTaskTemplateID
TKTID getTaskTemplateID()
Returns the object ID of the task template this instance is derived
 from. Returns null when the task is not derived from a template.
    - getTaskTemplateName
java.lang.String getTaskTemplateName()
Returns the name of the task template this instance is derived
 from. Returns null when the task is not derived from a template.
    - getType
java.lang.String getType()
Returns the type of the task. Returns null when there is no associated
 type.
    - isWaitingForSubTask
boolean isWaitingForSubTask()
States whether the task is waiting for the completion of a subtask.
    - getContextAuthorizationOfOwner
int getContextAuthorizationOfOwner()
Returns the authorization rights of the task owner to the associated context.
 
 Possible values are:
 AUTH\_NONE, AUTH\_READER.
    - supportsClaimIfSuspended
boolean supportsClaimIfSuspended()
States whether the task can be claimed even if it is suspended. True states that
 the task can be claimed if it is suspended. False states that the task cannot
 be claimed if it is suspended.
    - getEventHandlerName
java.lang.String getEventHandlerName()
Returns the name of the associated event handler. Returns
 null if there is no event handler.
    - getPositionInHierarchy
int getPositionInHierarchy()
Returns the position in a possible task instance hierarchy.
 
 Values are:
 HIERARCHY\_POSITION\_TOP\_TASK, HIERARCHY\_POSITION\_SUB\_TASK, HIERARCHY\_POSITION\_FOLLOW\_ON\_TASK.
    - getResumptionTime
java.util.Calendar getResumptionTime()
Returns the resumption time of the task instance if the task instance
 is suspended and is to be resumed automatically. If the task instance
 is not suspended or not to be resumed automatically, null is returned.
Since:
6.1.
    - getAutoDeletionMode
int getAutoDeletionMode()
Returns whether the task instance is automatically or
 conditionally deleted when it reaches an end execution state. Refer to
 AutoDeletionMode for the possible deletion modes.
 
 End execution states are STATE\_FINISHED, STATE\_FAILED, STATE\_TERMINATED, or
 STATE\_EXPIRED.
 
 Note that the task instance is actually deleted depending on the duration until deletion specification -
 refer to getDurationUntilDeleted.
Since:
6.1.
    - getDefinitionName
java.lang.String getDefinitionName()
Returns the name of the task definition in the TEL.
Since:
6.1.
    - getDefinitionNamespace
java.lang.String getDefinitionNamespace()
Returns the namespace of the task definition in the TEL.
Since:
6.1.
    - getSubstitutionPolicy
int getSubstitutionPolicy()
Returns the substitution policy that takes place when people assignments are performed.
 
 Possible substitution policies are SUBSTITUTION\_POLICY\_NO\_SUBSTITUTION, SUBSTITUTION\_POLICY\_SUBSTITUTE\_IF\_ABSENT,
 SUBSTITUTION\_POLICY\_SELECT\_USER\_IF\_PRESENT.
Since:
6.1.
    - supportsFollowOnTasks
boolean supportsFollowOnTasks()
States whether the task supports the creation of follow-on tasks.
Since:
6.1.
    - getApplicationName
java.lang.String getApplicationName()
Returns the name of the application the task is part of.
Since:
6.1.
    - isChild
boolean isChild()
States for stand-alone tasks whether the task instance runs dependently of its parent or not.
 True states that the stand-alone task is a child of its parent. False states
 that the stand-alone task is no child of its parent.
 When there is no parent or when the task is an inline task, false is returned.
Since:
6.2.
    - getDeletionTime
java.util.Calendar getDeletionTime()
Returns the time when the task is deleted. The deletion time is
 either set explicitely or
 calculated from the duration until deletion time.
 
 If the deletion time is not set, null is returned.
Since:
6.2.
    - getAssignmentType
int getAssignmentType()
Returns whether the task can be assigned to a single person only or
 to multiple persons in parallel.
 
 Possible assignment types are ASSIGNMENT\_TYPE\_SINGLE,
 ASSIGNMENT\_TYPE\_PARALLEL.
Since:
7.0.
    - getInheritedAuthorization
int getInheritedAuthorization()
States for a subtask which kind of authorization is inherited from a parent task.
 
 Possible values are INHERITED\_AUTH\_NONE, INHERITED\_AUTH\_ADMINISTRATOR,
 INHERITED\_AUTH\_ALL.
Since:
7.0.
    - getInvokedInstanceID
OID getInvokedInstanceID()
Returns the object ID of the invoked service, for example, the object ID of
 a process, an activity, or task instance.
 Returns null
 for invoked services run by an IBM Websphere Workflow Server Version less than 7.0,
 when the task called is not an invocation task.
 or when the invoked service is unknown to the Human Task Manager.
 
 You can use
 getInvokedInstanceType
 to determine whether the object ID returned is a PIID, AIID, or TKIID.
Since:
7.0.
    - getInvokedInstanceType
int getInvokedInstanceType()
Returns the type of service called by this task, that is,
 describes the type of the object ID returned by
 getInvokedInstanceID.
 Using this method, you can determine whether a PIID, AIID, or TKIID is returned.
 
 States INVOKED\_INSTANCE\_TYPE\_NOT\_SET when no object ID is returned by
 getInvokedInstanceID.
Since:
7.0.
    - isRead
boolean isRead()
States whether the task instance is marked read. True states that
 the task is marked read. False states that the task is not marked read.
 Refer to setRead or
 setTaskRead for setting the value.
Since:
7.0.
    - isTransferredToWorkBasket
boolean isTransferredToWorkBasket()
States whether the task instance had been transferred to some work basket. True states that
 the task had been transferred to some work basket. False states that the task
 had not been transferred to some work basket.
Since:
7.0.
    - getWorkBasketName
java.lang.String getWorkBasketName()
Returns the name of the work basket the task belongs to.
 Returns null if the task does not belong to any work basket.
 Refer to setWorkBasketName for setting the value.
Since:
7.0.
    - getCustomText1
java.lang.String getCustomText1()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_1.
 Refer to setInlineCustomProperty
 for setting the value.
Since:
7.5.1.
    - getCustomText2
java.lang.String getCustomText2()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_2.
 Refer to setInlineCustomProperty
 for setting the value.
Since:
7.5.1.
    - getCustomText3
java.lang.String getCustomText3()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_3.
 Refer to setInlineCustomProperty
 for setting the value.
Since:
7.5.1.
    - getCustomText4
java.lang.String getCustomText4()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_4.
 Refer to setInlineCustomProperty
 for setting the value.
Since:
7.5.1.
    - getCustomText5
java.lang.String getCustomText5()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_5.
 Refer to setInlineCustomProperty
 for setting the value.
Since:
7.5.1.
    - getCustomText6
java.lang.String getCustomText6()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_6.
 Refer to setInlineCustomProperty
 for setting the value.
Since:
7.5.1.
    - getCustomText7
java.lang.String getCustomText7()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_7.
 Refer to setInlineCustomProperty
 for setting the value.
Since:
7.5.1.
    - getCustomText8
java.lang.String getCustomText8()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_8.
 Refer to setInlineCustomProperty
 for setting the value.
Since:
7.5.1.
    - setDisplayName
void setDisplayName(java.lang.String displayName,
                  java.util.Locale locale)
Sets the display name in the specified locale.
 
Parameters:displayName - The new value of the display name.locale - The locale for which the display name is set.
    - isDisplayNameUpdateable
boolean isDisplayNameUpdateable()
Signals whether the display name property can be changed for the kind and current state of the object.
    - setDescription
void setDescription(java.lang.String description,
                  java.util.Locale locale)
Sets the description in the specified locale.
 
Parameters:description - The new value of the description.locale - The locale for which the description is set.
    - isDescriptionUpdateable
boolean isDescriptionUpdateable()
Signals whether the description property can be changed for the kind and current state of the object.
    - setSupportsClaimIfSuspended
void setSupportsClaimIfSuspended(boolean supportsClaimSuspended)
Sets whether the task can be claimed if it is suspended.
 
Parameters:supportsClaimSuspended - An indication whether the task can be claimed even if it is suspended. True states that
 the task can be claimed if it is suspended. False states that the task cannot be claimed
 if it is suspended.
    - isSupportsClaimIfSuspendedUpdateable
boolean isSupportsClaimIfSuspendedUpdateable()
Signals whether the supports claim suspended property can be changed for the kind and current state of the object.
    - setContextAuthorizationOfOwner
void setContextAuthorizationOfOwner(int contextAuthorization)
Sets the authorization rights of the task owner to the associated context.
 
Parameters:contextAuthorization - The authorization rights of the task owner for the associated context.
 
 Possible values are:
 AUTH\_NONE, AUTH\_READER.
    - isContextAuthorizationOfOwnerUpdateable
boolean isContextAuthorizationOfOwnerUpdateable()
Signals whether the context authorization property can be changed for the kind and current state of the object.
    - setName
void setName(java.lang.String name)
Sets the name of the task instance.
 
Parameters:name - The new name of the task instance.
    - isNameUpdateable
boolean isNameUpdateable()
Signals whether the name property can be changed for the kind and current state of the object.
    - setNamespace
void setNamespace(java.lang.String namespace)
Sets the namespace for the task name and type properties.
 
Parameters:namespace - The new namespace of the task instance.
    - isNamespaceUpdateable
boolean isNamespaceUpdateable()
Signals whether the namespace property can be changed for the kind and current state of the object.
    - setDurationUntilDue
void setDurationUntilDue(java.lang.String durationUntilDue)
Sets the duration the task is expected to become due. The due time is calculated
 once the task reaches the ready state, or recalculated when the ready state
 is already reached or passed.
 
 This value is also used when restarting the task instance.
 
 Note that the due time is informal only and not used for scheduling.
 
Parameters:durationUntilDue - The duration the task instance is expected to become due. The format of the
 duration depends on the calendar that is used and may, for example, be "5days".
 Additionally, TimerSpecification.DURATION\_IMMEDIATE
 may be specified to indicate that the task is due immediately
 and TimerSpecification.DURATION\_INFINITE
 to indicate that the task has no due time.
    - isDurationUntilDueUpdateable
boolean isDurationUntilDueUpdateable()
Signals whether the duration until due property can be changed for the kind and current state of the object.
    - setDueTime
void setDueTime(java.util.Calendar dueTime)
Sets the time the task is expected to become due.
 Note that the due time is informal only and not used for scheduling.
 
 Note, however, that updating this time prevents a duration until due to be calculated
 when restarting the task instance.
 
Parameters:dueTime - The time when the task instance is expected to become due.
 Note that setting the due time to null is not accepted by the update method,
 that is, an exception will be thrown,Since:
7.0.
    - isDueTimeUpdateable
boolean isDueTimeUpdateable()
Signals whether the due time property can be changed for the kind and current state of the object.
    - setDurationUntilDeleted
void setDurationUntilDeleted(java.lang.String durationUntilDeleted)
Sets the duration that passes until the task is deleted after it reached an end state.
 The deletion time is calculated once the task reaches an end state,
 or recalculated when the task is already in an end state.
 
 This value is also used to set up a deletion timer
 when restarting the task instance.
 
Parameters:durationUntilDeleted - The duration that passes until the task instance is deleted. The format of the
 duration depends on the calendar that is used and may, for example, be "5days".
 Additionally, TimerSpecification.DURATION\_IMMEDIATE
 may be specified to indicate that the task is to be deleted immediately
 and TimerSpecification.DURATION\_INFINITE
 to indicate that the task is deleted manually.
    - isDurationUntilDeletedUpdateable
boolean isDurationUntilDeletedUpdateable()
Signals whether the duration until deleted property can be changed for the kind and current state of the object.
    - setDeletionTime
void setDeletionTime(java.util.Calendar deletionTime)
Sets the time when the task is to be deleted. See also
 getDeletionTime.
 
 Note, however, that updating this time prevents a duration until deletion to be calculated
 when restarting the task instance. A deletion timer is then not set up.
 
Parameters:deletionTime - The time when the task instance is automatically deleted.
 Note that setting the deletion time to null is not accepted by the update method,
 that is, an exception will be thrown,Since:
7.0.
    - isDeletionTimeUpdateable
boolean isDeletionTimeUpdateable()
Signals whether the deletion time property can be changed for the kind and current state of the object.
    - setPriority
void setPriority(java.lang.Integer priority)
Sets the priority of the task instance. No special meaning is associated
 with this property. But a caller can, for example, use it
 for sorting a list of tasks.
 
Parameters:priority - The priority of the task instance.
    - isPriorityUpdateable
boolean isPriorityUpdateable()
Signals whether the priority property can be changed for the kind and current state of the object.
    - setType
void setType(java.lang.String type)
Sets the type of the task instance.
 
Parameters:type - The type of the task instance.
    - isTypeUpdateable
boolean isTypeUpdateable()
Signals whether the type property can be changed for the kind and current state of the object.
    - setSupportsDelegation
void setSupportsDelegation(boolean supportsDelegation)
Sets whether the task supports delegation, for example, by transferring work items.
 
Parameters:supportsDelegation - An indication whether the task instance supports delegation. True states
 that the task supports delegation. False states that the task does not
 support delegation.
    - isSupportsDelegationUpdateable
boolean isSupportsDelegationUpdateable()
Signals whether the supports delegation property can be changed for the kind and current state of the object.
    - setSupportsSubTasks
void setSupportsSubTasks(boolean supportsSubTask)
Sets whether the task supports the creation of subtasks.
 
Parameters:supportsSubTask - An indication whether the task instance supports the creation of
 subtasks. True states that the task supports the creation
 of subtasks. False states that the task
 does not support the creation of subtasks.
    - isSupportsSubTasksUpdateable
boolean isSupportsSubTasksUpdateable()
Signals whether the supports sub task property can be changed for the kind and current state of the object.
    - setBusinessRelevance
void setBusinessRelevance(boolean businessRelevance)
Sets whether the task is a business relevant or an "auxiliary" step. A
 business relevant step can, for example, be logged into the audit trail.
 
Parameters:businessRelevance - An indication whether the task instance is business relevant. True
 states that the task is business relevant. False states that the task is
 not business relevant.
    - isBusinessRelevanceUpdateable
boolean isBusinessRelevanceUpdateable()
Signals whether the business relevance property can be changed for the kind and current state of the object.
    - setEventHandlerName
void setEventHandlerName(java.lang.String eventHandlerName)
Sets the name of the associated event handler.
 
Parameters:eventHandlerName - The name of the event handler to be associated.
    - isEventHandlerNameUpdateable
boolean isEventHandlerNameUpdateable()
Signals whether the event handler name property can be changed for the kind and current state of the object.
    - setParentContextID
void setParentContextID(OID parentContextID)
Sets the object ID of the parent context.
 The task must be a stand-alone task and cannot be a subtask or follow-on task.
 
 Changing the parent context has no impact on the task instance itself.
 You may, however, use this property to group tasks for queries. For example,
 a process instance object ID (PIID) can group all stand-alone tasks that
 belong to the specified process instance.
 
Parameters:parentContextID - The object ID of the parent context.
    - isParentContextIDUpdateable
boolean isParentContextIDUpdateable()
Signals whether the parent context ID property can be changed for the kind and current state of the object.
    - setSupportsFollowOnTasks
void setSupportsFollowOnTasks(boolean supportsFollowOnTask)
Sets whether the task supports the creation of follow-on tasks.
 
Parameters:supportsFollowOnTask - An indication whether the task instance supports the creation of
 follow-on tasks. True states that the task supports the creation
 of follow-on tasks. False states that the task
 does not support the creation of follow-on tasks.
    - isSupportsFollowOnTasksUpdateable
boolean isSupportsFollowOnTasksUpdateable()
Signals whether the supports follow on task property can be changed for the kind and current state of the object.
    - setDurationUntilExpires
void setDurationUntilExpires(java.lang.String durationUntilExpires)
Sets the duration that may pass until the task expires.
 The expiration time is calculated once the task reaches the ready state,
 or recalculated when the ready state is already reached or passed.
 
 This value is also used to set up an expiration timer
 when restarting the task instance.
 
Parameters:durationUntilExpires - The duration that may pass until the task instance expires. The format of the
 duration depends on the calendar that is used and may, for example, be "5days".
 Additionally, TimerSpecification.DURATION\_IMMEDIATE
 may be specified to indicate that the task expires immediately
 and TimerSpecification.DURATION\_INFINITE
 to indicate that the task never expires.Since:
7.0.
    - isDurationUntilExpiresUpdateable
boolean isDurationUntilExpiresUpdateable()
Signals whether the duration until expires property can be changed for the kind and current state of the object.
    - setExpirationTime
void setExpirationTime(java.util.Calendar expirationTime)
Sets the time when the task expires. See also
 getExpirationTime.
 
 Note, however, that updating this time prevents a duration until expires to be calculated
 when restarting the task instance. An expiration timer is not set up.
 
Parameters:expirationTime - The time when the task instance expires.
 Note that setting the expiration time to null is not accepted by the update method,
 that is, an exception will be thrown,Since:
7.0.
    - isExpirationTimeUpdateable
boolean isExpirationTimeUpdateable()
Signals whether the expiration time property can be changed for the kind and current state of the object.
    - setEscalated
void setEscalated(boolean isEscalated)
Sets the escalation state of the task, that is, allows to manually escalate a task.
 Refer to isEscalated for reading the current value.
 
Parameters:isEscalated - An indication whether the task instance should be escalated or not. True
 states that the task should be escalated. False states that the task should not be escalated.Since:
7.0.
    - isEscalatedUpdateable
boolean isEscalatedUpdateable()
Signals whether the isEscalated property can be changed for the kind and current state of the object.
    - setRead
void setRead(boolean isRead)
Marks the task instance as read.
 Refer to isRead or
 getTaskRead for reading the current value.
 
Parameters:isRead - An indication whether the task instance should be marked as read or not. True
 states that the task should be marked as read. False states that the task
 should not be marked as read.Since:
7.0.
    - isReadUpdateable
boolean isReadUpdateable()
Signals whether the isRead property can be changed for the kind and current state of the object.
    - setWorkBasketName
void setWorkBasketName(java.lang.String workBasket)
Sets the name of the work basket the task belongs to. The
 isTransferredToWorkBasket
 property remains unchanged.
 Refer to getWorkBasketName for reading the current value.
 
Parameters:workBasket - The name of the work basket to be associated. Null means that the task
 is no longer associated to any work basket.Since:
7.0.
    - isWorkBasketNameUpdateable
boolean isWorkBasketNameUpdateable()
Signals whether the work basket property can be changed for the kind and current state of the object.