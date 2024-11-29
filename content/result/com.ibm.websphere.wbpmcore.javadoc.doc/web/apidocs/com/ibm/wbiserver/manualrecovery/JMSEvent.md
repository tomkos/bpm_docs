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

## Interface JMSEvent

- All Superinterfaces: FailedEvent public interface JMSEvent extends FailedEvent The JMSEvent is an interface to obtain detailed information of a failed event, and set new information for failed event resubmission. The detailed information includes

```
public interface JMSEvent
extends FailedEvent
```

    - Failed event parameters
    - CEI trace level
    - Expiration time

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String COPYRIGHT

### Field Summary

| Modifier and Type       | Field and Description   |
|-------------------------|-------------------------|
| static java.lang.String | COPYRIGHT               |

- Fields inherited from interface com.ibm.wbiserver.manualrecovery.FailedEvent
STATUS\_FAILED, STATUS\_STOPPED, STATUS\_TERMINATED, TYPE\_BFMHOLD, TYPE\_BPC, TYPE\_JMS, TYPE\_MQ, TYPE\_SCA

- Method Summary Methods Modifier and Type Method and Description java.lang.String getJMSCorrelationID () java.lang.String getJMSDeliveryMode () java.lang.String getJMSDestination () java.util.Date getJMSExpiration () int getJMSPriority () boolean getJMSRedelivered () java.lang.String getJMSReplyTo () java.lang.String getJMSType () int getJMSXDeliveryCount () java.util.List<FailedEventParameter > getPayload () Return parameters of the failed event. java.util.List<FailedEventParameter > getPayload (java.util.Properties adminClientProperties) Return parameters of the failed event with admin client connection properties. void setJMSExpiration (java.util.Date expiration) void setPayload (java.util.List payload)

### Method Summary

| Modifier and Type                    | Method and Description                                                                                                                |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String                     | getJMSCorrelationID()                                                                                                                 |
| java.lang.String                     | getJMSDeliveryMode()                                                                                                                  |
| java.lang.String                     | getJMSDestination()                                                                                                                   |
| java.util.Date                       | getJMSExpiration()                                                                                                                    |
| int                                  | getJMSPriority()                                                                                                                      |
| boolean                              | getJMSRedelivered()                                                                                                                   |
| java.lang.String                     | getJMSReplyTo()                                                                                                                       |
| java.lang.String                     | getJMSType()                                                                                                                          |
| int                                  | getJMSXDeliveryCount()                                                                                                                |
| java.util.List<FailedEventParameter> | getPayload() Return parameters of the failed event.                                                                                   |
| java.util.List<FailedEventParameter> | getPayload(java.util.Properties adminClientProperties) Return parameters of the failed event with admin client connection properties. |
| void                                 | setJMSExpiration(java.util.Date expiration)                                                                                           |
| void                                 | setPayload(java.util.List payload)                                                                                                    |

    - Methods inherited from interface com.ibm.wbiserver.manualrecovery.FailedEvent
didInitiateStore, getCorrelationId, getDeploymentTarget, getDestinationComponentName, getDestinationMethodName, getDestinationModuleName, getFailureDateTime, getFailureMessage, getInteractionType, getMsgId, getOwner, getResubmitDestination, getSessionId, getSourceComponentName, getSourceModuleName, getStatus, getType, isESQualified, isProcessResponse