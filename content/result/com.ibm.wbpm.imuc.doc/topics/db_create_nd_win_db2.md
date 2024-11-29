# Creating DB2 databases

You can create the required databases for IBM® Business Automation
Workflow either before or after you run the
BPMConfig command with the -create -de parameters to create
profiles and configure your deployment environment.

- If the property is set to false, database tables are automatically created when
you run the BPMConfig command to create the profiles and deployment environment.
Therefore, the empty databases must exist before you run the BPMConfig command.
- If the property is set to true, database table creation is deferred when you
run the BPMConfig command to create the profiles and deployment environment.
Therefore, you can create the databases either before or after running the command. You might find
it useful to create the databases after running the BPMConfig command because you
can use the set of populated scripts, which the command generates, to create the databases and
database tables at a time that you choose.
- If your PostgreSQL DB
server uses Certificate Authentication, you must set
bpm.de.deferSchemaCreation property to true in
bpmconfig.properties. You cannot run BPMConfig -validate -db
bpmconfig.properties to validate database connections. There is no place in
bpmconfig.properties to specify the location of certificates, hence the
BPMConfig command cannot be used to connect directly to PostgreSQL DB with client
authentication.

## About this task

The default database names are BPMDB for the Process database,
PDWDB for the Performance Data Warehouse database, CMNDB for the Common database, and CPEDB for the
Content database. For details about databases and schemas, see Planning the number of databases.

The Process and Performance Data Warehouse require their own separate databases and
cannot be configured on the same database as the other IBM Business Automation Workflow components.

In an AdvancedOnly
deployment environment, you
need only the Common database. For both Advanced
deployment environment and AdvancedOnly
deployment environment, the Common database has two parts: one is scoped to
the cell and the other is scoped to the deployment environment. Both parts can be defined to use
CMNDB (which is the default) or they can use separate databases.

- DB2\_DEFERRED\_PREPARE\_SEMANTICS
- DB2\_COMPATIBILITY\_VECTOR

```
db2set DB2\_DEFERRED\_PREPARE\_SEMANTICS=
db2set DB2\_COMPATIBILITY\_VECTOR=
db2stop                                                   
db2start
```

- Creating the databases before creating the profiles and configuring the deployment environment
- Creating the databases after creating the profiles and configuring the deployment environment

## Related tasks

- Configuring profiles and creating a network deployment environment using BPMConfig

## Creating the databases before creating the profiles and configuring
the deployment environment

To generate the database scripts that can be used by
the BPMConfig command to create and configure your databases, you can run
BPMConfig with the -create -sqlfiles parameters, and
additionally include the -outputDir parameter to specify a location for the
generated scripts. When you run the BPMConfig command with these parameters, it
generates the database scripts without configuring your environment.

### Before you begin

- Information about the database configuration that you are designing.This might be a document that describes the general purpose of thedatabase configuration supplied by the database administrator or solutionarchitect. Alternatively, it might be a description of required parametersand properties. This information must include:
    - The location of the databases
    - The user ID and password for authenticating to the database
- Information about how IBM Business Automation Workflow and
its components have been installed, the database software used, and
the properties required by that type of database.
- An understanding of the profiles that you plan to create, specifically,
the functional relationship between the profile types and the databases.
- Information about the topology pattern to be implemented, and
an understanding of how the database design fits into the pattern
that you plan to use.

### Procedure

1. On the computer where you installed IBM Business Automation Workflow, navigate to the following directory where
the sample configuration properties files are stored: 
install\_root\BPM\samples\config
2 Find the sample properties file that most closely represents your target deployment environmentand make a copy of this file. For each of the different product configurations, there is adifferent folder containing sample properties files. For example, for configuring an Advanced,AdvancedOnly, or Standard deployment environment, there is an advanced ,advancedonly , or standard folder containing a set ofsample properties files. Within each folder, there is a set of files that is specific to thedifferent database types and configuration environments. The sample properties files are namedaccording to the following format:de\_type [-environment\_type ]-topology -DB2 , where: For example, the sampleconfiguration properties file for configuring an Advanced deployment environment with Workflow Center and a single cluster topologyusing a DB2 database is named Advanced-PC-SingleCluster-DB2.properties .
    - de\_type can be set to
Advanced, AdvancedOnly, or
Standard.
    - environment\_type can be set to PS for Workflow Server or PC for Workflow Center. This variable is
not used if de\_type is AdvancedOnly.
    - topology can be set to
SingleCluster or ThreeClusters.
3 Edit the copied propertiesfile and update the values as required to reflect your profile, deployment environment, and databaseconfiguration. When modifying the sample properties file, use the guidance provided within the file forspecifying values.Tip: You should use this sameproperties file later when you run the BPMConfig command to create your profilesand deployment environment. Additional considerations: For more information about the available properties, see the BPMConfig command-line utility topic and the descriptions in the Configuration properties for the BPMConfig command topic.

- Your modified properties file must use UTF-8 encoding.
- If you want to automatically create your database tables when you
run the BPMConfig command later to create profiles and configure your deployment
environment, set the bpm.de.deferSchemaCreation property to
false.
- Do not add any custom properties to this file when you perform
your modifications or the BPMConfig command will fail when it is run.
- If you need to use a backslash character (\) in your properties file,
for instance when specifying path names or passwords, you must use an escape backslash before it.
For example: bpm.dmgr.installPath=c:\\IBM\\BPM85.
- If
you are configuring a three-cluster setup that is based on the Advanced or AdvancedOnly template,
and you want your deployment environment to include the optional Business Process Archive Manager,
include the properties file entries that are described in the topic Configuring Business Process Archive Manager.

For more information about the available properties, see the BPMConfig command-line utility topic and the descriptions in the Configuration properties for the BPMConfig command topic.

4 Run the BPMConfig command on thecomputer where IBM Business Automation Workflow is installed, passingit the name of the properties file that you created. Forexample:install\_root \bin\BPMConfig -create -sqlfiles directory\_path \my\_environment.properties -outputDir my\_bpmscripts\_dir Inthis syntax,directory\_path \my\_environment .properties is the location and name of your customized properties file, andmy\_bpmscripts\_dir is the directory where you want togenerate the database scripts. The generated scripts include a set of files namedcreateDatabase.sql , which can be used to create the databases. ThecreateDatabase.sql files are generated into the following default locations: The number of subdirectories that are generated is dependenton the deployment environment type and the number of databases that were defined in the propertiesfile. Note: These scripts areoverwritten if you run the BPMConfig command again.

```
install\_root\bin\BPMConfig -create -sqlfiles directory\_path\my\_environment.properties -outputDir my\_bpmscripts\_dir
```

In
this syntax,
directory\_path\my\_environment.properties
is the location and name of your customized properties file, and
my\_bpmscripts\_dir is the directory where you want to
generate the database scripts.

- my\_bpmscripts\_dir\dbscripts\cell\_name\DB2\CMNDB
- my\_bpmscripts\_dir\dbscripts\cell\_name.deployment\_environment\_name\DB2\CMNDB
- my\_bpmscripts\_dir\dbscripts\cell\_name.deployment\_environment\_name\DB2\BPMDB
- my\_bpmscripts\_dir\dbscripts\cell\_name.deployment\_environment\_name\DB2\PDWDB
- my\_bpmscripts\_dir\dbscripts\cell\_name.deployment\_environment\_name\DB2\CPEDB
5. For each createDatabase.sql file that was generated, run the following
command on your local or remote database server to create the Common database (CMNDB), Process
database (BPMDB), and Performance Data Warehouse database (PDWDB):

db2 -tvf createDatabase.sql
Note: The CMNDB database only needs to be created once, which means that you only need to run the
command in one of the two CMNDB subdirectories.
6 Create the Content database (CPEDB) and manually create the table spaces for it.

1 Run the following command to create the Content database: Tip: In some Content database scripts, there is a @DB\_DIR@ variable that should bereplaced manually. Use the backslash ("\") to replace the forward slash as the file separator. createDatabase\_ECM.bat Notes:

```
createDatabase\_ECM.bat
```

    - If you plan to use an external Content Platform Engine
instead of the embedded Content Platform Engine during
deployment environment creation, you need only the IBM Content
Navigator database and can run db2
-tvf createDatabase\_ICN.sql instead of createDatabase\_ECM.bat.
    - If you see the following error, shut down and restart
Db2.SQL1363W One or more of the parameters submitted for immediate modification
were not changed dynamically. For these configuration parameters, the database
must be shutdown and reactivated before the configuration parameter changes
become effective.
    - If you drop the Content database, you must manually remove the directories that were created for
it.
2. Manually create the table spaces for the Content database by running the
createTablespace\_Advanced.sql,
createTablespace\_Standard.sql, or
createTablespace\_Express.sql script.

db2 -tvf createTablespace\_DeType.sql
Tip: In some Content database scripts, there is a @DB\_DIR@ variable that should be
replaced manually. Use the backslash ("\") to replace the forward slash as the file separator.

## Creating the databases after creating the profiles and configuring
the deployment environment

When you run the BPMConfig
command with the -create -de parameters to create the profiles and configure
the network deployment environment, database scripts are generated that are populated with the
values from the properties file that you specified. You can use some of these scripts to create the
databases if you chose to defer the creation of the database tables.

### Before you begin

You must
have already run the BPMConfig command to create
the profiles and configure the network deployment environment.

### Procedure

1 On the computer where you created the deployment manager profile, navigate to one or moreof the following default subdirectories where the SQL database scripts were generated: These directories contain the createDatabase.sql andcreateDatabase\_ECM.sql scripts that you can use to create the databases. The number of subdirectories that are generated is dependent on the deployment environmenttype and the number of databases that were defined in the properties file.
    - dmgr\_profile\_root\dbscripts\cell\_name\DB2\CMNDB
    - dmgr\_profile\_root\dbscripts\cell\_name.deployment\_environment\_name\DB2\CMNDB
    - dmgr\_profile\_root\dbscripts\cell\_name.deployment\_environment\_name\DB2\BPMDB
    - dmgr\_profile\_root\dbscripts\cell\_name.deployment\_environment\_name\DB2\PDWDB
    - dmgr\_profile\_root\dbscripts\cell\_name.deployment\_environment\_name\DB2\CPEDB

These directories contain the createDatabase.sql and
createDatabase\_ECM.sql scripts that you can use to create the databases.

The number of subdirectories that are generated is dependent on the deployment environment
type and the number of databases that were defined in the properties file.

2. For each createDatabase.sql file that was generated, run the following
command on your local or remote database server to create the Common database (CMNDB), Process
database (BPMDB), and Performance Data Warehouse database (PDWDB):

db2 -tvf createDatabase.sql
Note: The CMNDB database only needs to be created once, which means that you only need to run the
command in one of the two CMNDB subdirectories.
3 Create the Content database (CPEDB) and manually create the table spaces for it.

1 Run the following command to create the Content database: Tip: In some Content database scripts, there is a @DB\_DIR@ variable that should bereplaced manually. Use the backslash ("\") to replace the forward slash as the file separator. createDatabase\_ECM.bat Notes:

```
createDatabase\_ECM.bat
```

    - If you plan to use an external Content Platform Engine
instead of the embedded Content Platform Engine during
deployment environment creation, you need only the IBM Content
Navigator database and can run db2
-tvf createDatabase\_ICN.sql instead of createDatabase\_ECM.bat.
    - If you see the following error, shut down and restart
Db2.SQL1363W One or more of the parameters submitted for immediate modification
were not changed dynamically. For these configuration parameters, the database
must be shutdown and reactivated before the configuration parameter changes
become effective.
    - If you drop the Content database, you must manually remove the directories that were created for
it.
2. Manually create the table spaces for the Content database by running the
createTablespace\_Advanced.sql,
createTablespace\_Standard.sql, or
createTablespace\_Express.sql script.

db2 -tvf createTablespace\_DeType.sql
Tip: In some Content database scripts, there is a @DB\_DIR@ variable that should be
replaced manually. Use the backslash ("\") to replace the forward slash as the file separator.