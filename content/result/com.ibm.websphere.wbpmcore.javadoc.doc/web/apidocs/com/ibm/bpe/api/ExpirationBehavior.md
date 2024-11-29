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

## Interface ExpirationBehavior

- Deprecated. 
As of version 7.0, replaced by the more generalized TimerBehavior interface.

public interface ExpirationBehavior
This interface defines symbolic constants that state how to deal with expirations.
 These constants are to be used when an activity instance is repeated - see
 forceRetry.
Since:
6.1

- =========== FIELD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
CONTINUE\_EXPIRATION
Deprecated. 
Symbolic constant to indicate that the expiration period should continue when the activity is retried.

static java.lang.String
COPYRIGHT
Deprecated. 
 

static int
RESET\_EXPIRATION
Deprecated. 
Symbolic constant to indicate that the expiration timer is to be reset when the activity is retried.

static int
SUPPRESS\_EXPIRATION
Deprecated. 
Symbolic constant to indicate that the activity should not expire when retried.

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
Deprecated. 
See Also:Constant Field Values

- SUPPRESS\_EXPIRATION
static final int SUPPRESS\_EXPIRATION
Deprecated. 
Symbolic constant to indicate that the activity should not expire when retried.
See Also:Constant Field Values

- RESET\_EXPIRATION
static final int RESET\_EXPIRATION
Deprecated. 
Symbolic constant to indicate that the expiration timer is to be reset when the activity is retried.
 Any active expiration timer is cancelled, the expiration expression is reevaluated,
 and a new expiration timer is set up.
See Also:Constant Field Values

- CONTINUE\_EXPIRATION
static final int CONTINUE\_EXPIRATION
Deprecated. 
Symbolic constant to indicate that the expiration period should continue when the activity is retried.
 If there is no active expiration timer, the expiration expression is evaluated and the
 expiration timer is set up accordingly.
See Also:Constant Field Values