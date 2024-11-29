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

## Interface SCAEvent

- All Superinterfaces: FailedEvent All Known Implementing Classes: FailedEventDetail , com.ibm.wbiserver.manualrecovery.FailedEventWithParametersImpl public interface SCAEvent extends FailedEvent The SCAEvent is an interface to obtain detailed information of a failed event, and set new information for failed event resubmission. The detailed information includes

```
public interface SCAEvent
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

- Method Summary Methods Modifier and Type Method and Description java.lang.String getCEITraceControl () Return CEI trace control java.util.Date getExpirationTime () Return expiration time java.util.List getFailedEventParameters () Return parameters of the failed event. java.util.List getFailedEventParameters (java.util.Properties adminClientProperties) Return parameters of the failed event with admin client connection properties. void setCEITraceControl (java.lang.String ceiTraceControl) Set new CEI trace control void setExpirationTime (java.util.Date expirationTime) Set new expiration time void setFailedEventParameters (java.util.List failedEventParameters) Set new parameters to the failed event

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                              |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String    | getCEITraceControl() Return CEI trace control                                                                                                       |
| java.util.Date      | getExpirationTime() Return expiration time                                                                                                          |
| java.util.List      | getFailedEventParameters() Return parameters of the failed event.                                                                                   |
| java.util.List      | getFailedEventParameters(java.util.Properties adminClientProperties) Return parameters of the failed event with admin client connection properties. |
| void                | setCEITraceControl(java.lang.String ceiTraceControl) Set new CEI trace control                                                                      |
| void                | setExpirationTime(java.util.Date expirationTime) Set new expiration time                                                                            |
| void                | setFailedEventParameters(java.util.List failedEventParameters) Set new parameters to the failed event                                               |

    - Methods inherited from interface com.ibm.wbiserver.manualrecovery.FailedEvent
didInitiateStore, getCorrelationId, getDeploymentTarget, getDestinationComponentName, getDestinationMethodName, getDestinationModuleName, getFailureDateTime, getFailureMessage, getInteractionType, getMsgId, getOwner, getResubmitDestination, getSessionId, getSourceComponentName, getSourceModuleName, getStatus, getType, isESQualified, isProcessResponse