# BPMManageApplications command-line utility

- Before you take a snapshot of the source environment
- Before you run the migration command (BPMMigrate) in the target environment (to make sure that
no new events are coming into the source databases)

- After you apply all configuration updates in the target environment
- If migration fails, to restore the source environment

## Prerequisites

- The user name and password are taken from the migration.properties file.
The user name must have various WebSphere privileges. The WebSphere
primary administrative user has them all. In the source environment,
you can find the primary administrative user name in the administrative
console by going to Users and Groups > Administrative user roles. In
the target environment, if you do not have access to the administrative
console, you can find  bpm.de.authenticationAlias.#.name=CellAdminAlias in
the BPMConfig properties file. Use the user name
and password for that alias.

## Location

The BPMManageApplications command-line utility is in the
install\_root\_24.x/bin
directory.

If you installed the new version of the product on a different computer and copied the migration
files to the source environment, the file is found in
remote\_migration\_utility/bin on the source computer.

If you use the remote migration utility to run the command in the source environment, the log
file is in remote\_migration\_utility/logs/migration.

Otherwise, the log file is in install\_root\_24.x/logs/migration in the target environment.

## Syntax

- To disable the automatic starting of applications and
schedulers:BPMManageApplications 
-autoStart false 
-source|-target 
-propertiesFile migration\_properties\_file
- To enable the automatic starting of applications and
schedulers:BPMManageApplications 
-autoStart true 
-source|-target 
-propertiesFile migration\_properties\_file

You must restart the server after running this
command.

## Parameters

- If you installed the new version of the product on the same computer as the source environment,
the sample file is found in install\_root\_24.x/util/migration/resources/migration.properties.
- If you installed the new version of the product on a different computer and copied the migration
files to the source environment, the sample file is found in
remote\_migration\_utility/util/migration/resources/migration.properties.

You must check all the properties in this file, and edit them if required.

## Examples

- ./BPMManageApplications.sh -autoStart true -source -propertiesFile /opt/BPM24.x/util/migration/resources/source\_migration.properties
- BPMManageApplications.bat -autoStart false -target -propertiesFile "E:\Upgrade Utilities\util\migration\resources\target\_migration.properties"