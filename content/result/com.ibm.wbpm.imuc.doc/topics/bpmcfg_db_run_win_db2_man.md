# Running the generated DB2 database scripts

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

1 Locate thegenerated SQL scripts. A default configuration for an Advanced deployment environment with DB2 databases contains the following sub-foldersand SQL scripts: Note: The BPMDB ,PDWDB , and CPEDB folders for Process, Performance DataWarehouse, and Content databases are not generated for an AdvancedOnly deployment environment .
    - cell\_name
        - DB2
            - CMNDB
                - createSchema\_Advanced.sql
- cell\_name.deployment\_environment\_name

- DB2
    - CMNDB
        - createSchema\_Advanced.sql
        - createSchema\_Messaging.sql

- BPMDB
    - createSchema\_Advanced.sql
    - createProcedure\_Advanced.sql

- PDWDB
    - createSchema\_Advanced.sql

- CPEDB
    - createSchema\_Advanced.sql
2. Run the scripts to
apply the schema to the CMNDB.
For
example, use the following commands to run the scripts manually for
a cell-scoped Common database configuration:db2 connect to CMNDB USER username USING password
db2 -tvf profiles\DmgrProfile\dbscripts\cell\_name\DB2\CMNDB\createSchema\_Advanced.sql
db2 connect reset
For example, use the following
commands to run the scripts manually for a deployment environment-level Common
database configuration:db2 connect to CMNDB USER username USING password
db2 -tvf profiles\DmgrProfile\dbscripts\cell\_name.deployment\_environment\_name\DB2\CMNDB\createSchema\_Advanced.sql

db2 -tvf profiles\DmgrProfile\dbscripts\cell\_name.deployment\_environment\_name\DB2\CMNDB\createSchema\_Messaging.sql
db2 connect reset
3. Run the scripts to
apply the schema to the BPMDB.
For example, use the following
commands to run the scripts manually for Process database configuration:db2 connect to BPMDB USER username USING password
db2 -tvf profiles\DmgrProfile\dbscripts\cell\_name.deployment\_environment\_name\DB2\BPMDB\createSchema\_Advanced.sql
db2 -tdGO -vf profiles\DmgrProfile\dbscripts\cell\_name.deployment\_environment\_name\DB2\BPMDB\createProcedure\_Advanced.sql
db2 connect reset
4. Run the scripts to apply the schema to the PDWDB.

For example, use the following commands to run the scripts manually for Performance Data
Warehouse database
configuration:db2 connect to PDWDB USER username USING password
db2 -tvf profiles\DmgrProfile\dbscripts\cell\_name.deployment\_environment\_name\DB2\PDWDB\createSchema\_Advanced.sql
db2 connect reset
5. Run the scripts to apply the schema to the Content database.

For example, use the following commands to run the scripts manually for Content database
configuration:db2 connect to CPEDB USER username USING password
db2 -tvf profiles\DmgrProfile\dbscripts\cell\_name.deployment\_environment\_name\DB2\CPEDB\createSchema\_Advanced.sql
db2 connect reset

## What to do next

If you created a Standard
deployment environment or an Advanced
deployment environment,
you must now run the bootstrap utility to load configuration data for the IBM® Business Automation Workflow applications into the Process
database. This data is required for the applications to run correctly.

## Related tasks

- Configuring profiles and creating a network deployment environment using BPMConfig

## Related information

- Creating Db2 databases in a network deployment environment on Windows
- Loading the database with system information in a network deployment environment on Windows
- BPMConfig command-line utility