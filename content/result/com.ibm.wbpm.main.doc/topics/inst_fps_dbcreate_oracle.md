# Creating the Process Federation Server database
for Oracle

## Before you begin

## About this task

- createTablespace\_PFS.sql
- createSchema\_PFS.sql
- createTable\_PFS.sql

## Procedure

1. Replace the variables in the script files with the values
for your federated environment: 
@SCHEMA@
The name of the user who owns the Process Federation Server database
tables.
@DB\_PASSWORD@
The password for the user that is identified by the @SCHEMA@ variable.
@TAB\_TS@
The table space that is used for storing data. 
@IDX\_TS@
The table space that is used for storing indexes. 
@TSDIR@
The directory path for the table space or a prefix for the table
space name, for example, PFSTS, that is added
to all table spaces.
@DB\_USER@
The user name that you want to use to create the database. During
database creation, this user is granted RESOURCE privileges.
To secure the database, you can remove the privileges for RESOURCE in the createSchema\_PFS.sql script
and enable them in the createTable\_PFS.sql script.
The database scripts contain more information about these changes.
2 From a command prompt, run the scripts to create the tablespaces, schema, and tables. The following variables areused in the script calls:dbadmin The Oracle user with administrative authority. database\_name The Oracle service name, for example, orcl . The Oracle database is created.
    1. Create the table spaces. sqlplus dbadmin/password@database\_name @createTablespace.sql
    2. Create the schema. sqlplus dbadmin/password@database\_name @createSchema.sql
    3. Create the tables. sqlplus dbadmin/password@database\_name @createTable.sql

## What to do next

Create a process federation server. See Creating a process federation server.