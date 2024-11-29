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

## Interface HTTPControl

- public interface HTTPControl begin-user-doc A representation of the model object 'HTTP Control '. end-user-doc The following features are supported: See Also: HeadersPackage.getHTTPControl()

```
public interface HTTPControl
```

The following features are supported:
 
URL
Version
Method
Dynamic Override URL
Dynamic Override Version
Dynamic Override Method
Media Type
Charset
Transfer Encoding
Content Encoding
Status Code
Reason Phrase
Content Length
Export Context Path
Authentication
SSL Settings
Proxy Settings

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

HTTPAuthentication
getAuthentication()
Returns the value of the 'Authentication' containment reference.

java.lang.String
getCharset()
Returns the value of the 'Charset' attribute.

java.lang.String
getContentEncoding()
Returns the value of the 'Content Encoding' attribute.

int
getContentLength()
Returns the value of the 'HTTP Message Content Length' attribute.

java.lang.String
getDynamicOverrideMethod()
Returns the value of the 'Dynamic Override HTTP Method' attribute.

java.lang.String
getDynamicOverrideURL()
Returns the value of the 'Dynamic Override URL' attribute.

HTTPVersion
getDynamicOverrideVersion()
Returns the value of the 'Dynamic Override Version' attribute.

java.lang.String
getExportContextPath()
Returns the value of the 'HTTP Export Request Context Path' attribute.

java.lang.String
getMediaType()
Returns the value of the 'Media Type' attribute.

java.lang.String
getMethod()
Returns the value of the 'HTTP Method' attribute.

java.util.List
getProxySettings()
Returns the value of the 'Proxy Settings' containment reference list.

java.lang.String
getReasonPhrase()
Returns the value of the 'HTTP Response Reason Phrase' attribute.

HTTPSSLSettings
getSSLSettings()
Returns the value of the 'SSL Settings' containment reference.

int
getStatusCode()
Returns the value of the 'HTTP Status Code' attribute.

java.lang.String
getTransferEncoding()
Returns the value of the 'Transfer Encoding' attribute.

java.lang.String
getURL()
Returns the value of the 'URL' attribute.

HTTPVersion
getVersion()
Returns the value of the 'Version' attribute.

boolean
isSetAuthentication()
Returns whether the value of the 'Authentication' containment reference is set

boolean
isSetCharset()
Returns whether the value of the 'Charset' attribute is set

boolean
isSetContentEncoding()
Returns whether the value of the 'Content Encoding' attribute is set

boolean
isSetContentLength()
Returns whether the value of the 'Content Length' attribute is set

boolean
isSetDynamicOverrideMethod()
Returns whether the value of the 'Dynamic Override Method' attribute is set

boolean
isSetDynamicOverrideURL()
Returns whether the value of the 'Dynamic Override URL' attribute is set

boolean
isSetDynamicOverrideVersion()
Returns whether the value of the 'Dynamic Override Version' attribute is set

boolean
isSetExportContextPath()
Returns whether the value of the 'Export Context Path' attribute is set

boolean
isSetMediaType()
Returns whether the value of the 'Media Type' attribute is set

boolean
isSetMethod()
Returns whether the value of the 'Method' attribute is set

boolean
isSetReasonPhrase()
Returns whether the value of the 'Reason Phrase' attribute is set

boolean
isSetSSLSettings()
Returns whether the value of the 'SSL Settings' containment reference is set

boolean
isSetStatusCode()
Returns whether the value of the 'Status Code' attribute is set

boolean
isSetTransferEncoding()
Returns whether the value of the 'Transfer Encoding' attribute is set

boolean
isSetURL()
Returns whether the value of the 'URL' attribute is set

boolean
isSetVersion()
Returns whether the value of the 'Version' attribute is set

void
setAuthentication(HTTPAuthentication value)
Sets the value of the 'Authentication' containment reference

void
setCharset(java.lang.String value)
Sets the value of the 'Charset' attribute

void
setContentEncoding(java.lang.String value)
Sets the value of the 'Content Encoding' attribute

void
setContentLength(int value)
Sets the value of the 'Content Length' attribute

void
setDynamicOverrideMethod(java.lang.String value)
Sets the value of the 'Dynamic Override Method' attribute

void
setDynamicOverrideURL(java.lang.String value)
Sets the value of the 'Dynamic Override URL' attribute

void
setDynamicOverrideVersion(HTTPVersion value)
Sets the value of the 'Dynamic Override Version' attribute

void
setExportContextPath(java.lang.String value)
Sets the value of the 'Export Context Path' attribute

void
setMediaType(java.lang.String value)
Sets the value of the 'Media Type' attribute

void
setMethod(java.lang.String value)
Sets the value of the 'Method' attribute

void
setReasonPhrase(java.lang.String value)
Sets the value of the 'Reason Phrase' attribute

void
setSSLSettings(HTTPSSLSettings value)
Sets the value of the 'SSL Settings' containment reference

void
setStatusCode(int value)
Sets the value of the 'Status Code' attribute

void
setTransferEncoding(java.lang.String value)
Sets the value of the 'Transfer Encoding' attribute

void
setURL(java.lang.String value)
Sets the value of the 'URL' attribute

void
setVersion(HTTPVersion value)
Sets the value of the 'Version' attribute

void
unsetAuthentication()
Unsets the value of the 'Authentication' containment reference

void
unsetCharset()
Unsets the value of the 'Charset' attribute

void
unsetContentEncoding()
Unsets the value of the 'Content Encoding' attribute

void
unsetContentLength()
Unsets the value of the 'Content Length' attribute

void
unsetDynamicOverrideMethod()
Unsets the value of the 'Dynamic Override Method' attribute

void
unsetDynamicOverrideURL()
Unsets the value of the 'Dynamic Override URL' attribute

void
unsetDynamicOverrideVersion()
Unsets the value of the 'Dynamic Override Version' attribute

void
unsetExportContextPath()
Unsets the value of the 'Export Context Path' attribute

void
unsetMediaType()
Unsets the value of the 'Media Type' attribute

void
unsetMethod()
Unsets the value of the 'Method' attribute

void
unsetReasonPhrase()
Unsets the value of the 'Reason Phrase' attribute

void
unsetSSLSettings()
Unsets the value of the 'SSL Settings' containment reference

void
unsetStatusCode()
Unsets the value of the 'Status Code' attribute

void
unsetTransferEncoding()
Unsets the value of the 'Transfer Encoding' attribute

void
unsetURL()
Unsets the value of the 'URL' attribute

void
unsetVersion()
Unsets the value of the 'Version' attribute

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getURL
java.lang.String getURL()
Returns the value of the 'URL' attribute.
Returns:the value of the 'URL' attribute.See Also:isSetURL(), 
unsetURL(), 
setURL(String), 
HeadersPackage.getHTTPControl\_URL()
    - setURL
void setURL(java.lang.String value)
Sets the value of the 'URL' attribute.
 

Parameters:value - the new value of the 'URL' attribute.See Also:isSetURL(), 
unsetURL(), 
getURL()
    - unsetURL
void unsetURL()
Unsets the value of the 'URL' attribute.
 

See Also:isSetURL(), 
getURL(), 
setURL(String)
    - isSetURL
boolean isSetURL()
Returns whether the value of the 'URL' attribute is set.
 

Returns:whether the value of the 'URL' attribute is set.See Also:unsetURL(), 
getURL(), 
setURL(String)
    - getVersion
HTTPVersion getVersion()
Returns the value of the 'Version' attribute.
 The default value is "1.0".
Returns:the value of the 'Version' attribute.See Also:isSetVersion(), 
unsetVersion(), 
setVersion(HTTPVersion), 
HeadersPackage.getHTTPControl\_Version()
    - setVersion
void setVersion(HTTPVersion value)
Sets the value of the 'Version' attribute.
 

Parameters:value - the new value of the 'Version' attribute.See Also:isSetVersion(), 
unsetVersion(), 
getVersion()
    - unsetVersion
void unsetVersion()
Unsets the value of the 'Version' attribute.
 

See Also:isSetVersion(), 
getVersion(), 
setVersion(HTTPVersion)
    - isSetVersion
boolean isSetVersion()
Returns whether the value of the 'Version' attribute is set.
 

Returns:whether the value of the 'Version' attribute is set.See Also:unsetVersion(), 
getVersion(), 
setVersion(HTTPVersion)
    - getMethod
java.lang.String getMethod()
Returns the value of the 'HTTP Method' attribute.
Returns:the value of the 'HTTP Method' attribute.See Also:isSetMethod(), 
unsetMethod(), 
setMethod(String), 
HeadersPackage.getHTTPControl\_Method()
    - setMethod
void setMethod(java.lang.String value)
Sets the value of the 'Method' attribute.
 

Parameters:value - the new value of the 'Method' attribute.See Also:isSetMethod(), 
unsetMethod(), 
getMethod()
    - unsetMethod
void unsetMethod()
Unsets the value of the 'Method' attribute.
 

See Also:isSetMethod(), 
getMethod(), 
setMethod(String)
    - isSetMethod
boolean isSetMethod()
Returns whether the value of the 'Method' attribute is set.
 

Returns:whether the value of the 'Method' attribute is set.See Also:unsetMethod(), 
getMethod(), 
setMethod(String)
    - getDynamicOverrideURL
java.lang.String getDynamicOverrideURL()
Returns the value of the 'Dynamic Override URL' attribute.
Returns:the value of the 'Dynamic Override URL' attribute.See Also:isSetDynamicOverrideURL(), 
unsetDynamicOverrideURL(), 
setDynamicOverrideURL(String), 
HeadersPackage.getHTTPControl\_DynamicOverrideURL()
    - setDynamicOverrideURL
void setDynamicOverrideURL(java.lang.String value)
Sets the value of the 'Dynamic Override URL' attribute.
 

Parameters:value - the new value of the 'Dynamic Override URL' attribute.See Also:isSetDynamicOverrideURL(), 
unsetDynamicOverrideURL(), 
getDynamicOverrideURL()
    - unsetDynamicOverrideURL
void unsetDynamicOverrideURL()
Unsets the value of the 'Dynamic Override URL' attribute.
 

See Also:isSetDynamicOverrideURL(), 
getDynamicOverrideURL(), 
setDynamicOverrideURL(String)
    - isSetDynamicOverrideURL
boolean isSetDynamicOverrideURL()
Returns whether the value of the 'Dynamic Override URL' attribute is set.
 

Returns:whether the value of the 'Dynamic Override URL' attribute is set.See Also:unsetDynamicOverrideURL(), 
getDynamicOverrideURL(), 
setDynamicOverrideURL(String)
    - getDynamicOverrideVersion
HTTPVersion getDynamicOverrideVersion()
Returns the value of the 'Dynamic Override Version' attribute.
 The default value is "1.0".
Returns:the value of the 'Dynamic Override Version' attribute.See Also:isSetDynamicOverrideVersion(), 
unsetDynamicOverrideVersion(), 
setDynamicOverrideVersion(HTTPVersion), 
HeadersPackage.getHTTPControl\_DynamicOverrideVersion()
    - setDynamicOverrideVersion
void setDynamicOverrideVersion(HTTPVersion value)
Sets the value of the 'Dynamic Override Version' attribute.
 

Parameters:value - the new value of the 'Dynamic Override Version' attribute.See Also:isSetDynamicOverrideVersion(), 
unsetDynamicOverrideVersion(), 
getDynamicOverrideVersion()
    - unsetDynamicOverrideVersion
void unsetDynamicOverrideVersion()
Unsets the value of the 'Dynamic Override Version' attribute.
 

See Also:isSetDynamicOverrideVersion(), 
getDynamicOverrideVersion(), 
setDynamicOverrideVersion(HTTPVersion)
    - isSetDynamicOverrideVersion
boolean isSetDynamicOverrideVersion()
Returns whether the value of the 'Dynamic Override Version' attribute is set.
 

Returns:whether the value of the 'Dynamic Override Version' attribute is set.See Also:unsetDynamicOverrideVersion(), 
getDynamicOverrideVersion(), 
setDynamicOverrideVersion(HTTPVersion)
    - getDynamicOverrideMethod
java.lang.String getDynamicOverrideMethod()
Returns the value of the 'Dynamic Override HTTP Method' attribute.
Returns:the value of the 'Dynamic Override HTTP Method' attribute.See Also:isSetDynamicOverrideMethod(), 
unsetDynamicOverrideMethod(), 
setDynamicOverrideMethod(String), 
HeadersPackage.getHTTPControl\_DynamicOverrideMethod()
    - setDynamicOverrideMethod
void setDynamicOverrideMethod(java.lang.String value)
Sets the value of the 'Dynamic Override Method' attribute.
 

Parameters:value - the new value of the 'Dynamic Override Method' attribute.See Also:isSetDynamicOverrideMethod(), 
unsetDynamicOverrideMethod(), 
getDynamicOverrideMethod()
    - unsetDynamicOverrideMethod
void unsetDynamicOverrideMethod()
Unsets the value of the 'Dynamic Override Method' attribute.
 

See Also:isSetDynamicOverrideMethod(), 
getDynamicOverrideMethod(), 
setDynamicOverrideMethod(String)
    - isSetDynamicOverrideMethod
boolean isSetDynamicOverrideMethod()
Returns whether the value of the 'Dynamic Override Method' attribute is set.
 

Returns:whether the value of the 'Dynamic Override Method' attribute is set.See Also:unsetDynamicOverrideMethod(), 
getDynamicOverrideMethod(), 
setDynamicOverrideMethod(String)
    - getMediaType
java.lang.String getMediaType()
Returns the value of the 'Media Type' attribute.
Returns:the value of the 'Media Type' attribute.See Also:isSetMediaType(), 
unsetMediaType(), 
setMediaType(String), 
HeadersPackage.getHTTPControl\_MediaType()
    - setMediaType
void setMediaType(java.lang.String value)
Sets the value of the 'Media Type' attribute.
 

Parameters:value - the new value of the 'Media Type' attribute.See Also:isSetMediaType(), 
unsetMediaType(), 
getMediaType()
    - unsetMediaType
void unsetMediaType()
Unsets the value of the 'Media Type' attribute.
 

See Also:isSetMediaType(), 
getMediaType(), 
setMediaType(String)
    - isSetMediaType
boolean isSetMediaType()
Returns whether the value of the 'Media Type' attribute is set.
 

Returns:whether the value of the 'Media Type' attribute is set.See Also:unsetMediaType(), 
getMediaType(), 
setMediaType(String)
    - getCharset
java.lang.String getCharset()
Returns the value of the 'Charset' attribute.
Returns:the value of the 'Charset' attribute.See Also:isSetCharset(), 
unsetCharset(), 
setCharset(String), 
HeadersPackage.getHTTPControl\_Charset()
    - setCharset
void setCharset(java.lang.String value)
Sets the value of the 'Charset' attribute.
 

Parameters:value - the new value of the 'Charset' attribute.See Also:isSetCharset(), 
unsetCharset(), 
getCharset()
    - unsetCharset
void unsetCharset()
Unsets the value of the 'Charset' attribute.
 

See Also:isSetCharset(), 
getCharset(), 
setCharset(String)
    - isSetCharset
boolean isSetCharset()
Returns whether the value of the 'Charset' attribute is set.
 

Returns:whether the value of the 'Charset' attribute is set.See Also:unsetCharset(), 
getCharset(), 
setCharset(String)
    - getTransferEncoding
java.lang.String getTransferEncoding()
Returns the value of the 'Transfer Encoding' attribute.
Returns:the value of the 'Transfer Encoding' attribute.See Also:isSetTransferEncoding(), 
unsetTransferEncoding(), 
setTransferEncoding(String), 
HeadersPackage.getHTTPControl\_TransferEncoding()
    - setTransferEncoding
void setTransferEncoding(java.lang.String value)
Sets the value of the 'Transfer Encoding' attribute.
 

Parameters:value - the new value of the 'Transfer Encoding' attribute.See Also:isSetTransferEncoding(), 
unsetTransferEncoding(), 
getTransferEncoding()
    - unsetTransferEncoding
void unsetTransferEncoding()
Unsets the value of the 'Transfer Encoding' attribute.
 

See Also:isSetTransferEncoding(), 
getTransferEncoding(), 
setTransferEncoding(String)
    - isSetTransferEncoding
boolean isSetTransferEncoding()
Returns whether the value of the 'Transfer Encoding' attribute is set.
 

Returns:whether the value of the 'Transfer Encoding' attribute is set.See Also:unsetTransferEncoding(), 
getTransferEncoding(), 
setTransferEncoding(String)
    - getContentEncoding
java.lang.String getContentEncoding()
Returns the value of the 'Content Encoding' attribute.
Returns:the value of the 'Content Encoding' attribute.See Also:isSetContentEncoding(), 
unsetContentEncoding(), 
setContentEncoding(String), 
HeadersPackage.getHTTPControl\_ContentEncoding()
    - setContentEncoding
void setContentEncoding(java.lang.String value)
Sets the value of the 'Content Encoding' attribute.
 

Parameters:value - the new value of the 'Content Encoding' attribute.See Also:isSetContentEncoding(), 
unsetContentEncoding(), 
getContentEncoding()
    - unsetContentEncoding
void unsetContentEncoding()
Unsets the value of the 'Content Encoding' attribute.
 

See Also:isSetContentEncoding(), 
getContentEncoding(), 
setContentEncoding(String)
    - isSetContentEncoding
boolean isSetContentEncoding()
Returns whether the value of the 'Content Encoding' attribute is set.
 

Returns:whether the value of the 'Content Encoding' attribute is set.See Also:unsetContentEncoding(), 
getContentEncoding(), 
setContentEncoding(String)
    - getStatusCode
int getStatusCode()
Returns the value of the 'HTTP Status Code' attribute.
Returns:the value of the 'Status Code' attribute.See Also:isSetStatusCode(), 
unsetStatusCode(), 
setStatusCode(int), 
HeadersPackage.getHTTPControl\_StatusCode()
    - setStatusCode
void setStatusCode(int value)
Sets the value of the 'Status Code' attribute.
 

Parameters:value - the new value of the 'Status Code' attribute.See Also:isSetStatusCode(), 
unsetStatusCode(), 
getStatusCode()
    - unsetStatusCode
void unsetStatusCode()
Unsets the value of the 'Status Code' attribute.
 

See Also:isSetStatusCode(), 
getStatusCode(), 
setStatusCode(int)
    - isSetStatusCode
boolean isSetStatusCode()
Returns whether the value of the 'Status Code' attribute is set.
 

Returns:whether the value of the 'Status Code' attribute is set.See Also:unsetStatusCode(), 
getStatusCode(), 
setStatusCode(int)
    - getReasonPhrase
java.lang.String getReasonPhrase()
Returns the value of the 'HTTP Response Reason Phrase' attribute.
Returns:the value of the 'Reason Phrase' attribute.See Also:isSetReasonPhrase(), 
unsetReasonPhrase(), 
setReasonPhrase(String), 
HeadersPackage.getHTTPControl\_ReasonPhrase()
    - setReasonPhrase
void setReasonPhrase(java.lang.String value)
Sets the value of the 'Reason Phrase' attribute.
 

Parameters:value - the new value of the 'Reason Phrase' attribute.See Also:isSetReasonPhrase(), 
unsetReasonPhrase(), 
getReasonPhrase()
    - unsetReasonPhrase
void unsetReasonPhrase()
Unsets the value of the 'Reason Phrase' attribute.
 

See Also:isSetReasonPhrase(), 
getReasonPhrase(), 
setReasonPhrase(String)
    - isSetReasonPhrase
boolean isSetReasonPhrase()
Returns whether the value of the 'Reason Phrase' attribute is set.
 

Returns:whether the value of the 'Reason Phrase' attribute is set.See Also:unsetReasonPhrase(), 
getReasonPhrase(), 
setReasonPhrase(String)
    - getContentLength
int getContentLength()
Returns the value of the 'HTTP Message Content Length' attribute.
Returns:the value of the 'HTTP Message Content Length' attribute.See Also:isSetContentLength(), 
unsetContentLength(), 
setContentLength(int), 
HeadersPackage.getHTTPControl\_ContentLength()
    - setContentLength
void setContentLength(int value)
Sets the value of the 'Content Length' attribute.
 

Parameters:value - the new value of the 'Content Length' attribute.See Also:isSetContentLength(), 
unsetContentLength(), 
getContentLength()
    - unsetContentLength
void unsetContentLength()
Unsets the value of the 'Content Length' attribute.
 

See Also:isSetContentLength(), 
getContentLength(), 
setContentLength(int)
    - isSetContentLength
boolean isSetContentLength()
Returns whether the value of the 'Content Length' attribute is set.
 

Returns:whether the value of the 'Content Length' attribute is set.See Also:unsetContentLength(), 
getContentLength(), 
setContentLength(int)
    - getExportContextPath
java.lang.String getExportContextPath()
Returns the value of the 'HTTP Export Request Context Path' attribute.
Returns:the value of the 'HTTP Export Request Context Path' attribute.See Also:isSetExportContextPath(), 
unsetExportContextPath(), 
setExportContextPath(String), 
HeadersPackage.getHTTPControl\_ExportContextPath()
    - setExportContextPath
void setExportContextPath(java.lang.String value)
Sets the value of the 'Export Context Path' attribute.
 

Parameters:value - the new value of the 'Export Context Path' attribute.See Also:isSetExportContextPath(), 
unsetExportContextPath(), 
getExportContextPath()
    - unsetExportContextPath
void unsetExportContextPath()
Unsets the value of the 'Export Context Path' attribute.
 

See Also:isSetExportContextPath(), 
getExportContextPath(), 
setExportContextPath(String)
    - isSetExportContextPath
boolean isSetExportContextPath()
Returns whether the value of the 'Export Context Path' attribute is set.
 

Returns:whether the value of the 'Export Context Path' attribute is set.See Also:unsetExportContextPath(), 
getExportContextPath(), 
setExportContextPath(String)
    - getAuthentication
HTTPAuthentication getAuthentication()
Returns the value of the 'Authentication' containment reference.
Returns:the value of the 'Authentication' containment reference.See Also:isSetAuthentication(), 
unsetAuthentication(), 
setAuthentication(HTTPAuthentication), 
HeadersPackage.getHTTPControl\_Authentication()
    - setAuthentication
void setAuthentication(HTTPAuthentication value)
Sets the value of the 'Authentication' containment reference.
 

Parameters:value - the new value of the 'Authentication' containment reference.See Also:isSetAuthentication(), 
unsetAuthentication(), 
getAuthentication()
    - unsetAuthentication
void unsetAuthentication()
Unsets the value of the 'Authentication' containment reference.
 

See Also:isSetAuthentication(), 
getAuthentication(), 
setAuthentication(HTTPAuthentication)
    - isSetAuthentication
boolean isSetAuthentication()
Returns whether the value of the 'Authentication' containment reference is set.
 

Returns:whether the value of the 'Authentication' containment reference is set.See Also:unsetAuthentication(), 
getAuthentication(), 
setAuthentication(HTTPAuthentication)
    - getSSLSettings
HTTPSSLSettings getSSLSettings()
Returns the value of the 'SSL Settings' containment reference.
Returns:the value of the 'SSL Settings' containment reference.See Also:isSetSSLSettings(), 
unsetSSLSettings(), 
setSSLSettings(HTTPSSLSettings), 
HeadersPackage.getHTTPControl\_SSLSettings()
    - setSSLSettings
void setSSLSettings(HTTPSSLSettings value)
Sets the value of the 'SSL Settings' containment reference.
 

Parameters:value - the new value of the 'SSL Settings' containment reference.See Also:isSetSSLSettings(), 
unsetSSLSettings(), 
getSSLSettings()
    - unsetSSLSettings
void unsetSSLSettings()
Unsets the value of the 'SSL Settings' containment reference.
 

See Also:isSetSSLSettings(), 
getSSLSettings(), 
setSSLSettings(HTTPSSLSettings)
    - isSetSSLSettings
boolean isSetSSLSettings()
Returns whether the value of the 'SSL Settings' containment reference is set.
 

Returns:whether the value of the 'SSL Settings' containment reference is set.See Also:unsetSSLSettings(), 
getSSLSettings(), 
setSSLSettings(HTTPSSLSettings)
    - getProxySettings
java.util.List getProxySettings()
Returns the value of the 'Proxy Settings' containment reference list.
 The list contents are of type HTTPProxySettings.
Returns:the value of the 'Proxy Settings' containment reference list.See Also:HeadersPackage.getHTTPControl\_ProxySettings()