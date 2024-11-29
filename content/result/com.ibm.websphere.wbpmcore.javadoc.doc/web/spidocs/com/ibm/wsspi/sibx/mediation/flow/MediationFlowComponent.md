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

## Interface MediationFlowComponent

- All Known Implementing Classes:
MediationFlowBean

Deprecated.

public interface MediationFlowComponent
Interface that represents a mediation flow component.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid
Deprecated. 
 

static java.lang.String
COPYRIGHT
Deprecated.
    - Method Summary

Methods 

Modifier and Type
Method and Description

void
invokeFaultFlow(MediationFlowKey key,
               commonj.sdo.DataObject message,
               com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction)
Deprecated.  

void
invokeRequestFlow(MediationFlowKey key,
                 commonj.sdo.DataObject message,
                 com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction)
Deprecated.  

void
invokeResponseFlow(MediationFlowKey key,
                  commonj.sdo.DataObject message,
                  com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction)
Deprecated.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
Deprecated. 
See Also:Constant Field Values

- $sccsid
static final java.lang.String $sccsid
Deprecated. 
See Also:Constant Field Values

- Method Detail

### Method Detail

    - invokeRequestFlow
void invokeRequestFlow(MediationFlowKey key,
                     commonj.sdo.DataObject message,
                     com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction)
                       throws MediationRuntimeException,
                              MediationConfigurationException,
                              MediationBusinessException
Deprecated. 
Invoke the request flow identified by the supplied key.
Parameters:key - the key identifying the request flow to invokemessage - the message to mediateflowAction - the flow action factory
Throws:
MediationRuntimeException - thrown by mediation runtime
MediationConfigurationException - thrown by mediation primitives
MediationBusinessException - thrown by mediation primitives
    - invokeResponseFlow
void invokeResponseFlow(MediationFlowKey key,
                      commonj.sdo.DataObject message,
                      com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction)
                        throws MediationRuntimeException,
                               MediationConfigurationException,
                               MediationBusinessException
Deprecated. 
Invoke the response flow identified by the supplied key.
Parameters:key - the key identifying the response flow to invokemessage - the message to mediateflowAction - the flow action factory
Throws:
MediationRuntimeException - thrown by mediation runtime
MediationConfigurationException - thrown by mediation primitives
MediationBusinessException - thrown by mediation primitives
    - invokeFaultFlow
void invokeFaultFlow(MediationFlowKey key,
                   commonj.sdo.DataObject message,
                   com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction)
                     throws MediationRuntimeException,
                            MediationConfigurationException,
                            MediationBusinessException
Deprecated. 
Invoke the fault flow identified by the supplied key.
Parameters:key - the key identifying the fault flow to invokemessage - the message to mediateflowAction - the flow action factory
Throws:
MediationRuntimeException - thrown by mediation runtime
MediationConfigurationException - thrown by mediation primitives
MediationBusinessException - thrown by mediation primitives