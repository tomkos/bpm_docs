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

## Interface BPCEvent

- All Superinterfaces: FailedEvent public interface BPCEvent extends FailedEvent The BPCEvent is an interface to obtain detailed information of a failed event, and set new information for failed event resubmission. The detailed information includes

```
public interface BPCEvent
extends FailedEvent
```

    - Process Instance Name
    - Top Level Process ID
    - Input Message
    - Stopped Activitis in the failed event
    - Process Instance ID

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String COPYRIGHT

### Field Summary

| Modifier and Type       | Field and Description   |
|-------------------------|-------------------------|
| static java.lang.String | COPYRIGHT               |

- Fields inherited from interface com.ibm.wbiserver.manualrecovery.FailedEvent
STATUS\_FAILED, STATUS\_STOPPED, STATUS\_TERMINATED, TYPE\_BFMHOLD, TYPE\_BPC, TYPE\_JMS, TYPE\_MQ, TYPE\_SCA

- Method Summary Methods Modifier and Type Method and Description java.util.List<FailedEventParameter > getInputMessage () Return parameters of the BPC failed event. java.util.List<FailedEventParameter > getInputMessage (java.util.Properties adminClientProperties) Return parameters of the failed event with admin client connection properties. java.lang.String getPiid () java.lang.String getProcessInstanceName () Return the process instance name for the failed event BPCActivity [] getStoppedActivities () Return the stopped activity list for the BPC failed event(running-stopped) java.lang.String getTopLevelProcessId () The top level process ID for the process instance of the failed event boolean isTopLevelProcess () The procecss intance for the failed event is the top level process or not

### Method Summary

| Modifier and Type                    | Method and Description                                                                                                                     |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| java.util.List<FailedEventParameter> | getInputMessage() Return parameters of the BPC failed event.                                                                               |
| java.util.List<FailedEventParameter> | getInputMessage(java.util.Properties adminClientProperties) Return parameters of the failed event with admin client connection properties. |
| java.lang.String                     | getPiid()                                                                                                                                  |
| java.lang.String                     | getProcessInstanceName() Return the process instance name for the failed event                                                             |
| BPCActivity[]                        | getStoppedActivities() Return the stopped activity list for the BPC failed event(running-stopped)                                          |
| java.lang.String                     | getTopLevelProcessId() The top level process ID for the process instance of the failed event                                               |
| boolean                              | isTopLevelProcess() The procecss intance for the failed event is the top level process or not                                              |

    - Methods inherited from interface com.ibm.wbiserver.manualrecovery.FailedEvent
didInitiateStore, getCorrelationId, getDeploymentTarget, getDestinationComponentName, getDestinationMethodName, getDestinationModuleName, getFailureDateTime, getFailureMessage, getInteractionType, getMsgId, getOwner, getResubmitDestination, getSessionId, getSourceComponentName, getSourceModuleName, getStatus, getType, isESQualified, isProcessResponse