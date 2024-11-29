# Configuring IBM Business Automation
Workflow with an external
IBM Content
Navigator

You can configure IBM Business Automation
Workflow to work with an external
IBM Content
Navigator.

## Before you begin

These prerequisites are necessary to configure IBM Business Automation
Workflow with an external IBM Content
Navigator.

- IBM Content
Navigator V3.0.5 must be
installed on WebSphere® Application
Server v8.5 or later. See Installing IBM Content Navigator for instructions.
- Install or upgrade to IBM Content
Navigator V3.0.5.
- The IBM Content
Navigator computer must be
in the same domain as the IBM Business Automation
Workflow
computers.
- If there are multiple nodes for Business Automation Workflow, you must configure a web
server to work with Business Automation Workflow. For more information,
see Customizing Business Automation Workflow to work with a web server.Note: It is not recommended
to install Business Automation Workflow and
IBM Content
Navigator
into a single WebSphere Application
Server
cell.
- The same external IBM Content
Navigator installation
cannot be used for both Business Automation Workflow development and
production profiles. There is a 1:1 mapping between the Content Navigator desktops and the
case-related plug-ins. If there are custom widgets installed in the development profiles, and the
same custom widgets are installed in the production profile, the custom widgets might not work
correctly.

## About this task

- You cannot reverse this configuration and return to using the IBM Business Automation
Workflow embedded IBM Content
Navigator. After you configure, you must
always use the external IBM Content
Navigator.
- After you run the setExternalNavigator command, the following capabilitiesare disabled:
    - Process Designer in Case Manager Builder is disabled. To enable the stand-alone Process
Designer, follow the instructions in Configuring IBM Business Automation Workflow to use the stand-alone IBM FileNet Process Designer.
    - The IBM Forms and
eForms are also disabled. The IBM Forms and eForms are supported
only by embedded IBM Content
Navigator
configuration.

Back up your system configuration and databases before you begin this configuration. This
backup means you can roll back your configuration if needed. See Backing up and restoring administrative configuration files.

## Procedure

1 Configure access to a shared user repository, such as a Lightweight Directory Access Protocol(LDAP) directory. Both IBM Business AutomationWorkflow and IBM ContentNavigator must have access to the same set ofusers.
    1. In the administration console on both systems, select Security > Global Security. The Global Security page opens.
    2. In the Available realm definitions, select Federated
Repositories and then click Configure. The Federated
Repositories page opens.
    3. Configure your shared user repository with matching user and group attributes.
    4. In any environment, select Require SSL communications for the user
repositories.
    5. Test your LDAP connection. See Configuring Content Platform Engine application server authentication
(LDAP) settings.
    6. If the realm names of IBM Business Automation
Workflow and IBM Content
Navigator are
different (for example, because you set different active realm definitions), make certain that in
each cell the realm of the other cell is trusted. From the navigation pane, click Security > Global security. Under RMI/IIOP security, click CSIv2 inbound
communications. Click Trusted authentication realms - inbound.
Select Trust realms as indicated below. Click Add external
realm and add the realm of the remote cell. Click Apply.
    7. In the administration console on both systems, select Users and Groups > Manage Users and search for the IBM Business Automation
Workflow user
ID that you are going to define as the IBM Content
Navigator administrative user. Verify that
the user ID is unique and it is in the shared user repository.
2. Configure single sign-on (SSO) security for the external IBM Content
Navigator, including
the configuration of the user registry and trusted realm. Follow the instructions in Configuring single sign-on with LTPA for an external IBM Business Automation Navigator.
3 On both the IBM Business AutomationWorkflow and IBM ContentNavigator systems, configure SSL to exchangeSSL certificates in both directions between the servers.

1. In the administration console, select Security > SSL certificate and key management. The SSL certificate and key management page open.
2. Select the keystores and certificates link. The keystores and
certificates page opens.
3. Select NodeDefaultTrustStore (for Base Server) or
CellDefaultTrustStore (if on a Network Deployment cell).
4. Either extract the certificate to a file and copy it to the other system to add, or use the
Retrieve from port button to connect and retrieve the certificate. For
details on retrieving from the port, see Configuring cross-cell security for IBM Workflow Center .
4 Set up a network shared directory between all computers in the IBM Business Automation Workflow cluster and theIBM ContentNavigator cluster. The shared directory must be the same on all computers. The computers must have the sameoperating system.

- By default, the shared directory on the IBM Business Automation
Workflow computer is
install\_root/CaseManagement/properties. If you customized
the path to the shared directory, use that customized path. You can mount remote file systems. You
can also use network file systems or distributed file systems to share files across computers, such
as NFS, GPFS.
- By default, the shared path on the IBM Business AutomationWorkflow computer isinstall\_root \CaseManagement\properties . If you customizedthe path to the shared directory, use that customized path. If the path is a UNC path to share filesamong Windows servers, use a forward slash, for example //WIN129146/shareFolder instead of \\WIN129146/shareFolder .

<!-- image -->

    1. On the IBM Content
Navigator computer,
create a folder with the same path as the IBM Business Automation
Workflow shared directory.
    2. Share the directories between the computers.
- For more information on how to change the default network shared directory, see Changing the network shared directory.
- Containers: To usean external IBM Business AutomationNavigator runningin a container, complete the following steps:

1. Create a folder on the Business Automation Workflow computer. This folder
must match the mountPath as seen by the container of the Custom plug-ins for
IBM Business Automation
Navigator, for example,
/opt/ibm/plugins. See Creating volumes and folders for deployment on Kubernetes.
2. Mount the folder that you created to the same shared directory for Custom plug-ins for IBM Business Automation
Navigator, following the instructions in
the same topic.
3. Copy all folders and files from the previous network shared directory to the new network shared
directory. By default, the network shared directory on the Business Automation Workflow computer is
install\_root\CaseManagement\properties.
4. Run the BPMConfig command with the -update
option. BPMConfig -update -profile DmgrProfile [-de deName] -networkDirectory new\_directory\_path
5. Restart your Business Automation Workflow
environment.
5. Optional:  Containers: To use an external
IBM Business Automation
Navigator running in a
container, follow the instructions in Configuring IBM Business Automation Workflow with an IBM Business Automation Navigator container . Then, return to the
next step.
6. Stop the deployment environment. On the IBM Business Automation
Workflow computer, run the
setExternalNavigator command to configure IBM Business Automation
Workflow to use the external
IBM Content
Navigator. 
Change the directories to
install\_root/profiles/deployment\_manager\_profile/bin
and run the command. 
For example, wsadmin.bat -connType none -lang jython
AdminTask.setExternalNavigator(['-de', 'ProcessCenter', '-icnURL', 'https://icnhostname:ssl\_port/navigator', '-icnAdminUser', 'P8Admin', '-icnAdminPassword', 'IBMFileNetP8'])
AdminConfig.save()

Note: The hostname and port number icnhostname:ssl\_port applies to either a
standalone IBM Content
Navigator host or a
clustered IBM Content
Navigator
environment.
See setExternalNavigator command.
7. For the Case client to access resources on IBM Business Automation
Workflow server, run the
setBPMproperty command with CSP and configuration settings, which in turn
improves and hardens security. 
Start the wsadmin scripting client from
install\_root/profiles/deployment\_manager\_profile/bin and run the command. 
For example, wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.setBPMProperty(['-de', 'De1', '-name', 'Security.ContentSecurityPolicyHeaderValue', '-value', "default-src 'self' 'unsafe-inline' 'unsafe-eval';worker-src blob:;frame-ancestors 'self' icnhostname:port; img-src 'self' data:; font-src 'self' fonts.gstatic.com data:;"])
 For setBPMproperty to be run on an on-premise IBM Business Automation
Workflow configured to external
CPE/ICN environment where IBM
Process Federation Server is also enabled.
AdminTask.setBPMProperty(['-de', 'De1', '-name', 'Security.ContentSecurityPolicyHeaderValue', '-value', "default-src 'self' 'unsafe-inline' 'unsafe-eval';worker-src blob:;font-src 'self' fonts.gstatic.com data:; connect-src 'self' pfshost:pfsport bawhost:bawport; frame-ancestors 'self' cnhost:icnport pfshost:pfsport bawhost:bawport;img-src 'self' data: blob:; frame-src 'self' pfshost:pfsport bawhost:bawport; script-src-elem 'self' 'unsafe-inline' 'unsafe-eval' pfshost:pfsport bawhost:bawport"])

See setBPMProperty command.
8 Import the IBM ContentNavigator SSLcertificate into the IBM Business AutomationWorkflow Case configuration tool .

1. On the IBM Business Automation
Workflow computer, access
https://icn\_host\_name:ssl\_port/navigator
to obtain the SSL certificate from the IBM Content
Navigator server. See Adding trusted certificates in Liberty.
2. Import the certificate into the IBM Business Automation
Workflow JVM by using the keytool
command.
For example,/opt/IBM/baw/java/jre/bin/keytool -import -keystore
/opt/IBM/baw/java/jre/lib/security/cacerts -storepass changeit -file
/u/ICN/certificate.crt
9. If you are upgrading from IBM Case
Manager, return to Upgrading IBM Case Manager to IBM Business Automation Workflow  and follow the rest of the steps. If you are configuring an
external Content Platform Engine, return
to Configuring IBM Business Automation Workflow with an existing external Content Platform Engine  and follow the rest of the steps. Otherwise, start the
deployment environment.
10 With the deployment environment running, run the Business Automation Workflow Case configuration tool to deploy the caseplug-ins onto the IBM ContentNavigator server. For information about the Case configuration tool, which is located underWorkflow\_install\_root /CaseManagement/configure/ , see thetopic for your environment:

- Workflow Center: Preparing to run the case configuration tasks for the development environment
- Workflow Server: Preparing to run the case configuration tasks for the production environment
11. Restart the deployment environment.

- Configuring single sign-on with LTPA for an external IBM Business Automation Navigator

To allow access to case information on an external ECM system for an IBM Business Automation Workflow user, you must configure cross-cell single sign-on (SSO) access control. Unless you are using User Management Service (UMS), use Lightweight Third-Party Authentication (LTPA). This configuration is for the Business Automation Workflow cell and the external IBM Business Automation Navigator cell. The configuration includes the configuration of the user registry and trusted realm.
- Configuring single sign-on with LTPA for an IBM Content Navigator or Content Platform Engine container

Learn how to configure LTPA single sign-on (SSO) for an IBM Content Navigator or Content Platform Engine container.
- Configuring IBM Business Automation Workflow with an IBM Business Automation Navigator container

 Containers: 
If you are running IBM Business Automation Navigator in a container, you can configure IBM Business Automation Workflow to work with your containerized version.

## Related information

- setExternalNavigator command