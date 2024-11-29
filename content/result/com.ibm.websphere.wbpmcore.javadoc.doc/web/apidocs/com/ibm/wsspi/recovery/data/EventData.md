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

## Interface EventData

- All Superinterfaces:
java.io.Serializable

public interface EventData
extends java.io.Serializable
The  EventData  interface defines the information of a failed event.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static java.lang.String
DATA\_TYPE\_BYTES
Data types of the payload.

static java.lang.String
DATA\_TYPE\_OBJECT 

static java.lang.String
DATA\_TYPE\_TEXT
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getDataType()
Return data type of the payload.

java.lang.String
getEventId()
Return the event identifier.

HeadersType
getHeaders()
Return the headers which can contain JMS/MQ header information.

java.io.InputStream
getInputStream()
Obtain InputStream to read the payload.

java.lang.Object
getObject()
Obtain the Object representing the payload.

java.io.OutputStream
getOutputStream()
Obtain OutputStream to write the payload.

java.io.Reader
getReader()
Obtain Reader to read the payload.

java.io.Writer
getWriter()
Obtain Writer to write the payload.

void
setDataType(java.lang.String dataType)
Set data type of the payload.

void
setEventId(java.lang.String eventId)
Set event identifier.

void
setHeaders(HeadersType headers)
Set headers.

void
setObject(java.lang.Object object)
Set object as new payload.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- DATA\_TYPE\_BYTES
static final java.lang.String DATA\_TYPE\_BYTES
Data types of the payload.
See Also:Constant Field Values

- DATA\_TYPE\_TEXT
static final java.lang.String DATA\_TYPE\_TEXT
See Also:Constant Field Values

- DATA\_TYPE\_OBJECT
static final java.lang.String DATA\_TYPE\_OBJECT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getEventId
java.lang.String getEventId()
Return the event identifier.
Returns:event identifier
    - setEventId
void setEventId(java.lang.String eventId)
Set event identifier.
Parameters:eventId -
    - getDataType
java.lang.String getDataType()
Return data type of the payload.
  TEXT 
 BYTES 
 OBJECT 
Returns:payload data type
    - setDataType
void setDataType(java.lang.String dataType)
Set data type of the payload.
Parameters:dataType -
    - getHeaders
HeadersType getHeaders()
Return the headers which can contain JMS/MQ header information.
Returns:headers
    - setHeaders
void setHeaders(HeadersType headers)
Set headers.
Parameters:headers -
    - getInputStream
java.io.InputStream getInputStream()
Obtain InputStream to read the payload.
Returns:InputStream
    - getOutputStream
java.io.OutputStream getOutputStream()
Obtain OutputStream to write the payload.
Returns:OutputStream
    - getReader
java.io.Reader getReader()
Obtain Reader to read the payload.
Returns:Reader
    - getWriter
java.io.Writer getWriter()
Obtain Writer to write the payload.
Returns:Writer
    - getObject
java.lang.Object getObject()
Obtain the Object representing the payload.
Returns:payload as object
    - setObject
void setObject(java.lang.Object object)
Set object as new payload.
Parameters:object -