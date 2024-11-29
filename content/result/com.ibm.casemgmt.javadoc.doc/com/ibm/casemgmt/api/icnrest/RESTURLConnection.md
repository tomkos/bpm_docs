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

## Class RESTURLConnection

- java.lang.Object
    - com.ibm.casemgmt.api.icnrest.RESTURLConnection

- Direct Known Subclasses:
RESTHttpsURLConnection, RESTHttpURLConnection

public abstract class RESTURLConnection
extends java.lang.Object
Abstract class for any class that uses URL Connections, so that we can
 use the same variables for HTTP or HTTPS

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
ACCE\_DESKTOP\_APPNAME 

static java.lang.String
ACCE\_DESKTOP\_DESC 

static java.lang.String
ACCE\_DESKTOP\_ID 

static java.lang.String
ACCE\_DESKTOP\_NAME 

static java.lang.String
ACCE\_PLUGIN\_ID 

static java.lang.String
ADMIN\_PLUGIN\_ID 

static java.lang.String
BOX\_EVENT\_LISTENER\_PLUGIN\_ID 

static java.lang.String
BPM\_PLUGIN\_ID 

static java.lang.String
CC\_PLUGIN\_ID 

static java.lang.String
customDocumentContextMenuBPM 

static java.lang.String
ICM\_ADMIN\_DESKTOP\_APPNAME 

static java.lang.String
ICM\_ADMIN\_DESKTOP\_DESC 

static java.lang.String
ICM\_ADMIN\_DESKTOP\_ID 

static java.lang.String
ICM\_ADMIN\_DESKTOP\_NAME 

static java.lang.String
ICM\_API\_PLUGIN\_ID 

static java.lang.String
ICM\_DESKTOP\_APPNAME 

static java.lang.String
ICM\_DESKTOP\_DESC 

static java.lang.String
ICM\_DESKTOP\_ID 

static java.lang.String
ICM\_DESKTOP\_NAME 

static java.lang.String
ICM\_MONITOR\_DESKTOP\_APPNAME 

static java.lang.String
ICM\_MONITOR\_DESKTOP\_DESC 

static java.lang.String
ICM\_MONITOR\_DESKTOP\_ID 

static java.lang.String
ICM\_MONITOR\_DESKTOP\_NAME 

static java.lang.String
ICM\_MONITOR\_PLUGIN\_ID 

static java.lang.String
MOBILE\_PLUGIN\_ID 

static java.lang.String
NAVIGATOR\_ADMIN\_DESKTOP\_ID 

static java.lang.String
NAVIGATOR\_ADMIN\_DESKTOP\_NAME 

static java.lang.String
PD\_PLUGIN\_ID 

static java.lang.String
XT\_PLUGIN\_ID
    - Constructor Summary

Constructors 

Constructor and Description

RESTURLConnection()
    - Method Summary All Methods Static Methods Instance Methods Abstract Methods Concrete Methods Modifier and Type Method and Description static RESTURLConnection createURLConnection (java.lang.String url, java.lang.String username, java.lang.String password) Factory Method for creating a RESTURLConnection, based on the intended URL to be used. abstract void disconnect () static java.lang.String formatJSON (java.lang.String jsonText, int numIndents) Formats the input JSON text in a visually pleasing manner. static java.lang.String formatNexusError (java.lang.String nexusError) Formats the returned Nexus error into something human readable. abstract java.lang.String getBearerToken (java.lang.String umsURL) abstract java.lang.String getBearerToken (java.lang.String iam\_external\_hostname, java.lang.String preAuthURL) java.io.InputStream getErrorStream () java.util.List<java.lang.String> getHeaderField (java.lang.String name) java.io.InputStream getInputStream () static java.lang.String getLastResponse () abstract org.apache.commons.json.JSONObject getNavigatorSecurityToken (java.lang.String navigatorURL, java.lang.String bearerToken) org.apache.commons.json.JSONObject getP8TOSRepoId (java.lang.String url, java.lang.String osSymbolicName) Get the properties for a P8 repository for an object store static java.lang.String getParamString (java.util.Map<java.lang.String,java.lang.String> params) Takes a list of HTTP parameters (String key/value pairs) and formats them into the URL parameter string static java.lang.String getResponse (java.io.InputStream in) Helper for getting the response of the HTTP connection int getResponseCode () java.lang.String getResponseMessage () java.lang.String getSecurityToken () java.lang.String getUmsURL (java.lang.String umsClientID) abstract boolean invoke (java.lang.String resourceURL, java.lang.String requestMethod, java.util.HashMap<java.lang.String,java.util.List<java.lang.String>> requestHeaders, java.lang.String content) Invokes the desired CASE REST API on the specified URL. static boolean isSSL (java.lang.String url) Determine if the URL needs to use SSL java.util.List<org.apache.commons.json.JSONObject> listRepositories (java.lang.String url) List existing repositories, including name and id void setSecurityToken (java.lang.String securityToken) Sets the Security token to use for Nexus transactions boolean testLogin (java.lang.String url) Test connection to the Nexus server boolean testNavigatorlogin (java.lang.String nexusURL) boolean testUMSNavigatorlogin (java.lang.String umsURL, java.lang.String nexusURL) boolean useUmsOrZen ()

### Method Summary

| Modifier and Type                                  | Method and Description                                                                                                                                                                                                                                        |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static RESTURLConnection                           | createURLConnection(java.lang.String url,                    java.lang.String username,                    java.lang.String password) Factory Method for creating a RESTURLConnection, based on the intended  URL to be used.                                 |
| abstract void                                      | disconnect()                                                                                                                                                                                                                                                  |
| static java.lang.String                            | formatJSON(java.lang.String jsonText,           int numIndents) Formats the input JSON text in a visually pleasing manner.                                                                                                                                    |
| static java.lang.String                            | formatNexusError(java.lang.String nexusError) Formats the returned Nexus error into something human readable.                                                                                                                                                 |
| abstract java.lang.String                          | getBearerToken(java.lang.String umsURL)                                                                                                                                                                                                                       |
| abstract java.lang.String                          | getBearerToken(java.lang.String iam\_external\_hostname,               java.lang.String preAuthURL)                                                                                                                                                             |
| java.io.InputStream                                | getErrorStream()                                                                                                                                                                                                                                              |
| java.util.List<java.lang.String>                   | getHeaderField(java.lang.String name)                                                                                                                                                                                                                         |
| java.io.InputStream                                | getInputStream()                                                                                                                                                                                                                                              |
| static java.lang.String                            | getLastResponse()                                                                                                                                                                                                                                             |
| abstract org.apache.commons.json.JSONObject        | getNavigatorSecurityToken(java.lang.String navigatorURL,                          java.lang.String bearerToken)                                                                                                                                               |
| org.apache.commons.json.JSONObject                 | getP8TOSRepoId(java.lang.String url,               java.lang.String osSymbolicName) Get the properties for a P8 repository for an object store                                                                                                                |
| static java.lang.String                            | getParamString(java.util.Map<java.lang.String,java.lang.String> params) Takes a list of HTTP parameters (String key/value pairs) and formats  them into the URL parameter string                                                                              |
| static java.lang.String                            | getResponse(java.io.InputStream in) Helper for getting the response of the HTTP connection                                                                                                                                                                    |
| int                                                | getResponseCode()                                                                                                                                                                                                                                             |
| java.lang.String                                   | getResponseMessage()                                                                                                                                                                                                                                          |
| java.lang.String                                   | getSecurityToken()                                                                                                                                                                                                                                            |
| java.lang.String                                   | getUmsURL(java.lang.String umsClientID)                                                                                                                                                                                                                       |
| abstract boolean                                   | invoke(java.lang.String resourceURL,       java.lang.String requestMethod,       java.util.HashMap<java.lang.String,java.util.List<java.lang.String>> requestHeaders,       java.lang.String content) Invokes the desired CASE REST API on the specified URL. |
| static boolean                                     | isSSL(java.lang.String url) Determine if the URL needs to use SSL                                                                                                                                                                                             |
| java.util.List<org.apache.commons.json.JSONObject> | listRepositories(java.lang.String url) List existing repositories, including name and id                                                                                                                                                                      |
| void                                               | setSecurityToken(java.lang.String securityToken) Sets the Security token to use for Nexus transactions                                                                                                                                                        |
| boolean                                            | testLogin(java.lang.String url) Test connection to the Nexus server                                                                                                                                                                                           |
| boolean                                            | testNavigatorlogin(java.lang.String nexusURL)                                                                                                                                                                                                                 |
| boolean                                            | testUMSNavigatorlogin(java.lang.String umsURL,                      java.lang.String nexusURL)                                                                                                                                                                |
| boolean                                            | useUmsOrZen()                                                                                                                                                                                                                                                 |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait