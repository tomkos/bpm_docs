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

## Interface EscalationActions

- public interface EscalationActions
This interface defines symbolic constants for all actions that can be performed on
 escalation instances. These constants are to be used when determining the actions
 allowed in the current escalation state.
 Currently allowed actions are returned
 when calling the getAvailableActions()
 method for an escalation instance.
Since:
6.1

- =========== FIELD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
CREATEWORKITEM
Symbolic constant for escalation action create work item.

static int
DELETEWORKITEM
Symbolic constant for escalation action delete work item.

static int
GETCUSTOMPROPERTY
Symbolic constant for escalation action get custom property.

static int
GETDOCUMENTATION
Symbolic constant for escalation action get documentation.

static int
GETESCALATION
Symbolic constant for escalation action get escalation.

static int
GETESCALATIONTEMPLATE
Symbolic constant for escalation action get escalation template.

static int
GETROLEINFO
Symbolic constant for escalation action to retrieve role related information.

static int
SETCUSTOMPROPERTY
Symbolic constant for escalation action set custom property.

static int
TRANSFERWORKITEM
Symbolic constant for escalation action transfer work item.

static int
TRIGGERESCALATION
Symbolic constant for escalation action trigger escalation.

static int
UPDATE
Symbolic constant for escalation action update.

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- CREATEWORKITEM
static final int CREATEWORKITEM
Symbolic constant for escalation action create work item.
See Also:Constant Field Values

- GETDOCUMENTATION
static final int GETDOCUMENTATION
Symbolic constant for escalation action get documentation.
See Also:Constant Field Values

- GETCUSTOMPROPERTY
static final int GETCUSTOMPROPERTY
Symbolic constant for escalation action get custom property.
See Also:Constant Field Values

- SETCUSTOMPROPERTY
static final int SETCUSTOMPROPERTY
Symbolic constant for escalation action set custom property.
See Also:Constant Field Values

- GETESCALATION
static final int GETESCALATION
Symbolic constant for escalation action get escalation.
See Also:Constant Field Values

- UPDATE
static final int UPDATE
Symbolic constant for escalation action update.
Since:
7.0
See Also:Constant Field Values

- GETESCALATIONTEMPLATE
static final int GETESCALATIONTEMPLATE
Symbolic constant for escalation action get escalation template.
See Also:Constant Field Values

- DELETEWORKITEM
static final int DELETEWORKITEM
Symbolic constant for escalation action delete work item.
See Also:Constant Field Values

- TRANSFERWORKITEM
static final int TRANSFERWORKITEM
Symbolic constant for escalation action transfer work item.
See Also:Constant Field Values

- GETROLEINFO
static final int GETROLEINFO
Symbolic constant for escalation action to retrieve role related information.
See Also:Constant Field Values

- TRIGGERESCALATION
static final int TRIGGERESCALATION
Symbolic constant for escalation action trigger escalation.
Since:
7.0
See Also:Constant Field Values