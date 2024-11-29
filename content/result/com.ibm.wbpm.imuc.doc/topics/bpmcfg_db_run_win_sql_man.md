# Running the generated SQL Server database scripts

## Before you begin

Before you begin this task, you must have
run the BPMConfig command or the Deployment Environment
wizard to generate the correct SQL scripts.You
also need to have created the required databases using the generated
database creation scripts.

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

1 Locate thegenerated SQL scripts. A default configuration for an Advanced deployment environment with SQL Server databases contains the followingsub-folders and SQL scripts: Note: The BPMDB , PDWDB , andCPEDB folders for Process, Performance Data Warehouse, and Content databases arenot generated for an AdvancedOnly deployment environment .
    - cell\_name
        - SQLServer
            - CMNDB
                - schema name
                    - createSchema\_Advanced.sql
- cell\_name.deployment\_environment\_name

- SQLServer
    - CMNDB
        - schema name
            - createSchema\_Advanced.sql
            - createSchema\_Messaging.sql

- BPMDB
    - schema name
        - createSchema\_Advanced.sql
        - createProcedure\_Advanced.sql

- CPEDB
    - schema name
        - createSchema\_Advanced.sql
2. Run the scripts to
apply the schema to the CMNDB.
For
example, use the following commands to run the scripts manually for
a cell-scoped Common database configuration: sqlcmd -U @DB\_USER@ -P @DB\_PASSWD@ -d CMNDB -i profiles\DmgrProfile\dbscripts\cell\_name\SQLServer\CMNDB\schema1\createSchema\_Advanced.sql
For example, use the following commands to run the scripts manually for a deployment
environment-level Common database
configuration:sqlcmd -U @DB\_USER@ -P @DB\_PASSWD@ -d CMNDB -i profiles\DmgrProfile\dbscripts\cell\_name.deployment\_environment\_name\SQLServer\CMNDB\schema1\createSchema\_Advanced.sqlsqlcmd -U @DB\_USER@ -P @DB\_PASSWD@ -d CMNDB -i profiles\DmgrProfile\dbscripts\cell\_name.deployment\_environment\_name\SQLServer\CMNDB\schema1\createSchema\_Messaging.sqlIn the previous and next examples, schema1 is the name of the
schema used.
3. Run the scripts to
apply the schema to the BPMDB.
For example, use the following
commands to run the scripts manually for the Process database configuration:sqlcmd -U @DB\_USER@ -P @DB\_PASSWD@ -d BPMDB -i profiles\DmgrProfile\dbscripts\cell\_name.deployment\_environment\_name\SQLServer\BPMDB\schema1\createSchema\_Advanced.sqlsqlcmd -U @DB\_USER@ -P @DB\_PASSWD@ -d BPMDB -i profiles\DmgrProfile\dbscripts\cell\_name.deployment\_environment\_name\SQLServer\BPMDB\schema1\createProcedure\_Advanced.sql
4. Run the scripts to apply the schema to the PDWDB.

For example, use the following commands to run the scripts manually for the Performance Data
Warehouse database
configuration:sqlcmd -U @DB\_USER@ -P @DB\_PASSWD@ -d PDWDB -i profiles\DmgrProfile\dbscripts\cell\_name.deployment\_environment\_name\SQLServer\PDWDB\schema1\createSchema\_Advanced.sql
5. Run the scripts to apply the schema to the Content database.

For example, use the following commands to run the scripts manually for the Content database
configuration:sqlcmd -U @DB\_USER@ -P @DB\_PASSWD@ -d CPEDB -i profiles\DmgrProfile\dbscripts\cell\_name.deployment\_environment\_name\SQLServer\CPEDB\schema1\createSchema\_Advanced.sql

## What to do next

If you created a Standard
deployment environment or an Advanced
deployment environment,
you must now run the bootstrap utility to load configuration data for the IBM® Business Automation Workflow applications into the Process
database. This data is required for the applications to run correctly.

## Related tasks

- Configuring profiles and creating a network deployment environment using BPMConfig on Windows with SQL Server

## Related information

- Creating SQL Server databases in a network deployment environment on Windows
- Loading the database with system information in a network deployment environment on Windows
- BPMConfig command-line utility