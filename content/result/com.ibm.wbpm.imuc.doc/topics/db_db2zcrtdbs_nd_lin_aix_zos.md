# Creating databases in the DB2 for z/OS subsystem

You
can use the BPMConfig script to
generate the database scripts that are required to create the databases
for the IBM® Business Automation Workflow components.

- The createDatabase.sh script, which was additionally
created with the database scripts
- Tools such as the DB2® command
line processor, SPUFI, or DSNTEP2

## Choosing which tool to use

You can choose one tool over another
based on experience and familiarity, or personal preference. Your
organization might also have implemented standards or conventions
for the tools that are used to create DB2 for z/OS® objects, particularly in a
production environment.

## Considerations for choosing the createDatabase.sh
script

- createDatabase.sh can create
all your database objects in a single execution of the tool, for each
database to be created. Therefore, using this script is a good choice
if this is your first server implementation.
- createDatabase.sh runs the
database scripts that the BPMConfig script
generates.
- createDatabase.sh runs the
SQL for each component in the correct sequence.
- createDatabase.sh creates
database objects according to a naming convention that you define.
- createDatabase.sh organizes
the layout of database objects across DB2 for z/OS databases.
- createDatabase.sh issues
GRANT permissions to database, storage group, and buffer pool objects.
- createDatabase.sh runs in
a UNIX System Services environment.
- createDatabase.sh produces
an audit trail of the objects that it creates.

## Considerations for choosing other tools

- You might prefer to use the DB2 command line processor to run the SQL statements
in the UNIX Systems Services
environment.
- There is no restriction on the naming
or organization conventions that apply to the database objects other
than the standard database subsystem restrictions.
- Some tools can be run from a z/OS environment.
- The tools can produce an audit trail of
the DB2 database commands that
have been issued.

- Configuring the DB2 command line processor

Before you run the createDatabase.sh script  in the z/OS UNIX System Services environment, you must configure the DB2 command line processor by defining a set of environment variables and a db2 command alias. You must also define alias names that can be used to connect to the DB2 for z/OS server.
- Creating DB2 for z/OS database objects using the createDatabase.sh script

You can run the createDatabase.sh script to create the product databases in the DB2 for z/OS subsystem (if required) and to also populate each database with objects. Depending on your organization or site standards, your DB2 for z/OS system administrator might have already created the databases.
- Creating DB2 for z/OS database objects using the DB2 command line processor

You can use the DB2 command line processor to run the database scripts to create and populate the product databases.
- Creating DB2 for z/OS database objects using SPUFI or DSNTEP2

You can use tools such as SPUFI or DSNTEP2 to run the database scripts that are used to create the DB2 for z/OS database objects for your configuration. This task assumes that a DB2 system administrator with SYSADM authority has created the physical databases and storage groups, and granted DBADM authority to a WebSphere® user that is identified as the owner of the databases.