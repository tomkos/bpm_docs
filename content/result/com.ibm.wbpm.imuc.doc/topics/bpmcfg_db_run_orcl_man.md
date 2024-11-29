# Running the generated Oracle database scripts

## Before you begin

Before you begin this task, you must have
run the BPMConfig command or the Deployment Environment
wizard to generate the correct SQL scripts. You
also need to have created the required database users using the generated createUser.sql scripts.

If the bpm.de.deferSchemaCreation property
is set to false, or if you used the Deployment Environment
wizard and did not clear the Create Tables option,
the SQL scripts used to create the database tables are automatically
run when you create the deployment environment.

## About this task

- cell\_name - If you are configuring an Advanced
deployment environment or AdvancedOnly
deployment environment,
this folder contains the SQL files for the CommonDB database that is configured on the cell.
- cell\_name.deployment\_environment\_name - For
each deployment environment, this folder will contain the SQL files
that need to be run.

## Procedure

1 Locate thegenerated SQL scripts. A default configuration for an Advanced deployment environment with Oracle databases contains the following sub-foldersand SQL scripts: In this example, orcl is the Oracle instance, celluser is the cell-scoped user, cmnuser is thedeployment environment-level user, psuser is the Workflow Server user, and pdwuser is thePerformance Data Warehouse user.Note: The BPMDB ,PDWDB , and CPEDB folders for Process, Performance DataWarehouse, and Content databases are not generated for an AdvancedOnly deployment environment .
    - cell\_name
        - Oracle
            - orcl
                - celluser
                    - createSchema\_Advanced.sql
- cell\_name.deployment\_environment\_name

- Oracle
    - orcl
        - cmnuser
            - createSchema\_Advanced.sql
            - createSchema\_Messaging.sql
    - psuser
        - createSchema\_Advanced.sql
        - createProcedure\_Advanced.sql
- pdwuser
    - createSchema\_Advanced.sql
- cpeuser

- createSchema\_Advanced.sql
2. Run the scripts to
apply the schema to the CMNDB.
For
example, use the following commands to run the scripts manually for
a cell-scoped Common database configuration: sqlplus celluser/cellpassword@orcl @BPM\_HOME/profiles/DmgrProfile/dbscripts/cell\_name/Oracle/orcl/celluser/createSchema\_Advanced.sql
For
example, use the following commands to run the scripts manually for
a deployment environment-level Common database configuration:sqlplus cmnuser/cmnpassword@orcl @BPM\_HOME/profiles/DmgrProfile/dbscripts/cell\_name.deployment\_environment\_name/Oracle/orcl/cmnuser/createSchema\_Advanced.sqlsqlplus cmnuser/cmnpassword@orcl @BPM\_HOME/profiles/DmgrProfile/dbscripts/cell\_name.deployment\_environment\_name/Oracle/orcl/cmnuser/createSchema\_Messaging.sql
3. Run the scripts to
apply the schema to the BPMDB.
For example, use the following
commands to run the scripts manually for the Process database configuration:sqlplus psuser/pspassword@orcl @BPM\_HOME/profiles/DmgrProfile/dbscripts/cell\_name.deployment\_environment\_name/Oracle/orcl/psuser/createSchema\_Advanced.sqlsqlplus psuser/pspassword@orcl @BPM\_HOME/profiles/DmgrProfile/dbscripts/cell\_name.deployment\_environment\_name/Oracle/orcl/psuser/createProcedure\_Advanced.sql
4. Run the scripts to apply the schema to the PDWDB.

For example, use the following commands to run the scripts manually for the Performance Data
Warehouse database
configuration:sqlplus pdwuser/pdwpassword@orcl @BPM\_HOME/profiles/DmgrProfile/dbscripts/cell\_name.deployment\_environment\_name/Oracle/orcl/pdwuser/createSchema\_Advanced.sql
5. Run the scripts to apply the schema to the Content database.

For example, use the following commands to apply the schema to the
ICN\_user:sqlplus icnuser/icnassword@orcl install\_root/profiles/DmgrProfile/dbscripts/cell\_name.deployment\_environment\_name/Oracle/orcl/icnuser/createSchema\_Advanced.sql

## What to do next

If you created a Standard
deployment environment or an Advanced
deployment environment,
you must now run the bootstrap utility to load configuration data for the IBM® Business Automation Workflow applications into the Process
database. This data is required for the applications to run correctly.

## Related tasks

- Configuring profiles and creating a network deployment environment using BPMConfig on AIX or Linux with Oracle

## Related information

- Creating users for Oracle databases in a network deployment environment on AIX or Linux
- Loading the database with system information in a network deployment environment on AIX or Linux
- BPMConfig command-line utility