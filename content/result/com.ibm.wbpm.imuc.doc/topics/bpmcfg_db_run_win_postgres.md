# Running the generated PostgreSQL database scripts

## Before you begin

Before you begin this task, you must have run the BPMConfig command to
generate the correct SQL scripts. You also need to have created the required databases using the
generated database creation scripts.

If the bpm.de.deferSchemaCreation property is set to
false, the SQL scripts used to create the database tables are automatically run
when you create the deployment environment.

## About this task

- cell\_name.deployment\_environment\_name - For each deployment environment, this
folder will contain the SQL files that need to be run.

## Procedure

1 Locate the generated SQL scripts. A default configuration for a Standard deployment environment with PostgreSQL databasescontains the following sub-folders and SQL scripts:
    - cell\_name.deployment\_environment\_name
        - PostgreSQL
            - bpmdb
                - schema\_name
                    - createSchema\_Standard.sql
                    - createProcedure\_Standard.sql
    - pdwdb
        - createSchema\_Standard.sql
- cpedb
    - createSchema\_Standard.sql
2. Run the scripts to apply the schema to the bpmdb.  Note: If
you set bpm.de.deferSchemaCreation=true, connect to your databases before you
run CreateSchema\_Standard.sql and
CreateProcedure\_Standard.sql. For example: \c xxxdb
SET ROLE xxx;
For example, use the following commands to run the scripts manually
for the Process database configuration:\c bpmdb
SET ROLE dbUser;
\i /bpmdb/createSchema\_Standard.sql 
\i /bpmdb/createProcedure\_Standard.sql
3. Run the scripts to apply the schema to the pdwdb. For example, use the
following commands to run the scripts manually for the Performance Data Warehouse database
configuration: 
\c pdwdb
SET ROLE dbUser;
\i /pdwdb/createSchema\_Standard.sql
4. Run the scripts to apply the schema to the cpedb. For example, use the
following commands to run the scripts manually for the Content database configuration: 
\c cpedb
SET ROLE dbUser;
\i /cpedb/createSchema\_Standard.sql

## What to do next

If your PostgreSQL
database server uses certificate authentication, refer to the Enabling a NIST SP800-131a compliant environment to do
SSL related configuration and then run the bootstrapProcessServerData command.
After this, start the deployment manager and the IBM Business Automation Workflow server. The server
will not start successfully, if you start the IBM Business Automation Workflow server without
configuring the SSL.