# Creating DB2 for z/OS database objects using the DB2 command line processor

You can use the DB2® command
line processor to run the database scripts to create and populate
the product databases.

You
can also run the database scripts by using any other database tool
of your choice, such as SPUFI or DSNTEP2.

## Before you begin

- Create the database scripts
for the IBM® Business Automation Workflow components
by using either the BPMConfig command utility or
the Deployment Environment wizard.
- Use FTP to transfer the database scripts,
including the createDatabase.sh script, to the z/OS® system that contains the DB2 for z/OS installation. Transfer the createDatabase.sh script
as an ASCII text file, and transfer the database schema files in binary
mode. Also ensure that you retain the directory structure when you
transfer the files.
- Create the required buffer pools. For
more information, see Sample DB2 for z/OS commands for allocating buffer pools.
- Configure the DB2 command line processor.

## About this task

When you generated the database scripts,
the files for configuring each of the databases were generated into
separate subdirectories for ease of execution.

## Procedure

Complete the following steps to create
the databases and database objects:

1 DB2 system administrator(SYSADM) Create the physical databases and storagegroups, and grant DBADM authority to a WebSphere® user that is identified as theowner of the databases: Tip: The createDatabase.sql files,which are in the subdirectories where the database scripts were generated,contain the relevant CREATE and GRANT statements. The defaultlocations of the database scripts are: You can copy the createDatabase.sql filesfrom the z/OS location to whichthey were transferred, and then run the SQL on the database server;for example:db2 -tvf createDatabase.sql
    1. Create the cell-scoped
database and storage group, and grant the WebSphere administrator DBADM access to
the database.
    2. Create the cluster-scoped databases
and storage groups, and grant the WebSphere administrator
DBADM access to the databases.
    - DMGR\_PROFILE/dbscripts/cell\_name/DB2zOS/cell\_database\_name
    - DMGR\_PROFILE/dbscripts/cell\_name.deployment\_environment\_name/DB2zOS/cluster\_database\_name

You can copy the createDatabase.sql files
from the z/OS location to which
they were transferred, and then run the SQL on the database server;
for example:
db2 -tvf createDatabase.sql

2 WebSphere administrator(DBADM) Populate each database with objects as follows:

1. To create the
database objects for the cell-scoped database, use the DB2 command line processor to run the createSchema\_Advanced.sql or createSchema\_AdvancedOnly.sql file
 that was transferred from the DMGR\_PROFILE/dbscripts/cell\_name/DB2zOS/cell\_database\_name subdirectory
on the IBM Business Automation Workflow system.
For example:db2 connect to cell\_database\_name USER user\_name USING password
db2 -tvf zos\_directory\_path/createSchema\_Advanced.sql
db2 connect reset
2 To create the database objects for thedeployment environment-scoped databases, use the DB2 command line processor to run the followingSQL files, which were transferred from the DMGR\_PROFILE/dbscripts/cell\_name.deployment\_environment\_name /DB2zOS/cluster\_database\_name subdirectorieson the IBM Business Automation Workflow system.Each cluster\_database\_name subdirectorycontains one or more of these files, which you must run in the followingorder: Note: In the createProcedure\_Advanced.sql file, the at sign(@) is used as a statement termination character, so when you usethe DB2 command line processorto run the SQL commands in this file, use the -td parameterto define @ as the statement termination character.
    1. createTablespace\_Advanced.sql or createTablespace\_AdvancedOnly.sql
    2. createSchema\_Advanced.sql or createSchema\_AdvancedOnly.sql
    3. createSchema\_Messaging.sql
    4. createProcedure\_Advanced.sql (generated only for an
Advanced
deployment environment)
3. DB2 system administrator
(SYSADM)  Grant access to views to the WebSphere administrator that has DBADM
authority.  You can use individual GRANT statements or a Resource Access Control Facility (RACF®) group to provide the required access. For more information, see Db2 for z/OS authorization prerequisites.

## Results

## What to do next

If you created a Standard
deployment environment or an Advanced
deployment environment,
you must now run the bootstrap utility to load configuration data for the IBM Business Automation Workflow applications into the Process
database. This data is required for the applications to run correctly.

## Related information

- Creating the Advanced Workflow Center deployment environment for Db2 for z/OS
- Creating the Standard Workflow Center deployment environment for Db2 for z/OS
- Creating the Advanced Workflow Server deployment environment for Db2 for z/OS
- Creating the Standard Workflow Server deployment environment for Db2 for z/OS
- Creating the AdvancedOnly Workflow Server deployment environment for Db2 for z/OS
- Loading the database with system information in a network deployment environment on Windows