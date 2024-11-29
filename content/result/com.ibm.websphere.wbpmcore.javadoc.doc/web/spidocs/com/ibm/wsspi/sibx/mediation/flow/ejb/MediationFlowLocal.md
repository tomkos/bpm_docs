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

## Interface MediationFlowLocal

- All Superinterfaces:
javax.ejb.EJBLocalObject

Deprecated.

public interface MediationFlowLocal
extends javax.ejb.EJBLocalObject
Local interface of the Mediation Flow bean.
See Also:MediationFlowBean

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
    - Method Summary Methods Modifier and Type Method and Description void invokeEventFlow (com.ibm.ws.sibx.mediation.esb.SIBXEvent event, commonj.sdo.DataObject message, com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction) Deprecated. void invokeFaultFlow (MediationFlowKey key, commonj.sdo.DataObject message, com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction) Deprecated. void invokeRequestFlow (MediationFlowKey key, commonj.sdo.DataObject message, com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction) Deprecated. void invokeResponseFlow (MediationFlowKey key, commonj.sdo.DataObject message, com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction) Deprecated. void transactionNotSupportedWriteContext (com.ibm.wsspi.sibx.context.ContextStore contextStore, java.lang.String key, long timeout, com.ibm.wsspi.sibx.context.Context context) Deprecated. void transactionSupportsWriteContext (com.ibm.wsspi.sibx.context.ContextStore contextStore, java.lang.String key, long timeout, com.ibm.wsspi.sibx.context.Context context) Deprecated.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                                                                                                                                                         |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                | invokeEventFlow(com.ibm.ws.sibx.mediation.esb.SIBXEvent event,                commonj.sdo.DataObject message,                com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction) Deprecated.                                                                                |
| void                | invokeFaultFlow(MediationFlowKey key,                commonj.sdo.DataObject message,                com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction) Deprecated.                                                                                                         |
| void                | invokeRequestFlow(MediationFlowKey key,                  commonj.sdo.DataObject message,                  com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction) Deprecated.                                                                                                   |
| void                | invokeResponseFlow(MediationFlowKey key,                   commonj.sdo.DataObject message,                   com.ibm.wsspi.sibx.mediation.flow.action.FlowActionFactory flowAction) Deprecated.                                                                                                |
| void                | transactionNotSupportedWriteContext(com.ibm.wsspi.sibx.context.ContextStore contextStore,                                    java.lang.String key,                                    long timeout,                                    com.ibm.wsspi.sibx.context.Context context) Deprecated. |
| void                | transactionSupportsWriteContext(com.ibm.wsspi.sibx.context.ContextStore contextStore,                                java.lang.String key,                                long timeout,                                com.ibm.wsspi.sibx.context.Context context) Deprecated.                 |

- Methods inherited from interface javax.ejb.EJBLocalObject
getEJBLocalHome, getPrimaryKey, isIdentical, remove