# DBUpgrade command-line utility

- System Data toolkit
- Process Portal process application
- Hiring Sample tutorial process application
- Topology information in the Business Process Choreographer database
- Schema and data for Process Server and Performance Data Warehouse databases, except for DB2 for
z/OS databases. To manually run the schema update separately, see the instructions at the end of
this topic.

- Although the DBUpgrade utility updates the System Data toolkit to IBM® Business Automation Workflow
24.x, it does not automatically update
existing dependencies. The dependencies are updated as part of the postmigration procedures.
- If you already have a version of Db2 installed
and you create the deployment environment without deferring schema creation, you must have Db2® 10.5.0.0 or above. Otherwise, the
database version validation will fail with an error; for example CWMCB0316E: Your database
system is not the required version. The minimum supported version is 10.5.0.0 but the current
version is 10.1.0.2.

You must run the DBUpgrade command once for each deployment environment.

You can also run the DBUpgrade
command with the -validate option to check that your configured database user
has the correct permissions to perform an upgrade.

## Prerequisites

- Before running the DBUpgrade command, make sure that the servers and cluster
members are stopped.
- If you are migrating from an earlier version, the user name and password are taken from the
target\_migration\_properties\_file. The user name must have various WebSphere
privileges. The WebSphere primary administrative user has them all. In the source environment, you
can find the primary administrative user name in the administrative console by going to Users and Groups > Administrative user roles. In the target environment, if you do not have access to the administrative console,
you can find  bpm.de.authenticationAlias.#.name=CellAdminAlias in the
BPMConfig properties file. Use the user name and password for that alias.
- In a DB2 high availability disaster recovery (HADR) environment, remove the
following line from the upgradeSchema\_ProcessServer.sql script in
target\_deployment\_manager\_profile/dbscripts/Upgrade/cell\_name.de\_name/database\_type/Process\_Server\_database\_name
before running the command.
"ALTER TABLE psbpmdb.LSW\_PO\_VERSIONS ACTIVATE NOT LOGGED INITIALLY"By
default, the DB2 blocknonlogged parameter is set to Yes
for HADR that causes failure of the ALTER TABLE statement with the NOT
LOGGED INITIALLY parameter. For more information, see the blocknonlogged - Block creation of tables that allow non-logged activity
configuration parameter topic.

## Location

The DBUpgrade command is in the
install\_root/bin directory, where
install\_root is the installation location of IBM Business Automation Workflow.

The logs are saved under the profile\_root/logs directory
in files named DBUpgrade\_TimeStamp.log and
bootstrapProcesServerData.AppClusterName.log or
bootstrapProcesServerData.log, where profile\_root is the root
of the stand-alone or deployment manager profile, or the profile directory that you specified for
the profile.name property in the target\_migration.properties
file.

## Syntax

- To migrate from an earlier version to IBM Business Automation Workflow
24.x:
DBUpgrade 
-propertiesFile target\_migration\_properties\_file 
-backupFolder snapshot\_folder
- To upgrade from IBM Business Automation Workflow V8.5.x to 24.x :
    - You can first run the DBUpgrade
-validate command to make sure that your configured database user has the correct
permissions to perform an upgrade. The bpmSchemaAdminUser needs read access to the database catalog
to check the permissions of the configured database
user.DBUpgrade -validate
-profileName deployment\_manager\_profile 
[-de deployment\_environment\_name]
-bpmSchemaAdminUser admin\_user
-bpmSchemaAdminPassword admin\_password
    - Business Automation Workflow Advanced or Standard:
DBUpgrade  
-profileName deployment\_manager\_profile 
[-de deployment\_environment\_name]
    - Business Automation Workflow
Express:DBUpgrade  
-profileName stand-alone\_profile 
[-de deployment\_environment\_name]

## Parameters

| Database   | How the command validates                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DB2        | Validates the authorities that are directly and indirectly granted to the Process Server and Performance Data Warehouse database user for the Create Table, Alter Table, Drop Table, Create Index, Drop Index, Create Procedure, and Drop Procedure statements. If the authority validation fails, checks the privileges that are granted directly and indirectly to the user on the schema level.                                                                                                                                                                                                                          |
| Oracle     | Checks all the privileges that are granted to the Process Server and Performance Data Warehouse database user, including privileges that are granted directly and privileges that are granted through roles. Validation succeeds if all the required privileges are found. Otherwise, it fails.                                                                                                                                                                                                                                                                                                                             |
| SQL Server | Checks all the privileges that are granted to the Process Server and Performance Data Warehouse database user, including privileges that are granted directly and privileges that are granted through roles. Validation succeeds if all the required privileges are found. If any of the required privileges are denied, validation fails. If any of the required privileges are not granted, the command continues to check if the user is a member of one of the fixed roles: db\_ddladmin, db\_datareader, or db\_datawriter. Validation succeeds if the user is a member of one of those fixed roles. Otherwise, it fails. |

| Database   | Required privileges                                                                                                                                                                                                                     |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DB2        | read access to system tables: SYSCAT.SCHEMAAUTH, SYSCAT.ROUTINEAUTHexecute privilege on built-in DB2 table functions: SYSPROC.AUTH\_LIST\_AUTHORITIES\_FOR\_AUTHID, SYSPROC.AUTH\_LIST\_GROUPS\_FOR\_AUTHID, SYSPROC.AUTH\_LIST\_ROLES\_FOR\_AUTHID |
| Oracle     | read access to system tables: DBA\_SYS\_PRIVS, DBA\_ROLE\_PRIVS                                                                                                                                                                             |
| SQL Server | read access to system tables: DATABASE\_PERMISSIONS, DATABASE\_PRINCIPALS, DATABASE\_ROLE\_MEMBERS                                                                                                                                          |

## Examples

- install\_root/bin/DBUpgrade.sh -propertiesFile /opt/BPM/util/migration/resources/target\_migration.properties -backupFolder /tmp/snapshot
- install\_root\bin\DBUpgrade.bat -propertiesFile "C:\IBM BPM\util\migration\resources\target\_migration.properties" -backupFolder C:\snapshot

- install\_root/bin/DBUpgrade.sh -propertiesFile 
/opt/BPM/util/migration/resources/target\_migration.properties
- install\_root\bin\DBUpgrade.bat -propertiesFile 
"C:\IBM BPM\util\migration\resources\target\_migration.properties"

- install\_root/bin/DBUpgrade.sh -profileName DmgrProfile
- install\_root\bin\DBUpgrade.bat -profileName DmgrProfile -de DE1

- install\_root/bin/DBUpgrade.sh -validate 
-profileName DmgrProfile -bpmSchemaAdminUser SchemaAdminUser 
-bpmSchemaAdminPassword SchemaAdminPassword
install\_root/bin/DBUpgrade.sh -profileName DmgrProfile
- install\_root\bin\DBUpgrade.bat -validate 
-profileName DmgrProfile -bpmSchemaAdminUser SchemaAdminUser
-bpmSchemaAdminPassword SchemaAdminPassword -de DE1
install\_root\bin\DBUpgrade.bat -profileName DmgrProfile 
-de DE1