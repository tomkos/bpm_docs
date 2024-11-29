# Installing snapshots onto a connected server by using wsadmin
commands

## Before you begin

In addition, ensure that
the user ID that you are using has access to install snapshots to the connected Workflow Server. For information, see Restricting installation access to runtime servers.

## About this task

You can script the installation of snapshots onto a connected server instead of using Workflow Center. By using a set of
scripts that contain wsadmin commands, you can automate the installation steps. When you install a
snapshot, you also install the toolkit snapshots that it depends on unless these toolkit snapshots
already exist on the Workflow Server.

## Procedure

To script the installation of a snapshot onto a connected
server, include the following wsadmin commands in the scripts:

1. Install the snapshot by running the BPMInstall command in the
profile\_root/bin directory.
For
example:AdminTask.BPMInstall('[-containerAcronym HSS -containerSnapshotAcronym SHSV856 -containerTrackAcronym Main -serverName ProcessServer01 -skipGovernance false]')
For information about the command, see BPMInstall command.If the process application is already installed, any running
instances are given the Leave migration option. For information, see Migrating snapshots by using Workflow Center.
2. Optional: If you are installing a snapshot
and you need a migration policy to migrate active instances, extract
the migration policy file for that snapshot using the BPMExtractMigrationPolicy command.
For example:AdminTask.BPMExtractMigrationPolicy('[-containerAcronym HSS -containerSourceSnapshotAcronym V1 -containerTargetSnapshotAcronym SHSV856 -outputFile C:\ftp\_source\V1\_to\_SHSV856.xml]')
The creator of the snapshot should create the migration policy
by analyzing the difference between the source and target snapshots.
The snapshot creator can use the migration policy editor to edit the
content of the migration policy file. For information, see Defining the migration policy by using the Process Center console.
3. On the Workflow Server, to migrate running
instances to the new snapshot, run the BPMMigrateInstances command in the
profile\_root/bin directory. 
In the command, identify an old snapshot as the source and the new snapshot as the target. If
you exported a migration policy file for the source snapshot, add the path to that file as the
orphanTokenPolicyFile parameter. For information about the command, see BPMMigrateInstances command.Tip: You can also delete all orphaned tokens in
Process Inspector. However, with Process Inspector, you cannot choose to delete individual orphaned
tokens or move any tokens.

For example:
AdminTask.BPMMigrateInstances(’[-containerAcronym HSS -sourceContainerSnapshotAcronym V1 -targetContainerSnapshotAcronym V2 C:\logFiles\V1\_to\_SHSV856.xml]')
4. Optional: 
If necessary, set environment variables.
For example, the correct value for a particular environment (such as test or production)
might not be known during the design phase. In these situations, provide the value after installing
the snapshot in the new environment.
For information, see BPMSetEnvironmentVariable command or Configuring runtime environment variables.
5. Optional: 
If necessary, establish runtime teams.
For example, after you install a snapshot in a new environment (such as test or
production), you might need to add or remove users in the teams for that project. That is, users in
the test environment might not have been available in the development environment.
For information, see Configuring runtime teams.
6. Optional: If necessary,
control exposed processes and services. For example,
after you install a snapshot in a new environment (such as test or
production), you might need to disable a particular exposed process
or service within that process applicationFor information,
see Configuring exposed processes and services.

## Results