- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class RESTHttpURLConnection

- java.lang.Object
    - com.ibm.casemgmt.api.icnrest.RESTURLConnection
        - com.ibm.casemgmt.api.icnrest.RESTHttpURLConnection

- public class RESTHttpURLConnection
extends RESTURLConnection
This code was adapted from the RESTHttpURLConnection from the RESTAPITEST
 component. It is used to handle the method invocation with the CASEREST APIs.

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

### Field Summary

    - Fields inherited from class com.ibm.casemgmt.api.icnrest.RESTURLConnection
ACCE\_DESKTOP\_APPNAME, ACCE\_DESKTOP\_DESC, ACCE\_DESKTOP\_ID, ACCE\_DESKTOP\_NAME, ACCE\_PLUGIN\_ID, ADMIN\_PLUGIN\_ID, BOX\_EVENT\_LISTENER\_PLUGIN\_ID, BPM\_PLUGIN\_ID, CC\_PLUGIN\_ID, customDocumentContextMenuBPM, ICM\_ADMIN\_DESKTOP\_APPNAME, ICM\_ADMIN\_DESKTOP\_DESC, ICM\_ADMIN\_DESKTOP\_ID, ICM\_ADMIN\_DESKTOP\_NAME, ICM\_API\_PLUGIN\_ID, ICM\_DESKTOP\_APPNAME, ICM\_DESKTOP\_DESC, ICM\_DESKTOP\_ID, ICM\_DESKTOP\_NAME, ICM\_MONITOR\_DESKTOP\_APPNAME, ICM\_MONITOR\_DESKTOP\_DESC, ICM\_MONITOR\_DESKTOP\_ID, ICM\_MONITOR\_DESKTOP\_NAME, ICM\_MONITOR\_PLUGIN\_ID, MOBILE\_PLUGIN\_ID, NAVIGATOR\_ADMIN\_DESKTOP\_ID, NAVIGATOR\_ADMIN\_DESKTOP\_NAME, PD\_PLUGIN\_ID, XT\_PLUGIN\_ID

- Constructor Summary

Constructors 

Constructor and Description

RESTHttpURLConnection(java.lang.String username,
                     java.lang.String password)

- Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description void disconnect () java.lang.String getBearerToken (java.lang.String umsURL) java.lang.String getBearerToken (java.lang.String openIDTokenURL, java.lang.String preAuthURL) org.apache.commons.json.JSONObject getNavigatorSecurityToken (java.lang.String navigatorURL, java.lang.String bearerToken) boolean invoke (java.lang.String resourceURL, java.lang.String requestMethod, java.util.HashMap<java.lang.String,java.util.List<java.lang.String>> requestHeaders, java.lang.String content) Invokes the desired CASE REST API on the specified URL.

### Method Summary

| Modifier and Type                  | Method and Description                                                                                                                                                                                                                                        |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                               | disconnect()                                                                                                                                                                                                                                                  |
| java.lang.String                   | getBearerToken(java.lang.String umsURL)                                                                                                                                                                                                                       |
| java.lang.String                   | getBearerToken(java.lang.String openIDTokenURL,               java.lang.String preAuthURL)                                                                                                                                                                    |
| org.apache.commons.json.JSONObject | getNavigatorSecurityToken(java.lang.String navigatorURL,                          java.lang.String bearerToken)                                                                                                                                               |
| boolean                            | invoke(java.lang.String resourceURL,       java.lang.String requestMethod,       java.util.HashMap<java.lang.String,java.util.List<java.lang.String>> requestHeaders,       java.lang.String content) Invokes the desired CASE REST API on the specified URL. |

    - Methods inherited from class com.ibm.casemgmt.api.icnrest.RESTURLConnection
createURLConnection, formatJSON, formatNexusError, getErrorStream, getHeaderField, getInputStream, getLastResponse, getP8TOSRepoId, getParamString, getResponse, getResponseCode, getResponseMessage, getSecurityToken, getUmsURL, isSSL, listRepositories, setSecurityToken, testLogin, testNavigatorlogin, testUMSNavigatorlogin, useUmsOrZen
    - Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait