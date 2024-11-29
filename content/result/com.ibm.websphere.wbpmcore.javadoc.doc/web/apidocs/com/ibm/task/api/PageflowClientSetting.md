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

## Interface PageflowClientSetting

- All Superinterfaces:
ClientSetting, java.lang.Cloneable, java.io.Serializable

public interface PageflowClientSetting
extends ClientSetting
Interface for pageflow client settings. Pageflow client settings
 extend the client settings with the ability to associate a set of
 usage patterns with a URL.
 
 A sample pageflow client setting follows:
 

<customClientSettings clientType="IBM-Pageflow-Coach">
 
 <customsetting name="pageflow" value="fileName.pageflow">
 
</customClientSettings>
 
Since:
7.1

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