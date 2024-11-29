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

## Interface MQRFH2

- public interface MQRFH2 begin-user-doc A representation of the model object 'MQRFH2 '. end-user-doc The following features are supported: See Also: WMQStructuresPackage.getMQRFH2()

```
public interface MQRFH2
```

The following features are supported:
 
Flags
Name Value CCSID
Folder

- ========== METHOD SUMMARY ===========
    - Method Summary

Methods 

Modifier and Type
Method and Description

int
getFlags()
Returns the value of the 'Flags' attribute.

java.util.List
getFolder()
Returns the value of the 'Folder' containment reference list.

int
getNameValueCCSID()
Returns the value of the 'Name Value CCSID' attribute.

boolean
isSetFlags()
Returns whether the value of the 'Flags' attribute is set

boolean
isSetNameValueCCSID()
Returns whether the value of the 'Name Value CCSID' attribute is set

void
setFlags(int value)
Sets the value of the 'Flags' attribute

void
setNameValueCCSID(int value)
Sets the value of the 'Name Value CCSID' attribute

void
unsetFlags()
Unsets the value of the 'Flags' attribute

void
unsetNameValueCCSID()
Unsets the value of the 'Name Value CCSID' attribute

- ============ METHOD DETAIL ==========
    - Method Detail

### Method Detail

- getFlags
int getFlags()
Returns the value of the 'Flags' attribute.
 The default value is "0".
 

 If the meaning of the 'Flags' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Flags' attribute.See Also:isSetFlags(), 
unsetFlags(), 
setFlags(int), 
WMQStructuresPackage.getMQRFH2\_Flags()

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

- getNameValueCCSID
int getNameValueCCSID()
Returns the value of the 'Name Value CCSID' attribute.
 The default value is "1208".
 

 If the meaning of the 'Name Value CCSID' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Name Value CCSID' attribute.See Also:isSetNameValueCCSID(), 
unsetNameValueCCSID(), 
setNameValueCCSID(int), 
WMQStructuresPackage.getMQRFH2\_NameValueCCSID()

- setNameValueCCSID
void setNameValueCCSID(int value)
Sets the value of the 'Name Value CCSID' attribute.
 

Parameters:value - the new value of the 'Name Value CCSID' attribute.See Also:isSetNameValueCCSID(), 
unsetNameValueCCSID(), 
getNameValueCCSID()

- unsetNameValueCCSID
void unsetNameValueCCSID()
Unsets the value of the 'Name Value CCSID' attribute.
 

See Also:isSetNameValueCCSID(), 
getNameValueCCSID(), 
setNameValueCCSID(int)

- isSetNameValueCCSID
boolean isSetNameValueCCSID()
Returns whether the value of the 'Name Value CCSID' attribute is set.
 

Returns:whether the value of the 'Name Value CCSID' attribute is set.See Also:unsetNameValueCCSID(), 
getNameValueCCSID(), 
setNameValueCCSID(int)

- getFolder
java.util.List getFolder()
Returns the value of the 'Folder' containment reference list.
 The list contents are of type MQRFH2Group.
 

 If the meaning of the 'Folder' containment reference list isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Folder' containment reference list.See Also:WMQStructuresPackage.getMQRFH2\_Folder()