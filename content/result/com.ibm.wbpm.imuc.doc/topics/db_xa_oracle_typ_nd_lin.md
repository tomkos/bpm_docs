# Configuring XA transactions for Oracle

You must configure XA transactions after the Oracle database is
installed and before you start the server.

## Before you begin

The
instructions in this topic must be performed after the Oracle
database is installed and before you start the server.

## About this task

XA is a two-phase commit protocol defined by
the X/Open DTP group.

The following
steps must be performed by a database user with SYS authority.

## Procedure

1. As the SYS user, enable the Oracle database for XA by switching
to the Oracle user and then configuring the database by running the following script on the BPMDB
database:

ORACLE\_HOME/javavm/install/initxa.sqlFor example:
su - oracle
sqlplus oracle\_user\_ID/oracle\_password@oracle\_instance\_name @initxa.sql 
Note: XA transactions might be configured by default, or you might have to enable this
configuration. For more information, see Developing Applications with Oracle XA.
2. Create the users and grant them access as described in the topic
Creating users for Oracle databases in a network deployment environment on AIX or Linux.