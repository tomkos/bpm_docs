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

## Interface EscalationTemplateActions

- public interface EscalationTemplateActions
This interface defines symbolic constants for all actions that can be performed on
 escalation templates. These constants are to be used when determining the
 actions allowed in the current escalation template state.
 Currently allowed actions are returned
 when calling the getAvailableActions()
 method for an escalation template.
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
GETCUSTOMPROPERTY
Symbolic constant for escalation template action get custom property.

static int
GETDOCUMENTATION
Symbolic constant for escalation template action get documentation.

static int
GETESCALATIONTEMPLATE
Symbolic constant for escalation template action get escalation template.

static int
GETROLEINFO
Symbolic constant for escalation template action to retrieve role related information.

static int
GETTASKTEMPLATE
Symbolic constant for escalation template action get task template.

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- GETDOCUMENTATION
static final int GETDOCUMENTATION
Symbolic constant for escalation template action get documentation.
See Also:Constant Field Values

- GETCUSTOMPROPERTY
static final int GETCUSTOMPROPERTY
Symbolic constant for escalation template action get custom property.
See Also:Constant Field Values

- GETESCALATIONTEMPLATE
static final int GETESCALATIONTEMPLATE
Symbolic constant for escalation template action get escalation template.
See Also:Constant Field Values

- GETTASKTEMPLATE
static final int GETTASKTEMPLATE
Symbolic constant for escalation template action get task template.
See Also:Constant Field Values

- GETROLEINFO
static final int GETROLEINFO
Symbolic constant for escalation template action to retrieve role related information.
See Also:Constant Field Values