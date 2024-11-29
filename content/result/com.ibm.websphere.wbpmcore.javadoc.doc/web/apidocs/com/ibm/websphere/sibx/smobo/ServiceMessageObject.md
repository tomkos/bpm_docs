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

## Interface ServiceMessageObject

- All Superinterfaces: commonj.sdo.DataObject, java.io.Serializable public interface ServiceMessageObject extends commonj.sdo.DataObject Provides the interface for the Service Message Object. The following features are supported:

```
public interface ServiceMessageObject
extends commonj.sdo.DataObject
```

The following features are supported:
 
Context
Headers
Body

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT 

static java.lang.String
SMO\_EXCEPTION\_TYPE
This is the value set into the MessageType field of the SMOHeader
 when the SMO represents an exception message.

static java.lang.String
SMO\_REQUEST\_TYPE
This is the value set into the MessageType field of the SMOHeader
 when the SMO represents a request message.

static java.lang.String
SMO\_RESPONSE\_TYPE
This is the value set into the MessageType field of the SMOHeader
 when the SMO represents a response message.

static java.lang.String
UNMODELLED\_FAULT\_ORIGIN
This is the value set into the failInfo.origin field for an
 unmodelled fault
    - Method Summary Methods Modifier and Type Method and Description AttachmentType addAttachment (java.lang.String contentID, java.lang.String contentType, byte[] data) Creates a new attachment with the provided content and adds it to the ServiceMessageObject. AttachmentType getAttachment (java.lang.String contentID) Searches the ServiceMessageObject for an attachment with the given 'contentID ' and returns the attachment. byte[] getAttachmentData (java.lang.String contentID) Searches the ServiceMessageObject for an attachment with the given 'contentID ' and returns the value of the 'Data ' attribute of the attachment. java.util.List<AttachmentType > getAttachments () Returns the value of the 'Attachments ' containment reference list. java.lang.Object getBody () Returns the value of the 'Body ' containment reference. java.lang.Object getBodyForSCAMessage (boolean isFaultMessage, boolean copySMOBody) Deprecated. boolean getBodyPopulated () Deprecated. ContextType getContext () Returns the value of the 'Context ' containment reference. HeadersType getHeaders () Returns the value of the 'Headers ' containment reference. boolean getSoapFaultInfoPopulated () Deprecated. AttachmentType removeAttachment (java.lang.String contentID) Searches the ServiceMessageObject for an attachment with the given 'contentID ' and removes the attachment from the ServiceMessageObject. void saveSCAData (com.ibm.wsspi.sca.message.Message donorSCAMessage, ServiceMessageObject requestSMO) Deprecated. void setBody (java.lang.Object value) Sets the value of the 'Body ' containment reference. void setBodyPopulated () Deprecated. void setContext (ContextType value) Sets the value of the 'Context ' containment reference. void setHeaders (HeadersType value) Sets the value of the 'Headers ' containment reference. void setSoapFaultInfoPopulated () Deprecated.

### Method Summary

| Modifier and Type              | Method and Description                                                                                                                                                                                       |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AttachmentType                 | addAttachment(java.lang.String contentID,              java.lang.String contentType,              byte[] data) Creates a new attachment with the provided content and adds it to   the ServiceMessageObject. |
| AttachmentType                 | getAttachment(java.lang.String contentID) Searches the ServiceMessageObject for an attachment with the given 'contentID'  and returns the attachment.                                                        |
| byte[]                         | getAttachmentData(java.lang.String contentID) Searches the ServiceMessageObject for an attachment with the given 'contentID'  and returns the value of the 'Data' attribute of the attachment.               |
| java.util.List<AttachmentType> | getAttachments() Returns the value of the 'Attachments' containment reference list.                                                                                                                          |
| java.lang.Object               | getBody() Returns the value of the 'Body' containment reference.                                                                                                                                             |
| java.lang.Object               | getBodyForSCAMessage(boolean isFaultMessage,                     boolean copySMOBody) Deprecated.                                                                                                            |
| boolean                        | getBodyPopulated() Deprecated.                                                                                                                                                                               |
| ContextType                    | getContext() Returns the value of the 'Context' containment reference.                                                                                                                                       |
| HeadersType                    | getHeaders() Returns the value of the 'Headers' containment reference.                                                                                                                                       |
| boolean                        | getSoapFaultInfoPopulated() Deprecated.                                                                                                                                                                      |
| AttachmentType                 | removeAttachment(java.lang.String contentID) Searches the ServiceMessageObject for an attachment with the given 'contentID'  and removes the attachment from the ServiceMessageObject.                       |
| void                           | saveSCAData(com.ibm.wsspi.sca.message.Message donorSCAMessage,            ServiceMessageObject requestSMO) Deprecated.                                                                                       |
| void                           | setBody(java.lang.Object value) Sets the value of the 'Body' containment reference.                                                                                                                          |
| void                           | setBodyPopulated() Deprecated.                                                                                                                                                                               |
| void                           | setContext(ContextType value) Sets the value of the 'Context' containment reference.                                                                                                                         |
| void                           | setHeaders(HeadersType value) Sets the value of the 'Headers' containment reference.                                                                                                                         |
| void                           | setSoapFaultInfoPopulated() Deprecated.                                                                                                                                                                      |

- Methods inherited from interface commonj.sdo.DataObject
createDataObject, createDataObject, createDataObject, createDataObject, createDataObject, createDataObject, delete, detach, get, get, get, getBigDecimal, getBigDecimal, getBigDecimal, getBigInteger, getBigInteger, getBigInteger, getBoolean, getBoolean, getBoolean, getByte, getByte, getByte, getBytes, getBytes, getBytes, getChangeSummary, getChar, getChar, getChar, getContainer, getContainmentProperty, getDataGraph, getDataObject, getDataObject, getDataObject, getDate, getDate, getDate, getDouble, getDouble, getDouble, getFloat, getFloat, getFloat, getInstanceProperties, getInstanceProperty, getInt, getInt, getInt, getList, getList, getList, getLong, getLong, getLong, getProperty, getRootObject, getSequence, getSequence, getSequence, getSequence, getShort, getShort, getShort, getString, getString, getString, getType, isSet, isSet, isSet, set, set, set, setBigDecimal, setBigDecimal, setBigDecimal, setBigInteger, setBigInteger, setBigInteger, setBoolean, setBoolean, setBoolean, setByte, setByte, setByte, setBytes, setBytes, setBytes, setChar, setChar, setChar, setDataObject, setDataObject, setDataObject, setDate, setDate, setDate, setDouble, setDouble, setDouble, setFloat, setFloat, setFloat, setInt, setInt, setInt, setList, setList, setList, setLong, setLong, setLong, setShort, setShort, setShort, setString, setString, setString, unset, unset, unset