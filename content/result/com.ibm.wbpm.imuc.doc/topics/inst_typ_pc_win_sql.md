# Installing and configuring Workflow Center with an SQL Server
database server

## Before you begin

```
install\_root\sqljdbc
```

To install IBM Business Automation
Workflow using the
typical installation option, you must confirm that the Process database, Performance Data Warehouse
database, Common database, and Content database exist and are empty.

- The user name and password for database authentication
- The database server host name and port
- The name of the Common database
- The name of the Process database
- The name of the Performance Data Warehouse database
- The name of the cell-only configuration database (for IBM Business Automation Workflow
Enterprise)
- The name of the Content database

## About this task

From the product launchpad, the typical installation process installs the
software, configures the deployment manager and managed-node profiles, and configures a
single-cluster deployment environment that consists of one node and one server. It also installs IBM WebSphere SDK Java Technology Edition 8 (Java 8).

Only one IBM Installation Manager is required to install multiple instances
of IBM Business Automation Workflow.

## Procedure

1 Optional: If you are connected to the Internet, the typicalinstallation process automatically upgrades your product to the latest refresh pack and interim fixlevel. If you want these upgrades to be installed from a local directory instead, or if you want tospecify the fix level, you can modify a properties file to direct Installation Manager to theupgrades to install. Create the following file: where Note: Ensure that you have read/write access to the folders that are specifiedin the bpm\_updates.properties file. The file uses three prefixes: ifix , fixpack , andlaunchpad . Each prefix must be followed by a period. The name after the prefix andthe period can be anything you want, which enables you to point to multiple locations for interimfixes, fixpacks, and launchpad upgrades. The locations can be either local directories or URLs. Thefollowing code is an example of the prefixes and names in the propertiesfile:ifix.1=C:/bpmUpdatesfixpack.2=http://test/replaunchpad.1=C:/launchpad\_updatesfixpack.WAS\_REP=C:/WAS\_updatesfixpack.BPM\_REP=C:/BPM\_updates
    - C:/HOMEPATH/bpm\_updates.properties
    - The HOMEPATH environment variable points to
C:/Users/user\_name

```
ifix.1=C:/bpmUpdates
fixpack.2=http://test/rep
launchpad.1=C:/launchpad\_updates
fixpack.WAS\_REP=C:/WAS\_updates
fixpack.BPM\_REP=C:/BPM\_updates
```

2 Run Launchpad64.exe , which is in the rootdirectory of the extracted files. You can run only one launchpad at a time.

- If you are using SQL Server authentication, right-click Launchpad64.exe and
select Run as administrator.
- If you are using Windows authentication, make sure that you copy
sqljdbc\_auth.dll to your install\_root\java\bin directory,
for example, C:\IBM\Workflow\v18.0\java\bin. Then double-click
Launchpad64.exe to run it.
3. Optional: 
If you are prompted to update the launchpad, click Update. The updates
are installed and your launchpad is restarted automatically.
If you do not have access to the Internet and want the updates to be installed from a local
directory, you can modify a properties file with the appropriate launchpad prefix as described in
step 1 to direct Installation Manager to the updates to install.
4. On the Welcome page, click Typical
installation.
5. Select Install Workflow Center and click Next.
6. Click Next.
7 Optional: Change the location information:

- Host name: This field shows the name of your machine. Important: If a value of localhost or 127.0.0.1 is used for the host name, Workflow Server installations on a remote system will not be able
to connect to Workflow Center.To use an external
Content Platform Engine, the hostname property value must have a
domain name suffix, for example
MyDmgrHost.my\_domain.com.
- Location : Enter the installation location for Workflow Center , or click Browse to selectthe location.Notes:
    - The installation location must either be an empty directory or a directory that does not exist
and is created during installation.
    - The installation location cannot contain National Language Strings
(NLS).
8. Specify the User name and Password for the cell
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
9. Specify the User name and
Password for the deployment environment administrative
account. The deployment environment administrator is the primary IBM Business Automation
Workflow administrator. A user who is assigned to this
role has administrative access to Process Center and Process Admin Console. Having this role
provides access to all interfaces, enabling users to alter or delete all types of available library
items and assets, including process applications and toolkits. The user in this role also
administers Workflow Servers, Performance Data Warehouses,
and internal users and groups.
10. Click Next.
11. Select Yes to use an existing
database.
12. Specify the required database information.

Table 1. Required database configuration fields for SQL Server

Field
Action needed

User name

Required only if you are not using Windows authentication.
Enter the user name to authenticate with the database. Restriction: User names must
not contain National Language Strings (NLS).

Password

Required only if you are not using Windows authentication.
Enter a password to authenticate with the database.

Select the Apply Windows authentication
option to indicate that you will connect to your databases using your Windows authentication
information. If you select this option, the previous fields become inactive.

Host name
Accept the default value of localhost or enter the
correct database server host name, for example, the IP address.

Port
Accept the default value of 1433 or enter the correct
server port number.

Common database name
Accept the default value of CMNDB, or enter the name for the Common
database.

Process database name
Accept the default value of BPMDB, or enter the Process database name.

Performance Data Warehouse database name
Accept the default value of PDWDB, or enter the Performance Data Warehouse
database name.

Cell-only configuration database
Accept the default value of CMNDB, or enter the name for the cell-scoped
Common database. This database is applicable only when there is an Advanced
deployment environment or AdvancedOnly
deployment environment.

Content database
Accept the default value of CPEDB, or enter the name for the Content
database.

For SQL Server databases, Test Database Connection always succeeds, even
if the connections to the databases are not successful. Click Next to
proceed.
13. Specify the JDBC driver path where the Java Database Connectivity (JDBC)
drivers for your database are installed.
14. Click Next to continue. 

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
15. On the Installation summary page, verify that the
installation options and read the license agreements. If you agree to the terms of the license
agreements, click  I have read and accepted the license agreement and
notices.
16. Click Install Software.

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