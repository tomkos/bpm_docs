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

## Interface BFMHoldQueueEvent

- All Superinterfaces: FailedEvent public interface BFMHoldQueueEvent extends FailedEvent The BFMHoldQueueEvent interface defines the detail information of a HLD failed event. The The detailed information includes

```
public interface BFMHoldQueueEvent
extends FailedEvent
```

    - Process Instance ID
    - Process Instance Name
    - Proces Instance State
    - Activity Instance ID
    - Activity Instance Name
    - Activity Template Name
    - Process Template Name

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String COPYRIGHT

### Field Summary

| Modifier and Type       | Field and Description   |
|-------------------------|-------------------------|
| static java.lang.String | COPYRIGHT               |

- Fields inherited from interface com.ibm.wbiserver.manualrecovery.FailedEvent
STATUS\_FAILED, STATUS\_STOPPED, STATUS\_TERMINATED, TYPE\_BFMHOLD, TYPE\_BPC, TYPE\_JMS, TYPE\_MQ, TYPE\_SCA

- Method Summary Methods Modifier and Type Method and Description java.lang.String getActivityInstanceName () Return Activity Instance Name java.lang.String getAIID () Return Activity Instance ID java.lang.String getATID () Return Activity Tempate ID java.lang.String getPIID () Return Process Instance ID java.lang.String getProcessInstanceName () Return Process InstanceName int getProcessInstanceState () Return Process Instance state java.lang.String getProcessTemplateName () Return Process Template Name

### Method Summary

| Modifier and Type   | Method and Description                                  |
|---------------------|---------------------------------------------------------|
| java.lang.String    | getActivityInstanceName() Return Activity Instance Name |
| java.lang.String    | getAIID() Return Activity Instance ID                   |
| java.lang.String    | getATID() Return Activity Tempate ID                    |
| java.lang.String    | getPIID() Return  Process Instance ID                   |
| java.lang.String    | getProcessInstanceName() Return Process InstanceName    |
| int                 | getProcessInstanceState() Return Process Instance state |
| java.lang.String    | getProcessTemplateName() Return Process Template Name   |

    - Methods inherited from interface com.ibm.wbiserver.manualrecovery.FailedEvent
didInitiateStore, getCorrelationId, getDeploymentTarget, getDestinationComponentName, getDestinationMethodName, getDestinationModuleName, getFailureDateTime, getFailureMessage, getInteractionType, getMsgId, getOwner, getResubmitDestination, getSessionId, getSourceComponentName, getSourceModuleName, getStatus, getType, isESQualified, isProcessResponse