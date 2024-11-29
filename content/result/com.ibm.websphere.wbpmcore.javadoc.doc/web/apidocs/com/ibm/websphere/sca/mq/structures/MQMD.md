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

## Interface MQMD

- public interface MQMD begin-user-doc A representation of the model object 'MQMD '. end-user-doc The following features are supported: See Also: WMQStructuresPackage.getMQMD()

```
public interface MQMD
```

The following features are supported:
 
Report
Msg Type
Expiry
Feedback
Priority
Persistence
Msg Id
Correl Id
Backout Count
Reply To Q
Reply To QMgr
User Identifier
Accounting Token
Appl Identity Data
Put Appl Type
Put Appl Name
Put Date
Put Time
Appl Origin Data
Group Id
Msg Seq Number
Offset
Msg Flags
Original Length

- ========== METHOD SUMMARY ===========
    - Method Summary

Methods 

Modifier and Type
Method and Description

byte[]
getAccountingToken()
Returns the value of the 'Accounting Token' attribute

java.lang.String
getApplIdentityData()
Returns the value of the 'Appl Identity Data' attribute

java.lang.String
getApplOriginData()
Returns the value of the 'Appl Origin Data' attribute

int
getBackoutCount()
Returns the value of the 'Backout Count' attribute

byte[]
getCorrelId()
Returns the value of the 'Correl Id' attribute

int
getExpiry()
Returns the value of the 'Expiry' attribute

int
getFeedback()
Returns the value of the 'Feedback' attribute

byte[]
getGroupId()
Returns the value of the 'Group Id' attribute

int
getMsgFlags()
Returns the value of the 'Msg Flags' attribute

byte[]
getMsgId()
Returns the value of the 'Msg Id' attribute

int
getMsgSeqNumber()
Returns the value of the 'Msg Seq Number' attribute

int
getMsgType()
Returns the value of the 'Msg Type' attribute

int
getOffset()
Returns the value of the 'Offset' attribute

int
getOriginalLength()
Returns the value of the 'Original Length' attribute

int
getPersistence()
Returns the value of the 'Persistence' attribute

int
getPriority()
Returns the value of the 'Priority' attribute

java.lang.String
getPutApplName()
Returns the value of the 'Put Appl Name' attribute

int
getPutApplType()
Returns the value of the 'Put Appl Type' attribute

java.lang.String
getPutDate()
Returns the value of the 'Put Date' attribute

java.lang.String
getPutTime()
Returns the value of the 'Put Time' attribute

java.lang.String
getReplyToQ()
Returns the value of the 'Reply To Q' attribute

java.lang.String
getReplyToQMgr()
Returns the value of the 'Reply To QMgr' attribute

int
getReport()
Returns the value of the 'Report' attribute

java.lang.String
getUserIdentifier()
Returns the value of the 'User Identifier' attribute

boolean
isSetBackoutCount()
Returns whether the value of the 'Backout Count' attribute is set

boolean
isSetExpiry()
Returns whether the value of the 'Expiry' attribute is set

boolean
isSetFeedback()
Returns whether the value of the 'Feedback' attribute is set

boolean
isSetMsgFlags()
Returns whether the value of the 'Msg Flags' attribute is set

boolean
isSetMsgSeqNumber()
Returns whether the value of the 'Msg Seq Number' attribute is set

boolean
isSetMsgType()
Returns whether the value of the 'Msg Type' attribute is set

boolean
isSetOffset()
Returns whether the value of the 'Offset' attribute is set

boolean
isSetOriginalLength()
Returns whether the value of the 'Original Length' attribute is set

boolean
isSetPersistence()
Returns whether the value of the 'Persistence' attribute is set

boolean
isSetPriority()
Returns whether the value of the 'Priority' attribute is set

boolean
isSetPutApplType()
Returns whether the value of the 'Put Appl Type' attribute is set

boolean
isSetReport()
Returns whether the value of the 'Report' attribute is set

void
setAccountingToken(byte[] value)
Sets the value of the 'Accounting Token' attribute

void
setApplIdentityData(java.lang.String value)
Sets the value of the 'Appl Identity Data' attribute

void
setApplOriginData(java.lang.String value)
Sets the value of the 'Appl Origin Data' attribute

void
setBackoutCount(int value)
Sets the value of the 'Backout Count' attribute

void
setCorrelId(byte[] value)
Sets the value of the 'Correl Id' attribute

void
setExpiry(int value)
Sets the value of the 'Expiry' attribute

void
setFeedback(int value)
Sets the value of the 'Feedback' attribute

void
setGroupId(byte[] value)
Sets the value of the 'Group Id' attribute

void
setMsgFlags(int value)
Sets the value of the 'Msg Flags' attribute

void
setMsgId(byte[] value)
Sets the value of the 'Msg Id' attribute

void
setMsgSeqNumber(int value)
Sets the value of the 'Msg Seq Number' attribute

void
setMsgType(int value)
Sets the value of the 'Msg Type' attribute

void
setOffset(int value)
Sets the value of the 'Offset' attribute

void
setOriginalLength(int value)
Sets the value of the 'Original Length' attribute

void
setPersistence(int value)
Sets the value of the 'Persistence' attribute

void
setPriority(int value)
Sets the value of the 'Priority' attribute

void
setPutApplName(java.lang.String value)
Sets the value of the 'Put Appl Name' attribute

void
setPutApplType(int value)
Sets the value of the 'Put Appl Type' attribute

void
setPutDate(java.lang.String value)
Sets the value of the 'Put Date' attribute

void
setPutTime(java.lang.String value)
Sets the value of the 'Put Time' attribute

void
setReplyToQ(java.lang.String value)
Sets the value of the 'Reply To Q' attribute

void
setReplyToQMgr(java.lang.String value)
Sets the value of the 'Reply To QMgr' attribute

void
setReport(int value)
Sets the value of the 'Report' attribute

void
setUserIdentifier(java.lang.String value)
Sets the value of the 'User Identifier' attribute

void
unsetBackoutCount()
Unsets the value of the 'Backout Count' attribute

void
unsetExpiry()
Unsets the value of the 'Expiry' attribute

void
unsetFeedback()
Unsets the value of the 'Feedback' attribute

void
unsetMsgFlags()
Unsets the value of the 'Msg Flags' attribute

void
unsetMsgSeqNumber()
Unsets the value of the 'Msg Seq Number' attribute

void
unsetMsgType()
Unsets the value of the 'Msg Type' attribute

void
unsetOffset()
Unsets the value of the 'Offset' attribute

void
unsetOriginalLength()
Unsets the value of the 'Original Length' attribute

void
unsetPersistence()
Unsets the value of the 'Persistence' attribute

void
unsetPriority()
Unsets the value of the 'Priority' attribute

void
unsetPutApplType()
Unsets the value of the 'Put Appl Type' attribute

void
unsetReport()
Unsets the value of the 'Report' attribute

- ============ METHOD DETAIL ==========
    - Method Detail

### Method Detail

- getReport
int getReport()
Returns the value of the 'Report' attribute.
 

 If the meaning of the 'Report' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Report' attribute.See Also:isSetReport(), 
unsetReport(), 
setReport(int), 
WMQStructuresPackage.getMQMD\_Report()

- setReport
void setReport(int value)
Sets the value of the 'Report' attribute.
 

Parameters:value - the new value of the 'Report' attribute.See Also:isSetReport(), 
unsetReport(), 
getReport()

- unsetReport
void unsetReport()
Unsets the value of the 'Report' attribute.
 

See Also:isSetReport(), 
getReport(), 
setReport(int)

- isSetReport
boolean isSetReport()
Returns whether the value of the 'Report' attribute is set.
 

Returns:whether the value of the 'Report' attribute is set.See Also:unsetReport(), 
getReport(), 
setReport(int)

- getMsgType
int getMsgType()
Returns the value of the 'Msg Type' attribute.
 

 If the meaning of the 'Msg Type' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Msg Type' attribute.See Also:isSetMsgType(), 
unsetMsgType(), 
setMsgType(int), 
WMQStructuresPackage.getMQMD\_MsgType()

- setMsgType
void setMsgType(int value)
Sets the value of the 'Msg Type' attribute.
 

Parameters:value - the new value of the 'Msg Type' attribute.See Also:isSetMsgType(), 
unsetMsgType(), 
getMsgType()

- unsetMsgType
void unsetMsgType()
Unsets the value of the 'Msg Type' attribute.
 

See Also:isSetMsgType(), 
getMsgType(), 
setMsgType(int)

- isSetMsgType
boolean isSetMsgType()
Returns whether the value of the 'Msg Type' attribute is set.
 

Returns:whether the value of the 'Msg Type' attribute is set.See Also:unsetMsgType(), 
getMsgType(), 
setMsgType(int)

- getExpiry
int getExpiry()
Returns the value of the 'Expiry' attribute.
 

 If the meaning of the 'Expiry' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Expiry' attribute.See Also:isSetExpiry(), 
unsetExpiry(), 
setExpiry(int), 
WMQStructuresPackage.getMQMD\_Expiry()

- setExpiry
void setExpiry(int value)
Sets the value of the 'Expiry' attribute.
 

Parameters:value - the new value of the 'Expiry' attribute.See Also:isSetExpiry(), 
unsetExpiry(), 
getExpiry()

- unsetExpiry
void unsetExpiry()
Unsets the value of the 'Expiry' attribute.
 

See Also:isSetExpiry(), 
getExpiry(), 
setExpiry(int)

- isSetExpiry
boolean isSetExpiry()
Returns whether the value of the 'Expiry' attribute is set.
 

Returns:whether the value of the 'Expiry' attribute is set.See Also:unsetExpiry(), 
getExpiry(), 
setExpiry(int)

- getFeedback
int getFeedback()
Returns the value of the 'Feedback' attribute.
 

 If the meaning of the 'Feedback' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Feedback' attribute.See Also:isSetFeedback(), 
unsetFeedback(), 
setFeedback(int), 
WMQStructuresPackage.getMQMD\_Feedback()

- setFeedback
void setFeedback(int value)
Sets the value of the 'Feedback' attribute.
 

Parameters:value - the new value of the 'Feedback' attribute.See Also:isSetFeedback(), 
unsetFeedback(), 
getFeedback()

- unsetFeedback
void unsetFeedback()
Unsets the value of the 'Feedback' attribute.
 

See Also:isSetFeedback(), 
getFeedback(), 
setFeedback(int)

- isSetFeedback
boolean isSetFeedback()
Returns whether the value of the 'Feedback' attribute is set.
 

Returns:whether the value of the 'Feedback' attribute is set.See Also:unsetFeedback(), 
getFeedback(), 
setFeedback(int)

- getPriority
int getPriority()
Returns the value of the 'Priority' attribute.
 

 If the meaning of the 'Priority' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Priority' attribute.See Also:isSetPriority(), 
unsetPriority(), 
setPriority(int), 
WMQStructuresPackage.getMQMD\_Priority()

- setPriority
void setPriority(int value)
Sets the value of the 'Priority' attribute.
 

Parameters:value - the new value of the 'Priority' attribute.See Also:isSetPriority(), 
unsetPriority(), 
getPriority()

- unsetPriority
void unsetPriority()
Unsets the value of the 'Priority' attribute.
 

See Also:isSetPriority(), 
getPriority(), 
setPriority(int)

- isSetPriority
boolean isSetPriority()
Returns whether the value of the 'Priority' attribute is set.
 

Returns:whether the value of the 'Priority' attribute is set.See Also:unsetPriority(), 
getPriority(), 
setPriority(int)

- getPersistence
int getPersistence()
Returns the value of the 'Persistence' attribute.
 

 If the meaning of the 'Persistence' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Persistence' attribute.See Also:isSetPersistence(), 
unsetPersistence(), 
setPersistence(int), 
WMQStructuresPackage.getMQMD\_Persistence()

- setPersistence
void setPersistence(int value)
Sets the value of the 'Persistence' attribute.
 

Parameters:value - the new value of the 'Persistence' attribute.See Also:isSetPersistence(), 
unsetPersistence(), 
getPersistence()

- unsetPersistence
void unsetPersistence()
Unsets the value of the 'Persistence' attribute.
 

See Also:isSetPersistence(), 
getPersistence(), 
setPersistence(int)

- isSetPersistence
boolean isSetPersistence()
Returns whether the value of the 'Persistence' attribute is set.
 

Returns:whether the value of the 'Persistence' attribute is set.See Also:unsetPersistence(), 
getPersistence(), 
setPersistence(int)

- getMsgId
byte[] getMsgId()
Returns the value of the 'Msg Id' attribute.
 

 If the meaning of the 'Msg Id' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Msg Id' attribute.See Also:setMsgId(byte[]), 
WMQStructuresPackage.getMQMD\_MsgId()

- setMsgId
void setMsgId(byte[] value)
Sets the value of the 'Msg Id' attribute.
 

Parameters:value - the new value of the 'Msg Id' attribute.See Also:getMsgId()

- getCorrelId
byte[] getCorrelId()
Returns the value of the 'Correl Id' attribute.
 

 If the meaning of the 'Correl Id' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Correl Id' attribute.See Also:setCorrelId(byte[]), 
WMQStructuresPackage.getMQMD\_CorrelId()

- setCorrelId
void setCorrelId(byte[] value)
Sets the value of the 'Correl Id' attribute.
 

Parameters:value - the new value of the 'Correl Id' attribute.See Also:getCorrelId()

- getBackoutCount
int getBackoutCount()
Returns the value of the 'Backout Count' attribute.
 

 If the meaning of the 'Backout Count' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Backout Count' attribute.See Also:isSetBackoutCount(), 
unsetBackoutCount(), 
setBackoutCount(int), 
WMQStructuresPackage.getMQMD\_BackoutCount()

- setBackoutCount
void setBackoutCount(int value)
Sets the value of the 'Backout Count' attribute.
 

Parameters:value - the new value of the 'Backout Count' attribute.See Also:isSetBackoutCount(), 
unsetBackoutCount(), 
getBackoutCount()

- unsetBackoutCount
void unsetBackoutCount()
Unsets the value of the 'Backout Count' attribute.
 

See Also:isSetBackoutCount(), 
getBackoutCount(), 
setBackoutCount(int)

- isSetBackoutCount
boolean isSetBackoutCount()
Returns whether the value of the 'Backout Count' attribute is set.
 

Returns:whether the value of the 'Backout Count' attribute is set.See Also:unsetBackoutCount(), 
getBackoutCount(), 
setBackoutCount(int)

- getReplyToQ
java.lang.String getReplyToQ()
Returns the value of the 'Reply To Q' attribute.
 

 If the meaning of the 'Reply To Q' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Reply To Q' attribute.See Also:setReplyToQ(String), 
WMQStructuresPackage.getMQMD\_ReplyToQ()

- setReplyToQ
void setReplyToQ(java.lang.String value)
Sets the value of the 'Reply To Q' attribute.
 

Parameters:value - the new value of the 'Reply To Q' attribute.See Also:getReplyToQ()

- getReplyToQMgr
java.lang.String getReplyToQMgr()
Returns the value of the 'Reply To QMgr' attribute.
 

 If the meaning of the 'Reply To QMgr' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Reply To QMgr' attribute.See Also:setReplyToQMgr(String), 
WMQStructuresPackage.getMQMD\_ReplyToQMgr()

- setReplyToQMgr
void setReplyToQMgr(java.lang.String value)
Sets the value of the 'Reply To QMgr' attribute.
 

Parameters:value - the new value of the 'Reply To QMgr' attribute.See Also:getReplyToQMgr()

- getUserIdentifier
java.lang.String getUserIdentifier()
Returns the value of the 'User Identifier' attribute.
 

 If the meaning of the 'User Identifier' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'User Identifier' attribute.See Also:setUserIdentifier(String), 
WMQStructuresPackage.getMQMD\_UserIdentifier()

- setUserIdentifier
void setUserIdentifier(java.lang.String value)
Sets the value of the 'User Identifier' attribute.
 

Parameters:value - the new value of the 'User Identifier' attribute.See Also:getUserIdentifier()

- getAccountingToken
byte[] getAccountingToken()
Returns the value of the 'Accounting Token' attribute.
 

 If the meaning of the 'Accounting Token' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Accounting Token' attribute.See Also:setAccountingToken(byte[]), 
WMQStructuresPackage.getMQMD\_AccountingToken()

- setAccountingToken
void setAccountingToken(byte[] value)
Sets the value of the 'Accounting Token' attribute.
 

Parameters:value - the new value of the 'Accounting Token' attribute.See Also:getAccountingToken()

- getApplIdentityData
java.lang.String getApplIdentityData()
Returns the value of the 'Appl Identity Data' attribute.
 

 If the meaning of the 'Appl Identity Data' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Appl Identity Data' attribute.See Also:setApplIdentityData(String), 
WMQStructuresPackage.getMQMD\_ApplIdentityData()

- setApplIdentityData
void setApplIdentityData(java.lang.String value)
Sets the value of the 'Appl Identity Data' attribute.
 

Parameters:value - the new value of the 'Appl Identity Data' attribute.See Also:getApplIdentityData()

- getPutApplType
int getPutApplType()
Returns the value of the 'Put Appl Type' attribute.
 

 If the meaning of the 'Put Appl Type' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Put Appl Type' attribute.See Also:isSetPutApplType(), 
unsetPutApplType(), 
setPutApplType(int), 
WMQStructuresPackage.getMQMD\_PutApplType()

- setPutApplType
void setPutApplType(int value)
Sets the value of the 'Put Appl Type' attribute.
 

Parameters:value - the new value of the 'Put Appl Type' attribute.See Also:isSetPutApplType(), 
unsetPutApplType(), 
getPutApplType()

- unsetPutApplType
void unsetPutApplType()
Unsets the value of the 'Put Appl Type' attribute.
 

See Also:isSetPutApplType(), 
getPutApplType(), 
setPutApplType(int)

- isSetPutApplType
boolean isSetPutApplType()
Returns whether the value of the 'Put Appl Type' attribute is set.
 

Returns:whether the value of the 'Put Appl Type' attribute is set.See Also:unsetPutApplType(), 
getPutApplType(), 
setPutApplType(int)

- getPutApplName
java.lang.String getPutApplName()
Returns the value of the 'Put Appl Name' attribute.
 

 If the meaning of the 'Put Appl Name' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Put Appl Name' attribute.See Also:setPutApplName(String), 
WMQStructuresPackage.getMQMD\_PutApplName()

- setPutApplName
void setPutApplName(java.lang.String value)
Sets the value of the 'Put Appl Name' attribute.
 

Parameters:value - the new value of the 'Put Appl Name' attribute.See Also:getPutApplName()

- getPutDate
java.lang.String getPutDate()
Returns the value of the 'Put Date' attribute.
 

 If the meaning of the 'Put Date' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Put Date' attribute.See Also:setPutDate(String), 
WMQStructuresPackage.getMQMD\_PutDate()

- setPutDate
void setPutDate(java.lang.String value)
Sets the value of the 'Put Date' attribute.
 

Parameters:value - the new value of the 'Put Date' attribute.See Also:getPutDate()

- getPutTime
java.lang.String getPutTime()
Returns the value of the 'Put Time' attribute.
 

 If the meaning of the 'Put Time' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Put Time' attribute.See Also:setPutTime(String), 
WMQStructuresPackage.getMQMD\_PutTime()

- setPutTime
void setPutTime(java.lang.String value)
Sets the value of the 'Put Time' attribute.
 

Parameters:value - the new value of the 'Put Time' attribute.See Also:getPutTime()

- getApplOriginData
java.lang.String getApplOriginData()
Returns the value of the 'Appl Origin Data' attribute.
 

 If the meaning of the 'Appl Origin Data' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Appl Origin Data' attribute.See Also:setApplOriginData(String), 
WMQStructuresPackage.getMQMD\_ApplOriginData()

- setApplOriginData
void setApplOriginData(java.lang.String value)
Sets the value of the 'Appl Origin Data' attribute.
 

Parameters:value - the new value of the 'Appl Origin Data' attribute.See Also:getApplOriginData()

- getGroupId
byte[] getGroupId()
Returns the value of the 'Group Id' attribute.
 

 If the meaning of the 'Group Id' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Group Id' attribute.See Also:setGroupId(byte[]), 
WMQStructuresPackage.getMQMD\_GroupId()

- setGroupId
void setGroupId(byte[] value)
Sets the value of the 'Group Id' attribute.
 

Parameters:value - the new value of the 'Group Id' attribute.See Also:getGroupId()

- getMsgSeqNumber
int getMsgSeqNumber()
Returns the value of the 'Msg Seq Number' attribute.
 

 If the meaning of the 'Msg Seq Number' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Msg Seq Number' attribute.See Also:isSetMsgSeqNumber(), 
unsetMsgSeqNumber(), 
setMsgSeqNumber(int), 
WMQStructuresPackage.getMQMD\_MsgSeqNumber()

- setMsgSeqNumber
void setMsgSeqNumber(int value)
Sets the value of the 'Msg Seq Number' attribute.
 

Parameters:value - the new value of the 'Msg Seq Number' attribute.See Also:isSetMsgSeqNumber(), 
unsetMsgSeqNumber(), 
getMsgSeqNumber()

- unsetMsgSeqNumber
void unsetMsgSeqNumber()
Unsets the value of the 'Msg Seq Number' attribute.
 

See Also:isSetMsgSeqNumber(), 
getMsgSeqNumber(), 
setMsgSeqNumber(int)

- isSetMsgSeqNumber
boolean isSetMsgSeqNumber()
Returns whether the value of the 'Msg Seq Number' attribute is set.
 

Returns:whether the value of the 'Msg Seq Number' attribute is set.See Also:unsetMsgSeqNumber(), 
getMsgSeqNumber(), 
setMsgSeqNumber(int)

- getOffset
int getOffset()
Returns the value of the 'Offset' attribute.
 

 If the meaning of the 'Offset' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Offset' attribute.See Also:isSetOffset(), 
unsetOffset(), 
setOffset(int), 
WMQStructuresPackage.getMQMD\_Offset()

- setOffset
void setOffset(int value)
Sets the value of the 'Offset' attribute.
 

Parameters:value - the new value of the 'Offset' attribute.See Also:isSetOffset(), 
unsetOffset(), 
getOffset()

- unsetOffset
void unsetOffset()
Unsets the value of the 'Offset' attribute.
 

See Also:isSetOffset(), 
getOffset(), 
setOffset(int)

- isSetOffset
boolean isSetOffset()
Returns whether the value of the 'Offset' attribute is set.
 

Returns:whether the value of the 'Offset' attribute is set.See Also:unsetOffset(), 
getOffset(), 
setOffset(int)

- getMsgFlags
int getMsgFlags()
Returns the value of the 'Msg Flags' attribute.
 

 If the meaning of the 'Msg Flags' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Msg Flags' attribute.See Also:isSetMsgFlags(), 
unsetMsgFlags(), 
setMsgFlags(int), 
WMQStructuresPackage.getMQMD\_MsgFlags()

- setMsgFlags
void setMsgFlags(int value)
Sets the value of the 'Msg Flags' attribute.
 

Parameters:value - the new value of the 'Msg Flags' attribute.See Also:isSetMsgFlags(), 
unsetMsgFlags(), 
getMsgFlags()

- unsetMsgFlags
void unsetMsgFlags()
Unsets the value of the 'Msg Flags' attribute.
 

See Also:isSetMsgFlags(), 
getMsgFlags(), 
setMsgFlags(int)

- isSetMsgFlags
boolean isSetMsgFlags()
Returns whether the value of the 'Msg Flags' attribute is set.
 

Returns:whether the value of the 'Msg Flags' attribute is set.See Also:unsetMsgFlags(), 
getMsgFlags(), 
setMsgFlags(int)

- getOriginalLength
int getOriginalLength()
Returns the value of the 'Original Length' attribute.
 

 If the meaning of the 'Original Length' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Original Length' attribute.See Also:isSetOriginalLength(), 
unsetOriginalLength(), 
setOriginalLength(int), 
WMQStructuresPackage.getMQMD\_OriginalLength()

- setOriginalLength
void setOriginalLength(int value)
Sets the value of the 'Original Length' attribute.
 

Parameters:value - the new value of the 'Original Length' attribute.See Also:isSetOriginalLength(), 
unsetOriginalLength(), 
getOriginalLength()

- unsetOriginalLength
void unsetOriginalLength()
Unsets the value of the 'Original Length' attribute.
 

See Also:isSetOriginalLength(), 
getOriginalLength(), 
setOriginalLength(int)

- isSetOriginalLength
boolean isSetOriginalLength()
Returns whether the value of the 'Original Length' attribute is set.
 

Returns:whether the value of the 'Original Length' attribute is set.See Also:unsetOriginalLength(), 
getOriginalLength(), 
setOriginalLength(int)