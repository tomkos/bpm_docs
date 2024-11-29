# BPMGenerateUpgradeSchemaScripts command-line utility

For a version-to-version migration:

- deployment\_environment\_name/DBType/database\_name.schema\_name

- Run the SQL scripts using the upgradeSchema.sh file that was generated along
with the SQL scripts.
- Run the SQL scripts directly using an SQL session. Note: If you are using SQL Server with
Windows Authentication, you must run the SQL scripts directly using an SQL session.

- Run all upgradeTablespac* scripts before you run any
upgradeSchema* scripts.
- Run the upgradSchema\_SchemaStatus.sql script before you run any other
"upgradeSchema*" SQL scripts.

For a refresh pack upgrade:

The BPMGenerateUpgradeSchemaScripts command is interactive and prompts for
properties such as temporary table names and table space names. The values you specify are used to
generate the appropriate SQL scripts. The upgrade SQL scripts are generated under the
target\_install\_root/profiles/profile\_name/dbscripts directory.

## Location

The BPMGenerateUpgradeSchemaScripts command-line utility is in the
install\_root/bin directory.

- install\_root/logs/migration/BPMGenerateUpgradeSchemaScripts.upgrade.timestamp.error
- install\_root\logs\migration\BPMGenerateUpgradeSchemaScripts.upgrade.timestamp.error

## Syntax

- To migrate from an earlier version to IBM® Business Automation Workflow
24.x:BPMGenerateUpgradeSchemaScripts 
-propertiesFile target\_migration\_properties\_file
- To upgrade from IBM Business Automation Workflow V8.5.x to 24.x:BPMGenerateUpgradeSchemaScripts 
-profileName deployment\_manager\_profile 
[-de deployment\_environment\_name]Tip: If you are upgrading a DB2 for z/OS database, you are prompted to enter new values for
the database specifications. If you press Enter, the default values are used.

## Parameters

## Examples

- BPMGenerateUpgradeSchemaScripts.sh -propertiesFile /tmp/remoteUtil/util/migration/resources/target\_migration.properties
- BPMGenerateUpgradeSchemaScripts.bat -propertiesFile "C:\bpm 85\util\migration\resources\target\_migration.properties"

- BPMGenerateUpgradeSchemaScripts.sh -profileName DmgrProfile
- BPMGenerateUpgradeSchemaScripts.bat -profileName DmgrProfile -de DE1