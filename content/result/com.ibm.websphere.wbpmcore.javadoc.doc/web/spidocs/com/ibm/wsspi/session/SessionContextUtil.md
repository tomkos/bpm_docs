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

## Interface SessionContextUtil

- Deprecated.

@Deprecated
public interface SessionContextUtil
utility interface to get/set activity data from/to a sca message

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
Deprecated. 
Copyright

static SessionContextUtil
INSTANCE
Deprecated. 
Comment for INSTANCE
    - Method Summary

Methods 

Modifier and Type
Method and Description

ActivityData
getSessionContext(com.ibm.wsspi.sca.message.Message message)
Deprecated. 
Get SessionContext from a Service message.

void
restoreSessionContext(com.ibm.wsspi.sca.message.Message msg)
Deprecated. 
Restore SessionContext from SCA message to current work area.

void
setContextToMessage(com.ibm.wsspi.sca.message.Message msg,
                   ActivityData theContext)
Deprecated. 
Set SessionContext to a Service message.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
Deprecated. 
Copyright
See Also:Constant Field Values

- INSTANCE
static final SessionContextUtil INSTANCE
Deprecated. 
Comment for INSTANCE

- Method Detail

### Method Detail

    - getSessionContext
ActivityData getSessionContext(com.ibm.wsspi.sca.message.Message message)
Deprecated. 
Get SessionContext from a Service message.
Parameters:message - 
Returns:ActivityData
    - setContextToMessage
void setContextToMessage(com.ibm.wsspi.sca.message.Message msg,
                       ActivityData theContext)
Deprecated. 
Set SessionContext to a Service message.
Parameters:msg - theContext -
    - restoreSessionContext
void restoreSessionContext(com.ibm.wsspi.sca.message.Message msg)
Deprecated. 
Restore SessionContext from SCA message to current work area.
Parameters:msg -