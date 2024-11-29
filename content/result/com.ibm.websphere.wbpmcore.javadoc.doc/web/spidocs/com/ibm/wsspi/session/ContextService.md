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

## Interface ContextService

- Deprecated.

@Deprecated
public interface ContextService
The ContextService interface represents the programming model for the
 context service in IBM Business Automation Workflow. The IBM Business Automation Workflow context service provides the ability to
 access and modify the execution context, and propagate the execution
 context to the downstream.
 
 This interface is used by all Workflow Server internal components. It includes not only all
 methods in the ContextService SPI,
 but also the methods which are available for the internal components.
See Also:com.ibm.bpm.context.ContextService

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
Deprecated. 
Copyright

static ContextService
INSTANCE
Deprecated. 
The singleton to access ContextService.
    - Method Summary

Methods 

Modifier and Type
Method and Description

com.ibm.websphere.sibx.smobo.ContextType
getContext()
Deprecated. 
Get the user context data from the current execution context.

com.ibm.websphere.sibx.smobo.HeadersType
getHeaders()
Deprecated. 
Get the protocol headers in the current execution context
 

 The protocol headers type is represented by
 HeadersType.

void
restoreUserContext(java.io.Serializable userContext)
Deprecated. 
Restore the UserContext to the current work area from a serializable object.

void
restoreUserContextFromString(java.lang.String value)
Deprecated. 
Restore the UserContext to the current work area from a serailzed string.

java.io.Serializable
saveUserContext()
Deprecated. 
Save the UserContext to a serializable object.

java.lang.String
saveUserContextToString()
Deprecated. 
Save the UserContext in the current work area to a serialized string .

void
setContext(com.ibm.websphere.sibx.smobo.ContextType context)
Deprecated. 
Set user context data to the current execution context.

void
setHeaders(com.ibm.websphere.sibx.smobo.HeadersType headers)
Deprecated. 
Set the protocol headers to the current execution context.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
Deprecated. 
Copyright
See Also:Constant Field Values

- INSTANCE
static final ContextService INSTANCE
Deprecated. 
The singleton to access ContextService.

- Method Detail

### Method Detail

    - saveUserContextToString
java.lang.String saveUserContextToString()
Deprecated. 
Save the UserContext in the current work area to a serialized string .

 It is used by the non-SCA bindings when they transforms the UserContext to the outbound message.
Returns:the serialized string
    - restoreUserContextFromString
void restoreUserContextFromString(java.lang.String value)
Deprecated. 
Restore the UserContext to the current work area from a serailzed string.

 It is used by the non-SCA bindings when they transforms the inbound message to the UserContext.
Parameters:value -
    - saveUserContext
java.io.Serializable saveUserContext()
Deprecated. 
Save the UserContext to a serializable object.

 It is used by JMS/MQ bindings to improve performance when they save the user context to async response message.
Returns:serializable user context
    - restoreUserContext
void restoreUserContext(java.io.Serializable userContext)
Deprecated. 
Restore the UserContext to the current work area from a serializable object.

 It is used by JMS/MQ bindings to improve performance when they restore the user context from async response message.
Parameters:userContext -
    - getHeaders
com.ibm.websphere.sibx.smobo.HeadersType getHeaders()
Deprecated. 
Get the protocol headers in the current execution context
 

 The protocol headers type is represented by
 HeadersType.
Returns:the protocol headers in current execution contextSee Also:HeadersType
    - setHeaders
void setHeaders(com.ibm.websphere.sibx.smobo.HeadersType headers)
Deprecated. 
Set the protocol headers to the current execution context.
 

 If the input headers value is null, the protocol headers in current execution
 context will be removed.
 

 The context service does not guarantee to propagate the context data if it
 is not set to current execution context.
Parameters:headers - the protocol headers.See Also:HeadersType
    - getContext
com.ibm.websphere.sibx.smobo.ContextType getContext()
Deprecated. 
Get the user context data from the current execution context.
 

 The user context type is presented by
 ContextType
Returns:the user context data in current execution contextSee Also:ContextType
    - setContext
void setContext(com.ibm.websphere.sibx.smobo.ContextType context)
Deprecated. 
Set user context data to the current execution context.
 

 If the input context value is null, the user context data in the current context
 will be removed.
 

 The context service does not guarantee to propagate the context data if it
 is not set to current execution context.
Parameters:context - the user context data.