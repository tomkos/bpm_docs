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

## Interface WebClientSetting

- All Superinterfaces:
ClientSetting, java.lang.Cloneable, java.io.Serializable

public interface WebClientSetting
extends ClientSetting
Interface for Web client settings. Web client settings
 extend the client settings with the ability to associate a set of
 usage patterns with a URL.
 
 A sample web client setting follows:
 

<wpc:webClientSettings clientType="HTM Web Client">
 
 <wpc:jsp for="page" uri="approvePage.jsp"/>
 
 <wpc:jsp for="input" uri="approveInput.jsp"/>
 
 <wpc:jsp for="output" uri="approveOutput.jsp"/>
 
 <wpc:jsp for="map" uri="approveMap.jsp"/>
 
</wpc:webClientSettings>
 
Since:
6.0 - introduced in 5.1

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description JspApplicableRoleEnum [] getApplicableRoles () Returns the roles the currently logged-on user belongs to. JspLocation getJspLocation (JspUsageEnum usage) Returns the JSP location for the specified usage pattern, if any. JspLocation getJspLocation (JspUsageEnum usage, JspApplicableRoleEnum applicableRole) Returns the JSP location for the specified usage pattern and role. JspLocation getJspLocation (java.lang.String faultName, JspApplicableRoleEnum applicableRole) Returns the JSP location for the usage pattern fault and the specified fault name and role. JspLocation [] getJspLocations (JspUsageEnum usage) Returns the JSP locations for the specified usage pattern, if any.

### Method Summary

| Modifier and Type       | Method and Description                                                                                                                                                                      |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| JspApplicableRoleEnum[] | getApplicableRoles() Returns the roles the currently logged-on user belongs to.                                                                                                             |
| JspLocation             | getJspLocation(JspUsageEnum usage) Returns the JSP location for the specified usage pattern, if any.                                                                                        |
| JspLocation             | getJspLocation(JspUsageEnum usage,               JspApplicableRoleEnum applicableRole) Returns the JSP location for the specified usage pattern and role.                                   |
| JspLocation             | getJspLocation(java.lang.String faultName,               JspApplicableRoleEnum applicableRole) Returns the JSP location for the usage pattern fault and the  specified fault name and role. |
| JspLocation[]           | getJspLocations(JspUsageEnum usage) Returns the JSP locations for the specified usage pattern, if any.                                                                                      |

- Methods inherited from interface com.ibm.task.api.ClientSetting
getClientType, getCustomSetting, getCustomSettingNames