# Adding IBM Business Automation Workflow and
IBM Federated Process Portal to
use the User Management Service

- If you are using UMS version 1.0.0 that shipped with IBM Business Automation Workflow V18.0.0.1, you must manually update
configuration properties in the
wlp/ibmUserManagement/extension/configTemplates/workflow/connectToUms.jy script
file.
- For UMS version 1.0.1 and later, the configuration properties are in a dedicated file and all
required files are provided in a single .zip package.
- Information that is marked as applying to UMS version 1.1.0 and later, also applies to all
IBM Cloud Pak for Business
Automation UMS versions 19.0.2 and
later.

1 Copy the file wlp/ibmUserManagement/extension/configTemplates/workflow/connectToUms-workflow.zip tothe IBM Business Automation Workflow environment(on the dmgr machine), and extract it to a separate directory foreach IBM Business Automation Workflow system.You will need the contents of this directory if you want to modifyor delete your SSO configuration.Tip: If you deployedUMS on OpenShift or Kubernetes as part of IBM Cloud Pak for BusinessAutomation ,perform the following actions to copy the connectToUms-workflow.zip filefrom your UMS deployment in a container to a local directory:
    1 List the available pods.
        - On OpenShift:oc get pods
        - On Kubernetes:kubectl get pods
2. Note the name of any one of the running UMS pods. The UMS pod
names start with the name of the custom resource and contain the string ums-deployment,
for example, cp4a-cr-ums-deployment-684c6f78bd-1sngq.
Substitute the pod name for podname in
the next step.
3 Get a copy of the connectToUms-workflow.zip file.
    - On OpenShift:oc cp podname:opt/ibm/wlp/ibmUserManagement/extension/configTemplates/workflow/connectToUms-workflow.zip connectToUms-workflow.zip
    - On Kubernetes:kubectl cp podname:opt/ibm/wlp/ibmUserManagement/extension/configTemplates/workflow/connectToUms-workflow.zip connectToUms-workflow.zip
4. Copy the connectToUms-workflow.zip file to
your IBM Business Automation Workflow installation.
2 Apply a matching configuration to the IBM Business Automation Workflow systemby performing the following actions:

1 Edit the provided properties file connectToUms-workflow.properties and set appropriate valuesfor the variables:ums\_host The host name of your User Management Service . ums\_port The HTTPS port of your User Management Service . internal\_ums\_host From UMS version 20.0.3: The internal host name of your User Management Service . internal\_ums\_port The internal HTTPS port of your User Management Service . oidcop\_url\_prefix The full URL prefix of your User Management Service . If this parameteris empty, the value is calculated ashttps://ums\_host :ums\_port /oidc/endpoint/ums . issuer\_identifier The issuer identifier is a value that UMS injects into the signed token. This value can usuallybe identical to oidcop\_url\_prefix . Set this parameter, if you require a differentissuer identifier. internal\_oidcop\_url\_prefix From UMS version 20.0.3: The full internal URL prefix of your User Management Service . oidc\_client\_id Any unique identifier for the client that is being registered with the User Management Service , for example baw2 orportal3 . oidc\_client\_name A description of the client that is being registered with the User Management Service . The default value for this parameter is set to the valueof the client\_id parameter. oidc\_client\_secret This secret for the client that is being registered with the User Management Service is used as a password. You can make up any suitablepassword, for example, baw\_secRET\_98721 . baw\_cellname WebSphere cell name of this environment. baw\_de The name of the IBM Business Automation Workflow deploymentenvironment. baw\_clustername Cluster where to install the OpenID Connect Relying Party application (typically AppTarget). Fora standalone environment leave this blank "" . baw\_nodename and baw\_servername Server where to install the OpenID Connect Relying Party application in a standalone(non-clustered) environment. Values will be ignored, if baw\_clustername isprovided. redirect\_uris (uri\_1, uri\_2,.. uri\_n) This parameter specifies an allowlist of full URLs in the OpenID Connect Relying Party to whichthe user can be redirected after successful authentication. For example, redirect\_uris =https://baw\_host :baw\_port /oidcclient/ums . If usersaccess Process Portal using different URLs, then eachpossible hostname must be listed, separated with commas, for example, redirect\_uris =https://baw:9443/oidcclient/ums,https://baw.example.com:9443/oidcclient/ums . For UMS versions 1.0.0 to 1.0.3, this parameter applies if you setregisterProductionConfiguration is set to true . From UMS version 1.1.0, this parameter must always be specified. BAW\_federated\_portal = (true | false) To set configuration and Oauth settings for Process Portal and register it set this value totrue . For UMS versions 1.0.0 to 1.0.3, this parameter only applies if you setregisterProductionConfiguration is set to true . From UMS version 1.1.0, this parameter does not depend on the value ofregisterProductionConfiguration . portal\_redirect\_uri The full URL in the OpenID Connect Relying Party to which the user can be redirected aftersuccessful authentication. For example,https://baw\_host:baw\_port/ProcessPortal/tokenReceiver.html . The port number must be definedexplicitly, even if you are using port 443. For UMS versions 1.0.0 to 1.0.3, this parameter only applies if you setregisterProductionConfiguration is set to true . From UMS version 1.1.0, this parameter does not depend on the value ofregisterProductionConfiguration . oidc\_portal\_client\_id The client identifier that is being registered with the Offering Party. Unless specified, thisparameter value is generated from oidc\_client\_name +"-ProcessPortal ". oidc\_portal\_client\_name A description for the client that is being registered with the OP. Unless specified, thisparameter is set to the client\_id parameter value by default. reauthAllowed Set to true if clients are allowed to reauthorize. The default value isfalse . logoutTimeoutInSeconds Timeout before user is logged out after they see reauthorization modal. The default value is 60seconds. logoutTimeoutInSecondsWhileReauth Timeout before user is logged out after they started the re-authorization process. The defaultvalue is 120 seconds. registerProductionConfiguration For UMS versions 1.0.0 to 1.0.3 only, this can be set to the value true orfalse . If it is set to true then the following propertiesapply. autoAcceptCertificate Set to true to automatically accept the certificates of the User Management Service server. certificateFingerprint If you specify this optional parameter, the User Management Service fingerprint must match the value specified. ums\_username Optionally specifies the user management admin user. This value must match your User Management Service configuration. If the user name is passed as a command lineparameter, this parameter is ignored. ums\_password Optionally specifies the user management admin user password. This value must match yourUser Management Service configuration. If the password is passed as acommand line parameter, this parameter is ignored. Web\_PD = (true | false) From UMS version 20.0.3: To register the web Process Designer set this value to true . oidc\_webPD\_client\_id From UMS version 20.0.3: A unique identifier for the client that is being registered with theUser Management Service , for example webpd1 . oidc\_webPD\_client\_name From UMS version 20.0.3: A description of the client that is being registered with the User Management Service . The default value for this parameter is set to the valueof the client\_id parameter. oidc\_webPD\_client\_secret From UMS version 20.0.3: This secret for the client that is being registered with the User Management Service is used as a password. You can make up any suitablepassword, for example, webpd\_secRET\_98721 . webPD\_redirect\_uri From UMS version 20.0.3: The full URL in the OpenID Connect Relying Party to which the user canbe redirected after successful authentication, for examplehttps://webPD\_host:webPD\_port/WebPD/jsp/tokenRecever.html . Important: For a production environment, setoidcop\_url\_prefix for all clones to the URL of your web server. Set thesame value for the attribute issuerIdentifier on theopenidConnectProvider configuration element in each clone'swlp/usr/servers/serverName/server.xml file. Forexample:<openidConnectProvider id="ums" oauthProviderRef="oidcOAuthProvider" issuerIdentifier="https://umshost/oidc/endpoint/ums" /> Aspart of the OpenID Connect protocol, the User Management Service issues IDtokens in JSON Web Token (JWT) format, as specified in RFC 7519 . One of the claims inthese tokens is issuer , which is used to identify the entity that issued the token.This step is required because by default, the User Management Service specifies the URL of the server as the issuer, which works for a single server, but doesn't work formultiple servers. For more information, see openidConnectProvider - OpenID Connect Server Provider(openidConnectProvider) .
    - If this parameter is empty, the value from ums\_host will be used.
    - If your  Business Automation Workflow and your User Management Service are both in the same
datacenter and need to use some internal connection to communicate, you have to set this
parameter.
    - If this parameter is empty, the value is calculated as
https://internal\_ums\_host:internal\_ums\_port/oidc/endpoint/ums.
    - If your  Business Automation Workflow and your User Management Service are both in the same
datacenter and need to use some internal connection to communicate, you might set this
parameter.

If users
access Process Portal using different URLs, then each
possible hostname must be listed, separated with commas, for example, redirect\_uris =
https://baw:9443/oidcclient/ums,https://baw.example.com:9443/oidcclient/ums.

```
<openidConnectProvider id="ums" oauthProviderRef="oidcOAuthProvider" 
     issuerIdentifier="https://umshost/oidc/endpoint/ums" />
```

2 Set up the environment variables that points to IBM Business Automation Workflow installationdirectory:

1 Open a command prompt and navigate to the following directory: Where profile\_name is the profile name of the DeploymentManager (typically, this is Dmgr01 ) and drive :is the system drive on which the file directory is stored. For example: C: or D: .
    - Linux: /opt/IBM/WebSphere/AppServer/profiles/profile\_name/bin
    - Windows: drive:\Program Files\IBM\WebSphere\AppServer\profiles\profile\_name\bin

Where profile\_name is the profile name of the Deployment
Manager (typically, this is Dmgr01) and drive:
is the system drive on which the file directory is stored. For example: C: or D:.

2 Execute the following script:

- Linux: . setupCmdLine.sh
- Windows: setupCmdLine.bat
3. Make sure that the Deployment Manager is running.
4 Make sure that the User Management Service is running.

- To start the Liberty server
named serverName, issue the following command from
the wlp\bin directory:server start serverName
- To stop the Liberty server
named serverName, issue the following command from
the wlp\bin directory:server stop serverName
5 Run connectToUms.bat or connectToUms.sh toexecute the parameters of your customized properties file. For example:connectToUms.[bat|sh][action][options...] For example, on Windows:connectToUms.bat add -username <user name> -password <password> -ums\_username <User Management admin user> -ums\_password <User Management admin user password> Where action can be one of the following:add Add a client. remove Remove an existing client. modify Modify an existing client. Options can be the following:-? | -help This help message. u <username> | -username <username> The user name of the Administrator role on WebSphere® ApplicationServer . Thisadministrator must be configured at the cell level, not at the cluster,node, or server level. -p <password> | -password <password> The password of the WebSphere ApplicationServer (unencrypted). -ums\_username <UMS username> User name of User Management Server administrator. -ums\_password <UMS password> The user password of User Management Server administrator (unencrypted). Note: The batch file performs the following actions: For more information, see Configuring an OpenID Connect Provider to acceptclient registration requests .

```
connectToUms.[bat|sh][action][options...]
```

```
connectToUms.bat add -username <user name> -password <password> 
     -ums\_username <User Management admin user>  -ums\_password <User Management admin user password>
```

1. Register the 
WebSphere
 provided
OpenID Connect Relying Party Trust Association Interceptor (TAI).
2. Configure custom properties for the TAI to point to the User Management Service.
3. Install the 
WebSphere
 provided
OpenID Connect application.
4. Import the SSL certificate of the User Management Service into IBM Business Automation Workflow default
trust store.
5. Configures a logout exit page so that users log out of the User Management Service after logging
out of IBM Business Automation Workflow.
6. Register IBM Business Automation Workflow as
a client with the OpenID Connect Provider.
7. Register Process Portal as
a client with the OpenID Connect Provider.
8. Configure OAuth for Process Portal.
9. Configure Mashups Config Service for Process Portal.

For more information, see Configuring an OpenID Connect Provider to accept
client registration requests.

3. Save and synchronize the configuration and restart your environment.
For information about synchronizing, see Synchronizing nodes using the wsadmin scripting tool.