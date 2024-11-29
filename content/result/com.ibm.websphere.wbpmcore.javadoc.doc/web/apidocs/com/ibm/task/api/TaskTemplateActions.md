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

## Interface TaskTemplateActions

- public interface TaskTemplateActions
This interface defines symbolic constants for all actions that can be performed on
 Task Templates. These constants are to be used when determining the actions
 allowed in the current task template state.
 
 Currently allowed actions are returned when calling the
 getAvailableActions()
 method for a task template.
Since:
6.1

- =========== FIELD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
COMPLETEWITHNEWFOLLOWONTASK
Symbolic constant for task template action complete task and create and
 start a new task as follow-on task.

static java.lang.String
COPYRIGHT 

static int
CREATEANDCALLTASK
Symbolic constant for task template action create and call task.

static int
CREATEANDSTARTTASK
Symbolic constant for task template action create and start task.

static int
CREATEANDSTARTTASKASSUBTASK
Symbolic constant for task template action create and start task as subtask.

static int
CREATEFAULTMESSAGE
Symbolic constant for task template action create fault message.

static int
CREATEINPUTMESSAGE
Symbolic constant for task template action create input message.

static int
CREATEOUTPUTMESSAGE
Symbolic constant for task template action create output message.

static int
CREATETASK
Symbolic constant for task template action create task.

static int
DELETETEMPLATE
Symbolic constant for task template action delete task template.

static int
GETCUSTOMPROPERTY
Symbolic constant for task template action get custom property.

static int
GETDOCUMENTATION
Symbolic constant for task template action get documentation.

static int
GETFAULTNAMES
Symbolic constant for task template action to retrieve fault name informations.

static int
GETROLEINFO
Symbolic constant for task instance action to retrieve role related information.

static int
GETTEMPLATE
Symbolic constant for task template action get task template.

static int
GETUISETTINGS
Symbolic constant for task template action get UI settings.

static int
STARTTEMPLATE
Symbolic constant for task template action start template.

static int
STOPTEMPLATE
Symbolic constant for task template action stop template.

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- GETCUSTOMPROPERTY
static final int GETCUSTOMPROPERTY
Symbolic constant for task template action get custom property.
Since:
6.0
See Also:Constant Field Values

- GETUISETTINGS
static final int GETUISETTINGS
Symbolic constant for task template action get UI settings.
Since:
6.0
See Also:Constant Field Values

- CREATETASK
static final int CREATETASK
Symbolic constant for task template action create task.
Since:
6.0
See Also:Constant Field Values

- CREATEANDSTARTTASK
static final int CREATEANDSTARTTASK
Symbolic constant for task template action create and start task.
Since:
6.0
See Also:Constant Field Values

- COMPLETEWITHNEWFOLLOWONTASK
static final int COMPLETEWITHNEWFOLLOWONTASK
Symbolic constant for task template action complete task and create and
 start a new task as follow-on task.
Since:
6.0.2
See Also:Constant Field Values

- CREATEANDSTARTTASKASSUBTASK
static final int CREATEANDSTARTTASKASSUBTASK
Symbolic constant for task template action create and start task as subtask.
Since:
6.0.2
See Also:Constant Field Values

- GETROLEINFO
static final int GETROLEINFO
Symbolic constant for task instance action to retrieve role related information.
Since:
6.0
See Also:Constant Field Values

- GETDOCUMENTATION
static final int GETDOCUMENTATION
Symbolic constant for task template action get documentation.
Since:
6.0
See Also:Constant Field Values

- DELETETEMPLATE
static final int DELETETEMPLATE
Symbolic constant for task template action delete task template.
Since:
6.0
See Also:Constant Field Values

- GETTEMPLATE
static final int GETTEMPLATE
Symbolic constant for task template action get task template.
Since:
6.0
See Also:Constant Field Values

- CREATEINPUTMESSAGE
static final int CREATEINPUTMESSAGE
Symbolic constant for task template action create input message.
Since:
6.0
See Also:Constant Field Values

- CREATEANDCALLTASK
static final int CREATEANDCALLTASK
Symbolic constant for task template action create and call task.
Since:
6.0
See Also:Constant Field Values

- STARTTEMPLATE
static final int STARTTEMPLATE
Symbolic constant for task template action start template.
Since:
6.0
See Also:Constant Field Values

- STOPTEMPLATE
static final int STOPTEMPLATE
Symbolic constant for task template action stop template.
Since:
6.0
See Also:Constant Field Values

- CREATEOUTPUTMESSAGE
static final int CREATEOUTPUTMESSAGE
Symbolic constant for task template action create output message.
Since:
6.2
See Also:Constant Field Values

- CREATEFAULTMESSAGE
static final int CREATEFAULTMESSAGE
Symbolic constant for task template action create fault message.
Since:
6.2
See Also:Constant Field Values

- GETFAULTNAMES
static final int GETFAULTNAMES
Symbolic constant for task template action to retrieve fault name informations.
Since:
6.2
See Also:Constant Field Values