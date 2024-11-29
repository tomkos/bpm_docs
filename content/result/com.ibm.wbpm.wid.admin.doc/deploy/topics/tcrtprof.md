<!-- image -->

# Creating or resetting default server profiles

## Before you begin

The default server profiles require an IBM Db2® database server, which
you can choose to install when you install IBM Integration
Designer.

Before starting Integration Designer to create or reset a
default server profile, make sure that you have permission to create and drop databases. The
database user who is prompted for in the procedures is usually able to drop and create database.
However, the program uses the login user's authority and that is a common fail point. In this case,
see IBM
Integration Designer example Unit Test Environment install.

Make sure that the local Db2 database server is set
up correctly on your system and is started. (You can use the Db2 Control Center to
check.) Make sure that you know the port number on which the database server is listening.

All
the profiles that you create and reset using the instructions below
will use the same local database server (instance). Make sure that
the IBM Integration
Designer environment
is set up to use the same database server.

- From the command line, run db2cmd /w /c /i db2 start database manager

DB20000I The START DATABASE MANAGER command completed successfully.

SQL1026N The database manager is already active.

If that does not work, ensure that the Db2 environment is set up
and the Db2
executable files are in your environment %PATH%.

## Procedure

To create or reset default server profiles:

1. Close any command windows or Windows Explorer browsers that are open in
the folder where the profile is installed. Otherwise, when the profile
is deleted, the removal of the directory will fail and the test environment
will not be reset.
2. In the Business Integration perspective, click the Servers tab to
open the Servers view.
3. If you want to reset a default server profile (which will delete the server profile and
then create it again), stop the server instance that references the profile. For example, if you
want to reset the IBM Workflow
Server server profile,
stop the IBM Workflow
Server server
instance.
4. Click Manage Server Profiles . (Alternatively, you
can right-click any server and select Manage Server Profiles.)
The Manage Server Profiles window opens.The window
displays the logical names of the default server profiles, which are
the names that you see when you install the Monitor test environment.
The window also displays the physical names of the default server
profiles, which are the actual names that are used in a server configuration.
(You can open a server configuration in the server configuration editor
by double-clicking a server instance in the Servers view.) For example, IBM Workflow
Server is
a logical name and qbpmaps is a physical
name. The server instances listed in the Servers that will
be deleted and Servers that will be created
or recreated list boxes refer to the physical names of
the default server profiles.
5. Select the check box beside each action that you want to
initiate for the listed servers. For each action that you select,
the Servers that will be deleted list displays
the names of any server instances that will be deleted from the Servers
view. Similarly, the Servers that will be created list
displays the names of any server instances that will be created or
reset in the Servers view.
6. Click OK to begin creating or resetting
the selected server profiles.
7. If the Administrator Credentials wizard opens, specify
a user ID and password for each profile name that is listed, then
click Next.
8. On the Add the Database Credentials page, you can see a list of the local databases (if
they exist) that will be dropped if you reset the profile or profiles you chose. Any data in those
databases will be lost. Make sure that the Db2 database instance is up
and running, that the credentials are correct, and that the port number is correct (the default is
50000 but it might be different on your system).
9. Click Finish.

## Results