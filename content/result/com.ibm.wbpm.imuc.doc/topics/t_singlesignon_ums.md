# Configuring single sign-on with UMS for an external Content Platform Engine

## Procedure

To configure single sign-on for an external Content Platform Engine, complete the following steps:

1 Configure access to a shared user repository. Both IBM Business Automation Workflow and Content Platform Engine must have access to the same set of users.Therefore, configure both cells to access the same user repository (such as a Lightweight DirectoryAccess Protocol (LDAP) directory). To configure access to a shared user repository, follow thesesteps: There is no need to remove or disable any file-based registries on the two systems.The registries can still be useful for administrative functions. Note, however, that users andgroups from file-based registries cannot be used in Business Automation Workflow case applications. In the WebSphereadministrative console of both systems, select Users and Groups > Manage Users and search for the Business Automation Workflow userID that you are going to define as the ECM administrative user. Verify that the user ID is uniqueand it is in the shared user repository.
    1. In the WebSphere® Application
Server administrative console on
both systems, select Security > Global Security. The Global Security page opens.
    2 In the Available realm definitions drop-down list, select one of theseoptions:
        - If Content Platform Engine is configured with a federated
repository, select Federated Repositories and then click
Configure. The Federated Repositories page opens.
        - If Content Platform Engine is configured with a stand-alone
LDAP, select Standalone LDAP and then click Configure.
The Standalone LDAP page opens.
3. Configure your shared user repository with matching user and group attributes.
4. Test your LDAP connection. See Configuring Content Platform
Engine application server authentication (LDAP) settings.
5. If the realm names of Business Automation Workflow and Content Platform Engine are different (for example, because you set
different active realm definitions), make certain that in each cell the realm of the other cell is
trusted. From the navigation panel, click Security > Global security. Under RMI/IIOP security, click CSIv2 inbound
communications. Click Trusted authentication realms - inbound.
Select Trust realms as indicated below. Click Add external
realm and add the realm of the remote cell. Click Apply.

In the WebSphere
administrative console of both systems, select Users and Groups > Manage Users and search for the Business Automation Workflow user
ID that you are going to define as the ECM administrative user. Verify that the user ID is unique
and it is in the shared user repository.

2. Configure single sign on with an OpenID connect Relying Party(OIDC RP) system. You must
configure Business Automation Workflow and Content Platform Engine with the same User Management Service (UMS). You must have consistently matching
configuration data for your relying party system and UMS, which acts as the OpenID Connect Offering
Party (OIDC OP).   For information about how to configure IBM Business Automation
Workflow with UMS, see Configuring single sign-on for UMS.
3. Configure the Java Authentication and Authorization Service (JAAS) login module used by
the Content Platform Engine client.

Make sure that you have configured the com.filenet.api.util.WSILoginModule in
WebSphere Application
Server global security. If you have not
configured it, add the login module by logging in to the WebSphere administrative console. Go to
Security > Global
security > Authentication > Java Authentication and
Authorization Service > Application logins and click
New. Enter FileNetP8WSI for the Alias. Click
New and enter com.filenet.api.util.WSILoginModule for
the Module class name. Check Use login module proxy  and save your
configuration.
4 Configure the Business Automation Workflow deploymentmanager to use a username and password for authentication when it connects to the Content Platform Engine server. Log in to the Business Automation Workflow WebSphereadministrative console. Go to System administration > Deployment manager > Java and ProcessManagement > Process definition > Java VirtualMachine > Configuration and add the followingparameters for Generic JVM arguments: Save your configuration.

- -Dcom.filenet.authentication.wsi.AutoDetectAuthToken=false
- -DFileNet.WSI.AutoDetectLTPAToken=false
- -DFileNet.WSI.custom.credential.class=com.filenet.apiimpl.wsi.WSICredential
5 Add the Jace.jar to your classpath: In the administrative console, go to System administration > Deployment manager > Java and ProcessManagement > Process definition > Java VirtualMachine > Configuration and add the followingparameters to the Classpath: Save your configuration.

- install\_root/BPM/FileNet/lib/Jace.jar
- install\_root/BPM/FileNet/lib/log4j.jar
- install\_root/BPM/FileNet/lib/log4j-1.2.17.jar
6. Restart your Business Automation Workflow environment for
the configuration to take effect.
7 Check your Content Platform Engine serverconfiguration to ensure you have at least the following parameters added in your JVM: Containers: If your Content Platform Engine server is running in a container, use thefollowing operation to find thejvm.options:install\_root /wlp/usr/servers/your-server-name/

- Dcom.filenet.AppServerType=liberty
- Dcom.filenet.authentication.token.userid=sso:ltpa
- DFileNet.WSI.custom.credential.class=com.filenet.apiimpl.wsi.WSICredential

```
install\_root/wlp/usr/servers/your-server-name/
```

8 Update the ECM system to support SSL. The default installation of Business Automation Workflow uses SSL. The default installation of Content Platform Engine uses TCP-IP without SSL. Update the Content Platform Engine system to support SSL by completing thefollowing substeps:

1. In the WebSphere administrative console on the Content Platform Engine system, select Security
> Global Security. The Global Security page opens.
2. Expand the RMI/IIOP security section. A list of inbound and
outbound links is displayed.
3. Click each inbound and outbound link, and then in the Transport
drop-down list, select either SSL-required or
SSL-supported.

For the SSL configuration steps for the CPE on
container, see step
3 in Configuring Business Automation Workflow with an external Content Platform Engine container.
9 On both the Business Automation Workflow and the Content Platform Engine systems, configure SSL to exchange SSLcertificates in both directions between the servers by completing the following substeps:

1. In the WebSphere administrative console, select Security > SSL certificate and key management. The SSL certificate and key management page opens.
2. Select the Key stores and certificates link. The Key stores and
certificates page opens.
3. Select NodeDefaultTrustStore (for Base Server) or
CellDefaultTrustStore (if on a Network Deployment cell).
4. Either extract the certificate to a file and copy it to the other system to add, or use the
Retrieve from port button to connect and retrieve the certificate. For
details on retrieving from the port, see Configuring cross-cell security for IBM Workflow Center.
10. Update the JVM configuration on the Business Automation Workflow cluster. Log in to the Business Automation Workflow
WebSphere Application
Server administrative console and go to
Servers > Clusters. Select the
cluster that is used for applications, such as BAW.AppCluster. Click
Additional Properties > Cluster
members and then go to Java and Process
Management > Process definition > Java Virtual
Machine > Configuration. Add the following
parameters in the Generic JVM arguments
field:-Dcom.filenet.authentication.wsi.AutoDetectAuthToken=true
-DFileNet.WSI.AutoDetectLTPAToken=false
-DFileNet.WSI.custom.credential.class=com.filenet.apiimpl.wsi.WSICredential
-Dcom.filenet.AppServerType=websphere
Save
your configuration.