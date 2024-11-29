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

## Interface EscalationChain

- All Superinterfaces:
java.io.Serializable

public interface EscalationChain
extends java.io.Serializable
Describes an escalation chain.
Since:
7.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

int
getActivationState()
Returns the activation state of the escalation chain.

Escalation
getEscalation(java.lang.String escalationName)
Returns the named escalation instance in the escalation chain.

java.util.List
getEscalations()
Returns the ordered list of escalations in the escalation chain.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getActivationState
int getActivationState()
Returns the activation state of the escalation chain.
Returns:The activation state for the escalation chain.
    Possible activation states are ready, running, claimed, and
    waiting-for-subtasks. See the definitions on the escalation object.
    - getEscalations
java.util.List getEscalations()
Returns the ordered list of escalations in the escalation chain.
Returns:The ordered list of escalations in the chain. The list may be empty, but not null.
    - getEscalation
Escalation getEscalation(java.lang.String escalationName)
Returns the named escalation instance in the escalation chain.
Parameters:escalationName - The name of the requested escalation.
Returns:The escalation instance or null if not found.