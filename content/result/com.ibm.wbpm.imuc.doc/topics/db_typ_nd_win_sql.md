# Creating SQL Server databases

## Before you begin

- You cannot share databases across multiple deployment environments.
- The Process and Performance Data Warehouse components require their own separate databases and
cannot be configured on the same database as the other IBM Business Automation Workflow components.
- The Process and Performance Data Warehouse components require the databases to be case
insensitive for SQL Server.
- The CommonDB (and legacy WebSphere® Process
Server) components
require the databases to be case sensitive for SQL Server.
- The user who creates the databases cannot be the same user that
you plan to assign as the login user for accessing the databases.
If you deviate from this requirement, the default schema dbo will
be used.
- The schema name used for each component should match the user.

## About this task

The default database names are BPMDB for the Process database, PDWDB for the
Performance Data Warehouse database, CMNDB for the Common database, and CPEDB for the Content
database.  In the case of an Advanced
deployment environment or AdvancedOnly
deployment environment, the Common database has two parts: one is
scoped to the cell and the other is scoped to the deployment environment. Both parts can be defined
to use CMNDB (which is the default) or they can use separate databases. For details about databases
and schemas, see Planning the number of databases.

## Procedure

1 Use one of the following methods to create the BPMDB andPDWDB databases:
    - Create and run the createDatabase\_CaseInsensitive.sql file as describedin the following substeps:
        1. Save the following SQL statement into a file named
createDatabase\_CaseInsensitive.sql (where CI in the COLLATE
attribute value is applicable for the case-insensitive
databases):CREATE DATABASE @DB\_NAME@ COLLATE SQL\_Latin1\_General\_CP1\_CI\_AS;
GO
ALTER DATABASE @DB\_NAME@ SET READ\_COMMITTED\_SNAPSHOT ON;
GO
        2. In the SQL statement, replace @DB\_NAME@ with the name of the database that
you want to create.
        3. Run the following command to create the
database:sqlcmd -i createDatabase\_CaseInsensitive.sql
- Run the following command from the command line (where @DB\_NAME@ is the
name of the database that you want to
create):sqlcmd -Q "CREATE DATABASE @DB\_NAME@ COLLATE SQL\_Latin1\_General\_CP1\_CI\_AS;"
sqlcmd -Q "ALTER DATABASE @DB\_NAME@ SET READ\_COMMITTED\_SNAPSHOT ON;"
2 Use one of the following methods to create the CMNDBdatabase:

- Create and run the createDatabase\_CaseSensitive.sql file as describedin the following substeps:
    1. Save the following SQL statement into a file named
createDatabase\_CaseSensitive.sql (where CS in the COLLATE
attribute value is applicable for the case-sensitive
databases):CREATE DATABASE @DB\_NAME@ COLLATE SQL\_Latin1\_General\_CP1\_CS\_AS;
GO
ALTER DATABASE @DB\_NAME@ SET READ\_COMMITTED\_SNAPSHOT ON;
GO
    2. In the SQL statement, replace @DB\_NAME@ with the name of the database that
you want to create.
    3. Run the following command to create the
database:sqlcmd -i createDatabase\_CaseSensitive.sql
- Run the following command from the command line (where @DB\_NAME@ is the
name of the database that you want to
create):sqlcmd -Q "CREATE DATABASE @DB\_NAME@ COLLATE SQL\_Latin1\_General\_CP1\_CS\_AS;"
sqlcmd -Q "ALTER DATABASE @DB\_NAME@ SET READ\_COMMITTED\_SNAPSHOT ON;"
3 Create the content database (CPEDB) and the schemas for the design objectstore (DOS), target object store (TOS), and IBM ContentNavigator (ICN):

1. Save the following SQL statements into a file named
createDatabase\_ECM.sql:

CREATE DATABASE @DB\_NAME@
ON PRIMARY
(  NAME = @DB\_NAME@\_DATA,
   FILENAME = '@DB\_DIR@\@DB\_NAME@\@DB\_NAME@\_DATA.mdf',
   SIZE = 5GB,
   FILEGROWTH = 1GB ),

FILEGROUP @DOS\_SCHEMA@\_DATA\_FG
(  NAME = @DOS\_SCHEMA@\_DATA,
   FILENAME = '@DB\_DIR@\@DB\_NAME@\@DOS\_SCHEMA@\_DATA.ndf',
   SIZE = 2GB,
   FILEGROWTH = 512MB),
  
FILEGROUP @DOS\_SCHEMA@\_IDX\_FG
(  NAME = @DOS\_SCHEMA@\_IDX,
   FILENAME = '@DB\_DIR@\@DB\_NAME@\@DOS\_SCHEMA@\_IDX.ndf',
   SIZE = 1GB,
   FILEGROWTH = 128MB),
   
FILEGROUP @TOS\_SCHEMA@\_DATA\_FG
(  NAME = @TOS\_SCHEMA@\_DATA,
   FILENAME = '@DB\_DIR@\@DB\_NAME@\@TOS\_SCHEMA@\_DATA.ndf',
   SIZE = 2GB,
   FILEGROWTH = 512MB),
  
FILEGROUP @TOS\_SCHEMA@\_IDX\_FG
(  NAME = @TOS\_SCHEMA@\_IDX,
   FILENAME = '@DB\_DIR@\@DB\_NAME@\@TOS\_SCHEMA@\_IDX.ndf',
   SIZE = 1GB,
   FILEGROWTH = 128MB)
  
LOG ON
(  NAME = '@DB\_NAME@\_LOG',
   FILENAME = '@DB\_DIR@\@DB\_NAME@\@DB\_NAME@\_LOG.ldf',
   SIZE = 1024MB,
   FILEGROWTH = 100MB )
GO

ALTER DATABASE @DB\_NAME@ SET RECOVERY SIMPLE 
GO

ALTER DATABASE @DB\_NAME@ SET AUTO\_CREATE\_STATISTICS ON 
GO

ALTER DATABASE @DB\_NAME@ SET AUTO\_UPDATE\_STATISTICS ON 
GO

ALTER DATABASE @DB\_NAME@ SET READ\_COMMITTED\_SNAPSHOT ON
GO
2. Replace @DB\_NAME@ with the name that you want to use for the database (such
as CPEDB). Replace @DOS\_SCHEMA@ with DOSSA and replace
@TOS\_SCHEMA@ with TOSSA. Replace @DB\_DIR@ with the location
where you want to store your database (for example, the default SQL Server store location is
C:\Program Files\Microsoft SQL Server\MSSQL12.MSSQLSERVER\MSSQL\DATA).
Manually, create a folder with the name of the @DB\_NAME@ under
@DB\_DIR@.
Remember the name you choose for the database. You will enter it in the launchpad if you are
using SQL Server authentication.
3. Run the createDatabase\_ECM.sql command to create the database.
4. To create the schemas, save the following SQL statements into a file named
createSchema\_ECM.sql:

-- MSSQL SQL Script for creating schema

USE @DB\_NAME@
GO
CREATE SCHEMA @SCHEMA@;
GO
5. Run the createSchema\_ECM.sql command three times, replacing @DB\_NAME@ with
the name of the content database that you specified before, and replacing @SCHEMA@ with first TOSSA,
then DOSSA, and finally ICNSA.
6. Change the schema owner for the three schemas (DOSSA, TOSSA,
and ICNSA) to the user you created in the previous step instead of the default user (dbo).
 Open the SQL Server Management Studio and right-click each schema name. On the General
tab, click Search for the Schema owner and choose the user
name.

## Related information

- Installing and configuring Workflow Center with an SQL Server database server on Windows
- Installing and configuring Workflow Server with an SQL Server database server on Windows