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

## Interface Escalation

- All Superinterfaces:
java.io.Serializable

All Known Implementing Classes:
EscalationBean

public interface Escalation
extends java.io.Serializable
Accesses the properties of an escalation instance.
 
 Escalations are activated at a certain task state and escalate
 when the escalation period times out before the associated task has reached
 an expected state. If escalated, the defined action is performed.
 
Since:
6.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
ACTION\_CREATE\_EVENT
Creates and publishes an event.

static int
ACTION\_CREATE\_WORK\_ITEM
Creates a work item for each escalation receiver.

static int
ACTION\_SEND\_EMAIL
Sends an e-mail to each escalation receiver.

static int
ACTIVATION\_STATE\_CLAIMED
States that the task has been claimed.

static int
ACTIVATION\_STATE\_READY
States that the to-do aka participating task or collaboration aka human task is ready to be claimed

static int
ACTIVATION\_STATE\_RUNNING
States that the invocation aka originating task is started and running

static int
ACTIVATION\_STATE\_WAITING\_FOR\_SUBTASK
States that the task is waiting for the completion of subtasks.

static int
AT\_LEAST\_EXPECTED\_STATE\_CLAIMED
States that the task must have been claimed.

static int
AT\_LEAST\_EXPECTED\_STATE\_ENDED
States that the task must be in a final state (FINISHED, FAILED, TERMINATED, or EXPIRED).

static int
AT\_LEAST\_EXPECTED\_STATE\_SUBTASKS\_COMPLETED
States that all subtasks of the task must be completed.

static java.lang.String
COPYRIGHT 

static int
INCREASE\_PRIORITY\_NO
The task priority will not be increased.

static int
INCREASE\_PRIORITY\_ONCE
The task priority will be increased once by 1.

static int
INCREASE\_PRIORITY\_REPEATED
The task priority will be increased by 1 each time the escalation repeats.

static int
STATE\_ESCALATED
States that the expected task state has not been reached in time.

static int
STATE\_INACTIVE
States that the escalation (timer) has not yet been started.

static int
STATE\_SUPERFLUOUS
States that the expected task state has been reached in time.

static int
STATE\_WAITING
States that the escalation (timer) has been started and waits for timeout.
    - Method Summary

Methods 

Modifier and Type
Method and Description

int
getAction()
Returns the action that is executed when the escalation occurs or that
 is executed when the escalation is repeated.

int
getActivationState()
Returns the task state when this escalation was activated.

java.util.Calendar
getActivationTime()
Returns the time when the escalation instance was activated.

int
getAtLeastExpectedState()
Returns the state of the associated task, that,
 if not reached when the escalation period runs out,
 triggers the escalation of this escalation instance.

OID
getContainmentContextID()
Returns the ID of the context the escalation belongs to.

java.lang.String
getDescription(java.util.Locale arg0)
Returns the description in the specified locale.

java.lang.String
getDisplayName(java.util.Locale arg0)
Returns the display name in the specified locale.

java.lang.String
getDurationUntilEscalated()
Returns the value that is used to calculate the escalation time when the
 activation state is reached - refer to
 getEscalationTime.

java.lang.String
getDurationUntilRepeated()
Returns the value that is used to calculate the next escalation time once the
 task is escalated - refer to
 getEscalationTime.

ESTID
getEscalationTemplateID()
Returns the object ID of the associated escalation template.

java.util.Calendar
getEscalationTime()
Returns the time when the escalation will fire or null when no
 escalation timer is running.

ESIID
getFirstEscalationID()
Returns the object ID of the first escalation in the escalation chain.

ESIID
getID()
Returns the object identifier.

java.util.List
getLocalesOfDescriptions()
Returns the locales of all descriptions.

java.util.List
getLocalesOfDisplayNames()
Returns the locales of all display names.

java.lang.String
getName()
Returns the name of the escalation instance.

ESIID
getNextEscalationID()
Returns the object ID of the next escalation in the escalation chain.

ESIID
getPreviousEscalationID()
Returns the object ID of the previous escalation in the escalation chain.

int
getPriorityIncrease()
States how this escalation increases the priority of the associated task.

int
getState()
Returns the state of the escalation instance.

TKIID
getTaskInstanceID()
Returns the object ID of the associated task instance.

boolean
isDurationUntilEscalatedUpdateable()
Signals whether the duration until escalation property can be changed for the kind and current state of the object.

boolean
isDurationUntilRepeatedUpdateable()
Signals whether the duration until repeats property can be changed for the kind and current state of the object.

boolean
isEscalationTimeUpdateable()
Signals whether the escalation time property can be changed for the kind and current state of the object.

boolean
isNameUpdateable()
Signals whether the name property can be changed for the kind and current state of the object.

void
setDurationUntilEscalated(java.lang.String durationUntilEscalation)
Sets the duration that passes until the escalation fires.

void
setDurationUntilRepeated(java.lang.String durationUntilRepeats)
Sets the duration that passes until the escalation fires next.

void
setEscalationTime(java.util.Calendar escalationTime)
Sets the time when the escalation will fire.

void
setName(java.lang.String name)
Sets the name of the escalation instance.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- ACTIVATION\_STATE\_READY
static final int ACTIVATION\_STATE\_READY
States that the to-do aka participating task or collaboration aka human task is ready to be claimed
See Also:Constant Field Values

- ACTIVATION\_STATE\_RUNNING
static final int ACTIVATION\_STATE\_RUNNING
States that the invocation aka originating task is started and running
See Also:Constant Field Values

- ACTIVATION\_STATE\_WAITING\_FOR\_SUBTASK
static final int ACTIVATION\_STATE\_WAITING\_FOR\_SUBTASK
States that the task is waiting for the completion of subtasks.
 Note: the states (values) must correspond to the values in TaskInstance.
See Also:Constant Field Values

- ACTIVATION\_STATE\_CLAIMED
static final int ACTIVATION\_STATE\_CLAIMED
States that the task has been claimed.
See Also:Constant Field Values

- AT\_LEAST\_EXPECTED\_STATE\_SUBTASKS\_COMPLETED
static final int AT\_LEAST\_EXPECTED\_STATE\_SUBTASKS\_COMPLETED
States that all subtasks of the task must be completed.
See Also:Constant Field Values

- AT\_LEAST\_EXPECTED\_STATE\_CLAIMED
static final int AT\_LEAST\_EXPECTED\_STATE\_CLAIMED
States that the task must have been claimed.
See Also:Constant Field Values

- AT\_LEAST\_EXPECTED\_STATE\_ENDED
static final int AT\_LEAST\_EXPECTED\_STATE\_ENDED
States that the task must be in a final state (FINISHED, FAILED, TERMINATED, or EXPIRED).
See Also:Constant Field Values

- ACTION\_CREATE\_WORK\_ITEM
static final int ACTION\_CREATE\_WORK\_ITEM
Creates a work item for each escalation receiver.
See Also:Constant Field Values

- ACTION\_SEND\_EMAIL
static final int ACTION\_SEND\_EMAIL
Sends an e-mail to each escalation receiver.
See Also:Constant Field Values

- ACTION\_CREATE\_EVENT
static final int ACTION\_CREATE\_EVENT
Creates and publishes an event.
See Also:Constant Field Values

- INCREASE\_PRIORITY\_NO
static final int INCREASE\_PRIORITY\_NO
The task priority will not be increased.
See Also:Constant Field Values

- INCREASE\_PRIORITY\_REPEATED
static final int INCREASE\_PRIORITY\_REPEATED
The task priority will be increased by 1 each time the escalation repeats.
See Also:Constant Field Values

- INCREASE\_PRIORITY\_ONCE
static final int INCREASE\_PRIORITY\_ONCE
The task priority will be increased once by 1.
See Also:Constant Field Values

- STATE\_WAITING
static final int STATE\_WAITING
States that the escalation (timer) has been started and waits for timeout.
See Also:Constant Field Values

- STATE\_INACTIVE
static final int STATE\_INACTIVE
States that the escalation (timer) has not yet been started.
See Also:Constant Field Values

- STATE\_SUPERFLUOUS
static final int STATE\_SUPERFLUOUS
States that the expected task state has been reached in time.
See Also:Constant Field Values

- STATE\_ESCALATED
static final int STATE\_ESCALATED
States that the expected task state has not been reached in time.
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getID
ESIID getID()
Returns the object identifier.
    - getActivationState
int getActivationState()
Returns the task state when this escalation was activated.
 
 Possible activation states are:
 STATE\_READY and STATE\_CLAIMED for tasks that are to be executed by humans
 and STATE\_RUNNING for tasks that are executed by a machine.
    - getActivationTime
java.util.Calendar getActivationTime()
Returns the time when the escalation instance was activated.
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
    - getDurationUntilEscalated
java.lang.String getDurationUntilEscalated()
Returns the value that is used to calculate the escalation time when the
 activation state is reached - refer to
 getEscalationTime.
 
 This property is a WebSphere Application Server calendar expression
 according to the calendar referenced by its name and JNDI name
 on the associated task.
 TimerSpecification.DURATION\_NOT\_USED
 means that the escalation time is set explicitely - see
 setExcalationTime.
 If the duration is not set, null is returned.
 
 To update the duration see the
 setDurationUntilEscalated method.
    - getAtLeastExpectedState
int getAtLeastExpectedState()
Returns the state of the associated task, that,
 if not reached when the escalation period runs out,
 triggers the escalation of this escalation instance.
 
 Possible states are AT\_LEAST\_EXPECTED\_STATE\_CLAIMED,
 AT\_LEAST\_EXPECTED\_STATE\_ENDED, AND AT\_LEAST\_EXPECTED\_STATE\_SUBTASKS\_COMPLETED.
    - getDurationUntilRepeated
java.lang.String getDurationUntilRepeated()
Returns the value that is used to calculate the next escalation time once the
 task is escalated - refer to
 getEscalationTime.
 
 This property is a WebSphere Application Server calendar expression
 according to the calendar referenced by its name and JNDI name
 on the associated task.
 If the duration is not set, null is returned.
 
 To update the duration see the
 setDurationUntilRepeated method.
    - getAction
int getAction()
Returns the action that is executed when the escalation occurs or that
 is executed when the escalation is repeated.
 
 Possible actions are ACTION\_CREATE\_WORK\_ITEM, ACTION\_SEND\_EMAIL, and
 ACTION\_CREATE\_EVENT.
    - getPriorityIncrease
int getPriorityIncrease()
States how this escalation increases the priority of the associated task.
 
 Possible values are INCREASE\_PRIORITY\_NO, INCREASE\_PRIORITY\_ONCE, and INCREASE\_PRIORITY\_REPEATED.
    - getName
java.lang.String getName()
Returns the name of the escalation instance.
    - getContainmentContextID
OID getContainmentContextID()
Returns the ID of the context the escalation belongs to. This ID
 is used for escalation instance deletion. In other words, when the context
 is deleted, the escalation instance is also deleted.
    - getFirstEscalationID
ESIID getFirstEscalationID()
Returns the object ID of the first escalation in the escalation chain.
    - getPreviousEscalationID
ESIID getPreviousEscalationID()
Returns the object ID of the previous escalation in the escalation chain.
 Returns null if there is no previous escalation.
    - getNextEscalationID
ESIID getNextEscalationID()
Returns the object ID of the next escalation in the escalation chain.
 Returns null if there is no following escalation.
    - getEscalationTemplateID
ESTID getEscalationTemplateID()
Returns the object ID of the associated escalation template. Returns null
 if there is no associated escalation template.
    - getTaskInstanceID
TKIID getTaskInstanceID()
Returns the object ID of the associated task instance.
    - getState
int getState()
Returns the state of the escalation instance.
 
 Returns either STATE\_INACTIVE, STATE\_WAITING, STATE\_ESCALATED,
 STATE\_SUPERFLUOUS.
    - getEscalationTime
java.util.Calendar getEscalationTime()
Returns the time when the escalation will fire or null when no
 escalation timer is running.
 
 Escalations are fired when the escalation period times out
 before the associated task reached a certain (at least expected)
 state.
Since:
7.0.
    - setName
void setName(java.lang.String name)
Sets the name of the escalation instance.
 
Parameters:name - The new name of the escalation instance.Since:
7.0.
    - isNameUpdateable
boolean isNameUpdateable()
Signals whether the name property can be changed for the kind and current state of the object.
    - setEscalationTime
void setEscalationTime(java.util.Calendar escalationTime)
Sets the time when the escalation will fire.
 If the escalation is in state WAITING, the existing timer is canceled
 and a new one is created. The duration until escalated is set to
 TimerSpecification.DURATION\_NOT\_USED.
 - see getDurationUntilEscalated.
 
 If the escalation is in state ESCALATED, the current repetition timer
 is canceled and a new one is created. The duration until repeated remains unchanged.
 
Parameters:escalationTime - The time when the escalation instance will fire.
 Note that setting the escalation time to null is not accepted by the update method,
 that is, an exception will be thrown,Since:
7.0.
    - isEscalationTimeUpdateable
boolean isEscalationTimeUpdateable()
Signals whether the escalation time property can be changed for the kind and current state of the object.
    - setDurationUntilEscalated
void setDurationUntilEscalated(java.lang.String durationUntilEscalation)
Sets the duration that passes until the escalation fires.
 If the escalation is in state INACTIVE, this value is used to calculate the
 escalation time once the associated task reaches state WAITING.
 If the escalation is in state WAITING, the current timer is canceled and a new
 timer is set up according to the passed value.
 
 This property is a WebSphere Application Server calendar expression
 according to the calendar referenced by its name and JNDI name
 on the associated task.
 
Parameters:durationUntilEscalation - The duration that should pass until the escalation instance fires.
 Note that setting the duration to
 TimerSpecification.DURATION\_IMMEDIATE
 is not accepted by the update method, that is, an exception will be thrown,Since:
7.0.
    - isDurationUntilEscalatedUpdateable
boolean isDurationUntilEscalatedUpdateable()
Signals whether the duration until escalation property can be changed for the kind and current state of the object.
    - setDurationUntilRepeated
void setDurationUntilRepeated(java.lang.String durationUntilRepeats)
Sets the duration that passes until the escalation fires next.
 If the escalation is in state INACTIVE or WAITING, this value is used to
 calculate the escalation time once the associated task reaches state ESCALATED.
 If the escalation is in state ESCALATED, the current timer is canceled and
 a new one is set up according to the passed value.
 If TimerSpecification.DURATION\_INFINITE
 is specified and the escalation is escalated, the escalation will not repeat.
 If TimerSpecification.DURATION\_IMMEDIATE
 is specified and the escalation is escalated, the
 escalation will repeat immediately.
 
 This property is a WebSphere Application Server calendar expression
 according to the calendar referenced by its name and JNDI name
 on the associated task.
 
Parameters:durationUntilRepeats - The duration that should pass until the escalation instance fires next.Since:
7.0.
    - isDurationUntilRepeatedUpdateable
boolean isDurationUntilRepeatedUpdateable()
Signals whether the duration until repeats property can be changed for the kind and current state of the object.