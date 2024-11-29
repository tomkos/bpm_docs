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

## Interface TimerSpecification

- public interface TimerSpecification
This interface defines symbolic constants that state how to deal with timers.
 These constants should be used when durations are updated and when no explicit duration is specified - see
 setDurationUntilDue as an example.
Since:
7.0

- =========== FIELD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static java.lang.String
DURATION\_IMMEDIATE
Symbolic constant for an immediate timer setup, that is, a duration of zero.

static java.lang.String
DURATION\_INFINITE
Symbolic constant for an infinite timer setup, that is, no timer is set up.

static java.lang.String
DURATION\_NOT\_USED
Symbolic constant to indicate that a duration is not used to set up a timer.

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- DURATION\_NOT\_USED
static final java.lang.String DURATION\_NOT\_USED
Symbolic constant to indicate that a duration is not used to set up a timer.
See Also:Constant Field Values

- DURATION\_IMMEDIATE
static final java.lang.String DURATION\_IMMEDIATE
Symbolic constant for an immediate timer setup, that is, a duration of zero.
See Also:Constant Field Values

- DURATION\_INFINITE
static final java.lang.String DURATION\_INFINITE
Symbolic constant for an infinite timer setup, that is, no timer is set up.
See Also:Constant Field Values