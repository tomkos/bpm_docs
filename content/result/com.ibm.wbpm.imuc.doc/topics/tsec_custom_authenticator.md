# Configuring a custom authenticator plug-in

## Before you begin

- The desktop Process Designer is deprecated. Use
the Process Designer instead.
- Verify the type of third-party authentication SSO that you are using, for example, IBM HTTP Server (IHS) or SiteMinder.
- Business Automation Workflow provides the plug-in extension
point and the required interfaces. You must build the plug-in and define the underlying logic that
interacts with the user and your SSO solution. This requires Eclipse plug-in development
skills.
- If the custom authenticator configuration is completed before you install desktop IBM
Process Designer, it can be included with
desktop Process Designer.
- The httpProtocolOnly property must be set to true for desktop Process Designer, which is the
default setting. See Configuring the httpProtocolOnly property for Process
Designer.
- For some external links to work properly with a custom authenticator plug-in, set
add-redirect-url-credentials to false, for example, the generated report link for a
process application. For information about setting properties, see Connections from IBM Process Designer to Workflow Center.

## About this task

You build a custom plug-in that defines a login authenticator in desktop Process Designer. The login authenticator must declare
an extension for client-side login logic to address special authentication requirements from the
server side. When authentication is triggered, Process Designer uses the custom plug-in to trigger the login
logic. The authenticator extension point is an API that is provided in the Eclipse plug-in
format.

- The first set of security tokens is shared among all connections that use Java™ HTTP clients that are triggered by user Create, Read, Update and Delete
(CRUD) activities in one desktop Process Designer.
This set supports inactivity timeouts on user interaction requests.
- The second set of security tokens is shared during desktop Process Designer and Workflow Center communication, CometD initialization, and the
use of embedded browsers. This set does not support inactivity timeouts.

## Procedure

1. In Eclipse or IBM Integration
Designer, create a
plug-in project for your custom authenticator plug-in.
2. Import the com.ibm.bpm.client.ae.security.authentication plug-in in to your
workspace to make its extension point available. The JAR file is in the <pd\_
install>/teamworks/eclipse/plugins/ directory.
3. Add a dependency to the com.ibm.bpm.client.ae.security.authentication plug-in
from your new plug-in.
4. In your plug-in, add an extension for the
com.ibm.bpm.client.ae.security.authentication.authenticators extension point. The
extension includes an authenticator element that has the following attributes:
class and isCustom. Add your class that implements the login API
to the class attribute. You can leave IsCustom blank or set it to
true. The default setting is true.
For example, your plugin.xml file might contain an extension that looks
similar to the following
code:<extension point="com.ibm.bpm.client.ae.security.authentication.authenticators">     
   <Authenticator           
      class="myauthPlugin.Authenticator1"           
      isCustom="true">
   </Authenticator>
</extension>
5. Define your class to implement the login API. Desktop Process Designer calls this API.
6 Implement the ILoginResult interface. It returns the results of the loginAPI. Note: You must define the logic to interact with the SSO system, the user, and theILoginResult interface as described in this topic. Business Automation Workflow does not provide the code for it. Business Automation Workflow includes aBPM\_GENERIC\_HEADER header in the response. If the HTTP return code for a particularHTTP request is less than 400 , for example 302 , and theBPM\_GENERIC\_HEADER header is not in the response, desktop Process Designer calls the login API from the customplug-in. In addition, if one of the following conditions are true, desktop Process Designer also calls the custom plug-in: public abstract ILoginResult login(String userId, String url, int returnCode, Map<String, List<String>> responseHeaders, InputStream responseBody) throws Exception; The login API uses the followingparameters:userId - the userId that is returned by the previous login. It is null if it is the first login.url - the url that is being accessedreturnCode - the HTTP return code that is returned when Process Designer accessed the URLresponseHeaders - Map<String, List<String>> containing the response headers. Keys are header names and values are a list of header values. responseBody - InputStream with the response body. Process Designer will close the InputStream.ILoginResult - This should contain the results of your login logic, which includes the security cookies, proxy details, and userID.exception: if login fails, throw an Exception with a localized message. In addition to the logic that is used to set variable data for the ILoginResult interface, you must implement these four methods that desktop Process Designer uses to get the results of the loginlogic. public Collection<String> getRequestTokens();Returns the security tokens for normal user interactions if login was needed otherwise returns null.The items in Collection are the external format of the cookies, such as: SMTRYNO=; expires=Fri, 11 Jan 2013 13:54:32 GMT; path=/; domain=ibm.com; HTTPOnly public Collection<String> getPollingTokens();Returns polling security tokens if an inactive-session timeout is required for normal user interactions otherwise returns null.The items in Collection are the external format of the cookies, such as: SMTRYNO=; expires=Fri, 11 Jan 2013 13:54:32 GMT; path=/; domain=ibm.com; HTTPOnly public String getProxyAuthorizationHeader();Obtains the proxy authorization header if the returnCode is 407 otherwise returns null, such as: NTLM TlRMTVNTUAADAAAAGAAYAHIAAAAYABgAigAAABIAEgBIAAAABgAGAFoAA public String getUserId();Returns the userId of the person logged in. The userId cannot be null.
    - If the HTTP return code is 401
    - If the HTTP return code is 407

```
public abstract ILoginResult login(String userId, String url, int returnCode, 
            Map<String, List<String>> responseHeaders, InputStream responseBody) 
            throws Exception;
```

```
userId - the userId that is returned by the previous login. It is null if it is the first login.
url - the url that is being accessed
returnCode - the HTTP return code that is returned when Process Designer accessed the URL
responseHeaders - Map<String, List<String>> containing the response headers. Keys are header names
             and values are a list of header values. 
responseBody - InputStream with the response body. Process Designer will close the InputStream.
ILoginResult - This should contain the results of your login logic, which includes the security cookies, proxy details, and userID.

exception: if login fails, throw an Exception with a localized message.
```

In addition to the logic that is used to set variable data for the ILoginResult
interface, you must implement these four methods that desktop Process Designer uses to get the results of the login
logic.

```
public Collection<String> getRequestTokens();
Returns the security tokens for normal user interactions if login was needed otherwise returns null.
The items in Collection are the external format of the cookies, such as:
     SMTRYNO=; expires=Fri, 11 Jan 2013 13:54:32 GMT; path=/; 
     domain=ibm.com; HTTPOnly
```

```
public Collection<String> getPollingTokens();
Returns polling security tokens if an inactive-session timeout is required for normal user interactions otherwise returns null.
The items in Collection are the external format of the cookies, such as:
      SMTRYNO=; expires=Fri, 11 Jan 2013 13:54:32 GMT; path=/; 
      domain=ibm.com; HTTPOnly
```

```
public String getProxyAuthorizationHeader();
Obtains the proxy authorization header if the returnCode is 407 otherwise returns null, such as:
     	NTLM TlRMTVNTUAADAAAAGAAYAHIAAAAYABgAigAAABIAEgBIAAAABgAGAFoAA
```

```
public String getUserId();
Returns the userId of the person logged in. The userId cannot be null.
```

7. Optional: 
After you generate your plug-in JAR file, test it with desktop Process Designer by placing it in the
<pd\_install>/teamworks/eclipse/plugins/ directory and restarting desktop Process Designer.
8 Make your custom plug-in JAR file available to new desktop Process Designer installations:

1. Place the custom authenticator plug-in JAR files in the
BPM\Lombardi\tools\designer\dropins directory.
2. Download desktop Process Designer from Workflow Center. Workflow Center discovers new files in
the dropins directory and includes them in the downloaded IBM Process
Designer.zip file.
9 Optional: Make your custom plug-in JAR file available to existing Process Designer installations:

1. Ensure that the new plug-in JAR files are added to the
BPM\Lombardi\tools\designer\dropins directory.
2. Uninstall desktop Process Designer.
3. Download an updated desktop Process Designer
installation .zip file from Workflow Center.