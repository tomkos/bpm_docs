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

## Interface EscalationTemplate

- All Superinterfaces:
java.io.Serializable

public interface EscalationTemplate
extends java.io.Serializable
Accesses the properties of an escalation template.
 
 An escalation template contains the specification of escalations.
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
States that the task is waiting
 for the completion of subtasks.

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
    - Method Summary

Methods 

Modifier and Type
Method and Description

int
getAction()
Returns the action that is executed when an escalation occurs.

int
getActivationState()
Returns the task state that triggers creation of escalations derived from this template.

int
getAtLeastExpectedState()
Returns the state of tasks associated to escalations derived from this template that,
 if not reached when the escalation period runs out,
 trigger escalations.

OID
getContainmentContextID()
Returns the ID of the context the escalation template belongs to.

java.lang.String
getDescription(java.util.Locale arg0)
Returns the description in the specified locale.

java.lang.String
getDisplayName(java.util.Locale arg0)
Returns the display name in the specified locale.

java.lang.String
getDurationUntilEscalated()
Returns the duration until escalations derived from this template are escalated.

java.lang.String
getDurationUntilRepeated()
Returns the duration that is spent until escalations derived from this template are
 repeated.

ESTID
getFirstEscalationTemplateID()
Returns the object ID of the first escalation template in an escalation template chain.

ESTID
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
Returns the name of the escalation template.

ESTID
getNextEscalationTemplateID()
Returns the object ID of the next escalation template in an escalation template chain.

ESTID
getPreviousEscalationTemplateID()
Returns the object ID of the previous escalation template in an escalation template chain.

int
getPriorityIncrease()
States how escalations derived from this template increase
 the priority of associated tasks when they are escalated.

TKTID
getTaskTemplateID()
Returns the object ID of the associated task template.

boolean
isNameUpdateable()
Signals whether the name property can be changed for the kind and current state of the object.

void
setName(java.lang.String name)
For future use.

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
States that the task is waiting
 for the completion of subtasks.
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

- Method Detail

### Method Detail

    - getID
ESTID getID()
Returns the object identifier.
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
Returns the duration until escalations derived from this template are escalated.
 Escalations are escalated when the escalation period times out
 before the associated task reached a certain (at least expected)
 state. If not set, null is returned.
    - getActivationState
int getActivationState()
Returns the task state that triggers creation of escalations derived from this template.
 
 Possible activation states are:
 STATE\_READY and STATE\_CLAIMED for tasks that are to be executed by humans
 and STATE\_RUNNING for tasks that are executed by a machine.
    - getAtLeastExpectedState
int getAtLeastExpectedState()
Returns the state of tasks associated to escalations derived from this template that,
 if not reached when the escalation period runs out,
 trigger escalations.
 
 Possible states are AT\_LEAST\_EXPECTED\_STATE\_CLAIMED,
 AT\_LEAST\_EXPECTED\_STATE\_ENDED, AND AT\_LEAST\_EXPECTED\_STATE\_SUBTASKS\_COMPLETED.
    - getDurationUntilRepeated
java.lang.String getDurationUntilRepeated()
Returns the duration that is spent until escalations derived from this template are
 repeated. Note that escalations are only repeated when the expected
 task state is still not reached. If not set, null is returned.
    - getAction
int getAction()
Returns the action that is executed when an escalation occurs.
 
 Possible actions are ACTION\_CREATE\_WORK\_ITEM, ACTION\_SEND\_EMAIL, and
 ACTION\_CREATE\_EVENT.
    - getPriorityIncrease
int getPriorityIncrease()
States how escalations derived from this template increase
 the priority of associated tasks when they are escalated.
 
 Possible values are INCREASE\_PRIORITY\_NO, INCREASE\_PRIORITY\_ONCE, and INCREASE\_PRIORITY\_REPEATED.
    - getName
java.lang.String getName()
Returns the name of the escalation template.
    - getContainmentContextID
OID getContainmentContextID()
Returns the ID of the context the escalation template belongs to. This ID
 is used for escalation template and instance deletion. In other words, when the context
 is deleted, the escalation template and derived instances are also deleted.
    - getFirstEscalationTemplateID
ESTID getFirstEscalationTemplateID()
Returns the object ID of the first escalation template in an escalation template chain.
    - getPreviousEscalationTemplateID
ESTID getPreviousEscalationTemplateID()
Returns the object ID of the previous escalation template in an escalation template chain.
 Returns null if there is no previous escalation template.
    - getNextEscalationTemplateID
ESTID getNextEscalationTemplateID()
Returns the object ID of the next escalation template in an escalation template chain.
 Returns null if there is no previous escalation template.
    - getTaskTemplateID
TKTID getTaskTemplateID()
Returns the object ID of the associated task template.
    - setName
void setName(java.lang.String name)
For future use.
    - isNameUpdateable
boolean isNameUpdateable()
Signals whether the name property can be changed for the kind and current state of the object.