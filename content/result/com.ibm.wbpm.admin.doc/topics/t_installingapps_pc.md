# Installing snapshots onto an offline server by using the Process Center console and wsadmin commands

## Before you begin

Export a snapshot. For more information, see Importing and exporting projects.

If you plan to migrate running instances, check that there is a
migration policy for the snapshot. The migration policy defines how to handle orphaned tokens if any
exist. If a migration policy is not listed for the source snapshot, notify the owner of the snapshot
that your are installing to create the migration policy. The snapshot owner can use the Process Center console to generate the migration policy file
and use the migration policy editor to modify it. For information, see Defining the migration policy by using the Process Center console.

## Procedure

1. Log in to the Process Center
console.
2. On the Process apps page, click Details for the
process application you want to install, and then click Snapshots.
3. Click Install next to the snapshot you want to install.
The Install a snapshot to a server window opens.
4. In the window, select the offline Process Server that you want to install the snapshot to.
If the process application already has an installation package for a different snapshot for
the offline Process Server, the window displays an
OK button. For example,
if there is an installation package for Snap1 and you clicked Install for
Snap2, the window displays the OK button. If you are
installing the first snapshot for the process application onto the Process Server, the window displays an Create
Installation Package button. Click the button.
If you clicked the OK button, the window displays the
Install Snapshot - Manage Instances page. If you clicked the Create
Installation Package, the window closes and the process to create the installation
package starts.
5. If the Install Snapshot - Manage Instances window is open, select
the type of installation package that you want to create. You can create a generic
installation package or you can create a custom installation package. A generic installation package
does not include migration instructions used to migrate tokens and instances from other snapshots to
the new snapshot.
6 If you selected to create a custom installation package, set how to handle running instancesfor each snapshot that is currently installed onto the Process Server . Your options are If you choose Leave , existing process instances continue to run usingthe previous snapshot. New process instances use the new snapshot. If you chooseMigrate , existing process instances migrate to the new snapshot. There is thepossibility that orphaned tokens could occur with this option. If you chooseDelete , which is only available on development servers, existing processinstances are deleted. For more information, see Migrating snapshots by using Workflow Center . Click Create InstallationPackage . For example, you have two snapshots, Snap1 and Snap2, already installed on the server. Youwant to install Snap3 onto the server and you select to create a custom installation package. In thewindow, you specify how to handle running instances for two migrations: After Process Center creates theinstallation package, you can see the installation packages listed with the snapshot. Installationpackages are available on the Process Center serveras long as the selected offline server exists in Process Center . If you delete the offline server fromProcess Center , the installation packages for thatserver are also deleted.
    - Leave
    - Migrate
    - Delete

If you choose Leave, existing process instances continue to run using
the previous snapshot. New process instances use the new snapshot. If you choose
Migrate, existing process instances migrate to the new snapshot. There is the
possibility that orphaned tokens could occur with this option. If you choose
Delete, which is only available on development servers, existing process
instances are deleted. For more information, see Migrating snapshots by using Workflow Center.

Click Create Installation
Package.

    - From Snap1 to Snap3
    - From Snap2 to Snap3
7 Expand the Migration Policy Available section to handle migrating running instances fromthe snapshot if either of the following conditions is true: The Migration Policy Available section lists the migration source snapshots that have amigration policy. For each snapshot that you are migrating instances from, clickExport and save the resulting .xml file. If the sectionis missing a migration policy, contact the owner of the snapshot you are installing to create one.For information, see Defining the migration policy by using the Process Center console .

- You selected to create a generic installation package.
- You selected to create a custom installation package and you selected the Leave option for at
least one snapshot.
8. Export the installation package to a file by clicking Export installation
package. Save the resulting .zip file.
9. Transfer the installation package to the offline Process Server by using FTP or a similar utility. If you
exported migration policy files, transfer them as well.
10. On the offline Process Server, run the
BPMInstallPackage command in the
profile\_root/bin directory.
For information about the command, see BPMInstallPackage command.
For
example:AdminTask.BPMInstallPackage('[-inputFile C:\myProcessApps\SHSV856.zip -showSnapshotInfo true]')

For information about the command, see BPMInstallPackage command.
11. To migrate running instances to the new snapshot, run the
BPMMigrateInstances command.
In the command, identify an old snapshot as the source and the new snapshot as the target. If
you exported a migration policy file for the source snapshot, add the path to that file as the
orphanTokenPolicyFile parameter. For information about the command, see BPMMigrateInstances command.Tip: You can also delete all orphaned tokens in
Process Inspector. However, with Process Inspector, you cannot choose to delete individual orphaned
tokens or move any tokens.

For
exampleAdminTask.BPMMigrateInstances(’[-containerAcronym HSS -sourceContainerSnapshotAcronym V1 -targetContainerSnapshotAcronym V2 C:\logFiles\V1\_to\_SHSV856.xml]')
12. Optional: 
If necessary, set environment variables.
For example, the correct value for a particular environment (such as test or production)
might not be known during the design phase. In these situations, provide the value after installing
the snapshot in the new environment.
For information, see BPMSetEnvironmentVariable command or Configuring runtime environment variables.
13. Optional: 
If necessary, establish runtime teams.
For example, after you install a snapshot in a new environment (such as test or
production), you might need to add or remove users in the teams for that project. That is, users in
the test environment might not have been available in the development environment.
For information, see Configuring runtime teams.
14. Optional: If necessary,
control exposed processes and services. For example,
after you install a snapshot in a new environment (such as test or
production), you might need to disable a particular exposed process
or service within that process applicationFor information,
see Configuring exposed processes and services.

## Results

The last snapshot that you install becomes the default snapshot and it is automatically active.