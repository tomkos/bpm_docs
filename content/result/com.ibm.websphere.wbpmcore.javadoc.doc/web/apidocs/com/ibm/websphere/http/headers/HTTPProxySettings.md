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

## Interface HTTPProxySettings

- public interface HTTPProxySettings begin-user-doc A representation of the model object 'HTTP Proxy Settings '. end-user-doc The following features are supported: See Also: HeadersPackage.getHTTPProxySettings()

```
public interface HTTPProxySettings
```

The following features are supported:
 
Proxy Host
Proxy Port
Proxy Type
Proxy Credentials
Non Proxy Host

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

java.util.List
getNonProxyHost()
Returns the value of the 'Non Proxy Host' attribute list.

HTTPCredentials
getProxyCredentials()
Returns the value of the 'Proxy Credentials' containment reference.

java.lang.String
getProxyHost()
Returns the value of the 'Proxy Host' attribute.

java.lang.Integer
getProxyPort()
Returns the value of the 'Proxy Port' attribute.

HTTPProxyType
getProxyType()
Returns the value of the 'Proxy Type' attribute.

boolean
isSetProxyCredentials()
Returns whether the value of the 'Proxy Credentials' containment reference is set

boolean
isSetProxyHost()
Returns whether the value of the 'Proxy Host' attribute is set

boolean
isSetProxyPort()
Returns whether the value of the 'Proxy Port' attribute is set

boolean
isSetProxyType()
Returns whether the value of the 'Proxy Type' attribute is set

void
setProxyCredentials(HTTPCredentials value)
Sets the value of the 'Proxy Credentials' containment reference

void
setProxyHost(java.lang.String value)
Sets the value of the 'Proxy Host' attribute

void
setProxyPort(java.lang.Integer value)
Sets the value of the 'Proxy Port' attribute

void
setProxyType(HTTPProxyType value)
Sets the value of the 'Proxy Type' attribute

void
unsetProxyCredentials()
Unsets the value of the 'Proxy Credentials' containment reference

void
unsetProxyHost()
Unsets the value of the 'Proxy Host' attribute

void
unsetProxyPort()
Unsets the value of the 'Proxy Port' attribute

void
unsetProxyType()
Unsets the value of the 'Proxy Type' attribute

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getProxyHost
java.lang.String getProxyHost()
Returns the value of the 'Proxy Host' attribute.
Returns:the value of the 'Proxy Host' attribute.See Also:isSetProxyHost(), 
unsetProxyHost(), 
setProxyHost(String), 
HeadersPackage.getHTTPProxySettings\_ProxyHost()
    - setProxyHost
void setProxyHost(java.lang.String value)
Sets the value of the 'Proxy Host' attribute.
 

Parameters:value - the new value of the 'Proxy Host' attribute.See Also:isSetProxyHost(), 
unsetProxyHost(), 
getProxyHost()
    - unsetProxyHost
void unsetProxyHost()
Unsets the value of the 'Proxy Host' attribute.
 

See Also:isSetProxyHost(), 
getProxyHost(), 
setProxyHost(String)
    - isSetProxyHost
boolean isSetProxyHost()
Returns whether the value of the 'Proxy Host' attribute is set.
 

Returns:whether the value of the 'Proxy Host' attribute is set.See Also:unsetProxyHost(), 
getProxyHost(), 
setProxyHost(String)
    - getProxyPort
java.lang.Integer getProxyPort()
Returns the value of the 'Proxy Port' attribute.
Returns:the value of the 'Proxy Port' attribute.See Also:isSetProxyPort(), 
unsetProxyPort(), 
setProxyPort(Integer), 
HeadersPackage.getHTTPProxySettings\_ProxyPort()
    - setProxyPort
void setProxyPort(java.lang.Integer value)
Sets the value of the 'Proxy Port' attribute.
 

Parameters:value - the new value of the 'Proxy Port' attribute.See Also:isSetProxyPort(), 
unsetProxyPort(), 
getProxyPort()
    - unsetProxyPort
void unsetProxyPort()
Unsets the value of the 'Proxy Port' attribute.
 

See Also:isSetProxyPort(), 
getProxyPort(), 
setProxyPort(Integer)
    - isSetProxyPort
boolean isSetProxyPort()
Returns whether the value of the 'Proxy Port' attribute is set.
 

Returns:whether the value of the 'Proxy Port' attribute is set.See Also:unsetProxyPort(), 
getProxyPort(), 
setProxyPort(Integer)
    - getProxyType
HTTPProxyType getProxyType()
Returns the value of the 'Proxy Type' attribute.
 The default value is "http".
Returns:the value of the 'Proxy Type' attribute.See Also:isSetProxyType(), 
unsetProxyType(), 
setProxyType(HTTPProxyType), 
HeadersPackage.getHTTPProxySettings\_ProxyType()
    - setProxyType
void setProxyType(HTTPProxyType value)
Sets the value of the 'Proxy Type' attribute.
 

Parameters:value - the new value of the 'Proxy Type' attribute.See Also:isSetProxyType(), 
unsetProxyType(), 
getProxyType()
    - unsetProxyType
void unsetProxyType()
Unsets the value of the 'Proxy Type' attribute.
 

See Also:isSetProxyType(), 
getProxyType(), 
setProxyType(HTTPProxyType)
    - isSetProxyType
boolean isSetProxyType()
Returns whether the value of the 'Proxy Type' attribute is set.
 

Returns:whether the value of the 'Proxy Type' attribute is set.See Also:unsetProxyType(), 
getProxyType(), 
setProxyType(HTTPProxyType)
    - getProxyCredentials
HTTPCredentials getProxyCredentials()
Returns the value of the 'Proxy Credentials' containment reference.
Returns:the value of the 'Proxy Credentials' containment reference.See Also:isSetProxyCredentials(), 
unsetProxyCredentials(), 
setProxyCredentials(HTTPCredentials), 
HeadersPackage.getHTTPProxySettings\_ProxyCredentials()
    - setProxyCredentials
void setProxyCredentials(HTTPCredentials value)
Sets the value of the 'Proxy Credentials' containment reference.
 

Parameters:value - the new value of the 'Proxy Credentials' containment reference.See Also:isSetProxyCredentials(), 
unsetProxyCredentials(), 
getProxyCredentials()
    - unsetProxyCredentials
void unsetProxyCredentials()
Unsets the value of the 'Proxy Credentials' containment reference.
 

See Also:isSetProxyCredentials(), 
getProxyCredentials(), 
setProxyCredentials(HTTPCredentials)
    - isSetProxyCredentials
boolean isSetProxyCredentials()
Returns whether the value of the 'Proxy Credentials' containment reference is set.
 

Returns:whether the value of the 'Proxy Credentials' containment reference is set.See Also:unsetProxyCredentials(), 
getProxyCredentials(), 
setProxyCredentials(HTTPCredentials)
    - getNonProxyHost
java.util.List getNonProxyHost()
Returns the value of the 'Non Proxy Host' attribute list.
 The list contents are of type String.
Returns:the value of the 'Non Proxy Host' attribute list.See Also:HeadersPackage.getHTTPProxySettings\_NonProxyHost()