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

## Class MediationFlowBean

- java.lang.Object
    - com.ibm.wsspi.sibx.mediation.flow.ejb.MediationFlowBean

- All Implemented Interfaces:
com.ibm.ws.sibx.mediation.flow.SIBXMediationFlowComponent, MediationFlowComponent, java.io.Serializable, javax.ejb.EnterpriseBean, javax.ejb.SessionBean

Deprecated.

public class MediationFlowBean
extends java.lang.Object
implements javax.ejb.SessionBean, com.ibm.ws.sibx.mediation.flow.SIBXMediationFlowComponent
Local EJB bean class for mediation flow container lifecycle management. This
 stateless session bean with a local home and interface allows the EJB
 container to manage the lifecycle of runtime mediation flows.
See Also:Serialized Form

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
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
    - Constructor Summary

Constructors 

Constructor and Description

MediationFlowBean()
Deprecated.
    - Method Summary Methods Modifier and Type Method and Description void ejbActivate () Deprecated. void ejbCreate () Deprecated. void ejbPassivate () Deprecated. void ejbRemove () Deprecated. com.ibm.ws.sibx.scax.mediation.engine.MediationFlow getMediationFlow (java.lang.String moduleName, java.lang.String componentName) Deprecated. javax.ejb.SessionContext getSessionContext () Deprecated. void invokeEventFlow (com.ibm.ws.sibx.mediation.esb.SIBXEvent event, commonj.sdo.DataObject message, com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction) Deprecated. void invokeFaultFlow (MediationFlowKey key, commonj.sdo.DataObject message, com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction) Deprecated. void invokeRequestFlow (MediationFlowKey key, commonj.sdo.DataObject message, com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction) Deprecated. void invokeResponseFlow (MediationFlowKey key, commonj.sdo.DataObject message, com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction) Deprecated. void setSessionContext (javax.ejb.SessionContext ctx) Deprecated. void transactionNotSupportedWriteContext (com.ibm.wsspi.sibx.context.ContextStore contextStore, java.lang.String key, long timeout, com.ibm.wsspi.sibx.context.Context context) Deprecated. void transactionSupportsWriteContext (com.ibm.wsspi.sibx.context.ContextStore contextStore, java.lang.String key, long timeout, com.ibm.wsspi.sibx.context.Context context) Deprecated.

### Method Summary

| Modifier and Type                                   | Method and Description                                                                                                                                                                                                                                                                         |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                                                | ejbActivate() Deprecated.                                                                                                                                                                                                                                                                      |
| void                                                | ejbCreate() Deprecated.                                                                                                                                                                                                                                                                        |
| void                                                | ejbPassivate() Deprecated.                                                                                                                                                                                                                                                                     |
| void                                                | ejbRemove() Deprecated.                                                                                                                                                                                                                                                                        |
| com.ibm.ws.sibx.scax.mediation.engine.MediationFlow | getMediationFlow(java.lang.String moduleName,                 java.lang.String componentName) Deprecated.                                                                                                                                                                                      |
| javax.ejb.SessionContext                            | getSessionContext() Deprecated.                                                                                                                                                                                                                                                                |
| void                                                | invokeEventFlow(com.ibm.ws.sibx.mediation.esb.SIBXEvent event,                commonj.sdo.DataObject message,                com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction) Deprecated.                                                                                |
| void                                                | invokeFaultFlow(MediationFlowKey key,                commonj.sdo.DataObject message,                com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction) Deprecated.                                                                                                         |
| void                                                | invokeRequestFlow(MediationFlowKey key,                  commonj.sdo.DataObject message,                  com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction) Deprecated.                                                                                                   |
| void                                                | invokeResponseFlow(MediationFlowKey key,                   commonj.sdo.DataObject message,                   com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction) Deprecated.                                                                                                |
| void                                                | setSessionContext(javax.ejb.SessionContext ctx) Deprecated.                                                                                                                                                                                                                                    |
| void                                                | transactionNotSupportedWriteContext(com.ibm.wsspi.sibx.context.ContextStore contextStore,                                    java.lang.String key,                                    long timeout,                                    com.ibm.wsspi.sibx.context.Context context) Deprecated. |
| void                                                | transactionSupportsWriteContext(com.ibm.wsspi.sibx.context.ContextStore contextStore,                                java.lang.String key,                                long timeout,                                com.ibm.wsspi.sibx.context.Context context) Deprecated.                 |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait