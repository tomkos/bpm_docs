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

## Interface PortalClientSetting

- All Superinterfaces:
ClientSetting, java.lang.Cloneable, java.io.Serializable

public interface PortalClientSetting
extends ClientSetting
Interface for Portal client settings. Portal client settings
 extend the client settings with the ability to associate a set of
 usage patterns with a URL.
 
 A sample portal client setting follows:
 

<portalClientSettings clientType="Portal">
 
</portalClientSettings>
 
Since:
6.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

### Method Summary

- Methods inherited from interface com.ibm.task.api.ClientSetting
getClientType, getCustomSetting, getCustomSettingNames