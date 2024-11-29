# Creating users for Oracle databases

You must create the users for Oracle databases before you
install IBM® Business Automation
Workflow. Create the cell-scoped
user, the Process database user, the Performance Data Warehouse user, and the three users for the
Content database: design object store user, target object store user, and IBM Content
Navigator user. The
Process, Performance Data Warehouse, and Content database users are not needed for an AdvancedOnly
deployment environment.

## Before you begin

For simplicity, the instructions on this page assign more than the minimum
required privileges to an IBM Business Automation Workflow database
user. The minimum required privileges are listed in the Oracle database privileges
topic. If you want to specify a more fine-grained list of privileges, change the instructions of
this page according to the privileges listed in the Oracle database privileges topic.

Before you create any users for Oracle databases, see the "Configuring XA transactions for Oracle
in a network environment" related
information.

| Tuning item      |   Minimum memory for initial settings (MB) |
|------------------|--------------------------------------------|
| Buffer cache     |                                       2048 |
| Shared pool size |                                       1024 |

Recommendations for database table space
settings:

On Oracle, IBM Business Automation
Workflow stores
large objects (LOBs) with the SECUREFILE option. For SECUREFILE, it
is recommended to use a table space with the AUTOALLOCATE option. If
you use UNIFORM SIZE extents, ensure that the UNIFORM SIZE is big
enough. Given the default block size of 8K, specify a UNIFORM SIZE
of at least 120K. Business Automation Workflow does
not explicitly prescribe the table space options; it relies on the
default Oracle settings (such as AUTOALLOCATE) to automatically manage
extents.

For new Business Automation Workflow installations,
create table spaces with the AUTOALLOCATE option.

For migrations, if you use table spaces with
a UNIFORM SIZE less than 120K, create new table spaces with the AUTOALLOCATE
option and make it the default table space for Business Automation Workflow database
schema users.

## About this task

The default database names are BPMDB for the Process database, PDWDB for the
Performance Data Warehouse database, CMNDB for the Common database, and CPEDB for the Content
database.  In the case of an Advanced
deployment environment or AdvancedOnly
deployment environment, the Common database has two parts: one is
scoped to the cell and the other is scoped to the deployment environment. Both parts can be defined
to use CMNDB (which is the default) or they can use separate databases. For details about databases
and schemas, see Planning the number of databases.

- Design object store (DOS)
- Target object store (TOS)
- IBM Content
Navigator (ICN)

## Procedure

For all databases except the Content database, use one of
the following methods to create each database user that you require. Then see the third bullet to
create the Content database.

- Create and run the createUser.sql fileas described in the following substeps:
    1. Save the following SQL statements into a file named
createUser.sql:
-- create a new user
CREATE USER @DB\_USER@ IDENTIFIED BY @DB\_PASSWD@;

-- allow the user to connect to the database
grant connect to @DB\_USER@;

-- provide quota on all table spaces with BPM tables
grant unlimited tablespace to @DB\_USER@;

-- grant privileges to create database objects:
grant resource to @DB\_USER@;
grant create view to @DB\_USER@;

-- grant access rights to resolve lock issues
grant execute on dbms\_lock to @DB\_USER@;

-- grant access rights to resolve XA related issues:
grant select on pending\_trans$ to @DB\_USER@;
grant select on dba\_2pc\_pending to @DB\_USER@;
grant select on dba\_pending\_transactions to @DB\_USER@;
-- If using Oracle 10.2.0.3 or lower JDBC driver, un-comment the following statement:
-- grant execute on dbms\_system to @DB\_USER@;
-- If not using Oracle 10.2.0.4 or higher JDBC driver, comment the following statement:
grant execute on dbms\_xa to @DB\_USER@;For information about recovering Oracle database
transactions, see the topic Configuring XA transactions for Oracle in a network environment on Windows.
    2. In the SQL statements, replace @DB\_USER@ with the user name that
you want to use for the database and replace @DB\_PASSWD@ with the password for
that user.
    3. Run the following command to create the database user:

sqlplus oracle\_user\_ID/oracle\_password@db\_name @createUser.sql
- Run SQL statements in a command editor as described in thefollowing substeps:

1. Copy the following SQL statements into a command editor:

-- create a new user
CREATE USER @DB\_USER@ IDENTIFIED BY @DB\_PASSWD@;

-- allow the user to connect to the database
grant connect to @DB\_USER@;

-- provide quota on all table spaces with BPM tables
grant unlimited tablespace to @DB\_USER@;

-- grant privileges to create database objects:
grant resource to @DB\_USER@;
grant create view to @DB\_USER@;

-- grant access rights to resolve lock issues
grant execute on dbms\_lock to @DB\_USER@;

-- grant access rights to resolve XA related issues:
grant select on pending\_trans$ to @DB\_USER@;
grant select on dba\_2pc\_pending to @DB\_USER@;
grant select on dba\_pending\_transactions to @DB\_USER@;
-- If using Oracle 10.2.0.3 or lower JDBC driver, un-comment the following statement:
-- grant execute on dbms\_system to @DB\_USER@;
-- If not using Oracle 10.2.0.4 or higher JDBC driver, comment the following statement:
grant execute on dbms\_xa to @DB\_USER@;
2. In the SQL statements, replace @DB\_USER@ with the user name that
you want to use for the database and replace @DB\_PASSWD@ with the password for
that user.
3. Run the SQL statements in the command editor.
- Create the content database (CPEDB) and the users for the design object store (DOS), targetobject store (TOS), and IBM ContentNavigator (ICN):

1. Save the following SQL statements into a file named
createDatabase\_ECM.sql:

CREATE SMALLFILE TABLESPACE @ECM\_DATA\_TS@ DATAFILE '@DB\_DIR@/@DB\_NAME@/@ECM\_DATA\_TS@.dbf' SIZE 100M REUSE AUTOEXTEND ON NEXT 51200K MAXSIZE 32767M LOGGING EXTENT MANAGEMENT LOCAL SEGMENT SPACE MANAGEMENT AUTO;

CREATE USER @DB\_USER@ PROFILE DEFAULT IDENTIFIED BY @DB\_PASSWD@ DEFAULT TABLESPACE @ECM\_DATA\_TS@ TEMPORARY TABLESPACE TEMP ACCOUNT UNLOCK;
GRANT CREATE TABLESPACE TO @DB\_USER@;
GRANT UNLIMITED TABLESPACE TO @DB\_USER@;
GRANT CONNECT TO @DB\_USER@;
GRANT RESOURCE TO @DB\_USER@;
grant create view to @DB\_USER@;
grant execute on dbms\_lock to @DB\_USER@;
grant select on pending\_trans$ to @DB\_USER@;
grant select on dba\_2pc\_pending to @DB\_USER@;
grant select on dba\_pending\_transactions to @DB\_USER@;
grant execute on dbms\_xa to @DB\_USER@;
2. Update and run the file to create the target object schema (TOS) user. Replace
@DB\_DIR@ with the data directory of your database, which you must create before
running the SQL files. Replace @DB\_NAME@ with the Oracle instance name, for
example, orcl, @DB\_USER@ with the schema name, and
@DB\_PASSWD@ with the password for the user. Replace
@ECM\_DATA\_TS@ with TOSSA\_DATA\_TS. 
Remember the names you choose for users. You will enter them in the launchpad.
3. Update and run the file again to create the design object schema (DOS) user. Replace
@ECM\_DATA\_TS@ with DOSSA\_DATA\_TS. 
Remember the names you choose for users. You will enter them in the launchpad.
4. Update and run the createUser.sql file you created in an earlier step to
create one user for the Content database.
5. Save the following SQL statements into a file named
createTablespaceICN.sql:

-- Create table spaces

CREATE TABLESPACE @ECMClient\_TBLSPACE@
    DATAFILE '@DB\_DIR@/@DB\_NAME@/@ECMClient\_TBLSPACE@.dbf' SIZE 200M REUSE
    AUTOEXTEND ON NEXT 20M
    EXTENT MANAGEMENT LOCAL
    SEGMENT SPACE MANAGEMENT AUTO
    ONLINE
    PERMANENT
;

CREATE TEMPORARY TABLESPACE @ECMClient\_TBLSPACE@TEMP
    TEMPFILE '@DB\_DIR@/@DB\_NAME@/@ECMClient\_TBLSPACE@TEMP.dbf' SIZE 200M REUSE
    AUTOEXTEND ON NEXT 20M
    EXTENT MANAGEMENT LOCAL
;

-- Alter existing schema

ALTER USER @ECMClient\_SCHEMA@
    DEFAULT TABLESPACE @ECMClient\_TBLSPACE@ 
    TEMPORARY TABLESPACE @ECMClient\_TBLSPACE@TEMP;

GRANT CONNECT, RESOURCE to @ECMClient\_SCHEMA@;
GRANT UNLIMITED TABLESPACE TO @ECMClient\_SCHEMA@;
6. Update and run the file to create the IBM Content
Navigator (ICN) user. Replace
@ECMClient\_SCHEMA@ with the user you created in createUser.sql. Replace
@DB\_USER@ with the user name that you want to use and replace @DB\_PASSWD@ with the password for that
user. Replace the table space name @ECMClient\_TBLSPACE@ with WFICNTS.