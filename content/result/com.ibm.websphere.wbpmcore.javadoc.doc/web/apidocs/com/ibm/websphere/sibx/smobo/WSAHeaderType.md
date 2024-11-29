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

## Interface WSAHeaderType

- public interface WSAHeaderType begin-user-doc A representation of the model object 'WSA Header Type '. end-user-doc The following features are supported:

```
public interface WSAHeaderType
```

The following features are supported:
 
To
Reference Parameters
From
Reply To
Fault To
Action
Message ID
Relates To
Version

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

AttributedURIType
getAction()
Returns the value of the 'Action' containment reference

EndpointReferenceType
getFaultTo()
Returns the value of the 'Fault To' containment reference

EndpointReferenceType
getFrom()
Returns the value of the 'From' containment reference

AttributedURIType
getMessageID()
Returns the value of the 'Message ID' containment reference

ReferenceParametersType
getReferenceParameters()
Returns the value of the 'Reference Parameters' containment reference

java.util.List<RelatesToType>
getRelatesTo()
Returns the value of the 'Relates To' containment reference list.

EndpointReferenceType
getReplyTo()
Returns the value of the 'Reply To' containment reference

AttributedURIType
getTo()
Returns the value of the 'To' containment reference

WSASchemaType
getVersion()
Returns the value of the 'Version' attribute.

boolean
isSetVersion()
Returns whether the value of the 'Version' attribute is set

void
setAction(AttributedURIType value)
Sets the value of the 'Action' containment reference

void
setFaultTo(EndpointReferenceType value)
Sets the value of the 'Fault To' containment reference

void
setFrom(EndpointReferenceType value)
Sets the value of the 'From' containment reference

void
setMessageID(AttributedURIType value)
Sets the value of the 'Message ID' containment reference

void
setReferenceParameters(ReferenceParametersType value)
Sets the value of the 'Reference Parameters' containment reference

void
setReplyTo(EndpointReferenceType value)
Sets the value of the 'Reply To' containment reference

void
setTo(AttributedURIType value)
Sets the value of the 'To' containment reference

void
setVersion(WSASchemaType value)
Sets the value of the 'Version' attribute

void
unsetVersion()
Unsets the value of the 'Version' attribute

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

    - getTo
AttributedURIType getTo()
Returns the value of the 'To' containment reference.
 

Returns:the value of the 'To' containment reference.See Also:setTo(AttributedURIType)
    - setTo
void setTo(AttributedURIType value)
Sets the value of the 'To' containment reference.
 

Parameters:value - the new value of the 'To' containment reference.See Also:getTo()
    - getReferenceParameters
ReferenceParametersType getReferenceParameters()
Returns the value of the 'Reference Parameters' containment reference.
 

Returns:the value of the 'Reference Parameters' containment reference.See Also:setReferenceParameters(ReferenceParametersType)
    - setReferenceParameters
void setReferenceParameters(ReferenceParametersType value)
Sets the value of the 'Reference Parameters' containment reference.
 

Parameters:value - the new value of the 'Reference Parameters' containment reference.See Also:getReferenceParameters()
    - getFrom
EndpointReferenceType getFrom()
Returns the value of the 'From' containment reference.
 

Returns:the value of the 'From' containment reference.See Also:setFrom(EndpointReferenceType)
    - setFrom
void setFrom(EndpointReferenceType value)
Sets the value of the 'From' containment reference.
 

Parameters:value - the new value of the 'From' containment reference.See Also:getFrom()
    - getReplyTo
EndpointReferenceType getReplyTo()
Returns the value of the 'Reply To' containment reference.
 

Returns:the value of the 'Reply To' containment reference.See Also:setReplyTo(EndpointReferenceType)
    - setReplyTo
void setReplyTo(EndpointReferenceType value)
Sets the value of the 'Reply To' containment reference.
 

Parameters:value - the new value of the 'Reply To' containment reference.See Also:getReplyTo()
    - getFaultTo
EndpointReferenceType getFaultTo()
Returns the value of the 'Fault To' containment reference.
 

Returns:the value of the 'Fault To' containment reference.See Also:setFaultTo(EndpointReferenceType)
    - setFaultTo
void setFaultTo(EndpointReferenceType value)
Sets the value of the 'Fault To' containment reference.
 

Parameters:value - the new value of the 'Fault To' containment reference.See Also:getFaultTo()
    - getAction
AttributedURIType getAction()
Returns the value of the 'Action' containment reference.
 

Returns:the value of the 'Action' containment reference.See Also:setAction(AttributedURIType)
    - setAction
void setAction(AttributedURIType value)
Sets the value of the 'Action' containment reference.
 

Parameters:value - the new value of the 'Action' containment reference.See Also:getAction()
    - getMessageID
AttributedURIType getMessageID()
Returns the value of the 'Message ID' containment reference.
 

Returns:the value of the 'Message ID' containment reference.See Also:setMessageID(AttributedURIType)
    - setMessageID
void setMessageID(AttributedURIType value)
Sets the value of the 'Message ID' containment reference.
 

Parameters:value - the new value of the 'Message ID' containment reference.See Also:getMessageID()
    - getRelatesTo
java.util.List<RelatesToType> getRelatesTo()
Returns the value of the 'Relates To' containment reference list.
 The list contents are of type RelatesToType.
 

Returns:the value of the 'Relates To' containment reference list.
    - getVersion
WSASchemaType getVersion()
Returns the value of the 'Version' attribute.
 The default value is "http://www.w3.org/2005/08/addressing".
 The literals are from the enumeration WSASchemaType.
 

Returns:the value of the 'Version' attribute.See Also:WSASchemaType, 
isSetVersion(), 
unsetVersion(), 
setVersion(WSASchemaType)
    - setVersion
void setVersion(WSASchemaType value)
Sets the value of the 'Version' attribute.
 

Parameters:value - the new value of the 'Version' attribute.See Also:WSASchemaType, 
isSetVersion(), 
unsetVersion(), 
getVersion()
    - unsetVersion
void unsetVersion()
Unsets the value of the 'Version' attribute.
 

See Also:isSetVersion(), 
getVersion(), 
setVersion(WSASchemaType)
    - isSetVersion
boolean isSetVersion()
Returns whether the value of the 'Version' attribute is set.
 

Returns:whether the value of the 'Version' attribute is set.See Also:unsetVersion(), 
getVersion(), 
setVersion(WSASchemaType)