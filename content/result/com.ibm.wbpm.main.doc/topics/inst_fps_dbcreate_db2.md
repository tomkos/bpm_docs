# Creating the Process Federation Server database
for DB2

## Before you begin

## About this task

- createDatabase\_PFS.sql
- createTablespace\_PFS.sql
- createTable\_PFS.sql

## Procedure

1. Replace the variables in the script files with the values
for your federated environment: 
@DB\_NAME@
The name of the Process Federation Server database,
for example, PFSDB.
@SCHEMA@
The name of the Process Federation Server schema,
for example, PFSDB.
@DB\_USER@
The user name that you want to use for database creation. During
database creation, this user is granted database administrator (DBADM)
privileges. To secure the database, you can remove the database administrator
privileges from the createDatabase\_PFS.sql script
and enable them in the createTables\_PFS.sql script.
The database scripts contain more information about these changes.
@TAB\_TS@
The regular table space that is used for storing data. 
@IDX\_TS@
The regular table space that is used for storing indexes. 
@LOB\_TS@
The regular table space that is used for storing binary data.
2 From a DB2 command line, run the scripts to create thedatabase, table spaces, and tables: The DB2 database is created with the following defaultterritory setting: TERRITORY EN\_US .The default territory setting determines the language that is usedfor the database. You can change the value of this setting to oneof the supported territory codes and code pages that DB2 supports.Territory settings must use the UTF-8 code set. For example, to changethe language to French, change the territory setting to TERRITORY FR\_FR .
    1. Create the database. db2 -tf createDatabase\_PFS.sql
    2. Create the table spaces. You must run this
command as the user that you substituted for the @DB\_USER@ variable.db2 connect to PFSDB
db2 -tf createTablespace\_PFS.sql
db2 connect reset
    3. Create the tables. db2 connect to PFSDB
db2 -tf createTable\_PFS.sql
db2 connect reset

## What to do next

Create a process federation server. See Creating a process federation server.