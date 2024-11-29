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

## Interface MQRFH

- public interface MQRFH begin-user-doc A representation of the model object 'MQRFH '. end-user-doc The following features are supported: See Also: WMQStructuresPackage.getMQRFH()

```
public interface MQRFH
```

The following features are supported:
 
Flags
Property

- ========== METHOD SUMMARY ===========
    - Method Summary

Methods 

Modifier and Type
Method and Description

int
getFlags()
Returns the value of the 'Flags' attribute.

java.util.List
getProperty()
Returns the value of the 'Property' containment reference list.

boolean
isSetFlags()
Returns whether the value of the 'Flags' attribute is set

void
setFlags(int value)
Sets the value of the 'Flags' attribute

void
unsetFlags()
Unsets the value of the 'Flags' attribute

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
WMQStructuresPackage.getMQRFH\_Flags()

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

- getProperty
java.util.List getProperty()
Returns the value of the 'Property' containment reference list.
 The list contents are of type MQRFHProperty.
 

 If the meaning of the 'Property' containment reference list isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Property' containment reference list.See Also:WMQStructuresPackage.getMQRFH\_Property()