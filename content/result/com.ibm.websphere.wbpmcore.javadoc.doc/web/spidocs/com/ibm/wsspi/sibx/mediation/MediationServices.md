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

## Interface MediationServices

- public interface MediationServices
Provides services to a mediation primitive. Each mediation primitive has a 
 mediation services object which provides access to the terminals defined
 for the primitive, the primitive name and display name. The display name
 is normally set by the creator of the flow, wheras the name will be the
 name by which the mediation primitive is known by the runtime.
 
 Mediation primitives will primarily use the mediation services to access
 input and output terminals via the getter methods.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

InputTerminal
getInputTerminal(java.lang.String name)
Gets the named input terminal for this primitive.

java.util.List
getInputTerminals()
Returns an unmodifiable list of all input terminals defined for this
 mediation primitive.

java.lang.String
getMediationDisplayName()
Gets the display name of this mediation primitive.

java.lang.String
getMediationName()
Gets the name of this mediation primitive.

OutputTerminal
getOutputTerminal(java.lang.String name)
Gets the named output terminal for this primitive.

java.util.List
getOutputTerminals()
Returns an unmodifiable list of all output terminals defined for this
 mediation primitive.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- $sccsid
static final java.lang.String $sccsid
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getMediationName
java.lang.String getMediationName()
Gets the name of this mediation primitive. This name is set by the 
 flow creation tooling.
Returns:the name of the mediation primitive
    - getMediationDisplayName
java.lang.String getMediationDisplayName()
Gets the display name of this mediation primitive. This display name is
 normally set by the user who created the flow.
Returns:the display name of the mediation primitive
    - getInputTerminal
InputTerminal getInputTerminal(java.lang.String name)
                               throws TerminalNotFoundException
Gets the named input terminal for this primitive.
Parameters:name - the name of the input terminal
Returns:the input terminal
Throws:
TerminalNotFoundException - if the named terminal is not defined
         for this mediation primitive
    - getOutputTerminal
OutputTerminal getOutputTerminal(java.lang.String name)
                                 throws TerminalNotFoundException
Gets the named output terminal for this primitive.
Parameters:name - the name of the output terminal
Returns:the output terminal
Throws:
TerminalNotFoundException - if the named terminal is not defined
         for this mediation primitive
    - getInputTerminals
java.util.List getInputTerminals()
Returns an unmodifiable list of all input terminals defined for this
 mediation primitive.
Returns:the list of input terminals
    - getOutputTerminals
java.util.List getOutputTerminals()
Returns an unmodifiable list of all output terminals defined for this
 mediation primitive.
Returns:the list of output terminals