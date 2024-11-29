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

## Interface ClientSetting

- All Superinterfaces:
java.lang.Cloneable, java.io.Serializable

All Known Subinterfaces:
PageflowClientSetting, PortalClientSetting, WebClientSetting

public interface ClientSetting
extends java.io.Serializable, java.lang.Cloneable
Interface that supports the definition of user specific client settings.
 
 Client settings can be attached to a task in order to overwrite
 Human Task Manager provided task instance property pages.
 
 A client setting specifies the type of the client for which it is to be used
 and a number of custom settings in the form of type name and value pairs.
 
 A client setting can look like following:
 

<wpc:webClientSettings clientType="Default">
 
 <wpc:customSetting name="approval" value="yes"/>
 
</wpc:webClientSettings>
 
Since:
5.1
See Also:Serializable

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
getClientType()
Returns the type of the client for which this setting is defined.

java.lang.String
getCustomSetting(java.lang.String name)
Returns the value of the specified custom setting.

java.util.List
getCustomSettingNames()
Returns the names of all defined custom settings.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getClientType
java.lang.String getClientType()
Returns the type of the client for which this setting is defined.
Returns:String - The client type.
    - getCustomSetting
java.lang.String getCustomSetting(java.lang.String name)
Returns the value of the specified custom setting.
 Null is returned when the specified custom setting cannot be found.
Parameters:name - The name of the custom setting whose value is to be returned.
Returns:String - The value of the specified custom setting.
    - getCustomSettingNames
java.util.List getCustomSettingNames()
Returns the names of all defined custom settings.
Returns:List - The names of all defined custom settings.