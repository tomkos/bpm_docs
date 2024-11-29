# Configuring IBM Business Automation Workflow without a
file-based user registry

## About this task

The default setup for IBM® Business Automation Workflow uses a
file-based user repository for some special users such as the deAdmin user and
cellAdmin users that are configured as
bpm.cell.authenticationAlias and bpm.de.authenticationAlias. By
having these users stored in a file-based registry, it ensures that admin users can still log into
the system even if the LDAP server is unavailable. However, if your security policy does not allow
user accounts to be stored in a file-based user repository, the default setup is not suitable for
your requirements.

## Procedure

To configure IBM Business Automation Workflow without
using a file-based user registry, so that it only uses your LDAP registry, perform the following
actions:

1 Install IBM Business Automation Workflow as described in thefollowing topics:
    1. Installing Business Automation Workflow on Linux
    2. Granting write permission of files and directories to nonroot users for network deployment profile creation or augmentation on AIX or Linux
2. Create a dmgr profile by running one of the following commands:

installation\_root/bin/ProfileManagement/pmt.sh
installation\_root/bin/ProfileManagement/pmt.bat
 Make sure that you select IBM Business Automation Workflow > IBM Business Automation Workflow deployment manager. You can use any user ID and password for the primary admin user and any profile
name, for example, dmgr01.
3. Start the deployment manager by using the command
install\_root/profiles/profile\_name/bin/startManager.sh
| .bat. For example:

c:\ibm\bpm\profiles\dmgr01\bin\startManager.bat
4. Open the WebSphere® Application
Server administrative console, by
using a browser to open the URL
https://dmgrhost:9043/ibm/console.
5. To add your LDAP as a federated repository, perform Configuring the user registry
.
6. Restart the dmgr.
7. Open the WebSphere Application
Server administrative console
again at https://dmgrhost:9043/ibm/console, and log in as
the primary admin user.
8 Grant WebSphere ApplicationServer administrative console adminrole permissions to the LDAP users that will be used for the DEAdmin andCellAdmin roles , remove the file-based user registry from the federated repository,and remove obsolete default users from the file registry:

1 To grant the necessary administrator permissions to LDAP users, click Users and groups > Administrative User roles and grant administrator permissions to the following LDAP users:
    - All human administrators
    - A system account, which must be the WebSphere Application
Server
administrative console primary administrative user ID. This account will later be used in the
CellAdmin role. The following example assumes that the primary admin user ID is
ldapaccount1.
2. To configure the WAS primary administrative user ID, click Security > Global security, in the User account repository section, select
Federated repositories, click Configure, then
configure the WAS primary administrative user ID.
3. To remove the file-based user registry from the federated repository, select
InternalFileRegistry, and click Remove.
4. To change the CellAdminAlias to the user account that is used for
cellAdmin, navigate to Security > Global security, then in the Authentication section, expand the
Java Authentication and Authorization Service entry, then click
J2C authentication data. Now select CellAdminAlias and
change the user ID to the account for CellAdmin, for example,
ldapaccount1.
5. Ensure the changes are saved and then restart the dmgr.
6. You can now remove file registry users from the list of users that have administrative
permissions. Click Users and groups > Administrative User roles, select the obsolete users and click Remove.
9 Create your Deployment Environment:

1. Edit a suitable sample BPMConfig.properties file, and add the LDAP user ID
and password for the de and cell authentication aliases.
 For
example:#######################################################################################################################################################
# Deployment environment administrator authentication alias. It cannot have the same user name as the authentication alias of the cell administrator. #
#######################################################################################################################################################
bpm.de.authenticationAlias.1.name=DeAdminAlias
bpm.de.authenticationAlias.1.user=ldapaccount2
bpm.de.authenticationAlias.1.password=passw0rd
...
##################################################
# Cell (WAS) administration authentication alias #
##################################################
bpm.cell.authenticationAlias.1.name=CellAdminAlias
bpm.cell.authenticationAlias.1.user=ldapaccount1
bpm.cell.authenticationAlias.1.password=passw0rd
2. To create the deployment environment, run the BPMConfig command on your properties file. For
example:BPMConfig.sh -create -de /opt/PCHomeLDAP/BPM/samples/config/advanced/Advanced-PC-SingleCluster-DB2.properties
3. Start your servers.
10 To verify the configuration:

1. Review SystemOut.log of Dmgr and all appservers and search for messages on
Warning or Error level. Pay special attention to error messages that repeat frequently, which might
indicate that the password is incorrect for the DeAdmin or
CellAdmin user.
2. Log in to Process Portal and perform a process,
for example the hiring sample.