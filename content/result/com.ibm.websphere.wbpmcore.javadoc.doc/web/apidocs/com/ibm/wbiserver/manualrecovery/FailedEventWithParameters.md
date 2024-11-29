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

## Interface FailedEventWithParameters

- All Superinterfaces:
FailedEvent

All Known Implementing Classes:
FailedEventDetail, com.ibm.wbiserver.manualrecovery.FailedEventWithParametersImpl

Deprecated.

public interface FailedEventWithParameters
extends FailedEvent
Since:
6.2
Version:
6.0.1
See Also:SCAEvent

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String COPYRIGHT Deprecated.

### Field Summary

| Modifier and Type       | Field and Description   |
|-------------------------|-------------------------|
| static java.lang.String | COPYRIGHT Deprecated.   |

- Fields inherited from interface com.ibm.wbiserver.manualrecovery.FailedEvent
STATUS\_FAILED, STATUS\_STOPPED, STATUS\_TERMINATED, TYPE\_BFMHOLD, TYPE\_BPC, TYPE\_JMS, TYPE\_MQ, TYPE\_SCA

- Method Summary Methods Modifier and Type Method and Description java.lang.String getCEITraceControl () Deprecated. Return CEI trace control java.util.Date getExpirationTime () Deprecated. Return expiration time java.util.List getFailedEventParameters () Deprecated. Return parameters of the failed event. java.util.List getFailedEventParameters (java.util.Properties adminClientProperties) Deprecated. Return parameters of the failed event with admin client connection properties. void setCEITraceControl (java.lang.String ceiTraceControl) Deprecated. Set new CEI trace control void setExpirationTime (java.util.Date expirationTime) Deprecated. Set new expiration time void setFailedEventParameters (java.util.List failedEventParameters) Deprecated. Set new parameters to the failed event

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                           |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String    | getCEITraceControl() Deprecated.  Return CEI trace control                                                                                                       |
| java.util.Date      | getExpirationTime() Deprecated.  Return expiration time                                                                                                          |
| java.util.List      | getFailedEventParameters() Deprecated.  Return parameters of the failed event.                                                                                   |
| java.util.List      | getFailedEventParameters(java.util.Properties adminClientProperties) Deprecated.  Return parameters of the failed event with admin client connection properties. |
| void                | setCEITraceControl(java.lang.String ceiTraceControl) Deprecated.  Set new CEI trace control                                                                      |
| void                | setExpirationTime(java.util.Date expirationTime) Deprecated.  Set new expiration time                                                                            |
| void                | setFailedEventParameters(java.util.List failedEventParameters) Deprecated.  Set new parameters to the failed event                                               |

    - Methods inherited from interface com.ibm.wbiserver.manualrecovery.FailedEvent
didInitiateStore, getCorrelationId, getDeploymentTarget, getDestinationComponentName, getDestinationMethodName, getDestinationModuleName, getFailureDateTime, getFailureMessage, getInteractionType, getMsgId, getOwner, getResubmitDestination, getSessionId, getSourceComponentName, getSourceModuleName, getStatus, getType, isESQualified, isProcessResponse