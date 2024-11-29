# createDatabase.sh script

## Prerequisites

Before you run the createDatabase.sh script,
you must configure the DB2 command
line processor by defining a set of environment variables and a db2 command
alias. You must also define alias names that can be used to connect
to the DB2 for z/OS server.

Create the required buffer
pools. For more information, see Sample Db2 for z/OS commands for allocating buffer pools.

## Location

The createDatabase.sh script
is created when you generate the database scripts that are required
to create the product databases for your network deployment cell.
The createDatabase.sh script is created in each
output subdirectory to which the database scripts are generated, and
you can run the createDatabase.sh command once
from each output subdirectory, for each instance of a database to
be created.

The createDatabase.sh script
produces an audit trail of the objects that it creates in the z\_output.txt file,
which is generated in the directory from which you ran the createDatabase.sh command.

## Syntax

```
createDatabase.sh
-DBAlias alias\_name
-DBCreate
-RunSQL
```

## Parameters

## Examples

```
createDatabase.sh -DBAlias DSNXWBD -DBCreate -RunSQL
```

1. Connect to the DB2 server
by using the DSNXWBD alias name.
2. Create a cell-scoped database named S4CELLDB and create the storage
group.
3. Create the database objects for the CellScopedDB component.

The user ID that runs createDatabase.sh will
have SYSADM authority for the S4CELLDB database.

In an Advanced
deployment environment, the user ID with
DBADM authority then runs the following command to connect to the DB2 server by using the DSNABCD
alias name, and to create the database objects in the S4SR01 database.
In this database, the Performance Data Warehouse objects are assigned
to a unique schema.

```
createDatabase.sh -DBAlias DSNABCD -RunSQL
```

- Sample Db2 for z/OS commands for allocating buffer pools

Before running the createDatabase.sh script to configure your databases, you must allocate the required buffer pools.