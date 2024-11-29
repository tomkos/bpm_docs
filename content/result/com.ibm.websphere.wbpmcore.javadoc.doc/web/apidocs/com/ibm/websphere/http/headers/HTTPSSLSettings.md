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

## Interface HTTPSSLSettings

- public interface HTTPSSLSettings begin-user-doc A representation of the model object 'HTTPSSL Settings '. end-user-doc The following features are supported: See Also: HeadersPackage.getHTTPSSLSettings()

```
public interface HTTPSSLSettings
```

The following features are supported:
 
SSL Version
SSL Debug
Key Store Type
Trust Store Type
Key Store
Key Store Alias
Key Store Password
Trust Store
Trust Store Password
Use Client Auth
Enabled Cipher Suites

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
getEnabledCipherSuites()
Returns the value of the 'Enabled Cipher Suites' attribute.

java.lang.String
getKeyStore()
Returns the value of the 'Key Store' attribute.

java.lang.String
getKeyStoreAlias()
Returns the value of the 'Key Store Alias' attribute.

java.lang.String
getKeyStorePassword()
Returns the value of the 'Key Store Password' attribute.

java.lang.String
getKeyStoreType()
Returns the value of the 'Key Store Type' attribute.

java.lang.Boolean
getSSLDebug()
Returns the value of the 'SSL Debug' attribute.

java.lang.String
getSSLVersion()
Returns the value of the 'SSL Version' attribute.

java.lang.String
getTrustStore()
Returns the value of the 'Trust Store' attribute.

java.lang.String
getTrustStorePassword()
Returns the value of the 'Trust Store Password' attribute.

java.lang.String
getTrustStoreType()
Returns the value of the 'Trust Store Type' attribute.

java.lang.Boolean
getUseClientAuth()
Returns the value of the 'Use Client Auth' attribute.

boolean
isSetEnabledCipherSuites()
Returns whether the value of the 'Enabled Cipher Suites' attribute is set

boolean
isSetKeyStore()
Returns whether the value of the 'Key Store' attribute is set

boolean
isSetKeyStoreAlias()
Returns whether the value of the 'Key Store Alias' attribute is set

boolean
isSetKeyStorePassword()
Returns whether the value of the 'Key Store Password' attribute is set

boolean
isSetKeyStoreType()
Returns whether the value of the 'Key Store Type' attribute is set

boolean
isSetSSLDebug()
Returns whether the value of the 'SSL Debug' attribute is set

boolean
isSetSSLVersion()
Returns whether the value of the 'SSL Version' attribute is set

boolean
isSetTrustStore()
Returns whether the value of the 'Trust Store' attribute is set

boolean
isSetTrustStorePassword()
Returns whether the value of the 'Trust Store Password' attribute is set

boolean
isSetTrustStoreType()
Returns whether the value of the 'Trust Store Type' attribute is set

boolean
isSetUseClientAuth()
Returns whether the value of the 'Use Client Auth' attribute is set

void
setEnabledCipherSuites(java.lang.String value)
Sets the value of the 'Enabled Cipher Suites' attribute

void
setKeyStore(java.lang.String value)
Sets the value of the 'Key Store' attribute

void
setKeyStoreAlias(java.lang.String value)
Sets the value of the 'Key Store Alias' attribute

void
setKeyStorePassword(java.lang.String value)
Sets the value of the 'Key Store Password' attribute

void
setKeyStoreType(java.lang.String value)
Sets the value of the 'Key Store Type' attribute

void
setSSLDebug(java.lang.Boolean value)
Sets the value of the 'SSL Debug' attribute

void
setSSLVersion(java.lang.String value)
Sets the value of the 'SSL Version' attribute

void
setTrustStore(java.lang.String value)
Sets the value of the 'Trust Store' attribute

void
setTrustStorePassword(java.lang.String value)
Sets the value of the 'Trust Store Password' attribute

void
setTrustStoreType(java.lang.String value)
Sets the value of the 'Trust Store Type' attribute

void
setUseClientAuth(java.lang.Boolean value)
Sets the value of the 'Use Client Auth' attribute

void
unsetEnabledCipherSuites()
Unsets the value of the 'Enabled Cipher Suites' attribute

void
unsetKeyStore()
Unsets the value of the 'Key Store' attribute

void
unsetKeyStoreAlias()
Unsets the value of the 'Key Store Alias' attribute

void
unsetKeyStorePassword()
Unsets the value of the 'Key Store Password' attribute

void
unsetKeyStoreType()
Unsets the value of the 'Key Store Type' attribute

void
unsetSSLDebug()
Unsets the value of the 'SSL Debug' attribute

void
unsetSSLVersion()
Unsets the value of the 'SSL Version' attribute

void
unsetTrustStore()
Unsets the value of the 'Trust Store' attribute

void
unsetTrustStorePassword()
Unsets the value of the 'Trust Store Password' attribute

void
unsetTrustStoreType()
Unsets the value of the 'Trust Store Type' attribute

void
unsetUseClientAuth()
Unsets the value of the 'Use Client Auth' attribute

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getSSLVersion
java.lang.String getSSLVersion()
Returns the value of the 'SSL Version' attribute.
 The default value is "SSL".
Returns:the value of the 'SSL Version' attribute.See Also:isSetSSLVersion(), 
unsetSSLVersion(), 
setSSLVersion(String), 
HeadersPackage.getHTTPSSLSettings\_SSLVersion()
    - setSSLVersion
void setSSLVersion(java.lang.String value)
Sets the value of the 'SSL Version' attribute.
 

Parameters:value - the new value of the 'SSL Version' attribute.See Also:isSetSSLVersion(), 
unsetSSLVersion(), 
getSSLVersion()
    - unsetSSLVersion
void unsetSSLVersion()
Unsets the value of the 'SSL Version' attribute.
 

See Also:isSetSSLVersion(), 
getSSLVersion(), 
setSSLVersion(String)
    - isSetSSLVersion
boolean isSetSSLVersion()
Returns whether the value of the 'SSL Version' attribute is set.
 

Returns:whether the value of the 'SSL Version' attribute is set.See Also:unsetSSLVersion(), 
getSSLVersion(), 
setSSLVersion(String)
    - getSSLDebug
java.lang.Boolean getSSLDebug()
Returns the value of the 'SSL Debug' attribute.
 The default value is "false".
Returns:the value of the 'SSL Debug' attribute.See Also:isSetSSLDebug(), 
unsetSSLDebug(), 
setSSLDebug(Boolean), 
HeadersPackage.getHTTPSSLSettings\_SSLDebug()
    - setSSLDebug
void setSSLDebug(java.lang.Boolean value)
Sets the value of the 'SSL Debug' attribute.
 

Parameters:value - the new value of the 'SSL Debug' attribute.See Also:isSetSSLDebug(), 
unsetSSLDebug(), 
getSSLDebug()
    - unsetSSLDebug
void unsetSSLDebug()
Unsets the value of the 'SSL Debug' attribute.
 

See Also:isSetSSLDebug(), 
getSSLDebug(), 
setSSLDebug(Boolean)
    - isSetSSLDebug
boolean isSetSSLDebug()
Returns whether the value of the 'SSL Debug' attribute is set.
 

Returns:whether the value of the 'SSL Debug' attribute is set.See Also:unsetSSLDebug(), 
getSSLDebug(), 
setSSLDebug(Boolean)
    - getKeyStoreType
java.lang.String getKeyStoreType()
Returns the value of the 'Key Store Type' attribute.
 The default value is "JKS".
Returns:the value of the 'Key Store Type' attribute.See Also:isSetKeyStoreType(), 
unsetKeyStoreType(), 
setKeyStoreType(String), 
HeadersPackage.getHTTPSSLSettings\_KeyStoreType()
    - setKeyStoreType
void setKeyStoreType(java.lang.String value)
Sets the value of the 'Key Store Type' attribute.
 

Parameters:value - the new value of the 'Key Store Type' attribute.See Also:isSetKeyStoreType(), 
unsetKeyStoreType(), 
getKeyStoreType()
    - unsetKeyStoreType
void unsetKeyStoreType()
Unsets the value of the 'Key Store Type' attribute.
 

See Also:isSetKeyStoreType(), 
getKeyStoreType(), 
setKeyStoreType(String)
    - isSetKeyStoreType
boolean isSetKeyStoreType()
Returns whether the value of the 'Key Store Type' attribute is set.
 

Returns:whether the value of the 'Key Store Type' attribute is set.See Also:unsetKeyStoreType(), 
getKeyStoreType(), 
setKeyStoreType(String)
    - getTrustStoreType
java.lang.String getTrustStoreType()
Returns the value of the 'Trust Store Type' attribute.
 The default value is "JKS".
Returns:the value of the 'Trust Store Type' attribute.See Also:isSetTrustStoreType(), 
unsetTrustStoreType(), 
setTrustStoreType(String), 
HeadersPackage.getHTTPSSLSettings\_TrustStoreType()
    - setTrustStoreType
void setTrustStoreType(java.lang.String value)
Sets the value of the 'Trust Store Type' attribute.
 

Parameters:value - the new value of the 'Trust Store Type' attribute.See Also:isSetTrustStoreType(), 
unsetTrustStoreType(), 
getTrustStoreType()
    - unsetTrustStoreType
void unsetTrustStoreType()
Unsets the value of the 'Trust Store Type' attribute.
 

See Also:isSetTrustStoreType(), 
getTrustStoreType(), 
setTrustStoreType(String)
    - isSetTrustStoreType
boolean isSetTrustStoreType()
Returns whether the value of the 'Trust Store Type' attribute is set.
 

Returns:whether the value of the 'Trust Store Type' attribute is set.See Also:unsetTrustStoreType(), 
getTrustStoreType(), 
setTrustStoreType(String)
    - getKeyStore
java.lang.String getKeyStore()
Returns the value of the 'Key Store' attribute.
Returns:the value of the 'Key Store' attribute.See Also:isSetKeyStore(), 
unsetKeyStore(), 
setKeyStore(String), 
HeadersPackage.getHTTPSSLSettings\_KeyStore()
    - setKeyStore
void setKeyStore(java.lang.String value)
Sets the value of the 'Key Store' attribute.
 

Parameters:value - the new value of the 'Key Store' attribute.See Also:isSetKeyStore(), 
unsetKeyStore(), 
getKeyStore()
    - unsetKeyStore
void unsetKeyStore()
Unsets the value of the 'Key Store' attribute.
 

See Also:isSetKeyStore(), 
getKeyStore(), 
setKeyStore(String)
    - isSetKeyStore
boolean isSetKeyStore()
Returns whether the value of the 'Key Store' attribute is set.
 

Returns:whether the value of the 'Key Store' attribute is set.See Also:unsetKeyStore(), 
getKeyStore(), 
setKeyStore(String)
    - getKeyStoreAlias
java.lang.String getKeyStoreAlias()
Returns the value of the 'Key Store Alias' attribute.
Returns:the value of the 'Key Store Alias' attribute.See Also:isSetKeyStoreAlias(), 
unsetKeyStoreAlias(), 
setKeyStoreAlias(String), 
HeadersPackage.getHTTPSSLSettings\_KeyStoreAlias()
    - setKeyStoreAlias
void setKeyStoreAlias(java.lang.String value)
Sets the value of the 'Key Store Alias' attribute.
 

Parameters:value - the new value of the 'Key Store Alias' attribute.See Also:isSetKeyStoreAlias(), 
unsetKeyStoreAlias(), 
getKeyStoreAlias()
    - unsetKeyStoreAlias
void unsetKeyStoreAlias()
Unsets the value of the 'Key Store Alias' attribute.
 

See Also:isSetKeyStoreAlias(), 
getKeyStoreAlias(), 
setKeyStoreAlias(String)
    - isSetKeyStoreAlias
boolean isSetKeyStoreAlias()
Returns whether the value of the 'Key Store Alias' attribute is set.
 

Returns:whether the value of the 'Key Store Alias' attribute is set.See Also:unsetKeyStoreAlias(), 
getKeyStoreAlias(), 
setKeyStoreAlias(String)
    - getKeyStorePassword
java.lang.String getKeyStorePassword()
Returns the value of the 'Key Store Password' attribute.
Returns:the value of the 'Key Store Password' attribute.See Also:isSetKeyStorePassword(), 
unsetKeyStorePassword(), 
setKeyStorePassword(String), 
HeadersPackage.getHTTPSSLSettings\_KeyStorePassword()
    - setKeyStorePassword
void setKeyStorePassword(java.lang.String value)
Sets the value of the 'Key Store Password' attribute.
 

Parameters:value - the new value of the 'Key Store Password' attribute.See Also:isSetKeyStorePassword(), 
unsetKeyStorePassword(), 
getKeyStorePassword()
    - unsetKeyStorePassword
void unsetKeyStorePassword()
Unsets the value of the 'Key Store Password' attribute.
 

See Also:isSetKeyStorePassword(), 
getKeyStorePassword(), 
setKeyStorePassword(String)
    - isSetKeyStorePassword
boolean isSetKeyStorePassword()
Returns whether the value of the 'Key Store Password' attribute is set.
 

Returns:whether the value of the 'Key Store Password' attribute is set.See Also:unsetKeyStorePassword(), 
getKeyStorePassword(), 
setKeyStorePassword(String)
    - getTrustStore
java.lang.String getTrustStore()
Returns the value of the 'Trust Store' attribute.
Returns:the value of the 'Trust Store' attribute.See Also:isSetTrustStore(), 
unsetTrustStore(), 
setTrustStore(String), 
HeadersPackage.getHTTPSSLSettings\_TrustStore()
    - setTrustStore
void setTrustStore(java.lang.String value)
Sets the value of the 'Trust Store' attribute.
 

Parameters:value - the new value of the 'Trust Store' attribute.See Also:isSetTrustStore(), 
unsetTrustStore(), 
getTrustStore()
    - unsetTrustStore
void unsetTrustStore()
Unsets the value of the 'Trust Store' attribute.
 

See Also:isSetTrustStore(), 
getTrustStore(), 
setTrustStore(String)
    - isSetTrustStore
boolean isSetTrustStore()
Returns whether the value of the 'Trust Store' attribute is set.
 

Returns:whether the value of the 'Trust Store' attribute is set.See Also:unsetTrustStore(), 
getTrustStore(), 
setTrustStore(String)
    - getTrustStorePassword
java.lang.String getTrustStorePassword()
Returns the value of the 'Trust Store Password' attribute.
Returns:the value of the 'Trust Store Password' attribute.See Also:isSetTrustStorePassword(), 
unsetTrustStorePassword(), 
setTrustStorePassword(String), 
HeadersPackage.getHTTPSSLSettings\_TrustStorePassword()
    - setTrustStorePassword
void setTrustStorePassword(java.lang.String value)
Sets the value of the 'Trust Store Password' attribute.
 

Parameters:value - the new value of the 'Trust Store Password' attribute.See Also:isSetTrustStorePassword(), 
unsetTrustStorePassword(), 
getTrustStorePassword()
    - unsetTrustStorePassword
void unsetTrustStorePassword()
Unsets the value of the 'Trust Store Password' attribute.
 

See Also:isSetTrustStorePassword(), 
getTrustStorePassword(), 
setTrustStorePassword(String)
    - isSetTrustStorePassword
boolean isSetTrustStorePassword()
Returns whether the value of the 'Trust Store Password' attribute is set.
 

Returns:whether the value of the 'Trust Store Password' attribute is set.See Also:unsetTrustStorePassword(), 
getTrustStorePassword(), 
setTrustStorePassword(String)
    - getUseClientAuth
java.lang.Boolean getUseClientAuth()
Returns the value of the 'Use Client Auth' attribute.
 The default value is "false".
Returns:the value of the 'Use Client Auth' attribute.See Also:isSetUseClientAuth(), 
unsetUseClientAuth(), 
setUseClientAuth(Boolean), 
HeadersPackage.getHTTPSSLSettings\_UseClientAuth()
    - setUseClientAuth
void setUseClientAuth(java.lang.Boolean value)
Sets the value of the 'Use Client Auth' attribute.
 

Parameters:value - the new value of the 'Use Client Auth' attribute.See Also:isSetUseClientAuth(), 
unsetUseClientAuth(), 
getUseClientAuth()
    - unsetUseClientAuth
void unsetUseClientAuth()
Unsets the value of the 'Use Client Auth' attribute.
 

See Also:isSetUseClientAuth(), 
getUseClientAuth(), 
setUseClientAuth(Boolean)
    - isSetUseClientAuth
boolean isSetUseClientAuth()
Returns whether the value of the 'Use Client Auth' attribute is set.
 

Returns:whether the value of the 'Use Client Auth' attribute is set.See Also:unsetUseClientAuth(), 
getUseClientAuth(), 
setUseClientAuth(Boolean)
    - getEnabledCipherSuites
java.lang.String getEnabledCipherSuites()
Returns the value of the 'Enabled Cipher Suites' attribute.
Returns:the value of the 'Enabled Cipher Suites' attribute.See Also:isSetEnabledCipherSuites(), 
unsetEnabledCipherSuites(), 
setEnabledCipherSuites(String), 
HeadersPackage.getHTTPSSLSettings\_EnabledCipherSuites()
    - setEnabledCipherSuites
void setEnabledCipherSuites(java.lang.String value)
Sets the value of the 'Enabled Cipher Suites' attribute.
 

Parameters:value - the new value of the 'Enabled Cipher Suites' attribute.See Also:isSetEnabledCipherSuites(), 
unsetEnabledCipherSuites(), 
getEnabledCipherSuites()
    - unsetEnabledCipherSuites
void unsetEnabledCipherSuites()
Unsets the value of the 'Enabled Cipher Suites' attribute.
 

See Also:isSetEnabledCipherSuites(), 
getEnabledCipherSuites(), 
setEnabledCipherSuites(String)
    - isSetEnabledCipherSuites
boolean isSetEnabledCipherSuites()
Returns whether the value of the 'Enabled Cipher Suites' attribute is set.
 

Returns:whether the value of the 'Enabled Cipher Suites' attribute is set.See Also:unsetEnabledCipherSuites(), 
getEnabledCipherSuites(), 
setEnabledCipherSuites(String)