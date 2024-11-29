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

## Interface HeadersType

- All Known Subinterfaces: HeaderInfoType public interface HeadersType A representation of the model object 'Headers Type '. The Headers Type should be considered as a folder that contains all other headers, SOAP Fault information and message properties. The following features are supported:

```
public interface HeadersType
```

The Headers Type should be considered as a folder that contains all other headers, SOAP Fault
 information and message properties.

The following features are supported:
 
SMO Header
JMS Header
SOAP Header
SOAP Fault Info
Properties
MQ Header

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

EISHeaderType
getEISHeader()
Returns the value of the 'EIS Header' containment reference

HTTPHeaderType
getHTTPHeader()
Returns the value of the 'HTTP Header' containment reference

JMSHeaderType
getJMSHeader()
Returns the value of the 'JMS Header' containment reference.

MQHeaderType
getMQHeader()
Returns the value of the 'MQ Header' containment reference.

java.util.List<PropertyType>
getProperties()
Returns the value of the 'Properties' containment reference list.

SMOHeaderType
getSMOHeader()
Returns the value of the 'SMO Header' containment reference.

SOAPFaultInfoType
getSOAPFaultInfo()
Returns the value of the 'SOAP Fault Info' containment reference.

java.util.List<SOAPHeaderType>
getSOAPHeader()
Returns the value of the 'SOAP Header' containment reference list.

WSAHeaderType
getWSAHeader()
Returns the value of the 'WSA Header' containment reference

void
setEISHeader(EISHeaderType value)
Sets the value of the 'EIS Header' containment reference

void
setHTTPHeader(HTTPHeaderType value)
Sets the value of the 'HTTP Header' containment reference

void
setJMSHeader(JMSHeaderType value)
Sets the value of the 'JMS Header' containment reference.

void
setMQHeader(MQHeaderType value)
Sets the value of the 'MQ Header' containment reference.

void
setSMOHeader(SMOHeaderType value)
Sets the value of the 'SMO Header' containment reference.

void
setSOAPFaultInfo(SOAPFaultInfoType value)
Sets the value of the 'SOAP Fault Info' containment reference.

void
setWSAHeader(WSAHeaderType value)
Sets the value of the 'WSA Header' containment reference

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

    - getSMOHeader
SMOHeaderType getSMOHeader()
Returns the value of the 'SMO Header' containment reference.
 
 Returns the value of the ServiceMessageObject header.
 
Returns:the value of the 'SMO Header' containment reference.See Also:setSMOHeader(SMOHeaderType)
    - setSMOHeader
void setSMOHeader(SMOHeaderType value)
Sets the value of the 'SMO Header' containment reference.
Parameters:value - the new value of the 'SMO Header' containment reference.See Also:getSMOHeader()
    - getJMSHeader
JMSHeaderType getJMSHeader()
Returns the value of the 'JMS Header' containment reference.
 
 This JMS Header contains all of Header Fields defined in the JMS specification.
 This header is typically only present when the message has flowed over either JMS
 (or possibly SOAP over JMS).  Any JMS properties will be presented in the properties 
 folder.
 
Returns:the value of the 'JMS Header' containment reference.See Also:setJMSHeader(JMSHeaderType)
    - setJMSHeader
void setJMSHeader(JMSHeaderType value)
Sets the value of the 'JMS Header' containment reference.
Parameters:value - the new value of the 'JMS Header' containment reference.See Also:getJMSHeader()
    - getSOAPHeader
java.util.List<SOAPHeaderType> getSOAPHeader()
Returns the value of the 'SOAP Header' containment reference list.
 The list contents are of type SOAPHeaderType.
 
 This a list of all of the SOAP Headers found in the inbound message. 
 
Returns:the value of the 'SOAP Header' containment reference list.
    - getSOAPFaultInfo
SOAPFaultInfoType getSOAPFaultInfo()
Returns the value of the 'SOAP Fault Info' containment reference.
Returns:the value of the 'SOAP Fault Info' containment reference.See Also:setSOAPFaultInfo(SOAPFaultInfoType)
    - setSOAPFaultInfo
void setSOAPFaultInfo(SOAPFaultInfoType value)
Sets the value of the 'SOAP Fault Info' containment reference.
Parameters:value - the new value of the 'SOAP Fault Info' containment reference.See Also:getSOAPFaultInfo()
    - getProperties
java.util.List<PropertyType> getProperties()
Returns the value of the 'Properties' containment reference list.
 The list contents are of type PropertyType.
 
 This is a list of the properties associated with the message and each list entry 
 consists of a name/value pair.
 
Returns:the value of the 'Properties' containment reference list.
    - getMQHeader
MQHeaderType getMQHeader()
Returns the value of the 'MQ Header' containment reference.
 
 Returns the value of the MQ header.
 
Returns:the value of the 'MQ Header' containment reference.See Also:setMQHeader(MQHeaderType)
    - setMQHeader
void setMQHeader(MQHeaderType value)
Sets the value of the 'MQ Header' containment reference.
Parameters:value - the new value of the 'MQ Header' containment reference.See Also:getMQHeader()
    - getHTTPHeader
HTTPHeaderType getHTTPHeader()
Returns the value of the 'HTTP Header' containment reference.
 

Returns:the value of the 'HTTP Header' containment reference.See Also:setHTTPHeader(HTTPHeaderType)
    - setHTTPHeader
void setHTTPHeader(HTTPHeaderType value)
Sets the value of the 'HTTP Header' containment reference.
 

Parameters:value - the new value of the 'HTTP Header' containment reference.See Also:getHTTPHeader()
    - getEISHeader
EISHeaderType getEISHeader()
Returns the value of the 'EIS Header' containment reference.
 

Returns:the value of the 'EIS Header' containment reference.See Also:setEISHeader(EISHeaderType)
    - setEISHeader
void setEISHeader(EISHeaderType value)
Sets the value of the 'EIS Header' containment reference.
 

Parameters:value - the new value of the 'EIS Header' containment reference.See Also:getEISHeader()
    - getWSAHeader
WSAHeaderType getWSAHeader()
Returns the value of the 'WSA Header' containment reference.
 

Returns:the value of the 'WSA Header' containment reference.See Also:setWSAHeader(WSAHeaderType)
    - setWSAHeader
void setWSAHeader(WSAHeaderType value)
Sets the value of the 'WSA Header' containment reference.
 

Parameters:value - the new value of the 'WSA Header' containment reference.See Also:getWSAHeader()