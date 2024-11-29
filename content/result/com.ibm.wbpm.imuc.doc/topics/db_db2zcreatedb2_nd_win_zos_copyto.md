# Creating DB2 for z/OS database objects using the
createDatabase.sh script

You can run the createDatabase.sh script
to create the product databases in the DB2® for z/OS® subsystem (if required) and
to also populate each database with objects. Depending on your organization
or site standards, your DB2 for z/OS system administrator might
have already created the databases.

You can also use tools such as the DB2 command line processor, SPUFI,
or DSNTEP2 to configure your databases.

## Before you begin

- Create the database scripts
for the IBM® Business Automation Workflow components
by using either the BPMConfig command utility or
the Deployment Environment wizard.
- Use FTP to transfer the database scripts,
including the createDatabase.sh script, to the z/OS system that contains the DB2 for z/OS installation. Transfer the createDatabase.sh script
as an ASCII text file, and transfer the database schema files in binary
mode. Also ensure that you retain the directory structure when you
transfer the files.
- Create the required buffer pools. For
more information, see Sample DB2 for z/OS commands for allocating buffer pools.
- Configure the DB2 command line processor.

## About this task

When you generated
the database scripts, the files for configuring each of the databases
were generated into separate subdirectories for ease of execution.
The createDatabase.sh script was additionally generated
in these subdirectories. You can run the createDatabase.sh script
once from each subdirectory, for each instance of a database to be
created or configured.

## Procedure

Use one of the following
methods to create and populate the databases, as appropriate for your
environment and standards:

- A user with SYSADM authoritycreates the databases and storage groups, and grants DBADM authorityto a WebSphere® user thatis identified as the owner of the databases. The WebSphere user with DBADM authority thenruns the createDatabase.sh script to populate thedatabases.
    1 DB2system administrator (SYSADM) Create the physical databasesas follows: Tip: The createDatabase.sql files,which are in the subdirectories where the database scripts were generated,contain the relevant CREATE and GRANT statements. Thedefault locations of the database scripts are: You can copy the createDatabase.sql filesfrom the z/OS location to whichthey were transferred, and then run the SQL on the database server;for example:db2 -tvf createDatabase.sql
        1. Create
the cell-scoped database and storage group, and grant the WebSphere administrator DBADM
access to the database.
        2. Create the cluster-scoped
databases and storage groups, and grant the WebSphere administrator DBADM access to
the databases.
        - DMGR\_PROFILE\dbscripts\cell\_name\DB2zOS\cell\_database\_name
        - DMGR\_PROFILE\dbscripts\de\_name\DB2zOS\cluster\_database\_name

You can copy the createDatabase.sql files
from the z/OS location to which
they were transferred, and then run the SQL on the database server;
for example:
db2 -tvf createDatabase.sql

2 WebSphereadministrator (DBADM) Populate each database with objectsas follows:
    1. In the z/OS system that contains the DB2 installation, access the UNIX System Services command shell and then
change to the directory to which you transferred the database scripts. For example, for the cell-level scripts: cd /u/work/dbscripts/Cell1/DB2zOS/S4CELLDB
    2. Check whether the createDatabase.sh script
is in EBCDIC format. If it is not, use the iconv command
to convert the script to  EBCDIC. For example: iconv
-t IBM-1047 -f ISO8859-1 createDatabase.sh > createDatabase\_EBCDIC.sh
Also
grant execute permissions to the createDatabase.sh script.
    3. Run the createDatabase.sh script (or the
											createDatabase\_EBCDIC.sh script if
										you converted it) by using the following
												syntax:createDatabase.sh -DBAlias
												alias\_name
											-RunSQL
where:
-DBAlias
Specifies an alias name that maps to the DB2 server URL, user ID, and password, and which
is used to connect to DB2. If
you do not specify this parameter when you run the createDatabase.sh script,
you are prompted for a value.
-RunSQL
Runs the SQL statements that create the database objects.

Examples:createDatabase.sh -DBAlias LOCDB11 -DBCreate -DBName DCLLDB -DBSto DCLLST -DBUser TUSER01 -DBVCat DB11 -RunSQL 
createDatabase\_EBCDIC.sh -DBAlias DSNXWBD
												-RunSQL
For further information about the
												createDatabase.sh script
											parameters and example usage, see createDatabase.sh script.
    4. Review the messages that are displayed in the console, checking
that no error messages are displayed.When the script has finished
running, you can also review the z\_output.txt file,
which provides an audit trail of the operations completed and status
messages. This file is saved to the directory from which you ran the createDatabase.sh script.
3. DB2 system administrator
(SYSADM)  Grant access to views to the WebSphere administrator that has DBADM
authority.  You can use individual GRANT statements or a Resource Access Control Facility (RACF®) group to provide the required access. For more information, see Db2 for z/OS authorization prerequisites.
- A user with SYSADM authorityruns the createDatabase.sh script to create thedatabases and storage groups, and populate the databases. Completethe following steps for each database:

1. In the z/OS system that contains the DB2 installation, access the UNIX System Services command shell and then
change to the directory to which you transferred the database scripts. For example, for the cell-level scripts:
cd /u/work/dbscripts/Cell1/DB2zOS/S4CELLDB
2. Check whether the createDatabase.sh script
is in EBCDIC format. If it is not, use the iconv command
to convert the script to  EBCDIC. For example: iconv
-t IBM-1047 -f ISO8859-1 createDatabase.sh > createDatabase\_EBCDIC.sh
Also
grant execute permissions to the createDatabase.sh script.
3. Run the createDatabase.sh script
by using the following syntax: createDatabase.sh
-DBAlias alias\_name -DBCreate -RunSQL
where:
-DBAlias
Specifies an alias name that maps to the DB2 server URL, user ID, and password, and which
is used to connect to DB2. If
you do not specify this parameter when you run the createDatabase.sh script,
you are prompted for a value.
-DBCreate
Creates the database.
-RunSQL
Runs the SQL statements that create the database objects.

For example:
createDatabase.sh
-DBAlias DSNXWBD -DBCreate -RunSQL
For further information
about the createDatabase.sh script parameters and
example usage, see createDatabase.sh script.
4. Review the messages that
are displayed in the console, checking that no error messages are
displayed. Tip: The first
time that you run createDatabase.sh to create the
database, you see a few messages because the script first attempts
to drop the database, which at that stage does not yet exist. These
messages can be ignored.When the script has finished running, you
can also review the z\_output.txt file, which
provides an audit trail of the operations completed and status messages.
This file is saved to the directory from which you ran the createDatabase.sh script.
5. Grant access to views to the WebSphere administrator that
has DBADM authority. You can use individual GRANT statements or a Resource Access Control Facility (RACF) group to provide the required access. For more information, see Db2 for z/OS authorization prerequisites.

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