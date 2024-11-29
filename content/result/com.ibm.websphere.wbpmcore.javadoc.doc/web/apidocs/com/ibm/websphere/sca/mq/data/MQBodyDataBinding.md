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

## Interface MQBodyDataBinding

- All Superinterfaces:
commonj.connector.runtime.DataBinding, java.io.Serializable

All Known Subinterfaces:
MQBodyObjectBinding

public interface MQBodyDataBinding
extends commonj.connector.runtime.DataBinding
A DataBinding represents the mapping between a native data
 format and an SDO DataObject, and vice-versa. 
 This interface is an extension of
 commonj.connector.runtime.DataBinding, and presents a
 WMQ-specific view which should be implemented for use in WMQ
 Exports and Imports. 
 It exposes methods which read and write to and from a WMQ
 message, as well as exporting which format of WMQ message is
 supported.
See Also:DataBinding

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getFormat () Called by the runtime to determine the WMQ header format supported by this DataBinding. boolean isBusinessException () Queries the DataBinding to determine whether the received message contains a fault (carried within a BusinessException). void read (MQMD md, java.util.List headers, MQDataInputStream input) Read the contents of the incoming WMQ message components into a DataObject. void setBusinessException (boolean isBusinessException) This method is called by the runtime if the outgoing message contains a BusinessException. void setFormat (java.lang.String format) Called before both the read and write methods, and contains the MQ format string identifying the format of the WMQ message body. void write (MQMD md, java.util.List headers, MQDataOutputStream output) Write the DataObject into an outgoing WMQ message.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                                |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String    | getFormat() Called by the runtime to determine the WMQ header format  supported by this DataBinding.                                                                  |
| boolean             | isBusinessException() Queries the DataBinding to determine whether the received  message contains a fault (carried within a  BusinessException).                      |
| void                | read(MQMD md,     java.util.List headers,     MQDataInputStream input) Read the contents of the incoming WMQ message components into  a DataObject.                   |
| void                | setBusinessException(boolean isBusinessException) This method is called by the runtime if the outgoing message  contains a BusinessException.                         |
| void                | setFormat(java.lang.String format) Called before both the read and  write methods, and contains the MQ format string  identifying the format of the WMQ message body. |
| void                | write(MQMD md,      java.util.List headers,      MQDataOutputStream output) Write the DataObject into an outgoing WMQ message.                                        |

- Methods inherited from interface commonj.connector.runtime.DataBinding
getDataObject, setDataObject