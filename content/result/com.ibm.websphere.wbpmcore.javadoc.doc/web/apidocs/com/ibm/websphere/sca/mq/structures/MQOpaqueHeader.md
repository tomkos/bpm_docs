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

## Interface MQOpaqueHeader

- public interface MQOpaqueHeader begin-user-doc A representation of the model object 'MQ Opaque Header '. end-user-doc The following features are supported: See Also: WMQStructuresPackage.getMQOpaqueHeader()

```
public interface MQOpaqueHeader
```

The following features are supported:
 
Struc Id
Version
Flags
Data

- ========== METHOD SUMMARY ===========
    - Method Summary

Methods 

Modifier and Type
Method and Description

byte[]
getData()
Returns the value of the 'Data' attribute

int
getFlags()
Returns the value of the 'Flags' attribute

java.lang.String
getStrucId()
Returns the value of the 'Struc Id' attribute

int
getVersion()
Returns the value of the 'Version' attribute

boolean
isSetFlags()
Returns whether the value of the 'Flags' attribute is set

boolean
isSetVersion()
Returns whether the value of the 'Version' attribute is set

void
setData(byte[] value)
Sets the value of the 'Data' attribute

void
setFlags(int value)
Sets the value of the 'Flags' attribute

void
setStrucId(java.lang.String value)
Sets the value of the 'Struc Id' attribute

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

- getStrucId
java.lang.String getStrucId()
Returns the value of the 'Struc Id' attribute.
 

 If the meaning of the 'Struc Id' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Struc Id' attribute.See Also:setStrucId(String), 
WMQStructuresPackage.getMQOpaqueHeader\_StrucId()

- setStrucId
void setStrucId(java.lang.String value)
Sets the value of the 'Struc Id' attribute.
 

Parameters:value - the new value of the 'Struc Id' attribute.See Also:getStrucId()

- getVersion
int getVersion()
Returns the value of the 'Version' attribute.
 

 If the meaning of the 'Version' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Version' attribute.See Also:isSetVersion(), 
unsetVersion(), 
setVersion(int), 
WMQStructuresPackage.getMQOpaqueHeader\_Version()

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
WMQStructuresPackage.getMQOpaqueHeader\_Flags()

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

- getData
byte[] getData()
Returns the value of the 'Data' attribute.
 

 If the meaning of the 'Data' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Data' attribute.See Also:setData(byte[]), 
WMQStructuresPackage.getMQOpaqueHeader\_Data()

- setData
void setData(byte[] value)
Sets the value of the 'Data' attribute.
 

Parameters:value - the new value of the 'Data' attribute.See Also:getData()