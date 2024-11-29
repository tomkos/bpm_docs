# Creating users and schemas for SQL Server databases

You must create the users and schemas after creating the SQL Server
databases.

## Before you begin

- db\_ddladmin
- db\_datawriter
- db\_datareader
- db\_securityadmin
- bulkadmin

- The user cannot be assigned to the system administrator (SYSADMIN) role.
- The user must be mapped to the master database with the SqlJDBCXAUser role.

## About this task

When using Windows authentication, you must ensure that the domain account is added
to the SQL Server login. You must login as the SQL Server administrator and do the following steps
to create users and schemas.

## Procedure

1 Complete one of the following steps: Note: The SQL Server login that is created must not have SYSADMIN privileges. If the login user hasSYSADMIN privileges, the specified schema value is ignored for database connections by SQL Serversince the sysadmin user's default schema is always dbo .
    - If you are using SQL authentication, create a SQL Server login account for the database user
of each of the databases that you specified in the deployment environment configuration. For
example, if sqluser is the database user name and secret1 is the
password for sqluser, use the following command
syntax:USE MASTER
GO
CREATE LOGIN sqluser WITH PASSWORD='secret1'
GO
    - If you are using Windows authentication, create the SQL Server login account for your
Windows machine using the login information for the machine. For example, if
domain1 is the domain name and user1 is the user name for your
Windows machine, use the following command
syntax:USE MASTER
GO
CREATE LOGIN [domain1\user1] FROM WINDOWS
GO
2. Update the master database to grant permission for XA transactions
for the login account (but first ensure that you have successfully completed the instructions in the
topic Configuring XA transactions).
For example, if sqluser is the database user name,
use the following command syntax to update the master database (where
login\_account is the same login account that you used in the previous
step):USE MASTER
GO
CREATE USER sqluser FOR LOGIN login\_account WITH DEFAULT\_SCHEMA=sqluser
GO
EXEC sp\_addrolemember N'SqlJDBCXAUser', N'sqluser';
GO
3. For each database that you create, you must set the default schema
for the SQL Server login (except for the Content database (CPEDB), where you already set the schema
in Creating SQL Server databases).
For example, if BPMDB
is the database name, and sqluser is the database user name, use the following
command syntax (where login\_account is the same login account that you used in
the previous
step):USE BPMDB
GO
CREATE USER sqluser FOR LOGIN login\_account WITH DEFAULT\_SCHEMA=sqluser
GO
CREATE SCHEMA sqluser AUTHORIZATION sqluser
GO
EXEC sp\_addrolemember 'db\_ddladmin', 'sqluser';
EXEC sp\_addrolemember 'db\_datareader', 'sqluser';
EXEC sp\_addrolemember 'db\_datawriter', 'sqluser';
EXEC sp\_addrolemember 'db\_securityadmin', 'sqluser';
EXEC sp\_addsrvrolemember 'login\_account', 'bulkadmin';
GO

## What to do next

When you create database schemas
using the generated scripts, your user ID must have the authority
to create tables. When the tables are created, you must have the authority
to select, insert, update, and delete information in the tables. For
information about the database privileges that are needed to access
the data stores, see the topic SQL Server database privileges.