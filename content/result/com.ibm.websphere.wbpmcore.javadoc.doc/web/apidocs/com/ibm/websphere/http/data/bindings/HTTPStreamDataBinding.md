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

## Interface HTTPStreamDataBinding

- All Superinterfaces: commonj.connector.runtime.DataBinding, java.io.Serializable public interface HTTPStreamDataBinding extends commonj.connector.runtime.DataBinding A DataBinding maps between a native data format and an SDO DataObject, and vice-versa. This interface is an extension of commonj.connector.runtime.DataBinding, and presents a HTTP-specific view which should be implemented for use in HTTP Binding Exports and Imports. HTTP Binding will invoke Data Binding in the following order:

```
public interface HTTPStreamDataBinding
extends commonj.connector.runtime.DataBinding
```

HTTP Binding will invoke Data Binding in the following order:
 
 1. Outbound processing (SDO to Native format):
 
1.1 setDataObject (...)
1.2 setHeaders(...)
1.3 setControlParameters(...)
1.4 setBusinessException(...)
1.5 convertToNativeData()
1.6 getControlParameters()
1.7 getHeaders()
1.8 write(...)

 2. Inbound processing (Native format to SDO):
 
2.1 setControlParameters(...)
2.2 setHeaders(...)
2.3 convertFromNativeData(...)
2.4 isBusinessException()
2.5 getDataObject()
2.6 getControlParameters()
2.7 getHeaders()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description void convertFromNativeData (HTTPInputStream input) Convert native data to SDO. void convertToNativeData () Convert SDO to native data. HTTPControl getControlParameters () Get HTTP control parameters. HTTPHeaders getHeaders () Get HTTP headers. boolean isBusinessException () Determines whether the message is a fault. void setBusinessException (boolean isBusinessException) Indicate to the Data Binding that data is a fault object. void setControlParameters (HTTPControl cp) Set HTTP control parameters. void setHeaders (HTTPHeaders headers) Set HTTP headers. void write (HTTPOutputStream output) Write native data to HTTPOutputStream after it has been converted by convertToNativeData() method.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                            |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| void                | convertFromNativeData(HTTPInputStream input) Convert native data to SDO.                                                          |
| void                | convertToNativeData() Convert SDO to native data.                                                                                 |
| HTTPControl         | getControlParameters() Get HTTP control parameters.                                                                               |
| HTTPHeaders         | getHeaders() Get HTTP headers.                                                                                                    |
| boolean             | isBusinessException() Determines whether the message is a fault.                                                                  |
| void                | setBusinessException(boolean isBusinessException) Indicate to the Data Binding that data is a fault object.                       |
| void                | setControlParameters(HTTPControl cp) Set HTTP control parameters.                                                                 |
| void                | setHeaders(HTTPHeaders headers) Set HTTP headers.                                                                                 |
| void                | write(HTTPOutputStream output) Write native data to HTTPOutputStream after it has been converted by convertToNativeData() method. |

- Methods inherited from interface commonj.connector.runtime.DataBinding
getDataObject, setDataObject