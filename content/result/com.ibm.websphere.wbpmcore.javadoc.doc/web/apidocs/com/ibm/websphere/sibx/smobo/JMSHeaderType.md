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

## Interface JMSHeaderType

- public interface JMSHeaderType A representation of the model object 'JMS Header Type '. The following features are supported: The reader should refer to the JMS specification and JMS provider documentation for details of the usage of each of these JMS Header fields.

```
public interface JMSHeaderType
```

The following features are supported:
 
JMS Destination
JMS Delivery Mode
JMS Message ID
JMS Timestamp
JMS Correlation ID
JMS Reply To
JMS Redelivered
JMS Type
JMS Expiration
JMS Priority

 The reader should refer to the JMS specification and JMS provider documentation for details of the
 usage of each of these JMS Header fields.

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
getJMSCorrelationID()
Returns the value of the 'JMS Correlation ID' attribute.

PersistenceType
getJMSDeliveryMode()
Returns the value of the 'JMS Delivery Mode' attribute.

java.lang.String
getJMSDestination()
Returns the value of the 'JMS Destination' attribute.

long
getJMSExpiration()
Returns the value of the 'JMS Expiration' attribute.

java.lang.String
getJMSMessageID()
Returns the value of the 'JMS Message ID' attribute.

java.math.BigInteger
getJMSPriority()
Returns the value of the 'JMS Priority' attribute.

java.lang.String
getJMSReplyTo()
Returns the value of the 'JMS Reply To' attribute.

long
getJMSTimestamp()
Returns the value of the 'JMS Timestamp' attribute.

java.lang.String
getJMSType()
Returns the value of the 'JMS Type' attribute.

boolean
isJMSRedelivered()
Returns the value of the 'JMS Redelivered' attribute.

boolean
isSetJMSDeliveryMode()
Returns whether the value of the 'JMS Delivery Mode' attribute is set.

boolean
isSetJMSExpiration()
Returns whether the value of the 'JMS Expiration' attribute is set.

boolean
isSetJMSRedelivered()
Returns whether the value of the 'JMS Redelivered' attribute is set.

boolean
isSetJMSTimestamp()
Returns whether the value of the 'JMS Timestamp' attribute is set.

void
setJMSCorrelationID(java.lang.String value)
Sets the value of the 'JMS Correlation ID' attribute.

void
setJMSDeliveryMode(PersistenceType value)
Sets the value of the 'JMS Delivery Mode' attribute.

void
setJMSDestination(java.lang.String value)
Sets the value of the 'JMS Destination' attribute.

void
setJMSExpiration(long value)
Sets the value of the 'JMS Expiration' attribute.

void
setJMSMessageID(java.lang.String value)
Sets the value of the 'JMS Message ID' attribute.

void
setJMSPriority(java.math.BigInteger value)
Sets the value of the 'JMS Priority' attribute.

void
setJMSRedelivered(boolean value)
Sets the value of the 'JMS Redelivered' attribute.

void
setJMSReplyTo(java.lang.String value)
Sets the value of the 'JMS Reply To' attribute.

void
setJMSTimestamp(long value)
Sets the value of the 'JMS Timestamp' attribute.

void
setJMSType(java.lang.String value)
Sets the value of the 'JMS Type' attribute.

void
unsetJMSDeliveryMode()
Unsets the value of the 'JMS Delivery Mode' attribute.

void
unsetJMSExpiration()
Unsets the value of the 'JMS Expiration' attribute.

void
unsetJMSRedelivered()
Unsets the value of the 'JMS Redelivered' attribute.

void
unsetJMSTimestamp()
Unsets the value of the 'JMS Timestamp' attribute.

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

    - getJMSDestination
java.lang.String getJMSDestination()
Returns the value of the 'JMS Destination' attribute.
Returns:the value of the 'JMS Destination' attribute.See Also:setJMSDestination(String)
    - setJMSDestination
void setJMSDestination(java.lang.String value)
Sets the value of the 'JMS Destination' attribute.
Parameters:value - the new value of the 'JMS Destination' attribute.See Also:getJMSDestination()
    - getJMSDeliveryMode
PersistenceType getJMSDeliveryMode()
Returns the value of the 'JMS Delivery Mode' attribute.
 The default value is "NonPersistent".
 The literals are from the enumeration PersistenceType.
Returns:the value of the 'JMS Delivery Mode' attribute.See Also:PersistenceType, 
isSetJMSDeliveryMode(), 
unsetJMSDeliveryMode(), 
setJMSDeliveryMode(PersistenceType)
    - setJMSDeliveryMode
void setJMSDeliveryMode(PersistenceType value)
Sets the value of the 'JMS Delivery Mode' attribute.
Parameters:value - the new value of the 'JMS Delivery Mode' attribute.See Also:PersistenceType, 
isSetJMSDeliveryMode(), 
unsetJMSDeliveryMode(), 
getJMSDeliveryMode()
    - unsetJMSDeliveryMode
void unsetJMSDeliveryMode()
Unsets the value of the 'JMS Delivery Mode' attribute.
See Also:isSetJMSDeliveryMode(), 
getJMSDeliveryMode(), 
setJMSDeliveryMode(PersistenceType)
    - isSetJMSDeliveryMode
boolean isSetJMSDeliveryMode()
Returns whether the value of the 'JMS Delivery Mode' attribute is set.
Returns:whether the value of the 'JMS Delivery Mode' attribute is set.See Also:unsetJMSDeliveryMode(), 
getJMSDeliveryMode(), 
setJMSDeliveryMode(PersistenceType)
    - getJMSMessageID
java.lang.String getJMSMessageID()
Returns the value of the 'JMS Message ID' attribute.
Returns:the value of the 'JMS Message ID' attribute.See Also:setJMSMessageID(String)
    - setJMSMessageID
void setJMSMessageID(java.lang.String value)
Sets the value of the 'JMS Message ID' attribute.
Parameters:value - the new value of the 'JMS Message ID' attribute.See Also:getJMSMessageID()
    - getJMSTimestamp
long getJMSTimestamp()
Returns the value of the 'JMS Timestamp' attribute.
Returns:the value of the 'JMS Timestamp' attribute.See Also:isSetJMSTimestamp(), 
unsetJMSTimestamp(), 
setJMSTimestamp(long)
    - setJMSTimestamp
void setJMSTimestamp(long value)
Sets the value of the 'JMS Timestamp' attribute.
Parameters:value - the new value of the 'JMS Timestamp' attribute.See Also:isSetJMSTimestamp(), 
unsetJMSTimestamp(), 
getJMSTimestamp()
    - unsetJMSTimestamp
void unsetJMSTimestamp()
Unsets the value of the 'JMS Timestamp' attribute.
See Also:isSetJMSTimestamp(), 
getJMSTimestamp(), 
setJMSTimestamp(long)
    - isSetJMSTimestamp
boolean isSetJMSTimestamp()
Returns whether the value of the 'JMS Timestamp' attribute is set.
Returns:whether the value of the 'JMS Timestamp' attribute is set.See Also:unsetJMSTimestamp(), 
getJMSTimestamp(), 
setJMSTimestamp(long)
    - getJMSCorrelationID
java.lang.String getJMSCorrelationID()
Returns the value of the 'JMS Correlation ID' attribute.
Returns:the value of the 'JMS Correlation ID' attribute.See Also:setJMSCorrelationID(String)
    - setJMSCorrelationID
void setJMSCorrelationID(java.lang.String value)
Sets the value of the 'JMS Correlation ID' attribute.
Parameters:value - the new value of the 'JMS Correlation ID' attribute.See Also:getJMSCorrelationID()
    - getJMSReplyTo
java.lang.String getJMSReplyTo()
Returns the value of the 'JMS Reply To' attribute.
Returns:the value of the 'JMS Reply To' attribute.See Also:setJMSReplyTo(String)
    - setJMSReplyTo
void setJMSReplyTo(java.lang.String value)
Sets the value of the 'JMS Reply To' attribute.
Parameters:value - the new value of the 'JMS Reply To' attribute.See Also:getJMSReplyTo()
    - isJMSRedelivered
boolean isJMSRedelivered()
Returns the value of the 'JMS Redelivered' attribute.
Returns:the value of the 'JMS Redelivered' attribute.See Also:isSetJMSRedelivered(), 
unsetJMSRedelivered(), 
setJMSRedelivered(boolean)
    - setJMSRedelivered
void setJMSRedelivered(boolean value)
Sets the value of the 'JMS Redelivered' attribute.
Parameters:value - the new value of the 'JMS Redelivered' attribute.See Also:isSetJMSRedelivered(), 
unsetJMSRedelivered(), 
isJMSRedelivered()
    - unsetJMSRedelivered
void unsetJMSRedelivered()
Unsets the value of the 'JMS Redelivered' attribute.
See Also:isSetJMSRedelivered(), 
isJMSRedelivered(), 
setJMSRedelivered(boolean)
    - isSetJMSRedelivered
boolean isSetJMSRedelivered()
Returns whether the value of the 'JMS Redelivered' attribute is set.
Returns:whether the value of the 'JMS Redelivered' attribute is set.See Also:unsetJMSRedelivered(), 
isJMSRedelivered(), 
setJMSRedelivered(boolean)
    - getJMSType
java.lang.String getJMSType()
Returns the value of the 'JMS Type' attribute.
Returns:the value of the 'JMS Type' attribute.See Also:setJMSType(String)
    - setJMSType
void setJMSType(java.lang.String value)
Sets the value of the 'JMS Type' attribute.
Parameters:value - the new value of the 'JMS Type' attribute.See Also:getJMSType()
    - getJMSExpiration
long getJMSExpiration()
Returns the value of the 'JMS Expiration' attribute.
Returns:the value of the 'JMS Expiration' attribute.See Also:isSetJMSExpiration(), 
unsetJMSExpiration(), 
setJMSExpiration(long)
    - setJMSExpiration
void setJMSExpiration(long value)
Sets the value of the 'JMS Expiration' attribute.
Parameters:value - the new value of the 'JMS Expiration' attribute.See Also:isSetJMSExpiration(), 
unsetJMSExpiration(), 
getJMSExpiration()
    - unsetJMSExpiration
void unsetJMSExpiration()
Unsets the value of the 'JMS Expiration' attribute.
See Also:isSetJMSExpiration(), 
getJMSExpiration(), 
setJMSExpiration(long)
    - isSetJMSExpiration
boolean isSetJMSExpiration()
Returns whether the value of the 'JMS Expiration' attribute is set.
Returns:whether the value of the 'JMS Expiration' attribute is set.See Also:unsetJMSExpiration(), 
getJMSExpiration(), 
setJMSExpiration(long)
    - getJMSPriority
java.math.BigInteger getJMSPriority()
Returns the value of the 'JMS Priority' attribute.
Returns:the value of the 'JMS Priority' attribute.See Also:setJMSPriority(BigInteger)
    - setJMSPriority
void setJMSPriority(java.math.BigInteger value)
Sets the value of the 'JMS Priority' attribute.
Parameters:value - the new value of the 'JMS Priority' attribute.See Also:getJMSPriority()