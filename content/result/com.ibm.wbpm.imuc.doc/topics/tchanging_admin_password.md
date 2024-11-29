# Changing IBM Business Automation Workflow passwords

## Before you begin

- The command must be run on the deployment manager node.
- If the deployment manager is stopped, use the wsadmin
-conntype none option to run the command in disconnected
mode.
- If the deployment manager is running, you must connect with a
user ID that has WebSphere Application Server configurator privileges.
Do not use the wsadmin -conntype none option.

Start the wsadmin scripting client from the deployment\_manager\_profile/bin directory.
The updateBPMAliasesAndRunAsRolesPasswords command
does not write to a log file, but the wsadmin scripting client always
writes a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## About this task

When you change the password for a user, user IDs that
are mapped to RunAs user roles also must be updated.

IBM Business Automation Workflow provides
the following applications that contain users that are mapped to the
RunAs roles:

- For Express, Standard, and Advanced deployment environments:
    - IBM\_BPM\_PerformanceDW\_supportDeploymentTarget
    - IBM\_BPM\_Teamworks\_applicationDeploymentTarget
- For Advanced and AdvancedOnly deployment environments:

- BPEContainer\_\_applicationDeploymentTarget
- TaskContainer\_\_applicationDeploymentTarget

where the suffix is either the application cluster or the stand-alone server (such as for the
IBM Integration
Designer Unit Test Environment (UTE)), and
the support cluster or stand-alone server: \_clusterName or
\_nodeName\_serverName.

## Procedure

You can change passwords for any user that is stored in the file registry, including the
CellAdmin security role (as long as the CellAdmin user is still the same primary administrative
account that was specified as the default when Business Automation Workflow was installed). To change passwords, complete
the following steps:

1 Go to the external security provider and change the passwordfor the user at the provider level. The following steps use WebSphere® ApplicationServer as theprovider:
    1. Change the password in the WebSphere Application
Server file registry
by logging into the WebSphere Application
Server admin
console.
    2. Click Users and Groups > Manage Users.
    3. Select the user and enter the new password in the Password field on the
General tab.
    4. Click Apply and then click OK.
    5. Save the changes.
    6. If you changed the password for the CellAdmin or DeAdmin user, verify the new password by
attempting to log into the WebSphere admin console as that user.

The users for the CellAdmin and DeAdmin roles are also stored in authentication aliases, which by
default are named CellAdminAlias and DeAdminAlias. If the BPMConfig command was
used to create the Business Automation Workflow profiles, the
default names of the authentication aliases might have been changed by using the
bpm.cell.authenticationAlias.1.name property. If the
manageprofiles command was used to create the Business Automation Workflow profiles, the default name of the authentication
aliases might have been changed by using the optional -adminAliasName
parameter. 
If you want to change the CellAdminAlias or DeAdminAlias user, ensure that the new user has the
appropriate roles as described in Business Automation Workflow security roles.
To change the password for the CellAdmin or DeAdmin user that is stored in the authentication
alias, complete the following steps:

1. In the WebSphere admin console, select Security > Global Security > Java
Authentication and Authorization Service > J2C Authentication Data >
cell\_admin\_alias or de\_admin\_alias, then change
the password to be the same as the password that you specified for the CellAdmin or DeAdmin user in
the previous step.
2. Verify the new password by starting the deployment manager and then running the following
command:
BPMConfig -validate -profile dmgrProfileName -de deName -outputDir \_validateIf
the password was not set correctly, the BPMConfig  command will fail to connect
to the deployment manager.

If you changed the CellAdmin user password, you generally do not need to complete any
additional steps, such as running the updateBPMAliasesAndRunAsRolesPasswords
command to synchronize the passwords. However, if the factory default settings were changed and the
CellAdmin user is now referenced by Business Automation Workflow
applications, you need to run the updateBPMAliasesAndRunAsRolesPasswords command
by completing the next steps. Similarly, if you changed the password for another user that is used
by Business Automation Workflow authentication aliases or RunAs
roles for Business Automation Workflow applications, you need to run
the updateBPMAliasesAndRunAsRolesPasswords command by completing the following
steps.

1. In an ND environment, stop the deployment manager. In the Integration Designer unit test environment, stop the app server.
2. In the deployment manager profile bin folder (or in the AppServer profile
bin folder for the Integration Designer UTE), run the
updateBPMAliasesAndRunAsRolesPasswords wsadmin command to synchronize passwords
for authentication aliases or application RunAs roles. If you have multiple deployment environments
configured, use the -de flag, and specify the target deployment environment in the
command.

The following example shows the command for a 3-cluster Advanced deployment
environment.dmgr\_profile\_root/bin>wsadmin -conntype NONE -lang jython

wsadmin>AdminTask.updateBPMAliasesAndRunAsRolesPasswords( [ '-userName', 'user\_name', '-password', 'new\_password' ] ) 
Processing: IBM\_BPM\_PerformanceDW\_SupportCluster
Processing: IBM\_BPM\_Teamworks\_AppCluster
Processing: BPEContainer\_AppCluster
Processing: TaskContainer\_AppCluster

wsadmin>AdminConfig.save()
The following example shows the command for a single-cluster Standard deployment
environment.dmgr\_profile\_root/bin>wsadmin -conntype NONE -lang jython

wsadmin>AdminTask.updateBPMAliasesAndRunAsRolesPasswords( [ '-userName', 'user\_name', '-password', 'new\_password' ] ) 
Processing: IBM\_BPM\_PerformanceDW\_SingleCluster
Processing: IBM\_BPM\_Teamworks\_SingleCluster

wsadmin>AdminConfig.save()
Additional information about the command is found in the topic
"updateBPMAliasesAndRunAsRolesPasswords command."
Important: On Linux®, UNIX, or AIX® platforms, run
the updateBPMAliasesAndRunAsRolesPasswords wsadmin command as the current owner
of the BPM installation folder and files.
3. If you are using the embedded Content Platform Engine, be sure to change the
technical user password through the Administrative Console for Content Platform Engine (ACCE). For
more information, see "Changing the technical user" in Administering the technical user for the BPM document store.
4. In an ND environment, start the deployment manager and synchronize your changes on the
other nodes. In the Integration Designer unit test
environment, start the app server.
5. In an ND environment, restart the application cluster members
and support cluster members.

## Related reference

- updateBPMAliasesAndRunAsRolesPasswords command

## Related information

- Starting and stopping the server
- Customizing the Workflow Server settings used to connect to Workflow Center