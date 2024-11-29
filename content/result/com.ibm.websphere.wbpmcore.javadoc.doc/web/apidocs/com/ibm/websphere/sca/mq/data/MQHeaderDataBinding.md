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

## Interface MQHeaderDataBinding

- All Superinterfaces:
commonj.connector.runtime.DataBinding, java.io.Serializable

public interface MQHeaderDataBinding
extends commonj.connector.runtime.DataBinding
A DataBinding represents the mapping between a native data
 format and an SDO DataObject, and vice-versa. 
 This interface is an extension of
 commonj.connector.runtime.DataBinding, and presents a
 WMQ-specific view which should be implemented for use in WMQ
 Exports and Imports specifically for support of WMQ headers.
 
 It exposes methods which read and write a WMQ header to and
 from a WMQ message, as well as exporting which format of WMQ
 message is supported, and the associated control data: CCSID,
 encoding and format.
See Also:DataBinding

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description int getNextCCSID () Called by the runtime after the read method and used to "unchain" the WMQ header context chaining. int getNextEncoding () Called by the runtime after the read method and used to "unchain" the WMQ header context chaining. java.lang.String getNextFormat () Called by the runtime after the read method and used to "unchain" the WMQ header context chaining. boolean isSupportedFormat (java.lang.String format) Called by the runtime to determine whether this MQHeaderDataBinding supports a particular WMQ header format. void read (java.lang.String format, MQDataInputStream input) Read the contents of the an incoming WMQ header into its DataObject representation. void setNextCCSID (int ccsid) Called by the runtime before the write method and used to "rechain" the WMQ header context chaining. void setNextEncoding (int encoding) Called by the runtime before the write method and used to "rechain" the WMQ header context chaining. void setNextFormat (java.lang.String format) Called by the runtime before the write method and used to "rechain" the WMQ header context chaining. void write (java.lang.String format, MQDataOutputStream output) Write the header DataObject representation into an outgoing WMQ message header.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                   |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| int                 | getNextCCSID() Called by the runtime after the read method and  used to "unchain" the WMQ header context chaining.                                       |
| int                 | getNextEncoding() Called by the runtime after the read method and  used to "unchain" the WMQ header context chaining.                                    |
| java.lang.String    | getNextFormat() Called by the runtime after the read method and  used to "unchain" the WMQ header context chaining.                                      |
| boolean             | isSupportedFormat(java.lang.String format) Called by the runtime to determine whether this  MQHeaderDataBinding supports a particular WMQ header format. |
| void                | read(java.lang.String format,     MQDataInputStream input) Read the contents of the an incoming WMQ header into its  DataObject representation.          |
| void                | setNextCCSID(int ccsid) Called by the runtime before the write method  and used to "rechain" the WMQ header context chaining.                            |
| void                | setNextEncoding(int encoding) Called by the runtime before the write method  and used to "rechain" the WMQ header context chaining.                      |
| void                | setNextFormat(java.lang.String format) Called by the runtime before the write method  and used to "rechain" the WMQ header context chaining.             |
| void                | write(java.lang.String format,      MQDataOutputStream output) Write the header DataObject representation into an outgoing  WMQ message header.          |

- Methods inherited from interface commonj.connector.runtime.DataBinding
getDataObject, setDataObject