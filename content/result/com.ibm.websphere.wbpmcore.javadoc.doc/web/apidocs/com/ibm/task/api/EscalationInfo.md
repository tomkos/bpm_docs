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

## Interface EscalationInfo

- All Superinterfaces:
java.io.Serializable

public interface EscalationInfo
extends java.io.Serializable
Returns information about all escalations of a task instance.
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

java.util.List
getEscalationChains(int activationState)
Returns the escalation chains for the specified activation state.

int
getTotalNumberOfChains()
Returns the total number of escalation chains, regardless of the activation state.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getEscalationChains
java.util.List getEscalationChains(int activationState)
                                   throws InvalidParameterException
Returns the escalation chains for the specified activation state.
Parameters:activationState - The activation state. Possible activation states are ready, running, claimed, and
    waiting-for-subtasks. Use the definitions on the escalation object.
Returns:A list of EscalationChain objects.
Throws:
InvalidParameterException
    - getTotalNumberOfChains
int getTotalNumberOfChains()
Returns the total number of escalation chains, regardless of the activation state.
Returns:The total number of chains.