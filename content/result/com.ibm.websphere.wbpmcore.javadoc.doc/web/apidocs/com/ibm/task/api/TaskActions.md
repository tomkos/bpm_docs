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

## Interface TaskActions

- public interface TaskActions
This interface defines symbolic constants for all actions that can be performed on
 task instances. These constants are to be used when determining the actions
 allowed in the current task instance state.
 Currently allowed actions are returned
 when calling the getAvailableActions()
 or getAvailableActionFlags()
 methods for a task instance.
Since:
7.0 - introduced in 5.1

- =========== FIELD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
CALLTASK
Symbolic constant for task instance action call task.

static int
CANCELCLAIM
Symbolic constant for task instance action cancel claim.

static int
CLAIM
Symbolic constant for task instance action claim.

static int
COMPLETE
Symbolic constant for task instance action complete.

static int
COMPLETEWITHFOLLOWONTASK
Symbolic constant for task instance action complete the current
 task and start a previously created task as follow-on task.

static java.lang.String
COPYRIGHT 

static int
CREATEFAULTMESSAGE
Symbolic constant for task instance action create fault message.

static int
CREATEINPUTMESSAGE
Symbolic constant for task instance action create input message.

static int
CREATEMESSAGE
Deprecated. 
Use CREATEINPUTMESSAGE, CREATEOUTPUTMESSAGE, CREATEFAULTMESSAGE.

static int
CREATEOUTPUTMESSAGE
Symbolic constant for task instance action create output message.

static int
CREATEWORKITEM
Symbolic constant for task instance action create work item.

static int
DELETE
Symbolic constant for task instance action delete task.

static int
DELETEWORKITEM
Symbolic constant for task instance action delete work item.

static int
GETCUSTOMPROPERTY
Symbolic constant for task instance action get custom property.

static int
GETDOCUMENTATION
Symbolic constant for task instance action get documentation.

static int
GETFAULTMESSAGE
Symbolic constant for task instance action get fault message.

static int
GETFAULTNAMES
Symbolic constant for task instance action get fault names.

static int
GETINPUTMESSAGE
Symbolic constant for task instance action get input message.

static int
GETOUTPUTMESSAGE
Symbolic constant for task instance action get output message.

static int
GETROLEINFO
Symbolic constant for task instance action to retrieve role related information.

static int
GETTASK
Symbolic constant for task instance action get task.

static int
GETTASKINSTANCE
Deprecated. 
Use GETTASK.

static int
GETUISETTINGS
Symbolic constant for task instance action get UI settings.

static int
RESTARTTASK
Symbolic constant for task instance action restart task.

static int
RESUME
Symbolic constant for task instance action resume task.

static int
SETCUSTOMPROPERTY
Symbolic constant for task instance action set custom properties.

static int
SETFAULTMESSAGE
Symbolic constant for task instance action set fault message.

static int
SETINPUTMESSAGE
Symbolic constant for task instance action set input message.

static int
SETOUTPUTMESSAGE
Symbolic constant for task instance action set output message.

static int
SETTASKREAD
Symbolic constant for task instance action set task read.

static int
STARTTASK
Symbolic constant for task instance action start task.

static int
STARTTASKASSUBTASK
Symbolic constant for task instance action start task as subtask.

static int
SUSPEND
Symbolic constant for task instance action suspend task.

static int
SUSPENDWITHCANCELCLAIM
Symbolic constant for task instance action suspend task and later cancelClaim.

static int
TERMINATE
Symbolic constant for task instance action terminate task.

static int
TRANSFERTOWORKBASKET
Symbolic constant for task instance action transfer to work basket.

static int
TRANSFERWORKITEM
Symbolic constant for task instance action transfer work item.

static int
UPDATE
Symbolic constant for task instance action update task.

static int
UPDATEINACTIVETASK
Symbolic constant for task instance action update inactive task.

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- CLAIM
static final int CLAIM
Symbolic constant for task instance action claim.
Since:
5.1
See Also:Constant Field Values

- COMPLETE
static final int COMPLETE
Symbolic constant for task instance action complete.
Since:
5.1
See Also:Constant Field Values

- CANCELCLAIM
static final int CANCELCLAIM
Symbolic constant for task instance action cancel claim.
Since:
5.1
See Also:Constant Field Values

- SETOUTPUTMESSAGE
static final int SETOUTPUTMESSAGE
Symbolic constant for task instance action set output message.
Since:
5.1
See Also:Constant Field Values

- SETCUSTOMPROPERTY
static final int SETCUSTOMPROPERTY
Symbolic constant for task instance action set custom properties.
Since:
5.1
See Also:Constant Field Values

- GETOUTPUTMESSAGE
static final int GETOUTPUTMESSAGE
Symbolic constant for task instance action get output message.
Since:
5.1
See Also:Constant Field Values

- GETINPUTMESSAGE
static final int GETINPUTMESSAGE
Symbolic constant for task instance action get input message.
Since:
5.1
See Also:Constant Field Values

- GETFAULTMESSAGE
static final int GETFAULTMESSAGE
Symbolic constant for task instance action get fault message.
Since:
5.1
See Also:Constant Field Values

- GETCUSTOMPROPERTY
static final int GETCUSTOMPROPERTY
Symbolic constant for task instance action get custom property.
 Includes getCustomPropertyNames() and getCustomProperties().
Since:
5.1
See Also:Constant Field Values

- GETTASKINSTANCE
static final int GETTASKINSTANCE
Deprecated. Use GETTASK.
Symbolic constant for task instance action get task instance.
Since:
5.1
See Also:Constant Field Values

- GETUISETTINGS
static final int GETUISETTINGS
Symbolic constant for task instance action get UI settings.
Since:
5.1
See Also:Constant Field Values

- SETFAULTMESSAGE
static final int SETFAULTMESSAGE
Symbolic constant for task instance action set fault message.
Since:
5.1
See Also:Constant Field Values

- CREATEMESSAGE
static final int CREATEMESSAGE
Deprecated. Use CREATEINPUTMESSAGE, CREATEOUTPUTMESSAGE, CREATEFAULTMESSAGE.
Symbolic constant for task instance action create message.
Since:
5.1
See Also:Constant Field Values

- CREATEWORKITEM
static final int CREATEWORKITEM
Symbolic constant for task instance action create work item.
Since:
5.1
See Also:Constant Field Values

- DELETEWORKITEM
static final int DELETEWORKITEM
Symbolic constant for task instance action delete work item.
Since:
5.1
See Also:Constant Field Values

- TRANSFERWORKITEM
static final int TRANSFERWORKITEM
Symbolic constant for task instance action transfer work item.
Since:
5.1
See Also:Constant Field Values

- GETFAULTNAMES
static final int GETFAULTNAMES
Symbolic constant for task instance action get fault names.
Since:
5.1
See Also:Constant Field Values

- CALLTASK
static final int CALLTASK
Symbolic constant for task instance action call task.
Since:
6.0
See Also:Constant Field Values

- CREATEFAULTMESSAGE
static final int CREATEFAULTMESSAGE
Symbolic constant for task instance action create fault message.
Since:
6.0
See Also:Constant Field Values

- CREATEINPUTMESSAGE
static final int CREATEINPUTMESSAGE
Symbolic constant for task instance action create input message.
Since:
6.0
See Also:Constant Field Values

- CREATEOUTPUTMESSAGE
static final int CREATEOUTPUTMESSAGE
Symbolic constant for task instance action create output message.
Since:
6.0
See Also:Constant Field Values

- DELETE
static final int DELETE
Symbolic constant for task instance action delete task.
Since:
6.0
See Also:Constant Field Values

- GETDOCUMENTATION
static final int GETDOCUMENTATION
Symbolic constant for task instance action get documentation.
Since:
6.0
See Also:Constant Field Values

- GETTASK
static final int GETTASK
Symbolic constant for task instance action get task.
Since:
6.0
See Also:Constant Field Values

- STARTTASK
static final int STARTTASK
Symbolic constant for task instance action start task.
Since:
6.0
See Also:Constant Field Values

- RESTARTTASK
static final int RESTARTTASK
Symbolic constant for task instance action restart task.
Since:
6.2.0
See Also:Constant Field Values

- RESUME
static final int RESUME
Symbolic constant for task instance action resume task.
Since:
6.0
See Also:Constant Field Values

- COMPLETEWITHFOLLOWONTASK
static final int COMPLETEWITHFOLLOWONTASK
Symbolic constant for task instance action complete the current
 task and start a previously created task as follow-on task.
Since:
6.0.2
See Also:Constant Field Values

- STARTTASKASSUBTASK
static final int STARTTASKASSUBTASK
Symbolic constant for task instance action start task as subtask.
Since:
6.0.2
See Also:Constant Field Values

- SUSPEND
static final int SUSPEND
Symbolic constant for task instance action suspend task.
Since:
6.0
See Also:Constant Field Values

- TERMINATE
static final int TERMINATE
Symbolic constant for task instance action terminate task.
Since:
6.0
See Also:Constant Field Values

- UPDATE
static final int UPDATE
Symbolic constant for task instance action update task.
Since:
6.0
See Also:Constant Field Values

- GETROLEINFO
static final int GETROLEINFO
Symbolic constant for task instance action to retrieve role related information.
 States whether getUsersInRole() or isUserInRole() can be called.
Since:
6.0
See Also:Constant Field Values

- UPDATEINACTIVETASK
static final int UPDATEINACTIVETASK
Symbolic constant for task instance action update inactive task.
Since:
6.0
See Also:Constant Field Values

- SUSPENDWITHCANCELCLAIM
static final int SUSPENDWITHCANCELCLAIM
Symbolic constant for task instance action suspend task and later cancelClaim.
Since:
6.0.2
See Also:Constant Field Values

- SETINPUTMESSAGE
static final int SETINPUTMESSAGE
Symbolic constant for task instance action set input message.
Since:
6.1.2
See Also:Constant Field Values

- TRANSFERTOWORKBASKET
static final int TRANSFERTOWORKBASKET
Symbolic constant for task instance action transfer to work basket.
Since:
7.0
See Also:Constant Field Values

- SETTASKREAD
static final int SETTASKREAD
Symbolic constant for task instance action set task read.
Since:
7.0
See Also:Constant Field Values