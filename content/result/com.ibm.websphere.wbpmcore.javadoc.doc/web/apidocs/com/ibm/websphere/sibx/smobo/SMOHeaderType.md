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

## Interface SMOHeaderType

- All Known Subinterfaces: SourceInfoType public interface SMOHeaderType A representation of the model object 'SMO Header Type '. The following features are supported:

```
public interface SMOHeaderType
```

The following features are supported:
 
Message UUID
Version
Message Type
Operation
Action
Target

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getAction()
Returns the value of the 'Action' attribute.

java.util.List<TargetAddressType>
getAlternateTarget()
Returns the value of the 'Alternate Target' containment reference list.

java.lang.String
getInterface()
Returns the value of the 'Interface' attribute

java.lang.String
getMessageType()
Returns the value of the 'Message Type' attribute.

java.lang.String
getMessageUUID()
Returns the value of the 'Message UUID' attribute.

java.lang.String
getOperation()
Returns the value of the 'Operation' attribute.

BindingTypeType
getSourceBindingType()
Returns the value of the 'Source Binding Type' attribute.

java.lang.String
getSourceNode()
Returns the value of the 'Source Node' attribute

TargetAddressType
getTarget()
Returns the value of the 'Target' containment reference.

VersionType
getVersion()
Returns the value of the 'Version' containment reference.

boolean
isSetSourceBindingType()
Returns whether the value of the 'Source Binding Type' attribute is set

void
setAction(java.lang.String value)
Sets the value of the 'Action' attribute.

void
setInterface(java.lang.String value)
Sets the value of the 'Interface' attribute

void
setMessageType(java.lang.String value)
Sets the value of the 'Message Type' attribute.

void
setMessageUUID(java.lang.String value)
Sets the value of the 'Message UUID' attribute.

void
setOperation(java.lang.String value)
Sets the value of the 'Operation' attribute.

void
setSourceBindingType(BindingTypeType value)
Sets the value of the 'Source Binding Type' attribute

void
setSourceNode(java.lang.String value)
Sets the value of the 'Source Node' attribute

void
setTarget(TargetAddressType value)
Sets the value of the 'Target' containment reference.

void
setVersion(VersionType value)
Sets the value of the 'Version' containment reference.

void
unsetSourceBindingType()
Unsets the value of the 'Source Binding Type' attribute

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- $sccsid
static final java.lang.String $sccsid
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getMessageUUID
java.lang.String getMessageUUID()
Returns the value of the 'Message UUID' attribute.
 
 This Universally Unique Identifier is a message tag that enables a specific message
 to be unambiguously referred to.
 
Returns:the value of the 'Message UUID' attribute.See Also:setMessageUUID(String)
    - setMessageUUID
void setMessageUUID(java.lang.String value)
Sets the value of the 'Message UUID' attribute.
Parameters:value - the new value of the 'Message UUID' attribute.See Also:getMessageUUID()
    - getVersion
VersionType getVersion()
Returns the value of the 'Version' containment reference.
Returns:the value of the 'Version' containment reference.See Also:setVersion(VersionType)
    - setVersion
void setVersion(VersionType value)
Sets the value of the 'Version' containment reference.
Parameters:value - the new value of the 'Version' containment reference.See Also:getVersion()
    - getMessageType
java.lang.String getMessageType()
Returns the value of the 'Message Type' attribute.
 
 Messages can be either 'Request', 'Response' or 'Exception' messages.
 
Returns:the value of the 'Message Type' attribute.See Also:setMessageType(String)
    - setMessageType
void setMessageType(java.lang.String value)
Sets the value of the 'Message Type' attribute.
Parameters:value - the new value of the 'Message Type' attribute.See Also:getMessageType()
    - getOperation
java.lang.String getOperation()
Returns the value of the 'Operation' attribute.
Returns:the value of the 'Operation' attribute.See Also:setOperation(String)
    - setOperation
void setOperation(java.lang.String value)
Sets the value of the 'Operation' attribute.
Parameters:value - the new value of the 'Operation' attribute.See Also:getOperation()
    - getAction
java.lang.String getAction()
Returns the value of the 'Action' attribute.
Returns:the value of the 'Action' attribute.See Also:setAction(String)
    - setAction
void setAction(java.lang.String value)
Sets the value of the 'Action' attribute.
Parameters:value - the new value of the 'Action' attribute.See Also:getAction()
    - getTarget
TargetAddressType getTarget()
Returns the value of the 'Target' containment reference.
Returns:the value of the 'Target' containment reference.See Also:setTarget(TargetAddressType)
    - setTarget
void setTarget(TargetAddressType value)
Sets the value of the 'Target' containment reference.
Parameters:value - the new value of the 'Target' containment reference.See Also:getTarget()
    - getAlternateTarget
java.util.List<TargetAddressType> getAlternateTarget()
Returns the value of the 'Alternate Target' containment reference list.
 The list contents are of type TargetAddressType.
 

Returns:the value of the 'Alternate Target' containment reference list.
    - getSourceNode
java.lang.String getSourceNode()
Returns the value of the 'Source Node' attribute.
 

Returns:the value of the 'Source Node' attribute.See Also:setSourceNode(String)
    - setSourceNode
void setSourceNode(java.lang.String value)
Sets the value of the 'Source Node' attribute.
 

Parameters:value - the new value of the 'Source Node' attribute.See Also:getSourceNode()
    - getSourceBindingType
BindingTypeType getSourceBindingType()
Returns the value of the 'Source Binding Type' attribute.
 The default value is "NotSet".
 The literals are from the enumeration BindingTypeType.
 

Returns:the value of the 'Source Binding Type' attribute.See Also:BindingTypeType, 
isSetSourceBindingType(), 
unsetSourceBindingType(), 
setSourceBindingType(BindingTypeType)
    - setSourceBindingType
void setSourceBindingType(BindingTypeType value)
Sets the value of the 'Source Binding Type' attribute.
 

Parameters:value - the new value of the 'Source Binding Type' attribute.See Also:BindingTypeType, 
isSetSourceBindingType(), 
unsetSourceBindingType(), 
getSourceBindingType()
    - unsetSourceBindingType
void unsetSourceBindingType()
Unsets the value of the 'Source Binding Type' attribute.
 

See Also:isSetSourceBindingType(), 
getSourceBindingType(), 
setSourceBindingType(BindingTypeType)
    - isSetSourceBindingType
boolean isSetSourceBindingType()
Returns whether the value of the 'Source Binding Type' attribute is set.
 

Returns:whether the value of the 'Source Binding Type' attribute is set.See Also:unsetSourceBindingType(), 
getSourceBindingType(), 
setSourceBindingType(BindingTypeType)
    - getInterface
java.lang.String getInterface()
Returns the value of the 'Interface' attribute.
 

Returns:the value of the 'Interface' attribute.See Also:setInterface(String)
    - setInterface
void setInterface(java.lang.String value)
Sets the value of the 'Interface' attribute.
 

Parameters:value - the new value of the 'Interface' attribute.See Also:getInterface()