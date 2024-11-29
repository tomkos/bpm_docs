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

## Interface Terminal

- All Known Subinterfaces:
InputTerminal, OutputTerminal

public interface Terminal
Defines a set of common methods for all terminal types. This interface
 provides access to the terminal name and type. All
 terminals on a mediation primitive must have a name, which is unique for
 that type of terminal. Equally, all terminals have display names,
 which may be user-defined, depending upon the type of mediation
 primitive with which they are associated.
 
 Terminals may have a particular Type, which is identified by the 
 TerminalType. If a terminal does not have a type, then getTerminalType()
 will return null so primitive implementations should expect to handle this.

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

java.lang.String
getDisplayName()
Returns the display name of this terminal.

java.lang.String
getName()
Returns the name of this terminal.

TerminalType
getType()
Returns the type of this terminal.

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

    - getName
java.lang.String getName()
Returns the name of this terminal.
Returns:the terminal name
    - getType
TerminalType getType()
Returns the type of this terminal.
Returns:the terminal type
    - getDisplayName
java.lang.String getDisplayName()
Returns the display name of this terminal.
Returns:the terminal display name