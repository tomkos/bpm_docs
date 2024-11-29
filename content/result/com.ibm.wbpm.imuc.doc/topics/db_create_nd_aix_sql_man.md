# Creating SQL Server databases (deprecated)

## Before you begin

- You cannot share databases across multiple deployment environments.
- The Process and Performance Data Warehouse components require their own separate databases and
cannot be configured on the same database as the other IBM Business Automation Workflow components.
- The Process and Performance Data Warehouse components require the databases to be case
insensitive for SQL Server.
- The CommonDB (and legacy WebSphere® Process
Server) components
require the databases to be case sensitive for SQL Server.
- The user who creates the databases cannot be the same user that
you plan to assign as the login user for accessing the databases.
If you deviate from this requirement, the default schema dbo will
be used.
- The schema name used for each component should match the user.

## About this task

- If the Create Tables option is selected, database tables are
automatically created at the same time as the deployment environment. Therefore, empty databases
must exist before you run the Deployment Environment wizard.
- If the Create Tables option is not selected, database table creation is
deferred when you create the deployment environment. Therefore, you can create the databases either
before or after you run the Deployment Environment wizard. You might find it useful to create the
databases after running the wizard because you can use the set of populated scripts, which the
wizard generates, to create the databases and database tables at a time that you choose.

The default database names are BPMDB for the Process database,
PDWDB for the Performance Data Warehouse database, CMNDB for the Common database, and CPEDB for the
Content database. For details about databases and schemas, see Planning the number of databases.

In an AdvancedOnly
deployment environment, you
need only the Common database. For both Advanced
deployment environment and AdvancedOnly
deployment environment, the Common database has two parts: one is scoped to
the cell and the other is scoped to the deployment environment. Both parts can be defined to use
CMNDB (which is the default) or they can use separate databases.

- Creating the databases before creating profiles or the deployment environment
- Creating the databases after creating the profiles and the deployment environment

## Creating the databases before creating profiles or the deployment
environment

To create the databases before you
create the profiles or before you use the Deployment Environment wizard to create your deployment
environment, you can use the createDatabase\_CaseInsensitive.sql and
createDatabase\_CaseSensitive.sql templates that are provided with your IBM Business Automation Workflow installation.

### Procedure

Complete the following steps for each database
that you want to create:

1. Navigate to the
BPM\_HOME/BPM/dbscripts/SQLServer/Create directory and make
two copies of the createDatabase\_CaseInsensitive.sql file and one copy of the
createDatabase\_CaseSensitive.sql file.
2 Complete the following substeps to create theProcess database:
    1. In the first copy of the createDatabase\_CaseInsensitive.sql file,
replace @DB\_NAME@ with the name that you want to use for the Process database.
Save the file.
    2. Create the database by running the following command on your local or remote database
server. For example: 
sqlcmd -i createDatabase\_CaseInsensitive.sql
3 Complete the following substeps to create thePerformance Data Warehouse database:

1. In the second copy of the createDatabase\_CaseInsensitive.sql
file, replace @DB\_NAME@ with the name that you want to use for the Performance
Data Warehouse database. Save the file.
2. Create the database by running the following command on your local or remote database
server. For example: 
sqlcmd -i createDatabase\_CaseInsensitive.sql
4 Complete the following substeps to create theCommon database:

1. In the copied createDatabase\_CaseSensitive.sql file, replace
@DB\_NAME@ with the name that you want to use for the Common database. Save the
file.
2. Create the database by running the following command on your local or remote database
server. For example: 
sqlcmd -i createDatabase\_CaseSensitive.sql
5 Complete the following substeps to create the Content database (CPEDB) andmanually create the table spaces for it.

1 Copy theinstall\_root /BPM/dbscripts/SQLServer/Create/createDatabase\_ECM.sql file to your working directory.
    - Replace @DB\_NAME@ with the name that you want to use for the database (such as CPEDB).
    - Replace @DB\_DIR@ with your SQL Server home directory.
    - Replace @DOS\_SCHEMA@ with the DOS schema value you choose, such as DOS. Later, you must enter
this DOS schema value in the Design Object Store database schema name field on the
Configure databases page of the Deployment Environment wizard.
    - Replace @TOS\_SCHEMA@ with the TOS schema value you choose, such as TOS. Later, you must enter
this TOS schema value in the Target Object Store database schema name field on the
Configure databases page of the Deployment Environment wizard.
    - Run the following command to create the Content
database:createDatabase\_ECM.sql
2. Follow the instructions in Creating users and schema for SQL Server databases in a network environment on AIX to create one login and
a user with the same name (such as sqluser) for each database.
Later, you must enter this name on the Configure databases page of the Deployment Environment
wizard.
3 Create the three required schema files. Copy theinstall\_root /BPM/dbscripts/SQLServer/Create/createSchema\_ECM.sql file to three files in your working directory. Name them createSchema\_DOS.sql (for the Design Object Store), createSchema\_TOS.sql (for the Target ObjectStore), and createSchema\_ICN.sql (for IBM ContentNavigator ). Later, you must enter theseschema names on the Configure databases page of the Deployment Environment wizard. In createSchema\_DOS.sql : In createSchema\_TOS.sql : In createSchema\_ICN.sql :

- Replace @SCHEMA@ with the DOS schema value you chose in substep a.
- Replace @ECMClient\_DBUSER@ with the user name you created in substep b.

- Replace @SCHEMA@ with the TOS schema value you chose in substep a.
- Replace @ECMClient\_DBUSER@ with the user name you created in substep b.

- Replace @SCHEMA@ with the IBM Content
Navigator schema value you choose, such as
ICN.
- Replace @ECMClient\_DBUSER@ with the user name you created in substep b.
4. Run the following commands:

createSchema\_DOS.sql
createSchema\_TOS.sql
createSchema\_ICN.sqlChange
the schema owner for the three schemas to the user you created instead of the default user (dbo).
Open the SQL Server Management Studio and right-click each schema name. On the General tab, click
Search for the Schema owner and choose the user name.

## Creating the databases after creating the profiles and the
deployment environment

After you create the profiles, you can use
the Deployment Environment wizard to create the deployment environment and generate the database
scripts. The scripts are populated with the configuration values that you specified in the wizard.
You can use some of these scripts to create the databases if you chose to defer the creation of the
database tables.

### Before you begin

You must have already used the Profile
Management Tool, the BPMConfig command, or the manageprofiles utility
to create and augment the profiles. You must also have used the Deployment
Environment wizard to configure the deployment environment.

### Procedure

1 On the computer where you created thedeployment manager profile, navigate to one or more of the following default subdirectories wherethe SQL database scripts were generated: These directories contain the createDatabase.sql andcreateDatabase\_ECM.sql scripts that you can use to create the databases. The number of subdirectories that are generated is dependent on thedeployment environment type and the number of databases that were configured in the DeploymentEnvironment wizard.
    - dmgr\_profile\_root/dbscripts/cell\_name/SQLServer/CMNDB/schema\_name
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/SQLServer/CMNDB/schema\_name
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/SQLServer/BPMDB/schema\_name
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/SQLServer/PDWDB/schema\_name
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/SQLServer/CPEDB/schema\_name

These directories contain the createDatabase.sql and
createDatabase\_ECM.sql scripts that you can use to create the databases.

The number of subdirectories that are generated is dependent on the
deployment environment type and the number of databases that were configured in the Deployment
Environment wizard.

2. For each createDatabase.sql file that was generated, run the following
command on your local or remote database server to create the Common database (CMNDB), Process
database (BPMDB), and Performance Data Warehouse database (PDWDB):

sqlcmd -i createDatabase.sql

Note: The CMNDB database only needs to be created once, which means that you
only need to run the command in one of the two CMNDB output directory paths.
3 For the Content database, create three copies of the createUser.sql fileand name them: createUser\_DOS.sqlcreateUser\_TOS.sqlcreateUser\_ICN.sql In thecreateUser\_DOS.sql and createUser\_TOS.sql files, uncommentthe followinglines:--EXEC sp\_addrolemember 'db\_securityadmin', @DB\_USER@;--EXEC sp\_addsrvrolemember @DB\_USER@, 'bulkadmin'; byremoving the dashes:EXEC sp\_addrolemember 'db\_securityadmin', @DB\_USER@;EXEC sp\_addsrvrolemember @DB\_USER@, 'bulkadmin'; Tips: To create the Content database, run the following commands on your local or remote databaseserver:createDatabase\_ECM.sqlcreateUser\_DOS.sqlcreateUser\_TOS.sqlcreateUser\_ICN.sqlcreateSchema\_ECM\_DOS.sqlcreateSchema\_ECM\_TOS.sqlcreateSchema\_ICN.sql Changethe schema owner for the three schemas to the user you created instead of the default user (dbo).Open the SQL Server Management Studio and right-click each schema name. On the General tab, clickSearch for the Schema owner and choose the user name.

```
createUser\_DOS.sql
createUser\_TOS.sql
createUser\_ICN.sql
```

```
--EXEC sp\_addrolemember 'db\_securityadmin', @DB\_USER@;
--EXEC sp\_addsrvrolemember @DB\_USER@, 'bulkadmin';
```

```
EXEC sp\_addrolemember 'db\_securityadmin', @DB\_USER@;
EXEC sp\_addsrvrolemember @DB\_USER@, 'bulkadmin';
```

- In some Content database scripts, there is a @DB\_DIR@ variable that should be replaced manually.
- If you are using the same login user or database user for the ICN, DOS, and TOS databases,
modify the SQL scripts to avoid SQL errors about creating duplicate login users or database
users.

```
createDatabase\_ECM.sql
createUser\_DOS.sql
createUser\_TOS.sql
createUser\_ICN.sql
createSchema\_ECM\_DOS.sql
createSchema\_ECM\_TOS.sql
createSchema\_ICN.sql
```