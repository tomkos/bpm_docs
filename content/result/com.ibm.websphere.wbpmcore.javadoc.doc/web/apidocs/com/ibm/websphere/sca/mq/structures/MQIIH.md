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

## Interface MQIIH

- public interface MQIIH begin-user-doc A representation of the model object 'MQIIH '. end-user-doc The following features are supported: See Also: WMQStructuresPackage.getMQIIH()

```
public interface MQIIH
```

The following features are supported:
 
Version
Flags
LTerm Override
MFS Map Name
Reply To Format
Authenticator
Tran Instance Id
Tran State
Commit Mode
Security Scope
Reserved

- ========== METHOD SUMMARY ===========
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getAuthenticator()
Returns the value of the 'Authenticator' attribute

java.lang.String
getCommitMode()
Returns the value of the 'Commit Mode' attribute

int
getFlags()
Returns the value of the 'Flags' attribute

java.lang.String
getLTermOverride()
Returns the value of the 'LTerm Override' attribute

java.lang.String
getMFSMapName()
Returns the value of the 'MFS Map Name' attribute

java.lang.String
getReplyToFormat()
Returns the value of the 'Reply To Format' attribute

java.lang.String
getReserved()
Returns the value of the 'Reserved' attribute

java.lang.String
getSecurityScope()
Returns the value of the 'Security Scope' attribute

byte[]
getTranInstanceId()
Returns the value of the 'Tran Instance Id' attribute

java.lang.String
getTranState()
Returns the value of the 'Tran State' attribute

int
getVersion()
Returns the value of the 'Version' attribute.

boolean
isSetFlags()
Returns whether the value of the 'Flags' attribute is set

boolean
isSetVersion()
Returns whether the value of the 'Version' attribute is set

void
setAuthenticator(java.lang.String value)
Sets the value of the 'Authenticator' attribute

void
setCommitMode(java.lang.String value)
Sets the value of the 'Commit Mode' attribute

void
setFlags(int value)
Sets the value of the 'Flags' attribute

void
setLTermOverride(java.lang.String value)
Sets the value of the 'LTerm Override' attribute

void
setMFSMapName(java.lang.String value)
Sets the value of the 'MFS Map Name' attribute

void
setReplyToFormat(java.lang.String value)
Sets the value of the 'Reply To Format' attribute

void
setReserved(java.lang.String value)
Sets the value of the 'Reserved' attribute

void
setSecurityScope(java.lang.String value)
Sets the value of the 'Security Scope' attribute

void
setTranInstanceId(byte[] value)
Sets the value of the 'Tran Instance Id' attribute

void
setTranState(java.lang.String value)
Sets the value of the 'Tran State' attribute

void
setVersion(int value)
Sets the value of the 'Version' attribute

void
unsetFlags()
Unsets the value of the 'Flags' attribute

void
unsetVersion()
Unsets the value of the 'Version' attribute

- ============ METHOD DETAIL ==========
    - Method Detail

### Method Detail

- getVersion
int getVersion()
Returns the value of the 'Version' attribute.
 The default value is "1".
 

 If the meaning of the 'Version' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Version' attribute.See Also:isSetVersion(), 
unsetVersion(), 
setVersion(int), 
WMQStructuresPackage.getMQIIH\_Version()

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
WMQStructuresPackage.getMQIIH\_Flags()

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

- getLTermOverride
java.lang.String getLTermOverride()
Returns the value of the 'LTerm Override' attribute.
 

 If the meaning of the 'LTerm Override' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'LTerm Override' attribute.See Also:setLTermOverride(String), 
WMQStructuresPackage.getMQIIH\_LTermOverride()

- setLTermOverride
void setLTermOverride(java.lang.String value)
Sets the value of the 'LTerm Override' attribute.
 

Parameters:value - the new value of the 'LTerm Override' attribute.See Also:getLTermOverride()

- getMFSMapName
java.lang.String getMFSMapName()
Returns the value of the 'MFS Map Name' attribute.
 

 If the meaning of the 'MFS Map Name' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'MFS Map Name' attribute.See Also:setMFSMapName(String), 
WMQStructuresPackage.getMQIIH\_MFSMapName()

- setMFSMapName
void setMFSMapName(java.lang.String value)
Sets the value of the 'MFS Map Name' attribute.
 

Parameters:value - the new value of the 'MFS Map Name' attribute.See Also:getMFSMapName()

- getReplyToFormat
java.lang.String getReplyToFormat()
Returns the value of the 'Reply To Format' attribute.
 

 If the meaning of the 'Reply To Format' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Reply To Format' attribute.See Also:setReplyToFormat(String), 
WMQStructuresPackage.getMQIIH\_ReplyToFormat()

- setReplyToFormat
void setReplyToFormat(java.lang.String value)
Sets the value of the 'Reply To Format' attribute.
 

Parameters:value - the new value of the 'Reply To Format' attribute.See Also:getReplyToFormat()

- getAuthenticator
java.lang.String getAuthenticator()
Returns the value of the 'Authenticator' attribute.
 

 If the meaning of the 'Authenticator' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Authenticator' attribute.See Also:setAuthenticator(String), 
WMQStructuresPackage.getMQIIH\_Authenticator()

- setAuthenticator
void setAuthenticator(java.lang.String value)
Sets the value of the 'Authenticator' attribute.
 

Parameters:value - the new value of the 'Authenticator' attribute.See Also:getAuthenticator()

- getTranInstanceId
byte[] getTranInstanceId()
Returns the value of the 'Tran Instance Id' attribute.
 

 If the meaning of the 'Tran Instance Id' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Tran Instance Id' attribute.See Also:setTranInstanceId(byte[]), 
WMQStructuresPackage.getMQIIH\_TranInstanceId()

- setTranInstanceId
void setTranInstanceId(byte[] value)
Sets the value of the 'Tran Instance Id' attribute.
 

Parameters:value - the new value of the 'Tran Instance Id' attribute.See Also:getTranInstanceId()

- getTranState
java.lang.String getTranState()
Returns the value of the 'Tran State' attribute.
 

 If the meaning of the 'Tran State' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Tran State' attribute.See Also:setTranState(String), 
WMQStructuresPackage.getMQIIH\_TranState()

- setTranState
void setTranState(java.lang.String value)
Sets the value of the 'Tran State' attribute.
 

Parameters:value - the new value of the 'Tran State' attribute.See Also:getTranState()

- getCommitMode
java.lang.String getCommitMode()
Returns the value of the 'Commit Mode' attribute.
 

 If the meaning of the 'Commit Mode' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Commit Mode' attribute.See Also:setCommitMode(String), 
WMQStructuresPackage.getMQIIH\_CommitMode()

- setCommitMode
void setCommitMode(java.lang.String value)
Sets the value of the 'Commit Mode' attribute.
 

Parameters:value - the new value of the 'Commit Mode' attribute.See Also:getCommitMode()

- getSecurityScope
java.lang.String getSecurityScope()
Returns the value of the 'Security Scope' attribute.
 

 If the meaning of the 'Security Scope' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Security Scope' attribute.See Also:setSecurityScope(String), 
WMQStructuresPackage.getMQIIH\_SecurityScope()

- setSecurityScope
void setSecurityScope(java.lang.String value)
Sets the value of the 'Security Scope' attribute.
 

Parameters:value - the new value of the 'Security Scope' attribute.See Also:getSecurityScope()

- getReserved
java.lang.String getReserved()
Returns the value of the 'Reserved' attribute.
 

 If the meaning of the 'Reserved' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Reserved' attribute.See Also:setReserved(String), 
WMQStructuresPackage.getMQIIH\_Reserved()

- setReserved
void setReserved(java.lang.String value)
Sets the value of the 'Reserved' attribute.
 

Parameters:value - the new value of the 'Reserved' attribute.See Also:getReserved()