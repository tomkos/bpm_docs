# Troubleshooting problems creating database tables

While trying to create database tables
for the Business Process Manager database and the Performance Data
Warehouse database, you might get errors or exceptions that prevent
you from creating the tables. Your bootstrap operation also fails.

```
DB21034E  The command was processed as an SQL statement because it was not a
valid Command Line Processor command.  During SQL processing it returned:
SQL0355N  The column "RECORD", as defined, is too large to be logged.
SQLSTATE=42993
```

## Procedure

1. Upgrade the database to the supported version (DB2 V9.7 fix pack 4 or later)
2. Drop the existing Process Server and Performance Data Warehouse
databases. This step is required because the databases
are not complete. The error indicates that some of the tables are
missing.
3. Create the  Process Server and Performance Data Warehouse
databases again.

## Results