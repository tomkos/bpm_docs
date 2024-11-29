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

## Interface JMSDataBinding

- All Superinterfaces:
commonj.connector.runtime.DataBinding, java.io.Serializable

All Known Subinterfaces:
JMSObjectBinding

All Known Implementing Classes:
JMSDataBindingImplJava, JMSDataBindingImplXML

public interface JMSDataBinding
extends commonj.connector.runtime.DataBinding
A DataBinding represents the mapping between a native data
 format and an SDO DataObject, and vice-versa. 
 This interface is an extension of
 commonj.connector.runtime.DataBinding, and presents a
 JMS-specific view which should be implemented for use in JMS
 Exports and Imports. 
 It exposes methods which read and write to and from a JMS
 message, as well as exporting which type of JMS message is
 supported.
See Also:DataBinding

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static int
ANY\_MESSAGE 

static int
BASE\_MESSAGE 

static int
BYTES\_MESSAGE 

static java.lang.String
COPYRIGHT 

static int
MAP\_MESSAGE 

static int
OBJECT\_MESSAGE 

static int
STREAM\_MESSAGE 

static int
TEXT\_MESSAGE
    - Method Summary Methods Modifier and Type Method and Description int getMessageType () Return the message type that is supported by this data binding. boolean isBusinessException () Queries the DataBinding to determine whether the received message contains a fault (carried within a BusinessException). void read (javax.jms.Message message) Read the contents of the incoming JMS Message into a DataObject. void setBusinessException (boolean isBusinessException) This method is called by the runtime if the outgoing message contains a BusinessException. void write (javax.jms.Message message) Write the DataObject into an outgoing JMS Message.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                           |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| int                 | getMessageType() Return the message type that is supported by this data  binding.                                                                |
| boolean             | isBusinessException() Queries the DataBinding to determine whether the received  message contains a fault (carried within a  BusinessException). |
| void                | read(javax.jms.Message message) Read the contents of the incoming JMS Message into a  DataObject.                                                |
| void                | setBusinessException(boolean isBusinessException) This method is called by the runtime if the outgoing message  contains a BusinessException.    |
| void                | write(javax.jms.Message message) Write the DataObject into an outgoing JMS Message.                                                              |

- Methods inherited from interface commonj.connector.runtime.DataBinding
getDataObject, setDataObject