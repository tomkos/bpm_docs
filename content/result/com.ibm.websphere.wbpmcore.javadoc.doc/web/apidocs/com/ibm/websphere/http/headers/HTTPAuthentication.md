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

## Interface HTTPAuthentication

- public interface HTTPAuthentication begin-user-doc A representation of the model object 'HTTP Authentication '. end-user-doc The following features are supported: See Also: HeadersPackage.getHTTPAuthentication()

```
public interface HTTPAuthentication
```

The following features are supported:
 
Credentials
Authentication Type

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

HTTPAuthenticationType
getAuthenticationType()
Returns the value of the 'Authentication Type' attribute.

HTTPCredentials
getCredentials()
Returns the value of the 'Credentials' containment reference.

boolean
isSetAuthenticationType()
Returns whether the value of the 'Authentication Type' attribute is set

boolean
isSetCredentials()
Returns whether the value of the 'Credentials' containment reference is set

void
setAuthenticationType(HTTPAuthenticationType value)
Sets the value of the 'Authentication Type' attribute

void
setCredentials(HTTPCredentials value)
Sets the value of the 'Credentials' containment reference

void
unsetAuthenticationType()
Unsets the value of the 'Authentication Type' attribute

void
unsetCredentials()
Unsets the value of the 'Credentials' containment reference

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getCredentials
HTTPCredentials getCredentials()
Returns the value of the 'Credentials' containment reference.
Returns:the value of the 'Credentials' containment reference.See Also:isSetCredentials(), 
unsetCredentials(), 
setCredentials(HTTPCredentials), 
HeadersPackage.getHTTPAuthentication\_Credentials()
    - setCredentials
void setCredentials(HTTPCredentials value)
Sets the value of the 'Credentials' containment reference.
 

Parameters:value - the new value of the 'Credentials' containment reference.See Also:isSetCredentials(), 
unsetCredentials(), 
getCredentials()
    - unsetCredentials
void unsetCredentials()
Unsets the value of the 'Credentials' containment reference.
 

See Also:isSetCredentials(), 
getCredentials(), 
setCredentials(HTTPCredentials)
    - isSetCredentials
boolean isSetCredentials()
Returns whether the value of the 'Credentials' containment reference is set.
 

Returns:whether the value of the 'Credentials' containment reference is set.See Also:unsetCredentials(), 
getCredentials(), 
setCredentials(HTTPCredentials)
    - getAuthenticationType
HTTPAuthenticationType getAuthenticationType()
Returns the value of the 'Authentication Type' attribute.
 The default value is "Basic".
Returns:the value of the 'Authentication Type' attribute.See Also:isSetAuthenticationType(), 
unsetAuthenticationType(), 
setAuthenticationType(HTTPAuthenticationType), 
HeadersPackage.getHTTPAuthentication\_AuthenticationType()
    - setAuthenticationType
void setAuthenticationType(HTTPAuthenticationType value)
Sets the value of the 'Authentication Type' attribute.
 

Parameters:value - the new value of the 'Authentication Type' attribute.See Also:isSetAuthenticationType(), 
unsetAuthenticationType(), 
getAuthenticationType()
    - unsetAuthenticationType
void unsetAuthenticationType()
Unsets the value of the 'Authentication Type' attribute.
 

See Also:isSetAuthenticationType(), 
getAuthenticationType(), 
setAuthenticationType(HTTPAuthenticationType)
    - isSetAuthenticationType
boolean isSetAuthenticationType()
Returns whether the value of the 'Authentication Type' attribute is set.
 

Returns:whether the value of the 'Authentication Type' attribute is set.See Also:unsetAuthenticationType(), 
getAuthenticationType(), 
setAuthenticationType(HTTPAuthenticationType)