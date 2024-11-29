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

## Interface HTTPCredentials

- public interface HTTPCredentials begin-user-doc A representation of the model object 'HTTP Credentials '. end-user-doc The following features are supported: See Also: HeadersPackage.getHTTPCredentials()

```
public interface HTTPCredentials
```

The following features are supported:
 
User Id
Password

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

java.lang.String
getPassword()
Returns the value of the 'Password' attribute.

java.lang.String
getUserId()
Returns the value of the 'User Id' attribute.

boolean
isSetPassword()
Returns whether the value of the 'Password' attribute is set

boolean
isSetUserId()
Returns whether the value of the 'User Id' attribute is set

void
setPassword(java.lang.String value)
Sets the value of the 'Password' attribute

void
setUserId(java.lang.String value)
Sets the value of the 'User Id' attribute

void
unsetPassword()
Unsets the value of the 'Password' attribute

void
unsetUserId()
Unsets the value of the 'User Id' attribute

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getUserId
java.lang.String getUserId()
Returns the value of the 'User Id' attribute.
Returns:the value of the 'User Id' attribute.See Also:isSetUserId(), 
unsetUserId(), 
setUserId(String), 
HeadersPackage.getHTTPCredentials\_UserId()
    - setUserId
void setUserId(java.lang.String value)
Sets the value of the 'User Id' attribute.
 

Parameters:value - the new value of the 'User Id' attribute.See Also:isSetUserId(), 
unsetUserId(), 
getUserId()
    - unsetUserId
void unsetUserId()
Unsets the value of the 'User Id' attribute.
 

See Also:isSetUserId(), 
getUserId(), 
setUserId(String)
    - isSetUserId
boolean isSetUserId()
Returns whether the value of the 'User Id' attribute is set.
 

Returns:whether the value of the 'User Id' attribute is set.See Also:unsetUserId(), 
getUserId(), 
setUserId(String)
    - getPassword
java.lang.String getPassword()
Returns the value of the 'Password' attribute.
Returns:the value of the 'Password' attribute.See Also:isSetPassword(), 
unsetPassword(), 
setPassword(String), 
HeadersPackage.getHTTPCredentials\_Password()
    - setPassword
void setPassword(java.lang.String value)
Sets the value of the 'Password' attribute.
 

Parameters:value - the new value of the 'Password' attribute.See Also:isSetPassword(), 
unsetPassword(), 
getPassword()
    - unsetPassword
void unsetPassword()
Unsets the value of the 'Password' attribute.
 

See Also:isSetPassword(), 
getPassword(), 
setPassword(String)
    - isSetPassword
boolean isSetPassword()
Returns whether the value of the 'Password' attribute is set.
 

Returns:whether the value of the 'Password' attribute is set.See Also:unsetPassword(), 
getPassword(), 
setPassword(String)