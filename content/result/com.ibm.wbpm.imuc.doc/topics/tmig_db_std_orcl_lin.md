# Upgrading Oracle databases

For Oracle, initialize new databases and upgrade
your existing schemas and data so that your databases work with the
new version of IBM® Business Automation Workflow.

Figure 1. Sample environment after existing schemas and data are updated.
The source environment is not running and the databases are not in
use. The databases contain updated schemas and data. The target is
not running but contains a deployment environment.

<!-- image -->

<!-- image -->

- System Data toolkit
- Heritage Process Portal process
application
- Hiring Sample tutorial process application

## Before you begin

Ensure that you have shut down the source
environment before you proceed with the migration.

If
you are migrating from IBM Business Process Manager
 V7.5.x
and you get an OutOfMemory error indicating too many or too large
data records, increase the heap size of the JVM for the DBUpgrade command.
Open the DBUpgrade.sh file in install\_root/bin and
find -Xmx2048m in this file. This parameter indicates
that the maximum JVM heap size is 2048 megabytes. Increase this value
to update the heap size.

- The CONNECT, RESOURCE, DBA\_TABLES, and SELECT privileges are required on the database
level.
- The upgrade process accesses system views. Grant the SELECT privilege to the user who performs
the upgrade. These privileges are already granted to the public group by default; it is not
necessary to grant them again unless they were revoked.all\_indexes
all\_tables
USER\_TAB\_COLUMNS
all\_objects
all\_constraints
all\_tab\_columns

```
Executing upgrade step: Upgrade 8.5.0 schema to 8.5.5 for database ProcessServerDatabase.
Error executing SQL statement: ORA-60019: Creating initial extent of size 14 in table space of extent size 8
```

## Procedure

For each deployment environment that
you are creating, complete the following steps:

1. Copy the whole folder target\_deployment\_manager\_profile/dbscripts/Upgrade/ to
your database computer.
2. If you did not create a new messaging
engine database and instead you plan to reuse your previous messaging
engine database and schema, you must manually drop the existing messaging
engine tables for each one.
 Tip: The messaging engine table names use the SIB prefix.
3. On the database computer, upgrade all schemas. To see which schemas
are upgraded, go to the directory where you copied the Upgrade folder and see
the upgradeSchemaScriptsHelp\_de\_name.txt file.

Go to the directory where you copied the Upgrade folder and run the
upgradeSchemaAll command. There is a different
upgradeSchemaAll command for each deployment environment in the source.

upgradeSchemaAll\_de\_name.sh

You are prompted to enter the user name and password for each database
connection. This command initializes the new database components and upgrades the schemas of all the
existing databases except for the Workflow Server
and Performance Data Warehouse databases. Those two databases are upgraded later by the
DBUpgrade command.

Alternatively, if you want to run the SQL scripts manually, use an SQL session and run the
scripts in the sequence listed in the
Upgrade\_folder/upgradeSchemaScriptsHelp\_de\_name.txt
file. The options are embedded in the SQL scripts. Additional options are not required.

Important: Run the table creation file for IBM Content
Navigator. The file is
in
Upgrade\_folder/cell\_name.DE\_name/db\_type/icn\_database.icn\_schema/createTable\_ICN.sql.

You might see warning messages when you run the scripts to upgrade the Business Space database
telling you that the result of a query is an empty table or that no row was found for FETCH, UPDATE,
or DELETE. These messages can safely be ignored.

The result.log files are found in
Upgrade\_folder/cell\_name or
cell\_name.de\_name/database\_type/database\_name.schema\_name.
4 Copy the sample migration.properties fileand rename it to target\_migration.properties .Update the file with the configuration information for the targetenvironment. Check all the target properties and edit themif required, following the instructions in the sample file. The samplefile is in install\_root /util/migration/resources/migration.properties . Specify target environment values for the following properties: You must specify the source cluster names, not target cluster names, for the followingproperties:Note: Because IBM BPM Express is a stand-alone server and not a cluster, you must not usethe following properties for the source cluster name.
    - admin.username and admin.password: Use the cellAdmin
user or the WebSphere primary administrative user name.
    - bpm.home: The installation root of your target product. Make sure that the
file separators are forward slashes (/). Use the full path. Do not use the tilde character (Ëœ) to
stand for the home directory. For example:
bpm.home=/opt/IBM/BPM
bpm.home=C:/IBM/BPM
    - profile.name: The target deployment manager profile.
    - target.config.property.file: The full path of the configuration properties
file that you used to create your target environment.
    - source.application.cluster.name
    - source.messaging.cluster.name
    - source.support.cluster.name
    - source.web.cluster.name
5 To upgrade the databases to 24.x , run theDBUpgrade utility on the deployment manager computer in the target environment.The DBUpgrade command automatically upgrades the schema and data for Workflow Server and Performance DataWarehouse. Tip: By default, DBUpgrade upgrades both the schema and data forWorkflow Server andPerformance Data Warehouse databases. For instructions for running the schema update separately, seethe DBUpgrade troubleshooting topic. Important: Ensure that your deployment manager and all the managed nodes in the sourceenvironment have been stopped before running this utility. install\_root /bin/DBUpgrade.sh -propertiesFile target\_migration\_properties\_file where: Forexample:install\_root /bin/DBUpgrade.sh -propertiesFile /opt/BPM24.x /util/migration/resources/target\_migration.properties The command displays each database upgrade action as it runs. After all the upgrades arefinished, you see a message similar to the following message:All upgrade steps have been completed successfully. The log location is listed in the output. If there are errors or exceptions, they appear in thelog. If you are migrating from IBM Business Process Manager V7.5.x and you get anout-of-memory error indicating too many or too large data records, you can try to increase the heapsize of the JVM for the DBUpgrade command. Open theDBUpgrade.sh file in install\_root /bin and find -Xmx2048m in this file. It indicates that the maximum JVM heap size is2048 megabytes. You can increase this value to update the heap size. If necessary for troubleshooting, you can run DBUpgrade -generateSQLOnly togenerate the SQL files without running them. You can then edit the generated SQL files manually andrun DBUpgrade -omitSQLGeneration to upgrade the database using the modifiedfiles.

```
install\_root/bin/DBUpgrade.sh -propertiesFile target\_migration\_properties\_file
```

- target\_migration\_properties\_file is the full path to the
migration properties file in which you specified the configuration information for the target
environment.

```
install\_root/bin/DBUpgrade.sh -propertiesFile /opt/BPM24.x/util/migration/resources/target\_migration.properties
```

```
All upgrade steps have been completed successfully.
```

The log location is listed in the output. If there are errors or exceptions, they appear in the
log.

If necessary for troubleshooting, you can run DBUpgrade -generateSQLOnly to
generate the SQL files without running them. You can then edit the generated SQL files manually and
run DBUpgrade -omitSQLGeneration to upgrade the database using the modified
files.

6. If you are migrating from IBM Business Process Manager
Express V8.6, run the
BPMUpdateSystemApp command on all .twx files except those files
that have the word sample in its name from the folder
install\_root/BPM/Lombardi/imports/. If, for example, the file was named
procurement-sample.twx, it would be excluded. If, for example, the file was named
system-toolkit.twx, the command would look like this:
 wsadmin -lang jython -conntype none -javaoption -Xms256m -javaoption -Xmx1024m
wsadmin>AdminTask.BPMUpdateSystemApp( [ '-twxFile', 'install\_root/BPM/Lombardi/imports/system-toolkit.twx', '-clusterName', 'PC\_clusterName' ] )See
BPMUpdateSystemApp command for more information about the command.

## What to do next

You might see warning
messages similar to the following in the upgrade log: Couldn't
load Resource META-INF*****. These messages can safely be
ignored.

## Related reference

- DBUpgrade troubleshooting

## Related information

- DBUpgrade command-line utility
- Sample migration.properties files
- Completing configuration for IBM Business Automation Workflow