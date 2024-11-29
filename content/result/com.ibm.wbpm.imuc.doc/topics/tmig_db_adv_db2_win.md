# Upgrading DB2 databases

For DB2, initialize new databases and upgrade your
existing schemas and data so that your databases work with the new
version of IBM Business Automation Workflow.

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

If you are migrating
from IBM Business Process Manager
 V7.5.x
and you get an OutOfMemory error indicating too many or too large
data records, increase the heap size of the JVM for the DBUpgrade command.
Open the DBUpgrade.bat file in install\_root\bin and
find -Xmx2048m in this file. This parameter indicates
that the maximum JVM heap size is 2048 megabytes. Increase this value
to update the heap size.

- The CONNECT and CREATETAB privileges are required on the database level.
- The upgrade process accesses system views and procedures. Grant the SELECT and EXECUTE
privileges to the user who performs the upgrade. These privileges are already granted to the public
group by default; it is not necessary to grant them again unless they were
revoked.syscat.tables
syscat.views
syscat.columns
syscat.indexes

PROCEDURE ADMIN\_CMD and REORG authority

## Procedure

For each deployment environment that
you are creating, complete the following steps:

1. Copy the whole folder target\_deployment\_manager\_profile\dbscripts\Upgrade\ to
your database computer.
2. If you did not create a new messaging
engine database and instead you plan to reuse your previous messaging
engine database and schema, you must manually drop the existing messaging
engine tables for each one.
 Tip: The messaging engine table names use the SIB prefix.

If you see any of the following error messages,
follow the instructions in the message to increase the default log
file size.CWMCB0350E: Database CMN172DB does not have defined a sufficient logfile size. Use UPDATE DB CFG FOR CMN172DB USING LOGFILSIZ 16384 DEFERRED to change. Actual size = 4096, minimum size = 16384.
CWMCB0350E: Database PS172DB does not have defined a sufficient logfile size. Use UPDATE DB CFG FOR PS172DB USING LOGFILSIZ 16384 DEFERRED to change. Actual size = 4096, minimum size = 16384.
CWMCB0350E: Database PDW172DB does not have defined a sufficient logfile size. Use UPDATE DB CFG FOR PDW172DB USING LOGFILSIZ 16384 DEFERRED to change. Actual size = 4096, minimum size = 16384.
CWMCB0350E: Database BPC172DB does not have defined a sufficient logfile size. Use UPDATE DB CFG FOR BPC172DB USING LOGFILSIZ 16384 DEFERRED to change. Actual size = 4096, minimum size = 16384.
3 On the database computer, upgradeall schemas. To see which schemas are upgraded, go to the directorywhere you copied the Upgrade folder and see the upgradeSchemaScriptsHelp\_de\_name .txt file. Go to the directory where you copiedthe Upgrade folder and run the upgradeSchemaAll command.There is a different upgradeSchemaAll command foreach deployment environment in the source. upgradeSchemaAll\_de\_name .bat You are prompted to enter the user name and password for each databaseconnection. This command initializes the new database components and upgrades the schemas of all theexisting databases except for the Workflow Server and Performance Data Warehouse databases. Those two databases are upgraded later by theDBUpgrade command. Alternatively, if you want to runthe SQL scripts manually, use an SQL session and run the scripts inthe sequence listed in the Upgrade\_folder \upgradeSchemaScriptsHelp\_de\_name .txt fileand use the following parameters and commands. db2 -s -t -v -z log name -f script\_name where: You might see warning messages when you run the scripts to upgrade the Business Space databasetelling you that the result of a query is an empty table or that no row was found for FETCH, UPDATE,or DELETE. These messages can safely be ignored. The result.log filesare found in Upgrade\_folder \cell\_name or cell\_name .de\_name \database\_type \database\_name .schema\_name .

Go to the directory where you copied
the Upgrade folder and run the upgradeSchemaAll command.
There is a different upgradeSchemaAll command for
each deployment environment in the source.

```
upgradeSchemaAll\_de\_name.bat
```

Alternatively, if you want to run
the SQL scripts manually, use an SQL session and run the scripts in
the sequence listed in the Upgrade\_folder\upgradeSchemaScriptsHelp\_de\_name.txt file
and use the following parameters and commands.

```
db2 -s -t -v -z log name  -f  script\_name
```

    - -s specifies that the script is to exit as soon as the first error
occurs
    - -t specifies that the statement is to be printed on the command line so
that it can be logged in a log file
    - -v specifies that the output from the command is to be sent to a log file
that can be used for error checking
    - -z specifies that the semicolon (;) is to be treated as a delimiter for the
commands in the file
    - -f specifies the input file name

You might see warning messages when you run the scripts to upgrade the Business Space database
telling you that the result of a query is an empty table or that no row was found for FETCH, UPDATE,
or DELETE. These messages can safely be ignored.

The result.log files
are found in Upgrade\_folder\cell\_name or cell\_name.de\_name\database\_type\database\_name.schema\_name.

4 Copy the sample migration.properties fileand rename it to target\_migration.properties .Update the file with the configuration information for the targetenvironment. Check all the target properties and edit themif required, following the instructions in the sample file. The samplefile is in install\_root \util\migration\resources\migration.properties . Specify target environment values for the following properties: You must specify the source cluster names, not target cluster names, for the followingproperties:Note: Because IBM BPM Express is a stand-alone server and not a cluster, you must not usethe following properties for the source cluster name.

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
5 To upgrade the databases to 24.x , run theDBUpgrade utility on the deployment manager computer in the target environment.The DBUpgrade command automatically upgrades the schema and data for Workflow Server and Performance DataWarehouse and updates the topology information in the Business Process Choreographer database. Tip: By default, DBUpgrade upgrades both the schema and data forWorkflow Server andPerformance Data Warehouse databases. For instructions for running the schema update separately, seethe DBUpgrade troubleshooting topic. Important: Ensure that your deployment manager and all the managed nodes in the sourceenvironment have been stopped before running this utility. install\_root \bin\DBUpgrade.bat -propertiesFile target\_migration\_properties\_file -backupFolder snapshot\_folder where: Forexample:install\_root \bin\DBUpgrade.bat -propertiesFile "C:\BPM 24.x \util\migration\resources\target\_migration.properties" -backupFolder C:\snapshot The command displays each database upgrade action as it runs. After all the upgrades arefinished, you see a message similar to the following message:All upgrade steps have been completed successfully. The log location is listed in the output. If there are errors or exceptions, they appear in thelog. If you are migrating from IBM Business Process Manager V7.5.x and you get anout-of-memory error indicating too many or too large data records, you can try to increase the heapsize of the JVM for the DBUpgrade command. Open theDBUpgrade.bat file in install\_root \bin and find -Xmx2048m in this file. It indicates that the maximum JVM heap size is2048 megabytes. You can increase this value to update the heap size. If necessary for troubleshooting, you can run DBUpgrade -generateSQLOnly togenerate the SQL files without running them. You can then edit the generated SQL files manually andrun DBUpgrade -omitSQLGeneration to upgrade the database using the modifiedfiles.

```
install\_root\bin\DBUpgrade.bat -propertiesFile target\_migration\_properties\_file -backupFolder snapshot\_folder
```

- target\_migration\_properties\_file is the full path to the
migration properties file in which you specified the configuration information for the target
environment.
- snapshot\_folder is the directory that contains the information that was
extracted from the source environment

```
install\_root\bin\DBUpgrade.bat -propertiesFile "C:\BPM 24.x\util\migration\resources\target\_migration.properties" -backupFolder C:\snapshot
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

6. If you did not increase the default
log file size, increase it by using the following SQL statement, where @DB\_NAME@ is
the name of your Workflow Server database.
 UPDATE DB CFG FOR @DB\_NAME@ USING LOGFILSIZ 16384 DEFERRED;

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