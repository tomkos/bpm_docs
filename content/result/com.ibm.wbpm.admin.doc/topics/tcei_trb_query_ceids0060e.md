# Error when querying events (message CEIDS0060E)

## Cause

The event service uses metadata stored
in the event database to map Common Base Event elements and attributes
to database tables and columns. This information is read from the
database the first time an application attempts to use the event service
after startup.

The metadata tables are populated when the event
database is created. This error occurs if the tables do not contain
the required metadata at run time.

## Remedy

| Database type       | Script name        |
|---------------------|--------------------|
| DB2®                | ins\_metadata.db2   |
| Informix®           | ins\_metadata.sql   |
| Oracle              | ins\_metadata.ora   |
| SQL Server          | ins\_metadata.mssql |
| DB2 UDB for iSeries | ins\_metadata.db2   |

By default, the script is created in the profile\_root/dbscripts/CEI\_database\_namenode directory.
You can run this script at any time.

- DB2:
db2
- Oracle: SQL*Plus
- Informix:
dbaccess
- SQL Server: osql

After repopulating the metadata, restart the server.