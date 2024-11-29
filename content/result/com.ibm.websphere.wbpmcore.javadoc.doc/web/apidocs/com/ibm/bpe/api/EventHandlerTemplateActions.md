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

## Interface EventHandlerTemplateActions

- public interface EventHandlerTemplateActions
This interface defines symbolic constants for all actions that can be performed on
 event handler templates. These constants are to be used when determining the actions
 allowed on the event handler template by the current user.
 Currently allowed actions are returned
 when calling the getAvailableActions()
 method on a event handler template.
Since:
6.0

- =========== FIELD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
CREATEMESSAGE
Symbolic constant for event handler template action create message.

static int
GETVARIABLENAMES
Symbolic constant for event handler template action get variable names.

static int
SENDMESSAGE
Symbolic constant for event handler template action send message.

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- SENDMESSAGE
static final int SENDMESSAGE
Symbolic constant for event handler template action send message.
See Also:Constant Field Values

- CREATEMESSAGE
static final int CREATEMESSAGE
Symbolic constant for event handler template action create message.
See Also:Constant Field Values

- GETVARIABLENAMES
static final int GETVARIABLENAMES
Symbolic constant for event handler template action get variable names.
See Also:Constant Field Values