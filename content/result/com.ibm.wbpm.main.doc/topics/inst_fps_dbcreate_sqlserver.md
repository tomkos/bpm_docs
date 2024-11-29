# Creating the Process Federation Server database
for Microsoft SQL Server

## Before you begin

- Ensure that SQL Server was installed with mixed mode (Windows
Authentication or SQL Server Authentication) as the authentication
mode.
- Ensure that XA transactions are configured for SQL Server. Important: SQL Server is
not pre-configured for XA transactions. XA support is delivered as part of the Microsoft JDBC driver
distribution but not enabled by default. To enable XA support, you must change the configuration in
the Microsoft Windows Distributed Transaction Coordinator (MS DTC) service.

## About this task

- createDatabase\_PFS.sql
- createTable\_PFS.sql

## Procedure

1. Replace the variables in the script files with the values
for your federated environment: 
@DB\_NAME@
The name of the Process Federation Server database,
for example, PFSDB.
@SCHEMA@
The name of the Process Federation Server schema,
for example, PFSDB.
@DB\_USER@
The user name that you want to use to create the database. During
database creation, this user is granted db\_owner privileges. To secure
the database, you can remove the db\_owner privileges in the createDatabase\_PFS.sql script
and enable them in the createTables\_PFS.sql script.
The database scripts contain more information about these changes.
@DB\_PASSWORD@
The password for the database user. You can create the database
user and password before you create the database, or you can edit
the script to create them for you. If the script is to create the
user and password, replace this variable with the password.
2 From a DB2 command prompt, run the scripts to create thedatabase, table spaces, and tables. The following variablesare used in the script calls:dbadmin The SQL Server user with administrative authority. The SQL Server database is created.
    1. Create the database. sqlcmd -U dbadmin -P password -e -i createDatabase\_PFS.sqlYou
can manage the locale settings for the database by using the COLLATE option
with the create database script: COLLATE SQL\_Latin1\_General\_CP1\_CS\_AS.
For example, to change the locale settings to French, include COLLATE
French\_100\_CS\_AS with the script call. To change the default
language, add the DEFAULT\_LANGUAGE option to the createDatabase\_PFS.sql file.
For example, to change the default language to French, set the option
to DEFAULT\_LANGUAGE=French.
    2. Create the tables. sqlcmd -U dbadmin -P password -e -i createTable\_PFS.sql

## What to do next

Create a process federation server. See Creating a process federation server.