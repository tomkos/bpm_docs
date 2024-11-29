# Creating DB2 for z/OS database objects using SPUFI
or DSNTEP2

## Before you begin

- Create the database scripts
for the IBM® Business Automation Workflow components
by using either the BPMConfig command utility or
the Deployment Environment wizard.
- Use FTP to transfer the database
scripts to the z/OS system
that contains the DB2 for z/OS installation. Transfer the createDatabase.sh script
as an ASCII text file, and transfer the database schema files in binary
mode. Also ensure that you retain the directory structure when you
transfer the files.
- Create the required buffer pools. For
more information, see Sample DB2 for z/OS commands for allocating buffer pools.
- Create the databases and assign the
relevant permissions.

## About this task

- DMGR\_PROFILE/dbscripts/cell\_name/DB2zOS/cell\_database\_name:
Contains the files that can be used to create the cell-scoped database.
- DMGR\_PROFILE/dbscripts/cell\_name.deployment\_environment\_name/DB2zOS/cluster\_database\_name:
Contains the files that can be used to create each of the cluster-scoped
databases.

## Procedure

1 On the z/OS systemthat contains the DB2 for z/OS installation, go to the locationto which you transferred the database scripts: These files are in ASCII format.
    - The cell\_database\_name subdirectory
contains a createSchema\_Advanced.sql or createSchema\_AdvancedOnly.sql file,
which you must run.
    - Each cluster\_database\_name subdirectorycontains one or more of these files, which you must run in the followingorder:
        1. createTablespace\_Advanced.sql or createTablespace\_AdvancedOnly.sql
        2. createSchema\_Advanced.sql or createSchema\_AdvancedOnly.sql
        3. createSchema\_Messaging.sql
        4. createProcedure\_Advanced.sql (generated only for an
Advanced
deployment environment)
2. Assign the appropriate read permissions to the SQL files;
for example: chmod 644 createSchema\_Advanced.sql
3. If the tool that you want to use to view and run the SQL
files requires the files to be in EBCDIC format, rather than ASCII
format, use the iconv command to convert the files
to EBCDIC.  For example:iconv -t IBM-1047
-f ISO8859-1 createSchema\_Advanced.sql >  createSchema\_Advanced\_EBCDIC.sql 
Important: After converting from ASCII to EBCDIC, check that
no SQL statements exceed 71 characters in length. Longer lines will
lead to line truncation and invalid statements when copying to fixed-width MVS data sets.
Tip: If you have converted the files from ASCII format to EBCDIC,
but need to run the files in ASCII format, you can also use iconv to
convert the files back to ASCII. For example:iconv -t
ISO8859-1 -f IBM-1047 createSchema\_Advanced\_EBCDIC.sql > createSchema\_Advanced.sql
4. To create database objects outside of the z/OS UNIX environment
by using SPUFI or DSNTEP2, copy the SQL files from z/OS UNIX to
a partitioned data set.
5. Run the SQL files by using the tool of your choice.
6. Verify that the database tables are created successfully
with no errors by inspecting the output.

## What to do next

If you created a Standard
deployment environment or an Advanced
deployment environment,
you must now run the bootstrap utility to load configuration data for the IBM Business Automation Workflow applications into the Process
database. This data is required for the applications to run correctly.

## Related information

- Creating Db2 for z/OS database objects using the Db2 command line processor: for Windows
- Creating the Advanced Workflow Center deployment environment for Db2 for z/OS
- Creating the Standard Workflow Center deployment environment for Db2 for z/OS
- Creating the Advanced Workflow Server deployment environment for Db2 for z/OS
- Creating the Standard Workflow Server deployment environment for Db2 for z/OS
- Creating the AdvancedOnly Workflow Server deployment environment for Db2 for z/OS
- Loading the database with system information in a network deployment environment on Windows