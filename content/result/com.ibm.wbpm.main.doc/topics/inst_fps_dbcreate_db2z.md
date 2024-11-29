# Creating the Process Federation Server database
for DB2 for z/OS

## Before you begin

- Ensure that a DB2 storage group is available for the Process Federation Server database.
Do not use the default storage group, SYSDEFAULT.
- The database scripts assume that a buffer pool called BP32K exists.
Work with your DB2 for z/OS database administrator to determine which
buffer pools to use, and update the database scripts accordingly.

## About this task

- createDatabase\_PFS.sql
- createTablespace\_PFS.sql
- createTable\_PFS.sql

## Procedure

1. Replace the variables in the script files with the values
for your federated environment: 
@STOGRP@
The name of the DB2 storage group, for example, SYSDEFLT.
@DB\_NAME@
The name of the Process Federation Server database,
for example, PFSDB.
@SCHEMA@
The name of the Process Federation Server schema,
for example, PFSDB.
@DB\_USER@
The database user for runtime operations. The user must have SELECT,
INSERT, UPDATE, and DELETE privileges for all tables in the schema
as granted by the administrator or the privileges that are specified
in the createTables\_PFS.sql script.
2 From a DB2 command line, run the scripts to create thedatabase, table spaces, and tables. The database user requiresSYSCTRL or SYSADM authority to run the commands. The DB2 for z/OS database is created.
    1. Create the database. db2 -tf createDatabase\_PFS.sql
    2. Create the table spaces. db2 -tf createTablespace\_PFS.sql
    3. Create the tables. db2 -tf createTable\_PFS.sql

## What to do next

Create a process federation server. See Creating a process federation server.