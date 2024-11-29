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

## Interface MQCIH

- public interface MQCIH begin-user-doc A representation of the model object 'MQCIH '. end-user-doc The following features are supported: See Also: WMQStructuresPackage.getMQCIH()

```
public interface MQCIH
```

The following features are supported:
 
Program Name
Version
Flags
Return Code
Comp Code
Reason
UOW Control
Get Wait Interval
Link Type
Output Data Length
Facility Keep Time
ADS Descriptor
Conversational Task
Task End Status
Facility
Function
Abend Code
Authenticator
Reserved1
Reply To Format
Remote Sys Id
Remote Trans Id
Transaction Id
Facility Like
Attention Id
Start Code
Cancel Code
Next Transaction Id
Reserved2
Reserved3
Cursor Position
Error Offset
Input Item
Reserved4

- ========== METHOD SUMMARY ===========
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getAbendCode()
Returns the value of the 'Abend Code' attribute.

int
getADSDescriptor()
Returns the value of the 'ADS Descriptor' attribute

java.lang.String
getAttentionId()
Returns the value of the 'Attention Id' attribute.

java.lang.String
getAuthenticator()
Returns the value of the 'Authenticator' attribute.

java.lang.String
getCancelCode()
Returns the value of the 'Cancel Code' attribute.

int
getCompCode()
Returns the value of the 'Comp Code' attribute

int
getConversationalTask()
Returns the value of the 'Conversational Task' attribute

int
getCursorPosition()
Returns the value of the 'Cursor Position' attribute

int
getErrorOffset()
Returns the value of the 'Error Offset' attribute

byte[]
getFacility()
Returns the value of the 'Facility' attribute

int
getFacilityKeepTime()
Returns the value of the 'Facility Keep Time' attribute

java.lang.String
getFacilityLike()
Returns the value of the 'Facility Like' attribute.

int
getFlags()
Returns the value of the 'Flags' attribute

java.lang.String
getFunction()
Returns the value of the 'Function' attribute.

int
getGetWaitInterval()
Returns the value of the 'Get Wait Interval' attribute

int
getInputItem()
Returns the value of the 'Input Item' attribute

int
getLinkType()
Returns the value of the 'Link Type' attribute

java.lang.String
getNextTransactionId()
Returns the value of the 'Next Transaction Id' attribute.

int
getOutputDataLength()
Returns the value of the 'Output Data Length' attribute

java.lang.String
getProgramName()
Returns the value of the 'Program Name' attribute

int
getReason()
Returns the value of the 'Reason' attribute

java.lang.String
getRemoteSysId()
Returns the value of the 'Remote Sys Id' attribute.

java.lang.String
getRemoteTransId()
Returns the value of the 'Remote Trans Id' attribute.

java.lang.String
getReplyToFormat()
Returns the value of the 'Reply To Format' attribute.

java.lang.String
getReserved1()
Returns the value of the 'Reserved1' attribute.

java.lang.String
getReserved2()
Returns the value of the 'Reserved2' attribute.

java.lang.String
getReserved3()
Returns the value of the 'Reserved3' attribute.

int
getReserved4()
Returns the value of the 'Reserved4' attribute

int
getReturnCode()
Returns the value of the 'Return Code' attribute

java.lang.String
getStartCode()
Returns the value of the 'Start Code' attribute.

int
getTaskEndStatus()
Returns the value of the 'Task End Status' attribute

java.lang.String
getTransactionId()
Returns the value of the 'Transaction Id' attribute.

int
getUOWControl()
Returns the value of the 'UOW Control' attribute

int
getVersion()
Returns the value of the 'Version' attribute

boolean
isSetAbendCode()
Returns whether the value of the 'Abend Code' attribute is set

boolean
isSetADSDescriptor()
Returns whether the value of the 'ADS Descriptor' attribute is set

boolean
isSetAttentionId()
Returns whether the value of the 'Attention Id' attribute is set

boolean
isSetAuthenticator()
Returns whether the value of the 'Authenticator' attribute is set

boolean
isSetCancelCode()
Returns whether the value of the 'Cancel Code' attribute is set

boolean
isSetCompCode()
Returns whether the value of the 'Comp Code' attribute is set

boolean
isSetConversationalTask()
Returns whether the value of the 'Conversational Task' attribute is set

boolean
isSetCursorPosition()
Returns whether the value of the 'Cursor Position' attribute is set

boolean
isSetErrorOffset()
Returns whether the value of the 'Error Offset' attribute is set

boolean
isSetFacilityKeepTime()
Returns whether the value of the 'Facility Keep Time' attribute is set

boolean
isSetFacilityLike()
Returns whether the value of the 'Facility Like' attribute is set

boolean
isSetFlags()
Returns whether the value of the 'Flags' attribute is set

boolean
isSetFunction()
Returns whether the value of the 'Function' attribute is set

boolean
isSetGetWaitInterval()
Returns whether the value of the 'Get Wait Interval' attribute is set

boolean
isSetInputItem()
Returns whether the value of the 'Input Item' attribute is set

boolean
isSetLinkType()
Returns whether the value of the 'Link Type' attribute is set

boolean
isSetNextTransactionId()
Returns whether the value of the 'Next Transaction Id' attribute is set

boolean
isSetOutputDataLength()
Returns whether the value of the 'Output Data Length' attribute is set

boolean
isSetReason()
Returns whether the value of the 'Reason' attribute is set

boolean
isSetRemoteSysId()
Returns whether the value of the 'Remote Sys Id' attribute is set

boolean
isSetRemoteTransId()
Returns whether the value of the 'Remote Trans Id' attribute is set

boolean
isSetReplyToFormat()
Returns whether the value of the 'Reply To Format' attribute is set

boolean
isSetReserved1()
Returns whether the value of the 'Reserved1' attribute is set

boolean
isSetReserved2()
Returns whether the value of the 'Reserved2' attribute is set

boolean
isSetReserved3()
Returns whether the value of the 'Reserved3' attribute is set

boolean
isSetReserved4()
Returns whether the value of the 'Reserved4' attribute is set

boolean
isSetReturnCode()
Returns whether the value of the 'Return Code' attribute is set

boolean
isSetStartCode()
Returns whether the value of the 'Start Code' attribute is set

boolean
isSetTaskEndStatus()
Returns whether the value of the 'Task End Status' attribute is set

boolean
isSetTransactionId()
Returns whether the value of the 'Transaction Id' attribute is set

boolean
isSetUOWControl()
Returns whether the value of the 'UOW Control' attribute is set

boolean
isSetVersion()
Returns whether the value of the 'Version' attribute is set

void
setAbendCode(java.lang.String value)
Sets the value of the 'Abend Code' attribute

void
setADSDescriptor(int value)
Sets the value of the 'ADS Descriptor' attribute

void
setAttentionId(java.lang.String value)
Sets the value of the 'Attention Id' attribute

void
setAuthenticator(java.lang.String value)
Sets the value of the 'Authenticator' attribute

void
setCancelCode(java.lang.String value)
Sets the value of the 'Cancel Code' attribute

void
setCompCode(int value)
Sets the value of the 'Comp Code' attribute

void
setConversationalTask(int value)
Sets the value of the 'Conversational Task' attribute

void
setCursorPosition(int value)
Sets the value of the 'Cursor Position' attribute

void
setErrorOffset(int value)
Sets the value of the 'Error Offset' attribute

void
setFacility(byte[] value)
Sets the value of the 'Facility' attribute

void
setFacilityKeepTime(int value)
Sets the value of the 'Facility Keep Time' attribute

void
setFacilityLike(java.lang.String value)
Sets the value of the 'Facility Like' attribute

void
setFlags(int value)
Sets the value of the 'Flags' attribute

void
setFunction(java.lang.String value)
Sets the value of the 'Function' attribute

void
setGetWaitInterval(int value)
Sets the value of the 'Get Wait Interval' attribute

void
setInputItem(int value)
Sets the value of the 'Input Item' attribute

void
setLinkType(int value)
Sets the value of the 'Link Type' attribute

void
setNextTransactionId(java.lang.String value)
Sets the value of the 'Next Transaction Id' attribute

void
setOutputDataLength(int value)
Sets the value of the 'Output Data Length' attribute

void
setProgramName(java.lang.String value)
Sets the value of the 'Program Name' attribute

void
setReason(int value)
Sets the value of the 'Reason' attribute

void
setRemoteSysId(java.lang.String value)
Sets the value of the 'Remote Sys Id' attribute

void
setRemoteTransId(java.lang.String value)
Sets the value of the 'Remote Trans Id' attribute

void
setReplyToFormat(java.lang.String value)
Sets the value of the 'Reply To Format' attribute

void
setReserved1(java.lang.String value)
Sets the value of the 'Reserved1' attribute

void
setReserved2(java.lang.String value)
Sets the value of the 'Reserved2' attribute

void
setReserved3(java.lang.String value)
Sets the value of the 'Reserved3' attribute

void
setReserved4(int value)
Sets the value of the 'Reserved4' attribute

void
setReturnCode(int value)
Sets the value of the 'Return Code' attribute

void
setStartCode(java.lang.String value)
Sets the value of the 'Start Code' attribute

void
setTaskEndStatus(int value)
Sets the value of the 'Task End Status' attribute

void
setTransactionId(java.lang.String value)
Sets the value of the 'Transaction Id' attribute

void
setUOWControl(int value)
Sets the value of the 'UOW Control' attribute

void
setVersion(int value)
Sets the value of the 'Version' attribute

void
unsetAbendCode()
Unsets the value of the 'Abend Code' attribute

void
unsetADSDescriptor()
Unsets the value of the 'ADS Descriptor' attribute

void
unsetAttentionId()
Unsets the value of the 'Attention Id' attribute

void
unsetAuthenticator()
Unsets the value of the 'Authenticator' attribute

void
unsetCancelCode()
Unsets the value of the 'Cancel Code' attribute

void
unsetCompCode()
Unsets the value of the 'Comp Code' attribute

void
unsetConversationalTask()
Unsets the value of the 'Conversational Task' attribute

void
unsetCursorPosition()
Unsets the value of the 'Cursor Position' attribute

void
unsetErrorOffset()
Unsets the value of the 'Error Offset' attribute

void
unsetFacilityKeepTime()
Unsets the value of the 'Facility Keep Time' attribute

void
unsetFacilityLike()
Unsets the value of the 'Facility Like' attribute

void
unsetFlags()
Unsets the value of the 'Flags' attribute

void
unsetFunction()
Unsets the value of the 'Function' attribute

void
unsetGetWaitInterval()
Unsets the value of the 'Get Wait Interval' attribute

void
unsetInputItem()
Unsets the value of the 'Input Item' attribute

void
unsetLinkType()
Unsets the value of the 'Link Type' attribute

void
unsetNextTransactionId()
Unsets the value of the 'Next Transaction Id' attribute

void
unsetOutputDataLength()
Unsets the value of the 'Output Data Length' attribute

void
unsetReason()
Unsets the value of the 'Reason' attribute

void
unsetRemoteSysId()
Unsets the value of the 'Remote Sys Id' attribute

void
unsetRemoteTransId()
Unsets the value of the 'Remote Trans Id' attribute

void
unsetReplyToFormat()
Unsets the value of the 'Reply To Format' attribute

void
unsetReserved1()
Unsets the value of the 'Reserved1' attribute

void
unsetReserved2()
Unsets the value of the 'Reserved2' attribute

void
unsetReserved3()
Unsets the value of the 'Reserved3' attribute

void
unsetReserved4()
Unsets the value of the 'Reserved4' attribute

void
unsetReturnCode()
Unsets the value of the 'Return Code' attribute

void
unsetStartCode()
Unsets the value of the 'Start Code' attribute

void
unsetTaskEndStatus()
Unsets the value of the 'Task End Status' attribute

void
unsetTransactionId()
Unsets the value of the 'Transaction Id' attribute

void
unsetUOWControl()
Unsets the value of the 'UOW Control' attribute

void
unsetVersion()
Unsets the value of the 'Version' attribute

- ============ METHOD DETAIL ==========
    - Method Detail

### Method Detail

- getProgramName
java.lang.String getProgramName()
Returns the value of the 'Program Name' attribute.
 

 If the meaning of the 'Program Name' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Program Name' attribute.See Also:setProgramName(String), 
WMQStructuresPackage.getMQCIH\_ProgramName()

- setProgramName
void setProgramName(java.lang.String value)
Sets the value of the 'Program Name' attribute.
 

Parameters:value - the new value of the 'Program Name' attribute.See Also:getProgramName()

- getVersion
int getVersion()
Returns the value of the 'Version' attribute.
 

 If the meaning of the 'Version' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Version' attribute.See Also:isSetVersion(), 
unsetVersion(), 
setVersion(int), 
WMQStructuresPackage.getMQCIH\_Version()

- setVersion
void setVersion(int value)
Sets the value of the 'Version' attribute.
 

Parameters:value - the new value of the 'Version' attribute.See Also:isSetVersion(), 
unsetVersion(), 
getVersion()

- unsetVersion
void unsetVersion()
Unsets the value of the 'Version' attribute.
 

See Also:isSetVersion(), 
getVersion(), 
setVersion(int)

- isSetVersion
boolean isSetVersion()
Returns whether the value of the 'Version' attribute is set.
 

Returns:whether the value of the 'Version' attribute is set.See Also:unsetVersion(), 
getVersion(), 
setVersion(int)

- getFlags
int getFlags()
Returns the value of the 'Flags' attribute.
 

 If the meaning of the 'Flags' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Flags' attribute.See Also:isSetFlags(), 
unsetFlags(), 
setFlags(int), 
WMQStructuresPackage.getMQCIH\_Flags()

- setFlags
void setFlags(int value)
Sets the value of the 'Flags' attribute.
 

Parameters:value - the new value of the 'Flags' attribute.See Also:isSetFlags(), 
unsetFlags(), 
getFlags()

- unsetFlags
void unsetFlags()
Unsets the value of the 'Flags' attribute.
 

See Also:isSetFlags(), 
getFlags(), 
setFlags(int)

- isSetFlags
boolean isSetFlags()
Returns whether the value of the 'Flags' attribute is set.
 

Returns:whether the value of the 'Flags' attribute is set.See Also:unsetFlags(), 
getFlags(), 
setFlags(int)

- getReturnCode
int getReturnCode()
Returns the value of the 'Return Code' attribute.
 

 If the meaning of the 'Return Code' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Return Code' attribute.See Also:isSetReturnCode(), 
unsetReturnCode(), 
setReturnCode(int), 
WMQStructuresPackage.getMQCIH\_ReturnCode()

- setReturnCode
void setReturnCode(int value)
Sets the value of the 'Return Code' attribute.
 

Parameters:value - the new value of the 'Return Code' attribute.See Also:isSetReturnCode(), 
unsetReturnCode(), 
getReturnCode()

- unsetReturnCode
void unsetReturnCode()
Unsets the value of the 'Return Code' attribute.
 

See Also:isSetReturnCode(), 
getReturnCode(), 
setReturnCode(int)

- isSetReturnCode
boolean isSetReturnCode()
Returns whether the value of the 'Return Code' attribute is set.
 

Returns:whether the value of the 'Return Code' attribute is set.See Also:unsetReturnCode(), 
getReturnCode(), 
setReturnCode(int)

- getCompCode
int getCompCode()
Returns the value of the 'Comp Code' attribute.
 

 If the meaning of the 'Comp Code' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Comp Code' attribute.See Also:isSetCompCode(), 
unsetCompCode(), 
setCompCode(int), 
WMQStructuresPackage.getMQCIH\_CompCode()

- setCompCode
void setCompCode(int value)
Sets the value of the 'Comp Code' attribute.
 

Parameters:value - the new value of the 'Comp Code' attribute.See Also:isSetCompCode(), 
unsetCompCode(), 
getCompCode()

- unsetCompCode
void unsetCompCode()
Unsets the value of the 'Comp Code' attribute.
 

See Also:isSetCompCode(), 
getCompCode(), 
setCompCode(int)

- isSetCompCode
boolean isSetCompCode()
Returns whether the value of the 'Comp Code' attribute is set.
 

Returns:whether the value of the 'Comp Code' attribute is set.See Also:unsetCompCode(), 
getCompCode(), 
setCompCode(int)

- getReason
int getReason()
Returns the value of the 'Reason' attribute.
 

 If the meaning of the 'Reason' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Reason' attribute.See Also:isSetReason(), 
unsetReason(), 
setReason(int), 
WMQStructuresPackage.getMQCIH\_Reason()

- setReason
void setReason(int value)
Sets the value of the 'Reason' attribute.
 

Parameters:value - the new value of the 'Reason' attribute.See Also:isSetReason(), 
unsetReason(), 
getReason()

- unsetReason
void unsetReason()
Unsets the value of the 'Reason' attribute.
 

See Also:isSetReason(), 
getReason(), 
setReason(int)

- isSetReason
boolean isSetReason()
Returns whether the value of the 'Reason' attribute is set.
 

Returns:whether the value of the 'Reason' attribute is set.See Also:unsetReason(), 
getReason(), 
setReason(int)

- getUOWControl
int getUOWControl()
Returns the value of the 'UOW Control' attribute.
 

 If the meaning of the 'UOW Control' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'UOW Control' attribute.See Also:isSetUOWControl(), 
unsetUOWControl(), 
setUOWControl(int), 
WMQStructuresPackage.getMQCIH\_UOWControl()

- setUOWControl
void setUOWControl(int value)
Sets the value of the 'UOW Control' attribute.
 

Parameters:value - the new value of the 'UOW Control' attribute.See Also:isSetUOWControl(), 
unsetUOWControl(), 
getUOWControl()

- unsetUOWControl
void unsetUOWControl()
Unsets the value of the 'UOW Control' attribute.
 

See Also:isSetUOWControl(), 
getUOWControl(), 
setUOWControl(int)

- isSetUOWControl
boolean isSetUOWControl()
Returns whether the value of the 'UOW Control' attribute is set.
 

Returns:whether the value of the 'UOW Control' attribute is set.See Also:unsetUOWControl(), 
getUOWControl(), 
setUOWControl(int)

- getGetWaitInterval
int getGetWaitInterval()
Returns the value of the 'Get Wait Interval' attribute.
 

 If the meaning of the 'Get Wait Interval' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Get Wait Interval' attribute.See Also:isSetGetWaitInterval(), 
unsetGetWaitInterval(), 
setGetWaitInterval(int), 
WMQStructuresPackage.getMQCIH\_GetWaitInterval()

- setGetWaitInterval
void setGetWaitInterval(int value)
Sets the value of the 'Get Wait Interval' attribute.
 

Parameters:value - the new value of the 'Get Wait Interval' attribute.See Also:isSetGetWaitInterval(), 
unsetGetWaitInterval(), 
getGetWaitInterval()

- unsetGetWaitInterval
void unsetGetWaitInterval()
Unsets the value of the 'Get Wait Interval' attribute.
 

See Also:isSetGetWaitInterval(), 
getGetWaitInterval(), 
setGetWaitInterval(int)

- isSetGetWaitInterval
boolean isSetGetWaitInterval()
Returns whether the value of the 'Get Wait Interval' attribute is set.
 

Returns:whether the value of the 'Get Wait Interval' attribute is set.See Also:unsetGetWaitInterval(), 
getGetWaitInterval(), 
setGetWaitInterval(int)

- getLinkType
int getLinkType()
Returns the value of the 'Link Type' attribute.
 

 If the meaning of the 'Link Type' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Link Type' attribute.See Also:isSetLinkType(), 
unsetLinkType(), 
setLinkType(int), 
WMQStructuresPackage.getMQCIH\_LinkType()

- setLinkType
void setLinkType(int value)
Sets the value of the 'Link Type' attribute.
 

Parameters:value - the new value of the 'Link Type' attribute.See Also:isSetLinkType(), 
unsetLinkType(), 
getLinkType()

- unsetLinkType
void unsetLinkType()
Unsets the value of the 'Link Type' attribute.
 

See Also:isSetLinkType(), 
getLinkType(), 
setLinkType(int)

- isSetLinkType
boolean isSetLinkType()
Returns whether the value of the 'Link Type' attribute is set.
 

Returns:whether the value of the 'Link Type' attribute is set.See Also:unsetLinkType(), 
getLinkType(), 
setLinkType(int)

- getOutputDataLength
int getOutputDataLength()
Returns the value of the 'Output Data Length' attribute.
 

 If the meaning of the 'Output Data Length' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Output Data Length' attribute.See Also:isSetOutputDataLength(), 
unsetOutputDataLength(), 
setOutputDataLength(int), 
WMQStructuresPackage.getMQCIH\_OutputDataLength()

- setOutputDataLength
void setOutputDataLength(int value)
Sets the value of the 'Output Data Length' attribute.
 

Parameters:value - the new value of the 'Output Data Length' attribute.See Also:isSetOutputDataLength(), 
unsetOutputDataLength(), 
getOutputDataLength()

- unsetOutputDataLength
void unsetOutputDataLength()
Unsets the value of the 'Output Data Length' attribute.
 

See Also:isSetOutputDataLength(), 
getOutputDataLength(), 
setOutputDataLength(int)

- isSetOutputDataLength
boolean isSetOutputDataLength()
Returns whether the value of the 'Output Data Length' attribute is set.
 

Returns:whether the value of the 'Output Data Length' attribute is set.See Also:unsetOutputDataLength(), 
getOutputDataLength(), 
setOutputDataLength(int)

- getFacilityKeepTime
int getFacilityKeepTime()
Returns the value of the 'Facility Keep Time' attribute.
 

 If the meaning of the 'Facility Keep Time' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Facility Keep Time' attribute.See Also:isSetFacilityKeepTime(), 
unsetFacilityKeepTime(), 
setFacilityKeepTime(int), 
WMQStructuresPackage.getMQCIH\_FacilityKeepTime()

- setFacilityKeepTime
void setFacilityKeepTime(int value)
Sets the value of the 'Facility Keep Time' attribute.
 

Parameters:value - the new value of the 'Facility Keep Time' attribute.See Also:isSetFacilityKeepTime(), 
unsetFacilityKeepTime(), 
getFacilityKeepTime()

- unsetFacilityKeepTime
void unsetFacilityKeepTime()
Unsets the value of the 'Facility Keep Time' attribute.
 

See Also:isSetFacilityKeepTime(), 
getFacilityKeepTime(), 
setFacilityKeepTime(int)

- isSetFacilityKeepTime
boolean isSetFacilityKeepTime()
Returns whether the value of the 'Facility Keep Time' attribute is set.
 

Returns:whether the value of the 'Facility Keep Time' attribute is set.See Also:unsetFacilityKeepTime(), 
getFacilityKeepTime(), 
setFacilityKeepTime(int)

- getADSDescriptor
int getADSDescriptor()
Returns the value of the 'ADS Descriptor' attribute.
 

 If the meaning of the 'ADS Descriptor' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'ADS Descriptor' attribute.See Also:isSetADSDescriptor(), 
unsetADSDescriptor(), 
setADSDescriptor(int), 
WMQStructuresPackage.getMQCIH\_ADSDescriptor()

- setADSDescriptor
void setADSDescriptor(int value)
Sets the value of the 'ADS Descriptor' attribute.
 

Parameters:value - the new value of the 'ADS Descriptor' attribute.See Also:isSetADSDescriptor(), 
unsetADSDescriptor(), 
getADSDescriptor()

- unsetADSDescriptor
void unsetADSDescriptor()
Unsets the value of the 'ADS Descriptor' attribute.
 

See Also:isSetADSDescriptor(), 
getADSDescriptor(), 
setADSDescriptor(int)

- isSetADSDescriptor
boolean isSetADSDescriptor()
Returns whether the value of the 'ADS Descriptor' attribute is set.
 

Returns:whether the value of the 'ADS Descriptor' attribute is set.See Also:unsetADSDescriptor(), 
getADSDescriptor(), 
setADSDescriptor(int)

- getConversationalTask
int getConversationalTask()
Returns the value of the 'Conversational Task' attribute.
 

 If the meaning of the 'Conversational Task' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Conversational Task' attribute.See Also:isSetConversationalTask(), 
unsetConversationalTask(), 
setConversationalTask(int), 
WMQStructuresPackage.getMQCIH\_ConversationalTask()

- setConversationalTask
void setConversationalTask(int value)
Sets the value of the 'Conversational Task' attribute.
 

Parameters:value - the new value of the 'Conversational Task' attribute.See Also:isSetConversationalTask(), 
unsetConversationalTask(), 
getConversationalTask()

- unsetConversationalTask
void unsetConversationalTask()
Unsets the value of the 'Conversational Task' attribute.
 

See Also:isSetConversationalTask(), 
getConversationalTask(), 
setConversationalTask(int)

- isSetConversationalTask
boolean isSetConversationalTask()
Returns whether the value of the 'Conversational Task' attribute is set.
 

Returns:whether the value of the 'Conversational Task' attribute is set.See Also:unsetConversationalTask(), 
getConversationalTask(), 
setConversationalTask(int)

- getTaskEndStatus
int getTaskEndStatus()
Returns the value of the 'Task End Status' attribute.
 

 If the meaning of the 'Task End Status' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Task End Status' attribute.See Also:isSetTaskEndStatus(), 
unsetTaskEndStatus(), 
setTaskEndStatus(int), 
WMQStructuresPackage.getMQCIH\_TaskEndStatus()

- setTaskEndStatus
void setTaskEndStatus(int value)
Sets the value of the 'Task End Status' attribute.
 

Parameters:value - the new value of the 'Task End Status' attribute.See Also:isSetTaskEndStatus(), 
unsetTaskEndStatus(), 
getTaskEndStatus()

- unsetTaskEndStatus
void unsetTaskEndStatus()
Unsets the value of the 'Task End Status' attribute.
 

See Also:isSetTaskEndStatus(), 
getTaskEndStatus(), 
setTaskEndStatus(int)

- isSetTaskEndStatus
boolean isSetTaskEndStatus()
Returns whether the value of the 'Task End Status' attribute is set.
 

Returns:whether the value of the 'Task End Status' attribute is set.See Also:unsetTaskEndStatus(), 
getTaskEndStatus(), 
setTaskEndStatus(int)

- getFacility
byte[] getFacility()
Returns the value of the 'Facility' attribute.
 

 If the meaning of the 'Facility' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Facility' attribute.See Also:setFacility(byte[]), 
WMQStructuresPackage.getMQCIH\_Facility()

- setFacility
void setFacility(byte[] value)
Sets the value of the 'Facility' attribute.
 

Parameters:value - the new value of the 'Facility' attribute.See Also:getFacility()

- getFunction
java.lang.String getFunction()
Returns the value of the 'Function' attribute.
 The default value is "".
 

 If the meaning of the 'Function' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Function' attribute.See Also:isSetFunction(), 
unsetFunction(), 
setFunction(String), 
WMQStructuresPackage.getMQCIH\_Function()

- setFunction
void setFunction(java.lang.String value)
Sets the value of the 'Function' attribute.
 

Parameters:value - the new value of the 'Function' attribute.See Also:isSetFunction(), 
unsetFunction(), 
getFunction()

- unsetFunction
void unsetFunction()
Unsets the value of the 'Function' attribute.
 

See Also:isSetFunction(), 
getFunction(), 
setFunction(String)

- isSetFunction
boolean isSetFunction()
Returns whether the value of the 'Function' attribute is set.
 

Returns:whether the value of the 'Function' attribute is set.See Also:unsetFunction(), 
getFunction(), 
setFunction(String)

- getAbendCode
java.lang.String getAbendCode()
Returns the value of the 'Abend Code' attribute.
 The default value is "".
 

 If the meaning of the 'Abend Code' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Abend Code' attribute.See Also:isSetAbendCode(), 
unsetAbendCode(), 
setAbendCode(String), 
WMQStructuresPackage.getMQCIH\_AbendCode()

- setAbendCode
void setAbendCode(java.lang.String value)
Sets the value of the 'Abend Code' attribute.
 

Parameters:value - the new value of the 'Abend Code' attribute.See Also:isSetAbendCode(), 
unsetAbendCode(), 
getAbendCode()

- unsetAbendCode
void unsetAbendCode()
Unsets the value of the 'Abend Code' attribute.
 

See Also:isSetAbendCode(), 
getAbendCode(), 
setAbendCode(String)

- isSetAbendCode
boolean isSetAbendCode()
Returns whether the value of the 'Abend Code' attribute is set.
 

Returns:whether the value of the 'Abend Code' attribute is set.See Also:unsetAbendCode(), 
getAbendCode(), 
setAbendCode(String)

- getAuthenticator
java.lang.String getAuthenticator()
Returns the value of the 'Authenticator' attribute.
 The default value is "".
 

 If the meaning of the 'Authenticator' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Authenticator' attribute.See Also:isSetAuthenticator(), 
unsetAuthenticator(), 
setAuthenticator(String), 
WMQStructuresPackage.getMQCIH\_Authenticator()

- setAuthenticator
void setAuthenticator(java.lang.String value)
Sets the value of the 'Authenticator' attribute.
 

Parameters:value - the new value of the 'Authenticator' attribute.See Also:isSetAuthenticator(), 
unsetAuthenticator(), 
getAuthenticator()

- unsetAuthenticator
void unsetAuthenticator()
Unsets the value of the 'Authenticator' attribute.
 

See Also:isSetAuthenticator(), 
getAuthenticator(), 
setAuthenticator(String)

- isSetAuthenticator
boolean isSetAuthenticator()
Returns whether the value of the 'Authenticator' attribute is set.
 

Returns:whether the value of the 'Authenticator' attribute is set.See Also:unsetAuthenticator(), 
getAuthenticator(), 
setAuthenticator(String)

- getReserved1
java.lang.String getReserved1()
Returns the value of the 'Reserved1' attribute.
 The default value is "".
 

 If the meaning of the 'Reserved1' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Reserved1' attribute.See Also:isSetReserved1(), 
unsetReserved1(), 
setReserved1(String), 
WMQStructuresPackage.getMQCIH\_Reserved1()

- setReserved1
void setReserved1(java.lang.String value)
Sets the value of the 'Reserved1' attribute.
 

Parameters:value - the new value of the 'Reserved1' attribute.See Also:isSetReserved1(), 
unsetReserved1(), 
getReserved1()

- unsetReserved1
void unsetReserved1()
Unsets the value of the 'Reserved1' attribute.
 

See Also:isSetReserved1(), 
getReserved1(), 
setReserved1(String)

- isSetReserved1
boolean isSetReserved1()
Returns whether the value of the 'Reserved1' attribute is set.
 

Returns:whether the value of the 'Reserved1' attribute is set.See Also:unsetReserved1(), 
getReserved1(), 
setReserved1(String)

- getReplyToFormat
java.lang.String getReplyToFormat()
Returns the value of the 'Reply To Format' attribute.
 The default value is "".
 

 If the meaning of the 'Reply To Format' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Reply To Format' attribute.See Also:isSetReplyToFormat(), 
unsetReplyToFormat(), 
setReplyToFormat(String), 
WMQStructuresPackage.getMQCIH\_ReplyToFormat()

- setReplyToFormat
void setReplyToFormat(java.lang.String value)
Sets the value of the 'Reply To Format' attribute.
 

Parameters:value - the new value of the 'Reply To Format' attribute.See Also:isSetReplyToFormat(), 
unsetReplyToFormat(), 
getReplyToFormat()

- unsetReplyToFormat
void unsetReplyToFormat()
Unsets the value of the 'Reply To Format' attribute.
 

See Also:isSetReplyToFormat(), 
getReplyToFormat(), 
setReplyToFormat(String)

- isSetReplyToFormat
boolean isSetReplyToFormat()
Returns whether the value of the 'Reply To Format' attribute is set.
 

Returns:whether the value of the 'Reply To Format' attribute is set.See Also:unsetReplyToFormat(), 
getReplyToFormat(), 
setReplyToFormat(String)

- getRemoteSysId
java.lang.String getRemoteSysId()
Returns the value of the 'Remote Sys Id' attribute.
 The default value is "".
 

 If the meaning of the 'Remote Sys Id' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Remote Sys Id' attribute.See Also:isSetRemoteSysId(), 
unsetRemoteSysId(), 
setRemoteSysId(String), 
WMQStructuresPackage.getMQCIH\_RemoteSysId()

- setRemoteSysId
void setRemoteSysId(java.lang.String value)
Sets the value of the 'Remote Sys Id' attribute.
 

Parameters:value - the new value of the 'Remote Sys Id' attribute.See Also:isSetRemoteSysId(), 
unsetRemoteSysId(), 
getRemoteSysId()

- unsetRemoteSysId
void unsetRemoteSysId()
Unsets the value of the 'Remote Sys Id' attribute.
 

See Also:isSetRemoteSysId(), 
getRemoteSysId(), 
setRemoteSysId(String)

- isSetRemoteSysId
boolean isSetRemoteSysId()
Returns whether the value of the 'Remote Sys Id' attribute is set.
 

Returns:whether the value of the 'Remote Sys Id' attribute is set.See Also:unsetRemoteSysId(), 
getRemoteSysId(), 
setRemoteSysId(String)

- getRemoteTransId
java.lang.String getRemoteTransId()
Returns the value of the 'Remote Trans Id' attribute.
 The default value is "".
 

 If the meaning of the 'Remote Trans Id' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Remote Trans Id' attribute.See Also:isSetRemoteTransId(), 
unsetRemoteTransId(), 
setRemoteTransId(String), 
WMQStructuresPackage.getMQCIH\_RemoteTransId()

- setRemoteTransId
void setRemoteTransId(java.lang.String value)
Sets the value of the 'Remote Trans Id' attribute.
 

Parameters:value - the new value of the 'Remote Trans Id' attribute.See Also:isSetRemoteTransId(), 
unsetRemoteTransId(), 
getRemoteTransId()

- unsetRemoteTransId
void unsetRemoteTransId()
Unsets the value of the 'Remote Trans Id' attribute.
 

See Also:isSetRemoteTransId(), 
getRemoteTransId(), 
setRemoteTransId(String)

- isSetRemoteTransId
boolean isSetRemoteTransId()
Returns whether the value of the 'Remote Trans Id' attribute is set.
 

Returns:whether the value of the 'Remote Trans Id' attribute is set.See Also:unsetRemoteTransId(), 
getRemoteTransId(), 
setRemoteTransId(String)

- getTransactionId
java.lang.String getTransactionId()
Returns the value of the 'Transaction Id' attribute.
 The default value is "".
 

 If the meaning of the 'Transaction Id' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Transaction Id' attribute.See Also:isSetTransactionId(), 
unsetTransactionId(), 
setTransactionId(String), 
WMQStructuresPackage.getMQCIH\_TransactionId()

- setTransactionId
void setTransactionId(java.lang.String value)
Sets the value of the 'Transaction Id' attribute.
 

Parameters:value - the new value of the 'Transaction Id' attribute.See Also:isSetTransactionId(), 
unsetTransactionId(), 
getTransactionId()

- unsetTransactionId
void unsetTransactionId()
Unsets the value of the 'Transaction Id' attribute.
 

See Also:isSetTransactionId(), 
getTransactionId(), 
setTransactionId(String)

- isSetTransactionId
boolean isSetTransactionId()
Returns whether the value of the 'Transaction Id' attribute is set.
 

Returns:whether the value of the 'Transaction Id' attribute is set.See Also:unsetTransactionId(), 
getTransactionId(), 
setTransactionId(String)

- getFacilityLike
java.lang.String getFacilityLike()
Returns the value of the 'Facility Like' attribute.
 The default value is "".
 

 If the meaning of the 'Facility Like' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Facility Like' attribute.See Also:isSetFacilityLike(), 
unsetFacilityLike(), 
setFacilityLike(String), 
WMQStructuresPackage.getMQCIH\_FacilityLike()

- setFacilityLike
void setFacilityLike(java.lang.String value)
Sets the value of the 'Facility Like' attribute.
 

Parameters:value - the new value of the 'Facility Like' attribute.See Also:isSetFacilityLike(), 
unsetFacilityLike(), 
getFacilityLike()

- unsetFacilityLike
void unsetFacilityLike()
Unsets the value of the 'Facility Like' attribute.
 

See Also:isSetFacilityLike(), 
getFacilityLike(), 
setFacilityLike(String)

- isSetFacilityLike
boolean isSetFacilityLike()
Returns whether the value of the 'Facility Like' attribute is set.
 

Returns:whether the value of the 'Facility Like' attribute is set.See Also:unsetFacilityLike(), 
getFacilityLike(), 
setFacilityLike(String)

- getAttentionId
java.lang.String getAttentionId()
Returns the value of the 'Attention Id' attribute.
 The default value is "".
 

 If the meaning of the 'Attention Id' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Attention Id' attribute.See Also:isSetAttentionId(), 
unsetAttentionId(), 
setAttentionId(String), 
WMQStructuresPackage.getMQCIH\_AttentionId()

- setAttentionId
void setAttentionId(java.lang.String value)
Sets the value of the 'Attention Id' attribute.
 

Parameters:value - the new value of the 'Attention Id' attribute.See Also:isSetAttentionId(), 
unsetAttentionId(), 
getAttentionId()

- unsetAttentionId
void unsetAttentionId()
Unsets the value of the 'Attention Id' attribute.
 

See Also:isSetAttentionId(), 
getAttentionId(), 
setAttentionId(String)

- isSetAttentionId
boolean isSetAttentionId()
Returns whether the value of the 'Attention Id' attribute is set.
 

Returns:whether the value of the 'Attention Id' attribute is set.See Also:unsetAttentionId(), 
getAttentionId(), 
setAttentionId(String)

- getStartCode
java.lang.String getStartCode()
Returns the value of the 'Start Code' attribute.
 The default value is "".
 

 If the meaning of the 'Start Code' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Start Code' attribute.See Also:isSetStartCode(), 
unsetStartCode(), 
setStartCode(String), 
WMQStructuresPackage.getMQCIH\_StartCode()

- setStartCode
void setStartCode(java.lang.String value)
Sets the value of the 'Start Code' attribute.
 

Parameters:value - the new value of the 'Start Code' attribute.See Also:isSetStartCode(), 
unsetStartCode(), 
getStartCode()

- unsetStartCode
void unsetStartCode()
Unsets the value of the 'Start Code' attribute.
 

See Also:isSetStartCode(), 
getStartCode(), 
setStartCode(String)

- isSetStartCode
boolean isSetStartCode()
Returns whether the value of the 'Start Code' attribute is set.
 

Returns:whether the value of the 'Start Code' attribute is set.See Also:unsetStartCode(), 
getStartCode(), 
setStartCode(String)

- getCancelCode
java.lang.String getCancelCode()
Returns the value of the 'Cancel Code' attribute.
 The default value is "".
 

 If the meaning of the 'Cancel Code' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Cancel Code' attribute.See Also:isSetCancelCode(), 
unsetCancelCode(), 
setCancelCode(String), 
WMQStructuresPackage.getMQCIH\_CancelCode()

- setCancelCode
void setCancelCode(java.lang.String value)
Sets the value of the 'Cancel Code' attribute.
 

Parameters:value - the new value of the 'Cancel Code' attribute.See Also:isSetCancelCode(), 
unsetCancelCode(), 
getCancelCode()

- unsetCancelCode
void unsetCancelCode()
Unsets the value of the 'Cancel Code' attribute.
 

See Also:isSetCancelCode(), 
getCancelCode(), 
setCancelCode(String)

- isSetCancelCode
boolean isSetCancelCode()
Returns whether the value of the 'Cancel Code' attribute is set.
 

Returns:whether the value of the 'Cancel Code' attribute is set.See Also:unsetCancelCode(), 
getCancelCode(), 
setCancelCode(String)

- getNextTransactionId
java.lang.String getNextTransactionId()
Returns the value of the 'Next Transaction Id' attribute.
 The default value is "".
 

 If the meaning of the 'Next Transaction Id' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Next Transaction Id' attribute.See Also:isSetNextTransactionId(), 
unsetNextTransactionId(), 
setNextTransactionId(String), 
WMQStructuresPackage.getMQCIH\_NextTransactionId()

- setNextTransactionId
void setNextTransactionId(java.lang.String value)
Sets the value of the 'Next Transaction Id' attribute.
 

Parameters:value - the new value of the 'Next Transaction Id' attribute.See Also:isSetNextTransactionId(), 
unsetNextTransactionId(), 
getNextTransactionId()

- unsetNextTransactionId
void unsetNextTransactionId()
Unsets the value of the 'Next Transaction Id' attribute.
 

See Also:isSetNextTransactionId(), 
getNextTransactionId(), 
setNextTransactionId(String)

- isSetNextTransactionId
boolean isSetNextTransactionId()
Returns whether the value of the 'Next Transaction Id' attribute is set.
 

Returns:whether the value of the 'Next Transaction Id' attribute is set.See Also:unsetNextTransactionId(), 
getNextTransactionId(), 
setNextTransactionId(String)

- getReserved2
java.lang.String getReserved2()
Returns the value of the 'Reserved2' attribute.
 The default value is "".
 

 If the meaning of the 'Reserved2' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Reserved2' attribute.See Also:isSetReserved2(), 
unsetReserved2(), 
setReserved2(String), 
WMQStructuresPackage.getMQCIH\_Reserved2()

- setReserved2
void setReserved2(java.lang.String value)
Sets the value of the 'Reserved2' attribute.
 

Parameters:value - the new value of the 'Reserved2' attribute.See Also:isSetReserved2(), 
unsetReserved2(), 
getReserved2()

- unsetReserved2
void unsetReserved2()
Unsets the value of the 'Reserved2' attribute.
 

See Also:isSetReserved2(), 
getReserved2(), 
setReserved2(String)

- isSetReserved2
boolean isSetReserved2()
Returns whether the value of the 'Reserved2' attribute is set.
 

Returns:whether the value of the 'Reserved2' attribute is set.See Also:unsetReserved2(), 
getReserved2(), 
setReserved2(String)

- getReserved3
java.lang.String getReserved3()
Returns the value of the 'Reserved3' attribute.
 The default value is "".
 

 If the meaning of the 'Reserved3' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Reserved3' attribute.See Also:isSetReserved3(), 
unsetReserved3(), 
setReserved3(String), 
WMQStructuresPackage.getMQCIH\_Reserved3()

- setReserved3
void setReserved3(java.lang.String value)
Sets the value of the 'Reserved3' attribute.
 

Parameters:value - the new value of the 'Reserved3' attribute.See Also:isSetReserved3(), 
unsetReserved3(), 
getReserved3()

- unsetReserved3
void unsetReserved3()
Unsets the value of the 'Reserved3' attribute.
 

See Also:isSetReserved3(), 
getReserved3(), 
setReserved3(String)

- isSetReserved3
boolean isSetReserved3()
Returns whether the value of the 'Reserved3' attribute is set.
 

Returns:whether the value of the 'Reserved3' attribute is set.See Also:unsetReserved3(), 
getReserved3(), 
setReserved3(String)

- getCursorPosition
int getCursorPosition()
Returns the value of the 'Cursor Position' attribute.
 

 If the meaning of the 'Cursor Position' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Cursor Position' attribute.See Also:isSetCursorPosition(), 
unsetCursorPosition(), 
setCursorPosition(int), 
WMQStructuresPackage.getMQCIH\_CursorPosition()

- setCursorPosition
void setCursorPosition(int value)
Sets the value of the 'Cursor Position' attribute.
 

Parameters:value - the new value of the 'Cursor Position' attribute.See Also:isSetCursorPosition(), 
unsetCursorPosition(), 
getCursorPosition()

- unsetCursorPosition
void unsetCursorPosition()
Unsets the value of the 'Cursor Position' attribute.
 

See Also:isSetCursorPosition(), 
getCursorPosition(), 
setCursorPosition(int)

- isSetCursorPosition
boolean isSetCursorPosition()
Returns whether the value of the 'Cursor Position' attribute is set.
 

Returns:whether the value of the 'Cursor Position' attribute is set.See Also:unsetCursorPosition(), 
getCursorPosition(), 
setCursorPosition(int)

- getErrorOffset
int getErrorOffset()
Returns the value of the 'Error Offset' attribute.
 

 If the meaning of the 'Error Offset' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Error Offset' attribute.See Also:isSetErrorOffset(), 
unsetErrorOffset(), 
setErrorOffset(int), 
WMQStructuresPackage.getMQCIH\_ErrorOffset()

- setErrorOffset
void setErrorOffset(int value)
Sets the value of the 'Error Offset' attribute.
 

Parameters:value - the new value of the 'Error Offset' attribute.See Also:isSetErrorOffset(), 
unsetErrorOffset(), 
getErrorOffset()

- unsetErrorOffset
void unsetErrorOffset()
Unsets the value of the 'Error Offset' attribute.
 

See Also:isSetErrorOffset(), 
getErrorOffset(), 
setErrorOffset(int)

- isSetErrorOffset
boolean isSetErrorOffset()
Returns whether the value of the 'Error Offset' attribute is set.
 

Returns:whether the value of the 'Error Offset' attribute is set.See Also:unsetErrorOffset(), 
getErrorOffset(), 
setErrorOffset(int)

- getInputItem
int getInputItem()
Returns the value of the 'Input Item' attribute.
 

 If the meaning of the 'Input Item' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Input Item' attribute.See Also:isSetInputItem(), 
unsetInputItem(), 
setInputItem(int), 
WMQStructuresPackage.getMQCIH\_InputItem()

- setInputItem
void setInputItem(int value)
Sets the value of the 'Input Item' attribute.
 

Parameters:value - the new value of the 'Input Item' attribute.See Also:isSetInputItem(), 
unsetInputItem(), 
getInputItem()

- unsetInputItem
void unsetInputItem()
Unsets the value of the 'Input Item' attribute.
 

See Also:isSetInputItem(), 
getInputItem(), 
setInputItem(int)

- isSetInputItem
boolean isSetInputItem()
Returns whether the value of the 'Input Item' attribute is set.
 

Returns:whether the value of the 'Input Item' attribute is set.See Also:unsetInputItem(), 
getInputItem(), 
setInputItem(int)

- getReserved4
int getReserved4()
Returns the value of the 'Reserved4' attribute.
 

 If the meaning of the 'Reserved4' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Reserved4' attribute.See Also:isSetReserved4(), 
unsetReserved4(), 
setReserved4(int), 
WMQStructuresPackage.getMQCIH\_Reserved4()

- setReserved4
void setReserved4(int value)
Sets the value of the 'Reserved4' attribute.
 

Parameters:value - the new value of the 'Reserved4' attribute.See Also:isSetReserved4(), 
unsetReserved4(), 
getReserved4()

- unsetReserved4
void unsetReserved4()
Unsets the value of the 'Reserved4' attribute.
 

See Also:isSetReserved4(), 
getReserved4(), 
setReserved4(int)

- isSetReserved4
boolean isSetReserved4()
Returns whether the value of the 'Reserved4' attribute is set.
 

Returns:whether the value of the 'Reserved4' attribute is set.See Also:unsetReserved4(), 
getReserved4(), 
setReserved4(int)