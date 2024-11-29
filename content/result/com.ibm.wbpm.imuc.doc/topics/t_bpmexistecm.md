# Configuring IBM Business Automation Workflow with an existing
external Content Platform Engine

You can configure IBM® Business Automation Workflow to work with an
existing external Content Platform Engine, also called an external Enterprise Content Management (ECM) system.

## Before you begin

- You can configure your Business Automation Workflow deployment environment to
use an empty object store in an external IBM
FileNet® Content Manager installation.
This configuration is useful if you set up a new Business Automation Workflow deployment environment.
You cannot configure your Business Automation Workflow deployment environment to
use an empty object store in an external IBM Content Manager installation immediately. Follow the
instructions in this set of steps.
- You can configure your Business Automation Workflow deployment environment to
reassign the BPM content store to the domain of an existing FileNet Content
Manager installation.
This configuration is useful if you already have a Business Automation Workflow deployment environment
set up. For instructions, see Reassigning the BPM document store.
- When you configure separate IBM Business Automation
Workflow environments with an
existing Content Platform Engine, it is
possible to configure separate IBM Business Automation
Workflow configurations with a
single FileNet P8 domain. The requirement is for all of the separate IBM Business Automation
Workflow configurations to be
on the same product version. For example, all IBM Business Automation
Workflow configurations are 24.0.0.0 or V21.0.2. Each
separate environment has its own set of unique object stores. Sharing of object stores across the
different IBM Business Automation
Workflow
configurations is not allowed. Configuring two separate FileNet P8 domains on the same WebSphere® Application
Server installation such that
each FileNet P8 domain,
services a different version of Business Automation Workflow is also not
supported.
- To use the same single FileNet P8 domain, all IBM Business Automation
Workflow configurations must
not only be on the same product version, but they must all have either development profiles
(Workflow Center) or production profiles (Workflow Server) but not a mix of both. Note: If all of
the IBM Business Automation
Workflow
configurations are not on the same product version, the gateway service installation might fail as
there are dependencies from the Gateway services.
- You cannot use the same Design and target object stores (DOS & TOS) for both Workflow Center
(development) and Workflow Server (production). You have to create new ones specifically for the
production profile. Also, when using a FileNet P8 domain for multiple IBM Business Automation
Workflow deployment
environments, ensure that they all have either development profiles (Workflow Center) or production
profiles (Workflow Server), but not a mix of both.

These prerequisites are necessary to configure IBM Business Automation Workflow with an existing external Content Platform Engine.

- Only standard and cluster ECM environments are supported. Single server or multiple server
(noncluster) network deployment ECM environments are not supported.
- The existing external Content Platform Engine must be configured
on a profile that is enabled for Java 8. Otherwise, the Case configuration tool fails.
- On Content Platform Engine, you must
have a domain that is already set up. There might be multiple object-stores that are already set up.
When you configure the Content Platform Engine, you will find a
three-to-three correlation between the IBM Business Automation Workflow server and the
FileNet Content
Manager object
store. The three object stores are IBM Business Automation Workflow document store (which
must be a new, empty object store), design object store, and target object store.
- As an application server, only WebSphere Application
Server is
supported. In addition, if you are using a version earlier than V18.0.0.2, the WebSphere Application
Server used by IBM Business Automation Workflow and the WebSphere Application
Server used by the FileNet Content
Manager must have the same version.
- The same Lightweight Directory Access Protocol (LDAP) user repository must be used by both
IBM Business Automation Workflow and FileNet Content
Manager.
- The same configuration properties for the Lightweight Directory Access Protocol (LDAP) must beused by both IBM Business Automation Workflow and FileNet ContentManager .For example, the user and group name attributes: For more information, see managing\_users\_extsecprov.html and https://www.ibm.com/docs/filenet-p8-platform/5.5.x?topic=security-directory-service-providers .
    - Business Automation Workflow - user-full-name-prop and group-name-prop
    - Content Platform Engine - userShortNameAttribute and GroupNameAttribute
- When you create the WebSphere Application
Server profile for the external
Content Platform Engine, you must use a
hostname with a domain name suffix, for example
MyDmgrHost.my\_domain.com.
- Business Automation Workflow and Content Platform Engine must have the same
registry for achieving single-sign on (SSO). For example, Business Automation Workflow and Content Platform Engine both might have federated
repositories such as the Virtual Member Manager (VMM) repositories. A combination of Business Automation Workflow with VMM and Content Platform Engine with a stand-alone LDAP
is not supported by IBM WebSphere Application
Server. If you use shared LDAP
repositories, they must be added to the WebSphere federated repositories on both the Content Platform Engine and IBM Business Automation
Workflow.

## About this task

Back up your system configuration and databases before you begin this configuration. This backup
means you can roll back your configuration if needed. See Backing up and restoring administrative configuration files.

## Procedure

1 Begin your configuration by checking that there is no content such as folders and documents inthe IBM Business Automation Workflow objectstore. Use the IBM Administration Console forContent Platform Engine to check that there is no content. See Using the IBM Administration Console for Content Platform Engine Note: Any content that you do not remove from the BPM content store is deleted when youcomplete this configuration.
    1. In the domain navigation tree, open Object Stores > docs.
    2. In the object store navigation tree, open Search.
    3. Click New Object Store Search.
    4. For each of the following classes, run a search: Document.
    5. If the result set is empty, there is no existing content.
2. Check the version level of the FileNet Content
Manager. It must be a supported version to work with IBM Business Automation Workflow. The external Content Platform Engine version must be the same or later than the Content Platform Engine version embedded in IBM Business Automation Workflow. In 19.0.0.2, that version is 5.5.2, so the
external Content Platform Engine version must be 5.5.2 or later. New
features available in IBM Business Automation Workflow releases after
19.0.0.2 might not work with earlier versions of Content Platform Engine.
3. Configure single sign-on (SSO) security for the external FileNet Content
Manager, including the configuration of the
user registry and trusted realm. Follow the instructions in Configuring single sign-on with LPTA for an external Content Platform Engine or
Configuring single sign-on with UMS for an external Content Platform Engine.
4. Stop the IBM Business Automation
Workflow deployment
environment.
5. Start the IBM Business Automation
Workflow deployment manager to
have the changes take effect.
6 Set up a network shared directory between all computers in the IBM Business Automation Workflow cluster and theContent Platform Engine cluster. The shared directory must be the same on all computers. The computers must have the sameoperating system.

- By default, the shared directory on the IBM Business AutomationWorkflow computer isinstall\_root /CaseManagement/properties . If you customizedthe path to the shared directory, use that customized path.

<!-- image -->

<!-- image -->

    - On the Content Platform Engine
computer, create a folder with the same path as the IBM Business Automation
Workflow shared directory.
    - You can mount remote file systems. You can also use network file systems or distributed file
systems to share files across computers, such as NFS, GPFS.
- By default, the shared path on the IBM Business AutomationWorkflow computer isinstall\_root \CaseManagement\properties . If you customizedthe path to the shared directory, use that customized path. If the path is a UNC path to share filesamong Windows servers, use a forward slash, for example //WIN129146/shareFolder instead of \\WIN129146/shareFolder .

<!-- image -->

1. On the Content Platform Engine
computer, create a folder with the same path as the IBM Business Automation
Workflow shared directory.
2. Share the directories between the computers.
7 Designate a user from the shared repository to be the administrator for the object store.Business Automation Workflow uses this user to do administrativeoperations like the creation of document class definitions. Then, map this user to the IBM Business Automation Workflow EmbeddedECMTechnicalUser role.

1 Check that the user defined in the Authentication Alias that is assigned to theEmbeddedECMTechnicalUser role is a user from the shared repository.
    1. Select Servers > Deployment Environments > DE name > Authentication aliases. Note the alias name that is used for the EmbeddedECMTechnicalUser role.
    2. Select Security > Global Security. Expand the Java Authentication and Authorization Service
section and select J2C authentication data. Verify that the user who is
assigned to the EmbeddedECMTechnicalUser alias is a user from the shared user repository.
2 If the user assigned to the EmbeddedECMTechnicalUser does not qualify, that is, the user is notfrom the shared repository, do the following steps.

1 Create an authentication alias with credentials from the shared user repository for the ContentPlatform Engine administrator.
    1. In the WebSphere administrative console for the IBM Business Automation Workflow server, select Security > Global Security. The Global Security page opens.
    2. Expand the Java Authentication and Authorization Service section and
select J2C authentication data. The JAAS - J2C Authentication
Data page opens.
    3. Click New and add an authentication alias with LDAP credentials for the
object store administrator.
2. Change the EmbeddedECMTechnicalUser role to use the new authentication alias that you created.
This authentication alias is for FileNet Content
Manager. To change the EmbeddedECMTechnicalUser role to use the new authentication alias, in the
WebSphere administrative console, select Servers > Deployment Environments. Select your deployment environment and continue to Authentication
Aliases. You see the EmbeddedECMTechnicalUser and can modify that alias.
8 Grant administrator roles to the user that you chose for the EmbeddedECMTechnicalUserrole.

1. Go to Users and Groups > Administrative user roles and click Add.
2. Select Administrator, Deployer, Operator roles in the Roles list and click
Search.
3. In the Available user list, select the EmbeddedECMTechnicalUser role-mapped
user and add it to the Mapped to role list. Click OK to apply all
changes.
4. Log in to the Process Admin Console. In the Group Management window, search for the tw\_admins and tw\_authors
groups, and add the EmbeddedECMTechnicalUser role-mapped user to both groups.
9. Restart the IBM Business Automation
Workflow deployment
manager.
10. Synchronize the custom profiles with the deployment manager profile.
For each custom profile, run the following command on the custom
node:custom\_profile\_install\_root/bin/syncNode.bat dmgr\_hostname dmgr\_soap\_port -user de\_admin\_user -password de\_admin\_password
11 Configure the FileNet Content Platform Engine .

1. Log in to the IBM Administration Console for
Content Platform Engine on the FileNet
Content Platform Engine as a domain administrator.
2 If you are creating a new Content Platform Engine environment, create thethree object stores for the IBM Business Automation Workflow document store, designobject store, and target object store. For considerations on object store configuration, see Planning for an external Content Platform Engine . If you are augmenting IBM CaseManager , you already havethe design object store and target object store and need to create only the IBM Business Automation Workflow document store. Usethe IBM Administration Console forContent Platform Engine on theFileNet Content Platform Engine asdescribed in Creating an object store .Use the following settings: After the object stores are created, you can add a user with administrative permissions on theobject store. See Update object store withnew users and groups . The permissionsthat you must grant to the user are listed in Permissions required for the new object store .
    - Use the user from step 7 when you grant
administrative access to this object store. You can also use a group that contains this user.Important: If you don't complete this step, you might see errors in the
SystemOut.log file because the ECM Technical User isn't considered a member of
the Object Store Administrators.
    - Grant all users that work with IBM Business Automation Workflow basic access. You
might want to use the #AUTHENTICATED-USERS security identifier as grantee to allow all users to work
with the object store. The individual instance objects are automatically protected based on the
teams that you create in IBM Business Automation Workflow.
    - When you choose the add-ons, check that the following extensions are installed. The add-ons arepart of the default configuration.
        - For IBM Business Automation Workflow document store:
            - Base Content Engine Extensions
    - For IBM Business Automation Workflow design object store and target object store:
        - Select Default Application Configuration to automatically select a list
of add-nos.
- After the object stores are created, the only access rights that you will need to add to the
administrative user is PRIVILEGED\_WRITE. In IBM Administration Console for
Content Platform Engine on FileNet Content
Manager, the checkbox
that you must select is Modify certain system properties (in English).
- After the target object store is created, you must create a new "Workflow System" for it.
Open the target document store, go to Administrative > Workflow System, click New, and enter the values for your environment. Make a
note of the connection point name because you need it in a later step when you run the case
configuration tasks in the Case configuration tool. You can ignore the
Broker servlet URL and Public listener URL in the
Process Orchestration section.
12. Containers:  To use an external Content Platform Engine running in a container, follow the instructions in
Configuring IBM Business Automation
Workflow
with an external Content Platform Engine container. Then,
return to the next step.
13 Running a command and then starting IBM Business Automation Workflow finishes theconfiguration. However, you must also verify that the configuration is working. You configured the external Content Platform Engine . To configure casemanagement, do the remaining steps.

1 Run the setBPMExternalECM admin command to configure IBM Business Automation Workflow to use an externalContent Platform Engine .
    1. Ensure the IBM Business Automation
Workflow
deployment manager and the Content Platform Engine are running.
    2. Run wsadmin with the parameter -conntype SOAP from the
dmgr\_profile\_root/bin directory.
    3 Run the setBPMExternalECM admin command and save your changes. UseNEW\_EXTERNAL\_OBJECT\_STORE as the value for the-ecmEnvironment parameter. For example:Important: This commandresults in execution times that exceed the default timeout setting for wsadmin command execution. Tochange the default to allow for the execution time required, open theprofile\_root /properties/soap.client.props file and changethe value for com.ibm.SOAP.requestTimeout to 0 , which means notimeout. Remember to restore the previous value after you run the command. This command takes along time to run. Do not close the command window. Notes: See setBPMExternalECM command .

This command takes a
long time to run. Do not close the command window.

        - Noncontainer version
example:wsadmin -conntype SOAP -port 8879 -host myHostName.mycompany.com -user admin\_user -password admin\_password -lang jython
wsadmin>print AdminTask.setBPMExternalECM(['-clientDownloadServicePort', '9081', '-de', 'De1', '-ceUrl', 'iiop://CE.mycompany.com:2809/FileNet/Engine', '-ecmEnvironment', 'NEW\_EXTERNAL\_OBJECT\_STORE', '-domainName', 'p8domain', '-objectStoreName', 'bpmdocs', '-designObjectStoreName', 'bpmdos'])
wsadmin>AdminConfig.save()
        - Containers: wsadmin -conntype SOAP -port 8879 -host myHostName.mycompany.com -user admin\_user -password admin\_password -lang jython
wsadmin>print AdminTask.setBPMExternalECM(['-clientDownloadServicePort', '9081', '-de', 'De1', '-ceUrl', 'iiop://CE.mycompany.com:2809/FileNet/Engine', '-ecmEnvironment', 'NEW\_EXTERNAL\_OBJECT\_STORE', '-domainName', 'p8domain', '-objectStoreName', 'bpmdocs', '-designObjectStoreName', 'bpmdos'])
wsadmin>AdminConfig.save()
        - The host and port parameters correspond to the deployment manager server host value and its SOAP
port value.
        - The -objectStoreName and -designObjectStoreName
parameters are case-sensitive.
        - If you see a message that updated .jar files exist on this deployment manager node machine, you
must manually copy the updated files to the other custom node machines.
4. If you started the deployment manager and node agents, manually restart them.
5. Synchronize the configuration of the nodes.
6. Restart the IBM Business Automation Workflow deployment environment by using the BPMConfig command. BPMConfig
-start. See BPMConfig command-line utility.
2. Check for errors in the IBM Business Automation Workflow logs. If you discover
errors, resolve them and restart the IBM Business Automation Workflow server.
3. Check the CMIS component in the Component Health Center (Servers > Deployment Environments > de\_name > Health Center) to verify that your external Content Platform Engine is up and running. The
switch to the external Content Platform Engine removes the BPM content store configuration.
Therefore, you cannot check the EmbeddedECM component anymore. Instead, check the CMIS component.
The CMIS component also reports errors for the connection to the external Content Platform Engine. 
Note: Health Center is unable to check PostgreSQL.
14. Optional: 
If you are planning to use an external IBM Content
Navigator and it is
not yet configured, follow the instructions in Configuring IBM Business Automation Workflow with an external IBM Content Navigator to configure it. Then,
return and complete the remaining steps to configure case management.
15 To import the external Content Platform Engine's signer and CA certificates to the Caseconfiguration tool, follow the two steps:

1 Import the external Content Platform Engine SSL certificate into theIBM Business AutomationWorkflow Case configuration tool .
    1. On the IBM Business Automation
Workflow
computer, access
https://cpe\_host\_name:ssl\_port/wsi/FNCEWS40MTOM
to obtain the external Content Platform Engine SSL certificate from the
server. See Adding trusted certificates in Liberty.
    2. Import the certificate into the IBM Business Automation
Workflow JVM by using the keytool
command. For example: /opt/IBM/baw/java/jre/bin/keytool -import -keystore
/opt/IBM/baw/java/jre/lib/security/cacerts -storepass changeit -file
/u/CPE/certificate.crt
2. Import the Content Platform Engine signer, see IBM Business Automation Workflow Case configuration tool  returns an SSLHandshakeException error.
16. Start the IBM Business Automation
Workflow
Case configuration tool by running
configmgr.exe in the directory
workflow-home/CaseManagement/configure.
 If the tool is run on Windows, it should be run with administrative privileges.Tip: If security is not a concern, enable saving passwords in the file system by clicking Windows > Preferences and selecting the Save all passwords checkbox.
17. Open the profile configuration file with the extension.cfgp that was
created when you configured your deployment environment. 
This profile file, which contains the default settings, is located in either
dmgr-profile-root/CaseManagement/de
name/profiles/ICM\_dev or
dmgr-profile-root/CaseManagement/de
name/profiles/ICM\_prod.
18 Edit the setting for the remote Content Platform Engine server connection properties.

1. Click File > Edit Profile Properties.
2. In the first panel, click Test Connection to verify that the default
values are correct and then click Next.
3. In the second panel, click Test Connection to verify that the default
values are correct and then click Next.
4. In the third panel, replace the default settings for the embedded Content Platform Engine server with the settings for the external
Content Platform Engine and then click Test
Connection.
5. Click Finish.
19. Copy the ejb-lookup.jar
file from the IBM Business Automation
Workflow
directory install\_root/CaseManagement/configure/deploy (for
example:  /opt/IBM/WebSphere/AppServer/CaseManagement/configure/deploy) to the
Content Platform Engine
WebSphere Application
Server directory
install\_root/lib/ext (for example: 
/opt/IBM/WebSphere/AppServer/lib/ext).
20. Restart the external Content Platform Engine to cause the
configuration changes to take effect.
21 Run the enabled configuration tasks in the order in which they are listed in the Case configuration tool . For the details of each task, see the topic for your environment.

- Workflow Center: Preparing to run the case configuration tasks
- Workflow Server: Preparing to run the configuration tasks
22. Restart the IBM Business Automation
Workflow environment.
23 For verification, see the topic for your environment.

- Workflow Center: Verifying the case applications in the development environment
- Workflow Server: Verifying the IBM Business Automation Workflow applications in the production environment
24. Optional: You can optionally configure the Content Services toolkit. For more
details, see Optional: Configuring the Content Services toolkit.

- Configuring single sign-on with LTPA for an external Content Platform Engine

To allow access to case information on an external ECM system for an IBM Business Automation Workflow user, you must configure cross-cell single sign-on (SSO) access control. Unless you are using User Management Service (UMS), use Lightweight Third-Party Authentication (LTPA). This configuration is for the Business Automation Workflow cell and the external Content Platform Engine cell. The configuration includes the configuration of the user registry and trusted realm.
- Configuring single sign-on with UMS for an external Content Platform Engine

To allow access to case information on an external ECM system for an IBM Business Automation Workflow user, you must configure cross-cell single sign-on (SSO) access control. If you are using User Management Service (UMS), or you need to configure your users through OpenID connect Relying Party (OIDC RP) system, use UMS SSO. Otherwise, use LTPA SSO. This configuration is for the Business Automation Workflow cell and the external Content Platform Engine cell. The configuration includes the configuration of the user registry and trusted realm.
- Configuring single sign-on with LTPA for an IBM Content Navigator or Content Platform Engine container

Learn how to configure LTPA single sign-on (SSO) for an IBM Content Navigator or Content Platform Engine container.
- Configuring IBM Business Automation Workflow with a Content Platform Engine container

 Containers: 
If you are running Content Platform Engine in a container, you can configure IBM Business Automation Workflow to work with your containerized version.
- Permissions required for the new object store

When you create a new external object store, permissions are required for IBM FileNet Content Manager users to work with  IBM Business Automation Workflow.
- Reassigning the BPM document store

You can configure IBM Business Automation Workflow to work with an existing external Content Platform Engine by reassigning the BPM document store.

## Related information

- setBPMExternalECM command
- BPMConfig command-line utility
- correctDocumentStoreInstanceAuthorization command