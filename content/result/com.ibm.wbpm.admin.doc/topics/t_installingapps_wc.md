# Installing snapshots onto an offline server by using Workflow Center and wsadmin commands

## Before you begin

Export a snapshot. For more information, see Importing and exporting projects.

If you plan to migrate running instances, check that there is a
migration policy for the snapshot. The migration policy defines how to handle orphaned tokens if any
exist. If a migration policy is not listed for the source snapshot, notify the owner of the snapshot
that your are installing to create the migration policy. The snapshot owner can use  Workflow Center to generate the
migration policy file and use the migration policy editor to modify it. For information, see Defining the migration policy by using the Process Center console.

## Procedure

1. Log in to Workflow Center.
2. On the Process apps or Case solutions page, click
Details for the process application or case solution that you want to
install, and then click Snapshots.
3. Click Install next to the snapshot you want to install.
The Install a snapshot to a server window opens.
4. In the window, select the offline Workflow Server
that you want to install the snapshot to. 
If the process application or case solution already has an installation package for a that
snapshot for the offline Workflow Server, the window
displays a message indicating the snapshot is already installed. If not, you can select the snapshot
and the click Install. After you do this, you get a notification that you
successfully installed the snapshot to your offline server.
5. Select the snapshot you created the installation package for.
6. On the snapshot page, select the Installation details and select Export
Installation Package for the offline server in question.
7. Transfer the installation package to the offline Workflow Server by using FTP or a similar utility. If you exported
migration policy files, transfer them as well.
8. On the offline Workflow Server, run the
BPMInstallPackage command in the
profile\_root/bin directory.
For information about the command, see BPMInstallPackage command.
For
example:AdminTask.BPMInstallPackage('[-inputFile C:\myProcessApps\SHSV856.zip -showSnapshotInfo true]')

For information about the command, see BPMInstallPackage command.
9. To migrate running instances to the new snapshot, run the
BPMMigrateInstances command.
In the command, identify an old snapshot as the source and the new snapshot as the target. If
you exported a migration policy file for the source snapshot, add the path to that file as the
orphanTokenPolicyFile parameter. For information about the command, see BPMMigrateInstances command.Tip: You can also delete all orphaned tokens in
Process Inspector. However, with Process Inspector, you cannot choose to delete individual orphaned
tokens or move any tokens.

For example:
AdminTask.BPMMigrateInstances(’[-containerAcronym HSS -sourceContainerSnapshotAcronym V1 -targetContainerSnapshotAcronym V2 C:\logFiles\V1\_to\_SHSV856.xml]')
10. Optional: 
If necessary, set environment variables.
For example, the correct value for a particular environment (such as test or production)
might not be known during the design phase. In these situations, provide the value after installing
the snapshot in the new environment.
For information, see BPMSetEnvironmentVariable command or Configuring runtime environment variables.
11. Optional: 
If necessary, establish runtime teams.
For example, after you install a snapshot in a new environment (such as test or
production), you might need to add or remove users in the teams for that project. That is, users in
the test environment might not have been available in the development environment.
For information, see Configuring runtime teams.
12. Optional: If necessary,
control exposed processes and services. For example,
after you install a snapshot in a new environment (such as test or
production), you might need to disable a particular exposed process
or service within that process applicationFor information,
see Configuring exposed processes and services.

## Results

The last snapshot that you install becomes the default snapshot and it is automatically active.