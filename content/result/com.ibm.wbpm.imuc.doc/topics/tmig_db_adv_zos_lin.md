# Upgrading DB2 for z/OS databases

For DB2 for z/OS databases, increase the buffer
size for table spaces, initialize new databases, and upgrade your
existing schemas and data.

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

- The CONNECT and CREATETAB privileges are required on the database level.
- The upgrade process accesses some system views. Grant the SELECT privilege to the user who
performs the upgrade. These privileges are already granted to the public group by default; it is not
necessary to grant them again unless they were revoked.sysibm.systables
sysibm.sysviews
sysibm.syscolumns
sysibm.sysindexes

## Procedure

For each deployment environment that
you are creating, complete the following steps:

1 To initialize your new database components,run the create*.sql files that were generatedwhen you ran the BPMConfig -create command.
    1. Copy the create*.sql scripts
for the new database components from target\_deployment\_manager\_profile/dbscripts/Upgrade/ to
your database computer.

You can then connect to each database and run the customized SQL files against the database.
    2 If you created a new common database forthe deployment-environment-scoped common database: Remember: Starting in IBM Business Process Manager V8.5.x,the common database is split into two pieces. One is cell-scoped andis used for the entire cell. The other, which includes event sequencingand the failed event manager, is deployment-environment-scoped, andmust be configured for each deployment environment. Youare not required to create the event sequencing and failed event tablesif you are using the old common database for the deployment-environment-scopedcommon database.
        1. Run createSchema\_CommonDB.sql to create the
event sequencing and failed event tables.
        2. If you have data in the event sequencing table (named PERSISTENTLOCK)
in the source environment, export the data from the jdbc/WPSDB data
source (JNDI) name in the source and import it into the event sequencing
table (PERSISTENTLOCK) in the new deployment-environment-scoped common
database component. See your database provider documentation for instructions
for extracting data from a table in one database and importing it
into another database.

You
are not required to create the event sequencing and failed event tables
if you are using the old common database for the deployment-environment-scoped
common database.

3 To create the messaging enginetables, complete the following steps:
    1. If you are reusing your previous messaging engine database and
schema, manually drop the existing messaging engine tables.Tip: The messaging engine table names use the SIB prefix.
    2. Run the createSchema\_Messaging.sql file to
re-create the tables manually on the database where you want to configure
Messaging. This file is in deployment\_manager\_profile/dbscripts/Upgrade/cell\_name.de\_name/database\_type/Messaging\_engine\_database\_name.Messaging\_engine\_schema\_name.
2 For Process and Performance Data Warehousedatabases, complete the following steps for your DB2 for z/OS database:

1 To ensure that you can successfully run the SQL scriptsfor the DB2® for z/OS® schema upgrade, alter the following tablespaces to increase the buffer pool size to 8K: To do so, drop the table spaces and create them again with 8kbuffer pools.Note: You should move the data to a temporary table spacebefore dropping it. Then, copy it back when you re-create the tablespace. Example SQL to re-create table spaces:SET CURRENT SQLID = 'ZASIPS';DROP TABLESPACE ZACELLDB.WLPT33;DROP TABLESPACE ZACELLDB.WLPT52;CREATE TABLESPACE WLPT33IN ZACELLDBUSING STOGROUP ZADBSTOSEGSIZE 32LOCKMAX SYSTEMLOCKSIZE ROWDEFINE YESCCSID UNICODEBUFFERPOOL BP8K1;CREATE TABLESPACE WLPT52IN ZACELLDBUSING STOGROUP ZADBSTOSEGSIZE 32LOCKMAX SYSTEMLOCKSIZE ROWDEFINE YESCCSID UNICODEBUFFERPOOL BP8K1;
    - WLPT33
    - WLPT34
    - WLPT52
    - WLPT53
    - WLPT134
    - WLPT145

```
SET CURRENT SQLID = 'ZASIPS';

DROP TABLESPACE ZACELLDB.WLPT33;
DROP TABLESPACE ZACELLDB.WLPT52;

CREATE TABLESPACE WLPT33
IN ZACELLDB
USING STOGROUP ZADBSTO
SEGSIZE 32
LOCKMAX SYSTEM
LOCKSIZE ROW
DEFINE YES
CCSID UNICODE
BUFFERPOOL BP8K1;

CREATE TABLESPACE WLPT52
IN ZACELLDB
USING STOGROUP ZADBSTO
SEGSIZE 32
LOCKMAX SYSTEM
LOCKSIZE ROW
DEFINE YES
CCSID UNICODE
BUFFERPOOL BP8K1;
```

2. From the target\_deployment\_manager\_profile/dbscripts/Upgrade/cell\_name.de\_name/database\_type/ProcessServer\_database\_name directory,
obtain the upgradeSchema\_ProcessServer.sql script
that corresponds to the product version that you are migrating from. 
For example, if you are migrating from IBM Business Process Manager
 V7.5.x,
copy the script named upgradeSchema751\_ProcessServer.sql to
your working directory. Connect to the DB2 for z/OS database, and run the upgradeSchema75x\_ProcessServer.sql or upgradeSchema8xx\_ProcessServer.sql script
against the database by using your preferred tool. Then, run the newly
created createProcedure\_ProcessServer.sql script
to create the stored procedures.
You can safely ignore SQL
errors about creating duplicate indexes.
You can safely ignore
SQL errors with text similar to the following text: ROW NOT
FOUND FOR FETCH, UPDATE, OR DELETE, OR THE RESULT OF A QUERY IS AN
EMPTY TABLE. SQLCODE=100, SQLSTATE=02000, DRIVER=3.61.96 for
the following SQL statement:UPDATE LSW\_BPD\_INSTANCE SET ATTACHMENT\_STORE = 3  WHERE BPD\_INSTANCE\_ID IN (SELECT DISTINCT  BPD\_INSTANCE\_ID FROM LSW\_BPD\_INSTANCE\_DOCUMENTS)
UPDATE LSW\_BPD\_INSTANCE SET  CASE\_FOLDER\_SERVER\_NAME='IBM\_BPM\_ContentStore'  WHERE NOT CASE\_FOLDER\_ID IS NULL
UPDATE LSW\_BPD\_ACTIVITY\_INSTANCE SET ENABLDOC\_SERVER\_NAME='IBM\_BPM\_ContentStore'  WHERE NOT ENABLING\_DOCUMENT\_ID IS NULL
UPDATE LSW\_BPD\_INSTANCE SET  STARTING\_DOCUMENT\_SERVER\_NAME='IBM\_BPM\_ContentStore'  WHERE NOT STARTING\_DOCUMENT\_ID IS NULL
The
script is generated in deployment\_manager\_profile/dbscripts/Upgrade/deployment\_environment\_name/database\_type/database\_name.schema\_name.
3. From the target\_deployment\_manager\_profile/dbscripts/Upgrade/cell\_name.de\_name/database\_type/PDW\_database\_name directory,
obtain the upgradeSchema\_PerformanceDW.sql script
that corresponds to the product version that you are migrating from.
For example, if you are migrating from Business Automation Workflow V7.5.x,
copy the script named upgradeSchema751\_PerformanceDW.sql to
your working directory. Connect to the DB2 for z/OS database, and run the upgradeSchemaPerformancexxx\_PerformanceDW.sql script
against the database by using your preferred tool.
You can
safely ignore SQL errors about creating duplicate indexes.
4. Check the status of the table
spaces. When you run the upgradeSchemaxxx\_ProcessServer.sql script,
you might see the warning message SQL CODE -162,
indicating that the table space is under Check Pending status. Use
the following command to identify table spaces that are under Check
Pending status: -DISPLAY DATABASE(PS\_DB\_NAME) SPACENAM(*) RESTRICTTip: For improved performance, list the table spaces in AREO*
status and use REORG to fix them.
After each table space is
identified, the database administrator can use the CHECK DATA utility
to fix it.If
you are using DB2 on a z/OS system, run the following command: Command Prefix DISPLAY DATABASE(PS\_DB\_NAME) SPACENAM(*) RESTRICT
3 For updating the other databases, completethe following steps:

1. Ensure that the scripts have write
permissions. If the tool that you want to use to view, edit, and run
the scripts requires the scripts to be in EBCDIC format, rather than
ASCII format, convert the files to EBCDIC.  Important: After you convert the files from ASCII to EBCDIC,
check that no SQL statements exceed 72 characters in length, and fix
if necessary. Longer lines can lead to line truncation and invalid
statements when you run the scripts.
2 Connect to the database and runthe customized scripts against the database by using your preferredtool; for example, the DB2 command line processor, SPUFI, or in abatch job. You can also use one of these methods torun the scripts: To run the SQL scriptsdirectly, run the scripts in the following sequence: The options are embeddedin the SQL scripts. Additional options are not required. Note: Ifyou had the Business Process Choreographer Reporting function configured,it was removed during runtime migration. However, the associated datawas not automatically removed from the database. If you determinethat you no longer need this data, run the dropSchema\_Observer.sql scriptand then the dropTablespace\_Observer.sql script usingan SQL session with special configuration.
    - Run the SQL scripts using the upgradeSchema.sh file
that was generated along with the SQL scripts.
    - Run the SQL scripts directly using an SQL session.
    - Run all upgradeTablespac* scripts before
you run any upgradeSchema* scripts.
    - Run the upgradSchema\_SchemaStatus.sql script
before you run any other "upgradeSchema*" SQL scripts.

The options are embedded
in the SQL scripts. Additional options are not required.

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
5. Go to the target\_install\_root/util/dbUpgrade  directory and set the database.is.db2zos property
to true in the upgrade.properties file. 
 For example:database.is.db2zos=true
6 To upgrade the databases to 24.x , run theDBUpgrade utility on the server in the target environment. Important: Ensure that your deployment manager and all the managed nodes in the sourceenvironment have been stopped before running this utility. install\_root /bin/DBUpgrade.sh -propertiesFile target\_migration\_properties\_file -backupFolder snapshot\_folder where: Forexample:install\_root /bin/DBUpgrade.sh -propertiesFile /opt/BPM24.x /util/migration/resources/target\_migration.properties -backupFolder /tmp/snapshot The command displays each database upgrade action as it runs. After all the upgrades arefinished, you see a message similar to the following message:All upgrade steps have been completed successfully. The log location is listed in the output. If there are errors or exceptions, they appear in thelog. If you are migrating from IBM Business Process Manager V7.5.x and you get anout-of-memory error indicating too many or too large data records, you can try to increase the heapsize of the JVM for the DBUpgrade command. Open theDBUpgrade.sh file in install\_root /bin and find -Xmx2048m in this file. It indicates that the maximum JVM heap size is2048 megabytes. You can increase this value to update the heap size. If necessary for troubleshooting, you can run DBUpgrade -generateSQLOnly togenerate the SQL files without running them. You can then edit the generated SQL files manually andrun DBUpgrade -omitSQLGeneration to upgrade the database using the modifiedfiles.

```
install\_root/bin/DBUpgrade.sh -propertiesFile target\_migration\_properties\_file -backupFolder snapshot\_folder
```

- target\_migration\_properties\_file is the full path to the
migration properties file in which you specified the configuration information for the target
environment.
- snapshot\_folder is the directory that contains the information that was
extracted from the source environment

```
install\_root/bin/DBUpgrade.sh -propertiesFile /opt/BPM24.x/util/migration/resources/target\_migration.properties -backupFolder /tmp/snapshot
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