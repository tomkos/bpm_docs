<!-- image -->

# Continue-on-error behavior of BPEL processes and activities

For most activities, the continue-on-error behavior is the same
as for the process. You can specify the continue-on-error behavior
explicitly for invoke, Java snippet, custom, and human task activities.
By default, the continue-on-error behavior of these activities is
also the same as for the process. If an unexpected fault is detected,
fault handling of the activity is started.

If the Continue processing upon unhandled faults setting is set to Yes, then the standard
fault handling is applied. If the Continue processing upon
unhandled faults setting for the activity or the process
is set to No and the fault is not handled by
a fault handler on the immediately enclosing scope or by a fault link
leaving this activity, the activity is stopped. If the activity has
an associated fault handler or compensation handler, the immediately
enclosing scope is the activity itself. In all other cases, the immediately
enclosing scope is the next surrounding scope in which the activity
is contained. If a catch-all fault link or fault handler is defined
on the immediately enclosing scope, the value of the Continue
processing upon unhandled faults setting does not have
any effect, because the fault is always handled and the activity is
never stopped.

| Value of the stopReason property        | Cause                                                                                                                                                                                                                                                                                                                                                                                                           | Allowed actions                                                    |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| STOP\_REASON\_ACTIVATION\_FAILED           | The evaluation of the join condition of the activity failed. You can use the force join condition to set the condition to true or false or to reevaluate it.                                                                                                                                                                                                                                                    | Force retry Force the join condition                               |
| STOP\_REASON\_IMPLEMENTATION\_FAILED       | The implementation of the activity threw a fault.                                                                                                                                                                                                                                                                                                                                                               |                                                                    |
| STOP\_REASON\_IMPLEMENTATION\_FAILED       | This value is set if the implementation of the activity failed, for example: A service called by an invoke activity returned a fault that is not handled by a fault handler. A timeout expression failed when a wait activity was activated. The evaluation of an exit condition of an activity failed.                                                                                                         | Force retry Force complete                                         |
| STOP\_REASON\_IMPLEMENTATION\_FAILED       | If the evaluation of a while or repeatUntil condition failed,  the value of the kind property is either KIND\_WHILE or KIND\_REPEAT.                                                                                                                                                                                                                                                                              | Force retry Force complete Force the loop condition                |
| STOP\_REASON\_IMPLEMENTATION\_FAILED       | If the evaluation of a forEach counter or condition failed, the value of the kind property is either KIND\_FOR\_EACH\_SERIAL or KIND\_FOR\_EACH\_PARALLEL.                                                                                                                                                                                                                                                            | Force retry Force complete Force the values of the forEach counter |
| STOP\_REASON\_IMPLEMENTATION\_FAILED       | The evaluation of the branch expression in choice activity (also known as a switch activity) failed.                                                                                                                                                                                                                                                                                                            | Force the navigation of the branch                                 |
| STOP\_REASON\_FOLLOW\_ON\_NAVIGATION\_FAILED | The evaluation of a transition condition of an outgoing link failed. This value is set in one of the following situations:  In a parallel flow (also known as a parallel activities activity), after an activity completed, the transition conditions of the outgoing links were evaluated, and one of them produced a fault. In a cyclic flow, if none of the outgoing links qualify for follow-on navigation. | Force the navigation of the outgoing link Force complete           |
| STOP\_REASON\_EXIT\_CONDITION\_FALSE        | The criteria for the exit condition were not met. This value is set only when the exit condition is evaluated on exit of an activity and the condition evaluates to false.If this error occurs, the activity is always stopped regardless of the Continue On Error setting.                                                                                                                                     | Force retry Force complete                                         |

| Repair action                                          | API method                                  | Action in Business Process Choreographer Explorer   |
|--------------------------------------------------------|---------------------------------------------|-----------------------------------------------------|
| Force retry                                            | forceRetry                                  | Restart                                             |
| Force complete                                         | forceComplete                               | Force Complete                                      |
| Force the join condition                               | forceJoinCondition                          | Repair Join                                         |
| Force the loop condition                               | forceLoopCondition                          | Next Iteration or End Loop                          |
| Force the values of the forEach counter                | forceForEachCounterValues                   | Repair For Each                                     |
| Force the navigation a branch within a choice activity | forceNavigate(...,    int positionOfBranch) | Force Case Navigation or Force Case Execution       |
| Force the navigation of an outgoing link               | forceNavigate(..., ... linksToBeFollowed)   | Force Navigation                                    |
| Force complete and jump                                | forceCompleteAndJump                        | Force Complete Source Activity and Jump             |
| Skip                                                   | skip                                        | Skip or Skip Activity                               |
| Skip and jump                                          | skipAndJump                                 | Skip Source Activity And Jump                       |