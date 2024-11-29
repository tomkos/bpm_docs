# SQL Server database privileges

Permissions in SQL Server are assigned to roles which can be assigned to users, similar to
Windows user groups. There are two types of roles:

- Server roles provision database server related permissions
such as backup, shutdown, creating new databases, managing logins,
and linking to other servers.
- Database roles provision more traditional database permissions such as table access and
those listed in the following note.

- db\_ddladmin
- db\_datawriter
- db\_datareader
- SqlJDBCXAUser

- The user cannot be assigned to the system administrator (SYSADMIN) role.
- The user must be mapped to the master database with the SqlJDBCXAUser role.

For more information, see the WebSphere® Application
Server page in
the related reference.

When
you create database schemas using the typical installation or database
scripts that are generated using the BPMConfig command-line utility,
your user ID must have the authority to create tables. When the tables
are created, you must have the authority to select, insert, update,
and delete information in the tables.

The previous fixed database roles cover 80% of the requirements; the remaining permissions
are:

- •CREATE INDEXTYPE: No INDEXTYPE. but db\_ddladmin can
create indexes and specify the type
- •CREATE TABLESPACE: No TABLESPACE but similar concepts
are WORKLOAD GROUP, RESOURCE POOL, and PARTITION SCHEME
- •ALTER LOCK TABLE: This functionality is available through
Lock hinting using the read or write commands (eg SELECT * FROM tbl
name WHERE TABLOCKX
- •CREATE SEQUENCE: This command is in the SQL Server 2012
documentation but not 2008 R2

| Minimum privileges that are required to create objects in the database                                         | Minimum privileges that are required to access objects in the database                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The user ID ideally requires DB OWNER privileges on the data stores used for IBM Business Automation Workflow. | Configure the SQL Server for SQL Server and Windows authentication so that authentication to be based on an SQL server login ID and password. The user ID must be the owner of the tables, or a member of a group that has sufficient authority to issue TRUNCATE TABLE statements.See the following table for the detailed privileges. |

The following table describes more SQL Server database
privileges for IBM Business Automation Workflow components.
The installation privileges are the privileges that are required to
install and configure the product. The runtime privileges are the
database privileges that are required to run the product.

| Component                                                                                | Installation and upgrade privileges                                                                                                             | Runtime privileges                                                                                                                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Common DB                                                                                | CREATE TABLE, ALTER TABLE, INSERT, CREATE USER, ALTER USER                                                                                      | SELECT, UPDATE, DELETE, INSERT, CREATE VIEW, CREATE PROCEDUREThe runtime user must have USAGE ON SEQUENCE privileges on all sequences in the createSchema\_*.sql script for the common DB.                                                                                                                       |
| Business Space                                                                           | CREATE TABLE, ALTER TABLE, INSERT, CREATE USER, ALTER USER                                                                                      | SELECT, UPDATE, DELETE, INSERT, CREATE VIEW, CREATE PROCEDURE                                                                                                                                                                                                                                                   |
| Business Process Choreographer                                                           | CREATE TABLE, ALTER TABLE, CREATE VIEW, CREATE USER, CREATE PROCEDURE                                                                           | SELECT, UPDATE, DELETE, INSERT                                                                                                                                                                                                                                                                                  |
| Messaging Engines                                                                        | CREATE TABLE                                                                                                                                    | SELECT, UPDATE, DELETE, INSERT, DROP ANY TABLENote: Messaging Engines use the TRUNCATE TABLE SQL statement, which might require the DROP ANY TABLE privilege. See Database privileges.                                                                                                                          |
| Process ServerNote: Only the Process Server component applies to Workflow on containers. | CREATE TABLE, SELECT, INSERT, UPDATE, DELETE TABLE, DROP TABLE, CREATE INDEX, CREATE VIEW, DROP VIEW, CREATE PROCEDURE, CREATE USER, ALTER USER | SELECT, UPDATE, DELETE, INSERT, CREATE VIEW, CREATE PROCEDURE, DROP TABLE, DROP VIEW                                                                                                                                                                                                                            |
| Performance Data Warehouse                                                               | CREATE TABLE, SELECT, INSERT, UPDATE, DELETE TABLE, DROP TABLE, CREATE INDEX, CREATE VIEW, DROP VIEW, CREATE PROCEDURE, CREATE USER, ALTER USER | SELECT, UPDATE, DELETE, INSERT, CREATE VIEW, CREATE PROCEDURE, DROP TABLE, DROP VIEW                                                                                                                                                                                                                            |
| Content                                                                                  | CREATE TABLE, ALTER TABLE, INSERT, CREATE USER, ALTER USER                                                                                      | db\_datawriter db\_datareader db\_ddladmin public                                                                                                                                                                                                                                                                  |
| BPM document store                                                                       |                                                                                                                                                 | db\_datawriter db\_datareader db\_ddladmin public  When you configure your database for the BPM document store, a database capability that is named EmbeddedECM is used. The privileges listed for the BPM content store are required for the database in the property file containing the EmbeddedECM capability. |

- The BPMDB and PDWDB databases must be created as case-insensitive. Use the command
COLLATE SQL\_Latin1\_General\_CP1\_CI\_AS, where CI is the
COLLATE attribute value that is applicable for the case-insensitive databases.
- The CommonDB database must be created as case-sensitive. Use the command COLLATE
SQL\_Latin1\_General\_CP1\_CS\_AS, where CS is the COLLATE
attribute value that is applicable for the case-sensitive databases.

## Related reference

- Database privileges in WebSphere Application Server