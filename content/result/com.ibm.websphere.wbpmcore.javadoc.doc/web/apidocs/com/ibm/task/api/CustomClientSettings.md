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

## Interface CustomClientSettings

- All Superinterfaces:
java.lang.Cloneable, java.io.Serializable

public interface CustomClientSettings
extends java.io.Serializable, java.lang.Cloneable
Interface for all client and Web client settings.
Since:
5.1

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

ClientSetting
getClientSetting(java.lang.String type)
Returns the client settings for the specified client type.

java.util.List
getClientSettings()
Returns a list of all client settings.

java.util.List
getClientTypes()
Returns a list of all known client types.

PageflowClientSetting
getPageflowClientSetting(java.lang.String type)
Returns the pageflow client settings.

java.util.List
getPageflowClientSettings()
Returns a list of all defined portal client settings.

java.util.List
getPageflowClientTypes()
Returns a list of all portal client types.

PortalClientSetting
getPortalClientSetting(java.lang.String type)
Returns the portal client settings of the specified portal client type.

java.util.List
getPortalClientSettings()
Returns a list of all portal client settings.

java.util.List
getPortalClientTypes()
Returns a list of all portal client types.

WebClientSetting
getWebClientSetting()
Deprecated. 
Use getWebClientSetting(String) instead.

WebClientSetting
getWebClientSetting(java.lang.String type)
Returns the web client settings for the specified web client type.

java.util.List
getWebClientSettings()
Returns a list of all web client settings.

java.util.List
getWebClientTypes()
Returns a list of all web client types.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getClientSetting
ClientSetting getClientSetting(java.lang.String type)
Returns the client settings for the specified client type.
 Returns null when the specified type is not found or when there is no client setting.
Parameters:type - The type of the client for which the setting is to be returned.
Returns:ClientSetting -
    The client settings of the specified type.Since:
5.1
    - getClientTypes
java.util.List getClientTypes()
Returns a list of all known client types.
Returns:List -
    The names of all known client types, that is, returns a list of String objects.Since:
5.1
    - getClientSettings
java.util.List getClientSettings()
Returns a list of all client settings.
Returns:List -
    A list of ClientSetting objects.Since:
5.1
    - getWebClientSetting
WebClientSetting getWebClientSetting()
Deprecated. Use getWebClientSetting(String) instead.
Returns the web client settings.
 Returns null when there are no web client settings.
Returns:WebClientSetting -
    The web client settings.Since:
5.1
    - getWebClientSetting
WebClientSetting getWebClientSetting(java.lang.String type)
Returns the web client settings for the specified web client type.
 Returns null when the specified web client type is not found or when there are no web client settings.
Parameters:type - The type of the client for which the web client settings are to be returned.
Returns:WebClientSetting -
    The web client settings.Since:
6.0
    - getWebClientTypes
java.util.List getWebClientTypes()
Returns a list of all web client types.
Returns:List -
    The names of all known web client types, that is, returns a list of String objects.Since:
6.0
    - getWebClientSettings
java.util.List getWebClientSettings()
Returns a list of all web client settings.
Returns:List -
    A list of WebClientSetting objects.Since:
6.0
    - getPortalClientSetting
PortalClientSetting getPortalClientSetting(java.lang.String type)
Returns the portal client settings of the specified portal client type.
 Returns null when the specified type is not found or when there are no portal client settings.
Parameters:type - The type of the client for which the setting is to be returned.
Returns:PortalClientSetting -
    The portal client settings.Since:
6.0
    - getPortalClientTypes
java.util.List getPortalClientTypes()
Returns a list of all portal client types.
Returns:List -
    The names of all known portal client types, that is, returns a list of String objects.Since:
6.0
    - getPortalClientSettings
java.util.List getPortalClientSettings()
Returns a list of all portal client settings.
Returns:List -
    A list of PortalClientSetting objects.Since:
6.0
    - getPageflowClientSetting
PageflowClientSetting getPageflowClientSetting(java.lang.String type)
Returns the pageflow client settings.
 Returns null when there are no pageflow client settings.
Parameters:type - The type of the client for which the setting is to be returned.
Returns:PageflowClientSetting -
    The pageflow client settings.
    - getPageflowClientTypes
java.util.List getPageflowClientTypes()
Returns a list of all portal client types.
Returns:List -
    The names of all known portal client types,
            that is, returns a list of String objects.
    - getPageflowClientSettings
java.util.List getPageflowClientSettings()
Returns a list of all defined portal client settings.
Returns:List -
    A list of PortalClientSetting objects.