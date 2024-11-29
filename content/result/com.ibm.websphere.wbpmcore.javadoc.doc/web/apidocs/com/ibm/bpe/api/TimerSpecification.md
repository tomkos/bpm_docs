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

## Class TimerSpecification

- java.lang.Object
    - com.ibm.bpe.api.TimerSpecification

- All Implemented Interfaces:
java.io.Serializable

public final class TimerSpecification
extends java.lang.Object
implements java.io.Serializable
Describes options that can be used to set timers.
 For example, you can use this specification when
 rescheduling the expiration time
 of a waiting activity.
Since:
7.0
See Also:Serialized Form

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static TimerSpecification
TIMER\_SPECIFICATION\_IMMEDIATE
An out-of-the-box timer specification that can be used as a timer that is triggered immediately.

static TimerSpecification
TIMER\_SPECIFICATION\_INFINITE
An out-of-the-box timer specification that can be used as a timer that is never triggered.

static int
TYPE\_DEADLINE
Symbolic constant for the type of a timer specification that uses a deadline.

static int
TYPE\_DURATION
Symbolic constant for the type of a timer specification that uses a duration.

static int
TYPE\_IMMEDIATE
Symbolic constant for the type of a timer specification that is triggered immediately.

static int
TYPE\_INFINITE
Symbolic constant for the type of a timer specification that is never triggered,
 that is, no timer is set up.

static int
TYPE\_TIMEOUT
Symbolic constant for the type of a timer specification that uses a timeout.
    - Constructor Summary

Constructors 

Constructor and Description

TimerSpecification()
Default constructor that sets up an infinite time, that is, no timer is set up.

TimerSpecification(java.util.Calendar deadline)
Constructor that uses a deadline as timer specification.

TimerSpecification(java.lang.Integer duration)
Constructor that uses a duration as timer specification.

TimerSpecification(java.lang.String timeoutExpression,
                  java.lang.String calendarName,
                  java.lang.String JNDINameOfCalendar)
Constructor that uses a timeout expression as timer specification.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getCalendarName () Returns the name of the calendar used for the timeout expression. java.util.Calendar getDeadline () Returns the deadline specification. java.lang.Integer getDuration () Returns the duration specification in seconds. java.lang.String getJNDINameOfCalendar () Returns the JNDI name of a user-defined calendar used for the timeout expression. java.lang.String getTimeoutExpression () Returns a calendar specific timeout expression. int getType () Returns the type of the timer specification. java.lang.String toString () Returns a string representation of the TimerSpecification object.

### Method Summary

| Modifier and Type   | Method and Description                                                                                    |
|---------------------|-----------------------------------------------------------------------------------------------------------|
| java.lang.String    | getCalendarName() Returns the name of the calendar used for the timeout expression.                       |
| java.util.Calendar  | getDeadline() Returns the deadline specification.                                                         |
| java.lang.Integer   | getDuration() Returns the duration specification in seconds.                                              |
| java.lang.String    | getJNDINameOfCalendar() Returns the JNDI name of a user-defined calendar used for the timeout expression. |
| java.lang.String    | getTimeoutExpression() Returns a calendar specific timeout expression.                                    |
| int                 | getType() Returns the type of the timer specification.                                                    |
| java.lang.String    | toString() Returns a string representation of the TimerSpecification object.                              |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait