# Creating DB2 databases (deprecated)

You can create the required databases for IBM® Business Automation
Workflow either before or after you create the
profiles and the deployment environment.

- If the Create Tables option is selected, database tables are
automatically created at the same time as the deployment environment. Therefore, empty databases
must exist before you run the Deployment Environment wizard.
- If the Create Tables option is not selected, database table creation is
deferred when you create the deployment environment. Therefore, you can create the databases either
before or after you run the Deployment Environment wizard. You might find it useful to create the
databases after running the wizard because you can use the set of populated scripts, which the
wizard generates, to create the databases and database tables at a time that you choose.

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

- Creating the databases before creating profiles or the deployment environment
- Creating the databases after creating the profiles and the deployment environment

## Creating the databases before creating profiles or the deployment
environment

To create the databases before you create
the profiles or before you use the Deployment Environment wizard to create your deployment
environment, you can use the createDatabase.sql template that is provided with
your IBM Business Automation
Workflow installation.

### Procedure

Complete the following steps for each database that
you want to create:

1. Navigate to the
BPM\_HOME/BPM/dbscripts/DB2/Create directory and make a copy
of the createDatabase.sql file.
2. In the copied file, replace @DB\_NAME@ with the name that you want to use for
the database and replace @DB\_USER@ with the user name that you want to use for
the database. Save the file.
3. For each createDatabase.sql file that was generated, run the following
command on your local or remote database server to create the Common database (CMNDB), Process
database (BPMDB), and Performance Data Warehouse database (PDWDB):

db2 -tvf createDatabase.sql
Note: The CMNDB database only needs to be created once, which means that you only need to run the
command in one of the two CMNDB subdirectories.
4 Create the Content database (CPEDB) and manually create the table spaces for it. If you plan to use an external Content Platform Engine instead of the embeddedContent Platform Engine duringdeployment environment creation, you can skip this step.
    1 Update the database creations files with the correct values for yourenvironment. In the createDatabase\_ECM.sh file, replace the following variables: Replace @DB\_DIR@ with your Db2 instance homedirectory. Replace @DB\_NAME@ with the name that you want to use for the database(such as CPEDB). Replace @DOS\_SCHEMA@ with DOSSA and replace@TOS\_SCHEMA@ with TOSSA. Remember the name you chose for the database. You willenter it in the launchpad. In the createDatabase\_ECM.sql file, replace the following variables: Replace @DB\_DIR@ and @DB\_NAME@ with the same values as inthe previous file, and replace @DB\_USER@ with the user name.
        - @DB\_DIR@
        - @DB\_NAME@
        - @DOS\_SCHEMA@
        - @TOS\_SCHEMA@
        - @DB\_DIR@
        - @DB\_USER@
        - @DB\_NAME@
2 Run the createDatabase\_ECM.sh command to create the Contentdatabase. Notes:
    - If you see the following error, shut down and restart
Db2.SQL1363W One or more of the parameters submitted for immediate modification
were not changed dynamically. For these configuration parameters, the database
must be shutdown and reactivated before the configuration parameter changes
become effective.
    - If you drop the Content database, you must manually remove the directories that were created for
it.
3 Copy theinstall\_root \BPM\dbscripts\DB2\Create\createTablespace\_ECM.sql file to two files in your working directory. Name themcreateTablespace\_ECM\_DOS.sql (for the Design Object Store) andcreateTablespace\_ECM\_TOS.sql (for the Target Object Store). Update and run the two new files to create the table spaces.IncreateTablespace\_ECM\_DOS.sql : In createTablespace\_ECM\_TOS.sql :

- Replace @DB\_DIR@, @DB\_NAME@, and @DB\_USER@ with the names that you used in the previous files.
- Replace @SCHEMA@ with the DOS schema value you chose in substep a, such as
DOSSA. Later, you must enter this DOS schema value in the Design
Object Store database schema name field on the Configure databases page of the Deployment
Environment wizard.
- Replace the table spaces @ECM\_DATA\_TS@, @ECM\_IDX\_TS@, and @ECM\_LOB\_TS@ with DOSDATTS, DOSIDXTS,
and DOSLOBTS.
- Run:db2 -tvf createTablespace\_ECM\_DOS.sql

- Replace @DB\_DIR@, @DB\_NAME@, and @DB\_USER@ with the names that you used in the previous files.
- Replace @SCHEMA@ with the TOS schema value you chose in substep a, such as
TOSSA. Later, you must enter this TOS schema value in the Target
Object Store database schema name field on the Configure databases page of the Deployment
Environment wizard.
- Replace the table spaces @ECM\_DATA\_TS@, @ECM\_IDX\_TS@, and @ECM\_LOB\_TS@ with TOSDATTS, TOSIDXTS,
and TOSLOBTS.
- Run:db2 -tvf createTablespace\_ECM\_TOS.sql
5 Create the IBM ContentNavigator databaseand the table spaces for it. If you plan to use an external IBM ContentNavigator instead ofthe embedded IBM ContentNavigator duringdeployment environment creation, you can skip this step.

1. Create the database if you have not already done so.
Note: If you created a Content database in the previous step, do not create an IBM Content
Navigator database. You must create the
IBM Content
Navigator table spaces in the
Content database.
To create the database,
run:createDatabase\_ICN.sql
2 Update and run the file to create the IBM ContentNavigator table spaces.
    - Copy the install\_root/BPM/dbscripts/DB2/Create/createTablespace\_ICN.sql
file to your working directory.
    - Replace @ECMClient\_SCHEMA@ with the IBM Content
Navigator schema value you choose, such as
ICN. Later, you must enter this ICN schema value in the IBM Content
Navigator database schema name field
on the Configure databases page of the Deployment Environment wizard.
    - Replace @ECMClient\_TBLSPACE@ with ICNTS.
    - Run:db2 -tvf createTablespace\_ICN.sql

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

1 On the computer where you created the deploymentmanager profile, navigate to one or more of the following default subdirectories where the SQLdatabase scripts were generated: These directories contain the createDatabase.sql andcreateDatabase\_ECM.sql scripts that you can use to create the databases. The number of subdirectories that are generated is dependent on thedeployment environment type and the number of databases that were configured in the DeploymentEnvironment wizard.
    - dmgr\_profile\_root/dbscripts/cell\_name/DB2/CMNDB
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/DB2/CMNDB
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/DB2/BPMDB
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/DB2/PDWDB
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/DB2/CPEDB

These directories contain the createDatabase.sql and
createDatabase\_ECM.sql scripts that you can use to create the databases.

The number of subdirectories that are generated is dependent on the
deployment environment type and the number of databases that were configured in the Deployment
Environment wizard.

2. For each createDatabase.sql file that was generated, run the following
command on your local or remote database server to create the Common database (CMNDB), Process
database (BPMDB), and Performance Data Warehouse database (PDWDB):

db2 -tvf createDatabase.sql
Note: The CMNDB database only needs to be created once, which means that you only need to run the
command in one of the two CMNDB subdirectories.
3 Create the Content database (CPEDB) and manually create the table spaces for it.

1 Run the following command to create the Content database: Tip: In some Content database scripts, there is a @DB\_DIR@ variable that should bereplaced manually. createDatabase\_ECM.sh Notes:

```
createDatabase\_ECM.sh
```

    - If you plan to use an external Content Platform Engine
instead of the embedded Content Platform Engine during
deployment environment creation, you need only the IBM Content
Navigator database and can run db2
-tvf createDatabase\_ICN.sql instead of createDatabase\_ECM.sh.
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
replaced manually.