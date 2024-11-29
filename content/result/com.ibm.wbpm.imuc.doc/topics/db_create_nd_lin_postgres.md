# Creating PostgreSQL
databases

## Before you begin

Be aware of the following limitations.

- IBM Business Automation Workflow with
PostgreSQL supports only
standard functions. Advanced functions are not supported.
- For IBM Business Automation Workflow with
PostgreSQL,  Business Automation Workflow is required to share
a file storage between all nodes. For example, you can configure NFS file share and make it
accessible on all IBM Business Automation Workflow node machines.
- You cannot share databases across multiple deployment environments.
- The Process and Performance Data Warehouse components require their own separate databases and
cannot be configured on the same database as the other IBM Business Automation Workflow components.
- Ensure that the schema name that is used for each component matches the user.
- Ensure that all the database-related names for the BPMConfig command are
lowercase. Otherwise, you receive a validation error when you run the command.
- High-Availability Data Replication (HADR) is not fully supported for Traditional Business Automation Workflow with PostgreSQL. The transaction logs
cannot be stored in the PostgreSQL database, so supporting
High Availability (HA) requires a shared file system to host the transaction logs, which must be
configured manually. There is no good Data Replication (DR) solution for this topology on public
cloud. For example, on Azure cloud, The transaction log and service integration bus are in files and
are replicated to the DR site by the Azure file system. The rest of the data is in the database and
is replicated to the DR site by the Azure database system. There is no way to guarantee consistency
between the replications. The transaction log, service integration bus, and database might get out
of sync and cause errors, even resulting in unable to start the DR server.
- Use the latest PostgreSQL JDBC driver and make sure
the PostgreSQL database is
configured correctly for the customer workload. Adjust the following parameters in the
postgresql.conf file of the database server: 
Table 1. PostgreSQL parameters

Parameter
Setting
Description

shared\_buffers
minimum 1024 MB
The normal PostgreSQL performance tuning recommendation is to use about 25% of the memory for the shared buffer.
Adjustments to the Linux® kernel configuration might also be
required; check the PostgreSQL tuning guides.

work\_mem
minimum 20 MB
This parameter applies to each session, and many user sessions can cause large memory usage.
This memory is critical because it is used for sort operations. If the value is set too low, the
running time can increase significantly (over an hour for toolkit deployments, for example).

max\_prepared\_transactions
for example, 200
This value must be at least as large as the max\_connections setting.

max\_wal\_size
for example, 6 GB
For larger workloads, the default value must be increased. If an increase is required, you
can find advice in the PostgreSQL server log files.

log\_min\_duration\_statement
for example, 5000
It is optional to set this parameter. It allows for additional logging of statements that
exceed the specified running time in milliseconds (which corresponds to 5 seconds in this example)
to identify bottlenecks and tuning areas.

## About this task

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

The default database names are bpmdb for the Process database, pdwdb
for the Performance Data Warehouse database, and cpedb for the Content database. For more
information about databases and schemas, see Planning the number of databases.

- Creating the databases before creating the profiles and configuring the deployment environment
- Creating the databases after creating the profiles and configuring the deployment environment

## Creating the databases before creating the profiles and configuring the deployment
environment

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

| Parameter                  | Setting           | Description                                                                                                                                                                                                                                                                                |
|----------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| shared\_buffers             | minimum 1024 MB   | The normal PostgreSQL performance tuning recommendation is to use about 25% of the memory for the shared buffer. Adjustments to the Linux kernel configuration might also be required; check the PostgreSQL tuning guides.                                                                 |
| work\_mem                   | minimum 20 MB     | This parameter applies to each session, and many user sessions can cause large memory usage. This memory is critical because it is used for sort operations. If the value is set too low, the running time can increase significantly (over an hour for toolkit deployments, for example). |
| max\_prepared\_transactions  | for example, 200  | This value must be at least as large as the max\_connections setting.                                                                                                                                                                                                                       |
| max\_wal\_size               | for example, 6 GB | For larger workloads, the default value must be increased. If an increase is required, you can find advice in the PostgreSQL server log files.                                                                                                                                             |
| log\_min\_duration\_statement | for example, 5000 | It is optional to set this parameter. It allows for additional logging of statements that exceed the specified running time in milliseconds (which corresponds to 5 seconds in this example) to identify bottlenecks and tuning areas.                                                     |

### Procedure

1. On the computer where you installed IBM Business Automation Workflow, navigate to the following directory where
the sample configuration properties files are stored: 
install\_root/BPM/samples/config
2 Find the sample properties file that most closely represents your target deployment environmentand make a copy of this file. Only the Standard deployment environment is supported for PostgreSQL . Ininstall\_root /BPM/samples/config , you can find astandard folder with a set of sample properties files. Within the folder is aset of files that are specific to the Standard deployment environment. The sample propertiesfiles are named according to the following format:de\_type [-environment\_type ]-topology -PostgreSQL[-suffix ] . For example, the sample configuration properties file for configuring a Standard deployment environment with Workflow Center and a single clustertopology that uses a PostgreSQL database is namedStandard-PC-SingleCluster-PostgreSQL.properties .
    - de\_type is set to Standard.
    - environment\_type can be set to PS for Workflow Server or
PC for Workflow Center.
    - topology can be set to SingleCluster or
ThreeClusters.
3 Edit the copied properties file and update the values as requiredto reflect your profile, deployment environment, and database configuration. When you modify the sample properties file, use the guidance that is provided within the filefor specifying values.Tip: You must use this same properties file later when you run theBPMConfig command to create your profiles and deployment environment. Additional considerations: For more information about the available properties, see the BPMConfig command-line utility topic and the descriptions in the Configuration properties for the BPMConfig command topic.

- Your modified properties file must use UTF-8 encoding.
- If you want to automatically create your database tables when you run the
BPMConfig command later to create profiles and configure your deployment
environment, set the bpm.de.deferSchemaCreation property to
false.
- Do not add any custom properties to this file when you perform your modifications or the
BPMConfig command might fail when it is run.
- If you need to use a backslash character (\) in your properties file, when you specify path
names or passwords, you must use an escape backslash before it. For example, bpm.dmgr.installPath=c:\\IBM\\BPM85.

For more information about the available properties, see the BPMConfig command-line utility
topic and the descriptions in the Configuration properties for the BPMConfig command topic.

4 Run the BPMConfig command on the computer where IBM Business Automation Workflow is installed, passingit the name of the properties file that you created. For example,:install\_root /bin/BPMConfig -create -sqlfiles directory\_path /my\_environment.properties -outputDir /my\_bpmscripts\_dir Inthis syntax,directory\_path /my\_environment .properties is the location and name of your customized properties file, andmy\_bpmscripts\_dir is the directory where you want togenerate the database scripts. The generated scripts include the filecreateDatabase.sql , which can be used to create the databases. The files aregenerated into the following default locations: The number of subdirectories that are generated depends on the number of databases thatwere defined in the properties file.Note: These scripts are overwritten if you run theBPMConfig command again.

```
install\_root/bin/BPMConfig -create -sqlfiles directory\_path/my\_environment.properties -outputDir /my\_bpmscripts\_dir
```

In
this syntax,
directory\_path/my\_environment.properties
is the location and name of your customized properties file, and
my\_bpmscripts\_dir is the directory where you want to
generate the database scripts.

- my\_bpmscripts\_dir/dbscripts/cell\_name.deployment\_environment\_name/PostgreSQL/bpmdb
- my\_bpmscripts\_dir/dbscripts/cell\_name.deployment\_environment\_name/PostgreSQL/pdwdb
- my\_bpmscripts\_dir/dbscripts/cell\_name.deployment\_environment\_name/PostgreSQL/cpedb
5. Before you create your database, you must create a user. To create a user, use the
following command: psql - U postgres
CREATE ROLE dbUserName PASSWORD ‘dbPassword’ SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;For
example:CREATE ROLE workflowadmin PASSWORD 'password' SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;
6. To create the Process database (bpmdb) and Performance Data Warehouse database (pdwdb), run the
following commands for each of them on your local or remote database server:

psql -U postgres -f createDatabase.sql
psql -U postgres -f createSchema.sql
7. If you want to use embedded Content Platform Engine and embedded IBM Content
Navigator (which means
in bpmconfig.properties, bpm.de.useExternalNavigator=false and
bpm.de.useExternalCPE=false), then the operations on cpedb include: 
chmod +x createDatabase\_ECM.sh
./createDatabase\_ECM.sh
psql -U postgres -f ./createTablespace\_Standard.sql
psql -U postgres -f ./createSchema\_ICN.sql
 
If you want to use external Content Platform Engine and embedded IBM Content
Navigator (which means
in bpmconfig.properties, bpm.de.useExternalNavigator=false
and bpm.de.useExternalCPE=true), then the operations on cpedb
include:psql -U postgres -f ./createDatabase.sql
psql -U postgres -f ./createSchema\_ICN.sql

## Creating the databases after creating the profiles and configuring the deployment
environment

When you run the BPMConfig
command with the -create -de parameters to create the profiles and configure
the network deployment environment, database scripts are generated that are populated with the
values from the properties file that you specified. You can use some of these scripts to create the
databases if you chose to defer the creation of the database tables.

### Before you begin

You must
have already run the BPMConfig command to create
the profiles and configure the network deployment environment.

| Parameter                  | Setting           | Description                                                                                                                                                                                                                                                                                |
|----------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| shared\_buffers             | minimum 1024 MB   | The normal PostgreSQL performance tuning recommendation is to use about 25% of the memory for the shared buffer. Adjustments to the Linux kernel configuration might also be required; check the PostgreSQL tuning guides.                                                                 |
| work\_mem                   | minimum 20 MB     | This parameter applies to each session, and many user sessions can cause large memory usage. This memory is critical because it is used for sort operations. If the value is set too low, the running time can increase significantly (over an hour for toolkit deployments, for example). |
| max\_prepared\_transactions  | for example, 200  | This value must be at least as large as the max\_connections setting.                                                                                                                                                                                                                       |
| max\_wal\_size               | for example, 6 GB | For larger workloads, the default value must be increased. If an increase is required, you can find advice in the PostgreSQL server log files.                                                                                                                                             |
| log\_min\_duration\_statement | for example, 5000 | It is optional to set this parameter. It allows for additional logging of statements that exceed the specified running time in milliseconds (which corresponds to 5 seconds in this example) to identify bottlenecks and tuning areas.                                                     |

### Procedure

1 On the computer where you created the deployment manager profile, go to one or more of thefollowing default subdirectories where the database scripts were generated: These directories contain the createDatabase.sql andcreateDatabase\_ECM.sql scripts that you can use to create the databases. The number of subdirectories that are generated depends on the number of databases that weredefined in the properties file.
    - my\_bpmscripts\_dir/dbscripts/cell\_name.deployment\_environment\_name/PostgreSQL/bpmdb
    - my\_bpmscripts\_dir/dbscripts/cell\_name.deployment\_environment\_name/PostgreSQL/pdwdb
    - my\_bpmscripts\_dir/dbscripts/cell\_name.deployment\_environment\_name/PostgreSQL/cpedb

These directories contain the createDatabase.sql and
createDatabase\_ECM.sql scripts that you can use to create the databases.

The number of subdirectories that are generated depends on the number of databases that were
defined in the properties file.

2. Before you create your database, you must create a user. To create a user, use the
following
command: psql - U postgresCREATE ROLE dbUserName PASSWORD ‘dbPassword’ SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;for
example
:CREATE ROLE workflowadmin PASSWORD 'password' SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;
3. For each createDatabase.sql file that was generated, run the following
commands on your local or remote database server to create the Process database (bpmdb) and
Performance Data Warehouse database (pdwdb):

psql -U postgres -f createDatabase.sql
psql -U postgres -f createSchema.sql
4 If you want to use embedded Content Platform Engine and embedded IBM ContentNavigator (which meansin bpmconfig.properties , bpm.de.useExternalNavigator=false and bpm.de.useExternalCPE=false ), then the operations on cpedb include: chmod +x createDatabase\_ECM.sh./createDatabase\_ECM.shpsql -U postgres -f ./createTablespace\_Standard.sqlpsql -U postgres -f ./createSchema\_ICN.sql If you want to use external Content Platform Engine and embedded IBM ContentNavigator (which meansin bpmconfig.properties , bpm.de.useExternalNavigator=false and bpm.de.useExternalCPE=true ), then the operations on cpedbinclude:psql -U postgres -f ./createDatabase.sqlpsql -U postgres -f ./createSchema\_ICN.sql Note: If you set bpm.de.deferSchemaCreation=true , connect to your databasesbefore you run createXXX\_Standard.sql . For example,\c xxxdbSET ROLE xxx; Note: The order of execution of .sql files for bpmdb and pdwdb is:

```
chmod +x createDatabase\_ECM.sh
./createDatabase\_ECM.sh
psql -U postgres -f ./createTablespace\_Standard.sql
psql -U postgres -f ./createSchema\_ICN.sql
```

```
psql -U postgres -f ./createDatabase.sql
psql -U postgres -f ./createSchema\_ICN.sql
```

```
\c xxxdb
SET ROLE xxx;
```

- createDatabase.sql
- createSchema.sql
- createSchema\_Standard.sql
- createProcedure\_Standard.sqlNote: createProcedure\_Standard.sql
is for bpmdb only.