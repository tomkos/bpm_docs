# BPMMigrationPreValidation command-line utility

- Profile validation:
    - Validates that the source product and version is supported
for migration
    - Validates the status of IBM® Business Process Manager
 applications
    - Validates the connection status of all IBM BPM data sources
    - Validates the status of IBM BPM messaging
engines
    - Performs the following checks:
        - Whether any existing service integration bus (SIB) message is
in a transaction
        - Whether too many SIB messages are stuck in a queue
        - Whether any failed events are not processed
- Notifies you of changes that you must make after you migrate,including the following changes:
    - Authentication aliases that are not migrated because
you added them in the source environment
    - Data sources that are not migrated because you added
them in the source environment
- Notifies you of the key changes that occur during migration, includingthe following changes:

- Security changes
- Changes to XML configuration properties files. Some
XML security configuration properties are moved to the WebSphere® Application
Server configuration
files automatically. These properties are exported to the properties
file and will be moved to the WebSphere Application
Server configuration
files when you run the command. See the table in WebSphere Lombardi
Edition XML configuration properties that are migrated to WebSphere
Application Server configuration files for a list of the properties
that have been moved.
- Notifies you of current configuration that you might need tofix after migration, including the following configuration:

- XML configuration properties files
- Lightweight Third-Party Authentication (LTPA) key file
- Topology information
- Database validation:

- Notifies you if the volume of data will increase the
downtime required for migration
- Checks for customized indexes
- Analyzes the tables for migration impact and, if required,
recommends actions that you can take before migration
- Checks that the log file size is sufficient and,
if not, provides the command that you should run to update it
- Checks that the records in the Business Space tables
are valid.
- Reminds you to check the oobLoadedStatus.properties
file.

After you run the command, go to the report directory that you specified and open the
index.html file in a browser to view the report. If you see validation errors
or warnings, click the row to see the details of the problem and the steps that you must take to fix
it before migration.

## Prerequisites

- Make sure that the deployment environment or stand-alone
server is running before you run this command.
- The user name and password are taken from the migration.properties file.
The user name must have various WebSphere privileges. The WebSphere
primary administrative user has them all. In the source environment,
you can find the primary administrative user name in the administrative
console by going to Users and Groups > Administrative user roles.

## Location

The BPMMigrationPreValidation command-line utility is in the
install\_root\_24.x/bin
directory.

If you installed the new version of the product on a different computer and copied the migration
files to the source environment, the command is found in
remote\_migration\_utility/bin on the source computer.

If you are not using the remote migration utility, the log file is in
install\_root\_24.x/logs/migration.

If you are using the remote migration utility, the log file is in
remote\_migration\_utility/logs/migration.

## Syntax

```
install\_root\_24.x/bin/BPMMigrationPreValidation 
-propertiesFile path\_to\_migration\_properties\_file 
-reportDir path\_to\_report\_package
```

## Parameters

- If you installed the new version of the product on the same computer as the source environment,
the sample file is found in install\_root\_24.x/util/migration/resources/migration.properties.
- If you installed the new version of the product on a different computer and copied the migration
files to the source environment, the sample file is found in
remote\_migration\_utility/util/migration/resources/migration.properties.

You must check all the properties in this file, and edit them if required.

## Examples

- BPMMigrationPreValidation.sh -propertiesFile /opt/BPM24.x/util/migration/resources/source\_migration.properties -reportDir /BPM751\_precheck\_report
- BPMMigrationPreValidation.bat -propertiesFile "C:\BPM 24.x\util\migration\resources\source\_migration.properties" -reportDir E:\BPM751\_precheck\_report