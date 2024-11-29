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

## Interface StateObserverEvent

- public interface StateObserverEvent
This interface returns observer event specific information as there are the event number
 and the creation time. It defines the observer event numbers.
Since:
6.0 - introduced in 5.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
ACTIVITY\_ALL\_BRANCH\_CONDITIONS\_FALSE
No branch in a switch including (default) has been selected.

static int
ACTIVITY\_BRANCH\_CONDITION\_TRUE
A branch in a switch has been selected.

static int
ACTIVITY\_CHILD\_PROCESS\_TERMINATING
Activity instance event force retry requestecd.

static int
ACTIVITY\_CLAIM\_CANCELED
Activity claim canceled.

static int
ACTIVITY\_CLAIMED
Activity claimed.

static int
ACTIVITY\_COMPLETED
Activity completed successfully.

static int
ACTIVITY\_CONDITION\_FORCED
Activity instance force join condition requested.

static int
ACTIVITY\_CUSTOMPROPERTY\_SET
The custom property of an activity instance has been changed.

static int
ACTIVITY\_ESCALATED
A human task activity (staff activity) is escalated.

static int
ACTIVITY\_EXPIRED
Activity expired.

static int
ACTIVITY\_FAILED
Activity failed.

static int
ACTIVITY\_FAILING
Activity failing.

static int
ACTIVITY\_FAULT\_MESSAGE\_SET
set fault message of an activity.

static int
ACTIVITY\_FOR\_EACH\_COUNTERS\_FORCED
Activity instance force forEach requested.

static int
ACTIVITY\_FORCE\_COMPLETED
Activity instance event force completed

static int
ACTIVITY\_FORCE\_RETRIED
Activity instance event force retried.

static int
ACTIVITY\_JUMPED
Activity instance jumped.

static int
ACTIVITY\_LOOP\_CONDITION\_FALSE
Activity instance event loop condition evaluated to false.

static int
ACTIVITY\_LOOP\_CONDITION\_FORCED
Activity instance force loop condition requested.

static int
ACTIVITY\_LOOP\_CONDITION\_TRUE
Activity instance event loop condition evaluated to true.

static int
ACTIVITY\_MESSAGE\_RECEIVED
Activity instance event message received.

static int
ACTIVITY\_OUTPUT\_MESSAGE\_SET
Set output message of an activity.

static int
ACTIVITY\_PARALLEL\_BRANCHES\_STARTED
Parallel branches for the activity have been started

static int
ACTIVITY\_READY
Activity ready.

static int
ACTIVITY\_RESCHEDULED
Deprecated. 
As of version 7.0, replaced by ACTIVITY\_TIMER\_RESCHEDULED.

static int
ACTIVITY\_RESTARTED\_EXIT\_CONDITION\_FALSE
Activity restarted because the exit condition was evaluated to false.

static int
ACTIVITY\_SKIP\_REQUESTED
Activity instance skip requested.

static int
ACTIVITY\_SKIPPED
Activity skipped.

static int
ACTIVITY\_SKIPPED\_ON\_EXIT\_CONDITION
Activity instance event exit condition evaluated.

static int
ACTIVITY\_SKIPPED\_ON\_REQUEST
Activity instance skipped on request.

static int
ACTIVITY\_STARTED
Activity started.

static int
ACTIVITY\_STOPPED
Activity stopped.

static int
ACTIVITY\_TERMINATED
Activity terminated because of an error occured in a perceding activity.

static int
ACTIVITY\_TERMINATING 

static int
ACTIVITY\_TIMER\_RESCHEDULED
Activity instance event activity timer rescheduled.

static int
ACTIVITY\_USERINPUT\_SET
Set user input of an activity.

static int
ACTIVITY\_WORKITEM\_CREATED
Activity instance event work item transferred.

static int
ACTIVITY\_WORKITEM\_DELETED
Activity instance event work item transferred.

static int
ACTIVITY\_WORKITEM\_REFRESHED
The work items for the activity instance are refreshed.

static int
ACTIVITY\_WORKITEM\_TRANSFERRED
The work item of an activity has been transferred.

static int
CONTROL\_LINK\_EVALUATED\_TO\_FALSE
Control link evaluated to false.

static int
CONTROL\_LINK\_EVALUATED\_TO\_TRUE
Control link evaluated to true.

static java.lang.String
COPYRIGHT 

static int
LINK\_EVALUATED\_TO\_FALSE
Link evaluated to false.

static int
LINK\_EVALUATED\_TO\_TRUE
Link evaluated to true.

static int
PROCESS\_COMPENSATED
Process compensated.

static int
PROCESS\_COMPENSATING
Process compensating.

static int
PROCESS\_COMPENSATION\_FAILED
Process compensation failed

static int
PROCESS\_COMPLETED
Process successfully completed.

static int
PROCESS\_CORRELATION\_SET\_INITIALIZED
Process instance event: correlation set initialized.

static int
PROCESS\_CORRELATION\_SET\_SET
Process instance event: correlation set set.

static int
PROCESS\_CORRELATION\_SET\_UNSET
Process instance event: correlation set deleted.

static int
PROCESS\_CUSTOMPROPERTY\_SET
The custom property of a process instance has been changed.

static int
PROCESS\_DELETED
Process successfully deleted.

static int
PROCESS\_EVENT\_ESCALATED
The oTask associated with the event handler of a process is escalated.

static int
PROCESS\_EVENT\_RECEIVED
Process event handler has received an event.

static int
PROCESS\_FAILED
Process failed.

static int
PROCESS\_FAILING
Process failing.

static int
PROCESS\_INSTALLED
Process template installed
 no related MQWF event.

static int
PROCESS\_MIGRATED
Process instance event: process migrated.

static int
PROCESS\_MIGRATION\_TRIGGERED
Process instance event: process migrated.

static int
PROCESS\_OWNER\_TRANSFERRED
Process instance event owner transferred

static int
PROCESS\_PA\_CHANGED
Partner link on process level was changed

static int
PROCESS\_RESTARTED
Process successfully restarted.

static int
PROCESS\_RESUMED
Process resumed.

static int
PROCESS\_STARTED
Process Started.

static int
PROCESS\_SUSPENDED
Process suspended.

static int
PROCESS\_TERMINATED
Process terminated.

static int
PROCESS\_TERMINATING
Process terminating.

static int
PROCESS\_UNINSTALLED
Process template uninstalled.

static int
PROCESS\_WORKITEM\_CREATED
Activity instance event work item transferred.

static int
PROCESS\_WORKITEM\_DELETED
Activity instance event work item transferred.

static int
PROCESS\_WORKITEM\_TRANSFERRED
The work item of an process has been transferred.

static int
SCOPE\_COMPENSATED
Scope instance compensated event.

static int
SCOPE\_COMPENSATING
Scope instance compensating event.

static int
SCOPE\_COMPENSATION\_FAILED
Scope instance compensation failed event.

static int
SCOPE\_COMPLETED
Scope instance completed event.

static int
SCOPE\_CONDITION\_FORCED
Scope instance force join condition requested.

static int
SCOPE\_EVENT\_ESCALATED
The oTask associated with the event handler of a scop is escalated.

static int
SCOPE\_EVENT\_RECEIVED
The event handler of a sope has received an event.

static int
SCOPE\_FAILED
Scope instance failed event.

static int
SCOPE\_FAILING
Scope instance failing event.

static int
SCOPE\_FORCE\_COMPLETED
Scope instance event force completed

static int
SCOPE\_FORCE\_RETRIED
Scope instance event force retried.

static int
SCOPE\_SKIPPED
Scope instance skipped event.

static int
SCOPE\_STARTED
Scope instance started event.

static int
SCOPE\_STOPPED
Scope instance stopped event.

static int
SCOPE\_TERMINATED
Scope instance terminated event.

static int
VARIABLE\_UPDATED
Variable updated.
    - Method Summary

Methods 

Modifier and Type
Method and Description

long
getCreationTimeInUTC() 

int
getObserverEvent()

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- PROCESS\_STARTED
static final int PROCESS\_STARTED
Process Started.
 Related to MQWF audit event : Process started 21000
See Also:Constant Field Values

- PROCESS\_SUSPENDED
static final int PROCESS\_SUSPENDED
Process suspended.
 related to MQWF event 21001
See Also:Constant Field Values

- PROCESS\_RESUMED
static final int PROCESS\_RESUMED
Process resumed.
  related to MQWF event 21002
See Also:Constant Field Values

- PROCESS\_COMPLETED
static final int PROCESS\_COMPLETED
Process successfully completed.
 Related with MQWF Audit Event : Process completed 21004
See Also:Constant Field Values

- PROCESS\_TERMINATED
static final int PROCESS\_TERMINATED
Process terminated.
  related to MQWF event 21005
See Also:Constant Field Values

- ACTIVITY\_READY
static final int ACTIVITY\_READY
Activity ready.
  Related with MQWF Audit Event : Activity ready, 21006
See Also:Constant Field Values

- ACTIVITY\_STARTED
static final int ACTIVITY\_STARTED
Activity started.
  Related with MQWF Audit Event : Activity started, 21007
See Also:Constant Field Values

- ACTIVITY\_COMPLETED
static final int ACTIVITY\_COMPLETED
Activity completed successfully.
  Related with MQWF audit event: Activity Completed 21011
See Also:Constant Field Values

- PROCESS\_RESTARTED
static final int PROCESS\_RESTARTED
Process successfully restarted.
 Related with MQWF Audit Event : Process deleted 21019
See Also:Constant Field Values

- PROCESS\_DELETED
static final int PROCESS\_DELETED
Process successfully deleted.
 Related with MQWF Audit Event : Process deleted 21020
See Also:Constant Field Values

- ACTIVITY\_CLAIM\_CANCELED
static final int ACTIVITY\_CLAIM\_CANCELED
Activity claim canceled.
  Related with MQWF Audit Event : Cancel check out activity, 21021
See Also:Constant Field Values

- ACTIVITY\_CLAIMED
static final int ACTIVITY\_CLAIMED
Activity claimed.
  Related with MQWF Audit Event : Check out activity, 21022
See Also:Constant Field Values

- ACTIVITY\_TERMINATED
static final int ACTIVITY\_TERMINATED
Activity terminated because of an error occured in a perceding activity.
  Related with MQWF Audit Event : Activity terminated 21027
See Also:Constant Field Values

- CONTROL\_LINK\_EVALUATED\_TO\_TRUE
static final int CONTROL\_LINK\_EVALUATED\_TO\_TRUE
Control link evaluated to true.
  Related with MQWF event : Control conector evaluated to true, 21034.
See Also:Constant Field Values

- LINK\_EVALUATED\_TO\_TRUE
static final int LINK\_EVALUATED\_TO\_TRUE
Link evaluated to true.
See Also:Constant Field Values

- ACTIVITY\_RESTARTED\_EXIT\_CONDITION\_FALSE
static final int ACTIVITY\_RESTARTED\_EXIT\_CONDITION\_FALSE
Activity restarted because the exit condition was evaluated to false.
  See MQWF Audit Event : Activity automatically restarted as exit condition evaluated to false
See Also:Constant Field Values

- ACTIVITY\_FAILED
static final int ACTIVITY\_FAILED
Activity failed.
  Related with MQWF Audit Event : Activity set in Error 21080
See Also:Constant Field Values

- ACTIVITY\_EXPIRED
static final int ACTIVITY\_EXPIRED
Activity expired.
  Related with MQWF Audit Event : Activity expired 21081
See Also:Constant Field Values

- VARIABLE\_UPDATED
static final int VARIABLE\_UPDATED
Variable updated.
 related with MQWF event 21090
See Also:Constant Field Values

- CONTROL\_LINK\_EVALUATED\_TO\_FALSE
static final int CONTROL\_LINK\_EVALUATED\_TO\_FALSE
Control link evaluated to false.
  No related MQWF event!
See Also:Constant Field Values

- LINK\_EVALUATED\_TO\_FALSE
static final int LINK\_EVALUATED\_TO\_FALSE
Link evaluated to false.
See Also:Constant Field Values

- PROCESS\_FAILED
static final int PROCESS\_FAILED
Process failed.
  No related MQWF event!
See Also:Constant Field Values

- PROCESS\_COMPENSATING
static final int PROCESS\_COMPENSATING
Process compensating.
 no related MQWF event.
See Also:Constant Field Values

- PROCESS\_COMPENSATED
static final int PROCESS\_COMPENSATED
Process compensated.
 no related MQWF event.
See Also:Constant Field Values

- ACTIVITY\_SKIPPED
static final int ACTIVITY\_SKIPPED
Activity skipped.
 no related MQWF event.
See Also:Constant Field Values

- PROCESS\_INSTALLED
static final int PROCESS\_INSTALLED
Process template installed
 no related MQWF event.
See Also:Constant Field Values

- PROCESS\_UNINSTALLED
static final int PROCESS\_UNINSTALLED
Process template uninstalled.
 no related MQWF event.
See Also:Constant Field Values

- ACTIVITY\_TERMINATING
static final int ACTIVITY\_TERMINATING
See Also:Constant Field Values

- PROCESS\_TERMINATING
static final int PROCESS\_TERMINATING
Process terminating.
 no related MQWF event.
See Also:Constant Field Values

- PROCESS\_FAILING
static final int PROCESS\_FAILING
Process failing.
 no related MQWF event.
See Also:Constant Field Values

- ACTIVITY\_FAILING
static final int ACTIVITY\_FAILING
Activity failing.
 no related MQWF event.
See Also:Constant Field Values

- ACTIVITY\_OUTPUT\_MESSAGE\_SET
static final int ACTIVITY\_OUTPUT\_MESSAGE\_SET
Set output message of an activity.
See Also:Constant Field Values

- ACTIVITY\_FAULT\_MESSAGE\_SET
static final int ACTIVITY\_FAULT\_MESSAGE\_SET
set fault message of an activity.
See Also:Constant Field Values

- ACTIVITY\_USERINPUT\_SET
static final int ACTIVITY\_USERINPUT\_SET
Set user input of an activity.
See Also:Constant Field Values

- ACTIVITY\_STOPPED
static final int ACTIVITY\_STOPPED
Activity stopped.
 no related MQWF event.
See Also:Constant Field Values

- SCOPE\_STARTED
static final int SCOPE\_STARTED
Scope instance started event.
See Also:Constant Field Values

- SCOPE\_SKIPPED
static final int SCOPE\_SKIPPED
Scope instance skipped event.
See Also:Constant Field Values

- SCOPE\_FAILED
static final int SCOPE\_FAILED
Scope instance failed event.
See Also:Constant Field Values

- SCOPE\_FAILING
static final int SCOPE\_FAILING
Scope instance failing event.
See Also:Constant Field Values

- SCOPE\_TERMINATED
static final int SCOPE\_TERMINATED
Scope instance terminated event.
See Also:Constant Field Values

- SCOPE\_COMPLETED
static final int SCOPE\_COMPLETED
Scope instance completed event.
See Also:Constant Field Values

- PROCESS\_CORRELATION\_SET\_INITIALIZED
static final int PROCESS\_CORRELATION\_SET\_INITIALIZED
Process instance event: correlation set initialized.
See Also:Constant Field Values

- ACTIVITY\_FORCE\_RETRIED
static final int ACTIVITY\_FORCE\_RETRIED
Activity instance event force retried.
See Also:Constant Field Values

- ACTIVITY\_FORCE\_COMPLETED
static final int ACTIVITY\_FORCE\_COMPLETED
Activity instance event force completed
See Also:Constant Field Values

- ACTIVITY\_MESSAGE\_RECEIVED
static final int ACTIVITY\_MESSAGE\_RECEIVED
Activity instance event message received.
See Also:Constant Field Values

- ACTIVITY\_LOOP\_CONDITION\_TRUE
static final int ACTIVITY\_LOOP\_CONDITION\_TRUE
Activity instance event loop condition evaluated to true.
See Also:Constant Field Values

- ACTIVITY\_LOOP\_CONDITION\_FALSE
static final int ACTIVITY\_LOOP\_CONDITION\_FALSE
Activity instance event loop condition evaluated to false.
See Also:Constant Field Values

- ACTIVITY\_WORKITEM\_DELETED
static final int ACTIVITY\_WORKITEM\_DELETED
Activity instance event work item transferred.
See Also:Constant Field Values

- ACTIVITY\_WORKITEM\_CREATED
static final int ACTIVITY\_WORKITEM\_CREATED
Activity instance event work item transferred.
See Also:Constant Field Values

- PROCESS\_WORKITEM\_DELETED
static final int PROCESS\_WORKITEM\_DELETED
Activity instance event work item transferred.
See Also:Constant Field Values

- PROCESS\_WORKITEM\_CREATED
static final int PROCESS\_WORKITEM\_CREATED
Activity instance event work item transferred.
See Also:Constant Field Values

- SCOPE\_COMPENSATING
static final int SCOPE\_COMPENSATING
Scope instance compensating event.
See Also:Constant Field Values

- SCOPE\_COMPENSATED
static final int SCOPE\_COMPENSATED
Scope instance compensated event.
See Also:Constant Field Values

- SCOPE\_COMPENSATION\_FAILED
static final int SCOPE\_COMPENSATION\_FAILED
Scope instance compensation failed event.
See Also:Constant Field Values

- PROCESS\_COMPENSATION\_FAILED
static final int PROCESS\_COMPENSATION\_FAILED
Process compensation failed
See Also:Constant Field Values

- PROCESS\_EVENT\_RECEIVED
static final int PROCESS\_EVENT\_RECEIVED
Process event handler has received an event.
See Also:Constant Field Values

- SCOPE\_EVENT\_RECEIVED
static final int SCOPE\_EVENT\_RECEIVED
The event handler of a sope has received an event.
See Also:Constant Field Values

- PROCESS\_EVENT\_ESCALATED
static final int PROCESS\_EVENT\_ESCALATED
The oTask associated with the event handler of a process is escalated.
See Also:Constant Field Values

- ACTIVITY\_ESCALATED
static final int ACTIVITY\_ESCALATED
A human task activity (staff activity) is escalated.
See Also:Constant Field Values

- SCOPE\_EVENT\_ESCALATED
static final int SCOPE\_EVENT\_ESCALATED
The oTask associated with the event handler of a scop is escalated.
See Also:Constant Field Values

- ACTIVITY\_WORKITEM\_REFRESHED
static final int ACTIVITY\_WORKITEM\_REFRESHED
The work items for the activity instance are refreshed.
See Also:Constant Field Values

- ACTIVITY\_WORKITEM\_TRANSFERRED
static final int ACTIVITY\_WORKITEM\_TRANSFERRED
The work item of an activity has been transferred.
See Also:Constant Field Values

- PROCESS\_WORKITEM\_TRANSFERRED
static final int PROCESS\_WORKITEM\_TRANSFERRED
The work item of an process has been transferred.
See Also:Constant Field Values

- ACTIVITY\_PARALLEL\_BRANCHES\_STARTED
static final int ACTIVITY\_PARALLEL\_BRANCHES\_STARTED
Parallel branches for the activity have been started
See Also:Constant Field Values

- PROCESS\_PA\_CHANGED
static final int PROCESS\_PA\_CHANGED
Partner link on process level was changed
Since:
6.1
See Also:Constant Field Values

- PROCESS\_CUSTOMPROPERTY\_SET
static final int PROCESS\_CUSTOMPROPERTY\_SET
The custom property of a process instance has been changed.
See Also:Constant Field Values

- ACTIVITY\_CUSTOMPROPERTY\_SET
static final int ACTIVITY\_CUSTOMPROPERTY\_SET
The custom property of an activity instance has been changed.
See Also:Constant Field Values

- ACTIVITY\_BRANCH\_CONDITION\_TRUE
static final int ACTIVITY\_BRANCH\_CONDITION\_TRUE
A branch in a switch has been selected.
See Also:Constant Field Values

- ACTIVITY\_ALL\_BRANCH\_CONDITIONS\_FALSE
static final int ACTIVITY\_ALL\_BRANCH\_CONDITIONS\_FALSE
No branch in a switch including (default) has been selected.
See Also:Constant Field Values

- ACTIVITY\_JUMPED
static final int ACTIVITY\_JUMPED
Activity instance jumped.
See Also:Constant Field Values

- ACTIVITY\_SKIP\_REQUESTED
static final int ACTIVITY\_SKIP\_REQUESTED
Activity instance skip requested.
See Also:Constant Field Values

- ACTIVITY\_SKIPPED\_ON\_REQUEST
static final int ACTIVITY\_SKIPPED\_ON\_REQUEST
Activity instance skipped on request.
See Also:Constant Field Values

- SCOPE\_STOPPED
static final int SCOPE\_STOPPED
Scope instance stopped event.
See Also:Constant Field Values

- SCOPE\_FORCE\_COMPLETED
static final int SCOPE\_FORCE\_COMPLETED
Scope instance event force completed
See Also:Constant Field Values

- SCOPE\_FORCE\_RETRIED
static final int SCOPE\_FORCE\_RETRIED
Scope instance event force retried.
See Also:Constant Field Values

- ACTIVITY\_RESCHEDULED
static final int ACTIVITY\_RESCHEDULED
Deprecated. As of version 7.0, replaced by ACTIVITY\_TIMER\_RESCHEDULED.
Activity instance event activity rescheduled.
See Also:Constant Field Values

- ACTIVITY\_TIMER\_RESCHEDULED
static final int ACTIVITY\_TIMER\_RESCHEDULED
Activity instance event activity timer rescheduled.
See Also:Constant Field Values

- ACTIVITY\_SKIPPED\_ON\_EXIT\_CONDITION
static final int ACTIVITY\_SKIPPED\_ON\_EXIT\_CONDITION
Activity instance event exit condition evaluated.
See Also:Constant Field Values

- PROCESS\_OWNER\_TRANSFERRED
static final int PROCESS\_OWNER\_TRANSFERRED
Process instance event owner transferred
See Also:Constant Field Values

- ACTIVITY\_CHILD\_PROCESS\_TERMINATING
static final int ACTIVITY\_CHILD\_PROCESS\_TERMINATING
Activity instance event force retry requestecd.
See Also:Constant Field Values

- ACTIVITY\_CONDITION\_FORCED
static final int ACTIVITY\_CONDITION\_FORCED
Activity instance force join condition requested.
See Also:Constant Field Values

- ACTIVITY\_LOOP\_CONDITION\_FORCED
static final int ACTIVITY\_LOOP\_CONDITION\_FORCED
Activity instance force loop condition requested.
See Also:Constant Field Values

- ACTIVITY\_FOR\_EACH\_COUNTERS\_FORCED
static final int ACTIVITY\_FOR\_EACH\_COUNTERS\_FORCED
Activity instance force forEach requested.
See Also:Constant Field Values

- SCOPE\_CONDITION\_FORCED
static final int SCOPE\_CONDITION\_FORCED
Scope instance force join condition requested.
See Also:Constant Field Values

- PROCESS\_CORRELATION\_SET\_SET
static final int PROCESS\_CORRELATION\_SET\_SET
Process instance event: correlation set set.
See Also:Constant Field Values

- PROCESS\_CORRELATION\_SET\_UNSET
static final int PROCESS\_CORRELATION\_SET\_UNSET
Process instance event: correlation set deleted.
See Also:Constant Field Values

- PROCESS\_MIGRATED
static final int PROCESS\_MIGRATED
Process instance event: process migrated.
See Also:Constant Field Values

- PROCESS\_MIGRATION\_TRIGGERED
static final int PROCESS\_MIGRATION\_TRIGGERED
Process instance event: process migrated.
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getObserverEvent
int getObserverEvent()
Returns:The event number of this event.
    - getCreationTimeInUTC
long getCreationTimeInUTC()
Returns:The time the event has been created in Millis.