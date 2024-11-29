# BPMExtractSourceInformation command-line utility

The BPMExtractSourceInformation command exports the SIB messages and advanced
applications from the source deployment manager environment so that they can be imported into the
target environment using the BPMMigrate command.

If you are migrating from IBM BPM Advanced, you must
use the BPMExtractSourceInformation command to extract the SIB messages and
advanced applications during migration so that you can migrate them to your new environment.

## Prerequisites

- Make sure that the deployment environment or stand-alone
server is running before you run this command.
- The user name and password are taken from the migration.properties file.
The user name must have various WebSphere privileges. The WebSphere
primary administrative user has them all. In the source environment,
you can find the primary administrative user name in the administrative
console by going to Users and Groups > Administrative user roles.

## Location

The BPMExtractSourceInformation command-line utility is in the
install\_root\_24.x/bin
directory.

If you installed the new version of the product on a different computer and copied the migration
files to the source environment, the command is found in
remote\_migration\_utility/bin on the source computer.

If the -backupFolder parameter is set, the log file is in
snapshot\_folder/logs.

If the -backupFolder parameter is not set and you are using the remote
migration utility, the log file is in
remote\_migration\_utility/logs/migration.

If the -backupFolder parameter is not set and you are not using the remote
migration utility, the log file is in
install\_root\_24.x/logs/migration.

## Syntax

```
install\_root\_24.x/bin/BPMExtractSourceInformation 
-backupFolder snapshot\_folder 
-propertiesFile source\_migration\_properties\_file
```

## Parameters

- If you installed the new version of the product on the same computer as the source environment,
the sample migration properties file is found in
install\_root\_24.x/util/migration/resources/migration.properties.
- If you installed the new version of the product on a different computer and copied the migration
files to the source environment, the sample migration properties file is found in
remote\_migration\_utility/util/migration/resources/migration.properties.

Check all the properties in this file and edit them if required.

## Examples

- BPMExtractSourceInformation -backupFolder /tmp/snapshot -propertiesFile /opt/BPM24.x/util/migration/resources/source\_migration.properties
- BPMExtractSourceInformation -backupFolder c:\snapshot -propertiesFile "C:\BPM 24.x\util\migration\resources\source\_migration.properties"