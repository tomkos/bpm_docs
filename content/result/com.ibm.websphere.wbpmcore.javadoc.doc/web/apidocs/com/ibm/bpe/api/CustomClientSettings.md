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
CustomClientSettings defines the interface for all client and Web client settings
 that are associated with a process template, process instance, or activity instance.
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
Returns a list of all defined client settings.

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
Returns the portal client settings.

java.util.List
getPortalClientSettings()
Returns a list of all defined portal client settings.

java.util.List
getPortalClientTypes()
Returns a list of all portal client types.

WebClientSetting
getWebClientSetting()
Deprecated. 
Use getWebClientSetting(String)
            instead.

WebClientSetting
getWebClientSetting(java.lang.String type)
Returns the web client settings.

java.util.List
getWebClientSettings()
Returns a list of all defined web client settings.

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
 Returns null when the specified type is not found.
Parameters:type - The type of the client for which the setting is to be returned.
Returns:ClientSetting -
    The client settings of the specified type.
    - getClientTypes
java.util.List getClientTypes()
Returns a list of all known client types.
Returns:List -
    The names of all known client types.
    - getClientSettings
java.util.List getClientSettings()
Returns a list of all defined client settings.
Returns:List -
    A list of client settings.
    - getWebClientSetting
WebClientSetting getWebClientSetting()
Deprecated. Use getWebClientSetting(String)
            instead.
Returns the web client settings.
 Returns null when there are no web client settings.
Returns:WebClientSetting -
    The web client settings.
    - getWebClientSetting
WebClientSetting getWebClientSetting(java.lang.String type)
Returns the web client settings.
 Returns null when there are no web client settings.
Parameters:type - The type of the client for which the setting is to be returned.
Returns:WebClientSetting -
    The web client settings.
    - getWebClientTypes
java.util.List getWebClientTypes()
Returns a list of all web client types.
Returns:List -
    The names of all known web client types,
            that is, returns a list of String objects.
    - getWebClientSettings
java.util.List getWebClientSettings()
Returns a list of all defined web client settings.
Returns:List -
    A list of WebClientSetting objects.
    - getPortalClientSetting
PortalClientSetting getPortalClientSetting(java.lang.String type)
Returns the portal client settings.
 Returns null when there are no portal client settings.
Parameters:type - The type of the client for which the setting is to be returned.
Returns:PortalClientSetting -
    The portal client settings.
    - getPortalClientTypes
java.util.List getPortalClientTypes()
Returns a list of all portal client types.
Returns:List -
    The names of all known portal client types,
            that is, returns a list of String objects.
    - getPortalClientSettings
java.util.List getPortalClientSettings()
Returns a list of all defined portal client settings.
Returns:List -
    A list of PortalClientSetting objects.
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