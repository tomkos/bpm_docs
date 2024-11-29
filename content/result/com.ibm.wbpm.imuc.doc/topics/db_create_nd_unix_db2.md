# Creating DB2 databases

You must create the required databases before the
installation of IBM® Business Automation
Workflow. Usually you
require the Process database, the Performance Data Warehouse database, the Common database, and the
Content database. In the case of an AdvancedOnly
deployment environment, you need only the Common database.

If you have an existing local DB2 server on your system, you
can choose to create the required databases as part of the installation. Otherwise, you must create
the databases before you install the product, as described in this topic.

## About this task

The Process and Performance Data Warehouse require their own separate databases and
cannot be configured on the same database as the other IBM Business Automation Workflow components.

The default database names are BPMDB for the Process database, PDWDB for the
Performance Data Warehouse database, CMNDB for the Common database, and CPEDB for the Content
database.  In the case of an Advanced
deployment environment or AdvancedOnly
deployment environment, the Common database has two parts: one is
scoped to the cell and the other is scoped to the deployment environment. Both parts can be defined
to use CMNDB (which is the default) or they can use separate databases. For details about databases
and schemas, see Planning the number of databases.

## Procedure

For all databases except the Content database, use one of the
following methods to create each database that you require. Then see the third bullet to create the
Content database.

- Create and run the createDatabase.sql fileas described in the following substeps:
    1. Save the following SQL statements into a file named
createDatabase.sql:

create database @DB\_NAME@ automatic storage yes  using codeset UTF-8 territory US pagesize 32768;
connect to @DB\_NAME@;
-- A user temporary table space is required to support stored procedures in BPM
create user temporary tablespace usrtmpspc1;
grant dbadm on database to user @DB\_USER@;
UPDATE DB CFG FOR @DB\_NAME@ USING LOGFILSIZ 16384 DEFERRED;
UPDATE DB CFG FOR @DB\_NAME@ USING LOGSECOND 64 IMMEDIATE;
connect reset;
    2. In the SQL statements, replace @DB\_NAME@ with the name that you
want to use for the created database and replace @DB\_USER@ with the user name
that you want to use for the database.
    3. Run the following command to create the database:

db2 -tvf createDatabase.sql
- Run SQL statements in a command editor as described in thefollowing substeps: Note: If a command fails to execute from the DB2 command prompt, remove the semicolon (;) and rerunthe command.

1. Copy the following SQL statements into a command editor:

create database @DB\_NAME@ automatic storage yes  using codeset UTF-8 territory US pagesize 32768;
connect to @DB\_NAME@;
-- A user temporary table space is required to support stored procedures in BPM
create user temporary tablespace usrtmpspc1;
grant dbadm on database to user @DB\_USER@;
UPDATE DB CFG FOR @DB\_NAME@ USING LOGFILSIZ 16384 DEFERRED;
UPDATE DB CFG FOR @DB\_NAME@ USING LOGSECOND 64 IMMEDIATE;
connect reset;
2. In the SQL statements, replace @DB\_NAME@ with the name that you
want to use for the created database and replace @DB\_USER@ with the user name
that you want to use for the database.
3. Run the SQL statements in the command editor.
- Create the content database (CPEDB) and the table spaces for the design object store (DOS),target object store (TOS), and IBM ContentNavigator (ICN) schemas:

1. Save the following text into a file named createDatabase\_ECM.sh:

#!/bin/sh
mkdir -p @DB\_DIR@/@DB\_NAME@/@DOS\_SCHEMA@/datafs1
mkdir -p @DB\_DIR@/@DB\_NAME@/@DOS\_SCHEMA@/datafs2
mkdir -p @DB\_DIR@/@DB\_NAME@/@DOS\_SCHEMA@/datafs3
mkdir -p @DB\_DIR@/@DB\_NAME@/@DOS\_SCHEMA@/indexfs1
mkdir -p @DB\_DIR@/@DB\_NAME@/@DOS\_SCHEMA@/indexfs2
mkdir -p @DB\_DIR@/@DB\_NAME@/@DOS\_SCHEMA@/lobfs1
mkdir -p @DB\_DIR@/@DB\_NAME@/@TOS\_SCHEMA@/datafs1
mkdir -p @DB\_DIR@/@DB\_NAME@/@TOS\_SCHEMA@/datafs2
mkdir -p @DB\_DIR@/@DB\_NAME@/@TOS\_SCHEMA@/datafs3
mkdir -p @DB\_DIR@/@DB\_NAME@/@TOS\_SCHEMA@/indexfs1
mkdir -p @DB\_DIR@/@DB\_NAME@/@TOS\_SCHEMA@/indexfs2
mkdir -p @DB\_DIR@/@DB\_NAME@/@TOS\_SCHEMA@/lobfs1
mkdir -p @DB\_DIR@/@DB\_NAME@/sys
mkdir -p @DB\_DIR@/@DB\_NAME@/systmp
mkdir -p @DB\_DIR@/@DB\_NAME@/usr
mkdir -p @DB\_DIR@/@DB\_NAME@/log

chmod -R 777 @DB\_DIR@/@DB\_NAME@

db2 -stf "./createDatabase\_ECM.sql"
exit $?
2. Save the following SQL statements into a file named
createDatabase\_ECM.sql:

-- Create the database:
CREATE DATABASE @DB\_NAME@
USING CODESET UTF-8 TERRITORY US COLLATE
USING
 SYSTEM PAGESIZE 32768 CATALOG TABLESPACE MANAGED BY SYSTEM USING ('@DB\_DIR@/@DB\_NAME@/sys')
 TEMPORARY TABLESPACE MANAGED BY SYSTEM USING ('@DB\_DIR@/@DB\_NAME@/systmp')
 USER TABLESPACE MANAGED BY SYSTEM USING ('@DB\_DIR@/@DB\_NAME@/usr')
;

-- Increase the application heap size
UPDATE DATABASE CONFIGURATION FOR @DB\_NAME@ USING APPLHEAPSZ 2560;

-- Connect to db
CONNECT TO @DB\_NAME@;

-- Drop unnecessary default table spaces
DROP TABLESPACE USERSPACE1;

UPDATE DB CFG FOR @DB\_NAME@ USING LOGFILSIZ 16384 DEFERRED;
UPDATE DB CFG FOR @DB\_NAME@ USING LOGSECOND 64 IMMEDIATE;

GRANT CREATETAB,CONNECT,DBADM ON DATABASE TO user @DB\_USER@;
GRANT SELECT ON SYSIBM.SYSVERSIONS TO user @DB\_USER@;
GRANT SELECT ON SYSCAT.DATATYPES TO user @DB\_USER@;
GRANT USAGE on WORKLOAD SYSDEFAULTUSERWORKLOAD TO user @DB\_USER@;
UPDATE DATABASE CONFIGURATION FOR @DB\_NAME@ USING NEWLOGPATH '@DB\_DIR@/@DB\_NAME@/log';
ALTER BUFFERPOOL IBMDEFAULTBP IMMEDIATE SIZE 250 AUTOMATIC;

-- Close connection
CONNECT RESET;
3. In both files, replace @DB\_DIR@ with your Db2 instance home directory.
Replace @DB\_NAME@ with the name that you want to use for the database (such as
CPEDB) and @DB\_USER@ with the user name. Replace @DOS\_SCHEMA@
with DOSSA and replace @TOS\_SCHEMA@ with TOSSA.
Remember the name you choose for the database. You will enter it in the launchpad.
4. Run the following command to create the database:

./createDatabase\_ECM.sh
Note: If you see the following error, shut down and restart
Db2.SQL1363W One or more of the parameters submitted for immediate modification
were not changed dynamically. For these configuration parameters, the database
must be shutdown and reactivated before the configuration parameter changes
become effective.
5. To start creating the table spaces for the schemas, save the following SQL statements into a
file named  createTablespace\_ECM.sql:

-- Connect to db
CONNECT TO @DB\_NAME@;

-- Create Schema
CREATE SCHEMA @SCHEMA@;
SET SCHEMA @SCHEMA@;

-- Create 256MB GCD buffer pool
CREATE Bufferpool @SCHEMA@\_DATA\_BP IMMEDIATE SIZE AUTOMATIC PAGESIZE 32K;
CREATE Bufferpool @SCHEMA@\_INDX\_BP IMMEDIATE SIZE AUTOMATIC PAGESIZE 32K;

-- Create additional buffer pools
CREATE Bufferpool @SCHEMA@\_LOB\_BP IMMEDIATE SIZE AUTOMATIC PAGESIZE 32K;
CREATE Bufferpool @SCHEMA@\_TEMP\_BP IMMEDIATE SIZE AUTOMATIC PAGESIZE 32K;
CREATE Bufferpool @SCHEMA@\_SYS\_BP IMMEDIATE SIZE AUTOMATIC PAGESIZE 32K;

CREATE STOGROUP @SCHEMA@DATA\_SG ON '@DB\_DIR@/@DB\_NAME@/@SCHEMA@/datafs1', '@DB\_DIR@/@DB\_NAME@/@SCHEMA@/datafs2', '@DB\_DIR@/@DB\_NAME@/@SCHEMA@/datafs3';
CREATE STOGROUP @SCHEMA@INDX\_SG ON '@DB\_DIR@/@DB\_NAME@/@SCHEMA@/indexfs1', '@DB\_DIR@/@DB\_NAME@/@SCHEMA@/indexfs2';
CREATE STOGROUP @SCHEMA@LOB\_SG ON '@DB\_DIR@/@DB\_NAME@/@SCHEMA@/lobfs1';

-- Create table spaces
CREATE LARGE TABLESPACE @ECM\_DATA\_TS@ PAGESIZE 32 K
MANAGED BY AUTOMATIC STORAGE
USING STOGROUP @SCHEMA@DATA\_SG
EXTENTSIZE 16 OVERHEAD 10.5 PREFETCHSIZE 16 TRANSFERRATE 0.14
BUFFERPOOL @SCHEMA@\_DATA\_BP DROPPED TABLE RECOVERY ON;

CREATE LARGE TABLESPACE @ECM\_IDX\_TS@ PAGESIZE 32 K
MANAGED BY AUTOMATIC STORAGE
USING STOGROUP @SCHEMA@INDX\_SG
EXTENTSIZE 16 OVERHEAD 10.5 PREFETCHSIZE 16 TRANSFERRATE 0.14
BUFFERPOOL @SCHEMA@\_INDX\_BP DROPPED TABLE RECOVERY ON;

CREATE LARGE TABLESPACE @ECM\_LOB\_TS@ PAGESIZE 32 K
MANAGED BY AUTOMATIC STORAGE
USING STOGROUP @SCHEMA@LOB\_SG
EXTENTSIZE 16 OVERHEAD 10.5 PREFETCHSIZE 16 TRANSFERRATE 0.14
BUFFERPOOL @SCHEMA@\_LOB\_BP DROPPED TABLE RECOVERY ON;

CREATE USER TEMPORARY TABLESPACE @SCHEMA@\_TEMP\_TS PAGESIZE 32 K
MANAGED BY AUTOMATIC STORAGE
EXTENTSIZE 16 OVERHEAD 10.5 PREFETCHSIZE 16 TRANSFERRATE 0.14
BUFFERPOOL @SCHEMA@\_TEMP\_BP;

CREATE SYSTEM TEMPORARY TABLESPACE @SCHEMA@\_SYSTMP\_TS PAGESIZE 32 K
MANAGED BY AUTOMATIC STORAGE
EXTENTSIZE 16 OVERHEAD 10.5 PREFETCHSIZE 16 TRANSFERRATE 0.14
BUFFERPOOL @SCHEMA@\_SYS\_BP;

GRANT USE OF TABLESPACE @ECM\_DATA\_TS@ TO user @DB\_USER@;
GRANT USE OF TABLESPACE @ECM\_IDX\_TS@ TO user @DB\_USER@;
GRANT USE OF TABLESPACE @ECM\_LOB\_TS@ TO user @DB\_USER@;
GRANT USE OF TABLESPACE @SCHEMA@\_TEMP\_TS TO user @DB\_USER@;

--GRANT IMPLICIT\_SCHEMA ON DATABASE TO user db2admin;

-- Optionally, grant GROUP access to table spaces
-- GRANT CREATETAB,CONNECT ON DATABASE  TO GROUP DB2USERS;
-- GRANT USE OF TABLESPACE USERTEMP1 TO GROUP DB2USERS;
-- GRANT USE OF TABLESPACE USERSPACE1 TO GROUP DB2USERS;

-- Close connection
CONNECT RESET;
6. Replace @DB\_DIR@, @DB\_NAME@, and
@DB\_USER@ with the names that you used in the previous files. Replace @SCHEMA@
with TOSSA. Replace the table spaces @ECM\_DATA\_TS@, @ECM\_IDX\_TS@, and @ECM\_LOB\_TS@ with
TOSSA\_DATA\_TS, TOSSA\_IDX\_TS, and TOSSA\_LOB\_TS.
7. Run the following command to create the table spaces for the target object store schema:

db2 -tvf createTablespace\_ECM.sql
8. To create the table space for the design object schema, replace @SCHEMA@ with DOSSA. Replace
the table spaces @ECM\_DATA\_TS@, @ECM\_IDX\_TS@, and @ECM\_LOB\_TS@ with DOSSA\_DATA\_TS, DOSSA\_IDX\_TS, and
DOSSA\_LOB\_TS.
9. Run the following command again to create the table spaces for the design object store
schema:

db2 -tvf createTablespace\_ECM.sql
10. To create the table spaces for the IBM Content
Navigator schema, save the following SQL
statements into a file named createTablespace\_ICN.sql:

 
-- Connect to db
CONNECT TO @DB\_NAME@;
 
--  Create a schema for the application to use
CREATE SCHEMA @ECMClient\_SCHEMA@ AUTHORIZATION @ECMClient\_DBUSER@;
-- Comments on the above statement. This is for sync. If the user who
-- creating the schema is the same as the one specified in @ECMClient\_DBUSER@
-- this turns out to be a noop (the user who creates an object is already
-- authorized. This is generally the case in CMUI. If someone is manually
-- installing this, they *could* specify a different user. For sync, that
-- user must be able to create/drop tables in the schema for sync. The
-- 'AUTHORIZATION' directive accomplishes just that.
-- *****************************************************************
--  Create buffer pools and table spaces for the application to use
CREATE Bufferpool @ECMClient\_TBLSPACE@BP IMMEDIATE SIZE AUTOMATIC PAGESIZE 32K;
CREATE Bufferpool @ECMClient\_TBLSPACE@TEMPBP IMMEDIATE SIZE 200 PAGESIZE 32K;
CREATE REGULAR TABLESPACE @ECMClient\_TBLSPACE@ PAGESIZE 32 K 
	MANAGED BY AUTOMATIC STORAGE AUTORESIZE YES INITIALSIZE 20 M 
	INCREASESIZE 20 M BUFFERPOOL @ECMClient\_TBLSPACE@BP;
CREATE USER TEMPORARY TABLESPACE @ECMClient\_TBLSPACE@TEMP PAGESIZE 32K 
	MANAGED BY AUTOMATIC STORAGE BUFFERPOOL @ECMClient\_TBLSPACE@TEMPBP;
-- *****************************************************************

-- Close connection
CONNECT RESET;
11. Replace @ECMClient\_SCHEMA@ with ICNSA. Replace the table space name @ECMClient\_TBLSPACE@ with
WFICNTS.
12. Run the following command to create the table spaces for the IBM Content
Navigator schema:

db2 -tvf createTablespace\_ICN.sql

## What to do next

If you drop the Content database, you must manually remove the directories
that were created for it.