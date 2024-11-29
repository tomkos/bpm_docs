# Creating users for Oracle databases (deprecated)

You can create the users for Oracle databases
either before or after you create the profiles and the deployment environment. Create the cell-scoped user, the deployment environment-level user, the
Process database user, the Performance Data Warehouse user, and the three users for the Content
database: design object store user, target object store user, and IBM® Content
Navigator user.
The Process, Performance Data Warehouse, and Content database users are
not needed for an AdvancedOnly
deployment environment.

- If the Create Tables option is selected, database tables are
automatically created at the same time as the deployment environment. Therefore, the database users
must exist before you run the Deployment Environment wizard.
- If the Create Tables option is not selected, database table creation is
deferred when you create the deployment environment. Therefore, you can create the database users
either before or after you run the Deployment Environment wizard. You might find it useful to create
the database users after running the wizard because you can use the set of populated scripts, which
the wizard generates, to create the database users and database tables at a time that you
choose.

## Before you begin

For simplicity, the createUser.sql script, which is
used to create the users for Oracle databases, assigns more than the minimum required privileges to
an IBM Business Automation Workflow database user. The minimum
required privileges are listed in the Oracle database privileges topic. If you want
to specify a more fine-grained list of privileges, change the createUser.sql
script according to the privileges listed in that topic.

- Design object store (DOS)
- Target object store (TOS)
- IBM Content
Navigator (ICN)

| Tuning item      |   Minimum memory for initial settings (MB) |
|------------------|--------------------------------------------|
| Buffer cache     |                                       2048 |
| Shared pool size |                                       1024 |

Recommendations for database table space
settings:

On Oracle, IBM Business Automation
Workflow stores
large objects (LOBs) with the SECUREFILE option. For SECUREFILE, it
is recommended to use a table space with the AUTOALLOCATE option. If
you use UNIFORM SIZE extents, ensure that the UNIFORM SIZE is big
enough. Given the default block size of 8K, specify a UNIFORM SIZE
of at least 120K. Business Automation Workflow does
not explicitly prescribe the table space options; it relies on the
default Oracle settings (such as AUTOALLOCATE) to automatically manage
extents.

For new Business Automation Workflow installations,
create table spaces with the AUTOALLOCATE option.

For migrations, if you use table spaces with
a UNIFORM SIZE less than 120K, create new table spaces with the AUTOALLOCATE
option and make it the default table space for Business Automation Workflow database
schema users.

## About this task

The default database names are BPMDB for the Process database, PDWDB for the
Performance Data Warehouse database, CMNDB for the Common database, and CPEDB for the Content
database.  In the case of an Advanced
deployment environment or AdvancedOnly
deployment environment, the Common database has two parts: one is
scoped to the cell and the other is scoped to the deployment environment. Both parts can be defined
to use CMNDB (which is the default) or they can use separate databases. For details about databases
and schemas, see Planning the number of databases.

- Creating users for the databases before creating profiles or the deployment environment
- Creating users for the databases after creating the profiles and the deployment environment

## Related information

- Troubleshooting Oracle transaction recovery messages

## Creating users for the databases before creating profiles or
the deployment environment

To create the users for the databases
before you create the profiles or before you use the Deployment Environment wizard to create your
deployment environment, you can use the createUser.sql template that is
provided with your IBM Business Automation
Workflow
installation.

### Procedure

Complete the following steps for each database
user that you want to create:

1. Navigate to the
BPM\_HOME/BPM/dbscripts/Oracle/Create directory and make a
copy of the createUser.sql file.
2. In the copied file, replace
@DB\_USER@ with the user name that you want to use for the database and replace
@DB\_PASSWD@ with the user password. Save the file.
3. Create the database user by running the following
command on your local or remote database server: 
sqlplus oracle\_user\_ID/oracle\_password@db\_name @createUser.sql
4 This step and its substeps are for Linux only. Manually create the table spaces for theContent database. Tip: In some Content database scripts, there is a @DB\_DIR@ variable that should bereplaced manually. Use the backslash ("\") to replace the forward slash as the file separator.
    1 If you plan to use the embedded Content Platform Engine during deploymentenvironment creation, copy theinstall\_root /BPM/dbscripts/Oracle/Create/createUserTablespace\_ECM.sql file to two files in your working directory. Name themcreateUserTablespace\_ECM\_DOS.sql (for the Design Object Store) and createUserTablespace\_ECM\_TOS.sql (for the Target ObjectStore). Update and run the two new files to create the table spaces.IncreateUserTablespace\_ECM\_DOS.sql : In createUserTablespace\_ECM\_TOS.sql :
        - Replace @DB\_DIR@ with your Oracle instance home directory.
        - Replace @DB\_NAME@ with the name that you want to use for the database (such as orcl), @DB\_USER@
with the user name, and @DB\_PASSWD@ with the password for that user. Later, you must enter these
values on the Configure databases page of the Deployment Environment wizard.
        - Replace @ECM\_DATA\_TS@ with DOSDATTS. Later, you must enter this value on the Configure databases
page of the Deployment Environment wizard.
        - Run:sqlplus oracle\_user\_ID/oracle\_password@db\_name @createUserTablespace\_ECM\_DOS.sql
        - Replace @DB\_DIR@ with your Oracle instance home directory.
        - Replace @DB\_NAME@ with the name that you want to use for the database (such as orcl), @DB\_USER@
with the user name, and @DB\_PASSWD@ with the password for that user. Later, you must enter these
values on the Configure databases page of the Deployment Environment wizard.
        - Replace @ECM\_DATA\_TS@ with TOSDATTS. Later, you must enter this value on the Configure databases
page of the Deployment Environment wizard.
        - Run:sqlplus oracle\_user\_ID/oracle\_password@db\_name @createUserTablespace\_ECM\_TOS.sql
2. Whether you plan to use an embedded or an external Content Platform Engine during deployment
environment creation, copy the
install\_root/BPM/dbscripts/Oracle/Create/createUser.sql file
to your working directory. Name it createUser\_ICN.sql

To create one user for IBM Content
Navigator,
run:sqlplus oracle\_user\_ID/oracle\_password@db\_name @createUser\_ICN.sql
3 Whether you plan to use an embedded or an external Content Platform Engine during deploymentenvironment creation, copy theinstall\_root /BPM/dbscripts/Oracle/Create/createTablespace\_ICN.sql file to your working directory. Update and run the file to create the IBM ContentNavigator table spaces. Remember the valuesbecause you will use them later on the Configure databases page of the Deployment Environmentwizard.
    - Replace @DB\_USER@ with the user name that you want to use and replace @DB\_NAME@ with the name
that you want to use for the database (such as orcl).
    - Replace the table space name @ECMClient\_TBLSPACE@ with ICNTS.
    - Run:sqlplus oracle\_user\_ID/oracle\_password@db\_name @createTablespace\_ICN.sql
5. This step is for AIX only. Manually create the table spaces for the Content database by running the
createUserTablespace\_ECM.sql script that is in each of the
DOS\_user and
TOS\_user folders. Also run the
createUser.sql script and the
createTablespace\_Advanced.sql,
createTablespace\_Standard.sql, or
createTablespace\_Express.sql script that is in the
ICN\_user folder.

## Creating users for the databases after creating the profiles
and the deployment environment

After you create the profiles, you can
use the Deployment Environment wizard to create the deployment environment and generate the database
scripts. The scripts are populated with the configuration values that you specified in the wizard.
You can use some of these scripts to create the users for the databases if you chose to defer the
creation of the database tables.

### Before you begin

You must have already used the Profile
Management Tool, the BPMConfig command, or the manageprofiles utility
to create and augment the profiles. You must also have used the Deployment
Environment wizard to configure the deployment environment.

### Procedure

1 On the computer where you created thedeployment manager profile, navigate to one or more of the following default subdirectories wherethe SQL database scripts were generated: These directories contain the createUser.sql scripts that you can use tocreate the users for the databases. The number of subdirectories that are generated is dependent on thedeployment environment type and the number of database users that were configured in the DeploymentEnvironment wizard.
    - dmgr\_profile\_root/dbscripts/cell\_name/Oracle/oracle\_instance\_name/cell\_user
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/Oracle/oracle\_instance\_name/CMN\_user
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/Oracle/oracle\_instance\_name/PS\_user
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/Oracle/oracle\_instance\_name/PDW\_user
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/Oracle/oracle\_instance\_name/DOS\_user
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/Oracle/oracle\_instance\_name/TOS\_user
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/Oracle/oracle\_instance\_name/ICN\_user

These directories contain the createUser.sql scripts that you can use to
create the users for the databases.

The number of subdirectories that are generated is dependent on the
deployment environment type and the number of database users that were configured in the Deployment
Environment wizard.

2. For each createUser.sql file
that was generated, run the following command on your local or remote database server: 
  sqlplus oracle\_user\_ID/oracle\_password@oracle\_instance\_name @createUser.sql schema\_user\_password

Note: Although you can specify the schema user password shown in the command syntax, you can
alternatively edit the createUser.sql script and replace the parameter
&1 with the schema user password and then run the script without specifying any
parameter.
3. This step is for Linux only. Manually create the table spaces for the Content database by running the
createUserTablespace\_ECM.sql script that is in each of the
DOS\_user and
TOS\_user folders. Also run the
createUser.sql script and the
createTablespace\_Advanced.sql,
createTablespace\_Standard.sql, or
createTablespace\_Express.sql script that is in the
ICN\_user folder. 
Tip: In some Content database scripts, there is a @DB\_DIR@ variable that should be
replaced manually.
4 This step is for AIX only. Manually create the table spaces for the Contentdatabase. Tip: In some Content database scripts, there is a @DB\_DIR@ variable that should bereplaced manually. Use the backslash ("\") to replace the forward slash as the file separator.

1 If you plan to use the embedded Content Platform Engine during deploymentenvironment creation, copy theinstall\_root /BPM/dbscripts/Oracle/Create/createUserTablespace\_ECM.sql file to two files in your working directory. Name themcreateUserTablespace\_ECM\_DOS.sql (for the Design Object Store) and createUserTablespace\_ECM\_TOS.sql (for the Target ObjectStore). Update and run the two new files to create the table spaces.IncreateUserTablespace\_ECM\_DOS.sql : In createUserTablespace\_ECM\_TOS.sql :
    - Replace @DB\_DIR@ with your Oracle instance home directory.
    - Replace @DB\_NAME@ with the name that you want to use for the database (such as orcl), @DB\_USER@
with the user name, and @DB\_PASSWD@ with the password for that user. Later, you must enter these
values on the Configure databases page of the Deployment Environment wizard.
    - Replace @ECM\_DATA\_TS@ with DOSDATTS. Later, you must enter this value on the Configure databases
page of the Deployment Environment wizard.
    - Run:sqlplus oracle\_user\_ID/oracle\_password@db\_name @createUserTablespace\_ECM\_DOS.sql
    - Replace @DB\_DIR@ with your Oracle instance home directory.
    - Replace @DB\_NAME@ with the name that you want to use for the database (such as orcl), @DB\_USER@
with the user name, and @DB\_PASSWD@ with the password for that user. Later, you must enter these
values on the Configure databases page of the Deployment Environment wizard.
    - Replace @ECM\_DATA\_TS@ with TOSDATTS. Later, you must enter this value on the Configure databases
page of the Deployment Environment wizard.
    - Run:sqlplus oracle\_user\_ID/oracle\_password@db\_name @createUserTablespace\_ECM\_TOS.sql
2. Whether you plan to use an embedded or an external Content Platform Engine during deployment
environment creation, copy the
install\_root/BPM/dbscripts/Oracle/Create/createUser.sql file
to your working directory. Name it createUser\_ICN.sql

To create one user for IBM Content
Navigator,
run:sqlplus oracle\_user\_ID/oracle\_password@db\_name @createUser\_ICN.sql
3 Whether you plan to use an embedded or an external Content Platform Engine during deploymentenvironment creation, copy theinstall\_root /BPM/dbscripts/Oracle/Create/createTablespace\_ICN.sql file to your working directory. Update and run the file to create the IBM ContentNavigator table spaces. Remember the valuesbecause you will use them later on the Configure databases page of the Deployment Environmentwizard.

- Replace @DB\_USER@ with the user name that you want to use and replace @DB\_NAME@ with the name
that you want to use for the database (such as orcl).
- Replace the table space name @ECMClient\_TBLSPACE@ with ICNTS.
- Run:sqlplus oracle\_user\_ID/oracle\_password@db\_name @createTablespace\_ICN.sql