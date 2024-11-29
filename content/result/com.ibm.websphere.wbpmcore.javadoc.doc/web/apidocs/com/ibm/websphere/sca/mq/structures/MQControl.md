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

## Interface MQControl

- All Known Subinterfaces: MQChainedHeaderType , MQHeader public interface MQControl begin-user-doc A representation of the model object 'MQ Control '. end-user-doc The following features are supported: See Also: WMQStructuresPackage.getMQControl()

```
public interface MQControl
```

The following features are supported:
 
Encoding
Coded Char Set Id
Format

- ========== METHOD SUMMARY ===========
    - Method Summary

Methods 

Modifier and Type
Method and Description

int
getCodedCharSetId()
Returns the value of the 'Coded Char Set Id' attribute

int
getEncoding()
Returns the value of the 'Encoding' attribute

java.lang.String
getFormat()
Returns the value of the 'Format' attribute

boolean
isSetCodedCharSetId()
Returns whether the value of the 'Coded Char Set Id' attribute is set

boolean
isSetEncoding()
Returns whether the value of the 'Encoding' attribute is set

void
setCodedCharSetId(int value)
Sets the value of the 'Coded Char Set Id' attribute

void
setEncoding(int value)
Sets the value of the 'Encoding' attribute

void
setFormat(java.lang.String value)
Sets the value of the 'Format' attribute

void
unsetCodedCharSetId()
Unsets the value of the 'Coded Char Set Id' attribute

void
unsetEncoding()
Unsets the value of the 'Encoding' attribute

- ============ METHOD DETAIL ==========
    - Method Detail

### Method Detail

- getEncoding
int getEncoding()
Returns the value of the 'Encoding' attribute.
 

 If the meaning of the 'Encoding' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Encoding' attribute.See Also:isSetEncoding(), 
unsetEncoding(), 
setEncoding(int), 
WMQStructuresPackage.getMQControl\_Encoding()

- setEncoding
void setEncoding(int value)
Sets the value of the 'Encoding' attribute.
 

Parameters:value - the new value of the 'Encoding' attribute.See Also:isSetEncoding(), 
unsetEncoding(), 
getEncoding()

- unsetEncoding
void unsetEncoding()
Unsets the value of the 'Encoding' attribute.
 

See Also:isSetEncoding(), 
getEncoding(), 
setEncoding(int)

- isSetEncoding
boolean isSetEncoding()
Returns whether the value of the 'Encoding' attribute is set.
 

Returns:whether the value of the 'Encoding' attribute is set.See Also:unsetEncoding(), 
getEncoding(), 
setEncoding(int)

- getCodedCharSetId
int getCodedCharSetId()
Returns the value of the 'Coded Char Set Id' attribute.
 

 If the meaning of the 'Coded Char Set Id' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Coded Char Set Id' attribute.See Also:isSetCodedCharSetId(), 
unsetCodedCharSetId(), 
setCodedCharSetId(int), 
WMQStructuresPackage.getMQControl\_CodedCharSetId()

- setCodedCharSetId
void setCodedCharSetId(int value)
Sets the value of the 'Coded Char Set Id' attribute.
 

Parameters:value - the new value of the 'Coded Char Set Id' attribute.See Also:isSetCodedCharSetId(), 
unsetCodedCharSetId(), 
getCodedCharSetId()

- unsetCodedCharSetId
void unsetCodedCharSetId()
Unsets the value of the 'Coded Char Set Id' attribute.
 

See Also:isSetCodedCharSetId(), 
getCodedCharSetId(), 
setCodedCharSetId(int)

- isSetCodedCharSetId
boolean isSetCodedCharSetId()
Returns whether the value of the 'Coded Char Set Id' attribute is set.
 

Returns:whether the value of the 'Coded Char Set Id' attribute is set.See Also:unsetCodedCharSetId(), 
getCodedCharSetId(), 
setCodedCharSetId(int)

- getFormat
java.lang.String getFormat()
Returns the value of the 'Format' attribute.
 

 If the meaning of the 'Format' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Format' attribute.See Also:setFormat(String), 
WMQStructuresPackage.getMQControl\_Format()

- setFormat
void setFormat(java.lang.String value)
Sets the value of the 'Format' attribute.
 

Parameters:value - the new value of the 'Format' attribute.See Also:getFormat()