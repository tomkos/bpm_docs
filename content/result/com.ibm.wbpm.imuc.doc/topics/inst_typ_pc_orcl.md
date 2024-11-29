# Installing and configuring Workflow Center with an Oracle database
server

## Before you begin

```
install\_root/ojdbc
```

To install IBM Business Automation
Workflow using the
typical installation option, you must confirm that the Process database, Performance Data Warehouse
database, Common database, and Content database exist and are empty.

- The user name and password for database authentication
- The database server host name and port
- The user name and password for the Common database
- The user name and password for the Process database
- The user name and password of the Performance Data Warehouse database
- The user name and password of the cell-only configuration database (for IBM Business Automation Workflow
Enterprise)
- The user name and password for the three Content database schemas: design object store, target
object store, and IBM Content
Navigator

To extract files on AIX, use the GNU tar program instead of the AIX tar program. The AIX tar
program might truncate long file names, which can cause installation errors. To install the GNU tar
program, see Use GNU tar to extract server installation images on AIX.

- For Linux systems, extract the installation files to a directory that does not contain spaces or
special characters. The launchpad cannot be started from a directory path that contains spaces or
special characters.
- Linux on Power LE does not support typical installation.

## About this task

From the product launchpad, the typical installation process installs the
software, configures the deployment manager and managed-node profiles, and configures a
single-cluster deployment environment that consists of one node and one server. It also installs IBM WebSphere SDK Java Technology Edition 8 (Java 8).

Only one IBM Installation Manager is required to install multiple instances
of IBM Business Automation Workflow.

## Procedure

1 Optional: If you are connected to the Internet, the typical installation process automatically upgradesyour product to the latest fix pack or refresh pack level and recommended interim fixes. If you wantthese upgrades to be installed from a local directory instead, or if you want to specify the fixlevel, you can modify a properties file to direct Installation Manager to the upgrades toinstall. Create the following file: Note: Ensure that you have read/write access to the folders that are specifiedin the bpm\_updates.properties file. The file uses three prefixes: ifix , fixpack , andlaunchpad . Each prefix must be followed by a period. The name after the prefix andthe period can be anything you want, which enables you to point to multiple locations for interimfixes, fix packs, and launchpad upgrades. The locations can be either local directories or URLs. Thefollowing code is an example of the prefixes and names in the propertiesfile:ifix.1=/bpmUpdatesfixpack.2=http://test/replaunchpad.1=/launchpad\_updatesfixpack.WAS\_REP=/WAS\_updatesfixpack.BPM\_REP=/BPM\_updates
    - /user\_home\_directory/bpm\_updates.properties

```
ifix.1=/bpmUpdates
fixpack.2=http://test/rep
launchpad.1=/launchpad\_updates
fixpack.WAS\_REP=/WAS\_updates
fixpack.BPM\_REP=/BPM\_updates
```

2. Run launchpad.sh, which is in the root directory of
the extracted files.  You can run only one launchpad at a time.
3. Optional: 
If you are prompted to update the launchpad, click Update. The updates
are installed and your launchpad is restarted automatically.
If you do not have access to the Internet and want the updates to be installed from a local
directory, you can modify a properties file with the appropriate launchpad prefix as described in
step 1 to direct Installation Manager to the updates to install.
4. On the Welcome page, click Typical
installation.
5. Select Install Workflow Center and click Next.
6 Optional: Change the location information:

- Host name: This field shows the name of your machine.Important: If a value of localhost or 127.0.0.1 is used for the host name, Workflow Server installations on a remote system will not be able
to connect to Workflow Center. To use an external
Content Platform Engine, the hostname property value must have a
domain name suffix, for example
MyDmgrHost.my\_domain.com.
- Location : Enter the installation location for Workflow Center , or click Browse to selectthe location.Notes:
    - The installation location must either be an empty directory or a directory that does not exist
and is created during installation.
    - The installation location cannot contain National Language Strings
(NLS).
7. Specify the User name and Password for the cell
administrative account.
The cell administrator is the primary WebSphere® Application
Server
administrator. A user who is assigned to this role can assign other administrator roles, and is
responsible for the administration of the cell and topology. A user who is assigned to this role is
not responsible for the administration of the IBM Business Automation
Workflow components. This role provides access to all
interfaces, enabling users to alter or delete all types of available library items and assets,
including process applications and toolkits. The user in this role also administers process servers,
Performance Data Warehouses, and internal users and groups. You must be a user assigned to this role
to deploy process applications on the Workflow Center
server.
8. Specify the User name and
Password for the deployment environment administrative
account. The deployment environment administrator is the primary IBM Business Automation
Workflow administrator. A user who is assigned to this
role has administrative access to Process Center and Process Admin Console. Having this role
provides access to all interfaces, enabling users to alter or delete all types of available library
items and assets, including process applications and toolkits. The user in this role also
administers Workflow Servers, Performance Data Warehouses,
and internal users and groups.
9. Click Next.
10. Select Yes to use an existing
database.
11 Specify the required database information. Table 1. Required database configuration fields for Oracle Field Action needed Service name Enter the service name of the Oracle database. Host name Accept the default value of localhost or enter thecorrect database server host name, for example, the IP address. Port Accept the default value of 1521 or enter the correctserver port number. Common database For the deployment environment-level Common database, enter values for theuser name and password parameters. Process database For the Process database, enter values for the user name and passwordparameters. Performance Data Warehouse database For the Performance Data Warehouse database, enter values for the user nameand password parameters. Cell-only configuration database For the cell-scoped Common database, enter values for the user name andpassword parameters. This database is applicable only when there is an Advanced deployment environment or AdvancedOnly deployment environment . Content database For the Content database, enter values for the user name and passwordparameters for the following schemas: Each user is distinct and they are different from the other database users.

| Field                               | Action needed                                                                                                                                                                                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Service name                        | Enter the service name of the Oracle database.                                                                                                                                                                                                                           |
| Host name                           | Accept the default value of localhost or enter the correct database server host name, for example, the IP address.                                                                                                                                                       |
| Port                                | Accept the default value of 1521 or enter the correct server port number.                                                                                                                                                                                                |
| Common database                     | For the deployment environment-level Common database, enter values for the user name and password parameters.                                                                                                                                                            |
| Process database                    | For the Process database, enter values for the user name and password parameters.                                                                                                                                                                                        |
| Performance Data Warehouse database | For the Performance Data Warehouse database, enter values for the user name and password parameters.                                                                                                                                                                     |
| Cell-only configuration database    | For the cell-scoped Common database, enter values for the user name and password parameters. This database is applicable only when there is an Advanced deployment environment or AdvancedOnly deployment environment.                                                   |
| Content database                    | For the Content database, enter values for the user name and password parameters for the following schemas: Design object store (DOS) Target object store (TOS) IBM Content Navigator (ICN)  Each user is distinct and they are different from the other database users. |

12. Specify the JDBC driver path where the Java Database Connectivity (JDBC)
drivers for your database are installed.
13. Click Next to continue. 

Note: If you are using a local properties file, you do not need to provide your IBMid and
password.
A connection to the service repositories is required to download and install fix packs and
required interim fixes from the Internet, including fixes for WebSphere Application
Server and IBM Business Automation Workflow. You can obtain an IBMid and password by
registering at http://www.ibm.com.
To continue installing without downloading the required fixes, click
Cancel or clear the Use your support account to include updates
with the installation option on the Installation summary page.
After successfully installing the product, you can use Installation Manager to install the
required fixes.
14. On the Installation summary page, verify that the
installation options and read the license agreements. If you agree to the terms of the license
agreements, click  I have read and accepted the license agreement and
notices.
15. Click Install Software.

## Results

After a successful installation, the Quick Start console starts
automatically.

## What to do next

To learn about security for the environment and applications, see Creating a secure environment.

After the server is started, if you want to use the case management features,
see the topic Configuring your system for case management.

## Related reference

- Warnings about GTK or ulimit on Linux or UNIX when installing or migrating

## Related information

- Messages and known issues during installation and profile creation
- Installation and profile creation log files
- Preparing to install and configure IBM Business Automation Workflow