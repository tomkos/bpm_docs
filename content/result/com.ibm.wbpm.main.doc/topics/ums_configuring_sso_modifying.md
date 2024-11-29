# Modifying a  single sign-on configuration

1 If you want to modify an IBM® Business Automation Workflow singlesign-on configuration, you must set up the environment variables thatpoints to IBM Business Automation Workflow installationdirectory:
    1 Open a command prompt and navigate to the following directory: Where profile\_name is the profile name of the DeploymentManager (typically, this is Dmgr01 ) and drive :is the system drive on which the file directory is stored. For example: C: or D: .
        - Linux: /opt/IBM/WebSphere/AppServer/profiles/profile\_name/bin
        - Windows: drive:\Program Files\IBM\WebSphere\AppServer\profiles\profile\_name\bin

Where profile\_name is the profile name of the Deployment
Manager (typically, this is Dmgr01) and drive:
is the system drive on which the file directory is stored. For example: C: or D:.

2 Execute the following script:
    - Linux: ./setupCmdLine.sh
    - Windows:  setupCmdLine.bat
2. Edit the properties file for configuration that you want to modify:
For an IBM Business Automation Workflow 
or Process Portal 
configuration
Reuse the connectToUms-workflow.properties file
that was edited in the add scenario and modify the parameters that
have changed. Important: If you connected your IBM Business Automation Workflow system
to User Management 1.0.0, you do not yet have a connectToUms-workflow.properties file.
Use the template from wlp/ibmUserManagement/extension/configTemplates/workflow/connectToUms-workflow.zip and
adapt the properties matching the connectToUms.jy script
that was executed at the time of connecting.

For a Process Federation Server 
configuration
Reuse the connectToUms-PFS.properties file
that was edited in the add scenario and modify the parameters that
have changed.
3 Run connectToUms.bat or connectToUms.sh to execute theparameters of your customized properties file. For example: For an IBM Business Automation Workflow or Process Portal configuration Enter thecommand:connectToUms.bat modify -username <user name> -password <password> -ums\_username <User Management admin user> -ums\_password <User Management admin user password> For a Process Federation Server configuration

```
connectToUms.bat modify -username <user name> -password <password> 
   -ums\_username <User Management admin user>  -ums\_password <User Management admin user password>
```

1. Enter the
command:connectToUms.bat modify
   -ums\_username <User Management admin user> -ums\_password <User Management admin user password>
2. If the modified parameters affect values that were entered into the Process Federation Server
server.xml file from the
wlp/ibmUserManagement/extension/configTemplates/pfs/PFS-template-server.xml
file, you must edit the changed values into the server.xml file.
3. If the modified parameter values affect the server certificates in the truststore, for example,
if a different User Management Service server is used, Add the new
User Management Service server certificate to the Process Federation Server truststore by using the standard
IBM
WebSphere® Application Server Liberty procedure. For more
information, see Adding trusted certificates in Liberty.
4. For an environment with multiple User Management Service servers behind a web server set the value for the attribute
issuerIdentifier on the openidConnectClient configuration element
in the server.xml file. For example:
<openidConnectClient id="umsClient" issuerIdentifier="https://webserverhost/oidc/endpoint/ums" />
This value must be identical with the issuerIdentifier set for the
openidConnectProvider configuration element in the User Management Server server.xml As part of
the OpenID Connect protocol, the User Management Service issues ID tokens in JSON Web Token (JWT)
format, as specified in RFC
7519. One of the claims in these tokens is issuer, which is used to identify the entity that
issued the token. This step is required because by default, the User Management Service specifies
the URL of the server as the issuer, which works for a single server, but doesn't work for multiple
servers. For more information, see openidConnectProvider - OpenID Connect Server Provider
(openidConnectProvider).
4. For UMS version 1.0.0, 1.0.1, and 1.0.3 quick start configurations, you must also modify the
client in your User Management Service configuration XML files.
5. For an IBM Business Automation Workflow 
or  Process Portal 
configuration, save and synchronize the configuration and restart
your environment. For information about synchronizing, see Synchronizing nodes using the wsadmin scripting tool.