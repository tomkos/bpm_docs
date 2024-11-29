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

## Interface MQEvent

- All Superinterfaces: FailedEvent public interface MQEvent extends FailedEvent The JMSEvent is an interface to obtain detailed information of a failed event, and set new information for failed event resubmission. The detailed information includes

```
public interface MQEvent
extends FailedEvent
```

    - Failed event parameters
    - CEI trace level
    - Expiration time

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String COPYRIGHT static int MQPER\_NOT\_PERSISTENT static int MQPER\_PERSISTENCE\_AS\_Q\_DEF static int MQPER\_PERSISTENT

### Field Summary

| Modifier and Type       | Field and Description      |
|-------------------------|----------------------------|
| static java.lang.String | COPYRIGHT                  |
| static int              | MQPER\_NOT\_PERSISTENT       |
| static int              | MQPER\_PERSISTENCE\_AS\_Q\_DEF |
| static int              | MQPER\_PERSISTENT           |

- Fields inherited from interface com.ibm.wbiserver.manualrecovery.FailedEvent
STATUS\_FAILED, STATUS\_STOPPED, STATUS\_TERMINATED, TYPE\_BFMHOLD, TYPE\_BPC, TYPE\_JMS, TYPE\_MQ, TYPE\_SCA

- Method Summary Methods Modifier and Type Method and Description byte[] getCorrelationID () java.lang.String getDeliveryMode () java.lang.String getDestination () java.util.Date getExpiration () java.util.List<FailedEventParameter > getPayload () Return parameters of the failed event. java.util.List<FailedEventParameter > getPayload (java.util.Properties adminClientProperties) Return parameters of the failed event with admin client connection properties. int getPriority () boolean getRedelivered () java.lang.String getReplyTo () java.lang.String getReplyToQMgr () java.lang.String getType () Get event type void setPayload (java.util.List<FailedEventParameter > payload)

### Method Summary

| Modifier and Type                    | Method and Description                                                                                                                |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| byte[]                               | getCorrelationID()                                                                                                                    |
| java.lang.String                     | getDeliveryMode()                                                                                                                     |
| java.lang.String                     | getDestination()                                                                                                                      |
| java.util.Date                       | getExpiration()                                                                                                                       |
| java.util.List<FailedEventParameter> | getPayload() Return parameters of the failed event.                                                                                   |
| java.util.List<FailedEventParameter> | getPayload(java.util.Properties adminClientProperties) Return parameters of the failed event with admin client connection properties. |
| int                                  | getPriority()                                                                                                                         |
| boolean                              | getRedelivered()                                                                                                                      |
| java.lang.String                     | getReplyTo()                                                                                                                          |
| java.lang.String                     | getReplyToQMgr()                                                                                                                      |
| java.lang.String                     | getType() Get event type                                                                                                              |
| void                                 | setPayload(java.util.List<FailedEventParameter> payload)                                                                              |

    - Methods inherited from interface com.ibm.wbiserver.manualrecovery.FailedEvent
didInitiateStore, getCorrelationId, getDeploymentTarget, getDestinationComponentName, getDestinationMethodName, getDestinationModuleName, getFailureDateTime, getFailureMessage, getInteractionType, getMsgId, getOwner, getResubmitDestination, getSessionId, getSourceComponentName, getSourceModuleName, getStatus, isESQualified, isProcessResponse