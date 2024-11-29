# manageprofiles command-line utility

The profile defines the runtime environment and includes
all of the files that the server processes can change during runtime.

The manageprofiles command-line
utility and its graphical user interface, the Profile Management Tool,
offer alternate ways to create, augment, and delete profiles. For
more information, see BPMConfig command-line utility.

The
command file is located in the install\_root/bin directory,
where install\_root is the installation location
of IBM Business Process Manager. The command file is a script named manageprofiles.sh for Linux® and UNIX platforms or manageprofiles.bat for Windows platforms.

- install\_root/logs/manageprofiles
- install\_root\logs\manageprofiles

- profile\_name\_create.log
- profile\_name\_augment.log
- profile\_name\_delete.log

If you have decided that your solution requires a network deployment configuration,
your runtime environment requires one or more managed nodes. A managed-node profile contains an
empty node that you must federate into a deployment manager cell to make operational. Federating the
managed-node profile changes it into a managed node. Do not federate a node unless the deployment
manager you are federating to is at a release level the same or higher than that of the managed-node
profile you are creating.

## Syntax

- Creating a profile (-create parameter).
- Augmenting a profile (-augment parameter).Note: Using
profiles that have been unaugmented (-unaugment parameter)
is not supported.
- Deleting a profile (-delete parameter).Follow
the instructions in Removing a managed node profile from a deployment environment.
- Deleting all profiles (-deleteAll parameter)
- Listing all profiles (-listProfiles parameter)
- Getting the name of an existing profile from its name (-getName parameter)
- Getting the name of an existing profile from its path (-getPath parameter)
- Validating a profile registry (-validateRegistry parameter)
- Validating and updating a profile registry (-validateAndUpdateRegistry parameter)
- Getting the default profile name (-getDefaultName parameter)
- Setting the default profile name (-setDefaultName parameter)
- Backing up a profile (-backupProfile parameter)
- Restoring a profile (-restoreProfile parameter)
- Using a response file containing the information required to run
a manageprofiles command-line utility (-response parameter)

For
detailed help including the required parameters for each of the tasks
accomplished with the manageprofiles command-line
utility, use the -help parameter. The following
is an example of using the help parameter with the manageprofiles command-line
utility -augment parameter on Windows operating systems: manageprofiles.bat
-augment -help. The output specifies which parameters are
required and which are optional.

## Parameters

Depending on
the operation that you want to perform with the manageprofiles command-line
utility, you might need to provide one or more of the parameters described
in manageprofiles parameters. The Profile Management
Tool validates that the required parameters are provided and the values
entered for those parameters are valid. Be sure to type the name of
the parameters with the correct case, because the command line does
not validate the case of the parameter name. Incorrect results can
occur when the parameter case is not typed correctly.

```
manageprofiles -create -help -templatePath template\_path
```

```
-profileName=<bpm.de.node.1.profileName=<bpm.de.node.1.name>Profile
-profilePath=<bpm.de.node.1.profilePath=<bpm.de.node.1.installPath>/profiles/<bpm.de.node.1.profileName>>
-cellName=<bpm.cell.name=PSCell1>
-nodeName=<bpm.de.node.1.name=Node1>
-serverName=server1
-hostName=<bpm.de.node.1.hostname>
-adminAliasName=<bpm.cell.roleMapping.1.alias=CellAdminAlias>
-adminUserName=<bpm.cell.authenticationAlias.1.user>
-adminPassword=<bpm.cell.authenticationAlias.1.password>
```

```
-profileName=<bpm.dmgr.profileName=<bpm.dmgr.name>Profile
-profilePath=<bpm.dmgr.profilePath=<bpm.dmgr.installPath>/profiles/<bpm.dmgr.profileName>>
-cellName=<bpm.cell.name=PSCell1>
-nodeName=<bpm.dmgr.name=Dmgr>
-hostName=<bpm.dmgr.hostname>
-adminAliasName=<bpm.cell.roleMapping.1.alias=CellAdminAlias>
-adminUserName=<bpm.cell.authenticationAlias.1.user>
-adminPassword=<bpm.cell.authenticationAlias.1.password>
```

```
-profileName=<bpm.de.node.1.profileName=<bpm.de.node.1.name>Profile
-profilePath=<bpm.de.node.1.profilePath=<bpm.de.node.1.installPath>/profiles/<bpm.de.node.1.profileName>>
# must not use the cell name from the config model here, or else node federation will fail - append the node name to ensure uniqueness
-cellName=<bpm.cell.name=PSCell1<bpm.de.node1.name>>
-nodeName=<bpm.de.node.1.name=Node1>
-hostName=<bpm.de.node.1.hostname>
```

## Command output

- INSTCONFSUCCESS: Profile creation succeeded.
- INSTCONFFAILED: Profile creation failed.
- INSTCONFPARTIALSUCCESS: Some non-critical post installation
configuration actions did not succeed.

- manageprofiles parameters

Use the following parameters with the manageprofiles command-line utility for IBM Business Automation Workflow.