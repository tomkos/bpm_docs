# Preparing Business Automation Workflow for an external
Content Platform Engine

## Before you begin

The maintainDocumentStoreAuthorization and
updateDocumentStoreApplication commands are run by using the AdminTask object of
the wsadmin scripting client. To run the commands, the following conditions must be met:

- maintainDocumentStoreAuthorization command:
    - The command must be run on the deployment manager node.
    - One or more application cluster members must be running.
    - Run the command in connected mode. Do not specify the wsadmin -conntype none
option.
    - You must connect to the deployment manager with a user ID that has WebSphere® Application
Server operator privileges.
- updateDocumentStoreApplication command:

- The command must be run on the deployment manager node.
- Run the command in either local or connected mode.
- When you are running the command in connected mode, you must specify a user ID that has WebSphere Application
Server operator and deployer privileges.

For the maintainDocumentStoreAuthorization command, start the wsadmin
scripting client from the profile\_root/bin directory of the
deployment manager profile. For the updateDocumentStoreApplication command, start
the wsadmin scripting client from the
deployment\_manager\_profile/bin directory on either IBM
Workflow Server or Workflow Center. The commands do not write to a log file, but
the wsadmin scripting client always writes a
profile\_root/logs/wsadmin.traceout log file where you find
exception stack traces and other information.

## About this task

All users and groups that are referenced by the Business Automation Workflow document store must be defined in the shared
user registry to work with the external Content Platform Engine. On the Business Automation Workflow server, you must update the
authentication to use only users and groups from the shared user repository. The
EmbeddedECMTechnicalUser authentication alias, which is used by Business Automation Workflow to access ECM with administrator privileges,
must refer to a user from the shared user repository.

## Procedure

1 Check that the user defined in the Authentication Alias assigned to theEmbeddedECMTechnicalUser role is a user from the shared repository. SelectServers > Deployment Environments >myDEname > Authentication aliases . Note the alias namethat is used for the EmbeddedECMTechnicalUser role. Select Security > Global Security . Expand the Java Authentication and Authorization Service section and selectJ2C authentication data . Verify that the user who is assigned to theEmbeddedECMTechnicalUser alias is a user from the shared user repository. Select Users and Groups > Administrative user roles . Verify that the user assigned to the EmbeddedECMTechnicalUser has the Administratorrole. Then, do the following steps.

Select Security > Global Security. Expand the Java Authentication and Authorization Service section and select
J2C authentication data. Verify that the user who is assigned to the
EmbeddedECMTechnicalUser alias is a user from the shared user repository. Select Users and Groups > Administrative user roles. Verify that the user assigned to the EmbeddedECMTechnicalUser has the Administrator
role.

Then, do the following steps.

    1 Create an authentication alias with credentials from the shared user repository for theContent Platform Engine administrator.
        1. In the WebSphere administrative console for the Business Automation Workflow server, select Security > Global Security. The Global Security page opens.
        2. Expand the Java Authentication and Authorization Service section and
select J2C authentication data. The JAAS - J2C Authentication Data page opens.
        3. Clear Prefix new alias names with the node name of the cell as this alias
must match an alias on the external ECM server.
        4. Click New and add an authentication alias with LDAP credentials for the
Content Platform Engine administrator.
2. Grant the user (defined by the alias you created in the previous step) the WebSphere Application
Server administrator role. This role is necessary for
the technical user who is described in subsequent steps. Since you are granting the user the
WebSphere Application
Server administrator role, you must use the
CellAdmin user ID and password. Select Users and Groups > Administrative user roles. Select the Add button and assign the Administrator role to
the user.
3. Restart WebSphere Application
Server.
4. Use the maintainDocumentStoreAuthorization wsadmin command to grant
administrative access in the BPM document store to the
Content Platform Engine administrator. To do this, run
AdminTask.maintainDocumentStoreAuthorization(['-deName', 'myDEname', '-add', 'user\_ID' |
'group\_ID']). 
For example:
AdminTask.maintainDocumentStoreAuthorization(['-deName', 'BPM', '-add', 'cn=P8Admin,ou=FederatedPortal,o=ibm,C=CN'])See
maintainDocumentStoreAuthorization command.
You must keep the users and groups assigned to the Java EE and the technical user roles updated.
To update the users and groups in the technical user role, always use the
AdminTask.maintainDocumentStoreAuthorization command. Do not use the IBM
Administration Console for Content Platform Engine.
Do not switch the EmbeddedECMTechnicalUser role alias before you successfully grant
administrative access to the new user. Run the
AdminTask.maintainDocumentStoreAuthorization command with the list option to see
which users are currently granted access. To do this, run
AdminTask.maintainDocumentStoreAuthorization(['-deName', 'myDEname',
'-list']).
5 Change the EmbeddedECMTechnicalUser role to use the newauthentication alias that you created. This authentication alias is for the Content Platform Engine administrator.
    1. To change the EmbeddedECMTechnicalUser role to use the new
authentication alias, in the WebSphere administrative console, select Servers > Deployment Environments. Select your deployment environment and continue to Authentication
Aliases. You see the EmbeddedECMTechnicalUser and can
modify the alias.
    2. Run the AdminTask.updateDocumentStoreApplication command. See Administering the technical user for the BPM document store.
    3. Run the AdminConfig.save() wsadmin command after the
AdminTask.updateDocumentStoreApplication command to persist these changes.
6. Run the AdminTask.maintainDocumentStoreAuthorization command with the list
option to see which users are currently granted access. To do this, run
AdminTask.maintainDocumentStoreAuthorization(['-deName', 'myDEname', '-list']).
Users or groups from the file repository need to be removed.
7. Run the AdminTask.maintainDocumentStoreAuthorization command with the remove
option to remove any users or groups from the file repository. To do this, run 
AdminTask.maintainDocumentStoreAuthorization(['-deName', 'myDEname', '-remove', 'user\_ID' |
'group\_ID']). 
For example:
AdminTask.maintainDocumentStoreAuthorization(['-deName', 'BPM', '-remove', 'uid=bpmadmin1,o=defaultWIMFileBasedRealm'])See
maintainDocumentStoreAuthorization command.
2. Use the maintainDocumentStoreAuthorization wsadmin command to revoke
access for any users that are not listed in the shared user registry. 
Do not remove administrative users before you verify that at least one user from the shared user
repository has administrative access. Run the
AdminTask.maintainDocumentStoreAuthorization command with the list option to see
which users are currently granted access. To do this, run
AdminTask.maintainDocumentStoreAuthorization(['-deName', 'myDEname', '-list']).
3 To validate the authentication and authorization updates, make sure that the LDAP user(for example, P8Admin) can do the following tasks:

1. Log in to the IBM Business Automation
Workflow
administration client for case management:  
http://virtual\_server\_name:port/navigator?desktop=bawadmin
2. Import a solution.
3. Delete a solution.
4. Log in to Case Builder and create a
solution.
5. Go to the IBM Business Automation
Workflow
desktop: http://virtual\_server\_name:port/navigator?desktop=bawand
run the solution.
4 Log in to the IBM Business AutomationWorkflow administrationclient for case management.

1. Make sure that the LDAP user (for example, P8Admin) has read and write permissions on
the DOS and TOS object stores in ACCE.
2. In the properties tab of the BPM domain in ACCE, change the system user and password
to the LDAP user and password.
3. Make sure that the LDAP user has read and write permissions in the "workflow system"
of TOS in ACCE.