<!-- image -->

# Removing redundant indexes

## Before you begin

- No applications use the query or query table APIs.
- Some applications use the query or query table APIs, but it does
not matter that the applications get slower response times from the
database for those queries.

## Procedure

1 Change to the directory where the tuning script for yourdatabase is located. Enter one of the commands: Where database\_type is the type of your databasesystem.
    - cd install\_root/BPM/dbscripts/database\_type/Tuning
    - cd install\_root\BPM\dbscripts\database\_type\Tuning
2. Make a copy of the optionalUpgradeIndexes.sql script,
for example, named myOptionalUpgradeIndexes.sql.
3 Edit your myOptionalUpgradeIndexes.sql scriptcopy.

1. Replace all occurrences of the string @SCHEMA@ with
the name of your schema. Important: If you
use an implicit schema, you must delete the string @SCHEMA@.,
including the trailing dot.
2. If you are using a DB2 for z/OS database, replace all
occurrences of the string @STOGRP@ with the name
of your storage group.
3. If you are using an Oracle database,  replace all occurrences
of the string @INDEXTS@ with the name of the index
table space.
4. Save your changes.
4 At a time when there is either a low load on the BusinessProcess Choreographer database (BPEDB ) or whenyour cluster is stopped, run your edited myOptionalUpgradeIndexes.sql script. In your database client command-line processor, enter one ofthe following commands: For more information about how to run scripts on your database,see the product documentation for your database. If thecluster is still running, there is an increased probability of deadlocksoccurring while the script is running.

- For DB2®: db2 -tf
myOptionalUpgradeIndexes.sql
- For Oracle: sqlplus dbUserID/dbPassword@database\_name
@myOptionalUpgradeIndexes.sql
- For Microsoft SQL Server: sqlcmd
-U dbUserID -P dbPassword -e -i myOptionalUpgradeIndexes.sql
5 If any errors are displayed, complete the following steps:

1. You can ignore any error messages that report that certain
indexes do not exist. This is either because you customized the schema
so that the indexes were never created, or some of the indexes were
already removed.
2. If there are any other types of errors, fix the problem,
then try running the script again.
6. Optional: If you configured a Business Process
Archive Manager, you can run the script against the archive database
(BPARCDB) to remove the same redundant indexes
from the archive database. If there are any problems, make sure that
the schema qualifier in the script matches that of the archive database.

## Results

<!-- image -->

## Related information

- Adding support for shared work items