# Preparing necessary security authorizations

## Before you begin

- Complete the design of your database.
- Determine the authentication system to use, for example, Lightweight
Directory Access Protocol (LDAP).
- Determine what controls are in place that affect the authorizations
required for your IBM® Business Automation Workflow installation.
- Identify the systems on which you are installing the product.

## About this task

## Procedure

To prepare security authorizations for an IBM Business
Process Manager database, complete the following steps:

- Prepare a list of user IDs and passwords that have authority
to install software on the systems. You must run the installation
wizards for IBM Business Automation Workflow user
IDs that have the authority to create files and folders.
- If you are installing in group mode, set up the installation user group
and add the appropriate users. Create the Installation Manager installation folder and
change the ownership to the installation group. Change the access rights for the group on the folder
to ensure they have read, write, and execute authority. Then install Installation Manager in group mode.
For more information, see the Installation Manager documentation topic Installing as an administrator, nonadministrator, or group.
- Prepare a list of user IDs, passwords, and roles that areneeded for daily operations of the system:
    - Administrative console user IDs and roles to limit capabilities.
You can have user IDs for configuring, administering, or monitoring
roles.
    - User IDs for each system bus to authenticate system communications.
    - Administrative and monitoring user IDs or
groups for each Business Process Choreographer container for authentication
with Business Flow Manager and Human Task Manager.
    - User IDs or groups for synchronous calls to
authenticate with Business Flow Manager and Human Task Manager.
- Prepare a list of user IDs and passwords that the system
uses to access the database tables that it uses during operation.
- Optional: Prepare a list of user IDs and passwords
that the system uses to create databases or database tables during
installation. Your site policies might restrict this authority to
the database administrator. In this case, you must provide generated
scripts to the administrator to create the databases or database tables.

## Results

## Related concepts

- Process and process application considerations
- Resource considerations
- Development and deployment version levels
- Naming considerations for profiles, nodes, servers, hosts, and cells

## Related reference

- Installation directories for the product and profiles