# Installing snapshots onto an offline server by using wsadmin
commands and generic installation packages

## Before you begin

If you plan to migrate
running instances, check that there is a migration policy for the snapshot. The migration policy
defines how to handle orphaned tokens if any exist. If a migration policy is not listed for the
source snapshot, notify the owner of the snapshot that your are installing to create the migration
policy. The snapshot owner can use Workflow Center to generate the
migration policy file and use the migration policy editor to modify it. For information, see Defining the migration policy by using the Process Center console.

## Procedure

1. On the IBM Workflow
Center server, create the
installation package for the snapshot for a specific server by running the
BPMExportInstallPackage command in the
profile\_root/bin directory.
For
example:AdminTask.BPMExportInstallPackage('[
-containerAcronym "HSS"
-containerTrackAcronym "Main"
-containerSnapshotAcronym "S1"
-outputFile "C:\SnapS1.zip"]')
For information about the command, see BPMExportInstallPackage command.
2. Optional: For each server and snapshot pair
that you are installing the process application onto, associate the
installation package with the server: For example:AdminTask.BPMUpdateInstallationInformation('[
-containerAcronym "TOLPC"
-containerTrackAcronym "Main"
-containerSnapshotAcronym "S1"
-serverName "InstallPackageServer1"]')For information about the command, see BPMUpdateInstallationInformation command.This step is not necessary for
connected servers because Workflow Center is
automatically updated with the association.
3. For each snapshot you want to migrate instances from, export
the migration policy by running the BPMExtractMigrationPolicy command.
The migration policy file is a standard XML file that you can
open and edit if necessary.For example:AdminTask.BPMExtractMigrationPolicy('[-containerAcronym HSS -containerSourceSnapshotAcronym V1 -containerTargetSnapshotAcronym V2 -outputFile C:\migrationPolicy\V1\_to\_V2.xml]')
For information about the command, see BPMExtractMigrationPolicy command.
4. Using FTP or a similar utility, transfer the installation
package (.zip) and the migration policy file
(.xml) to the server that hosts the new snapshot
or to a central location that the server can access.
5. On the Workflow Server, install the snapshot by
running the BPMInstallPackage command in the
profile\_root/bin directory.
For
example:BPMInstallPackage('[-inputFile "C:\SnapS1.zip"]')
For information about the command, see BPMInstallPackage command.
6. To migrate running instances to the new snapshot, run the
BPMMigrateInstances command on the server. 
In the command, identify an old snapshot as the source and the new snapshot as the target. If
you exported a migration policy file for the source snapshot, add the path to that file as the
orphanTokenPolicyFile parameter. For information about the command, see BPMMigrateInstances command.Tip: You can also delete all orphaned tokens in
Process Inspector. However, with Process Inspector, you cannot choose to delete individual orphaned
tokens or move any tokens.

For example:
AdminTask.BPMMigrateInstances(’[-containerAcronym HSS -sourceContainerSnapshotAcronym V1 -targetContainerSnapshotAcronym V2 C:\logFiles\V1\_to\_SHSV856.xml]')
7. Optional: 
If necessary, set environment variables.
For example, the correct value for a particular environment (such as test or production)
might not be known during the design phase. In these situations, provide the value after installing
the snapshot in the new environment.
For information, see BPMSetEnvironmentVariable command or Configuring runtime environment variables.
8. Optional: 
If necessary, establish runtime teams.
For example, after you install a snapshot in a new environment (such as test or
production), you might need to add or remove users in the teams for that project. That is, users in
the test environment might not have been available in the development environment.
For information, see Configuring runtime teams.
9. Optional: If necessary,
control exposed processes and services. For example,
after you install a snapshot in a new environment (such as test or
production), you might need to disable a particular exposed process
or service within that process applicationFor information,
see Configuring exposed processes and services.

## What to do next

If you experience problems with your installation, check
the process-installer.log file. For more information
about what issues can occur, see Troubleshooting snapshot installations.