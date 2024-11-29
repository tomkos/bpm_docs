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

## Interface TimerBehavior

- public interface TimerBehavior
This interface defines symbolic constants that state how to deal with timers.
 These constants are to be used when an activity instance is repeated - see
 forceRetry as an example.
Since:
7.0

- =========== FIELD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
CONTINUE\_TIMER
Symbolic constant to indicate that the timer period should continue when the activity is retried.

static java.lang.String
COPYRIGHT 

static int
RESET\_TIMER
Symbolic constant to indicate that the timer is to be reset when the activity is retried.

static int
SUPPRESS\_TIMER
Symbolic constant to indicate that the activity should not time out when retried.

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- SUPPRESS\_TIMER
static final int SUPPRESS\_TIMER
Symbolic constant to indicate that the activity should not time out when retried.
See Also:Constant Field Values

- RESET\_TIMER
static final int RESET\_TIMER
Symbolic constant to indicate that the timer is to be reset when the activity is retried.
 Any active timer is cancelled, the timer expression is reevaluated,
 and a new timer is set up.
See Also:Constant Field Values

- CONTINUE\_TIMER
static final int CONTINUE\_TIMER
Symbolic constant to indicate that the timer period should continue when the activity is retried.
 If there is no active timer, the timer expression is evaluated and the
 timer is set up accordingly.
See Also:Constant Field Values