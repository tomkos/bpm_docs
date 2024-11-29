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

## Interface ContextPropogation

- Deprecated.

@Deprecated
public interface ContextPropogation
Context propogation contract for runtime. Used by session/other runtime to
 access and set session context.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
Deprecated. 
Copyright

static ContextPropogation
INSTANCE
Deprecated. 
Comment for INSTANCE
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.io.Serializable
get(java.lang.String key)
Deprecated. 
Set one key from current WorkArea

ActivityData
getSessionContext()
Deprecated. 
Get SessionContext from current WorkArea.

commonj.sdo.DataObject
getSystemContext()
Deprecated. 
Get the session context from current work area.

void
restoreSessionContextFromString(java.lang.String theContext)
Deprecated. 
Restore the session context from serilizaed string to the current work area.

void
restoreSystemContext(java.io.Serializable theContext)
Deprecated. 
Restore the serialiable object.

java.lang.String
saveSessionContextToString()
Deprecated. 
Save the session context in the current work area to serialized string.

java.io.Serializable
saveSystemContext()
Deprecated. 
Save system context as serializable object.

void
set(java.lang.String key,
   java.io.Serializable value)
Deprecated. 
Set one key value into current WorkArea

void
setSessionContext(ActivityData theContext)
Deprecated. 
Set SessionContext to current WorkArea.

void
setSystemContext(commonj.sdo.DataObject sessionContext)
Deprecated. 
Set the session context to current work area.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
Deprecated. 
Copyright
See Also:Constant Field Values

- INSTANCE
static final ContextPropogation INSTANCE
Deprecated. 
Comment for INSTANCE

- Method Detail

### Method Detail

    - getSessionContext
ActivityData getSessionContext()
Deprecated. 
Get SessionContext from current WorkArea.
Returns:ActivityData
    - setSessionContext
void setSessionContext(ActivityData theContext)
                       throws com.ibm.ws.session.WBIReservedKeyException,
                              com.ibm.ws.session.WBIActivityNotActiveException
Deprecated. 
Set SessionContext to current WorkArea.
Parameters:theContext - 
Throws:
com.ibm.ws.session.WBIReservedKeyException
com.ibm.ws.session.WBIActivityNotActiveException
    - set
void set(java.lang.String key,
       java.io.Serializable value)
         throws com.ibm.ws.session.WBIReservedKeyException,
                com.ibm.ws.session.WBIActivityNotActiveException
Deprecated. 
Set one key value into current WorkArea
Parameters:key - value - 
Throws:
com.ibm.ws.session.WBIReservedKeyException
com.ibm.ws.session.WBIActivityNotActiveException
    - get
java.io.Serializable get(java.lang.String key)
                         throws com.ibm.ws.session.WBIActivityNotActiveException
Deprecated. 
Set one key from current WorkArea
Parameters:key - 
Returns:Serializable
Throws:
com.ibm.ws.session.WBIActivityNotActiveException
    - saveSessionContextToString
java.lang.String saveSessionContextToString()
Deprecated. 
Save the session context in the current work area to serialized string.

 It is used by the non-SCA bindings when they transforms the SessionContext to the outbound message.
Returns:the serialized string.
    - restoreSessionContextFromString
void restoreSessionContextFromString(java.lang.String theContext)
Deprecated. 
Restore the session context from serilizaed string to the current work area.

 It is used by the non-SCA bindings when they transforms the inbound message to the SessionContext.
Parameters:the - serialized string.
    - setSystemContext
void setSystemContext(commonj.sdo.DataObject sessionContext)
Deprecated. 
Set the session context to current work area.

 It is used by the web service binding.
Parameters:sessionContext: - DataObject.
    - getSystemContext
commonj.sdo.DataObject getSystemContext()
Deprecated. 
Get the session context from current work area.

 It is used by the web service binding.
Returns:DataObject: SessionContext instance.
         null: no session context existing in current work area.
    - saveSystemContext
java.io.Serializable saveSystemContext()
Deprecated. 
Save system context as serializable object.

 It is used by JMS binding to gain a better performance when they save
 SessionContext for the async response.
Returns:the serializable object
    - restoreSystemContext
void restoreSystemContext(java.io.Serializable theContext)
Deprecated. 
Restore the serialiable object.

 It is used by JMS binding to gain a better performance when they restore
  SessionContext to the async response
Parameters:theContext - the serializable object