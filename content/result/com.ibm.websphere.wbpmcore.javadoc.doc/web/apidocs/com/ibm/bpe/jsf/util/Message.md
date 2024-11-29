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

## Interface Message

- All Superinterfaces:
java.io.Serializable

public interface Message
extends java.io.Serializable
This interface is used to implement localised messages.
 The List Component can display such messages.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
ERROR
ERROR message type

static int
INFO
INFO message type

static int
WARNING
WARNING message yype
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getMessage()
Returns a localised message.

int
getType()
Returns the type of the message.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- INFO
static final int INFO
INFO message type
See Also:Constant Field Values

- WARNING
static final int WARNING
WARNING message yype
See Also:Constant Field Values

- ERROR
static final int ERROR
ERROR message type
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getMessage
java.lang.String getMessage()
Returns a localised message.
 The locale can be looked up using the FacesContext.
Returns:The localised message
    - getType
int getType()
Returns the type of the message.
 The message must be an INFO, WARNING or ERROR message.
Returns:The type of the message