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

## Interface FailedEvent

- All Known Subinterfaces:
BFMHoldQueueEvent, BPCEvent, FailedEventWithParameters, JMSEvent, MQEvent, SCAEvent

All Known Implementing Classes:
FailedEventDetail, com.ibm.wbiserver.manualrecovery.FailedEventImpl, com.ibm.wbiserver.manualrecovery.FailedEventWithParametersImpl

public interface FailedEvent
The  FailedEvent  interface defines the basic information of a failed event.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
STATUS\_FAILED 

static int
STATUS\_STOPPED 

static int
STATUS\_TERMINATED 

static java.lang.String
TYPE\_BFMHOLD 

static java.lang.String
TYPE\_BPC 

static java.lang.String
TYPE\_JMS 

static java.lang.String
TYPE\_MQ 

static java.lang.String
TYPE\_SCA
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.Boolean
didInitiateStore()
If the failed event caused store to be initiated (started)

java.lang.String
getCorrelationId()
Get correlation sphere id

java.lang.String
getDeploymentTarget()
Get deployment target

java.lang.String
getDestinationComponentName()
Get destination component name

java.lang.String
getDestinationMethodName()
Get destination method name

java.lang.String
getDestinationModuleName()
Get destination module name

java.util.Date
getFailureDateTime()
Get failure time

java.lang.String
getFailureMessage()
Get exception detail

java.lang.String
getInteractionType()
Get interaction type

java.lang.String
getMsgId()
Get message id

java.lang.String
getOwner() 

java.lang.String
getResubmitDestination()
Get destination name for resubmission

java.lang.String
getSessionId()
Get session id

java.lang.String
getSourceComponentName()
Get source component name

java.lang.String
getSourceModuleName()
Get source module name

int
getStatus()
Get event status

java.lang.String
getType()
Get event type

java.lang.Boolean
isESQualified()
If the event is associated with event sequencing qualifier

java.lang.Boolean
isProcessResponse()
If the failed event is caused because a failure response
 could not be sent back to the caller who is a process

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- TYPE\_BPC
static final java.lang.String TYPE\_BPC
See Also:Constant Field Values

- TYPE\_SCA
static final java.lang.String TYPE\_SCA
See Also:Constant Field Values

- TYPE\_JMS
static final java.lang.String TYPE\_JMS
See Also:Constant Field Values

- TYPE\_BFMHOLD
static final java.lang.String TYPE\_BFMHOLD
See Also:Constant Field Values

- TYPE\_MQ
static final java.lang.String TYPE\_MQ
See Also:Constant Field Values

- STATUS\_FAILED
static final int STATUS\_FAILED
See Also:Constant Field Values

- STATUS\_TERMINATED
static final int STATUS\_TERMINATED
See Also:Constant Field Values

- STATUS\_STOPPED
static final int STATUS\_STOPPED
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getMsgId
java.lang.String getMsgId()
Get message id
Returns:String
    - getStatus
int getStatus()
Get event status
Returns:int
    - getType
java.lang.String getType()
Get event type
Returns:String
    - getDestinationModuleName
java.lang.String getDestinationModuleName()
Get destination module name
Returns:destination module name
    - getDestinationComponentName
java.lang.String getDestinationComponentName()
Get destination component name
Returns:destination component name
    - getDestinationMethodName
java.lang.String getDestinationMethodName()
Get destination method name
Returns:destination method name
    - getSourceModuleName
java.lang.String getSourceModuleName()
Get source module name
Returns:source module name
    - getSourceComponentName
java.lang.String getSourceComponentName()
Get source component name
Returns:source component name
    - getResubmitDestination
java.lang.String getResubmitDestination()
Get destination name for resubmission
Returns:destination name for resubmission
    - getInteractionType
java.lang.String getInteractionType()
Get interaction type
Returns:interaction type
    - getFailureMessage
java.lang.String getFailureMessage()
Get exception detail
Returns:failure message
    - getSessionId
java.lang.String getSessionId()
Get session id
Returns:session id
    - getCorrelationId
java.lang.String getCorrelationId()
Get correlation sphere id
Returns:correlation sphere id
    - getDeploymentTarget
java.lang.String getDeploymentTarget()
Get deployment target
Returns:deployment target
    - getFailureDateTime
java.util.Date getFailureDateTime()
Get failure time
Returns:failure time
    - isESQualified
java.lang.Boolean isESQualified()
If the event is associated with event sequencing qualifier
Returns:Boolean.TRUE if ES-qualified
         Boolean.FALSE if not ES-qualified
         null not applicable
    - isProcessResponse
java.lang.Boolean isProcessResponse()
If the failed event is caused because a failure response
 could not be sent back to the caller who is a process
Returns:Boolean.TRUE if failed process response
         Boolean.FALSE if not failed process response
         null not applicable
    - didInitiateStore
java.lang.Boolean didInitiateStore()
If the failed event caused store to be initiated (started)
Returns:Boolean.TRUE if failed event caused store to start
         Boolean.FALSE if failed event did not cause store to start
         null not applicable
    - getOwner
java.lang.String getOwner()