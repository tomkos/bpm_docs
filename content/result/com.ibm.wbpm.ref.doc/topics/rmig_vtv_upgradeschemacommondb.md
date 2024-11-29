# upgradeSchema command-line utility

- DB2: DB2 Universal Database (for all operating systems except z/OS®)
- Oracle: Oracle Database
- SQLServer: Microsoft SQL Server

If the command is used with no parameters and it needs parameters, it runs in interactive mode,
prompting for parameters. The command can also be invoked in a noninteractive mode, where it takes a
set of parameters that are dependent on the database type being migrated.

## Prerequisites

For a database that is used, the database user who is configured for the data source must be
authorized to create and alter tables and create and drop indexes and views.

Any database that is accessed by a migrated server must have its schema updated before you start
the server. In the case of a cluster, any database that is accessed by any of the migrated cluster
members must have its schema updated before you start any of the cluster members.

Make sure the server or, if applicable, servers in the cluster remain stopped (do not start them
after the migration wizard or scripts have run before completing the database upgrade) while
executing this script.

If this script fails, there is no rollback possibility, so you must back up your database before
running the script. However, if the script is restarted, it will attempt to continue migrating the
data from the point at which it failed.

If this step is not completed before you start the target server, and if the configuration
supports automatic schema updates, the update will be performed as part of server startup.

## Location

The upgradeSchema command-line utility is in the
snapshot\_directory/DBType/Database
Name.Schema Name directory upgrades the schema for the
specified database.

## Syntax

- For DB2, Oracle, and SQLServer database types (interactive mode):
upgradeSchema
- For DB2 (noninteractive mode):
upgradeSchema 
-database\_user\_id 
-database\_password
- For Oracle (noninteractive mode):
upgradeSchema 
-database\_user\_id 
-database\_password
-Oracle\_SID
- For SQLServer (noninteractive mode):
upgradeSchema 
-database\_user\_id 
-database\_password 
-database\_host\_name

## Parameters

## Example

```
C:\DatabaseUtilities\MigrationSnapshots\ProcSrv01\DB2\WPRCSDB.CDBSchema> upgradeSchema.bat

Enter DB2 user[dbUserId]:db2admin

Enter current password for db2admin:*****
```